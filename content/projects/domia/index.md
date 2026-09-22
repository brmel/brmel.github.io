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
  - "**The provider's defaults were the bug.** With the full setup — a 2,661-character persona prompt, 32 tools and a 6,337-character page snapshot — the model started returning empty responses: no text, no tool call. Intermittent on small pages, consistent on large ones. Gemini's *thinking* was consuming the output budget before it reached the answer, and the loop was reading the empty response as a finished task. The fix is one line of provider config plus a retry, and it lives in the adapter where provider quirks belong — but it cost days, because everything I could see said my prompt was wrong."
  - "**The cheap pass has to run first.** Twenty verified findings on a real site in 215ms, in pure functions, with no model and no browser. The agent is only spent on what the deterministic pass leaves open. It also means the thing can be demonstrated with no API key at all, which I did not plan and would not give up."
  - "**Two false positives taught me more than the findings did.** The first audit of a real site reported `Server: AmazonS3` as a version leak because the check accepted any digit, and called a 456-byte document uncompressed. Both are regression tests now, and the fixture suite asserts a clean origin reports *exactly one* thing. When the deliverable is trust, a false positive costs more than a missed finding."
  - "**Recording everything by default was costing a third of every session.** Video and trace capture both ran on every run: about 1.0s of a 1.7s session startup, and video was the largest thing on disk. Video is off by default now and a one-turn run went from 2.8s to 2.0s with half the bytes. I had never measured it because it had always been on."
  - "**I deleted version one on purpose.** The Python agent that the [article](/tech/ai-agents-software-testing-domia/) describes was rebuilt as a TypeScript monorepo. I audited the old version feature by feature first, wrote down what still had no equivalent, closed that list, and only then deleted it — which is the only reason I know nothing was lost in the move."
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
