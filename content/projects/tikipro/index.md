---
title: "TikiPro"
date: 2025-08-04
projectNo: 1
domain: "saas"
status: "shipped"
pitch: "Gives a small clinic a numbered queue on a screen, so patients stop asking who is next."
description: "Gives a small clinic a numbered queue on a screen, so patients stop asking who is next."
metrics:
  - value: "1 PC"
    label: "runs reception, the waiting-room board and every doctor"
  - value: "3 languages"
    label: "French, Arabic and English, switched mid-sentence"
  - value: "Offline"
    label: "Ed25519 licences verified locally, no phone-home"
stack: ["Electron", "TypeScript", "Firebase", "Ed25519", "Turborepo"]
links:
  live: "https://tikipro.web.app"
lede: |
  Clinic queue management that runs entirely on the one PC already sitting at
  reception: the desk view, the waiting-room screen and each doctor's queue, with
  no server, no per-seat licence and no patient record leaving the building.
lessons:
  - "**The installer is the product for the first ten minutes.** The app refuses to start without a licence file, and the installer is not code-signed, so Windows SmartScreen blocks it. Two dead ends before anyone sees a feature. I now write the onboarding email before the release, because every warning it has to explain is a design failure I could have removed."
  - "**Manual beats automatic when the volume is low.** There is no automated licensing email anywhere. A request writes to Firestore, a function sends me a Telegram message, and I reply by hand. Building the automated flow would have taken a week and served maybe one clinic a month."
  - "**Rate limits need names.** Installer downloads are capped at 3 a day and 10 a week — across *all* visitors, not per person. Obvious in the code, invisible from outside: onboarding several clinics in one afternoon hits the cap and looks like an outage."
  - "**Offline licensing removed a whole class of support calls.** Ed25519-signed licence keys are verified locally with no phone-home, so a clinic with a dead internet connection still opens the app. Clinics lose connectivity often enough that this stopped being optional."
tags: ["Desktop", "TypeScript", "Firebase"]
---

## The story

A clinic's waiting room runs on shouting. Someone calls a name, half the room
does not hear it, and whoever stepped outside loses their turn. The cost nobody
puts in a feature list is the staff time: the receptionist spends the day
re-explaining the order to people certain they were skipped, and every one of
those conversations happens while somebody else waits.

The software that fixes this is built for hospitals — a server, a network, a
per-seat licence, an IT contact. The clinic I built this for has three doctors,
one PC at reception, and a television on the wall.

## The product

I made reception, the waiting-room board and each doctor's queue three views of
one application running on that single machine. The board is only a browser page
on the second screen, so there is no second machine and no second licence, and
patients can scan a QR code to follow the same live list on their phone.

Around it I put everything a stranger needs to buy it and run it alone:
offline-verified licence keys, an auto-update feed, an admin portal, and an audit
log on every operation that touches patient data. Nothing phones home, because a
clinic with a dead connection still has to open the door in the morning.
