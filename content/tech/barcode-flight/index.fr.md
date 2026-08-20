---
title: "Comment le traitement d'image a sauvé mon vol : codes-barres et couleur de premier plan"
date: 2025-12-03
tags: ["Traitement d’Images"]
summary: "Un exemple concret de l'importance du support de la couleur de premier plan dans la lecture de codes-barres."
cover:
    image: "01-boarding-pass-dark.jpeg"
    alt: "Code-barres en Mode Sombre"
    relative: true
---

Un jour, j'étais à l'aéroport de Düsseldorf pour prendre un vol. Je m'étais déjà enregistré en ligne et je n'avais que le code-barres sur mon téléphone.

{{< figure src="01-boarding-pass-dark.jpeg" alt="Code-barres en Mode Sombre" width="200" >}}

Quand je suis arrivé au contrôle de sécurité pour scanner mon code-barres, cela n'a pas fonctionné. J'étais déjà en retard. J'ai essayé tous les zooms, toutes les rotations… rien.
L'agent de sécurité m'a dit que je devais retourner au comptoir d'enregistrement et espérer qu'ils soient encore là pour imprimer une carte d'embarquement papier.

Mais j'ai réalisé : mon téléphone était en mode sombre, et le code-barres s'affichait avec une couleur de premier plan sombre. J'ai donc simplement basculé en mode clair… et cela m'a fait gagner du temps, mon vol, et m'a épargné beaucoup de stress.

{{< figure src="02-boarding-pass-read.jpeg" alt="Code-barres en Mode Clair" width="200" >}}

J'espère vraiment que l'aéroport de Düsseldorf et tous les aéroports amélioreront leur lecteur de code-barres.

Un lecteur qui suppose du sombre sur clair est un lecteur qui fonctionne
partout sauf sur un téléphone en soirée — c'est-à-dire là où vivent réellement
les cartes d'embarquement. La couleur de premier plan est un paramètre dans
toute bibliothèque d'imagerie sérieuse, dont l'[Aurora Imaging
Library](https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html)
sur laquelle je travaille, et il ne coûte rien de le régler correctement.

Je passe encore en mode clair avant chaque porte d'embarquement.
