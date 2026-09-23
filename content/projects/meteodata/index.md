---
title: "MeteoData"
date: 2026-08-20
projectNo: 10
domain: "data"
status: "shipped"
pitch: "I graded three weather services against the station next door, to find out which parts of a forecast you can actually believe."
description: "I graded three weather services against the station next door, to find out which parts of a forecast you can actually believe."
metrics:
  - value: "30 days"
    label: "of forecasts graded against what a station actually recorded"
  - value: "1.3 °C"
    label: "average temperature miss, a day ahead"
  - value: "71%"
    label: "of the rain calls an hour ahead never happened"
stack: ["Python", "asyncio", "httpx", "Docker", "Google Cloud Storage"]
links:
  live: "/tech/montreal-forecast-reliability/"
lede: |
  Three services publish an hourly forecast for two places in Montréal. An
  Environment Canada station sits beside each of them, measuring what actually
  happens. This records both for thirty days and grades every prediction against
  the reading for the hour it described — at one hour ahead, or three, six,
  twelve, twenty-four, or three days.
lessons:
  - "**The forecast is not bad at weather. It is bad at rain.** Temperature is 1.2 °C off six hours ahead and barely degrades out to a full day, and humidity holds. Rain does not: 419 of 583 calls six hours ahead passed without a drop, 72% false alarms, and the precipitation error does not improve as the hour approaches. A single accuracy score would have averaged the good half with the useless half."
  - "**A forecast only counts if it was on record before the hour it describes.** Services quietly restate values for hours that have already passed, so a scorer reading the current file is grading hindsight and reports suspiciously good numbers. Only forecasts published strictly before the hour they describe are scored, and that rule is written into the report method section rather than left in the code."
  - "**\"The truth\" had to be defined before anything could be graded.** The station reports every minute; the forecast describes an hour. I match the instant within ±5 minutes and leave a forecast ungraded rather than score it against the wrong time. Rain is the exception, compared against the hour it fell in, because that is the hour the station attributes it to."
  - "**One measure could not be measured, and the report says so.** No station here reports cloud cover. Sunshine stands in for it, and that row reads \"not measurable\" rather than printing a number that looks like the others."
  - "**Poll on change, not on schedule.** Reading three services every five minutes would have stored mostly duplicates. A snapshot is saved only when a service revises its forecast, which is why a month of three forecasters fits in a file you can open — and why the record shows when each service changed its mind, not just what it settled on."
resources:
  - src: "gallery/01-forecast-report.png"
    params:
      caption: "The generated report. The headline is the answer to the question I started with; the tabs re-grade every measure, and the row of horizons re-asks it for one hour ahead or three days."
tags: ["Python", "Data Analysis", "Québec"]
---

## The story

I kept cancelling things because an app said rain, and then it did not rain. That
is an ordinary complaint and a completely untestable one, because nobody
remembers the times the forecast was right.

The [HydroData](/projects/hydro-quebec/) collector already existed and had the
shape of the answer in it: poll a public source on a schedule, keep every
version, and compare what was promised against what happened. The only thing
missing was a source of truth. Environment Canada publishes station observations
every minute, and there is a station close enough to two places I care about in
Montréal to use as one.

So the question stopped being *does the forecast feel wrong* and became something
with an answer: for each hour that has now passed, what did each service say
about it, and when did they say it?

## The product

Two collectors in Docker containers. One reads the Open-Meteo API every five
minutes for ECMWF, GFS and HRDPS at Parc Henri-Julien and Montréal—Trudeau, and
writes a new record only when a service changes its mind. The other pulls
Environment Canada's SWOB-ML observations from the McTavish and Trudeau stations.
Both land in date-partitioned JSONL and mirror hourly to Google Cloud Storage.

The scorer joins them on the instant rather than the hour, refuses any forecast
published after the moment it describes, and emits a single self-contained HTML
file — inline SVG, no chart library, no network calls once it is open. The
horizon control at the top re-grades every measure on the page: the same data
asked a different question, which is the question the report exists to let you
ask.

[Read the report →](/tech/montreal-forecast-reliability/)

A month is short, and one late summer in one city is not a verdict on
forecasting. It is enough to separate the measures that hold from the one that
does not, which was the thing I actually wanted to know.
