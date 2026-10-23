---
title: "Hydro-Québec Outage Analysis: Two Months of Grid Reliability Data"
featured: 3
date: 2026-06-01
description: "Two months of Hydro-Québec’s public outage feed, graded: regional reliability, Montréal boroughs, ETA accuracy and causes. Interactive charts and map."
cover:
    image: "cover.jpg"
    alt: "Montréal outage statistics from the Hydro-Québec reliability report"
findings:
  - "Of the 6,437 outages where Hydro-Québec published a restoration estimate, 5.0% came back within an hour of the promised time. Bas-Saint-Laurent averaged 3.53 hours of error, Estrie 11.4."
  - "The median outage lasted 6.57 hours and affected 11 clients, but the period added up to 21.5 million client-hours without power. The longest outage ran 37.5 days in Montréal, the largest hit 18,255 clients in the Laurentides, and at the worst moment 611 outages were active at once."
  - "Nord-du-Québec lost 72,358 client-hours over the two months and Outaouais 3,857,245. On the island, Ahuntsic-Cartierville recorded 153 outages against Senneville’s three."
  - "Two thirds of outages have no published cause; of those that do, the largest category is planned maintenance (3,651 outages)."
methods: |-
  From 7 April to 1 June 2026 (55.8 days), I saved a snapshot of Hydro-Québec’s public outage feed every time it changed, roughly every ten minutes: 7,870 readings covering 98.5% of the hours, deduplicated into 16,561 distinct outages across 18 administrative regions, 1,280 municipalities and 33 Montréal boroughs. An outage is one (start time, GPS location) pair; its client count is the peak Hydro-Québec reported, and its duration runs from the reported start to the last reading it appeared in.

  Two months in spring is one season. Start times that predate collection are replaced with first-observed, which shortens those durations. Three collection gaps exist, the largest 21 hours. Hydro-Québec identifies municipalities by an internal code with no public name table, so results are reported by region and borough.
---

{{< reportframe src="reports/hydro-quebec-outage.html" title="Hydro-Québec Outage Reliability Report" >}}
