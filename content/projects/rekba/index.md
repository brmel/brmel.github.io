---
title: "Rekba"
date: 2024-11-21
projectNo: 3
domain: "infra"
status: "active"
pitch: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
description: "A bus, tram and metro app for Algeria, where no usable timetable existed until I built one."
metrics:
  - value: "281 stations"
    label: "and 374 connections, built from open map data"
  - value: "3 locales"
    label: "French, Arabic and English, right-to-left aware"
  - value: "1 pipeline"
    label: "three triggers: a service, a CLI and scheduled flows"
stack: ["Python", "FastAPI", "Prefect", "Typer", "GTFS", "Flutter"]
links:
  live: "https://rekba-landing.web.app"
lede: |
  Public transit for Algeria, in a country where no agency publishes a usable
  timetable. Two halves in order: a pipeline that manufactures a transit network
  out of open map data and estimates, and the rider app that makes it useful.
takeaway: "When the data doesn't exist, the pipeline that produces it is the product, not the app on top of it."
lessons:
  - "**I surveyed riders before writing the app, and it changed what I built.** The mapped rail network and the station-level survey came first. What people wanted was not a journey planner — it was knowing whether the thing they are standing at the stop for is actually coming."
  - "**One implementation, three triggers, and no regrets.** The business logic sits behind a FastAPI service, a Typer CLI and Prefect flows over a provider-agnostic data layer. Every rule has one home; the trigger is a detail. This is the decision I would keep on any project of this shape."
  - "**Transit feeds break constantly, so diffing became a product surface.** A feed refresh classifies every change by severity — 4 blocking, 4 critical, 24 high, 641 medium in one run across 281 stations and 374 edges — because publishing a broken timetable is worse than publishing a stale one. That screen exists because I shipped a bad feed once."
  - "**The hardest part isn't code, it's that the data doesn't exist.** No agency publishes usable GTFS. Most of the work is producing a feed at all — merging OpenStreetMap geometry, timetable estimates and coarse town-centre positions into something a router can use — and then defending it from its own upstreams."
tags: ["Python", "Transit", "Algeria"]
---

## The story

In Algiers you find out when the bus comes by standing where the bus comes and
waiting. No agency publishes a usable timetable, and the mapping apps everyone
already has show nothing, for the same reason: they consume open transit data,
and there is none to consume. Where a timetable does exist it describes an
intention rather than a schedule — which is its own kind of missing data, and
harder to detect than an empty file.

> The app everyone wants cannot exist until someone builds the data underneath
> it. The pipeline is the product; the app is the part you can see.

## The product

Riders get bus, tram and metro in one app, in the three languages the country
actually reads in. Underneath, a pipeline manufactures a network out of sources
never meant to be one: map geometry, timetable estimates, coarse positions. It
publishes the result as a standard transit feed.

The piece I did not expect to build is the review screen. Every candidate feed
is compared against the published one and every change is graded before anything
ships: routes removed, calendars changed, stations that quietly vanished. You
approve a release rather than accept it, because publishing a broken timetable
to someone standing at a stop is worse than publishing an old one.

I surveyed riders before writing any of it, and what they wanted was not a
journey planner. It was knowing whether the thing they are standing there for is
actually coming.
