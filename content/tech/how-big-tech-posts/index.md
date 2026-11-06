---
title: "How Big Tech Posts on LinkedIn"
date: 2026-11-05
description: "Thirty days of LinkedIn posts from 99 tech companies: when they publish, and whether the hour, the frequency or the format moves engagement."
cover:
    image: "cover.jpg"
    alt: "Heatmap of 2,585 LinkedIn posts by weekday and head-office hour, densest on weekdays during office hours"
findings:
  - "54% of 2,585 posts went out on a weekday between 9 a.m. and 5 p.m. in head-office time, and 6% on a weekend. The busiest hour is a tie, Tuesday and Wednesday at 2 p.m., with 48 posts each."
  - "The clock barely moves engagement. Against the company’s own median post, the five parts of the day run from 0.97 to 1.02, and the days of the week from 0.89 to 1.11."
  - "20% of posts went out at exactly :00, where chance would give 2%. 7 companies published 51% of them, and those posts earn 0.97 times the company’s usual."
  - "Engagement per 1,000 followers follows page size (rank correlation −0.78) far more than frequency (−0.32). The 12 pages with 12 or more posts a week sit at 0.03, against 0.14 under 3 a week, but a post under 3 hours after the last one still earns 1.01 times the company’s usual."
  - "Several images earn 1.35 times the company’s usual post, and document carousels 0.75. Video, the most common format at 37%, earns 1.00."
methods: |-
  From 6 Oct 2026 to 4 Nov 2026, an agent driving my own signed-in Chrome read the Posts tab of the main LinkedIn page of 99 tech companies across 31 head-office time zones, one page at a time. I picked the list, so it’s not a random sample, and it includes Zebra, where I work, and Matrox Video. A post’s time comes from its ID: the first 41 bits of a LinkedIn post ID are its creation time in milliseconds (`id >> 22`). 2,585 posts count, and the 338 plain reposts of other accounts are left out of every figure, because a repost shows the original post’s time.

  Impressions are visible only to a page’s admins, so engagement (reactions, comments and reposts) stands in for reach, read once and only on posts at least 72 hours old. Follower counts are the rounded figures the page shows. Comparing a post with its own company’s median takes out page size, not what the post is about, and it needs five such posts, which leaves 2,303 posts from 89 companies. It’s one 30-day window and no experiment, so none of this shows cause.

  The list had 100 companies. I dropped Sea because the page I read was the wrong one, with 54 followers. The feeds of AMD, Dell Technologies, Qualcomm and HP stopped loading before the window began, so their rates use the days read. An agent also labelled each post’s topic and whether it sold a product. In a random sample of 45 I checked, about six in ten topics were wrong, so no label is used here.
---

{{< reportframe src="reports/how-big-tech-posts.html" title="How Big Tech Posts on LinkedIn report" >}}