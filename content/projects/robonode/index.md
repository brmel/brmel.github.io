---
title: "RoboNode"
date: 2026-08-01
projectNo: 8
domain: "infra"
status: "active"
pitch: "Swap the vision, the planner or the controller of a running robot cell from a browser, and watch real physics decide whether you were right."
description: "An open platform for testing robotics algorithms in real physics: swap the vision, tracking, trajectory or control node of a running UR10e cell from a browser and watch MuJoCo decide."
startHereWhy: "robotics algorithms tested in real physics, C++"
metrics:
  - value: "4 nodes"
    label: "vision, tracking, trajectory, control — each swappable while running"
  - value: "1 command"
    label: "docker compose up, then a robot cell in the browser"
  - value: "0 rigs"
    label: "needed to find out an algorithm is wrong"
stack: ["C++", "MuJoCo", "OpenCV", "Ruckig", "three.js", "Docker"]
newToMe: ["MuJoCo physics", "WebAssembly sandboxing of user code", "Ruckig trajectories", "three.js"]
links:
  live: ""
  repo: ""
lede: |
  An open platform for testing robotics algorithms in real physics. Pick an
  application, swap the node that finds the part or plans the motion, and watch a
  UR10e on a rail try it in a physics engine that does not flatter anybody:
  everything you can change is data, everything you can replace sits behind one
  interface.
takeaway: "A simulator that lets your algorithm succeed is worse than no simulator, because you believe it."
lessons:
  - "**The scenario has to be unfair or the result means nothing.** An easy cell makes every algorithm look competent. The default scene moves the target, delays the sensor, and puts a decoy in the bin that is the same colour as the part — so a tracker that assumes a stationary world misses visibly, and the log names what it hit rather than reporting a lower score."
  - "**One interface per capability, and the seam is the product.** Vision, tracking, trajectory and control are four typed slots with interchangeable versions and a bring-your-own option. Because the seam is owned, swapping a planner touches neither the UI, nor the CLI, nor the real-time loop — and that is the entire reason a stranger's algorithm can be dropped into a running cell at all."
  - "**Reuse the mature engines; the platform is the glue.** MuJoCo for physics, Ruckig for trajectories, OpenCV for vision, Pinocchio for kinematics. None of them is reimplemented. What is actually hard, and what I built, is the clean modular boundary and the swap-and-compare experience around them."
  - "**Third-party code runs in a sandbox, not in my process.** User algorithms compile to WebAssembly and execute isolated, because the moment a platform invites strangers to write control code, a crash in their planner must not take the cell down with it."
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

Testing a robotics algorithm usually means building everything around it first.
A simulator, a robot model, a scene, a controller, a way to see what happened —
days of setup before the idea you actually wanted to try gets to run once. So
most algorithms are evaluated in a notebook, on a chart, or in a simulation
gentle enough that they pass.

That is the part worth removing. Not the physics, and not the robot — the
setup.

> A simulator that lets your algorithm succeed is worse than no simulator,
> because you believe it.

## The product

One command brings up a cell in the browser: a UR10e on a rail, a conveyor, a
bin, a pallet, and a running application you can watch. The physics is real —
the arm is stopped by whatever is in its way, a grasp is a constraint on the
part it actually caught, and the conveyor moves the workpiece by friction.

Four things in that cell are **nodes**: what sees, what tracks, what plans the
path, and what controls the arm. Each is one typed interface with several
implementations and an empty slot for yours. Open the editor, write a grasp
offset, and it compiles into a sandbox and becomes another selectable version
— then run the same application against both and compare.

Breaking it is the demonstration. Switch tracking to the snapshot version and
run the moving-bin application: the arm aims where the part *was* and misses,
in the same way it would miss on a real line. Nothing about that failure needs
a rig, a safety fence, or a technician.

The engines underneath are borrowed on purpose — MuJoCo, OpenCV, Ruckig,
Pinocchio. What I built is the boundary around them, the sandbox that lets a
stranger's code run beside mine, and the one wire contract that the browser,
the CLI and anything else all speak.
