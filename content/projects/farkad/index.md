---
title: "Farkad"
date: 2026-08-01
projectNo: 4
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
  about your day (*two eggs, a big glass of water, walked forty minutes, slept
  badly*) and a pipeline of AI agents files it under every area it mentions, each
  entry editable next to the words it came from.
---

## The story

Every habit tracker asks you to become a data-entry clerk for your own life. Six
taps for breakfast, a separate screen for water, a sleep slider you move without
believing it. After about nine days you stop, and the app has learned nothing
about you it couldn't have simply asked.
