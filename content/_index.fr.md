---
title: "Ibraverse"
date: 2025-01-08
outputs: ["HTML", "RSS", "JSON"]
description: "Ingénieur C++ senior chez Zebra Technologies : algorithmes de vision 2D et 3D, solveurs numériques et systèmes bas niveau. Projets et articles techniques."
---
Ingénieur C++ senior chez Zebra Technologies. Je suis responsable des
algorithmes 2D et 3D de l'Aurora Imaging Library — solveurs géométriques,
calibration et métrologie tournant en usine — et je les porte sur une caméra
intelligente sous fortes contraintes de mémoire et de processeur. C++17/20
moderne, Windows et Linux, sept ans sur la même base de code : Matrox Imaging
d'abord, puis Zebra après le rachat.

Concrètement :

- **Algorithmes numériques** — optimisation non linéaire et Levenberg–Marquardt, précision sous-pixel, et comportement en virgule flottante protégé par des suites de régression
- **Systèmes bas niveau** — mémoire virtuelle, working set, tas et fichiers mappés. J'ai écrit [MemoryTracer](/projects/memorytracer/) pour le mesurer et [deux articles](/tech/windows-memory-management-overview/) pour l'expliquer
- **Multithreading et concurrence** — conditions de course dans une bibliothèque dont dépendent des milliers d'applications installées
- **Vision industrielle** — appariement de motifs 2D, détection de contours, métrologie, SIFT et homographie, et apprentissage profond pour les codes-barres abîmés ou mal éclairés
- **Pratiques d'ingénierie** — CMake, GTest, sanitizers et Valgrind, revue de code, et suites de régression qui protègent des milliers d'applications installées

J'écris aussi la documentation des API et les exemples de code livrés avec la
bibliothèque, j'assiste les clients qui déboguent leurs propres applications, et
je définis le comportement des API avec les équipes UI, documentation et QA
avant chaque livraison.

En dehors du travail : [une cellule robotique dans un moteur physique](/projects/robonode/),
[un agent qui teste des applications web](/projects/domia/), et des
[articles](/tech/) sur ce que chacun m'a appris.
