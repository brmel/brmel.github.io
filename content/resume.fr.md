---
title: "CV"
layout: "resume"
lastmod: 2026-10-30
description: "Développeur logiciel senior, sept ans de C++ en production : vision industrielle 2D et 3D, apprentissage automatique et profond, aujourd’hui l’IA générative."
role: "Développeur logiciel senior à Montréal : du C++ en production pour la vision industrielle, l’apprentissage automatique et l’apprentissage profond"
location: "Montréal, Québec"
sameAs:
  - "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - "https://github.com/brmel"
  - "https://x.com/BrmelB"

highlights:
  - title: "Vision industrielle"
    text: "Des algorithmes 2D et 3D qui localisent, mesurent et inspectent des pièces dans des images prises en usine : appariement de motifs, détection de contours, calibration et métrologie."
  - title: "Apprentissage automatique en production"
    text: "D’un premier prototype à une fonctionnalité testée et documentée d’une bibliothèque C++ livrée aux clients."
  - title: "Évaluation de l’apprentissage profond"
    text: "Des modèles de détection d’objets, d’OCR et de détection de texte passés au banc d’essai sur CPU et GPU, avec les métriques qui décident si un modèle est livré."
  - title: "Matériel à ressources limitées"
    text: "Des algorithmes de vision qui respectent les limites de mémoire et de puissance de calcul des caméras intelligentes."
  - title: "Algorithmes numériques"
    text: "L’optimisation non linéaire pour une précision sous-pixel, avec des tests de régression qui protègent chaque résultat numérique."
  - title: "C++ moderne"
    text: "Du code multithread fiable, la mémoire mesurée avec [MemoryTracer](/projects/memorytracer/), la revue de code, les tests automatisés et les sanitizers."

experience:
  - period: "Août 2026 — aujourd’hui"
    role: "Développeur logiciel senior, IA générative"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Agents et recherche documentaire"
        text: >-
          Je construis des flux de travail agentiques et de la génération
          augmentée par récupération (RAG), ainsi que les évaluations qui
          décident quand un agent est prêt à être livré, avec la même
          rigueur que pour les modèles d’apprentissage profond.
    stack: ["flux de travail agentiques", "RAG", "évaluation d’agents"]

  - period: "Juillet 2024 — août 2026"
    role: "Développeur logiciel senior, Aurora Imaging Library"
    org: "Zebra Technologies"
    work:
      - title: "Algorithmes de vision 2D et 3D"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l’Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          J’étais responsable d’algorithmes de vision de l’Aurora Imaging
          Library, la bibliothèque de vision industrielle de Zebra (Edge
          Finder, Geometric Matcher et Calibration), de la conception à la
          livraison : conception des API, correction des bogues,
          documentation et exemples de code livrés avec chaque version, et
          assistance directe aux clients dont les applications plantaient
          en production. J’ai défini le comportement des API et la
          rétrocompatibilité avec les équipes UI, documentation et QA, et
          participé à la planification de la feuille de route.
      - title: "Traitement d’images sur caméras intelligentes"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "Une caméra intelligente Zebra en inspection sur un banc"
        text: >-
          J’ai adapté le traitement d’images de la bibliothèque aux caméras
          intelligentes Aurora Focus de Zebra, avec des algorithmes qui
          tiennent dans leur mémoire et leur puissance de calcul limitées.
          J’ai travaillé de l’interface utilisateur au backend : j’ai
          corrigé des bogues de multithreading et de concurrence, validé les
          correctifs avec l’équipe QA, et développé des fonctionnalités qui
          simplifient la configuration de la caméra.
      - title: "Apprentissage automatique classique en C++"
        text: >-
          J’ai implémenté des arbres de décision, des forêts aléatoires et
          les k-moyennes dans le C++ de la bibliothèque : multithread,
          thread-safe et avec arrêt anticipé.
      - title: "Apprentissage profond pour l’OCR et la détection d’objets"
        text: >-
          J’ai passé au banc d’essai, sur CPU et GPU, des modèles
          d’apprentissage profond de détection d’objets, d’OCR et de
          détection de texte, réglé leurs hyperparamètres et conçu les
          métriques qui décident si un modèle est livré. Puis j’ai mis en
          production ceux qui étaient retenus.
    stack: ["C++", "vision industrielle", "apprentissage automatique", "apprentissage profond", "OCR", "caméras intelligentes"]

  - period: "Juin 2022 — juin 2024"
    role: "Développeur logiciel II, traitement d’images"
    org: "Zebra Technologies"
    work:
      - title: "L’Advanced Geometric Matcher, de la recherche à la production"
        text: >-
          J’ai fait passer l’Advanced Geometric Matcher (AGM), un nouvel
          outil d’appariement de motifs, de la recherche et du prototype à
          la production, et conçu son API C++ publique avec l’équipe. Il
          fait aujourd’hui partie de l’Aurora Imaging Library de Zebra.
      - title: "Apprentissage automatique dans une bibliothèque géométrique"
        text: >-
          J’ai intégré de l’apprentissage automatique classique (forêts
          aléatoires et SVM) dans des modules jusque-là purement géométriques,
          pour classifier des motifs dans des scènes encombrées, avec les
          nouvelles API, leur documentation de référence et les exemples
          clients. J’ai aussi encadré des stagiaires et des développeurs
          juniors sur le C++ moderne, le multithreading et la revue de code.
      - title: "Bogues numériques et tests de régression"
        text: >-
          J’ai corrigé des bogues numériques et des régressions d’API, et
          ajouté des tests unitaires, d’intégration et aléatoires aux suites
          de régression.
    stack: ["C++", "appariement géométrique", "conception d’API publiques", "apprentissage classique", "tests de régression"]

  - period: "Juin 2019 — juin 2022"
    role: "Développeur logiciel, traitement d’images"
    org: "Matrox Imaging"
    note: "Matrox Imaging, à Dorval, a rejoint Zebra Technologies en 2022."
    work:
      - title: "Calibration, mesure et métrologie"
        text: >-
          Mon premier poste après la maîtrise : j’ai implémenté et débogué
          les modules Calibration, Measurement et Metrology de la
          bibliothèque, écrit leurs tests, leur documentation et leurs
          exemples clients, et assisté les clients qui les utilisaient. J’ai
          aussi maintenu Model Finder, Edge Finder et Bead.
      - title: "Solveurs non linéaires dans une base de code héritée"
        text: >-
          J’ai remplacé d’anciens solveurs géométriques de la base de code
          C++ de la bibliothèque, vieille de plusieurs décennies, par de
          l’optimisation non linéaire (dont Levenberg–Marquardt), pour une
          précision sous-pixel et une stabilité numérique. J’ai traqué des
          fuites mémoire et des références pendantes, et bâti des suites de
          régression qui protègent le comportement dont dépendent des
          milliers d’applications installées.
    stack: ["C++", "calibration", "métrologie", "optimisation non linéaire", "Levenberg–Marquardt", "stabilité numérique"]

  - period: "Janvier 2019 — mai 2019"
    role: "Stagiaire en développement logiciel"
    org: "Matrox Imaging"
    work:
      - title: "Apprentissage automatique dans la bibliothèque d’imagerie"
        text: >-
          J’ai intégré un classifieur à forêt aléatoire à la Matrox Imaging
          Library (aujourd’hui l’Aurora Imaging Library de Zebra), avec un
          entraînement multithread et le démarrage à chaud (warm start), pour
          que les lignes de production puissent trier les défauts en temps
          réel. J’ai aussi construit des générateurs de jeux de données
          synthétiques et des bancs d’essai automatisés qui mesuraient la
          précision et la vitesse du classifieur à chaque changement.
    stack: ["C++", "forêts aléatoires", "multithreading", "bancs d’essai"]

  - period: "2017 — 2019"
    role: "Maîtrise en ingénierie (M.Ing.), génie électrique — automatique"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Maîtrise professionnelle avec stage industriel · Moyenne 3,87/4 · Bourse de la Fondation Al Ghurair — 1 sur environ 100 boursiers parmi plus de 15 000 candidatures."
    work:
      - title: "Comment je suis arrivé au Canada"
        video: "BPkj-VETeX0"
        videoAlt: "À propos de la bourse de la Fondation Al Ghurair"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          La bourse a été accordée au mérite académique et a financé ma
          maîtrise. C’est ainsi que je suis arrivé à Montréal.
      - title: "Projets sur du vrai matériel"
        text: >-
          Chaque cours important se terminait par un projet sur du vrai
          matériel : commande de robot et exécution de trajectoires,
          ordonnancement temps réel sous QNX, traitement d’images pour
          localiser des pièces, et estimation d’état.
      - title: "Extraction de caractéristiques, assemblage et commande multi-robots"
        text: >-
          J’ai assemblé des panoramas à partir de plusieurs photos grâce à
          l’extraction de caractéristiques SIFT et à l’estimation
          d’homographies, et construit un système de vision en MATLAB et
          C++ qui localisait et identifiait des pièces dans l’espace de
          travail d’un robot Fanuc à 6 axes. J’ai aussi écrit des
          algorithmes de consensus distribué en Python et exécuté du suivi
          de formation sur la flotte multi-robots réelle du Georgia Tech
          Robotarium.
    stack: ["C++", "SIFT", "homographie", "commande numérique", "détection et estimation", "traitement d’images"]

  - period: "2012 — 2017"
    role: "Diplôme d’ingénieur d’État, génie électrique — automatique"
    kind: "education"
    org: "École Nationale Polytechnique, Alger"
    url: "https://www.enp.edu.dz/en/"
    note: "Moyenne 17,5/20 · 5e sur 1 400 au concours national d’entrée, après les classes préparatoires (top 1 %)."
    work:
      - title: "Deux années de classes préparatoires d’abord"
        text: >-
          Deux années intensives de mathématiques, de physique et de
          programmation, de 9 h à 18 h, six jours par semaine. Le
          classement national final décide de l’école d’ingénieurs où l’on
          entre.
      - title: "Systèmes de commande sur du vrai matériel"
        text: >-
          J’ai conçu des systèmes de commande pour du vrai matériel et des
          contraintes d’usine : un régulateur de vitesse adaptatif pour
          véhicule autonome, et un programme d’automate qui pilote une
          machine d’assemblage industrielle.
    stack: ["C", "MATLAB", "VHDL", "conception de commande", "identification de procédés", "commande optimale"]

skills:
  - group: "Langages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "SQL"]
  - group: "Vision industrielle"
    items: ["Aurora Imaging Library (anciennement Matrox Imaging Library)", "OpenCV", "appariement de motifs", "calibration", "métrologie", "mesure de contours", "SIFT", "homographie", "transformations 2D et 3D"]
  - group: "Apprentissage automatique"
    items: ["arbres de décision", "forêts aléatoires", "SVM", "k-moyennes", "scikit-learn", "apprentissage profond", "détection d’objets", "OCR", "évaluation de modèles sur CPU et GPU", "réglage d’hyperparamètres"]
  - group: "Mathématiques"
    items: ["optimisation non linéaire", "Levenberg–Marquardt", "moindres carrés non linéaires", "algèbre linéaire", "stabilité numérique", "théorie de la commande"]
  - group: "C++ & systèmes"
    items: ["C++ moderne (templates, STL)", "multithreading et concurrence", "mémoire virtuelle et working set", "CMake", "GTest", "ASan / MSan", "Valgrind", "gdb", "Windows et Linux", "Docker"]
  - group: "IA générative"
    items: ["flux de travail agentiques", "RAG", "évaluation d’agents"]
  - group: "Outils"
    items: ["Git / GitHub", "SVN", "CI/CD", "revue de code", "clang-tidy / clang-format", "SonarQube", "Visual Studio", "JIRA", "Confluence", "Google Cloud", "Firebase", "FastAPI"]
  - group: "Langues"
    items: ["français (langue maternelle)", "anglais (professionnel)", "arabe (langue maternelle)"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---
