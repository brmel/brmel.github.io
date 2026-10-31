---
title: "PariData"
date: 2026-09-15
layout: "tracker"
projectNo: 11
status: "active"
pitch: "A public football tipster posts their picks. I record every one of them at a fixed stake and grade it against what actually happened."
description: "Every pick a public football tipster posts, recorded at a fixed stake and graded against what actually happened. Nothing inferred, kept anonymous."
stack: ["Hugo", "JSON", "Python"]
cover:
  image: "cover.jpg"
  alt: "Illustration: a football pitch with a rising line of results drawn across it"
---

I follow an influencer who promotes a betting app and posts football picks, to answer one question: would following them make you money, or lose it?

- I store each pick as data when it is posted, and it is checked automatically before the page is published. The influencer and the app stay anonymous.
- A coupon wins only if every match in it wins. A cancelled match is removed from the coupon.
- All amounts are simulated. No real bet was placed. 18+.
