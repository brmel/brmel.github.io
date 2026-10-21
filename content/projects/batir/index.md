---
title: "Bâtir"
date: 2026-07-25
projectNo: 9
status: "active"
pitch: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
description: "Answers Algerian construction questions in Arabic, French or English, and shows the building rule behind each answer."
metrics:
  - value: "3 languages"
    label: "Arabic, French and English, answered from the same documents"
  - value: "5 stages"
    label: "fetch, promote, deploy, re-ingest, verify"
stack: ["Python", "FastAPI", "Next.js", "Postgres + pgvector", "LlamaIndex", "Gemini"]
lede: |
  A construction assistant for Algeria. It answers questions on seismic rules,
  concrete mixes, rebar spacing and permits in the language you asked in (Arabic,
  French or English), and cites the building code each answer came from.
  Operators change the prompts, the retrieval settings and the corpus itself from
  an admin console, with no deploy.
lessons:
  - "**Every answer is retrieved and cited.** Someone asking about rebar spacing will act on the reply, so nothing is generated without a source. Each answer comes from an Algerian-codes corpus and links back to the document it came from, which makes corpus quality the thing to work on rather than model quality."
  - "**I publish the corpus in stages, like a release.** Fetch, promote dev to prod, deploy the markdown, rebuild the index, verify. A retrieval index can regress silently, and the staging step is what catches it before a user gets a wrong citation."
  - "**One schema for both sides.** The frontend response types are generated from the API’s OpenAPI schema instead of written twice. It removes the bug where the backend renames a field and the UI renders `undefined` for three weeks."
  - "**Three languages is a retrieval problem, not a translation pass.** Right-to-left layout is the small half. The hard half is that a question arrives in one language while the regulation that answers it was written in another."
tags: ["AI", "Python", "RAG", "Algeria"]
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

You ask in Arabic, French or English and get an answer drawn from those codes,
with the source attached. I put three surfaces on one API: the chat itself, an
operator console, and the service underneath.

The console is the part I'd build first if I started again. Prompts,
retrieval settings, embedding configuration and the corpus documents are all
editable there, because the real improvement loop is someone reading a bad
answer and wanting to change one line, and that loop dies if it needs a
release.

Underneath, I layered the backend so the model provider is a detail: pure domain
types, use-cases that depend on protocols rather than vendors, and the adapters
at the edge. I put retrieval on Postgres with pgvector rather than a separate
vector service, which leaves one fewer system to run and one fewer place for the
data to disagree with itself.
