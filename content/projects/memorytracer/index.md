---
title: "MemoryTracer"
featured: 4
date: 2024-01-09
projectNo: 12
domain: "infra"
status: "shipped"
pitch: "A C++ library that watches where a Windows process's virtual memory goes, minute by minute, and writes it to CSV."
description: "A C++ library that watches where a Windows process's virtual memory goes, minute by minute, and writes it to CSV."
metrics:
  - value: "3 CSVs"
    label: "per run: memory by type, by state, and private bytes"
  - value: "VMMap"
    label: "checked against Sysinternals, column for column"
  - value: "2 articles"
    label: "on Windows memory, written from what it measured"
stack: ["C++", "Windows API", "VirtualQuery", "Tool Help API", "Visual Studio"]
links:
  live: "/tech/windows-memory-management-deep-dive/"
  repo: "https://github.com/brmel/MemoryTracer"
lede: |
  A small static library that snapshots a live Windows process (committed,
  reserved, private, working set, broken down by heap, stack, image and mapped
  file) on a schedule you control, and exports the result as CSV.
lessons:
  - "**The tracer needed checking too.** I checked every counter against Sysinternals VMMap, column for column, before trusting any of it, and found two I had wrong."
  - "**The tracer was moving the number it measured.** Taking a snapshot allocated memory, which then showed up in the snapshot. So reducing allocation on the snapshot path was a correctness fix."
  - "**64-bit broke the assumptions.** The approach I started from computed the process memory maximum in a way that was wrong for 64-bit processes, and reported unused regions incorrectly. Both only show up when you plot the total and it doesn't add up."
  - "**Writing it up taught me more than building it.** Turning the measurements into [two articles](/tech/windows-memory-management-overview/) forced me to explain copy-on-write, private bytes and working set precisely enough for someone else to follow."
tags: ["C++", "Windows", "Systems"]
resources:
  - src: "gallery/01-tracer-vs-vmmap.jpg"
    params:
      caption: "MemoryTracer's own output beside a VMMap snapshot. The figures match column for column."
  - src: "gallery/02-virtual-by-type.jpg"
    params:
      caption: "Plotted from the exported CSV: virtual memory split by type across a process's life. A leak is the band that never comes back down."
  - src: "gallery/03-private-bytes.jpg"
    params:
      caption: "Private bytes over time: the counter that answers whether a process is leaking."
---

## The story

A process was running out of virtual memory in production, and Task Manager had
one number for it. One number can't tell you whether the heap is fragmenting,
whether a mapped file is never being released, or whether a DLL's private pages
are growing on every load. VMMap from Sysinternals can show you all of that, but
only as a snapshot you take by hand, in a window, on the machine.

I wanted the same detail over time, from inside my own process, on a schedule.

## The product

You link the library, hand it a process id, and call it when it matters:

```cpp
CSnapshotMngr tracer(processId);
tracer.PrintNow();          // one snapshot to the console
tracer.Export(120, 2);      // every 2s for 120s, to CSV
```

It writes three files (memory by type, memory by state, and private bytes) and
you plot them. It reads the Windows memory APIs directly (`VirtualQuery`, the
Tool Help API, section objects) rather than shelling out to a tool, so it can run
inside the process being measured and snapshot exactly when you want it to.

It grew out of [a VMMap reimplementation](https://james-ross.co.uk/projects/vmmap)
that I fixed and extended: a private-bytes counter it didn't have, a corrected
maximum for 64-bit processes, a corrected unused-region count, fewer allocations
while snapshotting, CSV export, and control over when snapshots start.
