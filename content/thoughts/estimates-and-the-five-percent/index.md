---
title: "Why Deadlines Slip, Mine Included"
date: 2026-08-09
tags: ["Data Analysis", "Engineering"]
summary: "Hydro-Québec's restoration times were right one time in twenty. I recognised the failure immediately, because I make the same one."
---

For fifty-six days I recorded every power outage in Québec, once a minute. Not for a client, not for work — I wanted to know one thing.

When Hydro-Québec tells you the power is back at 4 p.m., how often is it back at 4 p.m.?

The answer is **five percent**. Across 16,561 outages and 7,870 readings, the restoration actually landed within an hour of the announced time about one time in twenty. The [full analysis](/tech/hydro-quebec-outage-analysis/) has the regional breakdown and the charts.

My first reaction was the obvious one. Five percent is terrible. Somebody should fix that.

My second reaction took longer, and it is the reason I am writing this instead of leaving the number in a report.

I have given that estimate. Not about power lines — about a feature, a fix, a release. Someone asks when it will be done, and I say Thursday. I am not lying. I believe Thursday when I say it. And then a dependency moves, or the bug is not the bug, and Thursday becomes the following Tuesday.

The utility is not being dishonest either. It is doing what I do: estimating from the information available at the moment of asking, in front of someone who wants a number and will not accept "I don't know yet."

That is the part worth sitting with. **The bad estimate is not a character flaw. It is a structural consequence of being asked too early.** A crew dispatched to a line does not know what it will find until it arrives. Neither do I, most of the time.

What I took from the data is not that estimates are useless. It is which estimate is worth trusting.

The one given at the moment the ticket opens carries almost no information — that is the five percent. The one given after somebody has actually looked at the problem is a different object entirely, built from evidence instead of hope. Same sentence, same confident tone, completely different thing.

So now I try to say which one I am giving. "Thursday, and I have not opened it yet" is a weaker-sounding answer than "Thursday." It is also the honest one, and it costs nothing to say.

Two months of data to arrive at something I could have been told in a sentence. But I would not have believed the sentence. I believed the five percent, because I collected it myself.

That is usually how it goes.
