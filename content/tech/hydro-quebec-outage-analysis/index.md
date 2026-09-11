---
title: "Hydro-Québec Outage Analysis: Two Months of Grid Reliability Data"
date: 2026-06-01
relatedProject: "hydro-quebec"
draft: false
layout: "standalone"
hideAutoHeader: true
fullBleed: true
disableShare: false
summary: "A two-month reliability study of Hydro-Québec's public outage feed — regional reliability, Montréal boroughs, ETA accuracy, causes, record outages, and the data pipeline behind it. Interactive charts + map."
description: "Two months of Hydro-Québec's public outage feed, graded: regional reliability, Montréal boroughs, ETA accuracy and causes. Interactive charts and map."
tags: ["Data Analysis", "Québec"]
cover:
    image: "cover.jpg"
    alt: "Montréal outage statistics from the Hydro-Québec reliability report"
    relative: true
# English-only by design: no index.fr.md / index.ar.md, and the standalone
# layout carries no language switcher — this article never appears translated.
---

<!-- DRAFT — numbers pulled from the generated report; verify before publishing. -->

> How this was built, and what it changed my mind about:
> [the HydroData project page](/projects/hydro-quebec/).

Last winter my power went out. The estimate said two hours, then it slipped to
one, then to three, and I spent the whole day in the dark. I wanted to know
whether that was bad luck or the normal case — so I recorded Hydro-Québec's
public outage feed for two months and graded it.

## What I measured

From **7 April to 1 June 2026** — 55.8 days — I saved a snapshot of the live
outage feed every time Hydro-Québec published a change, roughly every ten
minutes. That came to **7,870 readings covering 98.5% of the hours** in the
period, which deduplicated into **16,561 distinct outages** across 18
administrative regions, 1,280 municipalities and 33 Montréal boroughs.

An outage is one `(start time, GPS location)` pair. Its client count is the peak
Hydro-Québec reported for it, and its duration runs from the reported start to
the last reading it appeared in. Multiply those two and you get client-hours,
which is the only number here that describes people rather than equipment.

## What came out

**The restoration estimates do not hold.** Of the 6,437 outages where
Hydro-Québec published an ETA, **5.0% came back within an hour of the promised
time.** Not 50%. Five. The rest were off by more than an hour in one direction
or the other, and the regional spread is wide: Bas-Saint-Laurent averaged 3.53
hours of error, Estrie 11.4.

**The typical outage is short and small; the totals are not.** Median duration
was **6.57 hours** and the typical outage affected **11 clients** — but summed
across the period that is **21.5 million client-hours** without power. The
distribution has a long tail: the longest single outage ran **37.5 days** in
Montréal, and the largest hit **18,255 clients** in the Laurentides. At the worst
moment, **611 outages were active simultaneously.**

**Where you live matters more than I expected.** Nord-du-Québec lost 72,358
client-hours over the two months; Outaouais lost 3,857,245 — a fifty-fold gap.
On the island, Ahuntsic-Cartierville recorded 153 outages against Senneville's
three.

**Two thirds of outages have no published cause.** The feed leaves the cause
code blank most of the time. Of those it does fill in, the largest single
category is planned maintenance — 3,651 outages — which means a good share of
what reads as grid failure was scheduled work.

## Caveats

Two months in spring is one season, not a verdict on the grid. Outage start
times that predate collection are replaced with first-observed, which shortens
those durations. Three collection gaps exist, the largest 21 hours. And
Hydro-Québec identifies municipalities by an internal code with no public name
table, so results are reported by region and borough rather than by town.

## The full report

{{< reportframe src="reports/hydro-quebec-outage.html" title="Hydro-Québec Outage Reliability Report" >}}
