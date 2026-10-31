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
    text: "Des algorithmes 2D et 3D qui localisent, mesurent et inspectent des pièces : appariement de motifs, détection de contours, calibration et métrologie."
  - title: "Apprentissage automatique"
    text: "Arbres de décision, forêts aléatoires, SVM et k-moyennes en C++, du prototype à une fonctionnalité testée et documentée de la bibliothèque."
  - title: "Apprentissage profond"
    text: "Des modèles de détection d’objets et d’OCR passés au banc d’essai sur CPU et GPU, et ceux qui étaient retenus mis en production."
  - title: "Caméras intelligentes"
    text: "Des algorithmes de vision qui tiennent dans la mémoire et la puissance de calcul limitées d’une caméra."
  - title: "Algorithmes numériques"
    text: "L’optimisation non linéaire pour une précision sous-pixel, protégée par des tests de régression."
  - title: "C++ moderne"
    text: "Du code multithread, la mémoire mesurée avec [MemoryTracer](/projects/memorytracer/), les tests et les sanitizers."

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
          décident quand un agent est prêt à être livré.

  - period: "Juillet 2024 — août 2026"
    role: "Développeur logiciel senior, Aurora Imaging Library"
    org: "Zebra Technologies"
    work:
      - title: "Algorithmes de vision 2D et 3D"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l’Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          J’étais responsable d’Edge Finder, de Geometric Matcher et de
          Calibration dans l’Aurora Imaging Library, la bibliothèque de
          vision industrielle de Zebra, de la conception à la livraison :
          conception des API, correction des bogues, documentation, exemples
          de code et assistance aux clients. J’ai défini le comportement des
          API et la rétrocompatibilité avec les équipes UI, documentation et
          QA, et participé à la feuille de route.
      - title: "Caméras intelligentes"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "Une caméra intelligente Zebra en inspection sur un banc"
        text: >-
          J’ai adapté le traitement d’images de la bibliothèque aux caméras
          intelligentes Aurora Focus de Zebra, dans les limites de leur
          mémoire et de leur puissance de calcul. De l’interface utilisateur
          au backend, j’ai corrigé des bogues de multithreading et de
          concurrence et développé des fonctionnalités qui simplifient la
          configuration de la caméra.
      - title: "Apprentissage automatique en C++"
        text: >-
          J’ai implémenté des arbres de décision, des forêts aléatoires et
          les k-moyennes dans le C++ de la bibliothèque : multithread,
          thread-safe et avec arrêt anticipé.
      - title: "Apprentissage profond"
        text: >-
          J’ai passé au banc d’essai, sur CPU et GPU, des modèles
          d’apprentissage profond de détection d’objets, d’OCR et de
          détection de texte, réglé leurs hyperparamètres et conçu les
          métriques qui décident si un modèle est livré, puis mis en
          production ceux qui étaient retenus.

  - period: "Juin 2022 — juin 2024"
    role: "Développeur logiciel II, traitement d’images"
    org: "Zebra Technologies"
    work:
      - title: "L’Advanced Geometric Matcher"
        text: >-
          J’ai fait passer l’Advanced Geometric Matcher (AGM), un nouvel
          outil d’appariement de motifs, de la recherche et du prototype à
          la production, et conçu son API C++ publique avec l’équipe. Il
          fait aujourd’hui partie de l’Aurora Imaging Library de Zebra.
      - title: "Apprentissage automatique dans des outils géométriques"
        text: >-
          J’ai ajouté des forêts aléatoires et des SVM à des modules
          jusque-là purement géométriques, pour classifier des motifs dans
          des scènes encombrées, avec de nouvelles API, leur documentation
          et des exemples. J’ai aussi encadré des stagiaires et des
          développeurs juniors sur le C++ moderne, le multithreading et la
          revue de code.
      - title: "Bogues numériques et tests de régression"
        text: >-
          J’ai corrigé des bogues numériques et des régressions d’API, et
          ajouté des tests unitaires, d’intégration et aléatoires aux suites
          de régression.

  - period: "Juin 2019 — juin 2022"
    role: "Développeur logiciel, traitement d’images"
    org: "Matrox Imaging"
    note: "Matrox Imaging, à Dorval, a rejoint Zebra Technologies en 2022."
    work:
      - title: "Calibration, mesure et métrologie"
        text: >-
          J’ai implémenté et débogué les modules Calibration, Measurement et
          Metrology de la bibliothèque, avec leurs tests, leur documentation
          et leurs exemples, et assisté les clients qui les utilisaient.
          J’ai aussi maintenu Model Finder, Edge Finder et Bead.
      - title: "Solveurs non linéaires"
        text: >-
          J’ai remplacé d’anciens solveurs géométriques de la base de code
          C++ de la bibliothèque, vieille de plusieurs décennies, par de
          l’optimisation non linéaire (dont Levenberg–Marquardt), pour une
          précision sous-pixel et une stabilité numérique. J’ai traqué des
          fuites mémoire et des références pendantes, et bâti des suites de
          régression qui protègent le comportement dont dépendent des
          milliers d’applications installées.

  - period: "Janvier 2019 — mai 2019"
    role: "Stagiaire en développement logiciel"
    org: "Matrox Imaging"
    work:
      - title: "Un classifieur à forêt aléatoire"
        text: >-
          J’ai intégré un classifieur à forêt aléatoire à la Matrox Imaging
          Library (aujourd’hui l’Aurora Imaging Library de Zebra), avec un
          entraînement multithread et le démarrage à chaud (warm start), pour
          que les lignes de production puissent trier les défauts en temps
          réel, ainsi que les jeux de données synthétiques et les bancs
          d’essai automatisés qui mesuraient sa précision et sa vitesse à
          chaque changement.

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
          matériel : ordonnancement temps réel sous QNX, un système de vision
          en MATLAB et C++ qui localisait des pièces pour un robot Fanuc à
          6 axes, l’assemblage de panoramas avec SIFT, et le suivi de
          formation sur la flotte de robots du Georgia Tech Robotarium.

  - period: "2012 — 2017"
    role: "Diplôme d’ingénieur d’État, génie électrique — automatique"
    kind: "education"
    org: "École Nationale Polytechnique, Alger"
    url: "https://www.enp.edu.dz/en/"
    note: "Moyenne 17,5/20 · 5e sur 1 400 au concours national d’entrée, après les classes préparatoires (top 1 %)."
    work:
      - title: "Classes préparatoires"
        text: >-
          Deux années intensives de mathématiques, de physique et de
          programmation, avant le classement national qui décide de l’école
          d’ingénieurs où l’on entre.
      - title: "Systèmes de commande sur du vrai matériel"
        text: >-
          J’ai conçu un régulateur de vitesse adaptatif pour véhicule
          autonome et un programme d’automate qui pilote une machine
          d’assemblage industrielle.

skills:
  - group: "Langages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "SQL"]
  - group: "Vision industrielle"
    items: ["Aurora Imaging Library", "OpenCV", "appariement de motifs", "calibration", "métrologie", "mesure de contours", "SIFT", "homographie", "géométrie 2D et 3D"]
  - group: "Apprentissage automatique"
    items: ["arbres de décision", "forêts aléatoires", "SVM", "k-moyennes", "scikit-learn", "apprentissage profond", "détection d’objets", "OCR", "évaluation de modèles", "réglage d’hyperparamètres"]
  - group: "Mathématiques"
    items: ["optimisation non linéaire", "Levenberg–Marquardt", "algèbre linéaire", "stabilité numérique", "théorie de la commande"]
  - group: "C++ & systèmes"
    items: ["C++ moderne", "multithreading et concurrence", "mémoire virtuelle", "CMake", "GTest", "ASan / MSan", "Valgrind", "gdb", "Windows et Linux", "Docker"]
  - group: "IA générative"
    items: ["flux de travail agentiques", "RAG", "évaluation d’agents"]
  - group: "Outils"
    items: ["Git / GitHub", "SVN", "CI/CD", "revue de code", "clang-tidy", "SonarQube", "Visual Studio", "JIRA", "Confluence", "Google Cloud", "Firebase", "FastAPI"]
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
