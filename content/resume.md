---
title: "Resume"
layout: "resume"
summary: "Machine vision and image processing engineer — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Senior Software Developer specialising in machine vision, image processing and control systems."
aliases: ["/timeline/", "/about/"]
role: "Senior Software Developer — machine vision and AI"
location: "Montréal, Québec"
contact:
  - label: "Email"
    url: "mailto:mellah.brahim.redouane@gmail.com"
  - label: "LinkedIn"
    url: "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - label: "GitHub"
    url: "https://github.com/brmel"
  - label: "X"
    url: "https://x.com/BrmelB"

experience:
  - period: "2024 — Present"
    role: "Senior Software Developer"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "The algorithms other people ship on"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Walkthrough of the Aurora Imaging Library in Aurora Vision Studio"
        text: >-
          I am one of the engineers responsible for the algorithms in the
          library. The job runs past writing them: I agree the behaviour with
          the UI, documentation and test teams before it ships, and I go into
          the customer applications that will not work to find out why.
      - title: "Inspection that runs on the camera"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "The Aurora Focus smart camera inspecting parts on a bench"
        text: >-
          I moved the imaging library onto the camera itself, so inspection
          runs on the device instead of a PC wired to it. That meant fitting
          the algorithms into far less memory and watching every allocation.
    built: ["Aurora Imaging Library", "Aurora Focus smart camera"]
    stack: ["C++", "machine vision algorithms", "embedded / edge imaging"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA"]
    learned: >-
      I learned that a library is only finished when the algorithm, the
      documentation and the tests agree with each other. I usually find out they
      disagree in a customer's application, not in a test suite.

  - period: "2022 — 2024"
    role: "Software Developer II"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "The geometry underneath the 2D modules"
        text: >-
          I solved, implemented and debugged the geometry, algebra and
          non-linear optimisation behind Model Finder, Edge Finder, Measurement,
          Metrology, Calibration and Bead, and widened the tests that guard
          them. I also took the Advanced Geometric Matcher from an algorithm to
          a public API, designed with the team.
      - title: "Bringing machine learning into a geometric library"
        video: "CS4cs9xVecg"
        videoAlt: "Notes from the deep learning specialisation"
        text: >-
          I brought classical machine learning into modules that had been
          purely geometric, and wrote the new APIs and the customer examples
          that shipped with them. I supervised trainees and interns.
    built: ["Advanced Geometric Matcher API", "MIL 2D modules", "customer-facing API examples"]
    stack: ["C++", "geometric matching", "metrology", "non-linear optimisation", "classical ML"]
    tools: ["Visual Studio", "Git / GitHub", "JIRA", "Agile"]
    learned: >-
      I learned that writing the documentation and the examples is what really
      tests an API design. The questions that come back are almost always about
      the interface, not about the algorithm.

  - period: "2019 — 2022"
    role: "Software Developer"
    org: "Matrox Imaging"
    url: "https://video.matrox.com/en"
    note: "Matrox Imaging became part of Zebra Technologies in 2022; the work continued without a break."
    work:
      - title: "Learning the industry"
        video: "LcoPNbyuhZU"
        videoAlt: "Industrial image processing in the Matrox Imaging Library"
        text: >-
          My first job after the master's, on the modules that measure things:
          Calibration, Measurement and Metrology. I designed the Advanced
          Geometric Matcher here — the algorithm that later became a public
          API.
      - title: "Working inside a large C++ codebase"
        video: "sfLZ7v9gEnc"
        videoAlt: "Working through the Matrox Imaging Library codebase"
        text: >-
          I replaced older solvers in the geometry modules with non-linear
          optimisers, Levenberg–Marquardt among them, in a library whose
          behaviour thousands of installed applications already depend on.
    built: ["Pattern matching", "Edge detection", "Non-linear optimisation", "Memory investigations", "Calibration", "Measurement and metrology"]
    stack: ["C++", "non-linear optimisation", "Levenberg–Marquardt", "classical ML"]
    tools: ["Visual Studio", "Git", "SVN"]
    learned: >-
      I learned that writing a better algorithm is the easy half. Getting it
      into a library thousands of applications already depend on, without
      changing an answer they rely on, is the hard half.

  - period: "2017 — 2019"
    role: "M.Sc., Control Systems Engineering"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "GPA 3.87/4 · Al Ghurair Foundation Scholarship — 1 of 100 selected from more than 15,000 applicants."
    work:
      - title: "How I got to Canada"
        video: "BPkj-VETeX0"
        videoAlt: "On the Al Ghurair Foundation scholarship"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          The scholarship was awarded on academic merit and paid for the
          master's. It is the reason the rest of this page happens in Montréal.
      - title: "Systems, not only coursework"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotics and real-time control work during the master's"
        text: >-
          I finished every course that mattered with something that had to
          actually run: a robot that had to reach the point, a controller that
          had to hold its deadline, a camera that had to tell the arm where the
          part was.
    built: ["Control theory", "Robotics", "Image processing"]
    stack: ["C++", "digital control", "detection and estimation", "stochastic and robust control", "image processing"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "Fanuc robots"]
    learned: >-
      I learned that a control law can be correct on paper and still be wrong
      if it arrives ten milliseconds late. The deadline is part of the
      specification.

  - period: "2012 — 2017"
    role: "B.Eng., Electrical Engineering — Control Systems"
    kind: "education"
    org: "École Nationale Polytechnique, Algiers"
    url: "https://www.enp.edu.dz/en/"
    note: "GPA 17.5/20 · graduated 5th of 1,400 — top 1% nationally."
    work:
      - title: "Two years of preparatory classes first"
        video: "VjwIGG7Lbt0"
        videoAlt: "The preparatory-class years in Algiers"
        text: >-
          Mathematics, physics and programming, nine to six, six days a week,
          with the ranking at the end deciding which school you enter. I learned
          there to keep working a problem until it is actually solved.
      - title: "Engineering that left the classroom"
        video: "eGPbNTXTd1I"
        videoAlt: "Control systems and PLC projects during the engineering degree"
        text: >-
          I finished the degree building control systems against real hardware
          and real factory constraints, not simulations of them.
    built: ["Adaptive cruise control for an autonomous vehicle", "PLC program for an industrial assembly machine"]
    stack: ["C", "MATLAB", "VHDL", "control design", "process identification", "optimal control"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: >-
      I learned that hardware does not care how elegant the model is. The first
      assembly machine I programmed failed on sensors and wiring, not on the
      control logic I had spent the whole term on.

skills:
  - group: "Languages"
    items: ["C++", "C", "Python", "Dart / Flutter", "TypeScript", "MATLAB", "VHDL", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library", "Matrox Imaging Library", "OpenCV", "geometric matching", "calibration", "metrology", "edge measurement"]
  - group: "Maths & algorithms"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "control theory", "classical ML", "deep learning", "multi-agent pipelines"]
  - group: "Cloud & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Systems & tools"
    items: ["real-time systems", "QNX", "ROS", "Git / GitHub", "SVN", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "JIRA"]
  - group: "Spoken"
    items: ["French", "English", "Arabic"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---
