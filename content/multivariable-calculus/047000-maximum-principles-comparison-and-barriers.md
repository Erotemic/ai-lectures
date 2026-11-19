# Maximum Principles: Comparison, Positivity, and Barriers

**Track:** Multivariable Calculus from First Principles. **Focus:** signs in the Poisson equation, maximum and comparison principles, weak truncation proofs, barrier estimates, and limits of the principle.

<!-- BEGIN SPOKEN LECTURE -->

# Maximum Principles: Comparison, Positivity, and Barriers

Imagine a thin sheet held at temperature zero along its edge while a steady source deposits heat inside. We have already learned how to write a weak equation for its equilibrium temperature, how to prove that a solution exists, and under what assumptions it gains derivatives. But there is a question that none of those arguments, by itself, answers in an obvious way: can the temperature become negative somewhere inside when the source is everywhere nonnegative?

We expect not. The expectation is a mathematical theorem, but it is not simply a consequence of the solution having a small energy norm. The theorem is a comparison principle. It says that certain elliptic equations respect an ordering of data. From that one fact we can deduce positivity, uniqueness, quantitative bounds, and useful checks on numerical approximations.

The sign conventions matter. We will use the equation negative Laplacian of u equals f. If f is nonnegative and the boundary values are nonnegative, the conclusion is that u is nonnegative. That is a *minimum* principle for this sign of the equation. Harmonic functions, for which f is zero, satisfy both the maximum and minimum principles.

## The one-dimensional model

Take the unit interval. Fix u equal to zero at both ends, and impose negative u double prime equals two. Integrating twice gives u of x equal to x times one minus x. This is positive at every interior point, reaches one quarter at the midpoint, and is zero at the endpoints. The shape is concave downward because its second derivative is negative two.

That concavity is the first clue. A twice-differentiable function cannot have a strict negative interior minimum if its second derivative is negative there. For the multidimensional Laplacian we add the second derivatives in all coordinate directions. At an ordinary interior minimum the Hessian is positive semidefinite, so its trace, the Laplacian, is nonnegative. If negative Laplacian is strictly positive, that is impossible.

But this quick argument has two gaps. First, the source might be zero at a candidate minimum, so there is no strict contradiction. Second, the weak solutions we actually obtain may not have a classical Hessian at each point. The rigorous argument should accommodate both without pretending that extra derivatives are available.

## Order the boundary values and the sources

Suppose u and v solve two Poisson problems on the same bounded domain. Their source terms are f and g, and their boundary values are prescribed in the same Dirichlet sense. Assume f is at least g at every point and u is at least v along the boundary. Then u is at least v throughout the domain.

Subtract the equations. The difference w, equal to u minus v, has negative Laplacian equal to f minus g, which is nonnegative. Its boundary values are nonnegative. So all we need is this elementary principle: a function with nonnegative boundary values and nonnegative negative-Laplacian cannot drop below zero in the interior.

For a smooth function one can prove this with a tiny strictly curved perturbation. There is, however, a more flexible energy proof that works directly in the weak setting. It uses the *negative part* of w: the amount by which w falls below zero. Where w is positive, its negative part is zero. Where w is negative, its negative part equals negative w.

Because the boundary trace of w is nonnegative, this negative part has zero trace and belongs to the permitted test space. Test the weak inequality with it. On the region where w is negative, the gradient of its negative part is the negative of the gradient of w. Thus the left-hand side becomes the negative of the integral of the squared gradient of the negative part. The source ordering makes the right-hand side nonnegative. A nonpositive number must therefore be nonnegative. It can only be zero.

A zero gradient, together with zero boundary trace, means the negative part vanishes. We conclude that w is nonnegative almost everywhere. If the solution has a continuous representative, the inequality holds pointwise. Notice what this proof did *not* require: it never differentiated w twice, and it never required the source to be strictly positive.

The same argument works for negative divergence of A times the gradient, provided A is bounded and uniformly elliptic and we are dealing with a scalar equation. Symmetry is convenient for the energy formulation but not essential to this particular real-valued truncation argument; it is the positive quadratic form of A that is used. Boundary traces and the weak ordering of source functionals must still be interpreted correctly.

## Why comparison is stronger than a positivity example

The zero function solves the problem with zero source and zero boundary. Comparing a problem with nonnegative data to this zero solution gives positivity. But comparison tells us more.

For example, if two problems have identical boundary data and one source is larger, then its solution is larger. If a heat input is increased without changing the edge temperature, the equilibrium temperature cannot decrease anywhere. This is a monotonicity statement about the entire solution operator, not merely about a single solution.

Another application is uniqueness. If two solutions have the same source and the same Dirichlet boundary data, comparison gives u at least v. Exchange their roles and get v at least u. Therefore they coincide. We had already obtained uniqueness from coercivity in the energy setting. The comparison proof reveals the order structure behind that uniqueness, and it can be used in different function spaces and nonlinear settings when an appropriate comparison theorem is available.

There is an important asymmetry between sources of different sign. A positive source with zero boundary gives a nonnegative solution. If the source changes sign, no such conclusion follows. A solution can be positive in one region and negative in another. The comparison theorem remains valid, but the zero solution may no longer be a lower or upper comparison function everywhere.

## Construct a barrier instead of solving the whole PDE

Now ask a quantitative question. Suppose the boundary temperature is zero and the magnitude of f never exceeds a known number F. Can we bound the magnitude of u without actually solving the PDE?

Choose a ball of radius R containing the entire domain. Center it at some point x nought. Define a quadratic function b: take R squared minus the squared distance to x nought, multiply by F, and divide by twice the dimension. This function is nonnegative throughout the containing ball. It has a remarkably simple Laplacian: negative Laplacian of b equals F everywhere.

Because f is no larger than F, the difference b minus u has nonnegative negative-Laplacian. And because u is zero at the boundary while b is nonnegative there, comparison gives u no larger than b. Apply comparison again to b plus u, using negative f, and obtain negative b no larger than u. Put the inequalities together: the absolute value of u is at most b, hence at most F times R squared divided by twice the dimension.

For nonzero continuous Dirichlet values, add the largest absolute boundary value to this bound. The resulting estimate says that the solution cannot become arbitrarily large if both the boundary data and the forcing are uniformly bounded. It is a *supremum-norm* estimate, rather than the energy-norm estimate from Lax–Milgram.

Notice the squared radius. If we scale the domain by a factor of ten while keeping a source of the same physical magnitude, a typical Poisson solution scales by a factor of one hundred. That is consistent with the fact that the Laplacian contains two spatial derivatives. This dimensional check is valuable whenever a proposed elliptic estimate contains a power of the domain size.

The barrier need not be the true solution, or even vanish on the actual boundary. It only needs to satisfy the right differential inequality and dominate the boundary values. That freedom is exactly what makes barriers useful. A difficult domain can be enclosed inside a simple ball whose quadratic function we already understand.

For the interval with negative u double prime equal to two, choose the containing ball, in one dimension an interval, centered at one half with radius one half. The barrier based on this ball is one quarter minus the squared distance from the midpoint, which simplifies to x times one minus x. Here the comparison function happens to be the exact solution. In a complicated domain it generally will not be, but the bound survives.

## Weak and strong maximum principles are different claims

What we have established is a weak maximum or minimum principle: an inequality about the range of values. A *strong* maximum principle says more. On a connected domain, a nonconstant harmonic function cannot attain its maximum or minimum at an interior point. In particular, a nonnegative harmonic function that vanishes at one interior point must vanish identically.

The word connected is necessary: on two separate components a harmonic function can take different constants. The regularity and ellipticity hypotheses also matter. Later, the mean-value property will make the strong principle almost visual: the value at a point is an average of surrounding values, so an interior maximum can persist only if all nearby values match it.

Do not confuse this with the claim that a solution of negative Laplacian u equals a positive source cannot have an interior maximum. It often *does* have one; our parabola reaches its maximum in the middle. For that sign of the source, the prohibited event is a negative interior minimum when the boundary is nonnegative. Keeping the equation's sign in view prevents many apparently plausible but false maximum-principle statements.

## When the argument fails

Comparison relies on the form of the operator. Add an unfavorable zero-order term and it can fail. On the unit interval, the positive function sine of pi x vanishes at both endpoints and solves negative u double prime minus pi squared times u equals zero. The zero function solves the same boundary-value problem. Uniqueness and the earlier maximum principle do not hold for this operator at that parameter value. The negative coefficient multiplying u is not a harmless decoration.

Pure Neumann problems present a different issue. The differential equation does not determine an additive constant, so no bound on the absolute level of u follows from the source and normal derivative alone. We need a normalization, such as fixing the mean, and its estimates are different. For systems of coupled equations, testing a single scalar negative part is generally not enough; positivity of a matrix of coefficients is not automatically an order principle for every component.

Finally, a weak comparison theorem usually gives an almost-everywhere statement. To speak of a value at a particular point for rough-coefficient solutions, we need a suitable representative and a regularity theorem. Mathematics gains clarity when we do not slide between integral and pointwise statements.

We can now separate three tools. Energy methods show existence and control gradients. Regularity methods provide additional derivatives or continuity when hypotheses allow. Comparison methods preserve order and furnish bounds even when we have not computed a solution. Together they turn the elliptic equation from a formula into a collection of testable properties. The next natural construction will produce the solution itself as a weighted integral of its source, making positivity visible in a kernel.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Precise scalar comparison statement

Let \(\Omega\subset\mathbb R^d\) be bounded and let \(A\in L^\infty(\Omega;\mathbb R^{d\times d})\) satisfy \(\xi^T A(x)\xi\ge\lambda|\xi|^2\) a.e. with \(\lambda>0\). Suppose \(w\in H^1(\Omega)\), its negative part \(w_-\in H^1_0(\Omega)\), and
\[
\int_\Omega A\nabla w\cdot\nabla\phi\,dx\ge0\qquad\forall\phi\in H^1_0(\Omega),\ \phi\ge0.
\]
Taking \(\phi=w_-\) gives
\[
0\le\int A\nabla w\cdot\nabla w_-=-\int A\nabla w_-\cdot\nabla w_-\le-\lambda\|\nabla w_-\|_2^2.
\]
Thus \(w_-=0\). The boundary hypothesis is a nonnegative trace, not a request for classical pointwise boundary values.

### Quadratic barrier

If \(\Omega\subset B_R(x_0)\), \(-\Delta u=f\), \(u=g\) on the boundary, and \(F=\|f\|_{L^\infty(\Omega)}\), set
\[
b(x)=\frac{F}{2d}(R^2-|x-x_0|^2),\qquad-\Delta b=F.
\]
For sufficiently regular solutions and boundary traces, comparison yields
\[
\|u\|_{L^\infty(\Omega)}\le \|g\|_{L^\infty(\partial\Omega)}+\frac{R^2}{2d}\|f\|_{L^\infty(\Omega)}.
\]
The containing ball need not be centered inside \(\Omega\).

### Sign and uniqueness counterexample

With \(\Omega=(0,1)\), \(u(x)=\sin(\pi x)\) satisfies \(-u''-\pi^2u=0\), \(u(0)=u(1)=0\). The zero solution and \(u\) share all data. A maximum principle for \(-u''-\pi^2u\) cannot be asserted without extra spectral assumptions.

### Exercises and answers

1. **Source ordering.** If \(-u''=3\) and \(-v''=1\), with both functions zero at zero and one, compare them. **Answer:** \(u-v=x(1-x)\ge0\).
2. **Barrier geometry.** If a planar domain lies in a ball of radius three and \(|f|\le4\), with zero boundary values, what does the quadratic barrier give? **Answer:** \(\|u\|_\infty\le4\cdot9/(2\cdot2)=9\).
3. **Weak proof.** Why is testing with \(w_-\) legitimate when the boundary trace of \(w\) is nonnegative? **Answer:** The trace of \(w_-\) vanishes, so \(w_-\in H_0^1\).
4. **Sign check.** Which extremum is excluded by \(-\Delta u\ge0\) and nonnegative boundary data? **Answer:** A negative interior value (the weak minimum principle); an interior maximum is allowed.
5. **Neumann caution.** Why is a supremum bound based only on source and Neumann data impossible without further conditions? **Answer:** Adding an arbitrary constant leaves both unchanged.

### Sources and further reading

- [MIT OpenCourseWare, *Introduction to Partial Differential Equations*, lectures 3, 8 and 9](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2005/pages/lecture-notes/), classical and strong maximum principles.
- [Gautam Iyer, *Elliptic equations*](https://www.math.cmu.edu/~gautam/c/2026-632/notes/elliptic-equations.html), weak elliptic equations and energy estimates.
- [Wikipedia: Maximum principle](https://en.wikipedia.org/wiki/Maximum_principle), terminology and general context.
- Companion in this library: `multivariable-calculus:033000` for coercivity and `multivariable-calculus:044000` for Neumann normalization.
