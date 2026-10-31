---
title: "Resume"
layout: "resume"
lastmod: 2026-10-30
description: "Senior Software Developer with seven years of production C++: 2D and 3D machine vision, machine learning and deep learning, and today generative AI."
role: "Senior Software Developer in Montréal: production C++ for machine vision, machine learning and deep learning"
location: "Montréal, Québec"
sameAs:
  - "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - "https://github.com/brmel"
  - "https://x.com/BrmelB"

highlights:
  - title: "Machine vision"
    text: "2D and 3D algorithms that find, measure and inspect parts: pattern matching, edge detection, calibration and metrology."
  - title: "Machine learning"
    text: "Decision trees, random forests, SVMs and k-means in C++, from prototype to a tested, documented library feature."
  - title: "Deep learning"
    text: "Object detection and OCR models benchmarked on CPU and GPU, and the accepted ones taken to production."
  - title: "Smart cameras"
    text: "Vision algorithms that fit a camera’s limited memory and processing power."
  - title: "Numerical algorithms"
    text: "Non-linear optimisation for sub-pixel accuracy, guarded by regression tests."
  - title: "Modern C++"
    text: "Multithreaded code, memory measured with [MemoryTracer](/projects/memorytracer/), tests and sanitizers."

experience:
  - period: "Aug 2026 — Present"
    role: "Senior Software Developer, Generative AI"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Agents and retrieval"
        text: >-
          I build agentic workflows and retrieval-augmented generation
          (RAG), and the evaluations that decide when an agent is ready to
          ship.

  - period: "Jul 2024 — Aug 2026"
    role: "Senior Software Developer, Aurora Imaging Library"
    org: "Zebra Technologies"
    work:
      - title: "2D and 3D vision algorithms"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Walkthrough of the Aurora Imaging Library in Aurora Vision Studio"
        text: >-
          I owned Edge Finder, Geometric Matcher and Calibration in the
          Aurora Imaging Library, Zebra’s machine vision SDK, from feature
          to release: API design, bug fixes, documentation, code examples
          and customer support. I agreed API behaviour and backward
          compatibility with the UI, documentation and QA teams, and helped
          plan the roadmap.
      - title: "Smart cameras"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "A Zebra smart camera inspecting parts on a bench"
        text: >-
          I brought the library’s image processing to Zebra’s Aurora Focus
          smart cameras, within their limited memory and processing power.
          From the user interface to the backend, I fixed multithreading
          and concurrency bugs and built features that make the camera
          easier to configure.
      - title: "Machine learning in C++"
        text: >-
          I implemented decision trees, random forests and k-means in the
          library’s C++: multithreaded, thread-safe, with early stopping.
      - title: "Deep learning"
        text: >-
          I benchmarked deep learning models for object detection, OCR and
          text detection on CPU and GPU, tuned their hyperparameters and
          designed the metrics that decide whether a model ships, then took
          the accepted ones to production.

  - period: "Jun 2022 — Jun 2024"
    role: "Software Developer II, Image Processing"
    org: "Zebra Technologies"
    work:
      - title: "The Advanced Geometric Matcher"
        text: >-
          I took the Advanced Geometric Matcher (AGM), a new pattern-matching
          tool, from research and prototype to production, and designed its
          public C++ API with the team. It ships today in Zebra’s Aurora
          Imaging Library.
      - title: "Machine learning in geometric tools"
        text: >-
          I added random forests and SVMs to modules that had been purely
          geometric, so they could classify patterns in cluttered scenes,
          with new APIs, documentation and examples. I also mentored interns
          and junior developers on modern C++, multithreading and code
          review.
      - title: "Numerical bugs and regression tests"
        text: >-
          I fixed numerical bugs and API regressions, and added unit,
          integration and randomised tests to the regression suites.

  - period: "Jun 2019 — Jun 2022"
    role: "Software Developer, Image Processing"
    org: "Matrox Imaging"
    note: "Matrox Imaging, in Dorval, became part of Zebra Technologies in 2022."
    work:
      - title: "Calibration, measurement and metrology"
        text: >-
          I implemented and debugged the library’s Calibration, Measurement
          and Metrology modules, with their tests, documentation and
          examples, and supported the customers who used them. I also
          maintained Model Finder, Edge Finder and Bead.
      - title: "Non-linear solvers"
        text: >-
          I replaced older geometric solvers in the library’s decades-old
          C++ codebase with non-linear optimisation (including
          Levenberg–Marquardt), for sub-pixel accuracy and numerical
          stability. I tracked down memory leaks and dangling references,
          and built regression suites that protect the behaviour thousands
          of installed applications depend on.

  - period: "Jan 2019 — May 2019"
    role: "Software Development Intern"
    org: "Matrox Imaging"
    work:
      - title: "A random forest classifier"
        text: >-
          I built a random forest classifier into the Matrox Imaging Library
          (today Zebra’s Aurora Imaging Library), with multithreaded training
          and warm start, so production lines could sort defects in real
          time, and the synthetic datasets and automated benchmarks that
          measured its precision and speed on every change.

  - period: "2017 — 2019"
    role: "Master of Engineering (M.Eng.), Electrical Engineering — Control Systems"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Professional master’s with an industrial internship · GPA 3.87/4 · Al Ghurair Foundation Scholarship — 1 of about 100 recipients from more than 15,000 applicants."
    work:
      - title: "How I got to Canada"
        video: "BPkj-VETeX0"
        videoAlt: "On the Al Ghurair Foundation scholarship"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          The scholarship was awarded on academic merit and paid for the
          master’s. It’s how I came to Montréal.
      - title: "Projects on real hardware"
        text: >-
          Every major course ended in a project on real hardware: real-time
          scheduling under QNX, a MATLAB and C++ vision system that located
          parts for a Fanuc 6-axis robot, SIFT panorama stitching, and
          formation tracking on the Georgia Tech Robotarium’s robot fleet.

  - period: "2012 — 2017"
    role: "Engineering degree (Diplôme d’ingénieur d’État), Electrical Engineering — Control Systems"
    kind: "education"
    org: "École Nationale Polytechnique, Algiers"
    url: "https://www.enp.edu.dz/en/"
    note: "GPA 17.5/20 · ranked 5th of 1,400 in the national entrance exam after the preparatory classes (top 1%)."
    work:
      - title: "Preparatory classes"
        text: >-
          Two years of intensive mathematics, physics and programming,
          before the national ranking that decides which engineering school
          you enter.
      - title: "Control systems on real hardware"
        text: >-
          I built an adaptive cruise controller for an autonomous vehicle
          and a PLC program that drives an industrial assembly machine.

skills:
  - group: "Languages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library", "OpenCV", "pattern matching", "calibration", "metrology", "edge measurement", "SIFT", "homography", "2D and 3D geometry"]
  - group: "Machine learning"
    items: ["decision trees", "random forests", "SVMs", "k-means", "scikit-learn", "deep learning", "object detection", "OCR", "model evaluation", "hyperparameter tuning"]
  - group: "Maths"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "linear algebra", "numerical stability", "control theory"]
  - group: "C++ & systems"
    items: ["modern C++", "multithreading and concurrency", "virtual memory", "CMake", "GTest", "ASan / MSan", "Valgrind", "gdb", "Windows and Linux", "Docker"]
  - group: "Generative AI"
    items: ["agentic workflows", "RAG", "agent evaluation"]
  - group: "Tools"
    items: ["Git / GitHub", "SVN", "CI/CD", "code review", "clang-tidy", "SonarQube", "Visual Studio", "JIRA", "Confluence", "Google Cloud", "Firebase", "FastAPI"]
  - group: "Spoken"
    items: ["French (native)", "English (professional)", "Arabic (native)"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---
