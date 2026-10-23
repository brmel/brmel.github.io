---
title: "Rekba"
date: 2024-11-21
projectNo: 3
status: "active"
pitch: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
description: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
metrics:
  - value: "281 stations"
    label: "and 374 connections, built from open map data"
  - value: "3 locales"
    label: "French, Arabic and English, with right-to-left layout"
  - value: "1 pipeline"
    label: "three triggers: a service, a CLI and scheduled flows"
stack: ["Python", "FastAPI", "Prefect", "Typer", "GTFS", "Flutter"]
links:
  live: "https://rekba-landing.web.app"
lede: |
  Public transit for Algeria, in a country where no agency publishes a usable
  timetable. Two halves, built in that order: a pipeline that manufactures a
  transit network out of open map data and estimates, and the rider app that
  makes it useful.
---

## The story

In Algiers you find out when the bus comes by standing where the bus comes and
waiting. No agency publishes a usable timetable, and the mapping apps everyone
already has show nothing, for the same reason: they consume open transit data,
and there is none to consume. Where a timetable does exist it describes an
intention rather than a schedule, which is its own kind of missing data, and
harder to detect than an empty file.

## The product

Riders get bus, tram and metro in one app, in the three languages the country
reads in. Underneath it I built a pipeline that manufactures a network
out of sources never meant to be one: map geometry, timetable estimates, coarse
positions. It publishes the result as a standard transit feed.
