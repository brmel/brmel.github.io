---
title: "Domia"
date: 2026-07-26
projectNo: 7
status: "active"
pitch: "An agent that tests applications by reading the screen as a screen reader does, and using them the way a person would."
description: "An agent that tests applications by reading the screen as a screen reader does, and using them the way a person would."
metrics:
  - value: "~200 ms"
    label: "for 20 verified findings, before any AI model is involved"
  - value: "1 loop"
    label: "drives web and desktop alike, with no scripted steps"
  - value: "40"
    label: "design decisions recorded, each with the problem it fixed"
stack: ["TypeScript", "Playwright", "Electron", "AI SDK", "MCP", "SQLite"]
links:
  repo: "https://github.com/brmel/Domia"
lede: |
  Domia works from the accessibility tree, acts on what it finds, checks
  what changed, and keeps going until the task is done or it has a question.
cover:
  image: "cover.jpg"
  alt: "Illustration: a web page beside its accessibility tree, with the matching button highlighted and clicked"
---

## The story

An end-to-end test rarely fails because the product is broken. It fails because
a button moved, a class was renamed, or a page took 300ms longer than it used
to. So I watched tests get narrower until they checked almost nothing, or
watched someone spend a day a week keeping them alive.

A test written against selectors has no idea what it's
looking at. It knows there is an element at `.btn-primary`. It doesn't know
there's a button that says *Continue*. A person testing the same page never has
that problem, because a person reads the screen.

## The product

You ask Domia for something in plain language and it drives the application
until it's done. It reads the accessibility tree (the same structure a screen
reader uses), picks an action, acts on what is really there, checks what
changed, and decides again. One loop, no recorded steps, and the same loop for a
web page or an Electron app. I built it as a TypeScript monorepo: an agent layer
over any LLM provider, a Playwright tool layer, SQLite persistence, a tracing
system, an Electron desktop app and a CLI, all behind one API.

Calling the model is the expensive part, so it happens last. A deterministic pass over
a site's files, headers and HTML settles whatever it can in pure functions:
twenty findings in about a fifth of a second, with no model and no browser at
all. The agent only picks up what is left. Every run is recorded as a tree and
replays from its own tape without calling the model again.

## What it prints

The sweep runs on a clean checkout with no API key at all:

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

Every finding carries the rule that produced it and the fix, sized.

It's a beta and it says so. What's missing is the ordinary part: entering a
key from the desktop UI, proper empty states, and signed builds.
