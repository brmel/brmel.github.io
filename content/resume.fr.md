---
title: "CV"
layout: "resume"
lastmod: 2026-10-25
description: "Développeur logiciel senior, sept ans de C++ en production : vision industrielle 2D et 3D, apprentissage automatique et profond, aujourd’hui l’IA générative."
role: "Développeur logiciel senior à Montréal : du C++ en production pour la vision industrielle et l’apprentissage automatique, et aujourd’hui l’IA générative"
location: "Montréal, Québec"
sameAs:
  - "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - "https://github.com/brmel"
  - "https://x.com/BrmelB"

experience:
  - period: "Août 2026 — aujourd’hui"
    role: "Développeur logiciel senior, IA générative"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Flux de travail agentiques et RAG"
        text: >-
          Je mets en œuvre des flux de travail agentiques de bout en bout
          avec Google ADK et LlamaIndex : la boucle de l’agent, les outils
          que chaque agent peut appeler, sa mémoire et le contexte qu’il
          reçoit, dimensionné pour de petits modèles. Je construis de la
          génération augmentée par récupération (RAG) aux réponses fondées
          sur des sources, et je fais tourner de petits modèles en local.
      - title: "Évaluation des agents"
        text: >-
          Je construis les jeux d’évaluation et les métriques qui décident si
          un agent est assez bon pour être livré, avec la même rigueur que
          pour les modèles d’apprentissage profond.
    stack: ["Google ADK", "LlamaIndex", "flux de travail agentiques", "RAG", "évaluation d’agents", "petits modèles locaux"]

  - period: "Juillet 2024 — août 2026"
    role: "Développeur logiciel senior, Aurora Imaging Library"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Algorithmes de vision 2D et 3D"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l’Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          J’étais responsable d’algorithmes de vision de l’Aurora Imaging
          Library, la bibliothèque de vision industrielle de Zebra (Edge
          Finder, Geometric Matcher et Calibration), de la conception à la
          livraison. J’ai conçu leurs API, cherché la cause des bogues
          pour les corriger, et assisté directement les clients dont les
          applications plantaient en production. J’ai écrit la
          documentation des API et les exemples de code livrés avec chaque
          version, défini le comportement des API et la rétrocompatibilité
          avec les équipes UI, documentation et QA avant la livraison, et
          participé à la planification de la feuille de route.
      - title: "Traitement d’images sur caméras intelligentes"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "Une caméra intelligente Zebra en inspection sur un banc"
        text: >-
          J’ai adapté le traitement d’images de la bibliothèque aux caméras
          intelligentes Aurora Focus de Zebra, avec des algorithmes qui
          tiennent dans leur mémoire et leur puissance de calcul limitées.
          J’ai touché à tout le produit, de l’interface utilisateur au
          backend : j’ai corrigé des bogues de multithreading et de
          concurrence, reproduit et validé les correctifs avec l’équipe QA,
          et développé des fonctionnalités qui simplifient la configuration
          de la caméra.
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
    stack: ["C++", "algorithmes de vision industrielle", "apprentissage profond", "OCR", "apprentissage automatique", "imagerie embarquée"]

  - period: "Juin 2022 — juin 2024"
    role: "Développeur logiciel II, traitement d’images"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "L’Advanced Geometric Matcher, de la recherche à la production"
        text: >-
          J’ai fait passer l’Advanced Geometric Matcher (AGM), un nouvel
          outil d’appariement de motifs, de la recherche et du prototype à
          la production. J’ai conçu son API C++ publique avec l’équipe, et il
          fait aujourd’hui partie de l’Aurora Imaging Library de Zebra.
      - title: "Apprentissage automatique dans une bibliothèque géométrique"
        video: "CS4cs9xVecg"
        videoAlt: "Notes de la spécialisation en apprentissage profond"
        text: >-
          J’ai intégré de l’apprentissage automatique classique (forêts
          aléatoires et SVM) dans des modules jusque-là purement géométriques,
          pour classifier des motifs dans des scènes encombrées. J’ai écrit les
          nouvelles API, leur documentation de référence et les exemples
          clients livrés avec, et j’ai encadré des stagiaires et des
          développeurs juniors sur le C++ moderne, le multithreading et la
          revue de code.
      - title: "Bogues numériques et tests de régression"
        text: >-
          J’ai corrigé des bogues numériques et des régressions d’API, et
          ajouté des tests unitaires, d’intégration et aléatoires aux suites
          de régression.
    stack: ["C++", "appariement géométrique", "conception d’API publiques", "apprentissage classique", "tests de régression"]

  - period: "Juin 2019 — juin 2022"
    role: "Développeur logiciel, traitement d’images"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
    note: "Matrox Imaging, à Dorval, a rejoint Zebra Technologies en 2022."
    work:
      - title: "Calibration, mesure et métrologie"
        video: "LcoPNbyuhZU"
        videoAlt: "Le traitement d’images industriel dans la Matrox Imaging Library"
        text: >-
          Mon premier poste après la maîtrise portait sur les modules de
          mesure de la bibliothèque : Calibration, Measurement et
          Metrology. J’ai implémenté et débogué leurs algorithmes, écrit
          leurs tests, leur documentation et leurs exemples clients, et
          assisté les clients qui les utilisaient. J’ai aussi maintenu Model
          Finder, Edge Finder et Bead.
      - title: "Solveurs non linéaires dans une base de code héritée"
        video: "sfLZ7v9gEnc"
        videoAlt: "Travail au cœur de la base de code de la Matrox Imaging Library"
        text: >-
          J’ai modernisé les solveurs géométriques de la base de code C++
          de la bibliothèque, vieille de plusieurs décennies, en
          remplaçant d’anciennes méthodes par de l’optimisation non
          linéaire (dont Levenberg–Marquardt) pour une précision
          sous-pixel et une stabilité numérique. J’ai traqué des fuites
          mémoire et des références pendantes, et bâti des suites de
          régression qui protègent le comportement dont dépendent des
          milliers d’applications installées.
    stack: ["C++", "calibration", "métrologie", "optimisation non linéaire", "Levenberg–Marquardt", "stabilité numérique"]

  - period: "Janvier 2019 — mai 2019"
    role: "Stagiaire en développement logiciel"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
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
        video: "UZbmuAs2K2w"
        videoAlt: "Robotique et commande temps réel pendant la maîtrise"
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
    stack: ["C++", "SIFT", "homographie", "commande numérique", "détection et estimation", "commande stochastique et robuste", "traitement d’images"]

  - period: "2012 — 2017"
    role: "Diplôme d’ingénieur d’État, génie électrique — automatique"
    kind: "education"
    org: "École Nationale Polytechnique, Alger"
    url: "https://www.enp.edu.dz/en/"
    note: "Moyenne 17,5/20 · 5e sur 1 400 au concours national d’entrée, après les classes préparatoires (top 1 %)."
    work:
      - title: "Deux années de classes préparatoires d’abord"
        video: "VjwIGG7Lbt0"
        videoAlt: "Les années de classes préparatoires à Alger"
        text: >-
          Deux années intensives de mathématiques, de physique et de
          programmation, de 9 h à 18 h, six jours par semaine. Le
          classement national final décide de l’école d’ingénieurs où l’on
          entre.
      - title: "Systèmes de commande sur du vrai matériel"
        video: "eGPbNTXTd1I"
        videoAlt: "Projets de commande et d’automates pendant le diplôme d’ingénieur"
        text: >-
          J’ai conçu des systèmes de commande pour du vrai matériel et des
          contraintes d’usine : un régulateur de vitesse adaptatif pour
          véhicule autonome, et un programme d’automate qui pilote une
          machine d’assemblage industrielle.
    stack: ["C", "MATLAB", "VHDL", "conception de commande", "identification de procédés", "commande optimale"]

skills:
  - group: "Langages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "VHDL", "SQL"]
  - group: "Vision industrielle"
    items: ["Aurora Imaging Library (anciennement Matrox Imaging Library)", "OpenCV", "appariement géométrique", "appariement de motifs", "calibration", "métrologie", "mesure de contours", "SIFT", "homographie", "transformations 2D et 3D"]
  - group: "Maths & algorithmes"
    items: ["optimisation non linéaire", "Levenberg–Marquardt", "moindres carrés non linéaires", "algèbre linéaire", "stabilité numérique", "théorie de la commande", "apprentissage classique", "apprentissage profond"]
  - group: "C++ & systèmes"
    items: ["C++ moderne (templates, STL)", "multithreading et concurrence", "traitement d’images temps réel", "mémoire virtuelle et working set", "CMake", "GTest", "Clang / LLVM", "ASan / MSan", "Valgrind", "gdb", "multiplateforme Windows et Linux", "QNX", "ROS", "Docker"]
  - group: "IA générative"
    items: ["flux de travail agentiques", "RAG", "évaluation d’agents", "petits modèles locaux", "Google ADK", "LlamaIndex", "Gemini", "MCP"]
  - group: "Infonuagique & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Outils & pratiques"
    items: ["Visual Studio", "Git / GitHub", "SVN", "CI/CD", "revue de code", "clang-tidy / clang-format", "SonarQube", "JIRA", "Confluence", "Agile / Scrum", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)"]
  - group: "Langues"
    items: ["français", "anglais", "arabe"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---

- **Vision industrielle** — algorithmes 2D et 3D qui localisent, mesurent et inspectent des pièces dans des images prises en usine : appariement de motifs, détection de contours, calibration et métrologie
- **Apprentissage automatique, du prototype à la production** — faire passer un modèle d'un premier prototype à une fonctionnalité testée et documentée d'une bibliothèque C++ livrée aux clients
- **Évaluation de modèles d'apprentissage profond** — passer au banc d'essai, sur CPU et GPU, des modèles de détection d'objets, d'OCR et de détection de texte, et concevoir les métriques qui décident si un modèle est livré
- **Matériel à ressources limitées** — optimiser des algorithmes de vision pour qu'ils respectent les limites de mémoire et de puissance de calcul des caméras intelligentes
- **Algorithmes numériques** — optimisation non linéaire pour une précision sous-pixel, avec des tests de régression qui protègent chaque résultat numérique
- **C++ moderne** — code multithread fiable, mémoire mesurée avec [MemoryTracer](/projects/memorytracer/) et expliquée dans [deux articles](/tech/windows-memory-management-overview/), revue de code, tests automatisés et sanitizers
- **IA générative** — mon travail actuel : des flux de travail agentiques avec Google ADK et LlamaIndex, du RAG, et les évaluations qui décident quand un agent est prêt à être livré
