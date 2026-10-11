---
title: "Where Two Ellipses Meet: An AI Did the Maths, I Checked It 12,991 Times"
date: 2026-10-11
draft: false
description: "Two rotated ellipses cross in at most four points. An AI derived and coded the solver, I checked it on 12,991 cases. Move the sliders and watch it work."
tags: ["Mathematics", "AI", "Testing"]
cover:
    image: "cover.jpg"
    alt: "Two rotated ellipses crossing at four numbered points, with the coordinates of each point listed beside them"
---

AI labs now claim olympiad gold medals, solved Erdős problems and a result on Navier–Stokes. I can't
check those. So I gave Claude (Opus 5.5, in Claude Code) a problem I can check: where do two rotated
ellipses cross? It's a known problem, but the closed-form answer is ugly, and solvers that work on
ordinary inputs often fail when the ellipses touch, when one is very thin, or when they sit far from
the origin. I asked for the maths, a solver, and a way to prove the solver right.

## The problem

Stretch the unit circle \(x^2 + y^2 = 1\) by \(a\) along \(x\) and \(b\) along \(y\) and you get
\(x^2/a^2 + y^2/b^2 = 1\). Move its centre to \((h, k)\) and turn it by \(\theta\), and a point
\((x, y)\) is on the ellipse when its coordinates \(u, v\) in the ellipse's own axes satisfy

$$u = (x-h)\cos\,\theta + (y-k)\sin\,\theta$$

$$v = -(x-h)\sin\,\theta + (y-k)\cos\,\theta$$

$$\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$$

Five numbers describe each ellipse: the five sliders of the demo below. A point where the ellipses
meet satisfies both equations at once.

## Start simple: two circles

For two circles, subtract one equation from the other:

$$(x-h_1)^2 + (y-k_1)^2 = r_1^2$$

$$(x-h_2)^2 + (y-k_2)^2 = r_2^2$$

\(x^2\) and \(y^2\) cancel, and what is left is a straight line. Put that line back into either
circle and you get a quadratic: at most two points, solved exactly by hand.

For two ellipses with different shapes and angles, subtracting cancels nothing. Eliminating \(y\)
leaves an equation of degree 4 in \(x\), so two ellipses meet in at most 4 points (Bézout's theorem
says the same: \(2 \times 2 = 4\)). An exact formula for degree 4 exists, but it subtracts large,
nearly equal numbers and loses digits, worst of all when the ellipses touch and two roots merge.
So the solver takes another route.

## Step 1: one unknown instead of two

Every point of ellipse 1 can be named by one angle \(t\) between 0 and \(2\pi\):

$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h_1 \\ k_1 \end{pmatrix} + R(\theta_1) \begin{pmatrix} a_1 \cos\, t \\ b_1 \sin\, t \end{pmatrix}$$

where \(R(\theta)\) turns a vector by \(\theta\). Picture a walker going once around ellipse 1 as
\(t\) goes from 0 to \(2\pi\). The question becomes: at which angles is the walker also on
ellipse 2?

## Step 2: the equation we solve

Measure the walker in ellipse 2's own axes and divide by its semi-axes. In those coordinates
ellipse 2 is the unit circle, and the walker is at

$$q(t) = q_0 + q_c \cos\, t + q_s \sin\, t$$

Here \(q_0\) is the centre of ellipse 1 in those coordinates: the \(u_2/a_2\) and \(v_2/b_2\) of the
point \((h_1, k_1)\), with \(u_2, v_2\) from the formulas above. With \(\delta = \theta_1 - \theta_2\),
the other two vectors are

$$q_c = \begin{pmatrix} a_1 \cos\,\delta / a_2 \\ a_1 \sin\,\delta / b_2 \end{pmatrix}$$

$$q_s = \begin{pmatrix} -b_1 \sin\,\delta / a_2 \\ b_1 \cos\,\delta / b_2 \end{pmatrix}$$

The walker is on ellipse 2 when \(|q(t)| = 1\). So the equation is

$$g(t) = |q(t)|^2 - 1 = 0$$

\(g\) is negative while the walker is inside ellipse 2 and positive while it is outside. Expanding
the square with \(\cos^2 t = (1 + \cos\, 2t)/2\), \(\sin^2 t = (1 - \cos\, 2t)/2\) and
\(2 \sin\, t \cos\, t = \sin\, 2t\) gives

$$\begin{aligned} g(t) = {} & c_0 + c_1 \cos\, t + s_1 \sin\, t \\ & + c_2 \cos\, 2t + s_2 \sin\, 2t \end{aligned}$$

with

- \(c_0 = |q_0|^2 + (|q_c|^2 + |q_s|^2)/2 - 1\)
- \(c_1 = 2\, q_0 \cdot q_c\) and \(s_1 = 2\, q_0 \cdot q_s\)
- \(c_2 = (|q_c|^2 - |q_s|^2)/2\) and \(s_2 = q_c \cdot q_s\)

That's the whole problem: five numbers, one equation, one unknown. For the "Four points" example in
the demo, walking ellipse 1 as its \(g(t)\) strip does, \(\delta = -90°\), so \(q_c = (0, -3)\), \(q_s = (0.462, 0)\), and the equation is

$$\begin{aligned} 3.936 & - 3.435 \cos\, t - 0.039 \sin\, t \\ & + 4.394 \cos\, 2t = 0 \end{aligned}$$

## Step 3: why there are at most four answers

Write \(z = e^{it}\). Then \(\cos\, kt = (z^k + z^{-k})/2\) and \(\sin\, kt = (z^k - z^{-k})/(2i)\),
and multiplying \(g\) by \(z^2\) turns it into a polynomial of degree 4 in \(z\). A real angle \(t\)
is a root \(z\) on the unit circle, and a polynomial of degree 4 has at most four roots: at most four
intersection points, as Bézout said.

## Step 4: how the solver finds them

The equation is exact; its solutions are computed numerically, to about 16 significant digits, the
precision of the numbers the sliders give it, in three steps.

**Find where \(g\) turns.** Its derivative is

$$\begin{aligned} g'(t) = {} & -c_1 \sin\, t + s_1 \cos\, t \\ & - 2 c_2 \sin\, 2t + 2 s_2 \cos\, 2t \end{aligned}$$

and the same substitution turns \(z^2 g'\) into

$$\begin{aligned} T(z) = {} & 2(s_2 + i c_2)\, z^4 + (s_1 + i c_1)\, z^3 \\ & + (s_1 - i c_1)\, z + 2(s_2 - i c_2) \end{aligned}$$

The solver finds its four roots with the Durand–Kerner iteration: start from four guesses on the unit
circle, replace each guess by

$$z_1 - \frac{T(z_1)}{A\,(z_1 - z_2)(z_1 - z_3)(z_1 - z_4)}$$

(shown for \(z_1\), the same for the others), where \(A = 2(s_2 + i c_2)\) is the leading
coefficient, and repeat until the guesses stop moving. The angles \(t = \arg z\) cut the walk into at
most four stretches. On each stretch \(g\) only goes up or only goes down, so it crosses zero at most
once.

**Trap each crossing.** If \(g\) has opposite signs at the two ends of a stretch, there is exactly one
zero inside. Bisection halves the stretch and keeps the half where the sign changes; after about 53
halvings the two ends are neighbouring numbers in double precision, and that is the answer. Putting
\(t\) back into Step 1 gives \((x, y)\).

**Handle the special cases.** A turning point where \(g = 0\) is a touch: the walker reaches
ellipse 2 and turns back. If every coefficient except \(c_0\) is zero, \(g\) is constant: the same
ellipse when \(c_0 = 0\), no common point otherwise. "Zero" means within 64 rounding units of the
terms in \(g\), and the solver walks the smaller of the two ellipses, because walking the larger one
fails once one is ten million times smaller.

In the example, \(g\) turns at 78.8°, 180.1°, 281.3° and 359.8°, where it equals −0.83, 11.76, −0.75
and 4.90. The signs alternate, so each stretch holds one zero: \(t\) = 59.85°, 96.45°, 264.41° and
299.30°. Step 1 maps them to (1.061, 1.490), (−0.724, 1.005), (0.134, −1.222) and (1.737, −0.481),
the four points the demo shows.

Before it went on this page, I checked the solver against an independent method: eliminate \(y\) and
solve the degree-4 equation in \(x\) at 120 significant digits. On 12,991 cases, including touches,
identical ellipses, needle-thin shapes, coordinates up to a million and every value the sliders can
produce, the JavaScript running below found the same points. On ordinary inputs they agree within
4.4 × 10⁻¹⁵ of the smaller ellipse's size.

## Try it

Each time the curve on the right meets the dashed line, a numbered point appears on the left.

{{< reportframe src="reports/ellipse-intersection.html" title="Where two ellipses meet, interactive" >}}
