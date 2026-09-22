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
      - title: "Core 2D and 3D vision algorithms"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Walkthrough of the Aurora Imaging Library in Aurora Vision Studio"
        text: >-
          I develop and maintain 2D and 3D algorithms in the library: I add
          features, investigate and fix bugs, support customers whose
          applications misbehave, and help plan the roadmap and the work that
          completes each release. I specify API behaviour and backward
          compatibility with the UI, documentation and QA teams before it
          ships.
      - title: "Image processing on the smart camera"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "The Aurora Focus smart camera inspecting parts on a bench"
        text: >-
          I port image processing modules onto the Aurora Focus smart camera,
          writing algorithms under tight memory and CPU constraints. The work is
          full stack: I debug issues that cross the UI and the backend,
          investigate multithreading and concurrency problems, work with the
          test team on fixes, and implement features that make the camera
          simpler to configure.
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
      - title: "Geometry and solvers behind the 2D modules"
        text: >-
          I maintained and extended the 2D modules — Model Finder, Edge Finder,
          Measurement, Metrology, Calibration and Bead — implementing the
          geometry, linear algebra and non-linear optimisation they run on,
          fixing floating-point and stateful API bugs, and extending their
          regression tests. I co-designed and shipped the public C++ API for the
          Advanced Geometric Matcher.
      - title: "Machine learning inside a geometric library"
        video: "CS4cs9xVecg"
        videoAlt: "Notes from the deep learning specialisation"
        text: >-
          I integrated classical machine learning — Random Forests and SVMs —
          into modules that had been purely geometric, to classify patterns in
          complex scenes. I wrote the new APIs, their documentation and the
          customer examples that shipped with them, and mentored interns and
          trainees on modern C++, multithreading and code review.
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
      - title: "Calibration, measurement and metrology"
        video: "LcoPNbyuhZU"
        videoAlt: "Industrial image processing in the Matrox Imaging Library"
        text: >-
          My first job after the master's, on the measurement modules:
          Calibration, Measurement and Metrology. I implemented and debugged
          their algorithms, wrote tests and customer examples, and designed the
          Advanced Geometric Matcher that later became a public API.
      - title: "Non-linear solvers in a legacy C++ codebase"
        video: "sfLZ7v9gEnc"
        videoAlt: "Working through the Matrox Imaging Library codebase"
        text: >-
          I modernised the geometric solvers in a multi-decade C++ codebase,
          replacing older methods with non-linear optimisation including
          Levenberg–Marquardt for sub-pixel accuracy and numerical stability. I
          tracked down memory leaks and dangling references, and built
          regression suites to protect behaviour that thousands of installed
          applications depend on.
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
      - title: "Control, robotics and real-time systems"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotics and real-time control work during the master's"
        text: >-
          I finished every course that mattered with something that had to run
          on real hardware: robot control and trajectory execution, real-time
          scheduling under QNX, image processing for part localisation, and
          state estimation.
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
      - title: "Control systems on real hardware"
        video: "eGPbNTXTd1I"
        videoAlt: "Control systems and PLC projects during the engineering degree"
        text: >-
          I finished the degree building control systems against real hardware
          and factory constraints: an adaptive cruise controller for an
          autonomous vehicle, and a PLC program driving an industrial assembly
          machine.
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
