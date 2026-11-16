# 025000 - Validated Periodic Orbits and Floquet Multipliers

**Track:** Numerical Analysis. **Background:** ordinary differential equations, interval Newton methods, Poincare maps, and linearization of dynamical systems. **Central question:** how can a numerical closed orbit become a theorem about the existence and stability of a true periodic solution?

<!-- BEGIN SPOKEN LECTURE -->

# A closed curve on a screen is not a proof

A numerical solver can draw a trajectory that seems to close upon itself. After one revolution, the simulated state is close to where it started. Such a plot is evidence for a periodic orbit, but it can be misleading. Numerical error may close a trajectory that is not actually periodic. Or an actual orbit may be unstable, with the solver tracing it only because we carefully initialized near it.

To turn a computed picture into a mathematical statement, we need a quantitative enclosure of a true orbit, not just a small plotted discrepancy. Validated numerics does this by combining an approximate orbit with rigorous bounds on the differential equation's flow and derivatives.

There are two assertions to certify. Existence asks whether some exact solution returns to its initial condition after a positive time. Stability asks what nearby solutions do after that return. The second is measured by Floquet multipliers, and proving existence alone does not determine them.

# Shooting turns an orbit into a root

For an autonomous differential equation, write the flow as a function that takes an initial state and a time duration to the evolved state. A periodic orbit is an initial point and a positive period for which the flow returns exactly to the point.

The equation that the final state equals the initial state is called the shooting equation. A numerical method can solve it approximately. But an autonomous orbit has a built-in ambiguity: shifting the initial time along the same orbit produces another solution of the shooting equation. As a result, naive Newton iteration on the shooting equation has a singular Jacobian in the direction tangent to the orbit.

We remove that ambiguity by adding a phase condition. For example, we can require the initial point to lie on a chosen transverse section. The unknowns are then the initial state and the period, and the equations include periodic return plus one phase condition. Under a suitable nondegeneracy assumption, the augmented system has an invertible derivative.

This phase condition is mathematical gauge fixing. It does not change the closed geometric orbit; it selects one representative among all choices of starting point.

# The radial normal form has an exact cycle

Consider a planar system described in polar coordinates. Let the radius grow at a rate equal to radius times one minus radius squared, and let the angle advance at one radian per unit time. At radius one, the radial derivative is zero. The angle continues to rotate uniformly. Thus the unit circle is an exact periodic orbit with period two pi.

This is a clean reference problem because its stability is also calculable. Perturb the radius slightly above or below one. Differentiate the radial equation at radius one. The derivative is negative two. Therefore a small radial perturbation is multiplied by the exponential of negative two times elapsed time, to first order.

After one complete revolution, the radial multiplier is the exponential of negative four pi. This is strictly between zero and one, so small radial errors decay geometrically from period to period. The angular direction has multiplier one because translating the starting phase along the same orbit yields another point on the orbit.

The two multipliers have completely different meanings. The unit multiplier is the unavoidable neutral tangent direction. The smaller multiplier measures attraction transverse to the orbit. This separation is what a validated Floquet calculation must reproduce.

# Variational equations compute the derivative of the return

For a general differential equation, the derivative of the flow with respect to initial conditions satisfies a matrix differential equation called the variational equation. Its coefficient matrix is the Jacobian of the vector field evaluated along the evolving trajectory.

Integrate the variational equation for one period. The resulting matrix is the monodromy matrix. Its eigenvalues are Floquet multipliers. A multiplier of magnitude greater than one implies a linearly growing direction over repeated periods. Multipliers strictly inside the unit circle indicate linear transverse decay, provided the neutral directions required by symmetries are treated correctly.

Autonomous systems always have at least one multiplier equal to one along a non-equilibrium periodic orbit. Hamiltonian systems often have additional reciprocal-pairing structure, and conservation laws can create further neutral modes. Therefore a naive test that all multipliers lie strictly inside the unit circle is not the correct stability criterion for such systems.

# Why ordinary floating point is insufficient

Suppose an approximate shooting residual is one in a billion. That is impressive, but it is not proof of a zero nearby. The derivative might be nearly singular, the flow solver might have uncontrolled accumulated error, or a hidden nonlinear term might eliminate the apparent root.

Interval arithmetic encloses every computed quantity. A validated flow integrator supplies intervals guaranteed to contain the true flow and its derivative over the period. Using those intervals, an interval Newton or Krawczyk operator can test whether a candidate box contains a unique solution of the phase-fixed shooting equations.

The decisive result is usually an inward inclusion or contraction condition on an explicitly defined box. If it succeeds, the approximate closed orbit is replaced by a theorem: there exists an exact periodic orbit whose initial data and period lie within the stated bounds.

Careful treatment of time is required. Period uncertainty changes the integration endpoint. If a Poincare return map is used instead of fixed-time shooting, the event time must be enclosed and transversality of the section verified. A numerical event detector that reports the first sign change is not by itself a certified return map.

# Certifying the Floquet spectrum

After validating the orbit, enclose the monodromy matrix using rigorous integration of the variational equation. Then use interval spectral tools or verified bounds on the characteristic polynomial to locate its eigenvalues. For low dimensions, trace and determinant bounds can be enough. For larger systems, eigenvalue separation and invariant-subspace methods may be necessary.

One must distinguish an approximate eigenvalue from a proved spectral enclosure. In nonnormal systems, small matrix errors can move eigenvalues much more than a naive residual suggests. An interval containing the monodromy entries is a first step; a rigorous eigenvalue inclusion theorem is another step.

For the radial normal form, the exact transverse multiplier is the exponential of negative four pi. An interval computation might enclose it in a narrow positive interval strictly below one. That would certify local transverse linear attraction. But it would not by itself prove a global basin of attraction for every initial condition.

# Verifying an entire branch of cycles

Now suppose the vector field depends on a parameter. Numerical continuation may draw a smooth family of closed orbits as the parameter varies. Validating one point on that family does not certify the whole branch.

A rigorous continuation algorithm uses overlapping validated boxes or segments with parameter-dependent bounds. Each step proves the existence of a nearby periodic orbit; controlled overlaps show that the pieces connect. At a fold of cycles, ordinary parameterization can fail and a pseudo-arclength or other augmented system may be needed.

Even a rigorously continued branch may not be the only branch. Completeness requires additional exclusion arguments. This is the same distinction encountered when validating equilibrium bifurcations: local correctness and global census are different claims.

# Infinite-dimensional systems add a second layer

If the original problem is a partial differential equation and we discretize it into a finite set of ordinary differential equations, validating a periodic orbit of the discretization does not yet validate a periodic solution of the PDE. One must bound the discretization or truncation remainder in a function space.

Fourier-series approaches and radii-polynomial methods can provide these infinite-dimensional tail estimates for suitable analytic or smooth equations. The computer checks a finite collection of inequalities, while the accompanying estimates control all omitted modes. This creates a genuine computer-assisted proof instead of a high-resolution simulation.

# What a reproducible certificate records

A useful verification artifact specifies the vector field, parameter box, approximate initial state and period, phase condition, interval flow bounds, derivative bounds, zero-inclusion theorem, and spectral enclosures. It also states the region where uniqueness is proved and any unresolved global alternatives.

The principle is direct. A plot suggests a periodic orbit. An exact return equation defines it. A phase condition removes a redundant degree of freedom. Interval Newton certifies the return. The variational equation and verified Floquet multipliers describe its local stability. Each step has a distinct mathematical role, and combining them yields a claim stronger than any attractive trajectory plot.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `x'=f(x)`, denote the flow by `phi_T(x_0)`. A phase-fixed shooting system in dimension n is
\[
F(x_0,T)=\big(\phi_T(x_0)-x_0,\ g(x_0)\big)=0
\]
with n+1 equations for n+1 unknowns, where g fixes a transverse section and the root is restricted to `T>0`. The flow derivative `Phi(t)=D_(x_0)phi_t(x_0)` satisfies `Phi'=Df(phi_t(x_0))Phi`, `Phi(0)=I`. Floquet multipliers are eigenvalues of `Phi(T)`; an autonomous non-equilibrium periodic orbit has a unit tangential multiplier.

For `r'=r(1-r^2)`, `theta'=1`, the unit circle has period `T=2pi`. Linearizing radial dynamics gives `delta r'=-2 delta r`, so transverse multiplier `mu_r=e^(-4pi)`; the tangential multiplier is one. A Krawczyk inclusion on the augmented shooting box with rigorously enclosed flow and Jacobian can establish a unique phase-fixed root in the box, provided the standard nonsingularity/contraction hypotheses hold. Enclosing Phi(T) does **not** automatically certify its eigenvalues without a justified spectral inclusion method.

### Exercises with answers

1. What is the neutral multiplier of a generic autonomous periodic orbit? **Answer:** one, due to phase translation.
2. What is the transverse multiplier of the radial model after half a revolution? **Answer:** `e^(-2pi)`.
3. Why add a phase condition to shooting? **Answer:** to eliminate the free time-shift direction and make the local root system nonsingular.
4. Does verifying a Galerkin periodic orbit prove a periodic orbit of the original PDE? **Answer:** not without bounds on the omitted modes and discretization error.

### Reading and source notes

- [Hungria, Lessard, and Mireles James, Radii Polynomial Rigorous Numerics for Periodic Solutions](https://doi.org/10.1090/mcom/3046), infinite-dimensional a posteriori existence proofs.
- [Recent Advances in Rigorous Computation of Poincare Maps](https://doi.org/10.1016/j.cnsns.2022.106366), validated event maps and return sections.
- [Systematic Computer-Assisted Proofs of Periodic Orbits of Hamiltonian Systems](https://doi.org/10.1016/j.cnsns.2013.12.025), interval Newton and stability verification.
