---
title: "Bâtir"
date: 2026-07-25
projectNo: 9
status: "active"
pitch: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
description: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
stack: ["Python", "FastAPI", "Next.js", "Postgres + pgvector", "LlamaIndex", "Gemini"]
lede: |
  It answers questions on seismic rules, concrete mixes, rebar spacing and
  permits. Operators change the prompts, the retrieval settings and the corpus
  itself from an admin console, with no deploy.
cover:
  image: "cover.jpg"
  alt: "Illustration: a building frame under construction, a tower crane and a speech bubble with a cited answer"
---

## The story

Algerian building codes exist. But finding the clause that covers your slab
means knowing which document to open, in a corpus written across two languages,
and then reading it in a third if that is the one you think in.

So people ask a colleague instead, and the answer is whatever that person
remembers. For seismic rules and rebar spacing, "whatever someone remembers" is
holding up the building.

## The product

The console is the part I'd build first if I started again, because the real
improvement loop is someone reading a bad answer and wanting to change one
line, and that loop dies if it needs a release.

Underneath, I layered the backend so the model provider is a detail: pure domain
types, use-cases that depend on protocols rather than vendors, and the adapters
at the edge. I put retrieval on Postgres with pgvector rather than a separate
vector service, which leaves one fewer system to run.
