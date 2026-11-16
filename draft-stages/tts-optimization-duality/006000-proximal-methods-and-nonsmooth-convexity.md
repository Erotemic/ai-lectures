# 006000 — Proximal Methods: Optimization When the Best Point Has a Corner

**Track:** Optimization, Convexity, and Duality. **Background:** convexity, gradients, smoothness, and first-order methods. **Question:** how can we optimize a function whose gradient does not exist at important candidate solutions?

<!-- BEGIN SPOKEN LECTURE -->

# Proximal Methods: Optimization When the Best Point Has a Corner

Gradient descent works by following derivative information. But many useful objectives contain sharp corners: absolute values, maximums, constraints, and penalties intended to force exact zeros. At those corners, the ordinary derivative may not exist. In fact the optimum may lie at exactly such a point.

It would be a mistake to smooth away every corner just to make our favorite algorithm applicable. Convex analysis gives a better tool: the proximal operator. It solves a small optimization problem that respects the nonsmooth part of the objective, while the smooth part can still be handled by a gradient step.

## The simplest corner

Consider the absolute-value function. It decreases with slope negative one on the negative axis and increases with slope positive one on the positive axis. Its minimum is at zero, where there is no single derivative. If we insisted that a minimum must have derivative equal to zero, we would miss its obvious minimizer.

The convex replacement for a derivative at a point is the subdifferential: the set of slopes that define supporting lines lying below the graph. At a positive point, the absolute value has the single subgradient one. At a negative point, it has the single subgradient negative one. At zero, every slope from negative one through one is valid, because the line with any of those slopes stays below absolute x.

For a proper convex function, zero belonging to its subdifferential is equivalent to global optimality. The statement is not a local heuristic. If zero is a subgradient at x-star, the defining inequality says the function at every other point is at least the function at x-star.

## Add an attraction toward a target

Suppose we want an estimate x near the observation three but also want to penalize the magnitude of x. Consider the objective one-half times x minus three squared plus lambda times absolute x, where lambda is positive. The quadratic prefers x equals three. The absolute-value penalty prefers x equals zero. The optimum balances them.

For x greater than zero, the derivative is x minus three plus lambda. Setting it to zero yields x equals three minus lambda, valid in that positive region only when lambda is less than three. For x less than zero, the derivative is x minus three minus lambda, whose zero lies above three and therefore cannot belong to the negative region. At zero, the subgradient interval for the total objective runs from negative three minus lambda to negative three plus lambda. It contains zero exactly when lambda is at least three.

Thus the minimizer is three minus lambda when lambda is below three, and zero when lambda is at least three. Notice the exact zero. A nonsmooth penalty can create sparse solutions rather than merely shrinking coefficients toward zero.

This simple calculation is the prototype of soft thresholding.

## The proximal operator

Given a convex function g and a positive step size t, the proximal operator takes a point z and returns the minimizer of g of y plus one over two t times the squared distance between y and z. In words, we seek a point where g is small, but charge a quadratic cost for moving away from z.

When g is the absolute value multiplied by lambda, we just solved this problem in a slightly different form. For a positive z, the result is the larger of z minus t lambda and zero. For a negative z, the result is the smaller of z plus t lambda and zero. Put both cases together: preserve the sign of z and reduce its magnitude by t lambda, clipping to zero when the magnitude was too small. That operation is soft thresholding.

The proximal map does not mean taking a gradient of g. It handles g's corner exactly. Its definition is itself an optimization problem, but for many structured penalties that problem has a closed-form solution or can be computed more easily than the original objective.

## From gradient descent to proximal gradient

Now consider an objective F equal to f plus g, where f is differentiable and convex with Lipschitz-continuous gradient, and g is proper, closed, and convex but may be nonsmooth. The smoothness constant L means the gradient of f cannot change faster than L times the distance moved.

Ordinary gradient descent would take x minus t times the gradient of f. Proximal gradient takes that proposed point and applies the proximal map of t times g. In symbols spoken aloud: move according to the gradient of f, then take the point that best balances the g penalty against the cost of deviating from that move.

This update is not an arbitrary two-stage compromise. It minimizes a local model consisting of f at the current point, the linear approximation from its gradient, a quadratic movement penalty, and the exact nonsmooth term g. If t is at most one over L, the smoothness inequality ensures that this local quadratic model is an upper bound on the real objective, up to its constant at the current point. The method therefore gives a descent guarantee under those assumptions.

At a fixed point of this update, the optimality condition for the proximal step becomes zero belonging to the gradient of f plus the subdifferential of g. That is precisely the first-order optimality condition for minimizing the convex sum F. We have recovered a generalization of the familiar condition gradient equals zero, one that remains valid at corners.

## Constraints as an extreme penalty

There is another important proximal operator. Let C be a closed convex feasible set. Define a function that is zero inside C and positive infinity outside C. Adding it to an objective forces the minimizer to remain feasible. Its proximal map is the nearest-point projection onto C, because the infinity penalty rules out all points outside C and leaves only the squared-distance term to minimize.

Thus projected gradient descent is a special case of proximal gradient: take a gradient step for the objective, then project onto the constraint set. For example, projection onto the nonnegative real line replaces a negative proposed value by zero and leaves a nonnegative value unchanged. For the Euclidean ball, it keeps points inside the ball and rescales points outside back to the boundary.

This unifies algorithms that otherwise might look unrelated. Soft thresholding enforces an absolute-value penalty; projection enforces a hard constraint. In both cases the same operator balances the proposed move against a convex structure we do not want to differentiate away.

## What a convergence claim actually needs

Proximal methods rely on assumptions. A closed convex penalty ensures the proximal minimizer exists and is unique when the quadratic term makes the subproblem strongly convex. A step-size bound must be related to the smooth part's Lipschitz gradient. Under standard convex assumptions, proximal gradient converges in objective value toward the infimum, and standard analyses provide rates such as order one over the iteration count in objective gap. Stronger geometric or strong-convexity hypotheses support stronger claims.

A small step between iterations is not by itself a certificate of a small objective gap. Nor is an arbitrary nonconvex penalty guaranteed to have the same optimality or convergence theory. The algorithm can still be used in other settings, but the proof obligations change.

The practical importance of proximal methods is that they preserve meaningful nonsmooth structure. Corners often represent exact decisions—setting a coefficient to zero, touching a constraint boundary, choosing among active regimes. Instead of hiding those decisions behind a differentiable approximation, convex analysis lets the optimization method work with them directly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a proper convex \(g\),
\[
\partial g(x)=\{v:g(y)\ge g(x)+\langle v,y-x\rangle\ \forall y\},
\]
\[
\operatorname{prox}_{tg}(z)=\arg\min_y\left(g(y)+\frac1{2t}\|y-z\|^2\right).
\]

For \(g(x)=\lambda|x|\) on \(\mathbb R\):
\[
\operatorname{prox}_{t\lambda|\cdot|}(z)
=\operatorname{sign}(z)\max(|z|-t\lambda,0).
\]
For \(z=3\), \(t=1\), the proximal solution is \(\max(3-\lambda,0)\).

For \(F=f+g\) with \(f\) convex, differentiable, and \(L\)-smooth, \(g\) proper closed convex,
\[
x_{k+1}=\operatorname{prox}_{tg}(x_k-t\nabla f(x_k)),\quad 0<t\le 1/L.
\]
The descent inequality derived by comparison with the current iterate is
\[
F(x_{k+1})\le F(x_k)-\left(\frac1{2t}-\frac L2\right)\|x_{k+1}-x_k\|^2.
\]
A sharper estimate can follow from the optimality condition; the displayed conservative bound is sufficient for descent when \(t\le1/L\).

For an indicator \(\iota_C\) of a nonempty closed convex set \(C\), \(\operatorname{prox}_{t\iota_C}(z)=\Pi_C(z)\), the Euclidean projection.

### Exercises with answers

1. Compute \(\operatorname{prox}_{|\cdot|}(2)\). **Answer:** one.
2. Compute \(\operatorname{prox}_{|\cdot|}(0.5)\). **Answer:** zero.
3. Why is \(0\in\partial|x|\) true at \(x=0\)? **Answer:** the supporting slope zero lies in \([-1,1]\).
4. What is the proximal map of the indicator of \([0,\infty)\)? **Answer:** \(z\mapsto\max(z,0)\).

### Reading

Boyd and Vandenberghe, *Convex Optimization*, subgradients and constrained optimization; Stanford EE364A course materials on proximal and first-order methods; Parikh and Boyd, *Proximal Algorithms*, Foundations and Trends in Optimization (2014).
