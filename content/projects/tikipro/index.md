---
title: "TikiPro"
featured: 6
date: 2025-08-04
projectNo: 1
status: "shipped"
pitch: "A numbered queue on a waiting-room screen for small clinics, so patients stop asking who is next."
description: "A numbered queue on a waiting-room screen for small clinics, so patients stop asking who is next."
metrics:
  - value: "1 PC"
    label: "runs reception, the waiting-room board and every doctor’s queue"
  - value: "3 languages"
    label: "French, Arabic and English, switched mid-sentence"
stack: ["Electron", "TypeScript", "Firebase", "Ed25519", "Turborepo"]
links:
  live: "https://tikipro.web.app"
lede: |
  Clinic queue management that runs entirely on the one PC already sitting at
  reception: the desk view, the waiting-room screen and each doctor’s queue, with
  no server, no per-seat licence and no patient record leaving the building.
---

## The story

A clinic's waiting room runs on shouting. Someone calls a name, half the room
doesn't hear it, and whoever stepped outside loses their turn. The cost nobody
puts in a feature list is the staff time: the receptionist spends the day
re-explaining the order to people certain they were skipped, and every one of
those conversations happens while somebody else waits.

The software that fixes this is built for hospitals: a server, a network, a
per-seat licence, an IT contact. The clinic I built this for has three doctors,
one PC at reception, and a television on the wall.

## The product

Everything runs as one application on that single machine. The board is only a browser page
on the second screen, so there is no second machine and no second licence, and
patients can scan a QR code to follow the same live list on their phone.

Around it I put everything a stranger needs to buy it and run it alone:
offline-verified licence keys, an auto-update feed, an admin portal, and an audit
log on every operation that touches patient data. Nothing phones home, because a
clinic with a dead connection still has to open the door in the morning.
