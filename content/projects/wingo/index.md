---
title: "Wingo"
date: 2026-08-04
projectNo: 2
domain: "mobile"
status: "active"
pitch: "A small group decides where to go — nominate options, vote in real time, lock in a winner."
stack: ["Flutter", "Firebase Functions", "TypeScript", "React", "Firestore"]
links:
  live: ""
lede: |
  Five friends trying to pick a restaurant will fill a group chat with links,
  three thumbs-up reactions and no decision, and two days later nobody booked
  anything. The problem was never a shortage of options — it is that no message
  in a chat is ever the moment the group agreed. Wingo makes that moment
  explicit: a squad nominates options, everyone votes in real time, and one of
  them locks in, so the thread afterwards is about logistics instead of whether
  it is happening.
takeaway: "Build the deploy tooling before you need it — the second web property is when hand-run commands start costing real time."
lessons:
  - "**The control plane was the best decision on the project.** Two web properties, two audiences, two visibility rules, and deploys were hand-run CLI commands. `Operator/` turned build → deploy → publish → rollback into one model across Firebase Hosting, this machine, and any server, with an audit trail and health-check auto-rollback. It cost a fortnight and paid for itself the first time a bad deploy needed reverting."
  - "**Every write goes through Cloud Functions, and that constraint aged well.** No client writes straight to Firestore. It felt heavy while building the first screen and stopped being negotiable the moment real-time voting arrived — the vote rules live in one place, not in every client version anyone has installed."
  - "**Both hosting sites are 404 today, and I only found out writing this page.** Nothing monitors them, because the app never launched and I stopped deploying. A control plane with an audit trail and no uptime check is only half the problem solved."
  - "**Onboarding got built twice.** The first version explained the app; the second shows you the button. Four coach-mark steps replaced a tour nobody finished."
tags: ["Flutter", "Firebase", "Mobile"]
---

## The story

The moment matters more than the mechanism. A squad nominates options, everyone
votes in real time, and one of them locks in as the plan — and it is the locking
in, not the voting, that ends the argument. Before that moment every message is
just an opinion; after it, the thread is about logistics.

## The product

Three surfaces off one Firestore backend: a Flutter app for iOS and Android, a
Flutter-web admin console for curating public events, and a React marketing site
with share-link previews.

The app opens on **Discover** — what's on in Montréal this week, curated rather
than scraped, so the first screen is useful before you have a single friend on
the platform. Pick an event, choose which squad you're planning with, and it
becomes a plan the group votes on.

Two decisions shaped everything else:

- **Every write goes through Cloud Functions.** No client writes to Firestore
  directly. Voting rules, plan state, and membership are enforced server-side, so
  an old app version can't corrupt a live vote.
- **A local control plane, not a deploy script.** `Operator/` runs on localhost
  and manages build → deploy → publish → rollback for both web properties across
  heterogeneous targets — Firebase Hosting, this machine, or any server, bare or
  Docker — with the public site world-readable and the admin console gated to
  contributors, enforced by config validation rather than by remembering.

The app is pre-launch. The infrastructure around it is further along than the
launch is, which is its own lesson.
