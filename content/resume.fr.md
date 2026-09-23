---
title: "CV"
layout: "resume"
summary: "Ingénieur C++ senior — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Ingénieur C++ senior, sept ans sur des algorithmes de vision 2D et 3D : C++17/20 moderne, traitement d'images temps réel et optimisation non linéaire."
aliases: ["/fr/timeline/"]
role: "Développeur logiciel senior — C++ moderne, traitement d'images temps réel, algorithmes de vision 2D/3D"
location: "Montréal, Québec"
contact:
  - label: "Courriel"
    url: "mailto:mellah.brahim.redouane@gmail.com"
  - label: "LinkedIn"
    url: "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - label: "GitHub"
    url: "https://github.com/brmel"
  - label: "X"
    url: "https://x.com/BrmelB"

experience:
  - period: "2024 — Aujourd'hui"
    role: "Développeur logiciel senior"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Algorithmes de vision 2D et 3D"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l'Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          Je développe et maintiens les algorithmes 2D et 3D de la
          bibliothèque : j'ajoute des fonctionnalités, j'investigue et corrige
          des bogues, et j'assiste directement les clients dont les
          applications tombent en production. J'écris la documentation des API
          et les exemples de code livrés avec chaque version, et je définis le
          comportement des API et la compatibilité ascendante avec les équipes
          UI, documentation et QA avant la livraison. Je participe aussi à la
          planification de la feuille de route.
      - title: "Traitement d'images sur la caméra intelligente"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "La caméra intelligente Aurora Focus en inspection sur un banc"
        text: >-
          Je porte des modules de traitement d'images sur la caméra
          intelligente Aurora Focus, en écrivant des algorithmes qui tiennent
          dans des budgets mémoire et processeur serrés. Le travail couvre
          toute la pile : je débogue des problèmes qui traversent l'interface
          et le backend, je corrige des bogues de multithreading et de
          concurrence, je travaille avec l'équipe QA sur la reproduction et la
          validation des correctifs, et je développe des fonctionnalités qui
          simplifient la configuration de la caméra.
      - title: "Apprentissage profond pour l'OCR et la lecture de codes-barres"
        text: >-
          Je travaille sur le volet apprentissage profond de la bibliothèque :
          des modèles qui lisent les caractères et les codes que les décodeurs
          classiques ne savent pas lire — abîmés, flous, peu contrastés, ou
          imprimés sur des surfaces courbes et réfléchissantes. Le travail va
          de l'entraînement et l'évaluation des modèles à l'intégration de
          l'inférence dans le pipeline C++, en tenant le même budget de latence
          et de mémoire que la voie classique.
    built: ["Aurora Imaging Library", "Caméra intelligente Aurora Focus", "OCR par apprentissage profond", "Lecture de codes-barres par apprentissage profond"]
    stack: ["C++", "algorithmes de vision industrielle", "apprentissage profond", "OCR", "apprentissage automatique", "imagerie embarquée"]
    tools: ["Visual Studio", "Git / GitHub", "CMake", "GTest", "clang-tidy / clang-format", "SonarQube", "Valgrind & sanitizers", "gdb", "JIRA", "Confluence", "Agile / Scrum", "CI/CD"]
    learned: |-
      - L'apprentissage profond prend tout son sens là où les décodeurs classiques s'arrêtent — codes abîmés, flous, peu contrastés — et leur cède partout ailleurs sur la latence et la prévisibilité. Choisir quelle moitié du problème confier à un modèle, c'est l'essentiel de la conception.
      - Un modèle qui gagne sur un jeu de test peut échouer sur le terrain, parce que les échecs d'un client sont les images que personne n'a pensé à mettre dans le jeu de test. La métrique utile est la façon dont il échoue, pas sa fréquence d'échec.
      - Faire tourner l'inférence dans un pipeline temps réel est d'abord un problème de mémoire et de débit, ensuite un problème d'apprentissage. Le prétraitement, les allocations et la localité de cache décident si un modèle tient dans le budget d'une image.
      - Sur la caméra intelligente, la contrainte est toute la conception. Le working set, les allocations sur le chemin critique et la marge processeur éliminent des approches bien avant la précision.
      - L'essentiel du métier se joue autour de l'algorithme : la documentation de référence, les exemples livrés, le contrat d'API convenu avec les équipes UI et QA, et les applications clientes qui révèlent les bogues qu'une suite de tests ne voit pas.
      - Livrer dans une équipe de cette taille tient autant du processus que du code. Une fonctionnalité est spécifiée dans Confluence, suivie dans JIRA, conditionnée à clang-tidy, clang-format et SonarQube en revue, puis prouvée par GTest et les sanitizers avant d'atteindre une branche de livraison. Un changement qui passe la revue mais pas l'outillage n'est pas livré.

  - period: "2022 — 2024"
    role: "Développeur logiciel II"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Géométrie et solveurs des modules 2D"
        text: >-
          J'ai maintenu et étendu les modules 2D — Model Finder, Edge Finder,
          Measurement, Metrology, Calibration et Bead — en implémentant la
          géométrie, l'algèbre linéaire et l'optimisation non linéaire qui les
          font tourner, en corrigeant des bogues de virgule flottante et d'API à
          état, et en étendant leurs tests de régression. J'ai co-conçu et livré
          l'API C++ publique de l'Advanced Geometric Matcher.
      - title: "Apprentissage automatique dans une bibliothèque géométrique"
        video: "CS4cs9xVecg"
        videoAlt: "Notes de la spécialisation en apprentissage profond"
        text: >-
          J'ai intégré de l'apprentissage automatique classique — forêts
          aléatoires et SVM — dans des modules jusque-là purement géométriques,
          pour classifier des motifs dans des scènes complexes. J'ai écrit les
          nouvelles API, leur documentation de référence et les exemples
          clients livrés avec, et j'ai encadré des stagiaires et des
          développeurs juniors sur le C++ moderne, le multithreading et la
          revue de code.
    built: ["API Advanced Geometric Matcher", "Modules 2D de la MIL", "Exemples d'API pour les clients"]
    stack: ["C++", "appariement géométrique", "métrologie", "optimisation non linéaire", "apprentissage classique"]
    tools: ["Visual Studio", "Git / GitHub", "CMake", "GTest", "JIRA", "Confluence", "Agile / Scrum", "revue de code"]
    learned: |-
      - C'est en écrivant la documentation et les exemples qu'une API est vraiment mise à l'épreuve. Presque toutes les questions renvoyées par les clients portaient sur l'interface, pas sur l'algorithme.
      - Une API C++ publique est une promesse qu'on ne peut pas retirer. Le nommage, l'ordre des paramètres, le comportement par défaut et la remontée des erreurs survivent à tous les détails d'implémentation derrière eux.
      - L'apprentissage automatique classique dans une bibliothèque géométrique doit rester diagnosticable. Une forêt aléatoire qui classe un motif doit échouer d'une manière qu'un ingénieur support peut expliquer à un client, ce qui a écarté des modèles que je ne pouvais pas inspecter.
      - Les bogues d'API à état et les écarts en virgule flottante sont les deux défauts que les tests de régression attrapent et que la revue de code laisse passer. Les deux ne ressemblent à rien dans un diff.
      - Encadrer des stagiaires m'a obligé à dire pourquoi et pas seulement quoi, et c'est là que j'ai trouvé les habitudes que je ne savais pas défendre.

  - period: "2019 — 2022"
    role: "Développeur logiciel"
    org: "Matrox Imaging"
    url: "https://video.matrox.com/en"
    note: "Matrox Imaging a rejoint Zebra Technologies en 2022 ; le travail s'est poursuivi sans interruption."
    work:
      - title: "Calibration, mesure et métrologie"
        video: "LcoPNbyuhZU"
        videoAlt: "Le traitement d'images industriel dans la Matrox Imaging Library"
        text: >-
          Mon premier poste après la maîtrise, sur les modules de mesure :
          Calibration, Measurement et Metrology. J'ai implémenté et débogué
          leurs algorithmes, écrit les tests et les exemples clients, et conçu
          l'Advanced Geometric Matcher, livré plus tard comme API publique.
      - title: "Solveurs non linéaires dans une base de code héritée"
        video: "sfLZ7v9gEnc"
        videoAlt: "Travail au cœur de la base de code de la Matrox Imaging Library"
        text: >-
          J'ai modernisé les solveurs géométriques d'une base de code C++
          vieille de plusieurs décennies, en remplaçant d'anciennes méthodes par
          de l'optimisation non linéaire, dont Levenberg–Marquardt, pour une
          précision sous-pixel et une stabilité numérique. J'ai traqué des
          fuites mémoire et des références pendantes, et bâti des suites de
          régression qui protègent un comportement dont dépendent des milliers
          d'applications installées.
      - title: "Apprentissage automatique dans la bibliothèque d'imagerie"
        text: >-
          J'ai rejoint l'équipe comme stagiaire début 2019 et implémenté des
          forêts aléatoires directement dans la Matrox Imaging Library, pour la
          catégorisation de défauts en temps réel sur des lignes de production.
          J'ai aussi construit des générateurs de jeux de données synthétiques
          et des bancs d'essai automatisés mesurant la précision des
          classifieurs et le débit d'inférence à chaque changement.
    built: ["Appariement de motifs", "Détection de contours", "Optimisation non linéaire", "Investigations mémoire", "Calibration", "Mesure et métrologie", "Forêts aléatoires en C++"]
    stack: ["C++", "optimisation non linéaire", "Levenberg–Marquardt", "stabilité numérique", "apprentissage classique"]
    tools: ["Visual Studio", "Git", "SVN", "GTest", "VMMap", "Valgrind", "JIRA", "Confluence"]
    learned: |-
      - Écrire un meilleur algorithme est la moitié facile. Le livrer dans une bibliothèque dont des milliers d'applications dépendent déjà, sans changer une réponse sur laquelle elles comptent, est la moitié difficile.
      - L'optimisation non linéaire ne vaut que par son estimation initiale et son critère d'arrêt. Levenberg–Marquardt converge proprement dans un article et oscille sur des données réelles tant que ces deux points ne sont pas réglés.
      - La précision sous-pixel est un problème de stabilité numérique. L'ordre des opérations, le conditionnement de la matrice et la tolérance de comparaison décident des deux dernières décimales, pas les maths au tableau.
      - Dans une base de code C++ vieille de plusieurs décennies, les bogues mémoire qui coûtent du temps sont les références pendantes et une propriété que personne n'a écrite. Les fuites, au moins, se signalent.
      - Construire la suite de régression avant de toucher à l'algorithme. C'est la seule chose qui rende possible la modification de code numérique hérité.

  - period: "2017 — 2019"
    role: "M.Sc.A., génie des systèmes de contrôle"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Moyenne 3,87/4 · Bourse de la Fondation Al Ghurair — 1 sur 100 parmi plus de 15 000 candidatures."
    work:
      - title: "Comment je suis arrivé au Canada"
        video: "BPkj-VETeX0"
        videoAlt: "À propos de la bourse de la Fondation Al Ghurair"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          La bourse a été accordée au mérite académique et a financé ma
          maîtrise. C'est ainsi que je suis arrivé à Montréal.
      - title: "Commande, robotique et temps réel"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotique et contrôle temps réel pendant la maîtrise"
        text: >-
          Chaque cours important se terminait par un projet tournant sur du
          vrai matériel : commande de robot et exécution de trajectoires,
          ordonnancement temps réel sous QNX, traitement d'images pour la
          localisation de pièces, et estimation d'état. Les cours couvraient le
          traitement d'images, la détection et l'estimation de signaux, la
          robotique, les systèmes d'exploitation temps réel, la commande non
          linéaire et stochastique, et les systèmes cyber-physiques.
      - title: "Extraction de caractéristiques, assemblage et commande multi-robots"
        text: >-
          J'ai implémenté l'extraction de caractéristiques SIFT et l'estimation
          d'homographies pour assembler des panoramas à partir de plusieurs
          photos, et construit un système de vision en MATLAB et C++ qui
          localisait et identifiait des pièces dans l'espace de travail d'un
          robot Fanuc à 6 axes. J'ai aussi écrit des algorithmes de consensus
          distribué en Python et exécuté du suivi de formation sur la flotte
          multi-robots réelle du Georgia Tech Robotarium.
    built: ["Théorie du contrôle", "Robotique", "Traitement d'images", "SIFT et homographie", "Commande de formation multi-robots"]
    stack: ["C++", "SIFT", "homographie", "commande numérique", "détection et estimation", "commande stochastique et robuste", "traitement d'images"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "robots Fanuc", "Georgia Tech Robotarium"]
    learned: |-
      - Une loi de commande peut être juste sur le papier et rester fausse si elle arrive dix millisecondes trop tard. L'échéance fait partie du cahier des charges.
      - La géométrie est la partie facile de l'appariement de caractéristiques. SIFT produit des candidats ; tout ce qui fait fonctionner un panorama ou un localisateur de pièces, c'est le rejet des aberrants ensuite.
      - L'estimation d'état est là où j'ai appris à pondérer un modèle et une mesure selon ce que chacun ment.
      - Exécuter des algorithmes de consensus sur la flotte réelle du Robotarium plutôt qu'en simulation montre à quel point un algorithme distribué porte sur ce qui se passe quand un robot cesse de répondre.

  - period: "2012 — 2017"
    role: "Ingénieur d'État, génie électrique — systèmes de contrôle"
    kind: "education"
    org: "École Nationale Polytechnique, Alger"
    url: "https://www.enp.edu.dz/en/"
    note: "Moyenne 17,5/20 · 5e sur 1 400 — top 1 % national."
    work:
      - title: "Deux années de classes préparatoires d'abord"
        video: "VjwIGG7Lbt0"
        videoAlt: "Les années de classes préparatoires à Alger"
        text: >-
          Mathématiques, physique et programmation, de 9 h à 18 h, six jours
          par semaine. Le classement national final décide de l'école où l'on
          entre.
      - title: "Systèmes de contrôle sur matériel réel"
        video: "eGPbNTXTd1I"
        videoAlt: "Projets de contrôle et d'automates pendant le diplôme d'ingénieur"
        text: >-
          J'ai construit des systèmes de contrôle face à du vrai matériel et à
          des contraintes d'usine : un régulateur de vitesse adaptatif pour
          véhicule autonome, et un programme d'automate pilotant une machine
          d'assemblage industrielle.
    built: ["Régulateur de vitesse adaptatif pour véhicule autonome", "Programme d'automate pour une machine d'assemblage industrielle"]
    stack: ["C", "MATLAB", "VHDL", "conception de commande", "identification de procédés", "commande optimale"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: |-
      - La première machine d'assemblage que j'ai programmée tombait en panne à cause des capteurs et du câblage, pas de la logique de commande sur laquelle j'avais passé tout le semestre.
      - Un programme d'automate s'écrit pour celui qui le déboguera à trois heures du matin sur un plancher d'usine, pas pour celui qui l'écrit.
      - Identifier un procédé à partir de mesures réelles est plus difficile que concevoir le régulateur qui suit. L'erreur habite le modèle.

skills:
  - group: "Langages"
    items: ["C++ (17/20)", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "VHDL", "SQL"]
  - group: "Vision industrielle"
    items: ["Aurora Imaging Library", "Matrox Imaging Library", "OpenCV", "appariement géométrique", "appariement de motifs", "calibration", "métrologie", "mesure de contours", "SIFT", "homographie", "transformations 2D et 3D"]
  - group: "Maths & algorithmes"
    items: ["optimisation non linéaire", "Levenberg–Marquardt", "moindres carrés non linéaires", "algèbre linéaire", "stabilité numérique", "théorie du contrôle", "apprentissage classique", "apprentissage profond"]
  - group: "C++ & systèmes"
    items: ["C++ moderne (templates, STL)", "multithreading et concurrence", "traitement d'images temps réel", "mémoire virtuelle et working set", "CMake", "GTest", "Clang / LLVM", "ASan / MSan", "Valgrind", "gdb", "multiplateforme Windows et Linux", "QNX", "ROS", "Docker"]
  - group: "Infonuagique & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Outils & pratiques"
    items: ["Visual Studio", "Git / GitHub", "SVN", "CMake", "CI/CD", "revue de code", "clang-tidy / clang-format", "SonarQube", "JIRA", "Confluence", "Agile / Scrum", "Docker", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)"]
  - group: "Langues"
    items: ["français", "anglais", "arabe"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---
