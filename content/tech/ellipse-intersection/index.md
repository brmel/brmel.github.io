---
title: "How to Solve the Intersection of Two Rotated Ellipses"
date: 2026-10-11
draft: false
description: "Move two rotated ellipses and watch where they cross, then see how I find the points: one angle, one equation, solved numerically."
tags: ["Mathematics", "AI", "Testing"]
cover:
    image: "cover.jpg"
    alt: "Two rotated ellipses crossing at four numbered points, with the coordinates of each point listed beside them"
---

I wanted to find where two rotated ellipses cross, and to see it live. I worked on it with Claude, an
AI model, and I checked the results against a second method before putting it here.

Move the sliders. On the left you see the two ellipses and the points where they meet. On the right
you see the same thing as one curve: each time it crosses the dashed line, you get a point on the
left.

{{< reportframe src="reports/ellipse-intersection.html" title="Intersection of two rotated ellipses, interactive" >}}

## The idea

A point where the two ellipses meet must satisfy two equations at the same time, one for each
ellipse, with two unknowns \(x\) and \(y\). That gets messy fast.

So I remove one unknown. I walk around the first ellipse, and at each step I ask: am I inside or
outside the second one? The answer flips every time I cross it. Finding the intersections means
finding where it flips.

## An ellipse

An ellipse is a circle stretched by \(a\) along \(x\) and \(b\) along \(y\), moved to a centre
\((h, k)\) and turned by an angle \(\theta\). A point \((x, y)\) is on it when

$$u = (x-h)\cos\,\theta + (y-k)\sin\,\theta$$

$$v = -(x-h)\sin\,\theta + (y-k)\cos\,\theta$$

$$\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$$

\(u\) and \(v\) are the point's coordinates seen from the ellipse's own axes. These five numbers are
the sliders.

## The equation

Any point of the first ellipse can be written with one angle \(t\):

$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h_1 \\ k_1 \end{pmatrix} + R(\theta_1) \begin{pmatrix} a_1 \cos\, t \\ b_1 \sin\, t \end{pmatrix}$$

where \(R(\theta)\) is the rotation by \(\theta\). I put this point into the second ellipse's
equation:

$$g(t) = \frac{u_2(t)^2}{a_2^2} + \frac{v_2(t)^2}{b_2^2} - 1$$

\(g\) is negative inside the second ellipse, positive outside and zero on it. So the intersections are
the solutions of \(g(t) = 0\), with one unknown only. When you expand the squares, \(g\) always has
the same form:

$$\begin{aligned} g(t) = {} & c_0 + c_1 \cos\, t + s_1 \sin\, t \\ & + c_2 \cos\, 2t + s_2 \sin\, 2t \end{aligned}$$

The five coefficients only depend on the slider values. If you write \(z = e^{it}\), this becomes a
polynomial of degree 4 in \(z\), so there are at most four solutions: two ellipses meet in at most
four points.

For the "Four points" example in the demo, the equation is

$$\begin{aligned} 3.936 & - 3.435 \cos\, t - 0.039 \sin\, t \\ & + 4.394 \cos\, 2t = 0 \end{aligned}$$

## Solving it

There is an exact formula for degree 4, but it is long and it loses precision, mostly when the
ellipses touch. So I solve it numerically, to the precision of the computer:

1. Find where \(g\) turns, its highs and lows. There are at most four, and they come from
   \(g'(t) = 0\), another degree 4 polynomial in \(z\). I find its roots with the Durand–Kerner
   method.
2. Between two turns, \(g\) only goes up or only goes down, so it crosses zero at most once. If the
   sign is different at the two ends, I cut the interval in half again and again (bisection) until it
   can't get smaller. That gives \(t\), and \(t\) gives the point \((x, y)\).
3. If \(g\) is zero exactly at a turn, the ellipses touch there without crossing. If \(g\) doesn't
   change with \(t\) and is zero, it's the same ellipse twice.

In the example, \(g\) turns four times and changes sign between each turn, so there are four points.

To check it, I compared the results with a second method that removes \(y\) and solves for \(x\) with
very high precision, on thousands of cases: ellipses that touch, the same ellipse twice, very thin
ones, very far from the origin. Both methods always gave the same points.
