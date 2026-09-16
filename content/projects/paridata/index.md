---
title: "PariData"
date: 2026-09-15
layout: "tracker"
projectNo: 11
domain: "data"
status: "active"
pitch: "A public football tipster posts his picks. This records every one of them, flat-staked, and grades it against what actually happened."
description: "Every pick a public football tipster posts, recorded flat-staked and graded against what actually happened. Nothing inferred, every row sourced."
stack: ["Hugo", "JSON", "Python"]
lede: |
  Tipsters publish winners. Nobody publishes the running total — the only number
  that settles the question. Every ticket is recorded as it is posted, staked one
  flat unit, and the balance says what it says.
takeaway: "A record is only worth reading if it was fixed before the outcome was known — so every gate here enforces that by construction, not by promise."
lessons:
  - "**A voided leg silently inflates every coupon it touches.** A postponed match returns its share and its odds drop to 1.00, so the ticket published at 3.38 actually paid 2.70. The maths lives in one partial because it was wrong once, in one place."
  - "**Requiring the source URL in the schema beats intending to add one.** A row nobody can check is worth less than no row, and good intentions survive about three weeks. The gate refuses to publish a ticket without it."
  - "**The cheapest cross-check caught the most.** Total odds must equal the product of the legs within 0.02 — four lines that stop a misread digit before it reaches the balance."
tags: ["Data Analysis"]
---

## What is recorded

One ticket per published pick, entered by hand from the post. A single bet is a
ticket with one leg; a coupon is several, and each leg settles on its own —
a coupon dies on its worst one.

Every ticket is staked one flat unit. Flat staking is the only plan that measures
the tipster rather than the staker.

## How it settles

Pending until the matches finish, then won, lost, or void. A voided leg returns
its share and its odds divide out of the return. A result that cannot be verified
stays pending rather than being guessed into a column.

## What this is not

Not advice, not a system, not an accusation. The money column is hypothetical: it
shows what a flat stake would have returned. Nobody here placed a bet.

Gambling is 18+.
