#!/usr/bin/env python3
import collections, glob, json, math, os, re
from datetime import date
from gate import CONFIG, ROOT, finish

DATA = os.path.join(ROOT, "data", "paridata")
FLAGS = os.path.join(ROOT, "assets", "paridata", "flags")
MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.json$")
MATCH_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
TICKET_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-\d{2}$")
IDENTIFYING = re.compile(r"https?://|www\.|@\w")
PICK = re.compile(r"^(win|win-or-draw|goal):.+$|^draw$")
MATCH_KEYS = {"date", "competition", "home", "away", "status", "score", "scorers"}
STATUSES = {"scheduled", "played", "postponed"}
TICKET_KEYS = {"id", "posted", "odds", "legs"}
LEG_KEYS = {"match", "pick", "odds"}
fails = []

def load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fails.append(f"{os.path.relpath(path, DATA)}: {e}")
        return None

def iso_date(val):
    try: return date.fromisoformat(str(val))
    except ValueError: return None

def is_odds(v): return isinstance(v, (int, float)) and not isinstance(v, bool) and v > 1

def month_files(folder):
    for path in sorted(glob.glob(os.path.join(DATA, folder, "*.json"))):
        name = os.path.basename(path)
        if MONTH_FILE.match(name): yield name[:7], load(path)
        else: fails.append(f"{folder}/{name}: files are named YYYY-MM.json")

def anonymous(where, *vals):
    for v in vals:
        if isinstance(v, str) and IDENTIFYING.search(v):
            fails.append(f"{where}: {v!r} contains a link or handle — the experiment stays anonymous")

profile = load(os.path.join(DATA, "profile.json")) or {}
staking = profile.get("staking", {})
if not isinstance(staking.get("defaultStake"), (int, float)) or staking["defaultStake"] <= 0:
    fails.append("profile.json: staking.defaultStake must be a positive number")
for c in staking.get("currencies") or [None]:
    if not c or not c.get("code") or not c.get("symbol") or not isinstance(c.get("perUnit"), (int, float)) or c["perUnit"] <= 0 or c.get("decimals") not in (0, 1, 2, 3):
        fails.append("profile.json: every currency needs code, symbol, a positive perUnit and decimals 0 to 3")

regions = load(os.path.join(DATA, "regions.json")) or {}
for key, names in regions.items():
    if not os.path.isfile(os.path.join(FLAGS, f"{key}.svg")):
        fails.append(f"regions.json: {key!r} has no flag at assets/paridata/flags/{key}.svg")
    for lang in CONFIG["languages"]:
        if not (names or {}).get(lang): fails.append(f"regions.json: {key!r} needs a {lang} name")
if "mix" not in regions: fails.append("regions.json: needs 'mix', used when a coupon crosses countries")

competitions = load(os.path.join(DATA, "competitions.json")) or {}
for name, region in competitions.items():
    if region not in regions: fails.append(f"competitions.json: {name!r} maps to {region!r}, which is not in regions.json")

matches = {}
for month, data in month_files("matches"):
    if not isinstance(data, dict):
        fails.append(f"matches/{month}.json: must be an object of matches keyed by id")
        continue
    for mid, m in data.items():
        w = f"match {mid}"
        idm = MATCH_ID.match(mid)
        if not idm: fails.append(f"{w}: id must be YYYY-MM-DD-home-away in lowercase")
        elif idm.group(1) != m.get("date"): fails.append(f"{w}: id date does not match date {m.get('date')!r}")
        elif not idm.group(1).startswith(month): fails.append(f"{w}: lives in matches/{month}.json")
        for k in sorted(set(m) - MATCH_KEYS): fails.append(f"{w}: unknown field {k!r}")
        if iso_date(m.get("date")) is None: fails.append(f"{w}: date must be YYYY-MM-DD")
        for k in ("competition", "home", "away"):
            if not m.get(k): fails.append(f"{w}: needs {k}")
        if m.get("competition") and m["competition"] not in competitions:
            fails.append(f"{w}: competition {m['competition']!r} is missing from competitions.json")
        status = m.get("status")
        if status not in STATUSES: fails.append(f"{w}: status must be one of {sorted(STATUSES)}")
        if status == "played":
            s = m.get("score")
            if not isinstance(s, dict) or set(s) != {"home", "away"} or not all(isinstance(v, int) and v >= 0 for v in s.values()):
                fails.append(f"{w}: a played match needs score {{\"home\": n, \"away\": n}}")
        elif "score" in m or "scorers" in m:
            fails.append(f"{w}: only a played match has a score or scorers")
        if "scorers" in m and not (isinstance(m["scorers"], list) and all(isinstance(s, str) and s for s in m["scorers"])):
            fails.append(f"{w}: scorers must be a list of player names")
        anonymous(w, m.get("home"), m.get("away"), *(m.get("scorers") or []))
        matches[mid] = m

by_team = collections.defaultdict(list)
for mid, m in matches.items():
    day = iso_date(m.get("date"))
    for team in (m.get("home"), m.get("away")):
        if day and team: by_team[team].append((day, mid))
for team, games in by_team.items():
    games.sort()
    for (d1, a), (d2, b) in zip(games, games[1:]):
        if (d2 - d1).days <= 1: fails.append(f"{team} plays {a} and {b} within a day — one of those dates is wrong")

seen = set()
for month, data in month_files("tickets"):
    if not isinstance(data, list):
        fails.append(f"tickets/{month}.json: must be a list of tickets")
        continue
    for t in data:
        tid = t.get("id", "<no id>")
        err = lambda msg: fails.append(f"ticket {tid}: {msg}")
        for k in sorted(set(t) - TICKET_KEYS): err(f"unknown field {k!r}")
        if tid in seen: err("duplicate id")
        seen.add(tid)
        if "odds" in t and not is_odds(t["odds"]): err("odds must be a number above 1")
        legs = t.get("legs")
        if not isinstance(legs, list) or not legs:
            err("needs at least one leg")
            continue

        idm = TICKET_ID.match(str(tid))
        c_day = iso_date(idm.group(1)) if idm else None
        if not c_day: err("id must be YYYY-MM-DD-NN, dated by its first match")
        elif not idm.group(1).startswith(month): err(f"lives in tickets/{month}.json")

        days, teams, leg_odds = [], [], []
        for i, leg in enumerate(legs, 1):
            for k in sorted(set(leg) - LEG_KEYS): err(f"leg {i} has unknown field {k!r}")
            if "odds" in leg:
                if is_odds(leg["odds"]): leg_odds.append(leg["odds"])
                else: err(f"leg {i} odds must be a number above 1")
            m = matches.get(leg.get("match"))
            if not m:
                err(f"leg {i} match {leg.get('match')!r} is not in data/paridata/matches")
                continue
            day = date.fromisoformat(m["date"])
            if c_day and not 0 <= (day - c_day).days <= 2:
                err(f"leg {i} is {m['home']}–{m['away']} on {day}, outside this coupon's days — check it points at the right week")
            days.append(day)
            teams += [m["home"], m["away"]]
            picks = leg.get("pick")
            if not isinstance(picks, list) or not picks:
                err(f"leg {i} pick must be a list, e.g. [\"win:{m['home']}\"]")
                continue
            for p in picks:
                if not isinstance(p, str) or not PICK.match(p):
                    err(f"leg {i} pick {p!r} must be win:Team, win-or-draw:Team, draw or goal:Player")
                    continue
                kind, _, arg = p.partition(":")
                if kind in ("win", "win-or-draw") and arg not in (m["home"], m["away"]):
                    err(f"leg {i} pick {p!r} names a team not playing in {leg['match']}")
                if kind == "goal" and m.get("status") == "played" and "scorers" not in m:
                    err(f"leg {i} picks a scorer but {leg['match']} has no scorers list")
                anonymous(f"ticket {tid}", p)
            if m.get("status") == "postponed" and "odds" not in leg:
                err(f"leg {i} is on a postponed match and needs its odds to take them out of the coupon")

        if "odds" not in t and len(leg_odds) != len(legs): err("needs its posted odds, or odds on every leg to estimate them")
        if "odds" in t and is_odds(t["odds"]) and len(leg_odds) == len(legs):
            prod = math.prod(leg_odds)
            if abs(prod - t["odds"]) / t["odds"] > 0.01: err(f"odds {t['odds']} but the legs multiply to {prod:.3f}")
        for team, count in collections.Counter(teams).items():
            if count > 1: err(f"{team} appears in {count} legs of the same coupon")
        if c_day and days and min(days) > c_day: err(f"id should be dated {min(days)}, the day of its first match")
        if "posted" in t:
            posted = iso_date(t["posted"])
            if posted is None: err("posted must be YYYY-MM-DD")
            elif days and posted > min(days): err("posted after its first match was played")

print(f"checked {len(matches)} match(es), {len(seen)} ticket(s), {len(by_team)} team calendar(s)")
finish(fails, "every coupon points at real, dated matches; picks, odds and calendars are coherent; nothing identifies the account")

