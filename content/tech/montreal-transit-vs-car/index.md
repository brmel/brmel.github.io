---
title: "Transit or Car in Greater Montréal"
date: 2026-11-15
wide: true
description: "1,960 trips across Greater Montréal timed by car and by transit, at the weekday morning rush and on a Sunday, mapped from 100 places."
cover:
    image: "cover.jpg"
    alt: "Map of Greater Montréal at the weekday morning rush, coloured from blue near downtown and the metro to red on the outer suburbs by how much longer transit takes than the car"
findings:
  - "At 8 a.m. on a weekday, the median trip takes 45 minutes by car and 61 by transit (1.4×). On a Sunday afternoon it takes 28 against 66 (2.3×)."
  - "Transit kept up with the car on 23% of weekday trips, against 5% on the Sunday."
  - "It loses the most across a river: at 8 a.m., +18 minutes against the car from one shore to another, +10 on the same shore."
methods: |-
  I asked Google Maps for every trip between 100 places and 20 destinations, twice: leaving at the moment of the query on Sunday 15 November 2026, from 2:00 p.m. to 7:19 p.m., and leaving on Tuesday 17 November at 8 a.m. For that weekday, Google gives driving as a range and I use its middle; with the low end, transit takes 2.0× as long instead of 1.4×. Transit time is the median of the first three options, door to door, without the wait for the first departure. Only the 1,960 pairs answered in both runs are compared.

  I picked the places and destinations, so it’s not a random sample. These are planned times, not trips anyone took, and one Tuesday and one Sunday stand in for every weekday and weekend. Map data from OpenStreetMap.
---

{{< reportframe src="reports/montreal-transit-vs-car.html" title="Transit or Car in Greater Montréal report" >}}
