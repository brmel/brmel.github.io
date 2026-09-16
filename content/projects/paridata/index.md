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
takeaway: "A record is only worth reading if it was fixed before the outcome was known — so every gate here enforces that by construction, not by promise."
tags: ["Data Analysis"]
---

We are following an influencer who promotes a betting app and shares football picks, to answer one question: would following them make you money, or lose it?

- Every pick is recorded as it is posted, before the matches are played, with a link back to the post.
- A coupon wins only if every match wins. A cancelled match is taken out of the coupon, not counted as a loss.
- The money is hypothetical: it shows what a fixed stake would have returned. Nobody here placed a bet. 18+.
