---
title: "Transit or Car in Greater Montréal"
date: 2026-11-15
wide: true
description: "1,960 trips across Greater Montréal timed by car and by transit on one Sunday: a map of how much longer transit takes from 100 places."
cover:
    image: "cover.jpg"
    alt: "Map of Greater Montréal coloured by how many more minutes transit takes than the car, palest downtown and darkest on the outer South Shore"
findings:
  - "On a Sunday afternoon, the median trip took 28 minutes by car and 66 by transit, 2.3 times as long."
  - "Transit was as fast as the car on 97 of 1,960 trips (5%), and 45 of those ended at Berri-UQAM / Quartier Latin (19), Square-Victoria / Cité du Multimédia (13) and Plateau Mont-Royal / Mont-Royal Metro (13). 26% of trips took more than three times as long."
  - "From central Montréal, transit took 1.8 times the car time; from the outer South Shore, 3.2 times (98 minutes against 31)."
  - "Trips that cross from one shore to another took 45 more minutes by transit in the median, against 25 for trips that stay on one shore."
methods: |-
  On Sunday 15 November 2026, from 2:00 p.m. to 7:19 p.m., a script in a headless browser asked Google Maps for the driving time and the transit options between 100 places in Greater Montréal and 20 destinations, leaving at the moment of the query: 1,980 pairs. I picked the places (metro and train stations, bus terminals and neighbourhood centres across the island, Laval and both shores) and the destinations, so it’s not a random sample, and 7 of the 20 destinations are in central Montréal.

  Car time is Google’s estimate with the traffic of the moment. Transit time is the median of the first three options Google listed, door to door with the walking, and doesn’t count the wait for the first departure. A place’s number is the median of its trips. On the map, each pixel is a distance-weighted average of the places within a few kilometres, so the colour between two dots is an estimate. Google returned no time for 17 pairs, and I dropped 5 entries I had typed in by hand while testing the script.

  One Sunday afternoon is one moment. Weekday buses and trains run more often and weekday roads are slower, so a weekday rush hour could look different. The destinations were measured one after another, downtown first, so the last ones met evening service.
---

{{< reportframe src="reports/montreal-transit-vs-car.html" title="Transit or Car in Greater Montréal report" >}}
