---
title: "MeteoData"
date: 2026-08-20
projectNo: 10
domain: "data"
status: "shipped"
pitch: "I graded three weather services against the station next door, to find out which parts of a forecast you can actually believe."
description: "I graded three weather services against the station next door, to find out which parts of a forecast you can actually believe."
metrics:
  - value: "882"
    label: "forecasts graded against what a station actually recorded"
  - value: "1.19 °C"
    label: "average temperature miss, six hours ahead"
  - value: "70%"
    label: "of the rain calls never happened"
stack: ["Python", "asyncio", "httpx", "Docker", "Google Cloud Storage"]
links:
  live: "/tech/montreal-forecast-reliability/"
lede: |
  Three services publish an hourly forecast for two places in Montréal. An
  Environment Canada station sits beside each of them, measuring what actually
  happens every minute. This records both for just under five days and grades
  every prediction against the reading for the hour it described — at one hour
  ahead, or three, six, twelve, twenty-four.
takeaway: "A forecast is not one prediction, it is six, and they are not equally good — averaging them into \"accurate\" is how the useful part gets hidden."
lessons:
  - "**The app is not bad at weather. It is bad at rain.** Temperature is genuinely good — 1.19 °C off six hours ahead, and it barely degrades out to a full day. Humidity holds. Then rain: 95 of 136 calls passed without a drop, 70% false alarms, and unlike temperature the precipitation error does not improve as the hour approaches. 0.40 mm at six hours is 0.40 mm at twenty-four. Getting one number for \"is the forecast accurate\" would have averaged the good half with the useless half and told me nothing."
  - "**A forecast only counts if it was on record before the thing happened.** Services quietly restate values for hours that have already passed, and a scorer that reads the current file is grading hindsight and will report suspiciously good numbers. Only forecasts published strictly before the hour they describe are scored. This is the rule the whole result depends on, and it is invisible in the output — which is exactly why it is written into the report's method section rather than left in the code."
  - "**\"The truth\" needed defining before anything could be graded.** The station reports every minute; the forecast describes an hour. I match the instant, within ±5 minutes, and leave a forecast ungraded rather than score it against the wrong time — an unhelpful answer beats a confident wrong one. Rain is the exception and is compared against the hour it fell in, because that is the hour the station attributes it to."
  - "**One measure could not be measured, and saying so was better than substituting quietly.** No station here reports cloud cover. Sunshine stands in for it, and the report says \"not measurable\" in that row rather than printing a number that looks like the others. The temptation to fill the cell was real."
  - "**Poll on change, not on schedule.** Reading three services every five minutes and storing a copy every time would have been mostly duplicates. A snapshot is saved only when a service has changed its mind, which is why five days of three forecasters fits in a file you can open — and why the record shows when each service revised, not just what it ended up saying."
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

Five days is short, and one summer week in one city is not a verdict on
forecasting. It is enough to separate the measures that hold from the one that
does not, which was the thing I actually wanted to know.
