# Hopf's Boundary Lemma: Why a Positive Solution Cannot Touch Flatly

**Track:** Multivariable Calculus from First Principles. **Focus:** boundary point principles for the Laplacian, an explicit annular barrier, normal derivatives, and failures when the equation or geometry changes.

<!-- BEGIN SPOKEN LECTURE -->

# Hopf's Boundary Lemma: Why a Positive Solution Cannot Touch Flatly

Imagine a thin membrane held at zero height along a circular frame and pushed upward by a uniform load. The membrane rises inside the frame and returns to zero at the edge. We already know how to prove that its height cannot become negative. But how does the surface meet the frame? Could it glide toward zero so gently that its slope also vanishes at the boundary?

For the appropriate elliptic inequality, and at a boundary point with room for a ball to touch from the inside, the answer is no. If the solution is positive inside and zero at that point, it must rise at least linearly as we move into the domain. The outward normal slope, when it exists, must be strictly negative. This is the boundary point principle commonly called Hopf's lemma.

It is more than an aesthetic fact about the picture of a membrane. Boundary derivatives are fluxes for diffusion problems. A nonzero derivative at the edge can rule out supposed steady states, prove that two distinct solutions cannot meet in a certain way, and clarify how positive solutions begin to grow away from a boundary where they vanish.

## Start with an exact disk solution

Take the unit disk in the plane. Let the height at a point be one minus the square of its distance from the center. At the center the height is one, and on the circle it is zero. The Laplacian of this function is negative four, so the negative Laplacian is positive four, representing a constant positive forcing in our sign convention.

At a boundary point, walk outward in the radial direction. The derivative of the height is negative two. Walk inward, and the height initially increases at speed two per unit distance. The minimum principle tells us the height is nonnegative, but it alone would not give the strict derivative. A nonnegative smooth function can have zero derivative at its boundary minimum: on an interval, the function x squared does exactly that. What distinguishes the membrane is not simply positivity but the sign of its second-order differential inequality.

Here is the claim we will study. Let a connected domain have a boundary point p touched by an open ball lying entirely inside the domain. Let u be continuous up to that point, twice continuously differentiable inside, nonnegative in the domain, equal to zero at p, not identically zero, and assume its negative Laplacian is nonnegative. Then, moving from p along the radius into the touching ball, the increase in u is bounded below by a positive constant times the distance moved, at least for sufficiently small distances.

If u also has a first derivative at p, the derivative in the outward normal direction of that ball is strictly negative. When the domain has a differentiable boundary there, the ball's outward normal agrees with the domain's outward normal. For other uniformly elliptic operators, versions of the statement require suitable coefficient and sign assumptions; we will prove the clean Laplacian case.

## Why the interior ball matters

Picture a circle inside a region, touching the region's boundary at exactly one chosen point. The circle supplies a curved surface on which we can construct an explicit comparison function. It also identifies a distinguished inward direction: from the touching point toward the circle's center.

The hypothesis concerns local geometry. A smooth boundary has an interior tangent ball of some sufficiently small radius near each point. A sharp inward cusp need not. A corner can also violate the condition at its vertex. The theorem's conclusion is sensitive to that geometry because a positive harmonic function may vanish faster than linearly near a sharp corner.

We also need strict positivity on the inner comparison surface. Why do we have it? Under the stated assumptions, u is superharmonic: its Laplacian is nonpositive. The strong minimum principle says that a nonnegative superharmonic function on a connected domain is either identically zero or strictly positive at every interior point. We excluded the zero function. Hence u is positive on every closed sphere strictly inside the domain, and its minimum on that compact sphere is positive.

That positive minimum will let us fit a small barrier beneath u.

## Construct a barrier in an annulus

Let the touching ball have center c and radius R. Look only at the annulus inside this ball, from radius R over two out to radius R. We want a comparison function that vanishes on the outer sphere, is positive just inside it, and has a nonzero radial slope where the outer sphere meets the boundary.

An exponential does the job. Take the exponential of negative alpha times the squared distance from c, and subtract its value at radius R. For positive alpha this barrier is zero on the outer sphere and positive throughout the annulus. Its inward increase at the outer sphere is strictly linear to first order.

Now check the differential inequality instead of guessing. The Laplacian of the exponential is the exponential multiplied by four alpha squared times the squared radius minus two alpha times the dimension. In the annulus, the squared radius is at least R squared over four. If alpha is sufficiently large, the positive term dominates the negative one. Therefore the barrier's Laplacian is nonnegative throughout that annulus.

That sign is exactly what we need. The function u minus a small positive multiple of the barrier has nonpositive Laplacian, because u does and the barrier has nonnegative Laplacian. It is superharmonic.

On the outer sphere, the barrier is zero and u is nonnegative. On the inner sphere, u has a strictly positive minimum; choose the multiplier small enough that the barrier does not exceed u there. Thus u minus the scaled barrier is nonnegative on both boundaries of the annulus. The weak minimum principle makes it nonnegative throughout the annulus.

Consequently u stays above a specific positive function right up to the point of contact. We have transformed a qualitative positivity statement into a quantitative boundary growth estimate.

## Read a derivative from the barrier

Approach the touching point from inside the ball, walking distance t straight toward the center. The radius from c is then R minus t. The barrier's value is zero at t equals zero. Its first-order growth in t is two times alpha times R times the exponential of negative alpha R squared, multiplied by t. Every factor in that coefficient is positive.

Because u dominates the scaled barrier, the quotient of u at the interior point minus its boundary value, divided by t, has a strictly positive lower limit. We do not need to assume a boundary derivative exists to establish this one-sided growth statement. If the derivative does exist, it must be positive in the inward direction, so its outward normal counterpart is negative.

Notice what we did not prove. The lower-bound constant is not universal. It depends on the particular solution through its minimum on the inner sphere, and on the geometry and barrier parameters. Hopf's lemma provides strictness, not an absolute flux value for every positive solution.

Also, it does not say that every derivative of u at the boundary is nonzero. The statement concerns a specific inward direction, or the corresponding outward normal. Along the boundary itself a function identically zero there has zero tangential derivative whenever those derivatives make sense. That is compatible with a strictly nonzero normal derivative.

## Two ways the conclusion can fail

Return to the simple function x squared on the interval from zero to one. It is nonnegative, is positive inside, and vanishes at the left endpoint with zero slope. Its second derivative is positive two, however, so its negative second derivative is negative. It does not satisfy the superharmonic inequality. Dropping that sign permits flat contact even on a perfectly smooth boundary.

A more revealing failure keeps the Laplace equation but changes the geometry. Consider a planar wedge whose opening angle is less than half a turn. In polar coordinates there is an explicit harmonic function proportional to radius raised to the power pi divided by the wedge angle, multiplied by the sine of that exponent times the angular coordinate. This function is positive inside the wedge and zero on its two edges.

Because the wedge angle is less than pi, the exponent on the radius is greater than one. Near the vertex the function vanishes faster than linearly; its gradient tends to zero at the vertex. There is no interior disk tangent at that vertex while remaining inside the wedge. The missing geometric hypothesis explains the failure. A smooth solution within the wedge can have much flatter contact at a corner than at a smooth point.

This matters numerically as well. A mesh point on a reentrant or sharp corner is not entitled to the same derivative or regularity estimates as a point on a smooth part of the boundary. A numerical normal derivative computed at a corner needs more interpretation than one computed on a smooth arc.

## From the boundary slope to broader comparison arguments

Hopf's lemma is often paired with the strong maximum principle. The strong principle prohibits a nonconstant harmonic or superharmonic function from attaining an interior minimum of the appropriate kind. Hopf's lemma adds that if the minimum occurs at a smooth boundary point, the solution cannot merely touch its minimum with a flat normal slope.

For example, suppose two functions solve a linear elliptic equation and one is everywhere above the other. Their difference may be nonnegative and satisfy a homogeneous elliptic equation. If the difference vanishes at a smooth boundary point while remaining positive inside, the normal derivatives cannot agree there. This can lead to uniqueness and rigidity arguments when the boundary condition also prescribes a normal flux.

The example has limits. For a nonlinear equation, the difference of two solutions need not satisfy the same linear equation. One must first derive an appropriate linearized or comparison inequality and verify its coefficient signs. Merely saying the two functions solve the same nonlinear PDE is not enough.

Hopf's lemma also invites an important distinction between boundary growth and boundary comparison. The lemma bounds a positive solution below by a multiple of distance along a normal direction near a smooth contact point. A boundary Harnack principle compares the ratio of two positive harmonic functions that vanish along a shared boundary portion. It generally requires separate hypotheses and a separate proof. One statement does not automatically contain the other.

We began with a positive membrane and asked how it arrives at the frame. The answer depended on three different ingredients: an elliptic sign condition, a strong interior positivity result, and room for a carefully designed barrier near the boundary. All three matter. Knowing the name of the lemma is less useful than knowing which ingredient supplies which part of the conclusion.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### A precise Laplacian boundary-point statement

Let \(\Omega\subset\mathbb R^n\) be connected. Suppose \(u\in C^2(\Omega)\cap C(\overline\Omega)\) satisfies
\[
-\Delta u\ge0,\qquad u\ge0\quad\hbox{in }\Omega,
\]
with \(u\not\equiv0\) and \(u(p)=0\). Assume an open ball \(B_R(c)\subset\Omega\) touches \(p\in\partial\Omega\), so \(|p-c|=R\). Then there are \(\varepsilon,\delta>0\) such that
\[
u(p-t\nu)\ge \varepsilon\left(e^{-\alpha(R-t)^2}-e^{-\alpha R^2}\right)\ge \delta t
\quad(0<t\ll R),\qquad \nu=\frac{p-c}{R}.
\]
If \(u\) is differentiable at \(p\), then \(\partial_\nu u(p)<0\). For boundary points of a \(C^1\) domain with a tangent interior sphere, this agrees with the domain's outward normal.

### Barrier calculation

On \(A=B_R(c)\setminus\overline{B_{R/2}(c)}\), define
\[
\phi(x)=e^{-\alpha |x-c|^2}-e^{-\alpha R^2},\qquad
\Delta\phi(x)=e^{-\alpha |x-c|^2}\bigl(4\alpha^2|x-c|^2-2n\alpha\bigr).
\]
For \(\alpha\ge 2n/R^2\), the last parenthesis is nonnegative on \(A\). Choose \(\varepsilon>0\) with \(\varepsilon\max_{|x-c|=R/2}\phi(x)\le\min_{|x-c|=R/2}u(x)\). The minimum is positive by the strong minimum principle. Then
\[
\Delta(u-\varepsilon\phi)\le0,\quad
u-\varepsilon\phi\ge0\text{ on }\partial A.
\]
The weak minimum principle gives \(u\ge\varepsilon\phi\) on \(A\). Along \(p-t\nu\), Taylor expansion yields
\[
\phi(p-t\nu)=2\alpha R e^{-\alpha R^2}t+O(t^2),
\quad \liminf_{t\downarrow0}\frac{u(p-t\nu)-u(p)}t\ge 2\varepsilon\alpha R e^{-\alpha R^2}>0.
\]

### Sharp-corner counterexample

For a wedge \(W_\omega=\{r>0,\ 0<\theta<\omega\}\), \(0<\omega<\pi\), put \(\beta=\pi/\omega>1\):
\[
u(r,\theta)=r^\beta\sin(\beta\theta),\qquad
\Delta u=\partial_{rr}u+\frac1r\partial_ru+\frac1{r^2}\partial_{\theta\theta}u=0.
\]
The function is positive inside and zero on the edges, but along a fixed interior ray \(u(r,\theta)/r\to0\) as \(r\downarrow0\). The vertex has no interior tangent disk.

### Exercises and worked answers

1. **Sign check.** For \(u(x)=x^2\) on \((0,1)\), what hypothesis fails at zero? **Answer:** \(-u''=-2<0\), even though \(u\ge0\) and \(u'(0)=0\).
2. **Disk flux.** For \(u(x)=1-|x|^2\) in \(B_1(0)\subset\mathbb R^n\), compute forcing and boundary normal derivative. **Answer:** \(-\Delta u=2n\), \(\partial_\nu u=-2\).
3. **Barrier threshold.** Why can \(\alpha\ge2n/R^2\) be used? **Answer:** On \(r\ge R/2\), \(4\alpha^2r^2-2n\alpha\ge\alpha(\alpha R^2-2n)\ge0\).
4. **Wedge exponent.** For opening angle \(\omega=\pi/2\), identify the growth order. **Answer:** \(\beta=2\); the positive harmonic mode grows quadratically along interior rays.
5. **A boundary datum.** If a positive superharmonic solution has both zero Dirichlet value and zero normal derivative on a smooth boundary point, why is that incompatible with Hopf? **Answer:** The strict inequality \(\partial_\nu u<0\) contradicts the prescribed zero, provided the interior-ball and regularity hypotheses actually hold.

### Sources and further reading

- [Gautam Iyer, *Elliptic Equations* (CMU course notes)](https://www.math.cmu.edu/~gautam/c/2026-632/notes/elliptic-equations.html), barrier proof of Hopf's boundary-point lemma and strong maximum principle.
- [MIT OpenCourseWare, *Introduction to PDE*, lecture notes (lectures 3 and 9)](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2005/pages/lecture-notes/), maximum principles and Hopf's lemma.
- [Mikhail Safonov, *Boundary Estimates for Positive Solutions to Second Order Elliptic Equations*](https://arxiv.org/abs/0810.0522), geometry-sensitive Hopf–Oleinik estimates beyond the smooth setting.
- [Wikipedia: Hopf lemma](https://en.wikipedia.org/wiki/Hopf_lemma), terminology and history.
- Library prerequisites: `multivariable-calculus:047000` (comparison) and `multivariable-calculus:050000` (Harnack).
