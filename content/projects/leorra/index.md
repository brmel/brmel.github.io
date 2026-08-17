---
title: "Leorra"
date: 2021-08-29
projectNo: 6
domain: "mobile"
status: "archived"
pitch: "Peer-to-peer shipping between countries the courier companies price out — matching people who need to send something with travellers who have spare luggage."
metrics:
  - value: "20 months"
    label: "of work, three languages, store screenshots"
  - value: "1,134 lines"
    label: "deleted in one commit, two months in"
  - value: "0"
    label: "launches — the missing piece was never a feature"
stack: ["Flutter", "Dart", "Firebase", "BLoC", "Clean Architecture", "get_it"]
newToMe: ["clean architecture in Flutter", "BLoC state management", "dependency injection with get_it"]
links:
  live: ""
lede: |
  A marketplace for what Algerian families abroad already do informally —
  matching someone who needs a parcel moved with a traveller who has spare
  luggage. Twenty months of work, three languages, and it never launched.
takeaway: "Rewriting from scratch two months in was the right call. What was missing at the end was never the architecture."
lessons:
  - "**I threw away two months of work and it was correct.** The commit is still there: *Restart from a very clean project. Only login files are added* — 1,134 deletions against 45 insertions. The first version worked and was unextendable; everything lived in widgets. What followed was Domains / Application / Infrastructure / Presentation with value objects and validators, and adding the fourth feature cost about what the second did."
  - "**Layer discipline is measurable, and mine was lopsided.** 19 files of domain against 159 of presentation. The business rules were genuinely small and genuinely isolated — but I wrote eight test files, all for identification, and none for matching, trips or contracts. I tested the layer that was easy to test rather than the one that carried the risk."
  - "**Trust was the product, and I built the marketplace instead.** Listings, chat, contracts, matching — all shipped. Identity verification, escrow, dispute handling, what happens when a package does not arrive: none of it. For a stranger to hand another stranger a laptop at an airport, the trust layer *is* the app, and I treated it as a later phase."
  - "**Twenty months, three languages, store screenshots — and it never launched.** The gap between the last feature commit and the last commit of any kind is a translation pass. What was missing was never another feature."
tags: ["Flutter", "Firebase", "Mobile", "Clean Architecture"]
---

## The story

Sending a laptop from Montréal to Algiers costs more than the laptop, takes a
month, and may never arrive. Every Algerian family abroad already routes around
this: you ask until you find someone flying home with room in a suitcase. It
works entirely on trust, which means it only reaches as far as your own network
does.

Leorra tried to make that a marketplace — senders post what needs moving,
travellers post their route and spare kilos, the app matches them.

> For a stranger to hand another stranger a laptop at an airport, the trust
> layer *is* the app. I built the marketplace instead.

## The product

Listings, chat, contracts and matching all shipped, in three languages, with
store screenshots ready. Identity verification, escrow and what happens when a
package does not arrive: none of it.

Two months in I deleted the working version and started again — the commit says
*restart from a very clean project*, 1,134 deletions against 45 insertions. The
first build worked and could not be extended; everything lived in the widgets.
What replaced it separated domain from application from interface, and the
fourth feature cost about what the second had.

That was the right call and I would make it again. It is also not why the
project stopped.
