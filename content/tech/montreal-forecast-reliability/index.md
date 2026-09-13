---
title: "Montréal Forecast Reliability: 30 Days of Forecasts, Checked Hour by Hour"
date: 2026-08-20
relatedProject: "meteodata"
draft: false
summary: "Thirty days of Montréal weather forecasts, every one graded against the weather station beside it. Temperature holds up a day ahead. Rain does not: seven in ten rain calls never happened. Interactive report, from one hour ahead to three days."
description: "Thirty days of Montréal forecasts graded against the station next door. Temperature is 1.3 °C off a day ahead; seven in ten rain calls were false alarms."
tags: ["Data Analysis", "Québec"]
cover:
    image: "cover.jpg"
    alt: "The top of the forecast report: a day ahead, the temperature forecast misses by 1.3 °C on average"
    relative: true
---

> How this was built, and what it changed my mind about:
> [the MeteoData project page](/projects/meteodata/).

A forecast is a claim about the future that nobody goes back and grades. So I
graded one: thirty days of Montréal forecasts, every prediction checked against
the weather station standing beside it.

## What I measured

Three forecasters — ECMWF, GFS and HRDPS, read through Open-Meteo — publish an
hourly forecast a week ahead for **Parc Henri-Julien** and **Montréal–Trudeau**.
I polled all three every five minutes and saved a copy only when one of them
changed its mind. An Environment Canada station beside each point reports the
real weather every two minutes.

The rule that makes this a forecast test rather than a hindsight test: **only
values published before the hour they describe are scored.** A service that
restates a number afterwards is not forecasting. Truth is the station's reading
at that moment, matched within five minutes — not an hourly average. From
**14 August to 13 September** that saved **1,515 forecast versions**, and
something new arrived in **683 of 732 hours**.

The numbers below are for the European model at Trudeau airport, the view the
report shows.

## What came out

**Temperature barely cares how far ahead you ask, up to a day.** The average miss
was **1.2 °C one hour ahead and 1.3 °C a full day ahead**, within 1 °C about half
the time (53%, then 48%). Three days out it slips to **1.6 °C**, within 1 °C 42%
of the time.

**Rain is a different story.** One hour ahead the forecast caught **158 of 246**
rainy hours and raised **389 false alarms** — **71%** of its rain calls — while
88 rainy hours arrived with nothing forecast. A day ahead the false alarms are
73%, three days ahead 84%. The headline "wrong 11% of hours" hides that
asymmetry: most hours are dry, so the service looks accurate while being
systematically over-eager about rain.

**Rain amounts look good for the same reason.** The average miss is **0.25 mm**
an hour ahead, but in the hours when it actually rained the forecast was
**1.7 mm** off.

**Humidity is flat.** Off by **7.3%** an hour ahead, **7.7%** a day ahead and
**8.7%** three days ahead.

**The services change their minds constantly.** A new version typically arrived
every **20 minutes**.

**Cloud cover could not be graded at all.** Neither station reports it, so
sunshine stands in: **74 W/m²** off a day ahead, within 100 W/m² three times in
four.

## Caveats

This is **one month** of late-summer weather in one city — enough to show the
shape of the errors, not enough to characterise a year. Parc Henri-Julien has no
station of its own and is graded from McTavish, **7.3 km** away, so some of its
gap is distance rather than forecast error.

## The full report

{{< reportframe src="reports/montreal-forecast-reliability.html" title="Montréal Forecast Reliability Report" >}}
