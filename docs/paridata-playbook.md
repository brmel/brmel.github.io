# PariData — adding and updating tickets

Everything the page shows comes from `data/paridata/`. No template needs to change
to add a ticket, settle one, or add a league.

```
data/paridata/
  profile.json          currencies, default stake, sample flag
  competitions.json     competition name → flag
  tickets/YYYY-MM.json  one file per month, a list of tickets
```

## Add a ticket

Open the file for the month the pick was posted — create it if it is the first of
the month, starting with `[` and ending with `]` — and append:

```json
{
  "id": "2026-10-03-01",
  "postedAt": "2026-10-03T18:30:00Z",
  "settlement": "pending",
  "odds": 2.86,
  "legs": [
    {
      "competition": "Premier League",
      "home": "Tottenham",
      "away": "Wolves",
      "pick": "Tottenham to win",
      "odds": 1.65,
      "settlement": "pending"
    }
  ]
}
```

A single bet has one leg; a coupon has several. The page works out which it is.

The experiment is anonymous: no links, handles, account names or screenshots of his
posts anywhere in the data. The repository is public, so anything written here is
published. The check rejects any link or `@handle` it finds.

## Settle a ticket

When the matches finish, set each leg's `settlement` to `won`, `lost` or `void`
(postponed or cancelled), then set the ticket's own `settlement` to match: `lost`
if any leg lost, `won` if every other leg won, `void` if every leg was void.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | `YYYY-MM-DD-NN` — the posting date, then 01, 02… for that day |
| `postedAt` | yes | when the pick was posted, ISO time in UTC |
| `settlement` | yes | `pending`, `won`, `lost` or `void` |
| `odds` | yes | total odds as posted |
| `stake` | no | units, when the pick used more than the default stake |
| `notes` | no | one short sentence shown under the matches |
| `legs[].competition` | yes | must be a key in `competitions.json` |
| `legs[].home`, `legs[].away` | yes | team names |
| `legs[].pick` | yes | the bet in plain words: `Arsenal to win`, `Over 2.5 goals`, `Both teams to score` |
| `legs[].odds` | no | required when the leg is `void` |
| `legs[].settlement` | yes | as above |
| `legs[].kickoffAt` | no | ISO time; must be after `postedAt` |

## New league

Add it to `competitions.json`, pointing at a flag in `assets/paridata/flags/`
(`england`, `spain`, `italy`, `france`, `germany`, `netherlands`, `portugal`,
`europe`). A coupon mixing countries shows as Mix on its own.

## Check before publishing

```bash
python3 scripts/checks/check-paridata.py
```

It names the ticket and the problem: a link or handle, an unknown or misspelled field, a ticket in
the wrong month file, total odds that do not match the legs, a settlement its
legs contradict. `./scripts/check.sh` runs it with every other gate.

Set `"sample": false` in `profile.json` once the tickets are real — that removes
the sample-data notice from the page.
