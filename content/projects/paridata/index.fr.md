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
lede: |
  Les pronostiqueurs publient leurs gains. Personne ne publie le total courant —
  le seul chiffre qui tranche la question. Chaque ticket est enregistré dès sa
  publication, misé une unité fixe, et le solde dit ce qu'il dit.
takeaway: "Un relevé ne vaut d'être lu que s'il a été figé avant que le résultat soit connu — chaque garde-fou ici l'impose par construction, pas par promesse."
lessons:
  - "**Une sélection annulée gonfle silencieusement chaque combiné qu'elle touche.** Un match reporté rend sa part et sa cote retombe à 1,00 : le ticket publié à 3,38 a réellement payé 2,70. Le calcul vit dans un seul partial, parce qu'il a été faux une fois, à un seul endroit."
  - "**Exiger l'URL source dans le schéma vaut mieux que se promettre de l'ajouter.** Une ligne invérifiable vaut moins que pas de ligne, et les bonnes intentions tiennent environ trois semaines. Le contrôle refuse de publier un ticket sans elle."
  - "**Le contrôle croisé le moins cher a attrapé le plus d'erreurs.** La cote totale doit égaler le produit des sélections à 0,02 près — quatre lignes qui arrêtent un chiffre mal lu avant qu'il n'atteigne le solde."
tags: ["Data Analysis"]
---

## Ce qui est enregistré

Un ticket par pronostic publié, saisi à la main depuis la publication. Un pari
simple est un ticket à une sélection ; un combiné en compte plusieurs, et chacune
se règle seule — un combiné meurt sur sa pire sélection.

Chaque ticket est misé une unité fixe. La mise plate est le seul plan qui mesure
le pronostiqueur plutôt que le parieur.

## Comment ça se règle

En attente jusqu'à la fin des matchs, puis gagné, perdu ou annulé. Une sélection
annulée rend sa part et sa cote sort du calcul du retour. Un résultat invérifiable
reste en attente plutôt que d'être deviné dans une colonne.

## Ce que ceci n'est pas

Ni un conseil, ni une méthode, ni une accusation. La colonne en argent est
hypothétique : elle montre ce qu'une mise fixe aurait rendu. Personne ici n'a
placé de pari.

Les jeux d'argent sont interdits aux moins de 18 ans.
