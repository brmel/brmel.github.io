---
title: "Transit or Car in Greater Montréal"
date: 2026-11-15
wide: true
description: "1,960 trips across Greater Montréal timed by car and by transit, at the weekday morning rush and on a Sunday, mapped from 100 places."
cover:
    image: "cover.jpg"
    alt: "Map of Greater Montréal at the weekday morning rush, coloured from blue near downtown and the metro to red on the outer suburbs by how much longer transit takes than the car"
findings:
  - "At 8 a.m. on a weekday, the median trip takes 45 minutes by car and 61 by transit, 1.4 times as long. On a Sunday afternoon it takes 28 against 66, 2.3 times as long."
  - "Transit was as fast as the car on 444 of 1,960 trips at 8 a.m. on a weekday (23%), against 97 on the Sunday afternoon (5%)."
  - "At the weekday morning rush, transit takes 1.3 times the car time from central Montréal, and 1.6 times from the outer South Shore."
  - "At the weekday morning rush, trips that stay on one shore cost +10 minutes by transit against the car, and trips that cross to another shore +18."
methods: |-
  I asked Google Maps for every trip between 100 places in Greater Montréal and 20 destinations (1,980 pairs), twice, with a script in a headless browser. On Sunday 15 November 2026, from 2:00 p.m. to 7:19 p.m., it asked for each trip leaving at that moment, with the traffic of that moment. The same evening, it asked for each trip leaving on Tuesday 17 November at 8 a.m.: transit from the published schedules, and driving as Google’s typical range for that hour, such as 30 to 45 minutes, of which I take the middle. With the low end of the range instead, the median weekday trip takes 2.0 times as long by transit, not 1.4.

  Transit time is the median of the first three options Google listed, door to door with the walking, and doesn’t count the wait for the first departure. Only the 1,960 pairs with a time in both runs are compared; the other 20 returned no time, or were entries I had typed in by hand while testing the script. I picked the places (metro and train stations, bus terminals and neighbourhood centres across the island, Laval and both shores) and the destinations, so it’s not a random sample, and 7 of the 20 destinations are in central Montréal. A place’s number is the median of its trips. On the map, each pixel is a distance-weighted average of the places within a few kilometres, so the colour between two dots is an estimate. The water, the municipal and borough limits, the highways and the metro and REM lines come from OpenStreetMap.

  These are planned times, not trips anyone took: a late bus, a closed lane or a snowstorm aren’t in them. On the Sunday the destinations were measured one after another, downtown first, so the last ones met evening service. One Tuesday and one Sunday stand in for every weekday and every weekend.
---

{{< reportframe src="reports/montreal-transit-vs-car.html" title="Transit or Car in Greater Montréal report" >}}
