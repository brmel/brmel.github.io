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
lessons:
  - "**A decisions log with expiry dates outlives a design doc.** `DECISIONS.md` records every locked decision and what no longer holds. It exists because one navigation tab drifted three times in a single session, twice from reasoning off screens that were still only drawn. A test now reads the spec table and fails when the code disagrees."
  - "**Cutting the brief was the work.** Coach, widgets, Siri and Assistant capture, Back Tap, push, share cards, custom pillars, image capture — all closed unbuilt on the same day, each with a written reason. The shipped version does one loop: speak, structure, correct, see."
  - "**One engine, every configuration.** Users pick which of six pillars they track. The naive design is a parser per pillar; instead one pipeline handles any combination, so adding a pillar is data rather than code. Getting there meant rewriting the first two passes after they already worked."
  - "**Free-text input fails silently.** The model does not refuse — it returns a confidently wrong number. Every generated field stays editable next to the sentence it came from, because showing someone their own words back is the only correction UI that works."
tags: ["Flutter", "Python", "AI", "Firebase", "Mobile"]
---

## The story

Every habit tracker asks you to become a data-entry clerk for your own life. Six
taps for breakfast, a separate screen for water, a sleep slider you move without
believing it. After about nine days you stop, and the app has learned nothing
about you it could not have simply asked.

The information was never the hard part.

## The product

You say one line — *two eggs, a big glass of water, walked forty minutes, slept
badly* — and it comes back as structured entries across every area it touched,
each one editable next to the words it came from.

Showing the sentence beside the result is the part that matters. Free text
fails silently: the model does not refuse, it gives you a confidently wrong
number. The only correction interface I found that works is putting your own
words next to what was made of them.

You choose which of six areas to track, and the obvious build is one parser per
area. I wrote one engine instead, handling any combination, so adding an area is
data rather than code. I got to that two rewrites late, after the first version
had already worked.
