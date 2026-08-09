---
title: "Farkad"
date: 2026-08-01
projectNo: 4
domain: "mobile"
status: "active"
pitch: "Say one sentence about your day and a two-pass agent pipeline files it across every area it touched."
stack: ["Flutter", "Python", "Firebase Functions", "Multi-agent", "Dart"]
links:
  live: "https://farkad.web.app"
lede: |
  Every habit tracker asks you to become a data-entry clerk for your own life —
  six taps for breakfast, a separate screen for water, a sleep slider you move
  without believing it — so after nine days you stop. The information was never
  the hard part: you could say the whole day in one breath and a person would
  understand every piece of it. Farkad makes that sentence the entire interface,
  turning "two eggs, a big glass of water, walked forty minutes, slept badly"
  into structured, editable entries across every area it touched.
takeaway: "One engine that serves every user configuration beats six engines that each serve one — but only if you decide that before the second pillar ships."
lessons:
  - "**A decisions log with expiry dates outlives a design doc.** `DECISIONS.md` records every locked decision *and what no longer holds*. It exists because a navigation tab drifted three times in one session, twice from reasoning off a backlog of screens that were still only drawn. There is now a test that reads the spec table and fails when the code disagrees."
  - "**Cutting the brief was the work.** Coach, widgets, Siri and Assistant capture, Back Tap, push, share cards, custom pillars, image capture — all closed **unbuilt** on the same day, each with a written reason. The version that ships does one loop: speak, structure, correct, see. Everything that didn't serve that loop went."
  - "**One engine, every configuration.** Users pick which of six pillars they track, and the naive design is a parser per pillar. Instead one pipeline handles any combination, so adding a pillar is data rather than code. Getting there meant rewriting the first two passes after they had already worked."
  - "**Free-text input means the failure mode is silent.** The model doesn't refuse — it produces a confidently wrong number. Every generated field stays editable next to the sentence it came from, because the only workable correction UI is showing your own words back to you."
tags: ["Flutter", "Python", "AI", "Firebase", "Mobile"]
---

## The story

You speak once, in whatever language you were thinking in, and a two-pass agent
pipeline works out what you touched, how much, and when, then turns it into
structured entries you can edit.

The name is فرقد — *Pherkad*, the guide star of Ursa Minor. The second star you
find after the pole star, and the one that tells you you're looking at the right
part of the sky.

## The product

Four tabs and one record button that floats above all of them, because the
microphone is not a destination. Home shows today against your targets. Timeline
is every day you've logged. Trends draws each pillar in the shape that pillar
asks for. Profile owns the settings that change what the engine looks for.

The demo on the landing page is the real engine, not a mockup — the sentence in
the gallery above was typed into it and those cards are what came back. Water
300 ml, two eggs at 160 kcal with a slice of rye, sleep poor at 03:00, a 40-minute
walk to work. It also names what it *didn't* find: nothing about supplements or
recovery in that sentence.

Underneath:

- **A Python multi-agent backend on Firebase Functions v2** running two passes —
  one to read meaning, one to resolve amounts and units.
- **One engine for every user configuration.** Six pillars, any combination
  enabled, one pipeline. Adding a pillar is data, not a new parser.
- **A shared contract layer** generated into both Dart and TypeScript, so the
  client and the backend cannot disagree about a field name.
- **Four locales, prerendered, zero runtime JavaScript** on the landing page —
  including a fully mirrored Arabic build, not a translated one.

The app is in build. The engine is live and you can use it today, which is an
unusual order to ship in and was deliberate: the risky half is the one that
needed real sentences from real people first.
