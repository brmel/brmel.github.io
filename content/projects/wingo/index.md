---
title: "Wingo"
date: 2026-08-04
projectNo: 2
domain: "mobile"
status: "active"
pitch: "An app for deciding where a group is going, and actually settling it."
description: "An app for deciding where a group is going, and actually settling it."
metrics:
  - value: "3 surfaces"
    label: "app, admin console, marketing site"
  - value: "1 control plane"
    label: "build, deploy, publish, roll back"
  - value: "0"
    label: "launches — the infrastructure is further along than the product"
stack: ["Flutter", "Firebase Functions", "TypeScript", "React", "Firestore"]
links:
  live: ""
lede: |
  A group planning app built around the one thing a chat thread cannot do —
  end the conversation. A squad nominates options, everyone votes in real time,
  and one person locks the winner in.
takeaway: "By the second site, deploying by hand was costing me more time than building the tooling would have."
lessons:
  - "**The control plane was the best decision on the project.** Two web properties, two audiences, two visibility rules, and deploys were hand-run CLI commands. `Operator/` turned build → deploy → publish → rollback into one model across Firebase Hosting, this machine, and any server, with an audit trail and health-check auto-rollback. It cost a fortnight and paid for itself the first time a bad deploy needed reverting."
  - "**Every write goes through Cloud Functions, and that constraint aged well.** No client writes straight to Firestore. It felt heavy while building the first screen and stopped being negotiable the moment real-time voting arrived — the vote rules live in one place, not in every client version anyone has installed."
  - "**Both hosting sites are 404 today, and I only found out writing this page.** Nothing monitors them, because the app never launched and I stopped deploying. A control plane with an audit trail and no uptime check is only half the problem solved."
  - "**Onboarding got built twice.** The first version explained the app; the second shows you the button. Four coach-mark steps replaced a tour nobody finished."
tags: ["Flutter", "Firebase", "Mobile"]
---

## The story

Five friends picking a restaurant will fill a group chat with links, three
thumbs-up reactions and no decision, and two days later nobody has booked
anything. The problem was never a shortage of options.

> It is the locking in, not the voting, that ends the argument. Before that
> moment every message is only an opinion.

## The product

A squad nominates options, everyone votes in real time, and one person locks the
winner in. The app opens on a curated list of what is on in Montréal this week,
so the first screen is useful before you have a single friend on the platform.

Two decisions shaped the rest. **Every write goes through a server function** —
no client touches the database directly — so the voting rules live in one place
rather than in whichever app version someone still has installed. And deploys go
through a small control plane instead of hand-run commands: build, deploy,
publish, roll back, with an audit trail and a health check that reverts a bad
release on its own.

It has not launched. The honest reading of that is on the page below: the
tooling around the product got further than the product did, and the day I
wrote this page I found both of its sites returning 404 because nothing was
watching them.
