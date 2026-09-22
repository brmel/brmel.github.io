---
title: "CV"
layout: "resume"
summary: "Ingénieur en vision industrielle et traitement d'images — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Développeur C++ senior : vision industrielle 2D et 3D, traitement d'images, optimisation non linéaire et systèmes de contrôle."
aliases: ["/fr/timeline/"]
role: "Développeur logiciel senior — vision industrielle et IA"
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
          Je développe et maintiens des algorithmes 2D et 3D de la
          bibliothèque : j'ajoute des fonctionnalités, j'investigue et corrige
          des bogues, j'assiste les clients dont les applications se comportent
          mal, et je participe à la planification de la feuille de route et du
          contenu de chaque version. Je définis le comportement des API et la
          compatibilité ascendante avec les équipes UI, documentation et QA
          avant la livraison.
      - title: "Traitement d'images sur la caméra intelligente"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "La caméra intelligente Aurora Focus en inspection sur un banc"
        text: >-
          Je porte des modules de traitement d'images sur la caméra
          intelligente Aurora Focus, en écrivant des algorithmes sous fortes
          contraintes de mémoire et de processeur. Le travail est full stack :
          je débogue des problèmes qui traversent l'interface et le backend,
          j'investigue le multithreading et la concurrence, je travaille avec
          l'équipe de test sur les correctifs, et j'implémente des
          fonctionnalités qui simplifient la configuration de la caméra.
    built: ["Aurora Imaging Library", "Caméra intelligente Aurora Focus"]
    stack: ["C++", "algorithmes de vision industrielle", "imagerie embarquée"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA"]
    learned: >-
      J'ai appris qu'une bibliothèque n'est finie que lorsque l'algorithme, la
      documentation et les tests disent la même chose. En général, je découvre
      qu'ils se contredisent dans l'application d'un client, pas dans les
      tests.

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
          nouvelles API, leur documentation et les exemples clients livrés avec,
          et j'ai encadré des stagiaires sur le C++ moderne, le multithreading
          et la revue de code.
    built: ["API Advanced Geometric Matcher", "Modules 2D de la MIL", "Exemples d'API pour les clients"]
    stack: ["C++", "appariement géométrique", "métrologie", "optimisation non linéaire", "apprentissage classique"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA", "Agile"]
    learned: >-
      J'ai appris que c'est en écrivant la documentation et les exemples qu'une
      API est vraiment mise à l'épreuve. Les questions qui reviennent portent
      presque toujours sur l'interface, pas sur l'algorithme.

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
          Mon premier emploi après la maîtrise, sur les modules de mesure :
          Calibration, Measurement et Metrology. J'ai implémenté et débogué
          leurs algorithmes, écrit des tests et des exemples clients, et conçu
          l'Advanced Geometric Matcher devenu plus tard une API publique.
      - title: "Solveurs non linéaires dans une base de code héritée"
        video: "sfLZ7v9gEnc"
        videoAlt: "Travail au cœur de la base de code de la Matrox Imaging Library"
        text: >-
          J'ai modernisé les solveurs géométriques d'une base de code C++
          vieille de plusieurs décennies, en remplaçant d'anciennes méthodes par
          de l'optimisation non linéaire, dont Levenberg–Marquardt, pour une
          précision sous-pixel et une stabilité numérique. J'ai traqué des
          fuites mémoire et des références pendantes, et bâti des suites de
          régression pour protéger un comportement dont dépendent des milliers
          d'applications installées.
    built: ["Appariement de motifs", "Détection de contours", "Optimisation non linéaire", "Investigations mémoire", "Calibration", "Mesure et métrologie"]
    stack: ["C++", "optimisation non linéaire", "Levenberg–Marquardt", "apprentissage classique"]
    tools: ["Visual Studio", "Git", "SVN"]
    learned: >-
      J'ai appris qu'écrire un meilleur algorithme est la partie facile.
      L'intégrer à une bibliothèque dont des milliers d'applications dépendent
      déjà, sans changer une réponse sur laquelle elles comptent, est la partie
      difficile.

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
          maîtrise. C'est la raison pour laquelle la suite de cette page se
          passe à Montréal.
      - title: "Commande, robotique et temps réel"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotique et contrôle temps réel pendant la maîtrise"
        text: >-
          J'ai terminé chaque cours qui comptait par quelque chose qui devait
          tourner sur du vrai matériel : commande de robot et exécution de
          trajectoires, ordonnancement temps réel sous QNX, traitement d'images
          pour la localisation de pièces, et estimation d'état.
    built: ["Théorie du contrôle", "Robotique", "Traitement d'images"]
    stack: ["C++", "commande numérique", "détection et estimation", "commande stochastique et robuste", "traitement d'images"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "robots Fanuc"]
    learned: >-
      J'ai appris qu'une loi de commande peut être juste sur le papier et rester
      fausse si elle arrive dix millisecondes trop tard. L'échéance fait partie
      du cahier des charges.

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
          par semaine, avec un classement final qui décide de l'école où l'on
          entre. J'y ai appris à travailler un problème jusqu'à ce qu'il soit
          réellement résolu.
      - title: "Systèmes de contrôle sur matériel réel"
        video: "eGPbNTXTd1I"
        videoAlt: "Projets de contrôle et d'automates pendant le diplôme d'ingénieur"
        text: >-
          J'ai terminé le diplôme en construisant des systèmes de contrôle face
          à du vrai matériel et à des contraintes d'usine : un régulateur de
          vitesse adaptatif pour véhicule autonome, et un programme d'automate
          pilotant une machine d'assemblage industrielle.
    built: ["Régulateur de vitesse adaptatif pour véhicule autonome", "Programme d'automate pour une machine d'assemblage industrielle"]
    stack: ["C", "MATLAB", "VHDL", "conception de commande", "identification de procédés", "commande optimale"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: >-
      J'ai appris que le matériel se moque de l'élégance du modèle. La première
      machine d'assemblage que j'ai programmée tombait en panne à cause des
      capteurs et du câblage, pas de la logique de commande sur laquelle j'avais
      passé tout le semestre.

skills:
  - group: "Langages"
    items: ["C++", "C", "Python", "Dart / Flutter", "TypeScript", "MATLAB", "VHDL", "SQL"]
  - group: "Vision industrielle"
    items: ["Aurora Imaging Library", "Matrox Imaging Library", "OpenCV", "appariement géométrique", "calibration", "métrologie", "mesure de contours"]
  - group: "Maths & algorithmes"
    items: ["optimisation non linéaire", "Levenberg–Marquardt", "théorie du contrôle", "apprentissage classique", "apprentissage profond", "pipelines multi-agents"]
  - group: "Infonuagique & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Systèmes & outils"
    items: ["systèmes temps réel", "QNX", "ROS", "Git / GitHub", "SVN", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "JIRA"]
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
