---
title: "Resume"
layout: "resume"
lastmod: 2026-10-25
description: "Senior Software Developer with seven years of production C++: 2D and 3D machine vision, machine learning and deep learning, and today generative AI."
role: "Senior Software Developer in Montréal: production C++ for machine vision and machine learning, and today generative AI"
location: "Montréal, Québec"
sameAs:
  - "https://www.linkedin.com/in/brahim-redouane-mellah/"
  - "https://github.com/brmel"
  - "https://x.com/BrmelB"

experience:
  - period: "Aug 2026 — Present"
    role: "Senior Software Developer, Generative AI"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Agentic workflows and RAG"
        text: >-
          I implement agentic workflows end to end with Google ADK and
          LlamaIndex: the agent loop, the tools each agent can call, its
          memory, and the context it receives, sized for small models. I
          build retrieval-augmented generation (RAG) with grounded answers,
          and run small models locally.
      - title: "Agent evaluation"
        text: >-
          I build the evaluation sets and metrics that decide whether an
          agent is good enough to ship, the same discipline I used for deep
          learning models.
    stack: ["Google ADK", "LlamaIndex", "agentic workflows", "RAG", "agent evaluation", "small local models"]

  - period: "Jul 2024 — Aug 2026"
    role: "Senior Software Developer, Aurora Imaging Library"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "Core 2D and 3D vision algorithms"
        url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
        video: "m7KKRmOxRT0"
        videoAlt: "Walkthrough of the Aurora Imaging Library in Aurora Vision Studio"
        text: >-
          I owned vision algorithms in the Aurora Imaging Library, Zebra’s
          machine vision SDK (Edge Finder, Geometric Matcher and
          Calibration), from feature to release. I designed their APIs, fixed
          bugs, and supported customers directly when their applications
          failed in production. I wrote the API documentation and the code
          examples that ship with each release, agreed API behaviour and
          backward compatibility with the UI, documentation and QA teams
          before it went out, and helped plan the release roadmap.
      - title: "Image processing on smart cameras"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "A Zebra smart camera inspecting parts on a bench"
        text: >-
          I brought the library’s image processing to Zebra’s Aurora Focus
          smart cameras, writing algorithms that fit the camera’s limited
          memory and processing power. I worked across the whole product,
          from the user interface to the backend: I fixed multithreading and
          concurrency bugs, reproduced and validated fixes with the QA team,
          and built features that make the camera easier to configure.
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
    stack: ["C++", "machine vision algorithms", "deep learning", "OCR", "machine learning", "embedded / edge imaging"]

  - period: "Jun 2022 — Jun 2024"
    role: "Software Developer II, Image Processing"
    org: "Zebra Technologies"
    url: "https://www.zebra.com/us/en.html"
    work:
      - title: "The Advanced Geometric Matcher, from research to production"
        text: >-
          I took the Advanced Geometric Matcher (AGM), a new pattern-matching
          tool, from research and prototype to production. I designed its
          public C++ API with the team, and it ships today in Zebra’s Aurora
          Imaging Library.
      - title: "Machine learning inside a geometric library"
        video: "CS4cs9xVecg"
        videoAlt: "Notes from the deep learning specialisation"
        text: >-
          I integrated classical machine learning (Random Forests and SVMs)
          into modules that had been purely geometric, to classify patterns in
          cluttered scenes. I wrote the new APIs, their reference documentation
          and the customer examples that shipped with them, and mentored
          interns and junior developers on modern C++, multithreading and code
          review.
      - title: "Numerical bugs and regression tests"
        text: >-
          I fixed numerical bugs and API regressions, and added unit,
          integration and randomised tests to the regression suites.
    stack: ["C++", "geometric matching", "public API design", "classical ML", "regression testing"]

  - period: "Jun 2019 — Jun 2022"
    role: "Software Developer, Image Processing"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
    note: "Matrox Imaging, in Dorval, became part of Zebra Technologies in 2022."
    work:
      - title: "Calibration, measurement and metrology"
        video: "LcoPNbyuhZU"
        videoAlt: "Industrial image processing in the Matrox Imaging Library"
        text: >-
          My first role after the master’s was on the library’s
          measurement modules: Calibration, Measurement and Metrology. I
          implemented and debugged their algorithms, wrote their tests,
          documentation and customer examples, and supported the customers
          who used them. I also maintained Model Finder, Edge Finder and
          Bead.
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
    stack: ["C++", "calibration", "metrology", "non-linear optimisation", "Levenberg–Marquardt", "numerical stability"]

  - period: "Jan 2019 — May 2019"
    role: "Software Development Intern"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
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
    note: "Professional master’s with an industrial internship · GPA 3.87/4 · Al Ghurair Foundation Scholarship — 1 of about 100 recipients from more than 15,000 applicants."
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
    role: "Engineering degree (Diplôme d’ingénieur d’État), Electrical Engineering — Control Systems"
    kind: "education"
    org: "École Nationale Polytechnique, Algiers"
    url: "https://www.enp.edu.dz/en/"
    note: "GPA 17.5/20 · ranked 5th of 1,400 in the national entrance exam after the preparatory classes (top 1%)."
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
  - group: "Generative AI"
    items: ["agentic workflows", "RAG", "agent evaluation", "small local models", "Google ADK", "LlamaIndex", "Gemini", "MCP"]
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
- **Deep learning evaluation** — benchmarking deep learning models for object detection, OCR and text detection on CPU and GPU, and designing the metrics that decide whether a model ships
- **Constrained hardware** — optimising vision algorithms to fit the memory and processing limits of smart cameras
- **Numerical algorithms** — non-linear optimisation for sub-pixel accuracy, with regression tests that guard every numerical result
- **Modern C++** — safe multithreaded code, memory measured with [MemoryTracer](/projects/memorytracer/) and explained in [two articles](/tech/windows-memory-management-overview/), code review, automated tests and sanitizers
- **Generative AI** — my current work: agentic workflows with Google ADK and LlamaIndex, RAG, and the evaluations that decide when an agent is ready to ship
