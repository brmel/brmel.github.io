---
title: "Domia"
date: 2026-07-26
projectNo: 7
domain: "infra"
status: "active"
pitch: "An agent that tests applications by reading the accessibility tree and driving them the way a person would."
description: "An agent that tests applications by reading the accessibility tree and driving them the way a person would."
metrics:
  - value: "~200 ms"
    label: "for 20 verified findings, before a model is involved"
  - value: "1 loop"
    label: "drives web and desktop alike, with no scripted steps"
  - value: "40"
    label: "design decisions recorded, each with the problem it fixed"
stack: ["TypeScript", "Playwright", "Electron", "AI SDK", "MCP", "SQLite"]
links:
  live: ""
  repo: "https://github.com/brmel/Domia"
lede: |
  An agent that tests an application by reading the screen instead of the source.
  It works from the accessibility tree, acts on what is actually there, checks
  what changed, and keeps going until the task is done or it has a question.
lessons:
  - "**The provider defaults were the bug.** With a 2,661-character persona prompt, 32 tools and a 6,337-character page snapshot, Gemini started returning empty responses — no text, no tool call — and the loop read that as a finished task. The model thinking budget was consuming the output budget before it reached the answer. The fix is one line of provider config plus a retry, in the adapter where provider quirks belong."
  - "**The deterministic pass runs first.** Twenty verified findings on a real site in 215 ms, in pure functions, with no model and no browser. The agent is only spent on what that pass leaves open, and the tool can be demonstrated with no API key at all."
  - "**Two false positives were worth more than the findings.** The first audit of a real site reported `Server: AmazonS3` as a version leak because the check accepted any digit, and called a 456-byte document uncompressed. Both are regression tests now, and the fixture suite asserts that a clean origin reports exactly one thing. When the deliverable is trust, a false positive costs more than a missed finding."
  - "**Recording everything by default cost a third of every session.** Video and trace capture ran on every run: about 1.0s of a 1.7s startup, and video was the largest thing on disk. Video is off by default now, and a one-turn run went from 2.8s to 2.0s with half the bytes."
  - "**I rewrote version one deliberately.** The Python agent the [article](/tech/ai-agents-software-testing-domia/) describes became a TypeScript monorepo. I audited the old version feature by feature, wrote down what had no equivalent yet, closed that list, and only then deleted it."
tags: ["AI", "TypeScript", "Testing"]
---

## The story

An end-to-end test rarely fails because the product is broken. It fails because
a button moved, a class was renamed, or a page took 300ms longer than it used
to. So I watched tests get narrower until they checked almost nothing, or
watched someone spend a day a week keeping them alive.

The reason is that a test written against selectors has no idea what it is
looking at. It knows there is an element at `.btn-primary`. It does not know
there is a button that says *Continue*. A person testing the same page never has
that problem, because a person reads the screen.

## The product

You ask Domia for something in plain language and it drives the application
until it is done. It reads the accessibility tree — the same structure a screen
reader uses — picks an action, acts on what is really there, checks what
changed, and decides again. One loop, no recorded steps, and the same loop for a
web page or an Electron app. I built it as a TypeScript monorepo: an agent layer
over any LLM provider, a Playwright tool layer, SQLite persistence, a tracing
system, an Electron desktop app and a CLI, all behind one API.

Judgement is the expensive part, so I spend it last. A deterministic pass over
an origin's files, headers and HTML settles whatever it can in pure functions:
twenty findings in about a fifth of a second, with no model and no browser at
all. The agent only picks up what is left. Every run is recorded as a tree and
replays from its own tape without calling the model again.

## What it prints

The deterministic pass needs no model and no browser, so it runs on a clean
checkout with no API key at all:

```console
$ domia audit https://example.com --sweep-only

▶ sweep: https://example.com  (deterministic pass — no model)

  11 requests in 215ms → 20 findings

  ▲ serious  security       No Content-Security-Policy
    verified · security.csp-missing · fix (S): Ship a CSP, starting in report-only mode.
  ▲ serious  security       No HSTS
    verified · security.hsts-missing · fix (S): Send HSTS with a long max-age once https is confirmed.
  ● moderate files          No robots.txt
    verified · files.robots-txt · fix (S): Publish /robots.txt.
  ● moderate seo            No meta description
    verified · seo.description-missing · fix (S): Add a meta description of 120–160 characters.
  · minor    agentic        No /llms.txt
    verified · agentic.llms-txt · fix (S): Publish /llms.txt.
  …
```

Every finding carries the rule that produced it and the fix, sized. The agent is
only spent on what this pass leaves open.

It is a beta and it says so. What is missing is the ordinary part: entering a
key from the desktop UI, proper empty states, and signed builds.
