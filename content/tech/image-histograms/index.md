---
title: "Counting Saw Blade Teeth with Edge Measurement"
date: 2025-01-08
description: "Why scanning a circle around the arbor hole works on real images where thresholding doesn’t, and how the tooth spacing checks the count."
cover:
    image: "01-saw-blade.png"
    alt: "A circular saw blade with the arbor hole at its centre"
---

Counting the teeth on a saw blade looks trivial and isn't. You can see the
teeth. A vision system can't: it has a grid of intensities, and everything you
want to know has to come out of where those intensities change.

{{< figure src="01-saw-blade.png" alt="A circular saw blade with the arbor hole at its centre" caption="Every number below comes from the arbor hole and one circle drawn through the teeth." >}}

## Measure across the teeth

The instinct is to find the blade's outline and count the bumps on it. That
means separating blade from background, which means picking a threshold, and a
threshold assumes the lighting stays the same, which it won't.

Instead, put a circle on the image, centred on the arbor hole, at a radius that
passes through every tooth, and read the image along that circle. A closed path through all the teeth turns a two-dimensional
counting problem into a one-dimensional signal with one feature per tooth.

## The origin comes from the part

The circle needs a centre, and the centre has to be a feature of the blade
rather than a position in the frame. The arbor hole is the obvious candidate:
fit a circle to it and every measurement afterwards is expressed relative to
the part.

The blade is never placed the same way twice. If the origin travels with the
blade, that stops being a problem.

## Count stripes

An edge is a single transition. A stripe is a pair of them: a rising edge and
a falling edge, of a stated polarity, with a width between them.

Counting stripes rather than edges makes this reliable. An edge
is a place where the intensity moved, and plenty of things move it: a glint on
ground steel, a scratch, the seam of the background. A stripe has a width,
and a width is something you can reject on. Noise readily produces one
transition. It's much less likely to produce a matched pair of the right polarity,
of roughly the right width, at roughly the right spacing.

So the parameters that matter are the ones that describe the tooth as an
object: polarity, taken from which way the tooth is darker than what surrounds
it; a width range, taken from the blade specification rather than from the
image; and a contrast threshold set high enough that a soft gradient isn't
allowed to be a tooth. Edge positions come out at sub-pixel precision from the
shape of the intensity gradient.

## Check the spacing

If the count is right, the teeth are evenly spaced in angle. That's a
property of the part you're already holding, so it's free.

Convert each detected stripe to an angle about the centre, take the gaps
between consecutive angles, and look at their spread. Uniform gaps mean you
counted teeth. One gap at twice the others means you missed one, and the gap
tells you where to look. Gaps at half the spacing mean you counted
something twice.

A system that
reports 71 teeth is useless, because nobody can tell whether it is right. A
system that reports 72 and can say the angular spacing was uniform to within a
fraction of a degree has measured something.

## What breaks

Three things, in my experience, and none of them is the algorithm.

**Reflection.** Ground steel is close to a mirror. A specular highlight
crossing the scan path is high-contrast and looks like the transition
you are hunting for. This is a lighting problem, and the fix is diffuse,
off-axis lighting. Lowering a threshold until the highlight goes
away also removes the teeth.

**Teeth that are not identical.** Many blades are ground with an alternate top
bevel, so consecutive teeth are angled opposite ways and don't present the
same face to the camera. Anything that assumes every tooth looks like the last
one will find half of them. The width tolerance has to cover both appearances,
and the periodicity check has to expect one tooth per gap rather than one
bevel.

**The radius.** Too close to the hub and the path passes inside the tooth roots
and sees nothing. Too far and it leaves the blade between teeth and the signal
becomes background. It wants to sit where the teeth are widest, and it is worth
deriving it from the detected hole radius rather than fixing it, so that one
recipe covers a family of blade sizes.

## Where this generalises

None of this is specific to saw blades. It applies to gear teeth, holes in a
perforated sheet, splines on a shaft, threads, connector pins, or anything
repetitive arranged around something you can locate.

{{< youtube id="uJoLyFe7R1g" poster="02-tooth-count-demo.jpg" title="The tooth count running on the saw blade, on YouTube." >}}
