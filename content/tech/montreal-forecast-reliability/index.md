---
title: "Montréal Forecast Reliability: Three Services, Two Places, 882 Comparisons"
date: 2026-08-20
relatedProject: "meteodata"
draft: false
layout: "standalone"
hideAutoHeader: true
fullBleed: true
summary: "Three forecast services, two places in Montréal, every prediction graded against the weather station beside it over five days. Temperature holds up. Rain does not — 70% of the rain calls never happened. Interactive report, gradeable from one hour ahead to twenty-four."
description: "Three forecast services graded against the weather station next door over five days. Temperature holds up; 70% of the rain calls never happened."
tags: ["Data Analysis", "Québec"]
cover:
    image: "cover.jpg"
    alt: "The forecast reliability report, showing the two Montréal forecast points and the weather stations that grade them"
    relative: true
# English-only by design: no index.fr.md / index.ar.md, and the standalone
# layout carries no language switcher — this article never appears translated.
---

> How this was built, and what it changed my mind about:
> [the MeteoData project page](/projects/meteodata/).

A forecast is a claim about the future that nobody goes back and grades. So I
graded one: three services, two places in Montréal, every prediction checked
against the weather station standing beside it.

## What I measured

Three forecasters — ECMWF, GFS and HRDPS, read through Open-Meteo — publish an
hourly forecast a week ahead for **Parc Henri-Julien** and **Montréal–Trudeau**.
I polled all three every five minutes and saved a copy only when one of them
changed its mind. An Environment Canada station beside each point measures the
real weather every minute.

The rule that makes this a forecast test rather than a hindsight test: **only
values published before the hour they describe are scored.** A service that
restates a number afterwards is not forecasting. Truth is the station's reading
at that moment, matched within five minutes — not an hourly average. That gave
**1,622 tracked forecasts** and **147 scored hours**, compared six ways for
**882 comparisons**.

## What came out

**Temperature barely cares how far ahead you ask.** The average miss was
**1.21 °C one hour ahead and 1.38 °C a full day ahead.** A day-ahead temperature
forecast is very nearly as good as an hour-ahead one, which was not what I
expected. It lands within 1 °C about half the time (49%) and within half a degree
28% of the time, running **0.15 °C cold** on average.

**Rain is a different story.** One hour ahead, rain was forecast for 133 hours
and arrived in **43** of them — **90 false alarms**, about two thirds of every
rain call. Another **23** rainy hours arrived with nothing forecast at all. The
headline "wrong 12.9% of hours" hides that asymmetry: the service is not vague
about rain, it is systematically over-eager.

**Humidity is flat and biased.** Off by roughly **7.7%** at every range from one
hour to twenty-four, and consistently **3.3% too high**. A bias that stable is
correctable; random error is not.

**The services change their minds constantly.** **87% of forecasts were
rewritten at least once** before the hour they described.

**One measure could not be graded at all.** No station here reports cloud cover,
so there is nothing to check the cloud forecast against. Sunshine stands in for
it, and the honest answer is "not measurable".

## Caveats

This is **four days and twenty hours** of August weather — 116 of 148 hours
covered, longest quiet stretch ten hours. It is enough to show the shape of the
errors and nowhere near enough to characterise a season. Parc Henri-Julien is
graded from McTavish, 7.27 km away, so some of its gap is distance rather than
forecast error.

## The full report

{{< reportframe src="reports/montreal-forecast-reliability.html" title="Montréal Forecast Reliability Report" >}}
