---
title: "Leorra"
date: 2021-08-29
projectNo: 6
domain: "mobile"
status: "archived"
pitch: "An app for sending a parcel abroad with a traveller who has room in their suitcase."
description: "An app for sending a parcel abroad with a traveller who has room in their suitcase."
metrics:
  - value: "4 layers"
    label: "domain, application, infrastructure and presentation, cleanly separated"
  - value: "3 languages"
    label: "English, French and Arabic, right-to-left aware"
  - value: "20 months"
    label: "of design, build and iteration on a real marketplace"
stack: ["Flutter", "Dart", "Firebase", "BLoC", "Clean Architecture", "get_it"]
links:
  live: ""
lede: |
  A marketplace for something Algerian families abroad already do informally:
  matching someone who needs a parcel moved with a traveller who has spare
  luggage. Twenty months of design and build, across three languages. It was
  never released.
lessons:
  - "**I rewrote two months of work and it was the right call.** The commit is still there: *Restart from a very clean project. Only login files are added* — 1,134 deletions against 45 insertions. The first version worked and could not be extended; everything lived in widgets. What replaced it was Domain / Application / Infrastructure / Presentation with value objects and validators, and the fourth feature cost about what the second did."
  - "**Layer discipline is measurable, and mine was lopsided.** 19 domain files against 159 presentation files. The business rules were genuinely small and genuinely isolated, but I wrote eight test files, all for identification, and none for matching, trips or contracts. I tested the layer that was easy to test, not the one carrying the risk."
  - "**Trust was the product, and I built the marketplace instead.** Listings, chat, contracts and matching all shipped. Identity verification, escrow, dispute handling and what happens when a package does not arrive did not. For a stranger to hand another stranger a laptop at an airport, the trust layer is the app, and I treated it as a later phase."
  - "**The gap between the last feature commit and the last commit of any kind is a translation pass.** Twenty months, three languages and store screenshots, and what was missing at the end was never another feature."
tags: ["Flutter", "Firebase", "Mobile", "Clean Architecture"]
---

## The story

Sending a laptop from Montréal to Algiers costs more than the laptop, takes a
month, and may never arrive. Every Algerian family abroad already routes around
this: you ask until you find someone flying home with room in a suitcase. It
works entirely on trust, which means it only reaches as far as your own network
does.

I tried to turn that into a marketplace: senders post what needs moving,
travellers post their route and spare kilos, and the app matches them.

## The product

I shipped listings, chat, contracts and matching, in three languages, with the
store screenshots ready. Identity verification, escrow and what happens when a
package does not arrive: none of it.

Two months in I deleted the working version and started again — the commit says
*restart from a very clean project*, 1,134 deletions against 45 insertions. The
first build worked and could not be extended; everything lived in the widgets.
What replaced it separated domain from application from interface, and the
fourth feature cost about what the second had.

That was the right call and I would make it again. It is also not why the
project stopped.
