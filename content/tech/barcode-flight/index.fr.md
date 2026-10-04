---
title: "Pourquoi une carte d'embarquement en mode sombre ne se scanne pas : codes-barres et couleur de premier plan"
date: 2025-12-03
tags: ["Machine Vision"]
description: "Pourquoi un lecteur de codes-barres a besoin d'un réglage de couleur de premier plan, et ce qui se passe à une porte d'embarquement quand il ne l'a pas."
cover:
    image: "01-boarding-pass-dark.jpeg"
    alt: "Code-barres en mode sombre"
---

Un jour, j'étais à l'aéroport de Düsseldorf pour prendre un vol. Je m'étais déjà enregistré en ligne et je n'avais que le code-barres sur mon téléphone.

{{< figure src="01-boarding-pass-dark.jpeg" alt="Code-barres en mode sombre" >}}

Quand je suis arrivé au contrôle de sécurité pour scanner mon code-barres, ça n'a pas marché. J'étais déjà en retard. J'ai essayé tous les zooms, toutes les rotations… rien.
L'agent de sécurité m'a dit que je devais retourner au comptoir d'enregistrement et espérer qu'ils soient encore là pour imprimer une carte d'embarquement papier.

Puis je me suis rendu compte que mon téléphone était en mode sombre, et que le code-barres s'affichait avec une couleur de premier plan sombre. J'ai donc simplement basculé en mode clair… et ça m'a fait gagner du temps, ça a sauvé mon vol et ça m'a épargné beaucoup de stress.

{{< figure src="02-boarding-pass-read.jpeg" alt="Code-barres en mode clair" >}}

J'espère vraiment que l'aéroport de Düsseldorf et tous les aéroports amélioreront leur lecteur de code-barres.

Un lecteur qui suppose des barres sombres sur fond clair fonctionne partout
sauf sur un téléphone en soirée, et c'est justement sur le téléphone qu'on a
sa carte d'embarquement aujourd'hui. La couleur de premier plan est un paramètre dans
toute bibliothèque d'imagerie sérieuse, dont l'[Aurora Imaging
Library](https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html)
sur laquelle je travaille, et il ne coûte rien de le régler correctement.

Je passe encore en mode clair avant chaque porte d'embarquement.
