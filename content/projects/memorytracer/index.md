---
title: "MemoryTracer"
featured: 6
date: 2024-01-09
projectNo: 12
status: "shipped"
pitch: "A C++ library that records where a Windows process’s memory goes over time (stack, DLLs, mapped files, private data) and writes it to CSV."
description: "A C++ library that records where a Windows process’s memory goes over time (stack, DLLs, mapped files, private data) and writes it to CSV."
stack: ["C++", "Windows API", "VirtualQuery", "Tool Help API", "Visual Studio"]
links:
  live: "/tech/windows-memory-management-deep-dive/"
  repo: "https://github.com/brmel/MemoryTracer"
lede: |
  Each snapshot also splits that memory by state: committed, reserved, private
  and working set.
resources:
  - src: "gallery/01-tracer-vs-vmmap.jpg"
    params:
      caption: "MemoryTracer’s output beside a VMMap snapshot."
  - src: "gallery/02-virtual-by-type.jpg"
    params:
      caption: "Plotted from the exported CSV: virtual memory split by type across a process’s life. A leak is the band that never comes back down."
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

I wanted the same detail over time, from inside my own process.

## The product

You link the library, hand it a process id, and call it when it matters:

```cpp
CSnapshotMngr tracer(processId);
tracer.PrintNow();          // one snapshot to the console
tracer.Export(120, 2);      // every 2s for 120s, to CSV
```

You plot the files it writes. It reads the Windows memory APIs directly (`VirtualQuery`, the
Tool Help API, section objects) rather than calling an external tool, so it can run
inside the process being measured.

It grew out of [a VMMap reimplementation](https://james-ross.co.uk/projects/vmmap)
that I fixed and extended: a private-bytes counter it didn't have, CSV export,
and control over when snapshots start.
