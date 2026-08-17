---
title: "HydroData"
date: 2026-06-01
projectNo: 5
domain: "data"
status: "shipped"
pitch: "I recorded every power cut in Québec for two months, to see how often the power really returns when they say it will."
description: "I recorded every power cut in Québec for two months, to see how often the power really returns when they say it will."
startHereWhy: "two months of data I collected, and a number nobody publishes"
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
  Two months of Hydro-Québec's outage map, recorded every minute and turned into
  the reliability report the utility does not publish: where outages concentrate,
  how long they really last, and how often the announced restoration time holds.
takeaway: "A number I collected myself changed my mind in a way the same number from someone else would not have."
lessons:
  - "**The headline finding was about me, not the utility.** Announced restoration times land within an hour about 5% of the time. My second reaction was recognising the same failure in my own estimates — that became [a whole piece of writing](/thoughts/estimates-and-the-five-percent/), and it is the only thing from this project I still think about."
  - "**Collect first, decide the question later.** I started polling before I knew what I was looking for. Every interesting result — ETA accuracy, regional spread, the 611-outage peak — came from questions I could not have asked on day one, and could only ask because the data was already on disk."
  - "**Hourly files with a close-then-upload rule made the whole thing restartable.** Snapshots land in the open hour's JSONL; only closed hours upload. The collector can die at any moment and lose at most one minute, which it did, more than once, over 56 days."
  - "**Public does not mean tidy.** The outage map ships KMZ geometry meant for rendering, not analysis. Turning polygons into per-municipality attribution was most of the work, and it is why the borough map exists at all."
tags: ["Python", "Data Analysis", "Québec"]
---

## The story

Hydro-Québec publishes a live outage map: what is broken now, and when they
expect it back. Then it forgets. No history, no accuracy record, no way to ask
whether last Tuesday's estimate meant anything.

I wanted one number. When they say the power is back at four, how often is it
back at four? Nobody publishes that, so I wrote the map down every minute for
fifty-six days and worked it out.

> It is right about five percent of the time. The second thing I noticed was
> that I estimate exactly the same way.

## The product

A reliability report the utility does not produce: where outages concentrate,
how long they really last, which causes dominate, and how far the published
estimates fall from what happened. The Montréal borough map exists because the
raw feed ships geometry meant for drawing, not for counting, and turning
polygons into per-municipality attribution was most of the work.

The collector is deliberately dull. Snapshots append to the open hour's file and
only closed hours upload, so it can die at any moment and lose at most one
minute — which it did, more than once, over eight weeks.

I started polling before I knew the question. Every result worth having came
from something I could not have thought to ask on day one, and could only ask
because the data was already on disk.
