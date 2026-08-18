---
title: "CV"
layout: "resume"
disableShare: true
summary: "Ingénieur en vision industrielle et traitement d'images — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Développeur logiciel senior spécialisé en vision industrielle, traitement d'images et systèmes de contrôle."
ShowBreadCrumbs: false
aliases: ["/fr/timeline/", "/fr/about/"]
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

# Le parcours, période par période. La structure vient de
# layouts/partials/career-timeline.html ; seuls les mots changent d'une langue
# à l'autre. `learned` tient en une phrase — c'est la ligne qu'on retient.
experience:
  - period: "2024 — Aujourd'hui"
    role: "Développeur logiciel senior"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Des algorithmes sur lesquels d'autres livrent"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l'Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          L'un des ingénieurs responsables des algorithmes de la bibliothèque.
          Le travail va bien au-delà du code : fixer le comportement avec les
          équipes UI, documentation et test avant la livraison, et entrer dans
          les applications que les clients n'arrivent pas à faire fonctionner.
      - title: "L'inspection qui s'exécute dans la caméra"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "La caméra intelligente Aurora Focus en inspection sur un banc"
        text: >-
          Porter la bibliothèque d'imagerie dans la caméra elle-même, pour que
          l'inspection s'exécute sur l'appareil plutôt que sur un PC relié.
    built: ["Aurora Imaging Library", "Caméra intelligente Aurora Focus"]
    stack: ["C++", "algorithmes de vision industrielle", "imagerie embarquée"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA"]
    learned: >-
      Une bibliothèque ne devient un produit que lorsque l'algorithme, la
      documentation et les tests disent la même chose — et les désaccords
      apparaissent dans l'application d'un client bien avant les tests.

  - period: "2022 — 2024"
    role: "Développeur logiciel II"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "La géométrie sous les modules 2D"
        text: >-
          Model Finder, Edge Finder, Measurement, Metrology, Calibration et
          Bead — résoudre, implémenter et déboguer la géométrie, l'algèbre et
          l'optimisation non linéaire qui les portent, et élargir les tests qui
          les protègent. L'Advanced Geometric Matcher est passé d'un algorithme
          interne à une API publique, conçue avec l'équipe.
      - title: "Faire entrer l'apprentissage automatique dans une bibliothèque géométrique"
        video: "CS4cs9xVecg"
        videoAlt: "Notes de la spécialisation en apprentissage profond"
        text: >-
          Intégrer l'apprentissage automatique classique dans des modules
          jusque-là purement géométriques, puis documenter les nouvelles API et
          écrire les exemples clients livrés avec. Encadrement de stagiaires.
    built: ["API Advanced Geometric Matcher", "Modules 2D de la MIL", "Exemples d'API pour les clients"]
    stack: ["C++", "appariement géométrique", "métrologie", "optimisation non linéaire", "apprentissage classique"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA", "Agile"]
    learned: >-
      C'est en écrivant la documentation et les exemples qu'une API est
      vraiment mise à l'épreuve — les questions qui reviennent portent sur
      l'interface, presque jamais sur l'algorithme.

  - period: "2019 — 2022"
    role: "Développeur logiciel"
    org: "Matrox Imaging"
    url: "https://video.matrox.com/en"
    note: "Matrox Imaging a rejoint Zebra Technologies en 2022 ; le travail s'est poursuivi sans interruption."
    work:
      - title: "Apprendre le métier"
        video: "LcoPNbyuhZU"
        videoAlt: "Le traitement d'images industriel dans la Matrox Imaging Library"
        text: >-
          Premier emploi après la maîtrise, sur les modules qui mesurent :
          Calibration, Measurement et Metrology. Conception de l'Advanced
          Geometric Matcher, l'algorithme devenu plus tard une API publique.
      - title: "Travailler dans une grande base de code C++"
        video: "sfLZ7v9gEnc"
        videoAlt: "Travail au cœur de la base de code de la Matrox Imaging Library"
        text: >-
          Remplacer d'anciens solveurs des modules de géométrie par des
          optimiseurs non linéaires, dont Levenberg–Marquardt, dans une
          bibliothèque dont des milliers d'applications installées dépendent.
    built: ["Appariement de motifs", "Détection de contours", "Calibration", "Mesure et métrologie"]
    stack: ["C++", "optimisation non linéaire", "Levenberg–Marquardt", "apprentissage classique"]
    tools: ["Visual Studio", "Git", "SVN"]
    learned: >-
      Écrire un meilleur algorithme est la partie courte ; l'intégrer à une
      bibliothèque dont d'autres dépendent déjà, sans changer une réponse sur
      laquelle ils comptent, est la partie longue.

  - period: "2017 — 2019"
    role: "M.Sc.A., génie des systèmes de contrôle"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Moyenne 3,87/4 · Bourse de la Fondation Al Ghurair — 1 sur 100 parmi plus de 15 000 candidatures."
    work:
      - title: "Comment je suis arrivé au Canada"
        video: "BPkj-VETeX0"
        videoAlt: "À propos de la bourse de la Fondation Al Ghurair"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          La bourse a été accordée au mérite académique et a financé la
          maîtrise. C'est la raison pour laquelle la suite de cette page se
          passe à Montréal.
      - title: "Des systèmes, pas seulement des cours"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotique et contrôle temps réel pendant la maîtrise"
        text: >-
          Chaque cours qui comptait se terminait par quelque chose qui devait
          fonctionner : un robot qui devait atteindre le point, un contrôleur
          qui devait tenir son échéance, une caméra qui devait dire au bras où
          était la pièce.
    built: ["Théorie du contrôle", "Robotique", "Traitement d'images"]
    stack: ["C++", "commande numérique", "détection et estimation", "commande stochastique et robuste", "traitement d'images"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "robots Fanuc"]
    learned: >-
      Une loi de commande juste sur le papier et en retard de dix
      millisecondes est fausse — l'échéance fait partie du cahier des charges,
      pas des détails d'implémentation.

  - period: "2012 — 2017"
    role: "Ingénieur d'État, génie électrique — systèmes de contrôle"
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
          entre. C'est de là que vient l'habitude de travailler un problème
          jusqu'à ce qu'il soit réellement résolu.
      - title: "De l'ingénierie qui sort de la salle de cours"
        video: "eGPbNTXTd1I"
        videoAlt: "Projets de contrôle et d'automates pendant le diplôme d'ingénieur"
        text: >-
          Le diplôme s'est terminé sur des systèmes de contrôle construits face
          à du vrai matériel et à de vraies contraintes d'usine, plutôt qu'à
          leurs simulations.
    built: ["Régulateur de vitesse adaptatif pour véhicule autonome", "Programme d'automate pour une machine d'assemblage industrielle"]
    stack: ["C", "MATLAB", "VHDL", "conception de commande", "identification de procédés", "commande optimale"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: >-
      Le matériel se moque de l'élégance du modèle : la première machine
      d'assemblage que j'ai programmée passait ses pannes sur des capteurs et
      du câblage, pas sur la logique de commande travaillée tout le semestre.

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
