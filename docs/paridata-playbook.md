# PariData — adding coupons and results

Everything the page shows comes from `data/paridata/`. A result is typed once, on
the match; every coupon that uses that match settles from it, and the page works
out won, lost or pending on its own.

```
data/paridata/
  profile.json            stake per bet in each currency
  regions.json            country → name in en / fr / ar (flag: assets/paridata/flags/<country>.svg)
  competitions.json       competition name → country
  matches/YYYY-MM.json    every match, keyed by id, with its score once played
  tickets/YYYY-MM.json    every coupon, as a list of legs pointing at matches
```

The experiment is anonymous: no links, handles, account names or screenshots of
the influencer's posts anywhere in the data. The repository is public. The check
rejects any link or `@handle` it finds.

## 1 · Add the matches

In `matches/` for the month the match is played, add one entry per match:

```json
"2026-09-19-sevilla-barcelona": {
  "date": "2026-09-19",
  "competition": "La Liga",
  "home": "Sevilla",
  "away": "Barcelona",
  "status": "scheduled"
}
```

The id is the date, then the home team, then the away team, lowercase with dashes.
Check which team is at home on the official match page — preview sites and team
fixture lists do not always put the home side first.

## 2 · Add the coupon

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

- `id` — the date of the coupon's first match, then `01`, `02`… for that day.
- `posted` — the day the coupon was posted, when known. Leave it out otherwise.
- `odds` — the total odds as posted. When they were not recorded, leave `odds` out
  and give every leg its own `"odds"` from market prices instead: the page multiplies
  them, rounds to two decimals, and marks the coupon's odds as estimated (≈).
- `pick` — a list; every entry must hold for the leg to win:

| Pick | Wins when |
|---|---|
| `win:Team` | that team wins |
| `win-or-draw:Team` | that team does not lose |
| `draw` | the match is drawn |
| `goal:Player` | the player is in the match's `scorers` |

Use the team name exactly as written in the match. A bet-builder leg such as
"City win or draw + Haaland to score" is one leg with two picks.

## 3 · Enter the result

When the match ends, change its status and add the score:

```json
"status": "played",
"score": { "home": 1, "away": 2 }
```

Add `"scorers": ["Player Name", …]` when any coupon has a `goal:` pick on that match.
A postponed match is `"status": "postponed"`; the leg on it then needs its own
`"odds"` so they can be taken out of the coupon.

The stake is the same for every coupon: `perUnit` in `profile.json` is one bet in
that currency ($100, 10,000 DA). A visitor can type their own stake; the data never
changes.

## New country or competition

Add the country to `regions.json` with its three names, drop its flag SVG into
`assets/paridata/flags/` under the same name, then map the competition to it in
`competitions.json`. No template changes.

## Dates

Teams play several times a week, so a leg must point at the match on the right day.
The check rejects a leg more than two days away from its coupon's date, a team with
two matches a day apart, and a team appearing twice in one coupon. Confirm every date
and score on the match's own page, not on a preview or a team's fixture list.

## 4 · Check before publishing

```bash
python3 scripts/checks/check-paridata.py
./scripts/check.sh
```

The first names the match or coupon and the problem: a pick naming a team that is
not playing, a coupon pointing at a match that does not exist, a played match with
no score, a coupon dated differently from its first match, a link or handle.
