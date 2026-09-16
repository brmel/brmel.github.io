---
title: "PariData"
date: 2026-09-15
layout: "tracker"
projectNo: 11
domain: "data"
status: "active"
pitch: "Un pronostiqueur football publie ses pronostics. Ceci les enregistre tous, à mise fixe, et les confronte à ce qui s'est réellement passé."
description: "Chaque pronostic publié par un pronostiqueur football, enregistré à mise fixe et confronté au résultat réel. Rien d'inféré, chaque ligne sourcée."
stack: ["Hugo", "JSON", "Python"]
takeaway: "Un relevé ne vaut d'être lu que s'il a été figé avant que le résultat soit connu — chaque garde-fou ici l'impose par construction, pas par promesse."
tags: ["Data Analysis"]
---

PariData est un projet de données. Il suit un influenceur qui fait la promotion d'une application de paris et partage des pronostics de football, pour répondre à une seule question : le suivre fait-il gagner de l'argent, ou en perdre ?

- Chaque pronostic est enregistré sous forme de données, avec un lien vers la publication d'origine, et vérifié automatiquement avant la mise en ligne.
- Un combiné n'est gagnant que si tous ses matchs le sont. Un match annulé est retiré du combiné.
- Tous les montants sont simulés avec une mise fixe. Aucun vrai pari n'a été placé. 18+.
