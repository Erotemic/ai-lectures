# 020000 — Verified Nonlinear Systems: Interval Newton and Krawczyk Operators

**Track:** Numerical Analysis. **Background:** interval arithmetic, Jacobians, Newton's method, fixed-point theorems. **Central question:** when can computation prove that a root exists and is unique within a stated box?

<!-- BEGIN SPOKEN LECTURE -->

# A plausible root is not a proof

Suppose a nonlinear solver returns a vector and reports that the residual is extremely small. That is useful evidence, but it is not necessarily a proof that a nearby root exists. The Jacobian might be nearly singular. Rounding might have hidden an important error. There might be multiple roots in the neighborhood, or no exact root at all.

Validated numerical analysis asks a stronger question. Can we produce a box, with rigorously represented endpoints, and prove that the equation has a solution inside it? Better still, can we prove that the solution is unique in that box?

Interval Newton and Krawczyk methods provide answers when a suitable local enclosure and derivative information are available. They combine ordinary approximate computation with interval bounds and a fixed-point theorem.

## Return to Newton's idea

For a scalar equation f of x equals zero, Newton's method moves from a current guess by subtracting the function value divided by the derivative. For a system of equations, we solve a linear system involving the Jacobian matrix.

In an unverified implementation, both the function and the Jacobian are evaluated at approximate points. If those evaluations are inaccurate, the iteration can move in the wrong direction. Even if the iteration converges numerically, it might have converged to an answer without a rigorous error bound.

An interval method changes the goal. Instead of guessing where the next point is, it computes an enclosure that contains what the exact mathematics permits. A verified method uses directed rounding, so computed bounds are guaranteed to enclose the corresponding exact operations.

## Constructing the Krawczyk operator

Begin with a box X, a point m inside it, and an approximate inverse C of the Jacobian at m. We form a map T that takes x to x minus C times f of x. A zero of f is a fixed point of T, provided C is nonsingular. The derivative of T is the identity minus C times the Jacobian.

Now bound that derivative over every point of X using interval arithmetic. The mean-value theorem tells us that every value T of x lies in a particular interval expression built from m, f of m, C, and the interval Jacobian. This enclosure is the Krawczyk operator.

If the resulting enclosure fits strictly inside X, we have a compelling geometric picture: the fixed-point map sends a compact convex set into its own interior. Under the standard assumptions, this yields existence. If we also establish a contraction bound for the derivative, we obtain uniqueness of the fixed point and hence uniqueness of the root in the box.

Importantly, these are conditions to check, not properties that every Newton-like approximation automatically satisfies. A poor box or preconditioner may fail the test even though a root exists. Failure to certify is not proof of nonexistence.

## An exact one-dimensional example

Consider the equation x squared equals two. We know the positive root numerically as approximately one point four one four two. Let's prove it exists uniquely between one point four and one point five.

Choose the midpoint m equals one point four five. The derivative of x squared minus two is twice x, so on the proposed interval it lies between two point eight and three. Take C equal to one divided by two point nine, the inverse derivative at the midpoint.

The ordinary Newton correction from m is approximately one point four one four six five five. The interval derivative correction accounts for the fact that the true derivative changes across the box. In this case, the correction is small: its maximum magnitude is about one point seven two four thousandths.

Therefore the Krawczyk enclosure lies approximately between one point four one two nine three one and one point four one six three seven nine. This lies strictly inside our original interval. The derivative of the fixed-point map has absolute value no greater than one divided by twenty-nine throughout the original interval. That is less than one, so the map is a contraction. Banach's fixed-point theorem gives exactly one root in the interval.

This is stronger than saying the solver found about one point four one four. We have proved the existence and uniqueness of an exact mathematical solution in a rigorous enclosure.

## Interval Newton versus Krawczyk

The interval Newton method also uses a Jacobian enclosure, but it solves an interval linear system to bound the Newton correction. The Krawczyk method uses a chosen numerical preconditioner C, which can make computation easier and reduce sensitivity to directly inverting an interval matrix.

The two methods are closely related. Both can shrink a box, reject boxes that cannot contain a zero, and provide existence or uniqueness certificates under precise inclusion conditions. For larger systems, the quality of the preconditioner and the width of the interval Jacobian are critical.

An important difficulty is interval dependency. If a variable appears repeatedly in an expression, naive interval evaluation may treat those occurrences as though they were independent, producing an overly wide bound. Better formulations, automatic differentiation with rigorous enclosures, and box subdivision can help.

## What a certificate should contain

A verified computation should record the original equations, the interval box, the evaluation conventions, the preconditioner, and the actual inclusion or contraction inequalities. Merely labeling a solver result verified is not enough. The final inequalities must be reproducible with mathematically controlled arithmetic.

For a large nonlinear system, certification can be substantially harder than finding a candidate root. That extra work is justified when the result is to support a theorem, rule out an alternative branch, or validate a computed equilibrium in a sensitive scientific model.

The conceptual shift is from numerical plausibility to a fixed-point proof. We use floating-point computation to discover where to look, then use interval arithmetic and analytic conditions to demonstrate what is truly there.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `f:D subset R^n -> R^n` be continuously differentiable, `X subset D` a closed interval box, `m in X`, `C` a nonsingular approximate inverse Jacobian, and `J(X)` an interval matrix enclosing every exact Jacobian `Df(x)` for `x in X`. The Krawczyk enclosure is
\[
K(X)=m-Cf(m)+(I-CJ(X))(X-m).
\]
For the fixed-point map `T(x)=x-Cf(x)`, the mean-value theorem guarantees `T(X) subset K(X)` under inclusion-correct interval arithmetic. Thus `K(X) subset X` gives a self-map of a compact convex box, proving existence by Brouwer's theorem. If also `sup_{J in J(X)} ||I-CJ||<1` in a specified induced norm, Banach proves uniqueness of the fixed point in X; nonsingularity of C makes fixed points equivalent to roots of f. Standard interval-Newton/Krawczyk theorems provide further sufficient conditions, but state the actual assumptions used.

For `f(x)=x^2-2`, choose `X=[7/5,3/2]`, `m=29/20`, `C=10/29`. Then `f(m)=41/400`, `J(X)=[14/5,3]`, and
\[
I-CJ(X)=[-1/29,1/29],\qquad X-m=[-1/20,1/20].
\]
So
\[
K(X)=\left[\frac{1639}{1160},\frac{1643}{1160}\right]
\subset (7/5,3/2),
\]
and the contraction factor is at most `1/29`. The rational endpoints avoid any ambiguity about floating-point rounding; an actual implementation must use outward-rounded intervals.

### Exercises with answers

1. What does a small residual alone fail to establish? **Answer:** existence and uniqueness of a nearby exact zero without conditioning and derivative bounds.
2. What upper bound on the derivative of T is obtained in the square-root example? **Answer:** `1/29`.
3. If the Krawczyk enclosure is not contained in X, has nonexistence been proved? **Answer:** no; this sufficient test has simply failed.
4. Why must interval operations use outward rounding? **Answer:** otherwise computed endpoints may exclude exact values and invalidate the proof.

### Reading and source notes

- [Krawczyk and Neumaier, An Improved Interval Newton Operator](https://arnold-neumaier.at/scan/45.pdf), existence and uniqueness enclosures for nonlinear systems.
- [Moore, Kearfott, and Cloud, Introduction to Interval Analysis](https://doi.org/10.1137/1.9780898717716), interval Newton and validation.
- [Alefeld and Mayer, Interval Analysis: Theory and Applications](https://doi.org/10.1016/S0377-0427(00)00505-4), interval enclosures and computational techniques.
