# PariData playbook

How to add coupons and results. The page (`layouts/projects/tracker.html`) renders everything from
`data/paridata/`. A result is typed once, on the match; every coupon that uses the match settles from
it as won, lost or pending.

```
data/paridata/
  profile.json            default stake in units, and each currency's value per unit
  regions.json            country → name in en / fr / ar; flag at assets/paridata/flags/<country>.svg
  competitions.json       competition name → country
  matches/YYYY-MM.json    every match, keyed by id, with its score once played
  tickets/YYYY-MM.json    every coupon, as a list of legs pointing at matches
```

The experiment is anonymous and the repository is public: no links, handles, account names or
screenshots of the tipster's posts anywhere in the data. `check-paridata.py` rejects any link or
`@handle`.

## 1. Add the matches

In `matches/` for the month the match is played, one entry per match:

```json
"2026-09-19-sevilla-barcelona": {
  "date": "2026-09-19",
  "competition": "La Liga",
  "home": "Sevilla",
  "away": "Barcelona",
  "status": "scheduled"
}
```

The id is the date, the home team, then the away team, lowercase with dashes. Confirm the home side,
the date and later the score on the official match page; previews and team fixture lists are not
reliable. Teams play several times a week, so the check rejects a team with two matches a day apart.

## 2. Add the coupon

In `tickets/` for the month of its first match:

```json
{
  "id": "2026-09-19-01",
  "posted": "2026-09-19",
  "odds": 2.64,
  "legs": [
    { "match": "2026-09-19-sevilla-barcelona", "pick": ["win:Barcelona"] },
    { "match": "2026-09-20-bournemouth-liverpool", "pick": ["win-or-draw:Liverpool"] }
  ]
}
```

| Field | Rule |
|---|---|
| `id` | The date of the coupon's first match, then `01`, `02`… for that day. |
| `posted` | The day the coupon was posted; leave it out when unknown. |
| `odds` | The total odds as posted. When they were not recorded, leave `odds` out and give every leg its own `"odds"` from market prices: the page multiplies them, rounds to two decimals and marks the total as estimated (≈). |
| `pick` | A list; every entry must hold for the leg to win. |

| Pick | Wins when |
|---|---|
| `win:Team` | that team wins |
| `win-or-draw:Team` | that team does not lose |
| `draw` | the match is drawn |
| `goal:Player` | the player is in the match's `scorers` |

Team names match the match entry exactly. A bet-builder leg such as "City win or draw + Haaland to
score" is one leg with two picks. A leg must be within two days of its coupon's date, and a team
appears once per coupon.

## 3. Enter the result

When the match ends:

```json
"status": "played",
"score": { "home": 1, "away": 2 }
```

Add `"scorers": ["Player Name", …]` when a coupon has a `goal:` pick on that match. A postponed match
is `"status": "postponed"`, and the leg on it needs its own `"odds"` so they can be taken out of the
coupon.

Every coupon has the same stake, `staking.defaultStake` units in `profile.json`; each currency's
`perUnit` converts it ($100, 10,000 DA). A visitor can type their own stake; the data never changes.

## 4. New country or competition

Add the country to `regions.json` with its three names, put its flag SVG in `assets/paridata/flags/`
under the same name, then map the competition to it in `competitions.json`. `regions.json` keeps a
`mix` entry for coupons that cross countries. No template changes.

## 5. Check

```bash
python3 scripts/checks/check-paridata.py
./scripts/check.sh
```

The first names the match or coupon and the problem: a pick naming a team that is not playing, a leg
pointing at a missing match, a played match with no score, a coupon dated differently from its first
match, odds that disagree with the legs, a link or handle.
