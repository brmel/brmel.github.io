---
title: "Rekba"
date: 2024-11-21
projectNo: 3
status: "active"
pitch: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
description: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
metrics:
  - value: "281 stations"
    label: "and 374 connections"
  - value: "3 locales"
    label: "French, Arabic and English, with right-to-left layout"
stack: ["Python", "FastAPI", "Prefect", "Typer", "GTFS", "Flutter"]
links:
  live: "https://rekba-landing.web.app"
lede: |
  Two halves, built in that order: a pipeline that manufactures a transit
  network, and the rider app that makes it useful.
---

## The story

In Algiers you find out when the bus comes by standing where the bus comes and
waiting. The mapping apps everyone already has show nothing: they consume open
transit data, and there is none to consume. Where a timetable does exist it
describes an intention rather than a schedule, which is its own kind of missing
data, and harder to detect than an empty file.

## The product

The rider app comes in the three languages the country reads in. Underneath
it I built the network out of sources never meant to be one: map geometry,
timetable estimates, coarse positions. The pipeline publishes the result, 281
stations and 374 connections, as a standard transit feed.
