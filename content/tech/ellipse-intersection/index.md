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
\(x^2/a^2 + y^2/b^2 = 1\). Move its centre to \((h, k)\) and turn it by \(\theta\), and a point is on
the ellipse when its coordinates \(u, v\) in the ellipse's own axes satisfy

$$u = (x-h)\cos\,\theta + (y-k)\sin\,\theta$$

$$v = -(x-h)\sin\,\theta + (y-k)\cos\,\theta$$

$$\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$$

Five numbers per ellipse, the five sliders below. Both equations have degree 2, so two ellipses meet
in at most \(2 \times 2 = 4\) points (Bézout's theorem), or in infinitely many when both describe the
same ellipse. The textbook route eliminates \(y\) and solves a degree-4 equation in \(x\). Its
closed form loses precision, worst of all when the ellipses touch and two roots merge into one.

## Walking around one ellipse

Walk once around ellipse 1. At angle \(t\) the walker is at

$$P(t) = \begin{pmatrix} h_1 \\ k_1 \end{pmatrix} + R(\theta_1) \begin{pmatrix} a_1 \cos\, t \\ b_1 \sin\, t \end{pmatrix}$$

where \(R(\theta)\) turns a vector by \(\theta\). Put the walker into ellipse 2's equation:

$$g(t) = \frac{u_2(t)^2}{a_2^2} + \frac{v_2(t)^2}{b_2^2} - 1$$

\(g\) is negative inside ellipse 2, positive outside and zero on it, so the intersections are the
zeros of \(g\): one unknown instead of two. Expanding the squares gives

$$\begin{aligned} g(t) = {} & c_0 + c_1 \cos\, t + s_1 \sin\, t \\ & + c_2 \cos\, 2t + s_2 \sin\, 2t \end{aligned}$$

a trigonometric polynomial of degree 2, and that shape is what makes the solver stable:

- \(g'\) has the same shape, so \(g\) has at most four turning points. They are the roots on the
  unit circle of a degree-4 polynomial in \(z = e^{it}\).
- Between two turning points \(g\) only goes up or only goes down, so it crosses zero at most once
  there, and bisection traps that crossing to full precision.
- A turning point where \(g = 0\) is a touch. A constant \(g\) means the same ellipse if it is zero,
  and no common point otherwise.

Two rules came from testing. "Zero" means within 64 rounding units of the terms in \(g\), and the
solver walks the smaller ellipse: walking the larger one fails once one ellipse is ten million times
smaller than the other.

## Try it

Each time the curve on the right meets the dashed line, a numbered point appears on the left.

{{< reportframe src="reports/ellipse-intersection.html" title="Where two ellipses meet, interactive" >}}

## How I checked it

Claude also wrote the checks, in Python, before anything went on this page. An oracle derived another
way (eliminate \(y\), then solve for \(x\) at 120 significant digits with mpmath) judged 12,991 cases:
random pairs, touches from inside and outside, the same ellipse written three ways, semi-axes from
0.001 to 1,000, coordinates up to a million, size ratios up to a billion, and every value the sliders
can produce. The JavaScript is read straight out of this page's file and run on all of them, in both
argument orders. None was wrong; on ordinary inputs the worst point is off by 4.4 × 10⁻¹⁵ of the
smaller ellipse's size.

To check the checks, I broke the solver six ways, such as dropping the rounding tolerance or walking
the larger ellipse. Each break failed between 64 and 3,186 cases.

The tests caught mistakes on both sides: a hand-written expectation that was wrong, a first version
that found four points between two identical ellipses, and three oracle bugs at vertical tangents.
One case needed neither fix. In floating point, \(\theta + \pi\) isn't exactly half a turn, so at 120
digits "the same ellipse turned half a turn" crosses itself at four points. The solver answers "same
ellipse", the only useful answer at double precision.

## Where this sits in the debate

- **July 2025.** OpenAI and Google DeepMind both reported 35 of 42 points at the International
  Mathematical Olympiad
  ([DeepMind](https://deepmind.google/en/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/),
  [The Decoder](https://the-decoder.com/openai-claims-a-breakthrough-in-llm-reasoning-on-complex-math-problems/)).
  The IMO said it "cannot validate the methods, including the amount of compute used or whether there
  was any human involvement"
  ([IMO 2025](https://imo2025.au/news/the-66th-international-mathematical-olympiad-draws-to-a-close-today/)).
- **October 2025.** An OpenAI vice-president posted that GPT-5 had solved ten open Erdős problems.
  Thomas Bloom, who maintains the list, called it "a dramatic misrepresentation": the solutions were
  in papers he hadn't known about
  ([TechCrunch](https://techcrunch.com/2025/10/19/openais-embarrassing-math/)).
- **January 2026.** A team using Gemini went through 700 open Erdős problems and addressed 13, five
  with seemingly new solutions. They wrote that the open status came "through obscurity rather than
  difficulty" ([arXiv:2601.22401](https://arxiv.org/abs/2601.22401)).
- **September 2026.** OpenAI announced that about 10,000 agents had found a singularity in the
  three-dimensional Navier–Stokes equations, formalised in Lean
  ([Quanta](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908)).
  The Clay Institute wrote that the problem "has apparently been settled" and that its review is
  "deliberately unhurried" ([Clay](https://www.claymath.org/news/navier-stokes-announcement)). The
  same week, 28 Fields Medalists signed a statement that the goals of AI companies and of
  mathematicians "are severely misaligned" ([mathandai.org](https://mathandai.org/)).

My problem sits at the other end of that range: known, with an answer I could check.
