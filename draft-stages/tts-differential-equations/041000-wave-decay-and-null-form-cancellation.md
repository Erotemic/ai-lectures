# Wave decay and null-form cancellation

<!-- BEGIN SPOKEN LECTURE -->

# Wave decay and null-form cancellation

## Wave Decay and the Vector-Field Method

Strike a bell, and the resulting sound spreads into the room. Far from the source, its amplitude becomes smaller. Yet for an ideal wave equation in an unbounded space, energy is conserved. How can a quantity remain constant while the disturbance seems to disappear?

The answer is geometric spreading. The energy occupies an ever-larger region, even though the total remains fixed. Conservation of energy and pointwise decay are different statements. An energy estimate controls a spatial integral of squared derivatives. It does not automatically say how large the solution can be at one location.

To turn energy into a decay estimate, we need to understand which spacetime directions are special for waves. The relevant symmetries are translations, spatial rotations, Lorentz boosts, and sometimes scaling. These produce differential operators that nearly commute, or commute exactly, with the wave operator.

Klainerman's vector-field method makes that observation systematic. It combines conservation estimates for many differentiated versions of a solution with an inequality that converts integrated control into pointwise decay.

## An outgoing spherical wave

Start with a radial solution of the three-dimensional wave equation, away from the spatial origin. If we multiply the solution by the radius, the result obeys the ordinary one-dimensional wave equation. Consequently an outgoing profile is a function of radius minus time, divided by radius.

Think of a pulse shaped like a narrow shell. As the shell travels outward, its radius grows approximately like time. Its amplitude is divided by that radius, so along the traveling shell it decays like the reciprocal of time. The pulse has not lost all its energy; the same energy is spread over a spherical area that grows quadratically with radius.

There are qualifications. The expression divided by radius has to be handled carefully at the center. It is a local form for an outgoing radial wave, not automatically a globally smooth solution for every profile. It also demonstrates decay along the outgoing shell, not a universal pointwise bound for every forcing, dimension, or geometry.

## Why commuting derivatives helps

Let the wave operator be the negative second time derivative plus the spatial Laplacian. Translations commute with it because its coefficients are constant. Rotations commute because the Laplacian is rotationally invariant. Lorentz boosts commute because the Minkowski metric is invariant under those transformations.

If u solves the homogeneous wave equation and Z is one of those commuting vector fields, then Z applied to u also solves the same equation. We can therefore apply an energy estimate not only to u but to many first, second, and higher vector-field derivatives.

The resulting collection of energies controls the behavior of the solution in directions adapted to the light cone. A weighted Sobolev inequality converts those norms into a pointwise estimate. The weights involve one plus time plus radius, and another factor measuring distance from the light cone, the region where time is close to radius.

The decay is stronger away from certain characteristic regions because waves propagate along light cones. This is not a decorative coordinate choice; the geometry of propagation enters the inequality.

## The threshold for nonlinear problems

For a linear equation, this machinery gives sharp decay estimates under smoothness and localization assumptions. For a nonlinear equation, we use those estimates inside the energy method.

Suppose the right-hand side is quadratic in first derivatives of the solution. If each derivative decays only like the reciprocal of time along a large region, the integral in time of the nonlinear error may be borderline. Even small initial data can then require a much more delicate argument for global existence.

Certain quadratic combinations have additional cancellation along null directions. These are called null forms. The vector-field method can reveal that at least one factor in such a product has improved decay in the relevant directions. That extra factor often changes a borderline time integral into a convergent one.

This is a bridge from a linear geometric fact to a nonlinear global theorem. Conservation gives initial control; commuting symmetries preserve it for differentiated fields; weighted Sobolev inequalities yield decay; structural cancellation reduces nonlinear forcing.

## What is special about dimension three

The spreading power of an expanding wave depends on spatial dimension. In three dimensions, spherical area grows like the square of radius and the outgoing radial amplitude has reciprocal-radius behavior. In lower dimensions, decay is typically weaker and long-time nonlinear behavior can be more difficult. In higher dimensions, dispersion is often stronger.

This means no theorem about global small-data solutions should be quoted without its dimension, nonlinearity, and regularity assumptions. The phrase wave decay is not one estimate valid in all settings. It is a family of conclusions that depend on how solutions propagate and how nonlinear terms interact with that propagation.

## Geometry controls analysis

The wave equation is a particularly clear example of symmetry producing an analytic tool. Its Lorentzian geometry gives a collection of vector fields. Those fields generate higher-order energies. The energies, in combination with weighted Sobolev estimates, control pointwise amplitude. The pointwise control can then close a nonlinear argument when the right-hand side has suitable structure.

The outgoing spherical pulse is the guiding picture: the wave does not disappear; it spreads. The vector-field method is how that geometric picture becomes a proof for solutions that are not radial and not explicitly solvable.

## Null Forms and Small-Data Global Waves

Consider a wave equation with a quadratic term built from first derivatives. If the initial disturbance is small, the quadratic forcing is initially much smaller still. It is tempting to conclude that the disturbance will remain small forever. But that conclusion is false in general.

Small nonlinear effects can accumulate along characteristic directions. In three spatial dimensions, the free wave decays strongly enough to help, but quadratic derivative interactions can remain borderline in time. The difference between global regularity and finite-time breakdown can depend on the algebraic form of the quadratic term.

A null form is a quadratic combination of derivatives that vanishes when its derivative arguments point along the same null direction of Minkowski spacetime. This means that waves traveling together along the same light ray interact less strongly than a generic quadratic formula would suggest.

That cancellation is the null condition. It is not simply a small coefficient. It is a geometric relation between the coefficients of the nonlinearity and the light cone of the linear wave operator.

## A form that knows the light cone

Use the Minkowski metric with a negative time component and positive spatial components. Given two functions f and g, take the negative product of their time derivatives plus the dot product of their spatial gradients. This is the standard quadratic null form called Q zero.

Suppose f and g vary along the same null plane wave. Their derivatives are proportional to the same null covector. Since the Minkowski length of that covector is zero, Q zero vanishes.

Other null forms are antisymmetric differences of products of derivatives in two coordinate directions. They vanish when the derivative covectors are parallel. In scalar equations, the antisymmetric form evaluated twice on the same function vanishes identically; in systems, cross terms involving different fields are meaningful.

The point is not that all products of derivatives disappear. They disappear along precisely the alignments that cause the worst long-time interactions in the wave equation.

## An equation that can be linearized exactly

There is an instructive nonlinear wave equation that one can solve by a change of variables. Let the wave operator be negative second time derivative plus the Laplacian. Set the wave operator of u equal to negative Q zero applied to u with itself.

Now define v as the exponential of u. The chain rule says that the wave operator of v is the exponential of u times the sum of the wave operator of u and Q zero of the derivatives of u. The two terms cancel exactly. Therefore v satisfies the free linear wave equation.

This is not a perturbative argument. It is an exact algebraic identity. If the initial data for u are smooth, small, and suitably localized, the resulting linear solution v remains close enough to one that it stays positive. We may then recover u as the logarithm of v for all times.

Notice the qualification. Arbitrary large initial data need not keep a real linear solution positive. The global change of variables is controlled here by the smallness of the corresponding linear solution. The example shows how a null-form equation can have a hidden linear structure, not that every null-condition system admits an exponential substitution.

## The general small-data argument

In a more general system, no explicit substitution removes the nonlinear term. Instead, one uses a bootstrap argument. Assume for a finite time that sufficiently many energies are bounded by a small multiple of a mild growth factor. Then commute the equation with vector fields adapted to the wave operator, derive differential inequalities for those energies, and estimate nonlinear products with weighted decay inequalities.

The null structure places a better derivative into each dangerous product. The resulting time integrals can be controlled uniformly, allowing the assumed bound to be improved. Continuation of the local solution then extends it globally.

The algebraic cancellation and the analytic estimates are both essential. If one states only that the energy is conserved, the conclusion is unsupported, because the nonlinear energy need not be conserved in the required form. If one states only that null forms vanish along a ray, the conclusion also remains unsupported, because one must quantify the effect in spacetime norms.

## Null, weak null, and other structures

The classical null condition is a sufficient structural hypothesis for broad small-data global existence theorems for three-dimensional quadratic wave systems, under the usual smoothness and compatibility assumptions. It is not a necessary condition for every particular nonlinear equation. Some systems obey weaker structural conditions and still enjoy global existence, while others exhibit blow-up for arbitrarily small data.

Dimension matters. Wave decay is weaker in two spatial dimensions, so the same quadratic term may require a different argument. Couplings to curved backgrounds, variable coefficients, or boundaries introduce additional difficulties, even when a flat-space expression resembles a null form.

The safe principle is to state the equation, dimension, coefficient conditions, and the regularity class before drawing a global conclusion.

## Algebra in the service of long-time dynamics

Null forms show how a local algebraic identity can control a global dynamical outcome. A product of derivatives is not just a product: its contraction with the Lorentzian metric determines how it behaves when wave packets move along characteristic directions.

The exponential example supplies the clearest exact calculation. In more complicated systems the same cancellation is revealed through vector-field estimates rather than through a closed-form transformation. In either case, the light cone organizes the analysis, and the coefficients of the nonlinearity decide whether waves reinforce each other or pass with sufficient cancellation.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Wave Decay and the Vector-Field Method

**Track:** Differential Equations and Dynamical Systems. **Background:** wave equations, energy estimates, integration by parts, and Lorentzian geometry. **Central question:** how can a conserved energy coexist with a solution whose amplitude decays in time?

#### Mathematical companion (not spoken)

On `\mathbb R^{1+3}` use `\Box=-\partial_t^2+\Delta_x`. For radial `u(t,r)`, `v(t,r)=ru(t,r)` satisfies
\[
(-\partial_t^2+\partial_r^2)v=0\quad(r>0).
\]
Hence `u=F(r-t)/r` is an outgoing solution wherever `r>0`, with suitable care at `r=0`. On a shell `r\sim t`, its amplitude is `O(t^{-1})` if `F` is bounded. Its energy `E(t)=\tfrac12\int_{\mathbb R^3}(|\partial_tu|^2+|\nabla_xu|^2)dx` is conserved for smooth finite-energy solutions with no forcing.

Translations `\partial_\mu`, rotations `\Omega_{ij}=x_i\partial_j-x_j\partial_i`, and boosts `L_i=t\partial_i+x_i\partial_t` commute with `\Box`. The scaling field `S=t\partial_t+x\cdot\nabla_x` obeys `[\Box,S]=2\Box`, so it maps homogeneous solutions to homogeneous solutions but is not a strict commuting symmetry.

A schematic three-dimensional Klainerman–Sobolev estimate is
\[
|\partial u(t,x)|\lesssim\frac{\sum_{|\alpha|\le 2}\|Z^\alpha\partial u(t,\cdot)\|_{L^2_x}}{(1+t+r)(1+|t-r|)^{1/2}},\quad r=|x|,
\]
with the precise derivative budget, admissible vector fields, and regularity conditions fixed by the theorem invoked. The key is the light-cone weight, not an assertion that one conserved energy alone yields this bound.

##### Exercises with answers

1. What equation does `v=ru` satisfy for a radial three-dimensional free wave? **Answer:** the one-dimensional free wave equation for `r>0`.
2. Is total energy decay implied by pointwise amplitude decay? **Answer:** No; the total energy can remain constant while spreading spatially.
3. Does the scaling field strictly commute with the wave operator? **Answer:** No; its commutator is `2\Box`.
4. Why do nonlinear null forms matter? **Answer:** they provide a favorable directional cancellation that improves time integrability.

##### Reading and source notes

- [A. Shao, Nonlinear Wave Equations: Vector Field Methods (lecture notes)](https://lpde.maths.qmul.ac.uk/a.shao/teaching/notes/dispersive_w8.pdf), light-cone decay and the vector-field approach.
- [Q. Wang, Lectures on Nonlinear Wave Equations](https://people.maths.ox.ac.uk/wangq1/Lecture_notes/nonlinear_wave_9.pdf), nonlinear wave estimates and the null condition.

### Null Forms and Small-Data Global Waves

**Track:** Differential Equations and Dynamical Systems. **Background:** nonlinear PDEs, wave decay, chain rules, and energy methods. **Central question:** which quadratic nonlinearities allow small waves to persist globally rather than accumulating destructive interactions?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Evaluate `Q_0(\xi,\xi)` for the null covector `(1,1,0,0)`. **Answer:** `-1+1=0`.
2. What is `Q_{01}(\partial u,\partial u)`? **Answer:** `0` by antisymmetry.
3. Compute `\Box(e^u)` with the given Minkowski convention. **Answer:** `e^u(\Box u+Q_0(\partial u,\partial u))`.
4. Why is the positivity of `v` needed? **Answer:** to recover a real smooth `u=\log v` globally.

##### Reading and source notes

- [A. Shao, Nonlinear Wave Equations: Vector Field Methods (lecture notes)](https://lpde.maths.qmul.ac.uk/a.shao/teaching/notes/dispersive_w8.pdf), null-form identities and global small-data mechanisms.
- [Q. Wang, Lectures on Nonlinear Wave Equations](https://people.maths.ox.ac.uk/wangq1/Lecture_notes/nonlinear_wave_9.pdf), the precise null condition and examples.
