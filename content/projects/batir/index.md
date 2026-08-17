---
title: "Bâtir"
date: 2026-07-25
projectNo: 9
domain: "saas"
status: "active"
pitch: "Ask a construction question in Arabic, French or English and get an answer that cites the Algerian code it came from."
description: "A tri-lingual AI construction consultant for Algeria — retrieval-grounded answers on seismic rules, concrete mixes and permits, each cited back to the code it came from."
startHereWhy: "retrieval that has to cite a building code, in three languages"
metrics:
  - value: "3 languages"
    label: "Arabic, French and English, answered from one corpus"
  - value: "Cited"
    label: "answers are retrieved from the corpus and point back to the document"
  - value: "5 stages"
    label: "fetch, promote, deploy, re-ingest, verify — before a corpus change is live"
stack: ["Python", "FastAPI", "Next.js", "Postgres + pgvector", "LlamaIndex", "Gemini"]
links:
  live: ""
  repo: ""
lede: |
  A construction consultant for Algeria that answers in the language you asked
  in and shows its working: seismic rules, concrete mixes, rebar spacing,
  permits — each answer cited against the code it came from. Operators tune the
  prompts, the retrieval and the corpus itself without anyone shipping code.
takeaway: "If tuning a model needs a deploy, nobody tunes it — so the prompts, the retrieval settings and the corpus are data, not code."
lessons:
  - "**An ungrounded answer is worse than no answer here.** Someone asking about rebar spacing is going to act on the reply. Every answer is retrieved from an Algerian-codes corpus and cited back to the document, which turns the interesting question from *how good is the model* into *how good is the corpus* — and that second question is one I can actually work on."
  - "**Everything an operator tunes lives in `data/`, not in the code.** Prompts, retrieval parameters and the corpus documents are editable from an admin console. The rule came from watching how these systems really get improved: someone reads a bad answer and wants to change one line of prompt. If that needs a pull request and a deploy, the bad answer stays."
  - "**Publishing a corpus is a release, so it has stages.** Fetch, promote from dev to prod, deploy the markdown, rebuild the index, verify. A retrieval index that quietly regresses is invisible until a user gets a wrong citation, which is exactly the failure the staging step exists to catch."
  - "**One schema, generated both ways.** The frontend's response types are generated from the API's OpenAPI schema instead of being written twice. It is a small discipline that removes an entire category of bug — the one where the backend renamed a field three weeks ago and the UI has been quietly rendering `undefined`."
  - "**Three languages is a retrieval problem, not a translation pass.** Right-to-left is a layout job and a small one. The harder half is that a question can arrive in any of the three languages while the regulation that answers it was written in another."
tags: ["AI", "Python", "RAG", "Algeria"]
---

## The story

Algerian building codes exist, and they are not the problem. The problem is
that finding the clause that applies to your slab means knowing which document
to open, in a corpus written across two languages, and then reading it in a
third if that is the one you think in.

So the question gets asked to a colleague instead, and the answer is whatever
that person remembers. For seismic rules and rebar spacing, "whatever someone
remembers" is a load-bearing part of the process.

> A general model will answer confidently in all three languages and cite
> nothing. That is not an assistant, it is a liability with good grammar.

## The product

You ask in Arabic, French or English and get an answer grounded in the corpus,
with the source it came from attached. Three surfaces sit on one API: the chat
itself, an operator console, and the service underneath.

The console is the part I would build first again. Prompts, retrieval settings,
embedding configuration and the corpus documents are all editable there,
because the real improvement loop for a system like this is someone reading a
bad answer and wanting to change one line — and that loop dies if it needs a
release.

Underneath, the backend is layered so the model provider is a detail: pure
domain types, use-cases that depend on protocols rather than vendors, and the
adapters at the edge. The retrieval sits on Postgres with pgvector rather than
a separate vector service, which is one fewer system to run and one fewer
place for the data to disagree with itself.
