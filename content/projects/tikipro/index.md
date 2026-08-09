---
title: "TikiPro"
date: 2026-08-04
projectNo: 1
domain: "saas"
status: "shipped"
pitch: "Clinic ticketing and queue management that runs on one PC, with no cloud dependency for patient data."
stack: ["Electron", "TypeScript", "Firebase", "Ed25519", "Turborepo"]
links:
  live: "https://tikipro.web.app"
takeaway: "Shipping to non-technical users means the install path is the product — everything before first launch is where it fails."
lessons:
  - "**The installer is the product for the first ten minutes.** The app refuses to start without a licence file, and the installer is not code-signed, so Windows SmartScreen blocks it. Two dead ends before anyone sees a feature. I now write the onboarding email before the release, because every warning it has to explain is a design failure I could have removed."
  - "**Manual beats automatic when the volume is low.** There is no automated licensing email anywhere. A request writes to Firestore, a function sends me a Telegram message, and I reply by hand. Building the automated flow would have taken a week and served maybe one clinic a month."
  - "**Rate limits need names.** Installer downloads are capped at 3 a day and 10 a week — across *all* visitors, not per person. Obvious in the code, invisible from outside: onboarding several clinics in one afternoon hits the cap and looks like an outage."
  - "**Offline licensing removed a whole class of support calls.** Ed25519-signed licence keys are verified locally with no phone-home, so a clinic with a dead internet connection still opens the app. Clinics lose connectivity often enough that this stopped being optional."
tags: ["Electron", "TypeScript", "Firebase", "Desktop", "Licensing"]
---

## The story

A clinic waiting room runs on shouting. Someone at reception calls a name, half
the room doesn't hear it, and the person who stepped out to take a call loses
their turn. The staff spend the day re-explaining the order to people who are
convinced they were skipped.

The software that fixes this exists, and it is priced and architected for
hospitals: a server, a network, a per-seat licence, an IT contact. A three-doctor
clinic has none of those things. It has one PC at reception and a television on
the wall.

TikiPro is built for exactly that machine. Reception issues numbered tickets from
a desk view. The waiting room sees its position on a second screen. Each doctor
manages their own queue and writes consultation notes. All of it on the same
computer, and patient data never leaves it.

## The product

The reception desk, the waiting-room board, and the doctor's queue are three
views of one local application. The board is a browser page on a second monitor —
no second machine, no second licence. Patients can also scan a QR code and watch
the same live list on their phone.

Around that sit the parts that make it something a stranger can actually buy and
run: an offline-signed licence system, an auto-update feed, a marketing site with
a request form, and an admin portal for licences and leads. Three languages —
French, Arabic and English — because the clinics it was built for switch between
them mid-sentence.

The pieces worth naming:

- **Queue mechanics that match how rooms actually behave.** Priority, a status
  state machine, wait-time estimates, and the ability to call any waiting or late
  visitor out of order — because the person who stepped out does come back.
- **Ed25519 offline licences.** Signed keys verified locally, no phone-home. Two
  tiers gate optional features; a trial is just a premium licence with a 30-day
  expiry.
- **Backups that assume nobody will run them.** Daily automatic, with
  grandfather-father-son retention and in-app restore.
- **An audit log on every patient data operation**, because this is medical data
  on a machine in a room full of people.

The CLI and the HTTP API share the same use-case layer as the UI, so anything the
app can do is scriptable — which is how the demo board stays populated.
