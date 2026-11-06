---
title: "How Big Tech Posts on LinkedIn"
date: 2026-11-05
wide: true
description: "A 30-day study of 99 Big Tech companies on LinkedIn: when they post, how often, which formats work, and five lessons from 2,585 posts."
cover:
    image: "cover.jpg"
    alt: "Heatmap of 2,585 LinkedIn posts by weekday and head-office hour, densest on weekdays during office hours"
findings:
  - "The busiest hour of the week is a tie, Tuesday and Wednesday at 2 p.m. in head-office time. 54% of 2,585 posts went out between 9 a.m. and 5 p.m. on a weekday, and 6% on a weekend."
  - "Pages posting under 3 times a week earn about 5× more engagement per follower than pages posting 12 times or more (0.14 against 0.03), and the peak sits at 2 to 3 posts a week (0.42)."
  - "20% of posts went out at exactly :00, against 2% by chance, and 7 companies published 51% of them."
  - "Several images earn double the engagement of video (0.11 against 0.05 per 1,000 followers). Inside one company the gap is smaller."
  - "About 11% of posts are labelled as promoting a product, from labels that are rough."
methods: |-
  From 6 Oct 2026 to 4 Nov 2026, I read the Posts tab of the main LinkedIn page of 99 Big Tech companies across 31 time zones, newest first. I picked the list, so it’s not a random sample. Each post’s publishing time comes from its 64-bit Snowflake URN ID, which stores creation time in milliseconds (urn >> 22), read in the company’s head-office time zone.

  Reposts of other accounts are counted but left out of the timing analysis. Impressions are visible only to page admins, so engagement (reactions, comments and reposts) per 1,000 followers stands in for reach, measured on posts at least 72 hours old. Comparisons between groups of companies show what goes together, not what causes what.

  The list had 100 companies. I dropped Sea because the page I read was the wrong one. The feeds of AMD, Dell Technologies, Qualcomm and HP stopped loading before the window began, so their weekly rates use the days read. An AI agent labelled each post’s topic and whether it sells a product. In a spot check of 45 posts, many labels were wrong, so those charts are rough.
---

{{< reportframe src="reports/how-big-tech-posts.html" title="How Big Tech Posts on LinkedIn report" >}}