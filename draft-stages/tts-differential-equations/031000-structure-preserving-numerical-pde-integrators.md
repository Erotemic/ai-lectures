# 031000 — Structure-Preserving PDE Integrators: Discretizing Without Losing Geometry

**Track:** Differential Equations and Dynamical Systems. **Background:** wave equations, semidiscrete systems, Hamiltonian mechanics, and numerical time integration. **Central question:** when can a discrete evolution reproduce the conservation laws and geometry of a PDE?

<!-- BEGIN SPOKEN LECTURE -->

# A stable answer can still be physically wrong

Suppose we simulate a vibrating string for many thousands of oscillations. The numerical solution does not explode, and the time step is small. Yet the amplitude slowly grows or fades, and the oscillation phase drifts until the animation tells a different story from the physical string.

A small local truncation error does not guarantee that the right qualitative behavior survives over long times. A numerical integrator may approximate each short step well and still corrupt conservation laws, symmetries, or the geometry of the underlying flow.

Structure-preserving integration begins by identifying what the equation preserves and constructing the discrete method to respect an appropriate analogue. That structure might be a symplectic form, a quadratic energy, a mass integral, a momentum map, or a discrete multisymplectic conservation law. There is no universal method that exactly preserves all of them for every nonlinear equation. The task is to choose the right structure for the problem.

# Turning the wave equation into oscillators

Take the one-dimensional wave equation on a periodic interval, with unit wave speed for simplicity. Its second time derivative equals its second spatial derivative. The continuous energy is the integral of one half the squared velocity plus one half the squared spatial gradient. Differentiate it in time, integrate the spatial derivative by parts, and periodicity cancels the boundary terms. The energy is constant.

Now discretize space first, leaving time continuous. Let q be the vector of grid displacements and p the vector of momenta. A symmetric stiffness matrix records the coupling between neighboring grid values. The semidiscrete system has the form that the time derivative of q equals an inverse mass matrix times p, while the time derivative of p equals minus the stiffness matrix times q.

This is a finite-dimensional Hamiltonian system. Its energy is a quadratic form: kinetic energy in p plus potential energy in q. Eigenvectors of the stiffness operator provide independent oscillatory modes. A numerical time method must act on those modes without introducing artificial amplification or damping if it claims to conserve the semidiscrete energy.

# The midpoint rule and an exact algebraic identity

The implicit midpoint method evaluates the vector field at the average of the old and new states. For a linear Hamiltonian system with constant mass and stiffness matrices, it has a remarkable property: it preserves the quadratic Hamiltonian exactly in exact arithmetic.

Here is the calculation without hiding it behind a theorem. The difference of two squares equals the difference times the sum. Apply that identity to the kinetic term and the potential term. The change of kinetic energy is the average momentum paired with the momentum increment. The change of potential energy is the average displacement paired with the displacement increment, weighted by the stiffness matrix.

The midpoint update says the displacement increment is the time step times the inverse mass matrix applied to the average momentum. It also says the momentum increment is minus the time step times stiffness applied to the average displacement. Substitute both. The two energy changes cancel exactly.

This is not merely saying the method has small energy error. For the linear semidiscrete wave equation with the stated matrices and boundary treatment, the discrete energy after each step equals the energy before it, apart from floating-point solution error.

# What is preserved for nonlinear Hamiltonians?

A common misunderstanding is that implicit midpoint preserves the exact energy of every nonlinear Hamiltonian system. It does not. It is symplectic, which means it preserves the canonical symplectic two-form for Hamiltonian ODEs under the standard conditions. For quadratic Hamiltonians, symplecticity and midpoint's algebra also give exact energy conservation. For a general nonlinear Hamiltonian, exact energy is not guaranteed by symplecticity alone.

Why use a symplectic method if the original energy can vary slightly? Backward-error analysis often shows that, under smoothness, small step size, and suitable nonresonance assumptions, the numerical trajectory follows the flow of a nearby modified Hamiltonian over long intervals. Its energy error can remain bounded and oscillatory rather than systematically drifting. The quantitative time scale depends on the equation and the theorem's hypotheses.

This is a geometric rather than pointwise guarantee. It helps explain why symplectic integrators are valuable for long-duration Hamiltonian simulations even when their per-step accuracy is no better than that of a non-symplectic method of the same order.

# The explicit alternative: Störmer–Verlet

The leapfrog or Störmer–Verlet method is popular for wave equations because it separates updates of positions and momenta into simple half- and full-steps. For separable Hamiltonians it is symplectic and time-reversible. It does not require solving an implicit nonlinear system at each time step.

But it is conditionally stable. Consider one harmonic oscillator with frequency omega. The discrete recurrence has bounded oscillations only when the product of omega and the time step is less than two, with the boundary case requiring separate care. For a spatially discretized wave equation, the highest resolved frequency grows as the grid is refined, creating a Courant-type time-step restriction.

The implicit midpoint method avoids this particular linear stability restriction on purely imaginary eigenvalues, but its phases are still distorted: a discrete oscillation angle is related to the true angle by an arctangent. Energy conservation alone does not imply exact phase accuracy.

# What about multisymplectic PDEs?

Space and time can sometimes be treated more symmetrically. For suitable first-order Hamiltonian PDEs, one can write an equation involving skew-symmetric matrices multiplying space and time derivatives of a state vector. Solutions satisfy a local multisymplectic conservation law, not just a global energy balance.

Multisymplectic integrators attempt to preserve a discrete counterpart of that local law. This approach is useful for wave propagation and nonlinear field equations where a time-only Hamiltonian formulation hides some of the geometric structure.

Yet a discretization may preserve a discrete multisymplectic form and still have numerical dispersion or parasitic oscillation modes. Structure preservation needs to be combined with consistency, stability and resolution analysis. No preserved two-form compensates for a grid too coarse to resolve the physics of interest.

# Conservation claims must name the boundary

A periodic string and a string with fixed endpoints conserve energy when the boundary does no work. A string driven at one endpoint generally does not have constant interior energy, because energy flows through the boundary. A method that forces constant interior energy in that setting would be wrong.

The same is true for PDE systems with damping, forcing or shocks. A correct discrete method may need to preserve a balance law with fluxes and dissipation rather than an invariant. For compressible fluids, exact energy balance can coexist with entropy production at shocks. Preserving the wrong invariant is not a sign of quality.

There are also numerical qualifications. An implicit update solved only approximately may violate exact conservation by the nonlinear or linear solver residual. Floating-point arithmetic introduces small deviations. A theorem about the algebraic method in exact arithmetic must not be advertised as a computer-verified equality unless those implementation effects are bounded.

# Designing for the invariant rather than discovering drift later

Structure-preserving methods are not a promise of perfect simulation. They are a design strategy: identify the geometric or physical law, derive its discrete analogue, prove the method respects that analogue under explicit assumptions, and separately check stability, consistency, resolution, and solver error.

For the semidiscrete linear wave equation, implicit midpoint offers a clean example. The energy is quadratic, the midpoint identity makes the energy changes cancel, and the proof works for every step size in exact arithmetic. For nonlinear dynamics the story becomes subtler, and symplecticity is often the more robust long-time principle. Preserving the right structure can make a numerical model much more faithful than a method selected only for low short-time truncation error.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `M=M^T>0`, `K=K^T>=0` and the semidiscrete wave equation be `qdot=M^{-1}p`, `pdot=-Kq`. Define
\[
H(q,p)=\tfrac12p^TM^{-1}p+\tfrac12q^TKq.
\]
The implicit midpoint equations, with `bar q=(q_{n+1}+q_n)/2` and similarly `bar p`, are
\[
q_{n+1}-q_n=hM^{-1}\bar p,\qquad p_{n+1}-p_n=-hK\bar q.
\]
Using difference-of-squares,
\[
H_{n+1}-H_n=\bar p^TM^{-1}(p_{n+1}-p_n)+\bar q^TK(q_{n+1}-q_n)=0.
\]
This is exact for linear constant-coefficient semidiscrete systems and exact solves. For general nonlinear Hamiltonians, midpoint is symplectic but not necessarily energy preserving.

For the oscillator `q''+omega^2 q=0`, Störmer–Verlet yields `q_{n+1}-2q_n+q_{n-1}=-(h omega)^2 q_n`. The roots lie on the unit circle for `0<h omega<2`. At `h omega=2` there is a repeated root -1 with possible linear growth for general initial data; do not claim unconditional boundedness at equality. The implicit midpoint rotation satisfies `theta=2 arctan(h omega/2)`, displaying phase error despite exact quadratic energy.

### Exercises with answers

1. What assumption permits the midpoint energy cancellation? **Answer:** a constant quadratic Hamiltonian with symmetric mass and stiffness matrices, using an exact implicit solve.
2. Is a symplectic method necessarily exactly energy-preserving for a nonlinear potential? **Answer:** no.
3. What is the open stability interval for Verlet on a single harmonic oscillator? **Answer:** `0<h omega<2`.
4. Can energy flow through a driven boundary? **Answer:** yes; the correct PDE law is an energy balance with boundary flux.

### Reading and source notes

- [Hairer, Lubich and Wanner, Geometric Numerical Integration](https://link.springer.com/book/10.1007/3-540-30666-8), symplectic methods and backward-error analysis.
- [Frank, Moore and Reich, Linear PDEs and Numerical Methods That Preserve a Multisymplectic Conservation Law](https://doi.org/10.1137/050628271), multisymplectic methods and numerical dispersion.
- [Marsden, Patrick and Shkoller, Multisymplectic Geometry, Variational Integrators and Nonlinear PDEs](https://arxiv.org/abs/math/9807080), variational PDE discretization.
