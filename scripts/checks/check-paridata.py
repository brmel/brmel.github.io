#!/usr/bin/env python3
import glob, json, os, re, sys
from datetime import date

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DATA = os.path.join(ROOT, "data", "paridata")
FLAGS = os.path.join(ROOT, "assets", "paridata", "flags")

MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.json$")
MATCH_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
TICKET_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-\d{2}$")
IDENTIFYING = re.compile(r"https?://|www\.|@\w")
MATCH_KEYS = {"date", "competition", "home", "away", "status", "score", "scorers"}
STATUSES = {"scheduled", "played", "postponed"}
TICKET_KEYS = {"id", "posted", "odds", "legs"}
LEG_KEYS = {"match", "pick", "odds"}
PICK = re.compile(r"^(win|win-or-draw|goal):.+$|^draw$")
fails = []


def load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fails.append(f"{os.path.relpath(path, DATA)}: {e}")
        return None


def iso_date(value):
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return None


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def month_files(folder):
    for path in sorted(glob.glob(os.path.join(DATA, folder, "*.json"))):
        name = os.path.basename(path)
        if not MONTH_FILE.match(name):
            fails.append(f"{folder}/{name}: files are named YYYY-MM.json")
            continue
        yield name[:7], load(path)


def anonymous(where, *values):
    for value in values:
        if isinstance(value, str) and IDENTIFYING.search(value):
            fails.append(f"{where}: {value!r} contains a link or handle — the experiment stays anonymous")


profile = load(os.path.join(DATA, "profile.json")) or {}
staking = profile.get("staking", {})
if not number(staking.get("defaultStake")) or staking["defaultStake"] <= 0:
    fails.append("profile.json: staking.defaultStake must be a positive number")
for c in staking.get("currencies") or [None]:
    if not c or not c.get("code") or not c.get("symbol") or not number(c.get("perUnit")) or c.get("decimals") not in (0, 1, 2, 3):
        fails.append("profile.json: every currency needs code, symbol, a positive perUnit and decimals 0 to 3")

competitions = load(os.path.join(DATA, "competitions.json")) or {}
for name, region in competitions.items():
    if not os.path.isfile(os.path.join(FLAGS, f"{region}.svg")):
        fails.append(f"competitions.json: {name!r} maps to {region!r}, which has no flag")

matches = {}
for month, data in month_files("matches"):
    if not isinstance(data, dict):
        fails.append(f"matches/{month}.json: must be an object of matches keyed by id")
        continue
    for mid, m in data.items():
        where = f"match {mid}"
        idm = MATCH_ID.match(mid)
        if not idm:
            fails.append(f"{where}: id must be YYYY-MM-DD-home-away in lowercase")
        elif idm.group(1) != m.get("date"):
            fails.append(f"{where}: id date does not match date {m.get('date')!r}")
        elif not idm.group(1).startswith(month):
            fails.append(f"{where}: lives in matches/{month}.json")
        for key in sorted(set(m) - MATCH_KEYS):
            fails.append(f"{where}: unknown field {key!r}")
        if iso_date(m.get("date")) is None:
            fails.append(f"{where}: date must be YYYY-MM-DD")
        for key in ("competition", "home", "away"):
            if not m.get(key):
                fails.append(f"{where}: needs {key}")
        if m.get("competition") and m["competition"] not in competitions:
            fails.append(f"{where}: competition {m['competition']!r} is missing from competitions.json")
        status = m.get("status")
        if status not in STATUSES:
            fails.append(f"{where}: status must be one of {sorted(STATUSES)}")
        score = m.get("score")
        if status == "played":
            if not isinstance(score, dict) or set(score) != {"home", "away"} or not all(isinstance(v, int) and v >= 0 for v in score.values()):
                fails.append(f"{where}: a played match needs score {{\"home\": n, \"away\": n}}")
        elif "score" in m or "scorers" in m:
            fails.append(f"{where}: only a played match has a score or scorers")
        if "scorers" in m and not (isinstance(m["scorers"], list) and all(isinstance(s, str) and s for s in m["scorers"])):
            fails.append(f"{where}: scorers must be a list of player names")
        anonymous(where, m.get("home"), m.get("away"), *(m.get("scorers") or []))
        matches[mid] = m

seen = set()
for month, data in month_files("tickets"):
    if not isinstance(data, list):
        fails.append(f"tickets/{month}.json: must be a list of tickets")
        continue
    for t in data:
        tid = t.get("id", "<no id>")
        bad = lambda msg: fails.append(f"ticket {tid}: {msg}")
        for key in sorted(set(t) - TICKET_KEYS):
            bad(f"unknown field {key!r}")
        if tid in seen:
            bad("duplicate id")
        seen.add(tid)
        if t.get("odds") is not None and (not number(t["odds"]) or t["odds"] <= 1):
            bad("odds must be a number above 1, or null when unknown")
        legs = t.get("legs")
        if not isinstance(legs, list) or not legs:
            bad("needs at least one leg")
            continue

        first = None
        for i, leg in enumerate(legs, 1):
            for key in sorted(set(leg) - LEG_KEYS):
                bad(f"leg {i} has unknown field {key!r}")
            m = matches.get(leg.get("match"))
            if not m:
                bad(f"leg {i} match {leg.get('match')!r} is not in data/paridata/matches")
                continue
            first = min(first or m["date"], m["date"])
            picks = leg.get("pick")
            if not isinstance(picks, list) or not picks:
                bad(f"leg {i} pick must be a list, e.g. [\"win:{m['home']}\"]")
                continue
            for p in picks:
                if not isinstance(p, str) or not PICK.match(p):
                    bad(f"leg {i} pick {p!r} must be win:Team, win-or-draw:Team, draw or goal:Player")
                    continue
                kind, _, arg = p.partition(":")
                if kind in ("win", "win-or-draw") and arg not in (m["home"], m["away"]):
                    bad(f"leg {i} pick {p!r} names a team not playing in {leg['match']}")
                if kind == "goal" and m.get("status") == "played" and "scorers" not in m:
                    bad(f"leg {i} picks a scorer but {leg['match']} has no scorers list")
                anonymous(f"ticket {tid}", p)
            if m.get("status") == "postponed" and not number(leg.get("odds")):
                bad(f"leg {i} is on a postponed match and needs its odds to take them out of the coupon")

        idm = TICKET_ID.match(str(tid))
        if not idm:
            bad("id must be YYYY-MM-DD-NN, dated by its first match")
        elif first and idm.group(1) != first:
            bad(f"id should be dated {first}, the day of its first match")
        elif not idm.group(1).startswith(month):
            bad(f"lives in tickets/{month}.json")
        if "posted" in t:
            posted = iso_date(t["posted"])
            if posted is None:
                bad("posted must be YYYY-MM-DD")
            elif first and posted > date.fromisoformat(first):
                bad("posted after its first match was played")

print(f"checked {len(matches)} match(es) and {len(seen)} ticket(s)")
if fails:
    print(f"\n❌ {len(fails)} problem(s) in data/paridata:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every ticket points at a real match, picks are well formed, nothing identifies the account")
