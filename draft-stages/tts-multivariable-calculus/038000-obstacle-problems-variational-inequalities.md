# Obstacle Problems: From Energy Minima to Variational Inequalities

**Track:** Multivariable Calculus from First Principles. **Focus:** closed convex constraints in function spaces, variational inequalities, contact sets, complementary forces, free boundaries, and a solved one-dimensional obstacle problem.

<!-- BEGIN SPOKEN LECTURE -->

# Obstacle Problems: From Energy Minima to Variational Inequalities

Imagine a stretched elastic string suspended above a fixed curved barrier. The ends of the string are pinned. The string can rise above the barrier, and it can touch the barrier, but it cannot pass through it. Where it touches, the barrier supplies a contact force; where it is free, the string follows its ordinary equilibrium equation. We do not know in advance which parts will touch.

This is an obstacle problem. It differs from the fixed-boundary problems we have solved before because the constraint is an inequality at every point of an interval. The location of the active constraint is itself an unknown. Such problems arise in contact mechanics, membranes, potential theory, and mathematical models of free boundaries.

The calculus of variations still helps us, but the first-order condition changes. At an unconstrained minimum, the first variation vanishes in every admissible direction because both positive and negative perturbations are possible. At a point lying against an obstacle, some directions are forbidden. We get an inequality, not an equality. This is the infinite-dimensional relative of the Karush–Kuhn–Tucker conditions from constrained optimization.

We will derive the inequality, prove existence and uniqueness under transparent assumptions, and then solve a complete example. The example will have a central contact region, two free regions, and contact points that we determine exactly rather than guessing from a picture.

## Choose an admissible set

Let the string occupy the interval from negative one to one. Its endpoints have height zero, and the obstacle height is a prescribed function psi. A candidate u must be in the zero-boundary H one space and must remain at least as high as psi almost everywhere.

The phrase almost everywhere is the natural one in a Sobolev space. In one dimension, the functions have continuous representatives, so when psi is continuous the inequality also holds pointwise for those representatives. In higher dimensions one needs more care, since a Sobolev function need not have a well-defined value at each individual point.

Call the feasible set K. It must be nonempty. If the obstacle rises above the pinned endpoint values right at a boundary in a way no H one function can accommodate, feasibility itself could fail. In our explicit example the obstacle will lie below the endpoint heights, and we will be able to exhibit a feasible curve explicitly. The zero function, however, will not be feasible because the obstacle rises above zero at the center.

The set K is convex. If u and v both remain above the obstacle, every weighted average between them also remains above it. It is also closed in the H one norm: strong H one convergence implies strong L two convergence, from which the inequality is preserved in the limit. Because it is a norm-closed convex subset of a Hilbert space, it is weakly closed as well.

That last property matters. When we extract a weakly convergent subsequence from a sequence of feasible approximations, the limit is still feasible. We will not discover an apparent minimum that passes through the obstacle simply because we weakened the topology.

## The energy and its first-order condition

For now take no external load. The string's energy is one half the integral of squared slope from negative one to one. We seek the feasible u with the least energy. This is a strict convex minimization problem on K, since the pinned endpoints eliminate constant directions.

Let u be a minimizer and choose any other feasible function v. Since K is convex, the entire straight path in function space from u toward v is feasible. Move only a fraction t of the way, with t between zero and one. The energy cannot decrease for small positive t, so its right derivative at t equals zero or is positive.

Expanding the squared-slope energy gives the right derivative exactly: the integral of u prime times v prime minus u prime. Therefore the necessary condition is that the integral of u prime times the derivative of v minus u is at least zero for every feasible v.

This is a variational inequality. Notice the direction. At an interior point of the feasible set, we could perturb in both positive and negative directions, and the first variation would vanish. At the obstacle, we can only move into the feasible set. The first variation need only be nonnegative in those allowed directions.

In fact, for our convex quadratic energy, this condition is also sufficient. Expand the energy of any feasible v around u. The difference is the first-order term plus one half the squared slope norm of v minus u. Both are nonnegative. Therefore no feasible competitor has lower energy. Strict convexity makes the minimizer unique.

If we restore a load f, the condition becomes the integral of u prime times the derivative of v minus u, greater than or equal to the integral of f times v minus u. This is the basic weak form of the loaded obstacle problem.

## Contact force and complementarity

What does the variational inequality say away from contact? Suppose we have an open interval where u lies strictly above the obstacle by some positive margin. On a smaller interval inside it, both positive and negative perturbations of sufficiently small amplitude remain feasible. Testing both signs forces the first variation to vanish. With no load, the string has zero second derivative there. Thus it is a straight line wherever it is free.

At contact, negative perturbations may be forbidden. In a sufficiently regular situation, integration by parts turns the first variation into the distribution negative u double prime. The contact force is the nonnegative quantity negative u double prime minus f. It may be represented by a function or, more generally, by a distribution or measure under suitable conditions.

The familiar complementarity picture emerges: the gap u minus psi is nonnegative; the reaction pushing upward is nonnegative; and the reaction is supported on the contact region where the gap vanishes. Where the string is free, the contact reaction is zero. At contact, a positive reaction can balance the tendency of the unconstrained string to fall through the barrier.

These statements resemble the finite-dimensional conditions for an inequality constraint. But one must not assume every multiplier is a smooth ordinary function. Contact can concentrate forces, especially with corners or point constraints. The variational inequality remains meaningful in the energy space even when the classical multiplier picture needs additional regularity.

## A barrier for which we can find everything

Now make the obstacle explicit: its height at x is one minus four x squared, on the interval from negative one to one. It is a downward-opening parabola, reaching height one at the center. At the endpoints its value is negative three, safely below the pinned string height of zero. For example, the arch one minus x squared is a feasible curve: it has zero endpoints and lies at least as high as one minus four x squared everywhere.

The string must touch or pass above the central bump. If we minimize slope energy, it will not choose to rise higher than necessary; and in the free portions, where no obstacle reaction acts, it must be straight. By symmetry we should expect a central contact interval running from negative a to positive a, with straight segments leading to the endpoints.

Treat this as a candidate construction, not yet a proof. On the central interval let u equal the parabolic obstacle. On the right, let u be the line descending to zero at x equal to one. The left-hand line will be its mirror image.

Where the curved part meets the straight part, the simplest plausible physical condition is matching height and slope. If there were a sudden jump in slope, its second derivative would contain a concentrated contribution. For the smooth obstacle and the solution we seek, matching slope is consistent with the nonnegative reaction. We can also treat it as a condition to be verified afterward, rather than as a rule imposed without proof.

The slope of the obstacle at x equal to a is negative eight a. A line with that slope and value zero at x equal to one has height eight a times one minus x. At x equal to a, continuity of height requires eight a times one minus a to equal one minus four a squared.

Rearrange that equation and solve the quadratic. The root inside the interval is one minus the square root of three divided by two, approximately zero point one three four. The other root lies outside the interval and is not physically relevant to this construction.

The candidate solution is now explicit. Between negative a and a, it follows one minus four x squared. To the right of a, it is eight a times one minus x. To the left of negative a, it is eight a times one plus x. It is even, continuous, and continuously differentiable, and its endpoints are zero.

## Check the obstacle and prove optimality

It is not enough that the pieces match. We must check that the straight portions never pass below the obstacle. A tangent line to a concave parabola lies above the parabola. Our right line is exactly the tangent to the obstacle at a, and our left line is the corresponding tangent at negative a. Therefore the candidate lies above the obstacle everywhere, touching it on the central interval and leaving it on both sides.

Inside the contact interval the second derivative of our candidate is negative eight, so negative u double prime is positive eight. Outside, the function is affine and the second derivative is zero. Because the first derivative matches at the two transition points, there is no extra point mass in the distributional second derivative.

Now choose any feasible competitor v. Integrate the product of u prime with the derivative of v minus u by parts. The boundary terms vanish because both functions have the same pinned endpoints. The integral becomes the integral of negative u double prime times v minus u. It is eight times the integral, over the central contact region, of v minus the obstacle.

That integrand is nonnegative, because every competitor lies above the obstacle and our candidate equals it on the contact region. Therefore the variational inequality holds for every feasible v. We have verified the sufficient condition for a global minimum. Strict convexity then proves that no different feasible string has the same minimum energy.

This is a complete solution of a free-boundary problem. We did not know a in advance. The energy condition, the obstacle geometry, and the contact-force sign fixed it. The boundary between contact and noncontact is called a free boundary because its location is part of the solution.

## What if we add a downward or upward force?

Restoring an external load changes the free equation. Where the string is clear of the obstacle, its second derivative balances the load through negative u double prime equals f. Constant positive f produces a downward-opening parabola in the free regions, rather than a line. The contact region can widen or shrink depending on how the load acts and which sign convention we use.

The variational inequality still contains the entire problem. For every competitor v above the obstacle, the difference of slopes tested against u must dominate the work of the load against v minus u. The geometry of the contact set adjusts until that inequality holds globally.

From the computational point of view, the problem resembles an active-set method with potentially infinitely many constraints. Discretize the interval with a finite-element mesh, and each nodal obstacle restriction becomes an inequality on a nodal coefficient, provided the approximation space and obstacle representation make that interpretation valid. One can then solve a convex quadratic program and update the active nodes. As the mesh is refined, the numerical contact set should approximate the free boundary, subject to the discretization and regularity assumptions of the method.

But a small linear-system residual is not enough to certify the obstacle solution. We also need feasibility and a condition on the first variation in feasible directions. A method could solve its unconstrained equations extremely accurately and still pass through the obstacle. Constrained numerical work must check both stationarity and the inequalities.

## The existence argument behind the example

Our explicit solution was possible because the obstacle and interval were simple. We should also know that the abstract minimization problem is well posed. The admissible set K is nonempty, convex, and weakly closed in H naught one. The energy is continuous, coercive, and weakly lower semicontinuous. Therefore the direct method guarantees that a minimizer exists. Strict convexity guarantees uniqueness.

This proof remains available even when we cannot guess the contact set, and even when the obstacle is irregular enough that an elementary closed-form solution is out of reach. More general obstacle problems may require careful assumptions to make the feasible set nonempty, the energy meaningful, and the boundary data compatible. Under such assumptions, the variational inequality is often the most reliable formulation of the problem.

We have moved from optimizing a number, to optimizing a function, to optimizing a function subject to infinitely many inequalities. The basic logic has not changed. Existence comes from coercivity, weak compactness, and lower semicontinuity. Optimality comes from the sign of the first variation along feasible directions. The new element is that the set of active directions changes with the solution itself, producing contact regions and free boundaries.

This is why weak formulations and compactness matter beyond abstract analysis. They make physical contact constraints precise, support numerical algorithms, and let us distinguish a computed approximation from a solution whose existence and optimality are actually justified.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### The obstacle variational inequality

On \(I=(-1,1)\), let \(\psi\in H^1(I)\) be an obstacle with nonempty feasible set

\[
K=\{u\in H_0^1(I):u\ge\psi\text{ a.e.}\}.
\]

For \(f\in L^2(I)\), minimize

\[
E_f(u)=\frac12\int_I|u'|^2\,dx-\int_Ifu\,dx\qquad\text{over }u\in K.
\]

The set \(K\) is convex. It is strongly closed in \(H_0^1\): if \(u_n\to u\) strongly in \(L^2\), then \(\|(\psi-u)_+\|_2\le\|u-u_n\|_2\) whenever \(u_n\ge\psi\), hence \(u\ge\psi\) a.e. Since closed convex subsets of Hilbert spaces are weakly closed, the direct method applies. Coercivity follows from Poincaré and the quadratic derivative term; weak lower semicontinuity follows from the squared norm plus weak continuity of the load. Thus a unique minimizer exists.

For every \(v\in K\), \(u+t(v-u)\in K\) for \(0\le t\le1\). Differentiation at \(t=0^+\) gives

\[
\boxed{\int_I u'(v'-u')\,dx\ge\int_I f(v-u)\,dx\qquad\forall v\in K.}
\]

Conversely, if this inequality holds, then

\[
E_f(v)-E_f(u)=\int_Iu'(v'-u')\,dx-\int_If(v-u)\,dx
+\frac12\int_I|v'-u'|^2\,dx\ge0.
\]

This proves global optimality. Strict convexity on \(H_0^1\) proves uniqueness.

### Explicit central-contact solution for a quadratic barrier

Set \(f=0\), \(\psi(x)=1-4x^2\), and

\[
a=1-\frac{\sqrt3}{2}\in(0,1),\qquad c=8a.
\]

Define

\[
u(x)=\begin{cases}
c(1+x),&-1\le x<-a,\\
1-4x^2,&-a\le x\le a,\\
c(1-x),&a<x\le1.
\end{cases}
\]

Tangency follows from \(c=8a\) and the identity

\[
8a(1-a)=1-4a^2
\iff 4a^2-8a+1=0
\iff a=1-\frac{\sqrt3}{2}.
\]

The tangent lines to the concave obstacle satisfy \(u\ge\psi\) outside \([-a,a]\), and equality holds inside. The derivative is continuous at \(\pm a\), so there are no Dirac masses in \(u''\). As a distribution,

\[
-u''=8\,\mathbf{1}_{(-a,a)}\ge0.
\]

For every feasible \(v\), integrating by parts yields

\[
\int_{-1}^1u'(v'-u')\,dx
=\int_{-1}^1(-u'')(v-u)\,dx
=8\int_{-a}^a(v-\psi)\,dx\ge0.
\]

Thus \(u\) is the unique energy minimizer. The contact-force density \(\mu=-u''=8\mathbf{1}_{(-a,a)}\) satisfies \(\mu\ge0\), \(u-\psi\ge0\), and \(\mu(u-\psi)=0\) a.e. The free boundary consists of the two points \(\{-a,a\}\).

The energy is

\[
E_0(u)=\frac12\int_{-1}^1|u'|^2dx
=64a^2(1-a)+\frac{64}{3}a^3
=64a^2-\frac{128}{3}a^3.
\]

This explicit multiplier is a bounded function because the chosen obstacle is smooth and the candidate has matching slopes. For rougher obstacles and data, the reaction may require a measure or distribution interpretation; the variational inequality remains the primary statement.

### Exercises with answers

1. **Convex feasibility:** If \(u,v\ge\psi\) a.e., show \((1-t)u+tv\ge\psi\) for \(0\le t\le1\). **Answer:** Take the same convex combination of the inequalities.
2. **Right contact point:** Solve \(8a(1-a)=1-4a^2\) and select the root in \((0,1)\). **Answer:** \(a=1-\sqrt3/2\).
3. **Free equation:** Why is \(u\) affine on \((a,1)\) when \(f=0\)? **Answer:** On a free interval both perturbation signs are allowed, so \(-u''=0\) distributionally there.
4. **Complementarity:** Verify \(\mu(u-\psi)=0\). **Answer:** On \((-a,a)\), \(u=\psi\); elsewhere \(\mu=0\).
5. **Optimality certificate:** Explain why the variational inequality for \(f=0\) proves global minimality. **Answer:** The exact energy gap is the nonnegative first-order term plus \(\|v'-u'\|_2^2/2\).

### Sources and further reading

- Thomas Schmidt, [*Calculus of Variations*, Hamburg lecture notes](https://www.math.uni-hamburg.de/home/schmidt/lectures/CalcVar.pdf), §3.2 for convex constraints and obstacle problems.
- Andreas Minne, [*An Introduction to the Obstacle Problem* (2026), lecture notes](https://arxiv.org/abs/2610.37943), for one-dimensional models, variational inequalities and free-boundary structure.
- J. C. Wei, [*The Direct Methods in the Calculus of Variations*, UBC lecture notes](https://personal.math.ubc.ca/~jcwei/MATH517-2018-Lectnotes2.pdf), for existence via weakly closed feasible sets.
- [Wikipedia: Obstacle problem](https://en.wikipedia.org/wiki/Obstacle_problem) and [Variational inequality](https://en.wikipedia.org/wiki/Variational_inequality), for terminology and related models.

*Teaching connections:* `multivariable-calculus:028000` treats active inequalities and critical cones in finite dimensions; `035000`–`037000` supply weak compactness and direct-method existence; `034000` explains the finite-element approximation framework.
