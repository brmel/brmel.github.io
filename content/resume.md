---
title: "Resume"
layout: "resume"
lastmod: 2026-10-20
description: "Senior Software Developer, seven years on 2D and 3D machine vision algorithms in modern C++: real-time image processing, numerical optimisation and memory."
aliases: ["/timeline/", "/about/"]
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
    learned: |-
      - Deep learning earns its place where the classical decoders stop (damaged, blurred and low-contrast codes) and loses to them everywhere else on latency and predictability. Choosing which half of the problem goes to a model is most of the design work.
      - A model that wins on a benchmark can still lose in the field, because a customer’s failures are the images nobody thought to put in the test set. How it fails tells you more than how often it fails.
      - Running inference inside a real-time pipeline is a memory and throughput problem before it’s a machine learning one. Preprocessing, allocation and cache locality decide whether a model fits the frame budget at all.
      - On the smart camera, the constraints drive the whole design. Working set, allocation on the hot path and CPU headroom rule out approaches on the desktop build long before accuracy does.
      - Most of this job sits around the algorithm: the reference documentation, the shipped examples, the API contract agreed with the UI and QA teams, and the customer applications that surface the bugs a test suite doesn’t.

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
    learned: |-
      - Writing the documentation and the examples is how an API design gets tested. Almost every question that came back from customers was about the interface rather than the algorithm.
      - Once a C++ API is public, you can’t take it back. Naming, parameter order, default behaviour and how errors are reported outlive every implementation detail behind them.
      - Classical machine learning inside a geometric library has to stay diagnosable. A Random Forest that classifies a pattern must fail in a way a support engineer can explain to a customer, which ruled out models I couldn’t inspect.
      - Stateful API bugs and floating-point differences are the two failures that regression tests catch and code review doesn’t. Both look like nothing in a diff.
      - Mentoring interns made me say why and not just what, and that’s where I found the habits I couldn’t defend.

  - period: "2019 — 2022"
    role: "Software Developer"
    org: "Matrox Imaging"
    url: "https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html"
    note: "Matrox Imaging became part of Zebra Technologies in 2022; the work continued without a break."
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
    learned: |-
      - Writing a better algorithm is the easy half. Shipping it into a library thousands of applications already depend on, without changing an answer they rely on, is the hard half.
      - Non-linear optimisation is only as good as its initial guess and its stopping rule. Levenberg–Marquardt converges cleanly in a paper and oscillates on real data until both of those are right.
      - Sub-pixel accuracy is a numerical-stability problem. The order of operations, the conditioning of the matrix and the tolerance you compare against decide the last two decimals.
      - In a multi-decade C++ codebase the memory bugs that cost time are dangling references and ownership nobody wrote down. Leaks at least announce themselves.
      - I build the regression suite before touching the algorithm. It’s the only thing that makes changing legacy numerical code possible at all.

  - period: "2017 — 2019"
    role: "M.Eng., Electrical Engineering — Control Systems"
    kind: "education"
    org: "Polytechnique Montréal"
    url: "https://www.polymtl.ca/"
    note: "Professional master’s with an industrial internship · GPA 3.87/4 · Al Ghurair Foundation Scholarship — 1 of 100 selected from more than 15,000 applicants."
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
    learned: |-
      - A control law can be correct on paper and still be wrong if it arrives ten milliseconds late.
      - Geometry is the cheap part of feature matching. SIFT produces candidates; everything that makes a panorama or a part-locator work is the outlier rejection afterwards.
      - State estimation is where I learned to weigh a model against a measurement in proportion to how much each one lies.
      - Running consensus algorithms on the real Robotarium fleet instead of in simulation showed how much of a distributed algorithm is about what happens when one robot stops answering.

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
    learned: |-
      - The first assembly machine I programmed failed on sensors and wiring, not on the control logic I had spent the whole term on.
      - A PLC program is written for whoever debugs it at three in the morning on a factory floor.
      - Identifying a process from real measurements is harder than designing the controller that follows it. The error lives in the model.

skills:
  - group: "Languages"
    items: ["C++ (17/20)", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "VHDL", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library (formerly Matrox Imaging Library)", "OpenCV", "geometric matching", "pattern matching", "calibration", "metrology", "edge measurement", "SIFT", "homography", "2D and 3D transforms"]
  - group: "Maths & algorithms"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "non-linear least squares", "linear algebra", "numerical stability", "control theory", "classical ML", "deep learning"]
  - group: "C++ & systems"
    items: ["modern C++ (templates, STL)", "multithreading and concurrency", "real-time image processing", "virtual memory and working set", "CMake", "GTest", "Clang / LLVM", "ASan / MSan", "Valgrind", "gdb", "cross-platform Windows and Linux", "QNX", "ROS", "Docker"]
  - group: "Cloud & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Tools & practice"
    items: ["Visual Studio", "Git / GitHub", "SVN", "CI/CD", "code review", "clang-tidy / clang-format", "SonarQube", "JIRA", "Confluence", "Agile / Scrum", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)"]
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

- **Numerical algorithms** — non-linear optimisation for sub-pixel accuracy, with regression tests that guard every numerical result
- **Memory and performance** — how Windows manages a program's memory. I wrote [MemoryTracer](/projects/memorytracer/) to measure it and [two articles](/tech/windows-memory-management-overview/) explaining it
- **Concurrency** — keeping multithreaded code safe in a library thousands of installed applications depend on
- **Machine vision** — finding, measuring and reading objects in images: pattern matching, edge detection, metrology, and deep learning for damaged or badly lit barcodes
- **Engineering practice** — code review, automated tests and memory checks with CMake, GTest, sanitizers and Valgrind
