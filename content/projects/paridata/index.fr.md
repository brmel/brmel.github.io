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

- Chaque pronostic est enregistré dès sa publication, avant les matchs, avec un lien vers la publication.
- Un combiné n'est gagnant que si tous ses matchs le sont. Un match annulé est retiré du combiné, pas compté comme perdu.
- L'argent est fictif : il montre ce qu'une mise fixe aurait rapporté. Personne ici n'a parié. 18+.
