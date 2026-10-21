---
title: "How to Solve the Intersection of Two Rotated Ellipses"
date: 2026-10-11
description: "Move two rotated ellipses and see where they cross, then the exact solution: from the ellipse equation to a quartic, solved with Ferrari’s method."
tags: ["Mathematics"]
cover:
    image: "cover.jpg"
    alt: "Two rotated ellipses crossing at four numbered points, with the coordinates of each point listed beside them"
---

Move the sliders. Each time the curve on the right crosses the dashed line, a point appears on the
left.

{{< reportframe src="reports/ellipse-intersection.html" title="Intersection of two rotated ellipses, interactive" >}}

## The ellipse

An ellipse with centre \((h, k)\), semi-axes \(a\) and \(b\), turned by an angle \(\theta\), is the
set of points \((x, y)\) where

$$u = (x-h)\cos\,\theta + (y-k)\sin\,\theta$$

$$v = -(x-h)\sin\,\theta + (y-k)\cos\,\theta$$

$$\frac{u^2}{a^2} + \frac{v^2}{b^2} = 1$$

\(u\) and \(v\) are the coordinates of the point in the ellipse's own axes.

## From two unknowns to one

A point on both ellipses satisfies both equations. Instead of solving for \(x\) and \(y\) together,
write any point of the first ellipse with one angle \(t\):

$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h_1 \\ k_1 \end{pmatrix} + R(\theta_1) \begin{pmatrix} a_1 \cos\, t \\ b_1 \sin\, t \end{pmatrix}$$

where \(R(\theta)\) is the rotation by \(\theta\). Put this point into the second ellipse's equation:

$$g(t) = \frac{u_2^2}{a_2^2} + \frac{v_2^2}{b_2^2} - 1 = 0$$

\(g\) is negative inside the second ellipse and positive outside. Expanding it gives

$$\begin{aligned} g(t) = {} & c_0 + c_1 \cos\, t + s_1 \sin\, t \\ & + c_2 \cos\, 2t + s_2 \sin\, 2t \end{aligned}$$

The coefficients come from three vectors. \(q_0\) is the centre of the first ellipse in the second
ellipse's axes: \(u_2\) and \(v_2\) at \((h_1, k_1)\), divided by \(a_2\) and \(b_2\). With
\(\delta = \theta_1 - \theta_2\):

$$q_c = \begin{pmatrix} a_1 \cos\,\delta / a_2 \\ a_1 \sin\,\delta / b_2 \end{pmatrix}$$

$$q_s = \begin{pmatrix} -b_1 \sin\,\delta / a_2 \\ b_1 \cos\,\delta / b_2 \end{pmatrix}$$

- \(c_0 = |q_0|^2 + (|q_c|^2 + |q_s|^2)/2 - 1\)
- \(c_1 = 2\, q_0 \cdot q_c\) and \(s_1 = 2\, q_0 \cdot q_s\)
- \(c_2 = (|q_c|^2 - |q_s|^2)/2\) and \(s_2 = q_c \cdot q_s\)

## A polynomial of degree 4

Write \(w = \tan(t/2)\). Then \(\cos\, t = (1 - w^2)/(1 + w^2)\) and \(\sin\, t = 2w/(1 + w^2)\),
and multiplying \(g\) by \((1 + w^2)^2\) gives

$$A w^4 + B w^3 + C w^2 + D w + E = 0$$

- \(A = c_0 - c_1 + c_2\)
- \(B = 2 s_1 - 4 s_2\)
- \(C = 2 c_0 - 6 c_2\)
- \(D = 2 s_1 + 4 s_2\)
- \(E = c_0 + c_1 + c_2\)

A polynomial of degree 4 has at most four real roots, so two ellipses cross in at most four points.
\(w\) can't reach \(t = \pi\), so if that point is an intersection, \(A = 0\). To avoid this, choose
where \(t\) starts so that the point at \(t = \pi\) is clearly inside or outside the second ellipse.

## Solving the quartic

Divide by \(A\) to get \(w^4 + p_3 w^3 + p_2 w^2 + p_1 w + p_0 = 0\). Ferrari's idea is to split it
into two quadratics:

$$(w^2 + \alpha_1 w + \beta_1)(w^2 + \alpha_2 w + \beta_2) = 0$$

Matching the coefficients gives \(\alpha_1 + \alpha_2 = p_3\),
\(\beta_1 + \beta_2 + \alpha_1 \alpha_2 = p_2\), \(\alpha_1 \beta_2 + \alpha_2 \beta_1 = p_1\) and
\(\beta_1 \beta_2 = p_0\). With \(m = \beta_1 + \beta_2\), these reduce to a cubic:

$$\begin{aligned} m^3 & - p_2 m^2 + (p_3 p_1 - 4 p_0)\, m \\ & + 4 p_2 p_0 - p_3^2 p_0 - p_1^2 = 0 \end{aligned}$$

Cardano's formula solves it. With \(m = z + p_2/3\) it becomes \(z^3 + P z + Q = 0\), where

$$P = p_3 p_1 - 4 p_0 - \frac{p_2^2}{3}$$

$$\begin{aligned} Q = {} & 4 p_2 p_0 - p_3^2 p_0 - p_1^2 \\ & + \frac{p_2 (p_3 p_1 - 4 p_0)}{3} - \frac{2 p_2^3}{27} \end{aligned}$$

If \(\Delta = Q^2/4 + P^3/27 > 0\),

$$z = \sqrt[3]{-\frac{Q}{2} + \sqrt{\Delta}} + \sqrt[3]{-\frac{Q}{2} - \sqrt{\Delta}}$$

and if \(\Delta \le 0\), the three real roots are

$$z_k = 2 \sqrt{-\frac{P}{3}} \cos\left(\frac{\varphi - 2\pi k}{3}\right)$$

$$\cos\,\varphi = -\frac{Q}{2} \left(-\frac{3}{P}\right)^{3/2}$$

Any real \(m\) gives the two quadratics:

$$\alpha_{1,2} = \frac{p_3}{2} \pm \sqrt{\frac{p_3^2}{4} - p_2 + m}$$

$$\beta_{1,2} = \frac{m}{2} \pm \sqrt{\frac{m^2}{4} - p_0}$$

with the signs paired so that \(\alpha_1 \beta_2 + \alpha_2 \beta_1 = p_1\). Each quadratic gives two
roots \(w\). Every real one is an intersection: \(t = 2 \arctan\, w\), and the
first equation of this page gives the point \((x, y)\).

Two details matter on a computer. When one of the two square roots is close to zero, rounding makes it
inaccurate, so I take only the other one and get the remaining pair from
\(\alpha_1 \beta_2 + \alpha_2 \beta_1 = p_1\). And when the cubic has three real roots, I keep the one
that satisfies the four matching equations best.

A double root is a point where the ellipses touch without crossing. If \(c_1\), \(s_1\), \(c_2\) and
\(s_2\) are all zero, \(g\) doesn't depend on \(t\): it's the same ellipse twice if \(c_0 = 0\), and
no common point otherwise.

## Example

For "Four points" in the demo, the first ellipse has centre \((0, 0)\), \(a = 3\), \(b = 1.2\),
\(\theta = 20°\), and the second has centre \((0.5, 0.3)\), \(a = 2.6\), \(b = 1\),
\(\theta = 110°\). The quartic is

$$\begin{aligned} 11.764\, w^4 & - 0.079\, w^3 - 18.489\, w^2 \\ & - 0.079\, w + 4.895 = 0 \end{aligned}$$

The root \(m = {-1.290}\) of the cubic splits it into

$$\begin{aligned} & (w^2 + 0.527\, w - 0.635) \\ & \times (w^2 - 0.534\, w - 0.656) = 0 \end{aligned}$$

The four roots are \(w = 0.576\), \(1.119\), \(-1.103\) and \(-0.586\), so \(t = 59.85°\), \(96.45°\),
\(264.41°\) and \(299.29°\). They give the four points \((1.061, 1.490)\), \(({-0.724}, 1.005)\),
\((0.134, {-1.222})\) and \((1.737, {-0.481})\).

I checked the solver against a separate method with much higher precision, on thousands of cases,
including ellipses that touch and very thin ones. Both always gave the same points.
