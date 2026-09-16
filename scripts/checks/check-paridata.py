#!/usr/bin/env python3
import glob, json, os, re, sys
from datetime import datetime

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DATA = os.path.join(ROOT, "data", "paridata")
BUNDLE = os.path.join(ROOT, "content", "projects", "paridata")
FLAGS = os.path.join(ROOT, "assets", "paridata", "flags")

SETTLEMENTS = {"pending", "won", "lost", "void"}
TICKET_KEYS = {"id", "postedAt", "settlement", "odds", "stake", "source", "evidence", "notes", "legs"}
LEG_KEYS = {"competition", "home", "away", "pick", "odds", "settlement", "kickoffAt"}
MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.json$")
ID = re.compile(r"^(\d{4}-\d{2})-\d{2}-\d{2}$")
fails, seen, count = [], set(), 0


def load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fails.append(f"{os.path.relpath(path, DATA)}: {e}")
        return None


def timestamp(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


profile = load(os.path.join(DATA, "profile.json")) or {}
staking = profile.get("staking", {})
if not number(staking.get("defaultStake")) or staking["defaultStake"] <= 0:
    fails.append("profile.json: staking.defaultStake must be a positive number")
currencies = staking.get("currencies")
if not isinstance(currencies, list) or not currencies:
    fails.append("profile.json: staking.currencies needs at least one currency")
for c in currencies or []:
    code = c.get("code") or "?"
    if not c.get("code") or not c.get("symbol"):
        fails.append(f"profile.json: currency {code} needs a code and a symbol")
    if not number(c.get("perUnit")) or c["perUnit"] <= 0:
        fails.append(f"profile.json: currency {code} perUnit must be a positive number")
    if c.get("decimals") not in (0, 1, 2, 3):
        fails.append(f"profile.json: currency {code} decimals must be 0 to 3")

competitions = load(os.path.join(DATA, "competitions.json")) or {}
for name, region in competitions.items():
    if not os.path.isfile(os.path.join(FLAGS, f"{region}.svg")):
        fails.append(f"competitions.json: {name!r} maps to {region!r}, which has no flag in assets/paridata/flags/")

for path in sorted(glob.glob(os.path.join(DATA, "tickets", "*.json"))):
    name = os.path.basename(path)
    if not MONTH_FILE.match(name):
        fails.append(f"tickets/{name}: ticket files are named YYYY-MM.json")
        continue
    tickets = load(path)
    if not isinstance(tickets, list):
        fails.append(f"tickets/{name}: must be a list of tickets")
        continue

    for t in tickets:
        count += 1
        tid = t.get("id", "<no id>")
        bad = lambda msg: fails.append(f"{tid}: {msg}")

        for key in sorted(set(t) - TICKET_KEYS):
            bad(f"unknown field {key!r}")
        m = ID.match(str(tid))
        if not m:
            bad("id must be YYYY-MM-DD-NN")
        elif f"{m.group(1)}.json" != name:
            bad(f"is dated {m.group(1)} but lives in tickets/{name}")
        if tid in seen:
            bad("duplicate id")
        seen.add(tid)

        posted = timestamp(t.get("postedAt"))
        if posted is None:
            bad("postedAt must be an ISO timestamp")
        if t.get("settlement") not in SETTLEMENTS:
            bad(f"settlement must be one of {sorted(SETTLEMENTS)}")
        if not number(t.get("odds")) or t["odds"] <= 1:
            bad("odds must be a number above 1")
        if "stake" in t and (not number(t["stake"]) or t["stake"] <= 0):
            bad("stake, when set, must be a positive number")
        if not str(t.get("source", "")).startswith("http"):
            bad("source must be the URL of the post")
        if t.get("evidence") and not os.path.isfile(os.path.join(BUNDLE, t["evidence"])):
            bad(f"evidence {t['evidence']!r} is not in the page bundle")

        legs = t.get("legs")
        if not isinstance(legs, list) or not legs:
            bad("needs at least one leg")
            continue
        for i, leg in enumerate(legs, 1):
            for key in sorted(set(leg) - LEG_KEYS):
                bad(f"leg {i} has unknown field {key!r}")
            for key in ("competition", "home", "away", "pick"):
                if not leg.get(key):
                    bad(f"leg {i} needs {key}")
            if leg.get("competition") and leg["competition"] not in competitions:
                bad(f"leg {i} competition {leg['competition']!r} is missing from competitions.json")
            if leg.get("settlement") not in SETTLEMENTS:
                bad(f"leg {i} settlement must be one of {sorted(SETTLEMENTS)}")
            if "odds" in leg and (not number(leg["odds"]) or leg["odds"] <= 1):
                bad(f"leg {i} odds must be a number above 1")
            if leg.get("settlement") == "void" and not number(leg.get("odds")):
                bad(f"leg {i} is void and needs its odds")
            kickoff = timestamp(leg["kickoffAt"]) if leg.get("kickoffAt") else None
            if leg.get("kickoffAt") and kickoff is None:
                bad(f"leg {i} kickoffAt must be an ISO timestamp")
            if kickoff and posted and kickoff < posted:
                bad(f"leg {i} kicked off before the pick was posted")

        states = [leg.get("settlement") for leg in legs]
        if t.get("settlement") in SETTLEMENTS and all(s in SETTLEMENTS for s in states):
            derived = ("pending" if "pending" in states else "lost" if "lost" in states
                       else "void" if all(s == "void" for s in states) else "won")
            if derived != t["settlement"]:
                bad(f"declared {t['settlement']!r} but its legs say {derived!r}")

        if number(t.get("odds")) and all(number(leg.get("odds")) for leg in legs):
            product = 1.0
            for leg in legs:
                product *= leg["odds"]
            if abs(product - t["odds"]) > 0.02:
                bad(f"odds {t['odds']} but the legs multiply to {product:.3f}")

print(f"checked {count} ticket(s)")
if fails:
    print(f"\n❌ {len(fails)} problem(s) in data/paridata:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every ticket is sourced, consistent, and settles to what its legs say")
