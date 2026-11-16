# 041000 — Wave Decay and the Vector-Field Method

**Track:** Differential Equations and Dynamical Systems. **Background:** wave equations, energy estimates, integration by parts, and Lorentzian geometry. **Central question:** how can a conserved energy coexist with a solution whose amplitude decays in time?

<!-- BEGIN SPOKEN LECTURE -->

# A conserved quantity and a fading wave

Strike a bell, and the resulting sound spreads into the room. Far from the source, its amplitude becomes smaller. Yet for an ideal wave equation in an unbounded space, energy is conserved. How can a quantity remain constant while the disturbance seems to disappear?

The answer is geometric spreading. The energy occupies an ever-larger region, even though the total remains fixed. Conservation of energy and pointwise decay are different statements. An energy estimate controls a spatial integral of squared derivatives. It does not automatically say how large the solution can be at one location.

To turn energy into a decay estimate, we need to understand which spacetime directions are special for waves. The relevant symmetries are translations, spatial rotations, Lorentz boosts, and sometimes scaling. These produce differential operators that nearly commute, or commute exactly, with the wave operator.

Klainerman's vector-field method makes that observation systematic. It combines conservation estimates for many differentiated versions of a solution with an inequality that converts integrated control into pointwise decay.

# An outgoing spherical wave

Start with a radial solution of the three-dimensional wave equation, away from the spatial origin. If we multiply the solution by the radius, the result obeys the ordinary one-dimensional wave equation. Consequently an outgoing profile is a function of radius minus time, divided by radius.

Think of a pulse shaped like a narrow shell. As the shell travels outward, its radius grows approximately like time. Its amplitude is divided by that radius, so along the traveling shell it decays like the reciprocal of time. The pulse has not lost all its energy; the same energy is spread over a spherical area that grows quadratically with radius.

There are qualifications. The expression divided by radius has to be handled carefully at the center. It is a local form for an outgoing radial wave, not automatically a globally smooth solution for every profile. It also demonstrates decay along the outgoing shell, not a universal pointwise bound for every forcing, dimension, or geometry.

# Why commuting derivatives helps

Let the wave operator be the negative second time derivative plus the spatial Laplacian. Translations commute with it because its coefficients are constant. Rotations commute because the Laplacian is rotationally invariant. Lorentz boosts commute because the Minkowski metric is invariant under those transformations.

If u solves the homogeneous wave equation and Z is one of those commuting vector fields, then Z applied to u also solves the same equation. We can therefore apply an energy estimate not only to u but to many first, second, and higher vector-field derivatives.

The resulting collection of energies controls the behavior of the solution in directions adapted to the light cone. A weighted Sobolev inequality converts those norms into a pointwise estimate. The weights involve one plus time plus radius, and another factor measuring distance from the light cone, the region where time is close to radius.

The decay is stronger away from certain characteristic regions because waves propagate along light cones. This is not a decorative coordinate choice; the geometry of propagation enters the inequality.

# The threshold for nonlinear problems

For a linear equation, this machinery gives sharp decay estimates under smoothness and localization assumptions. For a nonlinear equation, we use those estimates inside the energy method.

Suppose the right-hand side is quadratic in first derivatives of the solution. If each derivative decays only like the reciprocal of time along a large region, the integral in time of the nonlinear error may be borderline. Even small initial data can then require a much more delicate argument for global existence.

Certain quadratic combinations have additional cancellation along null directions. These are called null forms. The vector-field method can reveal that at least one factor in such a product has improved decay in the relevant directions. That extra factor often changes a borderline time integral into a convergent one.

This is a bridge from a linear geometric fact to a nonlinear global theorem. Conservation gives initial control; commuting symmetries preserve it for differentiated fields; weighted Sobolev inequalities yield decay; structural cancellation reduces nonlinear forcing.

# What is special about dimension three

The spreading power of an expanding wave depends on spatial dimension. In three dimensions, spherical area grows like the square of radius and the outgoing radial amplitude has reciprocal-radius behavior. In lower dimensions, decay is typically weaker and long-time nonlinear behavior can be more difficult. In higher dimensions, dispersion is often stronger.

This means no theorem about global small-data solutions should be quoted without its dimension, nonlinearity, and regularity assumptions. The phrase wave decay is not one estimate valid in all settings. It is a family of conclusions that depend on how solutions propagate and how nonlinear terms interact with that propagation.

# Geometry controls analysis

The wave equation is a particularly clear example of symmetry producing an analytic tool. Its Lorentzian geometry gives a collection of vector fields. Those fields generate higher-order energies. The energies, in combination with weighted Sobolev estimates, control pointwise amplitude. The pointwise control can then close a nonlinear argument when the right-hand side has suitable structure.

The outgoing spherical pulse is the guiding picture: the wave does not disappear; it spreads. The vector-field method is how that geometric picture becomes a proof for solutions that are not radial and not explicitly solvable.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What equation does `v=ru` satisfy for a radial three-dimensional free wave? **Answer:** the one-dimensional free wave equation for `r>0`.
2. Is total energy decay implied by pointwise amplitude decay? **Answer:** No; the total energy can remain constant while spreading spatially.
3. Does the scaling field strictly commute with the wave operator? **Answer:** No; its commutator is `2\Box`.
4. Why do nonlinear null forms matter? **Answer:** they provide a favorable directional cancellation that improves time integrability.

### Reading and source notes

- [A. Shao, Nonlinear Wave Equations: Vector Field Methods (lecture notes)](https://lpde.maths.qmul.ac.uk/a.shao/teaching/notes/dispersive_w8.pdf), light-cone decay and the vector-field approach.
- [Q. Wang, Lectures on Nonlinear Wave Equations](https://people.maths.ox.ac.uk/wangq1/Lecture_notes/nonlinear_wave_9.pdf), nonlinear wave estimates and the null condition.
