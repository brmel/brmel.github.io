---
title: "Ibraverse"
date: 2025-01-08
description: "Senior C++ engineer at Zebra Technologies: 2D and 3D vision algorithms, numerical solvers and low-level systems. Projects, write-ups and field notes."
---
Senior C++ engineer at Zebra Technologies. I own 2D and 3D algorithms inside the
Aurora Imaging Library — geometric solvers, calibration and metrology running on
factory floors — and port them onto a smart camera under tight memory and CPU
budgets. Modern C++17/20, Windows and Linux, seven years on the same codebase:
Matrox Imaging first, then Zebra after the acquisition.

What that consists of:

- **Numerical algorithms** — non-linear optimisation and Levenberg–Marquardt, sub-pixel accuracy, and floating-point behaviour defended by regression suites
- **Low-level systems** — virtual memory, working set, heap and mapped files. I wrote [MemoryTracer](/projects/memorytracer/) to measure it and [two articles](/tech/windows-memory-management-overview/) explaining it
- **Multithreading and concurrency** — race conditions in a library thousands of installed applications depend on
- **Machine vision** — 2D pattern matching, edge detection, metrology, SIFT and homography, and deep learning for damaged or badly lit barcodes
- **Engineering practice** — CMake, GTest, sanitizers and Valgrind, code review, and regression suites that protect thousands of installed applications

I also write the API documentation and the code examples that ship with the
library, support customers debugging their own applications, and agree API
behaviour with the UI, documentation and QA teams before each release.

Outside work: [a robot cell in a physics engine](/projects/robonode/), [an agent
that tests web applications](/projects/domia/), and [write-ups](/tech/) of what
each one taught me.
