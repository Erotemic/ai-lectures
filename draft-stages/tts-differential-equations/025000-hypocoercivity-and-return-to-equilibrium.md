# 025000 — Hypocoercivity: How Transport Creates Dissipation

**Track:** Differential Equations. **Background:** kinetic equations, Gaussian integrals, energy estimates, spectral gaps. **Central question:** how can an equation relax to equilibrium even when its direct dissipation misses whole directions?

<!-- BEGIN SPOKEN LECTURE -->

# Dissipation in one direction, motion in another

Imagine a large collection of particles moving around a circular track. Each particle has a position and a velocity. Random collisions and friction change velocities, but there is no direct diffusion in the position variable. How could the distribution become uniform in position if the dissipative mechanism acts only on velocity?

The answer is that motion couples position and velocity. A particle's velocity determines where it travels. As friction and noise alter velocities, transport carries those changes into the spatial distribution. This interaction can produce relaxation in variables that the dissipative operator does not touch directly.

Hypocoercivity is the theory that quantifies this effect. Its name points to the difficulty: the dissipative part of the operator is not coercive on the whole state space. It has a large kernel. Yet when combined with a suitable transport operator, the full dynamics can converge exponentially to equilibrium under appropriate confinement, regularity, and spectral-gap assumptions.

## A concrete kinetic model

Consider particles with position x on a periodic circle and velocity v on the real line. Their distribution f depends on x, v, and time. Free transport contributes velocity times the position derivative. Velocity friction and noise are modeled by a Fokker–Planck operator: a velocity derivative of v times f plus a velocity derivative of f.

The equilibrium distribution is uniform in x and Gaussian in v, up to the conserved total mass. Friction prevents indefinitely large velocities, noise continuously perturbs them, and transport moves particles around the circle.

To see the difficulty, divide f by the Gaussian equilibrium and call the resulting ratio h. In the natural Gaussian-weighted inner product, the transport operator is antisymmetric: it moves information around without changing the squared norm. The velocity Ornstein–Uhlenbeck operator is dissipative: its contribution to the rate of change of the squared norm is minus the squared velocity derivative of h.

So far, that is ordinary energy accounting. The problem is that h could vary with position while being independent of velocity. Its velocity derivative would be zero. Our dissipation estimate would claim no immediate decrease, even though such a spatially varying distribution is not the global equilibrium.

## A mode that initially escapes dissipation

Take h initially equal to one plus a small sine wave in position, independent of velocity. The velocity dissipator sees no variation. At time zero the dissipative contribution to the energy derivative is exactly zero. Yet transport immediately changes h by a term proportional to minus v times the cosine wave in position.

Now the solution depends on velocity. The velocity derivative, previously zero, becomes nonzero. Friction and noise can dissipate this newly created variation. Transport has transferred a spatial mode into the direction where dissipation acts.

This is the essence of hypocoercivity. The energy might not decrease at its fastest possible rate at the initial instant, but its future behavior cannot remain trapped inside the nullspace of the dissipative operator. The transport term continually exposes hidden directions to damping.

There is an algebraic way to see the transfer. The commutator of differentiation with respect to velocity and the transport operator v times differentiation with respect to position is differentiation with respect to position. By taking a commutator, we generate a derivative that the dissipative term does not contain directly.

This resembles the bracket mechanism in Hörmander's theory of hypoellipticity, but regularity and long-time decay are distinct statements. A bracket condition can explain why missing directions become accessible. Exponential relaxation still needs additional global estimates.

## Building a better energy

The naive energy only measures the size of h. The improved energy also measures derivatives with respect to position and velocity, together with a cross term coupling those derivatives. Such a cross term can be chosen so that its time derivative produces a negative multiple of the spatial-gradient norm.

Why can a cross term help? Differentiate a product of the position derivative and the velocity derivative along the flow. The commutator produces precisely the position derivative that the original dissipation estimate lacked. The new energy is constructed to borrow coercivity from the combination of transport and collision.

The cross term must be small enough that the modified energy remains equivalent to a positive norm. One cannot insert an arbitrarily large mixed product and expect a useful estimate. The coefficients are tuned so that unfavorable terms can be absorbed by the velocity dissipation and by the newly generated spatial control.

On a periodic domain, the Poincaré inequality controls mean-zero spatial modes by their spatial gradients. In velocity, the Gaussian measure supplies a spectral gap for the Ornstein–Uhlenbeck operator. Together with the commutator, these ingredients can produce an estimate saying the modified energy decays exponentially toward its equilibrium component.

## When convergence does not follow

It is tempting to generalize: any amount of friction and transport must imply exponential convergence. That is false. The domain, collision operator, conserved quantities, and boundary conditions matter. On an unbounded spatial domain, there may be no uniform spectral gap. If the collision operator has extra conserved modes, a velocity-only estimate may leave a larger kernel. If transport fails to connect those modes to dissipative directions, convergence can be much slower or fail in the proposed norm.

In more complicated kinetic equations, like linearized Boltzmann equations, the collision nullspace includes mass, momentum, and energy modes. Hypocoercivity analyzes how transport couples these macroscopic modes to the microscopic dissipative ones. The decomposition is more involved than in our Gaussian example, but the organizing idea survives.

There is also a distinction between proving that the distribution eventually approaches equilibrium and proving a quantitative rate. A qualitative entropy argument may show monotonicity, while hypocoercive estimates produce an explicit inequality in a suitable norm and identify the hypotheses under which a uniform decay rate exists.

The valuable insight is that dissipation need not act directly on every coordinate. A coupled dynamical system can move information into the dissipative directions. To analyze it, we must understand not just how each operator behaves alone, but how transport and dissipation interact through their commutators and conserved modes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `x in T`, `v in R`, and
\[
\partial_t f+v\partial_x f=\partial_v(vf+\partial_v f),\qquad
M(v)=(2\pi)^{-1/2}e^{-v^2/2}.
\]
With `h=f/M`,
\[
\partial_t h+v\partial_x h=Lh,\qquad L=\partial_{vv}-v\partial_v.
\]
In `L^2(dx M(v)dv)`, periodic transport is skew-adjoint, `L` is symmetric and dissipative, and
\[
\frac12\frac{d}{dt}\|h\|^2=-\|\partial_v h\|^2.
\]
For mean-zero `h_0=sin x`, the right side initially vanishes, although `partial_t h|_{t=0}=-v cos x`. Thus `partial_v h(t)` becomes nonzero for small t. The commutator is `[partial_v,v partial_x]=partial_x`.

A modified Sobolev energy can contain `a ||partial_x h||^2 + b ||partial_v h||^2 + 2c <partial_x h,partial_v h>`, with parameters chosen to ensure positivity and a Grönwall-type inequality after removing the conserved mass mode. The torus Poincaré inequality and Gaussian velocity spectral gap are essential; these statements do not automatically extend to arbitrary domains or collisions.

### Exercises with answers

1. What distribution is stationary in this model for fixed total mass? **Answer:** a spatially constant multiple of the Maxwellian M(v).
2. Why does `h_0=sin x` have zero instantaneous dissipation in the naive norm? **Answer:** it has no v dependence, so `partial_v h_0=0`.
3. Compute `[partial_v,v partial_x]h`. **Answer:** `partial_x h`.
4. Why is Poincaré's inequality relevant? **Answer:** it controls mean-zero spatial modes by spatial derivatives, converting generated gradient control into decay of the original fluctuation.

### Reading and source notes

- [Villani, Hypocoercivity](https://arxiv.org/abs/math/0609050), systematic hypocoercive energy constructions and applications.
- [Dolbeault, Mouhot, and Schmeiser, Hypocoercivity for Linear Kinetic Equations](https://arxiv.org/abs/1005.1495), explicit estimates for transport–collision operators.
- [Hérau, Hypocoercivity and Exponential Time Decay for the Linear Inhomogeneous Relaxation Boltzmann Equation](https://arxiv.org/abs/math/0503351), a kinetic relaxation example.
