#!/usr/bin/env python3
import glob, json, os, re, sys
from datetime import datetime

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DATA = os.path.join(ROOT, "data", "paridata")
BUNDLE = os.path.join(ROOT, "content", "projects", "paridata")
FLAGS = os.path.join(ROOT, "assets", "paridata", "flags")

SETTLEMENTS = {"pending", "won", "lost", "void"}
ID = re.compile(r"^(\d{4}-\d{2})-\d{2}-\d{2}$")
fails, seen, count = [], {}, 0


def load(name):
    try:
        return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fails.append(f"{name}: {e}")
        return {}


def timestamp(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


profile = load("profile.json")
staking = profile.get("staking", {})
for key in ("defaultStake", "currencyPerUnit"):
    if not number(staking.get(key)) or staking[key] <= 0:
        fails.append(f"profile.json: staking.{key} must be a positive number")
for key in ("currency", "currencySymbol"):
    if not staking.get(key):
        fails.append(f"profile.json: staking.{key} is required")
if timestamp((profile.get("window") or {}).get("start")) is None:
    fails.append("profile.json: window.start must be an ISO date")

competitions = load("competitions.json")
for name, region in competitions.items():
    if not os.path.isfile(os.path.join(FLAGS, f"{region}.svg")):
        fails.append(f"competitions.json: {name!r} maps to {region!r}, which has no flag in assets/paridata/flags/")

for path in sorted(glob.glob(os.path.join(DATA, "[0-9][0-9][0-9][0-9]-[0-9][0-9].json"))):
    month = os.path.basename(path)[:7]
    tickets = load(os.path.basename(path)).get("tickets")
    if not isinstance(tickets, list):
        fails.append(f"{month}.json: no tickets array")
        continue

    for t in tickets:
        count += 1
        tid = t.get("id", "<no id>")
        bad = lambda msg: fails.append(f"{tid}: {msg}")

        m = ID.match(str(tid))
        if not m:
            bad("id must be YYYY-MM-DD-NN")
        elif m.group(1) != month:
            bad(f"lives in {month}.json but is dated {m.group(1)}")
        if tid in seen:
            bad("duplicate id")
        seen[tid] = True

        posted = timestamp(t.get("postedAt"))
        if posted is None:
            bad("postedAt must be an ISO timestamp")
        if not number(t.get("odds")) or t["odds"] <= 1:
            bad("odds must be a number above 1")
        if "stake" in t and (not number(t["stake"]) or t["stake"] <= 0):
            bad("stake, when set, must be a positive number")
        if t.get("settlement") not in SETTLEMENTS:
            bad(f"settlement must be one of {sorted(SETTLEMENTS)}")

        source = t.get("source") or {}
        if not source.get("url"):
            bad("source.url is required")
        if source.get("evidence") and not os.path.isfile(os.path.join(BUNDLE, source["evidence"])):
            bad(f"evidence {source['evidence']!r} is not in the page bundle")

        legs = t.get("legs")
        if not isinstance(legs, list) or not legs:
            bad("needs at least one leg")
            continue
        for i, leg in enumerate(legs, 1):
            if not leg.get("selection"):
                bad(f"leg {i} has no selection")
            if leg.get("settlement") not in SETTLEMENTS:
                bad(f"leg {i} settlement must be one of {sorted(SETTLEMENTS)}")
            if leg.get("settlement") == "void" and not number(leg.get("odds")):
                bad(f"leg {i} is void and needs its odds")
            if leg.get("competition") and leg["competition"] not in competitions:
                bad(f"leg {i} competition {leg['competition']!r} is missing from competitions.json")
            kickoff = timestamp(leg["kickoffAt"]) if leg.get("kickoffAt") else None
            if kickoff and posted and kickoff < posted:
                bad(f"leg {i} kicked off before the pick was posted")

        states = [leg.get("settlement") for leg in legs]
        if all(s in SETTLEMENTS for s in states):
            derived = ("pending" if "pending" in states else "lost" if "lost" in states
                       else "void" if all(s == "void" for s in states) else "won")
            if t.get("settlement") in SETTLEMENTS and derived != t["settlement"]:
                bad(f"declared {t['settlement']!r} but its legs say {derived!r}")

        if all(number(leg.get("odds")) for leg in legs) and number(t.get("odds")):
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
