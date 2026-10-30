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
    text: "2D and 3D algorithms that find, measure and inspect parts in factory images: pattern matching, edge detection, calibration and metrology."
  - title: "Machine learning to production"
    text: "From a first prototype to a tested, documented feature of a C++ library that ships to customers."
  - title: "Deep learning evaluation"
    text: "Object detection, OCR and text detection models benchmarked on CPU and GPU, against the metrics that decide whether a model ships."
  - title: "Constrained hardware"
    text: "Vision algorithms that fit the memory and processing limits of smart cameras."
  - title: "Numerical algorithms"
    text: "Non-linear optimisation for sub-pixel accuracy, with regression tests that guard every numerical result."
  - title: "Modern C++"
    text: "Safe multithreaded code, memory measured with [MemoryTracer](/projects/memorytracer/), code review, automated tests and sanitizers."

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
          ship, with the same discipline I used for deep learning models.
    stack: ["agentic workflows", "RAG", "agent evaluation"]

  - period: "Jul 2024 — Aug 2026"
    role: "Senior Software Developer, Aurora Imaging Library"
    org: "Zebra Technologies"
    work:
      - title: "Core 2D and 3D vision algorithms"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Walkthrough of the Aurora Imaging Library in Aurora Vision Studio"
        text: >-
          I owned vision algorithms in the Aurora Imaging Library, Zebra’s
          machine vision SDK (Edge Finder, Geometric Matcher and
          Calibration), from feature to release: API design, bug fixes,
          documentation and the code examples that ship with each release,
          and direct support when a customer’s application failed in
          production. I agreed API behaviour and backward compatibility
          with the UI, documentation and QA teams, and helped plan the
          release roadmap.
      - title: "Image processing on smart cameras"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "A Zebra smart camera inspecting parts on a bench"
        text: >-
          I brought the library’s image processing to Zebra’s Aurora Focus
          smart cameras, with algorithms that fit the camera’s limited
          memory and processing power. I worked from the user interface to
          the backend: I fixed multithreading and concurrency bugs,
          validated the fixes with the QA team, and built features that
          make the camera easier to configure.
      - title: "Classical machine learning in C++"
        text: >-
          I implemented decision trees, random forests and k-means in the
          library’s C++: multithreaded, thread-safe, and with early stopping.
      - title: "Deep learning for OCR and object detection"
        text: >-
          I benchmarked deep learning models for object detection, OCR and
          text detection on CPU and GPU, tuned their hyperparameters, and
          designed the metrics that decide whether a model ships. Then I took
          the accepted ones to production.
    stack: ["C++", "machine vision", "machine learning", "deep learning", "OCR", "smart cameras"]

  - period: "Jun 2022 — Jun 2024"
    role: "Software Developer II, Image Processing"
    org: "Zebra Technologies"
    work:
      - title: "The Advanced Geometric Matcher, from research to production"
        text: >-
          I took the Advanced Geometric Matcher (AGM), a new pattern-matching
          tool, from research and prototype to production, and designed its
          public C++ API with the team. It ships today in Zebra’s Aurora
          Imaging Library.
      - title: "Machine learning inside a geometric library"
        text: >-
          I added classical machine learning (random forests and SVMs) to
          modules that had been purely geometric, to classify patterns in
          cluttered scenes, with the new APIs, their reference documentation
          and customer examples. I also mentored interns and junior
          developers on modern C++, multithreading and code review.
      - title: "Numerical bugs and regression tests"
        text: >-
          I fixed numerical bugs and API regressions, and added unit,
          integration and randomised tests to the regression suites.
    stack: ["C++", "geometric matching", "public API design", "classical ML", "regression testing"]

  - period: "Jun 2019 — Jun 2022"
    role: "Software Developer, Image Processing"
    org: "Matrox Imaging"
    note: "Matrox Imaging, in Dorval, became part of Zebra Technologies in 2022."
    work:
      - title: "Calibration, measurement and metrology"
        text: >-
          My first role after the master’s: I implemented and debugged the
          library’s Calibration, Measurement and Metrology modules, wrote
          their tests, documentation and customer examples, and supported
          the customers who used them. I also maintained Model Finder, Edge
          Finder and Bead.
      - title: "Non-linear solvers in a legacy C++ codebase"
        text: >-
          I replaced older geometric solvers in the library’s decades-old
          C++ codebase with non-linear optimisation (including
          Levenberg–Marquardt), for sub-pixel accuracy and numerical
          stability. I tracked down memory leaks and dangling references,
          and built regression suites that protect the behaviour thousands
          of installed applications depend on.
    stack: ["C++", "calibration", "metrology", "non-linear optimisation", "Levenberg–Marquardt", "numerical stability"]

  - period: "Jan 2019 — May 2019"
    role: "Software Development Intern"
    org: "Matrox Imaging"
    work:
      - title: "Machine learning in the imaging library"
        text: >-
          I built a random forest classifier into the Matrox Imaging Library
          (today Zebra’s Aurora Imaging Library), with multithreaded training
          and warm start, so that production lines could sort defects in real
          time. I also built synthetic dataset generators and automated
          benchmarks that measured the classifier’s precision and speed on
          every change.
    stack: ["C++", "random forests", "multithreading", "benchmarking"]

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
          Every major course ended in a project on real hardware: robot
          control and trajectory execution, real-time scheduling under
          QNX, image processing to locate parts, and state estimation.
      - title: "Feature extraction, stitching and multi-robot control"
        text: >-
          I stitched panoramas from several photographs using SIFT feature
          extraction and homography estimation, and built a vision system
          in MATLAB and C++ that located and identified parts in the
          workspace of a Fanuc 6-axis robot. I also wrote distributed
          consensus algorithms in Python and ran formation tracking on the
          real multi-robot fleet at the Georgia Tech Robotarium.
    stack: ["C++", "SIFT", "homography", "digital control", "detection and estimation", "image processing"]

  - period: "2012 — 2017"
    role: "Engineering degree (Diplôme d’ingénieur d’État), Electrical Engineering — Control Systems"
    kind: "education"
    org: "École Nationale Polytechnique, Algiers"
    url: "https://www.enp.edu.dz/en/"
    note: "GPA 17.5/20 · ranked 5th of 1,400 in the national entrance exam after the preparatory classes (top 1%)."
    work:
      - title: "Two years of preparatory classes first"
        text: >-
          Two years of intensive mathematics, physics and programming,
          nine to six, six days a week. The national ranking at the end
          decides which engineering school you enter.
      - title: "Control systems on real hardware"
        text: >-
          I built control systems for real hardware and factory
          constraints: an adaptive cruise controller for an autonomous
          vehicle, and a PLC program driving an industrial assembly
          machine.
    stack: ["C", "MATLAB", "VHDL", "control design", "process identification", "optimal control"]

skills:
  - group: "Languages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library (formerly Matrox Imaging Library)", "OpenCV", "pattern matching", "calibration", "metrology", "edge measurement", "SIFT", "homography", "2D and 3D transforms"]
  - group: "Machine learning"
    items: ["decision trees", "random forests", "SVMs", "k-means", "scikit-learn", "deep learning", "object detection", "OCR", "model evaluation on CPU and GPU", "hyperparameter tuning"]
  - group: "Maths"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "non-linear least squares", "linear algebra", "numerical stability", "control theory"]
  - group: "C++ & systems"
    items: ["modern C++ (templates, STL)", "multithreading and concurrency", "virtual memory and working set", "CMake", "GTest", "ASan / MSan", "Valgrind", "gdb", "Windows and Linux", "Docker"]
  - group: "Generative AI"
    items: ["agentic workflows", "RAG", "agent evaluation"]
  - group: "Tools"
    items: ["Git / GitHub", "SVN", "CI/CD", "code review", "clang-tidy / clang-format", "SonarQube", "Visual Studio", "JIRA", "Confluence", "Google Cloud", "Firebase", "FastAPI"]
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
