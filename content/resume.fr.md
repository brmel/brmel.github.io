---
title: "CV"
layout: "resume"
summary: "Ingénieur en vision industrielle et traitement d'images — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Développeur logiciel senior spécialisé en vision industrielle, traitement d'images et systèmes de contrôle."
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
      - title: "Les algorithmes sur lesquels d'autres livrent"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Démonstration de l'Aurora Imaging Library dans Aurora Vision Studio"
        text: >-
          Je suis l'un des ingénieurs responsables des algorithmes de la
          bibliothèque. Mon travail ne s'arrête pas au code : je fixe le
          comportement avec les équipes UI, documentation et test avant la
          livraison, et je vais voir de près les applications que les clients
          n'arrivent pas à faire fonctionner.
      - title: "L'inspection qui s'exécute dans la caméra"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "La caméra intelligente Aurora Focus en inspection sur un banc"
        text: >-
          J'ai porté la bibliothèque d'imagerie dans la caméra elle-même, pour
          que l'inspection s'exécute sur l'appareil plutôt que sur un PC relié.
          Il a fallu faire tenir les algorithmes dans bien moins de mémoire et
          surveiller chaque allocation.
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
      - title: "La géométrie sous les modules 2D"
        text: >-
          J'ai résolu, implémenté et débogué la géométrie, l'algèbre et
          l'optimisation non linéaire derrière Model Finder, Edge Finder,
          Measurement, Metrology, Calibration et Bead, et j'ai élargi les tests
          qui les protègent. J'ai aussi fait passer l'Advanced Geometric Matcher
          d'un algorithme interne à une API publique, conçue avec l'équipe.
      - title: "Faire entrer l'apprentissage automatique dans une bibliothèque géométrique"
        video: "CS4cs9xVecg"
        videoAlt: "Notes de la spécialisation en apprentissage profond"
        text: >-
          J'ai fait entrer l'apprentissage automatique classique dans des
          modules jusque-là purement géométriques, et j'ai écrit les nouvelles
          API et les exemples clients livrés avec. J'ai encadré des stagiaires.
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
      - title: "Apprendre le métier"
        video: "LcoPNbyuhZU"
        videoAlt: "Le traitement d'images industriel dans la Matrox Imaging Library"
        text: >-
          Mon premier emploi après la maîtrise, sur les modules qui mesurent :
          Calibration, Measurement et Metrology. C'est là que j'ai conçu
          l'Advanced Geometric Matcher, l'algorithme devenu plus tard une API
          publique.
      - title: "Travailler dans une grande base de code C++"
        video: "sfLZ7v9gEnc"
        videoAlt: "Travail au cœur de la base de code de la Matrox Imaging Library"
        text: >-
          J'ai remplacé d'anciens solveurs des modules de géométrie par des
          optimiseurs non linéaires, dont Levenberg–Marquardt, dans une
          bibliothèque dont des milliers d'applications installées dépendent
          déjà.
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
      - title: "Des systèmes, pas seulement des cours"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotique et contrôle temps réel pendant la maîtrise"
        text: >-
          J'ai terminé chaque cours qui comptait par quelque chose qui devait
          vraiment fonctionner : un robot qui devait atteindre le point, un
          contrôleur qui devait tenir son échéance, une caméra qui devait dire
          au bras où était la pièce.
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
      - title: "De l'ingénierie qui sort de la salle de cours"
        video: "eGPbNTXTd1I"
        videoAlt: "Projets de contrôle et d'automates pendant le diplôme d'ingénieur"
        text: >-
          J'ai terminé le diplôme en construisant des systèmes de contrôle face
          à du vrai matériel et à de vraies contraintes d'usine, pas à leurs
          simulations.
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
