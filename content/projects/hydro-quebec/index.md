---
title: "HydroData"
featured: 3
date: 2026-06-01
projectNo: 5
status: "shipped"
pitch: "I recorded every power cut in Québec for two months, to see how often the power really returns when they say it will."
description: "I recorded every power cut in Québec for two months, to see how often the power really returns when they say it will."
metrics:
  - value: "56 days"
    label: "of the outage map, recorded every minute"
  - value: "16,561"
    label: "distinct outages across 1,280 municipalities"
  - value: "5%"
    label: "of announced restoration times landed within the hour"
stack: ["Python", "pandas", "Plotly", "KMZ", "Firebase Storage"]
links:
  live: "/tech/hydro-quebec-outage-analysis/"
lede: |
  Two months of Hydro-Québec’s outage map, recorded every minute and turned into
  the reliability report the utility doesn’t publish: where outages concentrate,
  how long they really last, which causes dominate, and how often the announced
  restoration time holds.
lessons:
  - "**I collected first and decided the question later.** I started polling before I knew what I was looking for. ETA accuracy, regional spread and the 611-outage peak were all questions I couldn’t have asked on day one, and could only answer because the data was already on disk."
  - "**Hourly files made the collector safe to restart.** Snapshots land in the open hour’s JSONL file and only closed hours upload, so a crash loses at most one minute. It crashed more than once over 56 days."
  - "**The public data wasn’t tidy.** The outage map ships KMZ geometry meant for rendering. Turning those polygons into per-municipality attribution was most of the work, and it’s why the borough map exists at all."
tags: ["Python", "Data Analysis", "Québec"]
---

## The story

Hydro-Québec publishes a live outage map: what is broken now, and when they
expect it back. Then it forgets. No history, no accuracy record, no way to ask
whether last Tuesday's estimate meant anything.

I wanted one number. When they say the power is back at four, how often is it
back at four? Nobody publishes that, so I wrote the map down every minute for
fifty-six days and worked it out.
