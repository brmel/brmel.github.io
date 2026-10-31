---
title: "Windows Memory Management: Virtual vs Physical"
date: 2023-11-29
description: "How the Windows Memory Manager separates virtual from physical memory, and a C++ tool that records where a process’s virtual memory goes over time."
lastmod: 2026-10-20
series: "Windows Memory Management"
seriesPart: 1
cover:
    image: "02-virtual-vs-physical-memory.jpg"
    alt: "Diagram of virtual memory mapped onto physical memory and the page file"
---

Even the people who build Windows don't agree on how much memory a process is
using. Task Manager has labelled the same
quantities differently across versions, and the
[Sysinternals](https://learn.microsoft.com/en-us/sysinternals) team criticised
one of those choices publicly.

I came to this from C++ and an electrical engineering background. After Mark
Russinovich's talks on [Virtual
Memory](https://youtu.be/AjTl53I_qzY?si=TONF91WbNu6d5Ra4) and [Physical Memory
management in Windows](https://youtu.be/6KZdNsq1YV4?si=xpSamR2OSN-xyjr1) I
wanted two things: to be able to state the difference precisely, and to watch a
process's usage over time instead of sampling it in a tool.

{{< figure src="01-task-manager-memory-columns.jpg" alt="Table comparing the memory columns shown by Windows Task Manager across Windows versions" caption="How Task Manager labelled memory across Windows versions." >}}

## Committed and reserved

Suppose you need to allocate a portion of memory on Windows. If you are using
C++, you can achieve this using the `new` keyword, for instance. Windows, if
possible, will then provide you with a pointer to the allocated memory.

The Memory Manager is responsible for handling this task, allowing you to
specify certain characteristics of the allocated memory. For example, you can
determine whether it should be **committed** immediately or **reserved** for
future use.

**Committed** implies that the memory is ready for immediate use and is backed
by **physical** memory. On the other hand, **reserved** indicates
that the memory is spoken for but not yet backed by anything physical; this
memory is purely **virtual**.

## Virtual and physical memory

- **Physical memory**, often referred to as RAM, is the
  hardware component in a computer that stores data that is actively
  being used or processed by the CPU.
- **Virtual memory** refers to the address space that applications can use. In a
  64-bit system, the virtual memory address space can theoretically address up to
  2^64 bytes (about 18.4 million TB). In practice, a 64-bit process on x64
  Windows gets 128 TB of user-mode address space (8 TB before Windows 8.1).

This separation gives more flexibility to Windows and the Memory Manager. When
Windows runs out of RAM, it uses your storage drive as extra space, allowing it
to handle multiple tasks and big programs.

{{< figure src="02-virtual-vs-physical-memory.jpg" alt="Diagram of virtual memory mapped onto physical memory and the page file" caption="Virtual address space, mapped by the Memory Manager onto physical RAM and the page file." >}}

Processes don't have direct control over physical memory. The Memory Manager
handles the mapping of virtual memory to physical memory and makes decisions
about where to place data in physical RAM based on system demands and memory
management policies.

## Private and shared

The memory you allocate can also have many *types*, but most importantly, it can
be **private** or **shared**. **Private** memory is accessed only by the owner
process, while **shared** memory is like a common area where different processes
can share and exchange information.

Sysinternals provides tools for monitoring memory:
[VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap) for
virtual memory and
[RAMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/rammap) for
physical memory. Both are explained in the videos mentioned at the beginning of
this article.

{{< figure src="03-vmmap-sysinternals.jpg" alt="VMMap showing the virtual memory breakdown of a running process" caption="VMMap by Sysinternals." >}}

## Debug virtual and physical memory usage

VMMap and RAMMap capture the state of virtual and physical memory at one
moment. They aren't built for
watching that state change: you can't set the sampling interval, and getting
the numbers out in a form you can plot is awkward. A leak that only shows up
over an hour is invisible to a snapshot.

### MemoryTracer

MemoryTracer is an open-source C++ project that records where a process's
virtual memory goes over time. It shows the data on the screen or exports it to
a file, at the snapshot frequency you choose.

Call it from your own code as a callback, to control when a snapshot is
taken. Or run it from a separate process, if you'd rather not touch the code
you're measuring.

This is an example of tracking virtual memory usage of the process with id
`32404`:

```cpp
// Process id you want to track
int Pid = 32404;

// Create MemoryTracer instance
CSnapshotMngr MyMemTracer(Pid);

// Specify the total duration and frequency, in seconds
int Duration = 120;
int PeriodT = 2;

// Export usage for 2 min by taking a snapshot each 2 seconds
MyMemTracer.Export(Duration, PeriodT);
```

{{< figure src="04-memorytracer-virtual-by-type.jpg" alt="Exported table of virtual memory usage grouped by memory type" caption="Virtual memory usage exported using MemoryTracer, regrouped by type." >}}

{{< figure src="05-memorytracer-virtual-timeline.jpg" alt="Exported chart of virtual memory usage over time, grouped by memory type" caption="The same export over time." >}}

{{< figure src="06-memorytracer-private-bytes.jpg" alt="Exported chart of the process's private bytes grouped by memory type" caption="Private bytes of the process, regrouped by memory type." >}}

## Sources

- Mark Russinovich — [Virtual Memory](https://youtu.be/AjTl53I_qzY?si=TONF91WbNu6d5Ra4) (video)
- Mark Russinovich — [Physical Memory management in Windows](https://youtu.be/6KZdNsq1YV4?si=xpSamR2OSN-xyjr1) (video)
- Microsoft — [Sysinternals](https://learn.microsoft.com/en-us/sysinternals)
- Microsoft — [VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap), the virtual memory map
- Microsoft — [RAMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/rammap), the physical memory map
