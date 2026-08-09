---
title: "HydroData"
date: 2026-06-01
projectNo: 5
domain: "data"
status: "shipped"
pitch: "Two months of Hydro-Québec outage snapshots, collected every minute, turned into a reliability report the utility doesn't publish."
stack: ["Python", "pandas", "Plotly", "KMZ", "Firebase Storage"]
links:
  live: "/tech/hydro-quebec-outage-analysis/"
lede: |
  Hydro-Québec publishes a live outage map that tells you what is broken right
  now and when they expect it back, and then forgets — no history, no accuracy
  record, no way to ask whether last Tuesday's estimate meant anything. I wanted
  one number: when they say the power is back at four, how often is it back at
  four? Nobody publishes that, so I wrote the map down every minute for
  fifty-six days and worked it out — the answer is five percent.
takeaway: "A number you collected yourself changes your mind in a way the same number from someone else never does."
lessons:
  - "**The headline finding was about me, not the utility.** Announced restoration times land within an hour about 5% of the time. My second reaction was recognising the same failure in my own estimates — that became [a whole piece of writing](/thoughts/estimates-and-the-five-percent/), and it is the only thing from this project I still think about."
  - "**Collect first, decide the question later.** I started polling before I knew what I was looking for. Every interesting result — ETA accuracy, regional spread, the 611-outage peak — came from questions I could not have asked on day one, and could only ask because the data was already on disk."
  - "**Hourly files with a close-then-upload rule made the whole thing restartable.** Snapshots land in the open hour's JSONL; only closed hours upload. The collector can die at any moment and lose at most one minute, which it did, more than once, over 56 days."
  - "**Public does not mean tidy.** The outage map ships KMZ geometry meant for rendering, not analysis. Turning polygons into per-municipality attribution was most of the work, and it is why the borough map exists at all."
tags: ["Python", "Data Analysis", "Hydro-Québec", "Web Scraping"]
---

## The story

The map is a live view with no memory: it tells you what is broken right now and
then forgets, so there is no accuracy record and no way to ask whether last
Tuesday's estimate meant anything.

The only way to get the number was to write the map down every minute for two
months and work it out afterwards.

## The product

A collector polls the public outage feed once a minute, writes snapshots to
hourly JSONL files, and uploads each hour only once it is closed. An analysis
pass rebuilds outage *events* out of those snapshots — an outage is not a row,
it is a thing that appears, moves, and disappears across hundreds of readings —
and renders an HTML report.

**56 days · 7,870 readings · 16,561 unique outages · 1,280 municipalities.**

What the data said:

- **Announced restoration times land within an hour of the estimate about 5% of
  the time.** That is the number the whole project existed to get.
- **21.5 million client-hours lost** over the period, with a single worst moment
  of **611 simultaneous outages**.
- **Outaouais is the most affected region** — 2,017 outages and 3.86 million
  client-hours — against **Nord-du-Québec** at 102 outages, roughly a twentieth
  of the impact.
- The longest single outage ran **37.5 days**, in Montréal.

The report is on this site: [Hydro-Québec Outage
Analysis](/tech/hydro-quebec-outage-analysis/) — interactive charts, a regional
map, borough-level reliability, and the methodology.

The data is Hydro-Québec's own public outage feed, which anyone can see; what
did not exist was the record of what it said yesterday.
