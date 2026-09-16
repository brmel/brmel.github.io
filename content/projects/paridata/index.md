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

PariData is a data project. It follows an influencer who promotes a betting app and shares football picks, to answer one question: would following them make you money, or lose it?

- Each pick is stored as data with a link to the original post, and checked automatically before the page is published.
- A coupon wins only if every match in it wins. A cancelled match is removed from the coupon.
- All amounts are simulated with a fixed stake. No real bet was placed. 18+.
