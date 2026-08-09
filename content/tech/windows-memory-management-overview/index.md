---
title: "A Very Shallow Overview of Windows Memory Management"
date: 2023-11-29
summary: "Virtual versus physical memory on Windows, committed versus reserved, private versus shared — and MemoryTracker, a C++ tool for watching a process's virtual memory over time."
description: "An introduction to how the Windows Memory Manager separates virtual from physical memory, and a C++ tool for tracking a process's usage over time."
tags: ["C++", "Windows", "Memory Management", "Sysinternals", "Systems"]
categories: ["Systems"]
series: "Windows Memory Management"
seriesPart: 1
cover:
    image: "02-virtual-vs-physical-memory.jpg"
    alt: "Diagram of virtual memory mapped onto physical memory and the page file"
    relative: true
canonicalOriginal: "https://www.linkedin.com/pulse/very-shallow-overview-windows-memory-management-mellah-thzse"
canonicalOriginalName: "LinkedIn"
---

If you are like me, a C++ developer with an electrical engineering background,
you are probably interested in understanding how software interacts with
hardware.

A few weeks ago, I watched a video by Mark Russinovich explaining [Virtual
Memory](https://youtu.be/AjTl53I_qzY?si=TONF91WbNu6d5Ra4) and [Physical Memory
management in Windows](https://youtu.be/6KZdNsq1YV4?si=xpSamR2OSN-xyjr1). I
found it so interesting that I decided to write this article and create a tool
that can help you debug your process memory usage — details will follow later.

But before we delve in, I want you to know this: this subject is so complex that
even Microsoft engineers found themselves in disagreement at some point. In this
image, we see the challenges faced by *Windows Task Manager* engineers to show
memory's usage across different Windows versions. It was so confusing, they even
got criticized from the [Sysinternals](https://learn.microsoft.com/en-us/sysinternals)
team… publicly!

{{< figure src="01-task-manager-memory-columns.jpg" alt="Table comparing the memory columns shown by Windows Task Manager across Windows versions" caption="How Task Manager labelled memory across Windows versions." >}}

## Committed and reserved

Suppose you need to allocate a portion of memory on Windows. If you are using
C++, you can achieve this using the `new` keyword, for instance. Windows, if
possible, will then provide you with a pointer to the allocated memory that you
can utilize in your program.

The Memory Manager is responsible for handling this task, allowing you to
specify certain characteristics of the allocated memory. For example, you can
determine whether it should be **committed** immediately or **reserved** for
future use.

**Committed** implies that the memory is ready for immediate use and is backed
by **physical** memory (real hardware). On the other hand, **reserved** indicates
that the memory will be utilized later, without involving physical memory at the
moment; this memory is purely **virtual**.

## Virtual and physical memory

**Virtual** and **physical** memory are important keywords. Let's try to define
them:

- **Physical memory**, often referred to as RAM (Random Access Memory), is the
  actual hardware component in a computer that stores data that is actively
  being used or processed by the CPU.
- **Virtual memory** refers to the address space that applications can use. In a
  64-bit system, the virtual memory address space can theoretically address up to
  2^64 (~17.4 million TB of memory). However, Windows 64-bit currently supports
  only ~16 TB.

This separation gives more flexibility to Windows and the Memory Manager. When
Windows runs out of RAM, it uses your storage drive as extra space, allowing it
to smoothly handle multiple tasks and big programs without getting overwhelmed.

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

Windows offers highly useful tools for monitoring both virtual and physical
memory through Sysinternals tools:
[VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap) for
virtual memory and
[RAMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/rammap) for
physical memory. These tools are easy to install and are thoroughly explained in
the videos mentioned at the beginning of this article.

{{< figure src="03-vmmap-sysinternals.jpg" alt="VMMap showing the virtual memory breakdown of a running process" caption="VMMap by Sysinternals." >}}

In the next article, I will discuss in detail every memory type, and how they can
be used in real applications, with examples. Your feedback and inputs are very
welcome.

## Debug virtual and physical memory usage

I noticed that Windows VMMap and RAMMap are excellent tools for capturing
snapshots of the current usage of virtual and physical memory at a specific
moment. However, they have some limitations, particularly when it comes to
tracking memory usage over an extended period of time or controlling the
snapshot frequency. Additionally, exporting formatted data that can be easily
utilized to detect and identify memory problems may be challenging with these
tools.

### Introducing MemoryTracker

Memory Tracker is a C++ open-source project designed to assist you in monitoring
the virtual memory of a specific process over time. It allows you to display data
on the screen, export well-formatted data to a file, and provides control over
the snapshot frequency.

You can integrate it into your code, utilizing it as a callback function to
precisely control when to take a snapshot. Alternatively, you can employ it in
another process if you prefer not to modify the code of the process you wish to
track.

This is an example of tracking virtual memory usage of the process with id
`32404`:

```cpp
// Process id you want to track
int Pid = 32404;

// Create MemoryTracker instance
CSnapshotMngr MyMemTracer(Pid);

// Specify the total duration and frequency, in seconds
int Duration = 120;
int PeriodT = 2;

// Export usage for 2 min by taking a snapshot each 2 seconds
MyMemTracer.Export(Duration, PeriodT);
```

{{< figure src="04-memorytracker-virtual-by-type.jpg" alt="Exported table of virtual memory usage grouped by memory type" caption="Virtual memory usage exported using MemoryTracker, regrouped by type." >}}

{{< figure src="05-memorytracker-virtual-timeline.jpg" alt="Exported chart of virtual memory usage over time, grouped by memory type" caption="The same export over time — the view VMMap's snapshots cannot give you." >}}

{{< figure src="06-memorytracker-private-bytes.jpg" alt="Exported chart of the process's private bytes grouped by memory type" caption="Private bytes of process usage exported using MemoryTracker, regrouped by memory type." >}}

I am very open to all your feedback and inputs. Thank you!

— Brahim

## Sources

- Mark Russinovich — [Virtual Memory](https://youtu.be/AjTl53I_qzY?si=TONF91WbNu6d5Ra4) (video)
- Mark Russinovich — [Physical Memory management in Windows](https://youtu.be/6KZdNsq1YV4?si=xpSamR2OSN-xyjr1) (video)
- Microsoft — [Sysinternals](https://learn.microsoft.com/en-us/sysinternals)
- Microsoft — [VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap), the virtual memory map
- Microsoft — [RAMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/rammap), the physical memory map
