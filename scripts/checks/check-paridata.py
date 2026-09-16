#!/usr/bin/env python3
"""The ledger is data, not prose: nothing here is checked by a human reading it.

Every rule below exists because breaking it would put a wrong number on the page
without anything looking wrong — a mistyped digit in the total odds, a voided leg
still multiplying into the return, a ticket declared won whose legs say otherwise.
"""
import glob, json, os, re, sys
from datetime import datetime, timezone

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DATA = os.path.join(ROOT, "data", "paridata")
BUNDLE = os.path.join(ROOT, "content", "projects", "paridata")

SETTLEMENTS = {"pending", "won", "lost", "void"}
ID = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(\d{2})$")
ODDS_TOLERANCE = 0.02

fails, tickets_seen, count = [], {}, 0


def bad(where, msg):
    fails.append(f"{where}: {msg}")


def when(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def derive(legs):
    states = [leg.get("settlement") for leg in legs]
    if "pending" in states:
        return "pending"
    if "lost" in states:
        return "lost"
    if all(s == "void" for s in states):
        return "void"
    return "won"


profile_path = os.path.join(DATA, "profile.json")
if not os.path.isfile(profile_path):
    bad("profile.json", "missing — the page cannot know the default stake")
else:
    profile = json.load(open(profile_path, encoding="utf-8"))
    staking = profile.get("staking", {})
    if not isinstance(staking.get("defaultStake"), (int, float)):
        bad("profile.json", "staking.defaultStake must be a number")
    if not isinstance(staking.get("currencyPerUnit"), (int, float)):
        bad("profile.json", "staking.currencyPerUnit must be a number")

for path in sorted(glob.glob(os.path.join(DATA, "[0-9][0-9][0-9][0-9]-[0-9][0-9].json"))):
    month = os.path.basename(path)[:7]
    try:
        payload = json.load(open(path, encoding="utf-8"))
    except json.JSONDecodeError as e:
        bad(os.path.basename(path), f"is not valid JSON — {e}")
        continue
    if not isinstance(payload.get("tickets"), list):
        bad(os.path.basename(path), "has no `tickets` array")
        continue

    for ticket in payload["tickets"]:
        count += 1
        tid = ticket.get("id", "<no id>")
        where = f"{month} {tid}"

        m = ID.match(str(tid))
        if not m:
            bad(where, "id must be YYYY-MM-DD-NN")
        elif f"{m.group(1)}-{m.group(2)}" != month:
            bad(where, f"id is dated {m.group(1)}-{m.group(2)} but lives in {month}.json")
        if tid in tickets_seen:
            bad(where, f"duplicate id — already used in {tickets_seen[tid]}")
        tickets_seen[tid] = month

        posted = when(ticket.get("postedAt"))
        if posted is None:
            bad(where, "postedAt is missing or not an ISO timestamp")

        odds = ticket.get("odds")
        if not isinstance(odds, (int, float)) or odds <= 1:
            bad(where, "odds must be a number greater than 1")

        stake = ticket.get("stake")
        if stake is not None and (not isinstance(stake, (int, float)) or stake <= 0):
            bad(where, "stake, when overridden, must be a positive number")

        settlement = ticket.get("settlement")
        if settlement not in SETTLEMENTS:
            bad(where, f"settlement {settlement!r} is not one of {sorted(SETTLEMENTS)}")

        url = (ticket.get("source") or {}).get("url")
        if not url:
            bad(where, "source.url is required — an unsourced row cannot be verified by a reader")

        evidence = (ticket.get("source") or {}).get("evidence")
        if evidence and not os.path.isfile(os.path.join(BUNDLE, evidence)):
            bad(where, f"source.evidence {evidence!r} is not in the page bundle")

        legs = ticket.get("legs")
        if not isinstance(legs, list) or not legs:
            bad(where, "needs at least one leg — a single is a one-leg ticket")
            continue

        for i, leg in enumerate(legs, 1):
            if not leg.get("selection"):
                bad(where, f"leg {i} has no selection")
            if leg.get("settlement") not in SETTLEMENTS:
                bad(where, f"leg {i} settlement {leg.get('settlement')!r} is not one of {sorted(SETTLEMENTS)}")
            if leg.get("settlement") == "void" and not isinstance(leg.get("odds"), (int, float)):
                bad(where, f"leg {i} is void and must carry odds — they divide out of the return")
            kickoff = when(leg["kickoffAt"]) if leg.get("kickoffAt") else None
            if kickoff and posted and kickoff < posted:
                bad(where, f"leg {i} kicks off before the pick was posted")

        if settlement in SETTLEMENTS and all(l.get("settlement") in SETTLEMENTS for l in legs):
            expected = derive(legs)
            if expected != settlement:
                bad(where, f"declared {settlement!r} but its legs say {expected!r}")

        leg_odds = [l.get("odds") for l in legs]
        if all(isinstance(o, (int, float)) for o in leg_odds) and isinstance(odds, (int, float)):
            product = 1.0
            for o in leg_odds:
                product *= o
            if abs(product - odds) > ODDS_TOLERANCE:
                bad(where, f"odds {odds} but legs multiply to {product:.3f} — one of them is mistyped")

print(f"checked {count} ticket(s) across {len(glob.glob(os.path.join(DATA, '[0-9]*.json')))} month file(s)")
if fails:
    print(f"\n❌ {len(fails)} problem(s) in the ledger:")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every ticket is sourced, internally consistent, and settles to what its legs say")
