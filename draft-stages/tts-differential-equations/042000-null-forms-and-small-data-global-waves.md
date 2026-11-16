# 042000 — Null Forms and Small-Data Global Waves

**Track:** Differential Equations and Dynamical Systems. **Background:** nonlinear PDEs, wave decay, chain rules, and energy methods. **Central question:** which quadratic nonlinearities allow small waves to persist globally rather than accumulating destructive interactions?

<!-- BEGIN SPOKEN LECTURE -->

# Not every quadratic term has the same effect

Consider a wave equation with a quadratic term built from first derivatives. If the initial disturbance is small, the quadratic forcing is initially much smaller still. It is tempting to conclude that the disturbance will remain small forever. But that conclusion is false in general.

Small nonlinear effects can accumulate along characteristic directions. In three spatial dimensions, the free wave decays strongly enough to help, but quadratic derivative interactions can remain borderline in time. The difference between global regularity and finite-time breakdown can depend on the algebraic form of the quadratic term.

A null form is a quadratic combination of derivatives that vanishes when its derivative arguments point along the same null direction of Minkowski spacetime. This means that waves traveling together along the same light ray interact less strongly than a generic quadratic formula would suggest.

That cancellation is the null condition. It is not simply a small coefficient. It is a geometric relation between the coefficients of the nonlinearity and the light cone of the linear wave operator.

# A form that knows the light cone

Use the Minkowski metric with a negative time component and positive spatial components. Given two functions f and g, take the negative product of their time derivatives plus the dot product of their spatial gradients. This is the standard quadratic null form called Q zero.

Suppose f and g vary along the same null plane wave. Their derivatives are proportional to the same null covector. Since the Minkowski length of that covector is zero, Q zero vanishes.

Other null forms are antisymmetric differences of products of derivatives in two coordinate directions. They vanish when the derivative covectors are parallel. In scalar equations, the antisymmetric form evaluated twice on the same function vanishes identically; in systems, cross terms involving different fields are meaningful.

The point is not that all products of derivatives disappear. They disappear along precisely the alignments that cause the worst long-time interactions in the wave equation.

# An equation that can be linearized exactly

There is an instructive nonlinear wave equation that one can solve by a change of variables. Let the wave operator be negative second time derivative plus the Laplacian. Set the wave operator of u equal to negative Q zero applied to u with itself.

Now define v as the exponential of u. The chain rule says that the wave operator of v is the exponential of u times the sum of the wave operator of u and Q zero of the derivatives of u. The two terms cancel exactly. Therefore v satisfies the free linear wave equation.

This is not a perturbative argument. It is an exact algebraic identity. If the initial data for u are smooth, small, and suitably localized, the resulting linear solution v remains close enough to one that it stays positive. We may then recover u as the logarithm of v for all times.

Notice the qualification. Arbitrary large initial data need not keep a real linear solution positive. The global change of variables is controlled here by the smallness of the corresponding linear solution. The example shows how a null-form equation can have a hidden linear structure, not that every null-condition system admits an exponential substitution.

# The general small-data argument

In a more general system, no explicit substitution removes the nonlinear term. Instead, one uses a bootstrap argument. Assume for a finite time that sufficiently many energies are bounded by a small multiple of a mild growth factor. Then commute the equation with vector fields adapted to the wave operator, derive differential inequalities for those energies, and estimate nonlinear products with weighted decay inequalities.

The null structure places a better derivative into each dangerous product. The resulting time integrals can be controlled uniformly, allowing the assumed bound to be improved. Continuation of the local solution then extends it globally.

The algebraic cancellation and the analytic estimates are both essential. If one states only that the energy is conserved, the conclusion is unsupported, because the nonlinear energy need not be conserved in the required form. If one states only that null forms vanish along a ray, the conclusion also remains unsupported, because one must quantify the effect in spacetime norms.

# Null, weak null, and other structures

The classical null condition is a sufficient structural hypothesis for broad small-data global existence theorems for three-dimensional quadratic wave systems, under the usual smoothness and compatibility assumptions. It is not a necessary condition for every particular nonlinear equation. Some systems obey weaker structural conditions and still enjoy global existence, while others exhibit blow-up for arbitrarily small data.

Dimension matters. Wave decay is weaker in two spatial dimensions, so the same quadratic term may require a different argument. Couplings to curved backgrounds, variable coefficients, or boundaries introduce additional difficulties, even when a flat-space expression resembles a null form.

The safe principle is to state the equation, dimension, coefficient conditions, and the regularity class before drawing a global conclusion.

# Algebra in the service of long-time dynamics

Null forms show how a local algebraic identity can control a global dynamical outcome. A product of derivatives is not just a product: its contraction with the Lorentzian metric determines how it behaves when wave packets move along characteristic directions.

The exponential example supplies the clearest exact calculation. In more complicated systems the same cancellation is revealed through vector-field estimates rather than through a closed-form transformation. In either case, the light cone organizes the analysis, and the coefficients of the nonlinearity decide whether waves reinforce each other or pass with sufficient cancellation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `\Box=-\partial_t^2+\Delta`, and use `Q_0(\partial f,\partial g)=-\partial_tf\partial_tg+\nabla f\cdot\nabla g`, plus antisymmetric null forms `Q_{\alpha\beta}(\partial f,\partial g)=\partial_\alpha f\partial_\beta g-\partial_\beta f\partial_\alpha g`. A quadratic form `a^{\mu\nu}\partial_\mu u\partial_\nu u` satisfies the classical null condition if `a^{\mu\nu}\xi_\mu\xi_\nu=0` for every Minkowski-null covector `\xi` (`-\xi_0^2+\sum_i\xi_i^2=0`).

For the special scalar equation
\[
\Box u=-Q_0(\partial u,\partial u),\qquad v=e^u,
\]
the chain rule gives
\[
\Box v=e^u(\Box u+Q_0(\partial u,\partial u))=0.
\]
If smooth, appropriately decaying small data produce a free solution `v` with `\inf_{t,x}v>0`, then `u=\log v` is a global smooth solution. For compactly supported sufficiently small data around `u=0`, the free solution `v=1+w` admits a global small uniform bound on `w` in `3+1` dimensions, so `v>0`.

In general, commuting with Minkowski vector fields and using Klainerman–Sobolev estimates is required. The classical null condition yields improved decay of `Q` along outgoing null directions; the full global existence theorem assumes suitable dimension, regularity, and smallness. No claim is made for arbitrary quadratic forms or arbitrary dimensions.

### Exercises with answers

1. Evaluate `Q_0(\xi,\xi)` for the null covector `(1,1,0,0)`. **Answer:** `-1+1=0`.
2. What is `Q_{01}(\partial u,\partial u)`? **Answer:** `0` by antisymmetry.
3. Compute `\Box(e^u)` with the given Minkowski convention. **Answer:** `e^u(\Box u+Q_0(\partial u,\partial u))`.
4. Why is the positivity of `v` needed? **Answer:** to recover a real smooth `u=\log v` globally.

### Reading and source notes

- [A. Shao, Nonlinear Wave Equations: Vector Field Methods (lecture notes)](https://lpde.maths.qmul.ac.uk/a.shao/teaching/notes/dispersive_w8.pdf), null-form identities and global small-data mechanisms.
- [Q. Wang, Lectures on Nonlinear Wave Equations](https://people.maths.ox.ac.uk/wangq1/Lecture_notes/nonlinear_wave_9.pdf), the precise null condition and examples.
