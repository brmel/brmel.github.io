---
title: "Farkad"
date: 2026-08-01
projectNo: 4
domain: "mobile"
status: "active"
pitch: "A health tracker you talk to: say what you ate, drank and did in one sentence, and it records it."
description: "A health tracker you talk to: say what you ate, drank and did in one sentence, and it records it."
metrics:
  - value: "1 sentence"
    label: "the entire interface"
  - value: "6 areas"
    label: "filed from one spoken line"
  - value: "2 passes"
    label: "speech to structured, editable entries"
stack: ["Flutter", "Python", "Firebase Functions", "Multi-agent", "Dart"]
links:
  live: "https://farkad.web.app"
lede: |
  A health tracker whose entire interface is one spoken sentence. You say a line
  about your day — *two eggs, a big glass of water, walked forty minutes, slept
  badly* — and an agent pipeline files it across every area it touched, each
  entry editable next to the words it came from.
takeaway: "One engine that handles every combination beats six that each handle one, but it has to be decided early — retrofitting it cost me a rewrite."
lessons:
  - "**A decisions log with expiry dates outlives a design doc.** `DECISIONS.md` records every locked decision *and what no longer holds*. It exists because a navigation tab drifted three times in one session, twice from reasoning off a backlog of screens that were still only drawn. There is now a test that reads the spec table and fails when the code disagrees."
  - "**Cutting the brief was the work.** Coach, widgets, Siri and Assistant capture, Back Tap, push, share cards, custom pillars, image capture — all closed **unbuilt** on the same day, each with a written reason. The version that ships does one loop: speak, structure, correct, see. Everything that didn't serve that loop went."
  - "**One engine, every configuration.** Users pick which of six pillars they track, and the naive design is a parser per pillar. Instead one pipeline handles any combination, so adding a pillar is data rather than code. Getting there meant rewriting the first two passes after they had already worked."
  - "**Free-text input means the failure mode is silent.** The model doesn't refuse — it produces a confidently wrong number. Every generated field stays editable next to the sentence it came from, because the only workable correction UI is showing your own words back to you."
tags: ["Flutter", "Python", "AI", "Firebase", "Mobile"]
---

## The story

Every habit tracker asks you to become a data-entry clerk for your own life.
Six taps for breakfast, a separate screen for water, a sleep slider you move
without believing it. After about nine days you stop, and the app has learned
nothing about you that it could not have asked.

The information was never the hard part.

> You could say the whole day in one breath and a person would understand every
> piece of it. So the sentence should be the interface.

## The product

You say one line — *two eggs, a big glass of water, walked forty minutes, slept
badly* — and it comes back as structured entries across every area it touched,
each one editable next to the words it came from.

That last detail is the whole design. Free text means the failure mode is
silent: the model does not refuse, it produces a confidently wrong number. The
only correction interface that works is showing you your own sentence beside
what was made of it.

Users choose which of six areas they track, and the obvious build is one parser
per area. It is one engine instead, handling any combination, so adding an area
is data rather than code. I made that decision two rewrites late, after the
first version had already worked.
