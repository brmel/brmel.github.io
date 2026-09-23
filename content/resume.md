---
title: "Resume"
layout: "resume"
summary: "Senior C++ engineer — Zebra Technologies, Matrox Imaging, Polytechnique Montréal."
description: "Senior C++ engineer, seven years on 2D and 3D vision algorithms: modern C++17/20, real-time image processing, non-linear optimisation and low-level memory."
aliases: ["/timeline/", "/about/"]
role: "Senior Software Developer — modern C++, real-time image processing, 2D/3D vision algorithms"
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
          I develop and maintain the 2D and 3D algorithms in the library: I
          add features, investigate and fix bugs, and support customers
          directly when their applications fail in production. I write the API
          documentation and the code examples that ship with each release, and
          I agree API behaviour and backward compatibility with the UI,
          documentation and QA teams before it goes out. I also help plan the
          release roadmap.
      - title: "Image processing on the smart camera"
        url: "https://www.zebra.com/us/en/products/industrial-machine-vision-fixed-scanners/smart-sensors-and-cameras.html"
        video: "N2DfQzTPwog"
        videoAlt: "The Aurora Focus smart camera inspecting parts on a bench"
        text: >-
          I port image processing modules onto the Aurora Focus smart camera,
          writing algorithms that fit tight memory and CPU budgets. The work
          spans the whole stack: I debug problems that cross the UI and the
          backend, fix multithreading and concurrency bugs, work with the QA
          team on reproducing and validating fixes, and build features that
          make the camera easier to configure.
      - title: "Deep learning for OCR and barcode reading"
        text: >-
          I work on the deep learning side of the library: models that read
          characters and codes the classical decoders cannot — damaged,
          blurred, low-contrast, or printed on curved and reflective surfaces.
          The work runs from training and evaluating the models to integrating
          inference into the C++ pipeline and keeping it inside the same
          latency and memory budget the classical path already meets.
    built: ["Aurora Imaging Library", "Aurora Focus smart camera", "Deep learning OCR", "Barcode reading with deep learning"]
    stack: ["C++", "machine vision algorithms", "deep learning", "OCR", "machine learning", "embedded / edge imaging"]
    tools: ["Visual Studio", "Git / GitHub", "CMake", "GTest", "clang-tidy / clang-format", "SonarQube", "Valgrind & sanitizers", "gdb", "JIRA", "Confluence", "Agile / Scrum", "CI/CD"]
    learned: |-
      - Deep learning earns its place exactly where the classical decoders stop — damaged, blurred and low-contrast codes — and loses to them everywhere else on latency and predictability. Choosing which half of the problem goes to a model is most of the design work.
      - A model that wins on a benchmark can still lose in the field, because a customer's failures are the images nobody thought to put in the test set. The useful metric is how it fails, not how often.
      - Running inference inside a real-time pipeline is a memory and throughput problem before it is a machine learning one. Preprocessing, allocation and cache locality decide whether a model fits the frame budget at all.
      - On the smart camera, the constraint is the whole design. Working set, allocation on the hot path and CPU headroom rule out approaches on the desktop build long before accuracy does.
      - Most of this job sits around the algorithm: the reference documentation, the shipped examples, the API contract agreed with the UI and QA teams, and the customer applications that surface the bugs a test suite does not.
      - Shipping on a team this size is as much process as code. A feature is specified in Confluence, tracked in JIRA, gated on clang-tidy, clang-format and SonarQube at review, and proven with GTest and sanitizers before it reaches a release branch. A change that passes review but not the tooling has not shipped.

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
          complex scenes. I wrote the new APIs, their reference documentation
          and the customer examples that shipped with them, and mentored
          interns and junior developers on modern C++, multithreading and code
          review.
    built: ["Advanced Geometric Matcher API", "MIL 2D modules", "customer-facing API examples"]
    stack: ["C++", "geometric matching", "metrology", "non-linear optimisation", "classical ML"]
    tools: ["Visual Studio", "Git / GitHub", "CMake", "GTest", "JIRA", "Confluence", "Agile / Scrum", "code review"]
    learned: |-
      - Writing the documentation and the examples is how an API design gets tested. Almost every question that came back from customers was about the interface, not the algorithm.
      - A public C++ API is a promise you cannot withdraw. Naming, parameter order, default behaviour and how errors are reported outlive every implementation detail behind them.
      - Classical machine learning inside a geometric library has to stay diagnosable. A Random Forest that classifies a pattern must fail in a way a support engineer can explain to a customer, which ruled out models I could not inspect.
      - Stateful API bugs and floating-point differences are the two failures that regression tests catch and code review does not. Both look like nothing in a diff.
      - Mentoring interns made me say why and not just what, and that is where I found the habits I could not actually defend.

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
          My first role after the master's, on the measurement modules:
          Calibration, Measurement and Metrology. I implemented and debugged
          their algorithms, wrote the tests and the customer examples, and
          designed the Advanced Geometric Matcher that later shipped as a
          public API.
      - title: "Non-linear solvers in a legacy C++ codebase"
        video: "sfLZ7v9gEnc"
        videoAlt: "Working through the Matrox Imaging Library codebase"
        text: >-
          I modernised the geometric solvers in a multi-decade C++ codebase,
          replacing older methods with non-linear optimisation including
          Levenberg–Marquardt for sub-pixel accuracy and numerical stability. I
          tracked down memory leaks and dangling references, and built
          regression suites that protect behaviour thousands of installed
          applications depend on.
      - title: "Machine learning in the imaging library"
        text: >-
          I joined as an intern in early 2019 and implemented Random Forest
          classifiers directly inside the Matrox Imaging Library, for
          real-time defect categorisation on production lines. I also built
          synthetic dataset generators and automated benchmarks that measured
          classifier precision and inference throughput on every change.
    built: ["Pattern matching", "Edge detection", "Non-linear optimisation", "Memory investigations", "Calibration", "Measurement and metrology", "Random Forest classifiers in C++"]
    stack: ["C++", "non-linear optimisation", "Levenberg–Marquardt", "numerical stability", "classical ML"]
    tools: ["Visual Studio", "Git", "SVN", "GTest", "VMMap", "Valgrind", "JIRA", "Confluence"]
    learned: |-
      - Writing a better algorithm is the easy half. Shipping it into a library thousands of applications already depend on, without changing an answer they rely on, is the hard half.
      - Non-linear optimisation is only as good as its initial guess and its stopping rule. Levenberg–Marquardt converges cleanly in a paper and oscillates on real data until both of those are right.
      - Sub-pixel accuracy is a numerical-stability problem. The order of operations, the conditioning of the matrix and the tolerance you compare against decide the last two decimals, not the maths on the whiteboard.
      - In a multi-decade C++ codebase the memory bugs that cost time are dangling references and ownership nobody wrote down. Leaks at least announce themselves.
      - Build the regression suite before touching the algorithm. It is the only thing that makes changing legacy numerical code possible at all.

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
          master's. It is how I came to Montréal.
      - title: "Control, robotics and real-time systems"
        video: "UZbmuAs2K2w"
        videoAlt: "Robotics and real-time control work during the master's"
        text: >-
          Every major course ended in a project running on real hardware:
          robot control and trajectory execution, real-time scheduling under
          QNX, image processing for part localisation, and state estimation.
          Coursework covered image processing, detection and estimation of
          signals, robotics, real-time operating systems, non-linear and
          stochastic control, and cyber-physical systems.
      - title: "Feature extraction, stitching and multi-robot control"
        text: >-
          I implemented SIFT feature extraction and homography estimation to
          stitch panoramas from multiple photographs, and built a vision
          system in MATLAB and C++ that located and identified workpieces in
          the workspace of a Fanuc 6-axis robot. I also wrote distributed
          consensus algorithms in Python and ran formation tracking on the
          real multi-robot fleet at the Georgia Tech Robotarium.
    built: ["Control theory", "Robotics", "Image processing", "SIFT and homography", "Multi-robot formation control"]
    stack: ["C++", "SIFT", "homography", "digital control", "detection and estimation", "stochastic and robust control", "image processing"]
    tools: ["QNX", "ROS", "MATLAB / Simulink", "Fanuc robots", "Georgia Tech Robotarium"]
    learned: |-
      - A control law can be correct on paper and still be wrong if it arrives ten milliseconds late. The deadline is part of the specification.
      - Geometry is the cheap part of feature matching. SIFT produces candidates; everything that makes a panorama or a part-locator actually work is the outlier rejection afterwards.
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
          Mathematics, physics and programming, nine to six, six days a week.
          The national ranking at the end decides which school you enter.
      - title: "Control systems on real hardware"
        video: "eGPbNTXTd1I"
        videoAlt: "Control systems and PLC projects during the engineering degree"
        text: >-
          I built control systems against real hardware and factory
          constraints: an adaptive cruise controller for an autonomous vehicle,
          and a PLC program driving an industrial assembly machine.
    built: ["Adaptive cruise control for an autonomous vehicle", "PLC program for an industrial assembly machine"]
    stack: ["C", "MATLAB", "VHDL", "control design", "process identification", "optimal control"]
    tools: ["Unity-Pro (Schneider)", "Simatic-Manager (Siemens)", "Simulink", "LabVIEW"]
    learned: |-
      - The first assembly machine I programmed failed on sensors and wiring, not on the control logic I had spent the whole term on.
      - A PLC program is written for whoever debugs it at three in the morning on a factory floor, not for whoever wrote it.
      - Identifying a process from real measurements is harder than designing the controller that follows it. The error lives in the model.

skills:
  - group: "Languages"
    items: ["C++ (17/20)", "C", "Python", "TypeScript", "Dart / Flutter", "MATLAB", "VHDL", "SQL"]
  - group: "Machine vision"
    items: ["Aurora Imaging Library", "Matrox Imaging Library", "OpenCV", "geometric matching", "pattern matching", "calibration", "metrology", "edge measurement", "SIFT", "homography", "2D and 3D transforms"]
  - group: "Maths & algorithms"
    items: ["non-linear optimisation", "Levenberg–Marquardt", "non-linear least squares", "linear algebra", "numerical stability", "control theory", "classical ML", "deep learning"]
  - group: "C++ & systems"
    items: ["modern C++ (templates, STL)", "multithreading and concurrency", "real-time image processing", "virtual memory and working set", "CMake", "GTest", "Clang / LLVM", "ASan / MSan", "Valgrind", "gdb", "cross-platform Windows and Linux", "QNX", "ROS", "Docker"]
  - group: "Cloud & backend"
    items: ["Google Cloud", "Firebase", "Cloud Functions", "Firestore", "Cloud Storage", "FastAPI", "Prefect"]
  - group: "Tools & practice"
    items: ["Visual Studio", "Git / GitHub", "SVN", "CMake", "CI/CD", "code review", "clang-tidy / clang-format", "SonarQube", "JIRA", "Confluence", "Agile / Scrum", "Docker", "Simulink", "LabVIEW", "Unity-Pro (Schneider)", "Simatic-Manager (Siemens)"]
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
