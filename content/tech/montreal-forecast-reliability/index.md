---
title: "Montréal Forecast Reliability: 30 Days of Forecasts, Checked Hour by Hour"
date: 2026-08-20
description: "Thirty days of Montréal forecasts graded against the station next door. Temperature is 1.3 °C off a day ahead; seven in ten rain calls were false alarms."
tags: ["Data Analysis", "Québec"]
cover:
    image: "cover.jpg"
    alt: "The top of the forecast report: a day ahead, the temperature forecast misses by 1.3 °C on average"
findings:
  - "Temperature is the reliable part: 1.2 °C off six hours ahead and 1.3 °C a day ahead, on average. Humidity holds as well."
  - "Rain is not: six hours ahead, 419 of 583 rain calls passed without a drop (72% false alarms), and the precipitation error does not improve as the hour approaches."
  - "No station here reports cloud cover, so sunshine stands in for it and that measure reads \"not measurable\"."
methods: |-
  From 14 August to 13 September 2026, I recorded the hourly forecasts of three services (ECMWF, GFS and HRDPS, through Open-Meteo) for Parc Henri-Julien and Montréal–Trudeau, saving a new record only when a service changed its forecast. Each forecast is graded against Environment Canada’s McTavish and Trudeau stations at one, three, six, twelve or twenty-four hours ahead, or three days ahead.

  A forecast counts only if it was published before the hour it describes. Instants are matched within ±5 minutes; rain is compared against the hour it fell in. One month of late summer in one city is not a verdict on forecasting.
---

{{< reportframe src="reports/montreal-forecast-reliability.html" title="Montréal Forecast Reliability Report" >}}
