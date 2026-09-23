---
title: "Bâtir"
date: 2026-07-25
projectNo: 9
domain: "saas"
status: "active"
pitch: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
description: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
metrics:
  - value: "3 languages"
    label: "Arabic, French and English, answered from one corpus"
  - value: "Cited"
    label: "every answer points back to the document it came from"
  - value: "5 stages"
    label: "fetch, promote, deploy, re-ingest, verify"
stack: ["Python", "FastAPI", "Next.js", "Postgres + pgvector", "LlamaIndex", "Gemini"]
links:
  live: ""
  repo: ""
lede: |
  A construction assistant for Algeria. It answers in the language you asked in
  — Arabic, French or English — on seismic rules, concrete mixes, rebar spacing
  and permits, and cites the code each answer came from. Operators change the
  prompts, the retrieval settings and the corpus itself from an admin console,
  with no deploy.
lessons:
  - "**Every answer is retrieved and cited.** Someone asking about rebar spacing will act on the reply, so nothing is generated ungrounded. Each answer comes from an Algerian-codes corpus and links back to the document it came from, which makes corpus quality the thing to work on rather than model quality."
  - "**Everything an operator tunes lives in `data/`, not in the code.** Prompts, retrieval parameters and corpus documents are all editable from an admin console. If fixing one line of a prompt needs a pull request and a deploy, the bad answer stays in production."
  - "**Publishing the corpus is a release, so it has stages.** Fetch, promote dev to prod, deploy the markdown, rebuild the index, verify. A retrieval index can regress silently, and the staging step is what catches it before a user gets a wrong citation."
  - "**One schema, generated both ways.** The frontend response types are generated from the API OpenAPI schema instead of written twice. It removes the bug where the backend renames a field and the UI renders `undefined` for three weeks."
  - "**Three languages is a retrieval problem, not a translation pass.** Right-to-left layout is the small half. The hard half is that a question arrives in one language while the regulation that answers it was written in another."
tags: ["AI", "Python", "RAG", "Algeria"]
---

## The story

Algerian building codes exist, and they are not the problem. The problem is that
finding the clause covering your slab means knowing which document to open, in a
corpus written across two languages, and then reading it in a third if that is
the one you think in.

So people ask a colleague instead, and the answer is whatever that person
remembers. For seismic rules and rebar spacing, "whatever someone remembers" is
holding up the building.

## The product

You ask in Arabic, French or English and get an answer grounded in the corpus,
with the source attached. I put three surfaces on one API: the chat itself, an
operator console, and the service underneath.

The console is the part I would build first if I started again. Prompts,
retrieval settings, embedding configuration and the corpus documents are all
editable there, because the real improvement loop is someone reading a bad
answer and wanting to change one line — and that loop dies if it needs a
release.

Underneath, I layered the backend so the model provider is a detail: pure domain
types, use-cases that depend on protocols rather than vendors, and the adapters
at the edge. I put retrieval on Postgres with pgvector rather than a separate
vector service, which leaves one fewer system to run and one fewer place for the
data to disagree with itself.
