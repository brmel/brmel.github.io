#!/usr/bin/env python3
import collections, glob, json, math, os, re
from datetime import date
from gate import ROOT, finish

DATA = os.path.join(ROOT, "data", "paridata")
FLAGS = os.path.join(ROOT, "assets", "paridata", "flags")

LANGS = ("en", "fr", "ar")
MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.json$")
MATCH_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*$")
TICKET_ID = re.compile(r"^(\d{4}-\d{2}-\d{2})-\d{2}$")
IDENTIFYING = re.compile(r"https?://|www\.|@\w")
PICK = re.compile(r"^(win|win-or-draw|goal):.+$|^draw$")
MATCH_KEYS = {"date", "competition", "home", "away", "status", "score", "scorers"}
STATUSES = {"scheduled", "played", "postponed"}
TICKET_KEYS = {"id", "posted", "odds", "legs"}
LEG_KEYS = {"match", "pick", "odds"}
MAX_COUPON_SPAN_DAYS = 2
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


def odds(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 1


def month_files(folder):
    for path in sorted(glob.glob(os.path.join(DATA, folder, "*.json"))):
        name = os.path.basename(path)
        if MONTH_FILE.match(name):
            yield name[:7], load(path)
        else:
            fails.append(f"{folder}/{name}: files are named YYYY-MM.json")


def anonymous(where, *values):
    for value in values:
        if isinstance(value, str) and IDENTIFYING.search(value):
            fails.append(f"{where}: {value!r} contains a link or handle — the experiment stays anonymous")


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
    for lang in LANGS:
        if not (names or {}).get(lang):
            fails.append(f"regions.json: {key!r} needs a {lang} name")
if "mix" not in regions:
    fails.append("regions.json: needs 'mix', used when a coupon crosses countries")

competitions = load(os.path.join(DATA, "competitions.json")) or {}
for name, region in competitions.items():
    if region not in regions:
        fails.append(f"competitions.json: {name!r} maps to {region!r}, which is not in regions.json")

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
        if status == "played":
            score = m.get("score")
            if not isinstance(score, dict) or set(score) != {"home", "away"} or not all(isinstance(v, int) and v >= 0 for v in score.values()):
                fails.append(f"{where}: a played match needs score {{\"home\": n, \"away\": n}}")
        elif "score" in m or "scorers" in m:
            fails.append(f"{where}: only a played match has a score or scorers")
        if "scorers" in m and not (isinstance(m["scorers"], list) and all(isinstance(s, str) and s for s in m["scorers"])):
            fails.append(f"{where}: scorers must be a list of player names")
        anonymous(where, m.get("home"), m.get("away"), *(m.get("scorers") or []))
        matches[mid] = m

by_team = collections.defaultdict(list)
for mid, m in matches.items():
    day = iso_date(m.get("date"))
    for team in (m.get("home"), m.get("away")):
        if day and team:
            by_team[team].append((day, mid))
for team, games in by_team.items():
    games.sort()
    for (d1, a), (d2, b) in zip(games, games[1:]):
        if (d2 - d1).days <= 1:
            fails.append(f"{team} plays {a} and {b} within a day — one of those dates is wrong")

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
        if "odds" in t and not odds(t["odds"]):
            bad("odds must be a number above 1")
        legs = t.get("legs")
        if not isinstance(legs, list) or not legs:
            bad("needs at least one leg")
            continue

        idm = TICKET_ID.match(str(tid))
        coupon_day = iso_date(idm.group(1)) if idm else None
        if not coupon_day:
            bad("id must be YYYY-MM-DD-NN, dated by its first match")
        elif not idm.group(1).startswith(month):
            bad(f"lives in tickets/{month}.json")

        days, teams, leg_odds = [], [], []
        for i, leg in enumerate(legs, 1):
            for key in sorted(set(leg) - LEG_KEYS):
                bad(f"leg {i} has unknown field {key!r}")
            if "odds" in leg:
                if odds(leg["odds"]):
                    leg_odds.append(leg["odds"])
                else:
                    bad(f"leg {i} odds must be a number above 1")
            m = matches.get(leg.get("match"))
            if not m:
                bad(f"leg {i} match {leg.get('match')!r} is not in data/paridata/matches")
                continue
            day = date.fromisoformat(m["date"])
            if coupon_day and not 0 <= (day - coupon_day).days <= MAX_COUPON_SPAN_DAYS:
                bad(f"leg {i} is {m['home']}–{m['away']} on {day}, outside this coupon's days — check it points at the right week")
            days.append(day)
            teams += [m["home"], m["away"]]
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
            if m.get("status") == "postponed" and "odds" not in leg:
                bad(f"leg {i} is on a postponed match and needs its odds to take them out of the coupon")

        if "odds" not in t and len(leg_odds) != len(legs):
            bad("needs its posted odds, or odds on every leg to estimate them")
        if "odds" in t and odds(t["odds"]) and len(leg_odds) == len(legs):
            product = math.prod(leg_odds)
            if abs(product - t["odds"]) / t["odds"] > 0.01:
                bad(f"odds {t['odds']} but the legs multiply to {product:.3f}")
        for team, count in collections.Counter(teams).items():
            if count > 1:
                bad(f"{team} appears in {count} legs of the same coupon")
        if coupon_day and days and min(days) > coupon_day:
            bad(f"id should be dated {min(days)}, the day of its first match")
        if "posted" in t:
            posted = iso_date(t["posted"])
            if posted is None:
                bad("posted must be YYYY-MM-DD")
            elif days and posted > min(days):
                bad("posted after its first match was played")

print(f"checked {len(matches)} match(es), {len(seen)} ticket(s), {len(by_team)} team calendar(s)")
finish(fails, "every coupon points at real, dated matches; picks, odds and calendars are coherent; nothing identifies the account")
