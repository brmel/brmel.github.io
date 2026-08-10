---
title: "Leorra"
date: 2021-08-29
projectNo: 6
domain: "mobile"
status: "archived"
pitch: "Peer-to-peer shipping between countries the courier companies price out — matching people who need to send something with travellers who have spare luggage."
stack: ["Flutter", "Dart", "Firebase", "BLoC", "Clean Architecture", "get_it"]
links:
  live: ""
lede: |
  Sending a laptop from Montréal to Algiers costs more than the laptop is worth,
  takes a month, and there is a real chance it never arrives — which is why
  every Algerian family abroad already does this informally, asking around until
  they find someone flying home with room in a suitcase. That arrangement works
  entirely on trust and word of mouth, so it only reaches as far as your own
  network reaches. Leorra was an attempt to make it a marketplace: senders post
  what they need moved, travellers post the route and the kilos they have spare,
  and the app matches them.
takeaway: "Rewriting from scratch two months in was the right call and I would make it again — but the architecture I bought with it was never the reason the project stopped."
lessons:
  - "**I threw away two months of work and it was correct.** The commit is still there: *Restart from a very clean project. Only login files are added* — 1,134 deletions against 45 insertions. The first version worked and was unextendable; everything lived in widgets. What followed was Domains / Application / Infrastructure / Presentation with value objects and validators, and adding the fourth feature cost about what the second did."
  - "**Layer discipline is measurable, and mine was lopsided.** 19 files of domain against 159 of presentation. The business rules were genuinely small and genuinely isolated — but I wrote eight test files, all for identification, and none for matching, trips or contracts. I tested the layer that was easy to test rather than the one that carried the risk."
  - "**Trust was the product, and I built the marketplace instead.** Listings, chat, contracts, matching — all shipped. Identity verification, escrow, dispute handling, what happens when a package does not arrive: none of it. For a stranger to hand another stranger a laptop at an airport, the trust layer *is* the app, and I treated it as a later phase."
  - "**Twenty months, three languages, store screenshots — and it never launched.** The gap between the last feature commit and the last commit of any kind is a translation pass. What was missing was never another feature."
tags: ["Flutter", "Dart", "Firebase", "Mobile", "Clean Architecture"]
---

## The story

The informal version of this already exists in every diaspora. Someone in a
family WhatsApp group is flying to Algiers on the 20th and has 8 kilos spare;
someone else needs a prescription, a document, a phone taken over. The
arrangement is old and it works, because both sides are inside the same circle of
trust.

What it cannot do is scale past that circle. If nobody you know is flying, you
are back to a courier quoting more than the item is worth.

Leorra put both sides on a board. Travellers post a route, a date, the kilos and
the categories they will carry. Senders post what needs to move, from where to
where, its weight and what they will pay. Each side sees the other, and a chat
opens when there is a match worth having.

## The product

Three real routes from the app's own listings give the shape of it: Algeria →
Canada, a 0.1 kg medication for $25. Turkey → Tunisia, 10 kg of documents for
$100. France → Morocco, a 0.3 kg electronic item for $10. Small, personal,
specific — the shipments that courier pricing treats worst.

A Flutter app on Firebase, in English, French and Arabic, with the layering
deliberate rather than incidental:

- **Domains** — entities (`Article`, `Trip`, `MatchUsers`, `Identification`),
  value objects (`Address`, `PhoneNumber`, `Image`) and validators per feature.
  19 files, 1,388 lines, no Flutter import anywhere in it.
- **Application** — a BLoC per feature with explicit event and state files;
  59 files.
- **Infrastructure** — Firestore, Auth, Storage, Messaging behind repository
  interfaces the domain defines.
- **Presentation** — 159 files, responsive through a screen-config layer that
  predates most of Flutter's own answers to the problem.

Dependency injection through `get_it` with a locator per feature, so a feature
could be added or removed as a unit. Two Cloud Functions — `createNewChat`,
`updateExistedChat` — because chat fan-out is the one thing that should not live
on the client.

**153 commits between December 2019 and August 2021.** The last one adds
translations. There is no listing on either store, and the Firebase project no
longer serves anything.

## Why it stopped

Not for a technical reason, which is the uncomfortable part. The architecture
held: by the end, features were cheap to add. What never got built was the
answer to the only question that matters when two strangers meet at an airport —
*what happens if this goes wrong?* No verified identity, no escrow, no dispute
path, no insurance.

That is not a feature you bolt on afterwards. It is the product, and I spent
twenty months building the marketplace that would sit on top of it.
