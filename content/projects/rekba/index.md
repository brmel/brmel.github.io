---
title: "Rekba"
date: 2026-08-06
projectNo: 3
domain: "infra"
status: "active"
pitch: "Public transit for Algeria — bus, tram and metro in one app, in a country with no reliable open timetable data."
stack: ["Python", "FastAPI", "Prefect", "Typer", "GTFS", "Flutter"]
links:
  live: "https://rekba-landing.web.app"
takeaway: "When the data doesn't exist, the product is the pipeline that produces it — not the app on top."
lessons:
  - "**I surveyed riders before writing the app, and it changed what I built.** The mapped rail network and the station-level survey came first. What people wanted was not a journey planner — it was knowing whether the thing they are standing at the stop for is actually coming."
  - "**One implementation, three triggers, and no regrets.** The business logic sits behind a FastAPI service, a Typer CLI and Prefect flows over a provider-agnostic data layer. Every rule has one home; the trigger is a detail. This is the decision I would keep on any project of this shape."
  - "**Transit feeds break constantly, so diffing became a product surface.** A feed refresh classifies every change by severity — 4 blocking, 4 critical, 24 high, 641 medium in one run across 281 stations and 374 edges — because publishing a broken timetable is worse than publishing a stale one. That screen exists because I shipped a bad feed once."
  - "**The hardest part isn't code, it's that the data doesn't exist.** No agency publishes usable GTFS. Most of the work is producing a feed at all — merging OpenStreetMap geometry, timetable estimates and coarse town-centre positions into something a router can use — and then defending it from its own upstreams."
tags: ["Python", "FastAPI", "GTFS", "Transit", "Algeria"]
---

## The story

In Algiers you find out when the bus comes by standing where the bus comes and
waiting. There is no timetable to check. For the routes that do have one, it
describes an intention rather than a schedule.

Every mapping app has the same gap, and for the same reason: they consume open
transit data, and Algeria doesn't publish any. There's nothing to consume. The
app you'd want can't be built until someone builds the feed underneath it.

Rekba is an attempt at both, in that order. The transit app is the visible half.
The half that took the work is the pipeline that manufactures a usable network
out of sources that were never meant to be one.

## The product

Riders get bus, tram and metro in one app — lines, live positions where they can
be estimated, and routes that reflect how the network actually runs. Three
locales, French, Arabic and English, RTL-aware, because that is how the country
reads.

Underneath, the backend is deliberately shaped: **one business-logic
implementation behind three triggers** — a FastAPI service, a Typer CLI and
Prefect flows — over a provider-agnostic `data/` layer, with infrastructure
concerns isolated and a dependency-free `kernel/` at the leaf. Adding a fourth
way to invoke something doesn't mean reimplementing it.

The piece I did not expect to build is the **feed refresh review screen**. Every
candidate feed is diffed against the published baseline and every change is
classified by severity before anything ships — routes removed, calendars
changed, stops that vanished. A run over the current network produces 281
stations, 374 edges, and a change list you approve rather than accept. Publishing
a broken timetable to someone standing at a stop is worse than publishing an old
one.

The app is not launched yet — the landing page says *bientôt disponible* and
means it. The network and the pipeline are the parts that exist.
