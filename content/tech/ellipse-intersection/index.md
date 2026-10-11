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

In July 2025, two AI labs announced gold-medal scores at the International Mathematical Olympiad.
In October, a post claiming that GPT-5 had solved ten open Erdős problems was deleted within days.
In September 2026, OpenAI announced a result on the Navier–Stokes equations, one of the Millennium
Prize problems. Those are claims I can't check myself.

So I took a problem I can check: where do two rotated ellipses cross? It's a known problem, solved in
textbooks and in geometry libraries, so this is not about new mathematics. But it's easy to state, the
closed-form answer is ugly, and a solver that is right on ordinary inputs is often wrong when the
ellipses touch, when one is a thousand times thinner than the other, or when they sit a million units
from the origin. I gave it to Claude (Opus 5.5, in Claude Code) and asked for three things: the maths,
a solver, and a way to prove the solver right before it went on this page.

## The problem

An ellipse is a stretched circle. Start from the circle of radius 1,

$$x^2 + y^2 = 1$$

stretch it by \(a\) along \(x\) and by \(b\) along \(y\) (the two semi-axes),

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

and move its centre to \((h, k)\):

$$\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$$

To turn it by an angle \(\theta\), measure each point in the ellipse's own tilted axes:

$$u = (x-h)\cos\,\theta + (y-k)\sin\,\theta$$

$$v = -(x-h)\sin\,\theta + (y-k)\cos\,\theta$$

$$\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$$

Five numbers, \(h\), \(k\), \(a\), \(b\) and \(\theta\), describe any ellipse. They are the five
sliders of each ellipse in the demo below.

A point lies on both ellipses when it satisfies both equations. Expand either one and you get a
general equation of degree 2:

$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$$

Two curves of degree 2 meet in at most \(2 \times 2 = 4\) points (Bézout's theorem). So the answer is
always 0, 1, 2, 3 or 4 points, or infinitely many when the two descriptions draw the same ellipse.

The classic way is to eliminate \(y\) and get one equation of degree 4 in \(x\). There is a formula
for its roots (Ferrari found it in the 1540s), but it is long and it loses precision. Two cases are
harder still. When the ellipses touch, two roots merge into one, and a rounding error decides whether
you see 0, 1 or 2 points. And when two intersection points share the same \(x\), the elimination
can't tell them apart.

## Walking around one ellipse

The method Claude proposed, and that I kept, avoids the elimination. Walk once around ellipse 1. At
angle \(t\) the walker is at

$$P(t) = \begin{pmatrix} h_1 \\ k_1 \end{pmatrix} + R(\theta_1) \begin{pmatrix} a_1 \cos\, t \\ b_1 \sin\, t \end{pmatrix}$$

where \(R(\theta)\) turns a vector by \(\theta\). At every step, put the walker into ellipse 2's
equation:

$$g(t) = \frac{u_2(t)^2}{a_2^2} + \frac{v_2(t)^2}{b_2^2} - 1$$

\(g\) is negative when the walker is inside ellipse 2, positive outside and zero on it. The
intersection points are the angles where \(g(t) = 0\), so the problem now has one unknown instead
of two.

Each of \(u_2/a_2\) and \(v_2/b_2\) is a constant plus a multiple of \(\cos\, t\) plus a multiple of
\(\sin\, t\). Squaring them and using \(\cos^2\, t = (1 + \cos\, 2t)/2\) turns \(g\) into

$$\begin{aligned} g(t) = {} & c_0 + c_1 \cos\, t + s_1 \sin\, t \\ & + c_2 \cos\, 2t + s_2 \sin\, 2t \end{aligned}$$

a trigonometric polynomial of degree 2. If \(q_0\), \(q_c\) and \(q_s\) are the vectors of constants,
cosine and sine multiples, the five coefficients are \(c_0 = |q_0|^2 + (|q_c|^2 + |q_s|^2)/2 - 1\),
\(c_1 = 2\, q_0 \cdot q_c\), \(s_1 = 2\, q_0 \cdot q_s\), \(c_2 = (|q_c|^2 - |q_s|^2)/2\) and
\(s_2 = q_c \cdot q_s\).

That shape is what makes the solver stable:

- Its derivative \(g'(t)\) has the same shape, so \(g\) has at most four turning points.
- Between two turning points \(g\) only goes up or only goes down, so it crosses zero at most once
  there. If its sign differs at the two ends, bisection traps the crossing: halve the interval, keep
  the half where the sign changes, and stop when the midpoint can't move any more.
- A turning point where \(g\) is zero is a touching point: the walker reaches ellipse 2 and turns back.
- If every coefficient except \(c_0\) is zero, \(g\) is constant. Zero everywhere means the two
  ellipses are the same curve; any other constant means they have no point in common.

That leaves finding the turning points. With \(z = e^{it}\), \(\cos\, t = (z + 1/z)/2\) and
\(\sin\, t = (z - 1/z)/(2i)\), so \(z^2 g'(t)\) is a polynomial of degree 4 in \(z\), and the turning
points are its roots on the unit circle \(|z| = 1\). The solver cuts the walk at the angle of every
root; a root off the circle only adds a harmless extra cut.

Two details came from testing rather than from the derivation. "Zero" means within 64 rounding units
of the size of the terms in \(g\), so a touch computed with rounding noise still reads as one touch.
And the solver always walks the smaller ellipse: walking the larger one gave the wrong number of points
every time one ellipse was ten million times smaller than the other.

## Try it

Move the sliders or pick an example. The numbers under the drawing are the solver's answer,
recomputed on every change in about 12 microseconds. The strip below them is \(g(t)\) for one walk
around ellipse 1: every time the curve meets the dashed line is a point in the drawing.

{{< reportframe src="reports/ellipse-intersection.html" title="Where two ellipses meet, interactive" >}}

## How I checked it

Before any of this went on the page, it ran in a scratch folder in Python:

- A reference solver in Python with numpy, the same algorithm step for step.
- An oracle derived another way: write both ellipses as conics, eliminate \(y\) with a resultant,
  solve the degree-4 equation in \(x\) and substitute back, all at 120 significant digits with mpmath.
  A mistake in the walking derivation can't hide in a derivation that doesn't walk.
- 12,991 cases in ten families, each solved in both argument orders.

| Family | Cases | What it tests |
|---|---:|---|
| Named edge cases | 28 | four points, touching from outside and inside, three points, a touch at \(t = \pi\), the same ellipse described three ways, needles, a million units from the origin |
| Random pairs | 2,000 | ordinary inputs |
| Touching from outside | 500 | an ellipse mirrored across its own tangent line, then scaled |
| Touching from inside | 500 | a scaled-down copy pinned to one point of the original |
| Same curve | 60 | turned half a turn, or axes swapped and turned 90° |
| Extreme shapes | 1,000 | semi-axes from 0.001 to 1,000 |
| Scaled, turned and moved | 1,000 | scale from 10⁻⁶ to 10⁶, shifts up to 10⁶ |
| Small on the edge of large | 500 | size ratios up to 10⁹ |
| Slider grid | 5,000 | the exact values the sliders produce |
| Walking through a touch | 2,403 | one ellipse sliding through a touch in small steps |

The JavaScript on this page is checked by reading the solver straight out of the page's file and
running it on the same 12,991 cases with Node. 0 were wrong. On ordinary inputs the worst point is off
by 4.4 × 10⁻¹⁵ of the smaller ellipse's size. It reaches 4.9 × 10⁻⁷ only when the coordinates are a
million times larger than the ellipse, which is the rounding of the input numbers themselves. A
separate Python run on 20,000 more slider positions and 6,003 sliding steps found no difference with
the oracle.

Then I broke the solver on purpose, one change at a time, to see whether the checks would notice:

| Change | Wrong answers out of 12,991 |
|---|---:|
| No rounding tolerance | 932 |
| Report every touch as a crossing | 1,006 |
| Always solve the degree-4 polynomial, even when it is really degree 2 | 404 |
| Never report "same ellipse" | 64 |
| Skip the first stretch between turning points | 3,186 |
| Walk ellipse 1 instead of the smaller one | 184 |

One step survived that: a Newton correction of the turning points. Removing it changed no answer, so
I removed it.

## What went wrong on the way

- The first test run had one failure: a narrow ellipse crossing another at its far end, \(t = \pi\).
  The solver found two points and the test expected one. The test was wrong. Claude had written the
  expectation by hand, and the ellipses do cross twice.
- The first version returned four meaningless points for two identical ellipses. Every coefficient was
  around 10⁻¹⁶ instead of zero, and the root finder found the roots of rounding noise. The constant
  check above fixed it.
- The oracle disagreed with the solver on three named cases, and all three were oracle bugs: its test
  for a real root was relative to quantities that are zero where an ellipse has a vertical tangent.
- One disagreement was neither. "The same ellipse turned half a turn" is not the same ellipse in
  floating point, because \(\theta + \pi\) is not exactly half a turn from \(\theta\). At 120 digits
  the two curves differ by about 10⁻¹⁶ radians and cross at four points. The solver says "same
  ellipse", which is the only useful answer at double precision.
- The first JavaScript check judged only one argument order, so removing the smaller-ellipse rule went
  unnoticed. It now judges both, and the "small on the edge of large" family was added because no
  random family put a tiny ellipse on a big one's edge.

## Where this sits in the debate

- **July 2025.** OpenAI and Google DeepMind both reported 35 out of 42 points at the International
  Mathematical Olympiad, gold-medal level, with proofs written in natural language
  ([DeepMind](https://deepmind.google/en/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/),
  [The Decoder](https://the-decoder.com/openai-claims-a-breakthrough-in-llm-reasoning-on-complex-math-problems/)).
  The IMO's president said it "cannot validate the methods, including the amount of compute used or
  whether there was any human involvement"
  ([IMO 2025](https://imo2025.au/news/the-66th-international-mathematical-olympiad-draws-to-a-close-today/)).
- **October 2025.** An OpenAI vice-president posted that GPT-5 had found solutions to ten previously
  unsolved Erdős problems. Thomas Bloom, who maintains the Erdős problems site, called it "a dramatic
  misrepresentation": the solutions were in papers he hadn't known about
  ([TechCrunch](https://techcrunch.com/2025/10/19/openais-embarrassing-math/)).
- **January 2026.** A team using Gemini went through 700 Erdős problems marked open and addressed 13:
  five with seemingly new solutions, eight already solved in the literature. They wrote that the open
  status came "through obscurity rather than difficulty"
  ([arXiv:2601.22401](https://arxiv.org/abs/2601.22401)).
- **February to June 2026.** In the First Proof challenge, mathematicians posed ten unpublished
  research problems. In the first round, Scientific American's early report counted two correct AI
  solutions; in the second round, 7 of the 10 problems got at least one passing solution
  ([Scientific American](https://www.scientificamerican.com/article/first-proof-is-ais-toughest-math-test-yet-the-results-are-mixed/),
  [arXiv:2606.18119](https://arxiv.org/abs/2606.18119)).
- **April 2026.** Terence Tao wrote that mathematics is moving "from an era of proof scarcity to an era
  of proof abundance" ([Mathstodon](https://mathstodon.xyz/@tao/116477351524980995)).
- **September 2026.** OpenAI announced that about 10,000 agents running on an unreleased model had
  found a singularity in the three-dimensional Navier–Stokes equations, formalised in Lean
  ([Quanta](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908)).
  The Clay Institute wrote that the problem "has apparently been settled" and that its review is
  "deliberately unhurried" ([Clay](https://www.claymath.org/news/navier-stokes-announcement)). The
  same week, 28 Fields Medalists, Tao among them, signed a statement that "the goals of the AI
  companies and the goals of the mathematical community are severely misaligned"
  ([mathandai.org](https://mathandai.org/)).

My problem sits at the other end: known, with a known answer. In one session Claude wrote the
derivation, the Python and JavaScript solvers, the 120-digit oracle and the 12,991 cases that let me
put it on this page.
