# 036000 - Multisymplectic Variational Integrators for Wave Equations

**Track:** Differential Equations and Dynamical Systems. **Background:** Lagrangian mechanics, wave equations, numerical time stepping, and symplectic geometry. **Central question:** can a discrete wave solver preserve the geometric conservation law inherited from an action principle?

<!-- BEGIN SPOKEN LECTURE -->

# A numerical wave can obey the wrong physics

A numerical solution of a wave equation may look convincing for a few periods and then gradually drift. Its phase shifts. Its energy changes. A wave that should remain bounded may grow for no physical reason. Small truncation errors are inevitable, but their long-term organization depends strongly on the numerical method.

One response is to use smaller time steps. Another is to design the scheme around the geometry of the original differential equation. Variational integrators take the second route. Instead of discretizing the differential equation directly, we discretize the action and demand stationarity of the discrete action. For field equations, this can yield a discrete multisymplectic conservation law.

The claim is not that such a method makes all physical invariants exactly constant. Symplectic and multisymplectic structures are particular geometric quantities. They constrain how errors accumulate, but stability and accurate energy behavior still depend on the mesh, the timestep, the boundary conditions and the particular discretization.

# The wave equation comes from an action

Consider a one-dimensional vibrating field u of position and time. Its kinetic energy density is one half times the square of its time derivative. Its elastic energy density is one half times a wave-speed constant squared times the square of its spatial derivative. We may also add a potential energy density depending on u.

The Lagrangian density is kinetic energy minus elastic and potential energy. Integrate this density over a space-time region. The result is the action. A physical solution makes the action stationary under variations that vanish at the prescribed boundary.

Perform the variation and integrate by parts. The resulting Euler-Lagrange equation is the wave equation with a potential force: the second time derivative of u, minus wave speed squared times the second spatial derivative, plus the derivative of the potential, equals zero.

This derivation already links dynamics to geometry. The field equation is not just a formula we decide to approximate. It is the condition that a functional be stationary. Boundary terms from the variation carry information about momentum and symplectic structure.

# Two variations produce a conserved current

Take two small variations around a solution, call them v and w. Both satisfy the linearized wave equation, whose potential term contains the second derivative of the potential evaluated along the background solution.

Multiply the linearized equation for w by v, multiply the equation for v by w, and subtract. The potential terms cancel because they involve the same scalar coefficient. The remaining terms form a divergence: a time derivative of one antisymmetric expression minus a spatial derivative of another.

Thus there is a local conservation law for a two-form current built from pairs of variations. It is called multisymplectic because space and time both contribute boundary fluxes of symplectic type. Integrating over a space-time rectangle shows that the flux through the boundary vanishes under the appropriate orientation conventions.

This is not simply the statement that total physical energy is conserved. Energy comes from time-translation symmetry and Noether's theorem. The multisymplectic conservation law comes from the antisymmetry of the second variation of the action. Both arise from variational structure, but they are different invariants.

# Discretize the action, not merely the acceleration

Now replace the continuum by a grid of space-time cells. On each cell, approximate the action using values at its corners or edges, together with quadrature weights. Sum the cell actions. Take partial derivatives of this discrete action with respect to every interior grid value. Setting those derivatives to zero gives the discrete field equations.

Because the equations arise as stationarity conditions, the discrete first and second variations retain an exact algebraic identity. Boundary contributions from neighboring cells cancel when assembled consistently. The result is a discrete multisymplectic form formula: an oriented sum of boundary two-form contributions vanishes for variations satisfying the linearized discrete equations.

This exact identity is the geometric advantage. It does not depend on pretending the grid has no truncation error. It follows algebraically from the fact that mixed second derivatives of the discrete action commute and boundary terms are organized consistently.

# A familiar wave stencil appears

In the simplest linear case, set the potential to zero and use centered differences in space and time. The resulting equation advances the field at a grid point using its values at the two neighboring time levels and the two neighboring spatial points.

Written as an update, the next field value equals twice the current field value minus the previous one, plus a factor proportional to the wave speed squared and the time-step squared over the space-step squared, multiplying the discrete spatial second derivative.

This is the standard leapfrog or centered scheme for a linear wave equation. It also arises from a suitable discrete variational principle. The example shows that structure preservation does not necessarily require exotic formulas. A familiar stencil can have a geometric interpretation that explains some of its long-time properties.

# Stability is still a separate calculation

Take a Fourier mode on a periodic spatial grid. The centered spatial second difference multiplies that mode by a negative number proportional to the square of the sine of half the grid frequency. Each Fourier mode therefore behaves like a harmonic oscillator with a mesh-dependent frequency.

The leapfrog recurrence for that oscillator is stable when the product of the timestep and the oscillator frequency is at most two, with marginal cases needing care. The largest mesh frequency gives the familiar one-dimensional Courant condition: wave speed times timestep divided by spatial step must not exceed one.

Notice the logic. The variational construction gave a discrete geometric conservation law. Fourier analysis supplied a stability restriction. A method can be variational and still become unstable if the timestep violates that restriction. Symplecticity never replaces the Courant analysis.

# Energy oscillation versus energy explosion

Even within the stable range, the discrete scheme does not generally preserve the exact continuum Hamiltonian at every step. For a harmonic oscillator, leapfrog exactly preserves a modified quadratic invariant and a symplectic area form. The physical energy oscillates around its correct value. This is very different from a slow monotone drift that accumulates over many periods.

For a nonlinear wave, backward error analysis can sometimes explain long-time near-conservation under additional smoothness, nonresonance and step-size assumptions. But one cannot infer global error bounds for every nonlinear field equation just from the label variational.

Boundary conditions matter as well. A periodic grid permits boundary flux cancellation. At an open boundary, physical energy and multisymplectic current can flow out. The correct discrete law must include that boundary contribution rather than declaring every integral constant.

# Why more than one symplectic form?

In finite-dimensional mechanics, symplectic structure concerns time evolution of positions and momenta. A field theory has infinitely many interacting spatial points, and its action is integrated over both space and time. The multisymplectic viewpoint treats the conservation law locally in space-time rather than only after integrating over the whole spatial slice.

This supports discretizations where temporal and spatial directions are treated more symmetrically. It also clarifies why some schemes preserve a global symplectic form after spatial discretization while others directly preserve a local multi-directional flux law. The two approaches overlap but are not logically identical.

The practical design principle is to begin with the structure one wants to preserve. If a field equation is variational, one can approximate its action and derive a scheme. If a numerical method must handle dissipation, shocks, irregular meshes or moving boundaries, the discrete action and boundary terms need corresponding modifications. For strongly dissipative or entropy-producing solutions, preserving a conservative symplectic form may not be the dominant requirement.

The broader lesson is that numerical approximation should respect more than pointwise differential identities when possible. A wave equation carries an action, symmetries, boundary terms and local geometric conservation laws. A discrete method can inherit some of those relationships exactly while still approximating the wave only up to finite resolution. Understanding both statements is the basis of reliable structure-preserving simulation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a scalar field, take
\[
\mathcal L(u,u_t,u_x)=\tfrac12u_t^2-\tfrac{c^2}{2}u_x^2-V(u).
\]
The Euler-Lagrange equation is `u_tt-c^2 u_xx+V'(u)=0`. Variations v,w satisfy `v_tt-c^2 v_xx+V''(u)v=0` and the same for w. Subtracting the equations after cross multiplication yields
\[
\partial_t(v w_t-w v_t)-c^2\partial_x(v w_x-w v_x)=0.
\]
This is a local multisymplectic conservation identity. A discrete action assembled from space-time cell Lagrangians yields a discrete analogue through its second variation, subject to compatible boundary orientations and discrete Euler-Lagrange equations.

For the linear wave and centered differences,
\[
\frac{u_j^{n+1}-2u_j^n+u_j^{n-1}}{\Delta t^2}
=c^2\frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{\Delta x^2}.
\]
The spatial Fourier frequency is `omega_k=(2c/Delta x)|sin(k Delta x/2)|`; leapfrog oscillator stability `Delta t omega_k<=2` for all modes requires `c Delta t/Delta x<=1` in one dimension, with endpoint marginality handled separately. Symplectic/multisymplectic conservation does not guarantee exact conservation of continuum energy or unconditional stability.

### Exercises with answers

1. What equation follows from the stated Lagrangian when `V(u)=m^2 u^2/2`? **Answer:** `u_tt-c^2u_xx+m^2u=0`.
2. What becomes of the local multisymplectic current integrated over a periodic spatial domain? **Answer:** its net spatial flux cancels, yielding a conserved temporal two-form for linearized variations.
3. If `c=2` and `Delta x=0.1`, what is the one-dimensional linear CFL timestep limit? **Answer:** `Delta t<=0.05`.
4. Does the variational derivation make leapfrog stable for `c Delta t/Delta x=2`? **Answer:** no; the highest-frequency modes are unstable.

### Reading and source notes

- [Marsden and West, Discrete Mechanics and Variational Integrators](https://doi.org/10.1017/S096249290100006X), action-based integrators and discrete symplectic structure.
- [Bridges and Reich, Multi-Symplectic Integrators](https://www.sciencedirect.com/science/article/abs/pii/S0375960101002948), space-time geometry and multi-symplectic schemes.
- [Marsden, Patrick and Shkoller, Multisymplectic Geometry, Variational Integrators, and Nonlinear PDEs](https://arxiv.org/abs/math/9807080), field-theoretic multisymplectic conservation and discretization.
