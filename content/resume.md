---
title: "Resume"
layout: "resume"
lastmod: 2026-10-21
description: "Senior Software Developer, seven years on 2D and 3D machine vision algorithms in modern C++: real-time image processing, numerical optimisation and memory."
role: "Senior Software Developer in Montréal, building machine vision and image processing algorithms in modern C++"
location: "Montréal, Québec"
sameAs:
  - "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - "https://github.com/brmel"
  - "https://x.com/BrmelB"

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
          I develop and maintain the 2D and 3D algorithms in the Aurora
          Imaging Library, Zebra’s machine vision SDK. I add features, fix
          bugs, and support customers directly when their applications
          fail in production. I write the API documentation and the code
          examples that ship with each release, agree API behaviour and
          backward compatibility with the UI, documentation and QA teams
          before it goes out, and help plan the release roadmap.
      - title: "Image processing on smart cameras"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "A Zebra smart camera inspecting parts on a bench"
        text: >-
          I bring the library’s image processing to Zebra’s smart cameras,
          writing algorithms that fit the camera’s limited memory and
          processing power. I work across the whole product, from the user
          interface to the backend: I fix multithreading and concurrency
          bugs, reproduce and validate fixes with the QA team, and build
          features that make the camera easier to configure.
      - title: "Deep learning for OCR and barcode reading"
        text: >-
          I work on the library’s deep learning models for reading text
          and codes that the classical decoders can’t: damaged, blurred,
          low-contrast, or printed on curved and reflective surfaces. I
          train and evaluate the models, integrate them into the C++
          processing pipeline, and keep them within the same speed and
          memory limits the classical path already meets.
    stack: ["C++", "machine vision algorithms", "deep learning", "OCR", "machine learning", "embedded / edge imaging"]

  - period: "2022 — 2024"
    role: "Software Developer II"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Geometry and solvers behind the 2D modules"
        text: >-
          I maintained and extended the library’s 2D tools for locating,
          measuring and inspecting parts (Model Finder, Edge Finder,
          Measurement, Metrology, Calibration and Bead), including the
          geometry, linear algebra and non-linear optimisation they run
          on. I fixed numerical and API bugs and extended their regression
          tests.
      - title: "Machine learning inside a geometric library"
        video: "CS4cs9xVecg"
        videoAlt: "Notes from the deep learning specialisation"
        text: >-
          I integrated classical machine learning (Random Forests and SVMs)
          into modules that had been purely geometric, to classify patterns in
          complex scenes. I wrote the new APIs, their reference documentation
          and the customer examples that shipped with them, and mentored
          interns and junior developers on modern C++, multithreading and code
          review.
    stack: ["C++", "geometric matching", "metrology", "non-linear optimisation", "classical ML"]

  - period: "2019 — 2022"
    role: "Software Developer"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
    note: "Matrox Imaging became part of Zebra Technologies in 2022."
    work:
      - title: "Calibration, measurement and metrology"
        video: "LcoPNbyuhZU"
        videoAlt: "Industrial image processing in the Matrox Imaging Library"
        text: >-
          My first role after the master’s was on the library’s
          measurement modules: Calibration, Measurement and Metrology. I
          implemented and debugged their algorithms, wrote their tests and
          customer examples, designed the Advanced Geometric Matcher and
          co-designed its public C++ API. It ships today in Zebra’s Aurora
          Imaging Library.
      - title: "Non-linear solvers in a legacy C++ codebase"
        video: "sfLZ7v9gEnc"
        videoAlt: "Working through the Matrox Imaging Library codebase"
        text: >-
          I modernised the geometric solvers in the library’s decades-old
          C++ codebase, replacing older methods with non-linear
          optimisation (including Levenberg–Marquardt) for sub-pixel
          accuracy and numerical stability. I tracked down memory leaks
          and dangling references, and built regression suites that
          protect the behaviour thousands of installed applications depend
          on.
      - title: "Machine learning in the imaging library"
        text: >-
          I joined as an intern in early 2019 and built Random Forest
          classifiers into the Matrox Imaging Library (today Zebra’s
          Aurora Imaging Library), so that production lines could sort
          defects in real time. I also built synthetic dataset generators
          and automated benchmarks that measured the classifiers’
          precision and speed on every change.
    stack: ["C++", "non-linear optimisation", "Levenberg–Marquardt", "numerical stability", "classical ML"]

  - period: "2017 — 2019"
    role: "M.Eng., Electrical Engineering — Control Systems"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Professional master’s with an industrial internship · GPA 3.87/4 · Al Ghurair Foundation Scholarship — 1 of 100 selected from more than 15,000 applicants."
    work:
      - title: "How I got to Canada"
        video: "BPkj-VETeX0"
        videoAlt: "On the Al Ghurair Foundation scholarship"
        url: "https://www.alghurairfoundation.org/"
        text: >-
          The scholarship was awarded on academic merit and paid for the
          master’s. It’s how I came to Montréal.
      - title: "Projects on real hardware"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotics and real-time control work during the master’s"
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
    stack: ["C++", "SIFT", "homography", "digital control", "detection and estimation", "stochastic and robust control", "image processing"]

  - period: "2012 — 2017"
    role: "B.Eng., Electrical Engineering — Control Systems"
    kind: "education"
    org: "École Nationale Polytechnique, Algiers"
    url: "https://www.enp.edu.dz/en/"
    note: "GPA 17.5/20 · graduated 5th of 1,400 — top 1% nationally."
    work:
      - title: "Two years of preparatory classes first"
        video: "VjwIGG7Lbt0"
        videoAlt: "The preparatory-class years in Algiers"
        text: >-
          Two years of intensive mathematics, physics and programming,
          nine to six, six days a week. The national ranking at the end
          decides which engineering school you enter.
      - title: "Control systems on real hardware"
        video: "eGPbNTXTd1I"
        videoAlt: "Control systems and PLC projects during the engineering degree"
        text: >-
          I built control systems for real hardware and factory
          constraints: an adaptive cruise controller for an autonomous
          vehicle, and a PLC program driving an industrial assembly
          machine.
    stack: ["C", "MATLAB", "VHDL", "control design", "process identification", "optimal control"]

skills:
  - group: "Languages"
    items: ["C++17 / C++20", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "VHDL", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library (formerly Matrox Imaging Library)", "OpenCV", "geometric matching", "pattern matching", "calibration", "metrology", "edge measurement", "SIFT", "homography", "2D and 3D transforms"]
  - group: "Maths & algorithms"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "non-linear least squares", "linear algebra", "numerical stability", "control theory", "classical ML", "deep learning"]
  - group: "C++ & systems"
    items: ["modern C++ (templates, STL)", "multithreading and concurrency", "real-time image processing", "virtual memory and working set", "CMake", "GTest", "Clang / LLVM", "ASan / MSan", "Valgrind", "gdb", "cross-platform Windows and Linux", "QNX", "ROS", "Docker"]
  - group: "Cloud & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Tools & practice"
    items: ["Visual Studio", "Git / GitHub", "SVN", "CI/CD", "code review", "clang-tidy / clang-format", "SonarQube", "JIRA", "Confluence", "Agile / Scrum", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)"]
  - group: "Spoken"
    items: ["French", "English", "Arabic"]
certifications:
  - year: "2023"
    name: "Neural Networks and Deep Learning · Convolutional Neural Networks"
    issuer: "DeepLearning.AI"
  - year: "2023"
    name: "Machine Learning: Classification"
    issuer: "University of Washington"
---

- **Machine vision** — 2D and 3D algorithms that find, measure and inspect parts in factory images: pattern matching, edge detection, calibration and metrology
- **Machine learning, prototype to production** — taking a model from a first prototype to a tested, documented feature of a C++ library that ships to customers
- **Deep learning evaluation** — testing deep learning models for object detection and text detection, including damaged, blurred and low-contrast codes
- **Constrained hardware** — optimising vision algorithms to fit the memory and processing limits of smart cameras
- **Numerical algorithms** — non-linear optimisation for sub-pixel accuracy, with regression tests that guard every numerical result
- **Modern C++** — safe multithreaded code, memory measured with [MemoryTracer](/projects/memorytracer/) and explained in [two articles](/tech/windows-memory-management-overview/), code review, automated tests and sanitizers
