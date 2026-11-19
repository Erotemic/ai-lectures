# 007000 — Convergence and Error Certificates: Knowing When to Stop

**Track:** Numerical Analysis and Reliable Computation. **Background:** limits, simple differentiation and integration, fixed-point iteration. **Purpose:** distinguish empirical convergence from provable error bounds, and combine discretization, iteration, rounding and data errors without pretending any one estimate controls the others.

<!-- BEGIN SPOKEN LECTURE -->

# Convergence and Error Certificates: Knowing When to Stop

A numerical program often shows us a sequence of numbers becoming more and more alike. It is tempting to call this convergence and declare success. But sameness is not enough. The computer might have run out of representable numbers. Two approximations might share the same systematic bias. A discretization might have reached a plateau where rounding dominates further refinement. And a model might be accurate to many decimals while describing the wrong physical assumptions.

What we want is not merely an iteration that appears to settle down. We want a defensible claim connecting the number returned by an algorithm to a specified mathematical quantity. Sometimes that claim can be proved in advance; sometimes it requires a posteriori estimates derived from quantities evaluated along the computation.

Here we will join the pieces of numerical reliability: discretization, convergence order, residuals, and certification.

## Approximation has more than one limit

Suppose our target is the integral of x squared from zero to one. Its exact value is one third. If we approximate the area by a sum of trapezoids, the result depends on the width of the panels. Making the panels narrower improves the approximation in exact arithmetic.

This is a discretization limit. We have replaced a continuum of points by a finite set of samples. Even if every arithmetic operation were exact, a finite number of panels would generally give an approximation rather than the exact integral.

There is also an arithmetic limit. As we use more panels, we perform more operations, each potentially rounded. Eventually the gain from smaller panels may be comparable to or smaller than accumulated rounding effects. Decreasing the step size no longer guarantees a more accurate final answer in a fixed floating-point format.

Finally there may be a data limit. If the integrand is measured with uncertainty, refining the mathematical quadrature cannot resolve that uncertainty. A reliable algorithm must know which limit it is approaching and which error source will dominate first.

## A convergence experiment with a known answer

For the integral of x squared on the unit interval, the composite trapezoidal rule gives a particularly clean calculation. With n equal panels, its exact-arithmetic result is one third plus one divided by six times n squared. In other words, the approximation is too large, and its error is exactly one divided by six n squared.

At ten panels, the answer is zero point three three five. At twenty panels it is zero point three three three seven five. The error has fallen by a factor of four, just as the formula predicts when the panel width halves. This is second-order convergence in the panel width. It tells us something structural about the method, not merely that two numbers happen to be close.

Why should the error scale with the square of the panel width? The trapezoid matches the integral of a straight line exactly. For a curved function, the first uncancelled term in a Taylor expansion involves the second derivative and the square of the panel width. Under a bounded second derivative, the composite trapezoidal error is bounded by the interval length times the panel width squared times the maximum second derivative magnitude, divided by twelve.

For our quadratic example, the second derivative is exactly two, so the bound becomes one sixth of n squared. Here the usual bound is attained. In other problems it is an upper bound, not an exact prediction.

This kind of proof gives us a meaningful stopping rule: choose n so the discretization bound is below the desired allowance. The allowance should still reflect the purpose and the input uncertainty; the theorem alone does not tell us what tolerance is worth paying for.

## When a fixed-point iteration can certify itself

Consider an iterative process described by a function T. We seek a fixed point, a number x-star that is unchanged by applying T. Starting from any candidate, repeatedly apply T.

Suppose T has a global contraction property on a complete region preserved by the iteration: every pair of points is drawn closer by a factor q, where q is strictly less than one. The contraction mapping theorem then guarantees a unique fixed point in that region and convergence toward it.

The decisive point is that we can turn a computed *step* into a bound on *distance to the fixed point*. Because T shrinks distances by at most q, the distance between the true fixed point and our candidate is no more than the distance between our candidate and its next image under T, divided by one minus q. The last distance is a residual for the fixed-point equation. If the contraction factor and residual are reliably bounded, we have a posteriori error control.

For a concrete example, take T of x equal to x plus two, divided by three. This transformation has fixed point one, because substituting one returns one. Its derivative is one third, so it contracts the real line by a factor of one third. Starting from zero produces two thirds, then eight ninths, then twenty-six twenty-sevenths. At the third value, the next change is two eighty-firsts. Divide that by one minus one third, and the certified error is at most one twenty-seventh. In fact the bound is exact in this example.

Contrast that with an arbitrary iteration that merely produces small changes. Without a contraction bound or comparable theorem, the step size does not certify distance to the answer.

## Why residuals must be scaled

For a linear system, the residual is the right-hand side minus the matrix times the candidate solution. For a nonlinear equation, it is the function evaluated at the candidate. In both cases the residual can be very small in one system of units and large in another. Dividing by a meaningful scale often produces a better diagnostic.

When an inverse or lower derivative bound is available, we can convert the residual to a forward-error bound. But that conversion can be numerically difficult. Computing the inverse exactly may be as hard as the original problem. A practical numerical certificate may instead use an independently computed bound on the inverse norm, an interval enclosure, or a structural argument particular to the problem.

If the function has a nearly multiple root, the residual can be tiny relative to the location error. If a linear system is ill-conditioned, the same phenomenon occurs in multiple dimensions. 'Residual below tolerance' is meaningful only if residual is the user's intended quantity or if an error theorem connects it to one.

## A posteriori versus a priori bounds

An a priori error estimate tells us, before computing a particular approximation, how the error should behave under assumptions. For the trapezoidal rule, the second-derivative bound is a priori once the derivative's supremum is known. A contraction factor may likewise be known before iteration.

An a posteriori estimate uses actual computed information. A residual bound, a verified interval bracket, or a rigorous bound derived from successive iterates can be a posteriori. Such estimates can be sharper because they adapt to the observed calculation. But they are not magically rigorous: the residual, interval, or estimator has to be evaluated with controlled rounding and validated hypotheses.

Comparing results on grids of size h and half h is often useful as a practical convergence study. If the method truly has known leading error proportional to h squared and is in the asymptotic regime, the difference between the two approximations can estimate the remaining discretization error. Without those assumptions, the observed difference is a diagnostic, not a theorem. Roundoff, boundary layers, discontinuities, and accidental cancellation can change the apparent convergence order.

A stopping rule based only on successive values agreeing to a fixed number of decimal places can mistake a stalled iteration for convergence.

## Extrapolation can help if its model is true

If a discretization error behaves like a constant times the square of the step size, two approximations at different resolutions can be combined to cancel that leading error. For a second-order method, the combination of four times the fine-grid answer minus the coarse-grid answer, divided by three, removes the leading quadratic term in an ideal asymptotic expansion. This is an example of Richardson extrapolation.

In the quadratic trapezoidal example, the error is *exactly* a constant times the square of the panel width, so extrapolating results with ten and twenty panels gives exactly one third in rational arithmetic. This is satisfying, but it would be dangerous to treat the same cancellation as guaranteed for every integrand. The argument requires a suitable expansion, compatible grids, and sufficient numerical precision. A discontinuity or boundary singularity can change the leading power; roundoff may dominate at very fine resolution.

The distinction between estimation and certification appears again. A grid-refinement difference can guide a practical solver, while a validated bound from derivative estimates or interval arithmetic is needed for a strict enclosure. Neither mode is automatically better in every application, but they support different claims.

## Combine error sources without hiding them

Suppose the goal is to approximate a mathematical integral given exact integrand values. We might bound discretization error by a theorem, rounding error by interval arithmetic or another floating-point analysis, and any iterative subsolver error by a residual estimate. The triangle inequality then combines the bounds. None of those estimates includes physical model uncertainty unless the model and uncertainty have been explicitly represented.

A numerical result can be communicated as a center and an interval radius, a certified lower and upper bound, or a point estimate accompanied by clearly labeled diagnostic errors. Different scientific and engineering settings need different reporting conventions.

If we have measurement uncertainty of one percent, a discretization allowance of one ten-thousandth, and a verified rounding allowance of one millionth, it is misleading to report the output as physically known to six digits. It can still be beneficial to compute more accurately than the measurements permit, so that numerical uncertainty is not the limiting factor. But the report should distinguish precision of arithmetic from accuracy of the underlying information.

## When further iteration has no value

Every additional step has a cost. A sensible stopping policy weighs that cost against the remaining uncertainty and the promised guarantee. If the discretization bound dominates, spend effort refining the grid rather than iterating the linear solver to extreme precision. If input uncertainty dominates, gather better data or report a sensitivity range. If floating-point stagnation dominates, change precision or reformulate the computation. If a condition number is enormous, focus on uncertainty propagation rather than pretending a small residual solves the scientific question.

Validated computation can be ambitious: one can use directed rounding to produce intervals that contain the mathematical solution of an equation, exploit contraction mappings to certify fixed points, or use residual and inverse estimates to enclose a linear solve. Each certificate has a scope. None proves the model is the real world.

A good numerical method is not finished when it prints a number. It is finished when its stopping condition supports the claim made about that number. That is the end of an algorithm and the beginning of a trustworthy answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Composite trapezoidal rule for \(x^2\).** With \(h=1/n\),
\[
T_n=h\left[\frac{f(0)+f(1)}2 +\sum_{k=1}^{n-1}f(kh)\right]
=\frac13+\frac{1}{6n^2},\qquad \int_0^1x^2dx=\frac13.
\]
Thus \(T_{10}=0.335\), \(T_{20}=0.33375\), and \(T_n-1/3=1/(6n^2)\). For \(f\in C^2([a,b])\), the general bound is
\[
\left|\int_a^b f(x)dx-T_n(f)\right|\le \frac{(b-a)h^2}{12}\max_{x\in[a,b]}|f''(x)|.
\]

**Contraction a posteriori bound.** If \(T:X\to X\) is a contraction on a complete metric space with constant \(0\le q<1\) and unique fixed point \(x_*\), then for any \(x\in X\),
\[
d(x,x_*)\le \frac{d(x,T(x))}{1-q}.
\]
Proof: \(d(x,x_*)\le d(x,T(x))+d(T(x),T(x_*))\le d(x,T(x))+qd(x,x_*)\). Rearrange. For \(T(x)=(x+2)/3\), \(q=1/3\), \(x_3=26/27\), \(T(x_3)=80/81\), so \(|x_3-T(x_3)|=2/81\), and the certified error bound is \((2/81)/(2/3)=1/27\).

**Error-budget decomposition.** If \(q\) is an ideal mathematical target, \(q_h\) a discretized target, \(q_{h,n}\) an exact-arithmetic iterate, and \(\hat q_{h,n}\) its floating-point realization, then
\[
\|q-\hat q_{h,n}\|\le \underbrace{\|q-q_h\|}_{\text{discretization}}+\underbrace{\|q_h-q_{h,n}\|}_{\text{iteration}}+\underbrace{\|q_{h,n}-\hat q_{h,n}\|}_{\text{roundoff}}.
\]
Input and model errors require additional comparison terms. Real-world uncertainty does not become certified by this purely mathematical inequality.

**Residual-to-error bound.** If \(F(r)=0\), \(F\in C^1(I)\), \(r,\hat x\in I\), \(|F'|\ge m>0\) on \(I\), then \(|\hat x-r|\le |F(\hat x)|/m\). For a rigorous numeric interval, evaluate the residual and derivative bound with certified enclosures.

### Exercises with answers

1. **Trapezoids:** How does the exact error change when \(n\) doubles for \(f(x)=x^2\) on \([0,1]\)? **Answer:** It falls by a factor of four, since it equals \(1/(6n^2)\).
2. **Contraction:** If \(q=0.8\) and the true norm of the fixed-point residual is at most \(10^{-4}\), how far can the candidate be from the fixed point? **Answer:** At most \(10^{-4}/0.2=5\cdot10^{-4}\), assuming the contraction hypotheses hold.
3. **Discretization:** Does agreement between two grid resolutions prove convergence order? **Answer:** No; it supports a heuristic estimate only when the asymptotic error model and rounding behavior are justified.
4. **Stopping:** Why might solving an inner linear system to machine precision be pointless? **Answer:** If discretization or data uncertainty already dominates the output error, reducing iteration error further may not improve the meaningful final result.

### References

- MIT OpenCourseWare, *18.330 Introduction to Numerical Analysis* (Spring 2004 and Spring 2012), quadrature and convergence notes.
- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, chapters 1 and 4.
- Richard L. Burden and J. Douglas Faires, *Numerical Analysis*, chapters on iterative methods and numerical integration.
- James Demmel, *Applied Numerical Linear Algebra*, chapter 2 on residuals and error estimates.
