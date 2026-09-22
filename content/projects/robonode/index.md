---
title: "RoboNode"
date: 2026-08-01
projectNo: 8
domain: "infra"
status: "active"
pitch: "A robot arm you drive from your browser, to test robotics code against real physics before touching hardware."
description: "A robot arm you drive from your browser, to test robotics code against real physics before touching hardware."
metrics:
  - value: "4 nodes"
    label: "vision, tracking, trajectory and control, swappable while running"
  - value: "1 command"
    label: "docker compose up, then a robot cell in the browser"
  - value: "Sandboxed"
    label: "third-party algorithms run isolated from the cell"
stack: ["C++", "MuJoCo", "OpenCV", "Ruckig", "three.js", "Docker"]
links:
  live: ""
  repo: "https://github.com/brmel/robonode"
lede: |
  An open platform for testing robotics algorithms in real physics. Pick an
  application, swap the node that finds the part or plans the motion, and watch a
  UR10e on a rail try it in a physics engine that does not flatter anybody:
  everything you can change is data, everything you can replace sits behind one
  interface.
lessons:
  - "**The scenario has to be unfair or the result means nothing.** An easy cell makes every algorithm look competent. The default scene moves the target, delays the sensor, and puts a decoy in the bin that is the same colour as the part — so a tracker that assumes a stationary world misses visibly, and the log names what it hit rather than reporting a lower score."
  - "**One interface per capability, and the seam is the product.** Vision, tracking, trajectory and control are four typed slots with interchangeable versions and a bring-your-own option. Because the seam is owned, swapping a planner touches neither the UI, nor the CLI, nor the real-time loop — and that is the entire reason a stranger's algorithm can be dropped into a running cell at all."
  - "**Reuse the mature engines; the platform is the glue.** MuJoCo for physics, Ruckig for trajectories, OpenCV for vision, Pinocchio for kinematics. None of them is reimplemented. What is actually hard, and what I built, is the clean modular boundary and the swap-and-compare experience around them."
  - "**Third-party code runs in a sandbox, not in my process.** User algorithms compile into a fuel-bounded VM with no host surface, so a runaway loop stops instead of taking the cell with it. The moment a platform invites strangers to write control code, that stops being optional."
  - "**Every UI action has a CLI verb, and that was not free.** One contract, three surfaces — web, CLI, and other clients — with the wire format defined once. It costs discipline on every feature, and it is why the thing can be driven by a script, a person, or an agent without three implementations drifting apart."
tags: ["Robotics", "C++", "Simulation"]
resources:
  - src: "gallery/01-dashboard.png"
    params:
      caption: "Mid-place. The Contacts card is reading the physics — `pallet ↔ wrist_2_link` — and every card on the right is an algorithm that can be swapped while the cell runs."
  - src: "gallery/02-grasp-in-physics.png"
    params:
      caption: "A grasp is a constraint the model closes on the part it actually caught, not an animation of a successful pick."
  - src: "gallery/03-real-ur10e.png"
    params:
      caption: "The same contract driving a real UR10e. The simulator is the safe half of the loop, not the whole of it."
---

## The story

Every time I wanted to try a robotics idea, I had to build everything around it
first: a simulator, a robot model, a scene, a controller, and some way to see
what happened. Days of setup before the idea itself got to run once. So I mostly
judged algorithms in a notebook, on a chart, or in a simulation gentle enough
that they passed.

That setup is what I wanted to remove — not the physics, and not the robot.

## The product

One command brings up a robot cell in your browser: a UR10e on a rail, a
conveyor, a bin, a pallet, and an application you can watch run. The physics is
real, so the arm is stopped by whatever is in its way, a grasp holds the part it
actually caught, and the conveyor moves the workpiece by friction.

Four things in that cell can be swapped: what sees, what tracks the part, what
plans the path, and what drives the arm. Each one is a single interface with
several implementations behind it and an empty slot for yours. You write a grasp
offset in the editor, it compiles into a sandbox, and it becomes another version
you can select — then you run the same application against both and compare.

The failure case is the point. Switch tracking to the snapshot version, run the
moving-bin application, and the arm aims where the part *was* and misses,
exactly as it would on a real line — no rig, no safety fence, no technician.

I reused the mature engines — MuJoCo for physics, OpenCV for vision, Ruckig for
trajectory generation, Pinocchio for kinematics. What I wrote is the C++ around
them: the typed interfaces each node implements, a fuel-bounded WASM sandbox for
untrusted code, the real-time control loop and its safety gate, an HTTP and SSE
wire protocol, and the browser client and CLI that both speak it.
