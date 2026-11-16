# 034000 — Pattern-Forming Interfaces: Stability Beyond an Exact Front

**Track:** Differential Equations and Dynamical Systems. **Background:** reaction–diffusion equations, stationary fronts, spectra, and energy methods. **Central question:** when does an exact interface solution persist under perturbation, and how does translation symmetry change what stability means?

<!-- BEGIN SPOKEN LECTURE -->

# An exact interface can still move

Imagine a material with two preferred states. On the left it is in one state, and on the right it is in the other. Between them is a narrow transition layer. A reaction–diffusion equation can describe how such an interface evolves under diffusion and local preference for one state or the other.

A stationary interface is an exact solution that keeps the same profile over time. But exact stationarity does not answer the stability question. If we slightly perturb the profile, does it recover? Does it drift? Does it develop waves or new spatial patterns? Or does it collapse toward one uniform phase?

The Allen–Cahn equation is an ideal model for separating these questions. In one dimension, the rate of change of a scalar field equals its second spatial derivative plus the field minus its cube. The uniform states plus one and minus one are stable equilibria of the local reaction term. The state zero is unstable.

Between the two stable states, there is a smooth stationary front. Its shape is the hyperbolic tangent of x divided by the square root of two. At the far left it approaches minus one; at the far right it approaches plus one.

# Why the hyperbolic tangent appears

To find a stationary solution, set the time derivative to zero. The remaining second-order equation balances diffusion against the double-well reaction force. It resembles the equation of a particle moving in a potential if the spatial coordinate is reinterpreted as time.

Multiply the stationary equation by the spatial derivative of the profile. The terms combine into an exact derivative. Integrating once gives a first-order relationship between the slope and the double-well potential. For a front connecting minus one to plus one with vanishing derivatives at infinity, the integration constant is fixed.

The first-order equation can be separated. Its solution is the hyperbolic tangent profile. The front's width is set by the competition between diffusion and reaction. Making diffusion stronger would broaden the transition; strengthening the reaction relative to diffusion would narrow it.

This explicit formula is useful because every stability calculation can be checked against it. We know the profile, its derivative, the states at infinity, and the energy it carries.

# Energy makes the flow directional

Allen–Cahn is a gradient flow for an energy with two contributions. Spatial gradients cost energy, and values away from the two preferred phases cost potential energy. The potential has two wells, one at plus one and the other at minus one.

Differentiate the energy along a smooth decaying solution. Integration by parts produces minus the integral of the square of the time derivative. The energy cannot increase. It falls unless the system is stationary.

This does not mean every solution converges to the particular front centred at zero. The equation is invariant under spatial translation. Shifting the front left or right produces another stationary solution with exactly the same energy. There is no mechanism requiring the interface to return to the original location after a perturbation that simply moves it.

The correct stable object is the family of translated fronts, not one isolated profile.

# Linearize around the front

Write the evolving field as the exact front plus a small perturbation. Retain the terms linear in the perturbation. The resulting operator is a second spatial derivative plus one minus three times the square of the front.

Differentiate the stationary front equation with respect to position. That derivative solves the linearized equation with eigenvalue zero. The reason is symmetry: moving the front a little to the right or left costs no restoring energy. The derivative of the front is the infinitesimal translation direction.

Other perturbations need not behave that way. In this model the remaining spectrum of the linearized operator lies strictly to the left of zero. There is one additional isolated eigenvalue at negative three halves, and the essential spectrum begins at negative two and extends toward more negative values.

This is a spectral-gap statement after translation is factored out. Small perturbations transverse to the family of shifts decay. The neutral translation mode remains. Therefore a solution near the front can approach some shifted front, rather than the same front with which it began.

# Modulation tracks the drifting location

To make this precise, one may write the evolving field as a translated front plus a remainder. The translation amount becomes a time-dependent variable. We choose it so that the remainder is orthogonal to the neutral eigenfunction.

This condition removes the ambiguity in how much of the perturbation is a simple shift. Spectral estimates then control the remainder, while an evolution equation controls the translation parameter. This is called modulation.

The same idea appears in the stability theory of traveling waves, solitons, periodic patterns, and interfaces in fluids. Symmetries create neutral directions. A stability theorem must either work in a quotient by those symmetries or explicitly track their parameters.

# A front is not an isolated oscillatory pattern

A single monotone Allen–Cahn front has no internal oscillation. It is useful to distinguish it from a train of stripes, spots, or Turing patterns produced by reaction–diffusion instabilities. Those patterns may have several critical wave numbers and more than one neutral mode.

If there are two well-separated interfaces, they may interact through the exponentially small tails of their profiles. Each isolated front looks stable, but the pair can drift slowly and eventually collide. This is metastability: the system remains close to a family of patterns for a long time without being at a stable equilibrium forever.

In higher spatial dimensions, a planar interface can wrinkle. The curvature of the interface influences its motion, and transverse Fourier modes contribute additional decay or instability depending on the model. Geometry and spectral analysis must be combined.

The two-phase Allen–Cahn example provides a baseline rather than a universal answer to every pattern-forming PDE. Other reaction kinetics can make fronts unstable, create pinned interfaces, or support oscillatory modes. Stability is a property of a specified equation and a specified wave, not an adjective that follows from knowing an exact formula.

# The proof has several layers

First, construct the profile and verify the stationary equation. Second, identify a Lyapunov energy if one is available. Third, calculate the linearized operator and its spectrum, paying attention to neutral symmetry modes. Fourth, use nonlinear estimates to show that small remainders remain controlled and decay toward the translated family.

A spectral gap is suggestive but not sufficient all by itself. One must know the relevant function spaces, the regularity of the nonlinear flow, and how the nonlinear error terms compare with the linear decay. Conversely, an energy inequality may establish stability even when exact spectral calculations are unavailable.

This sequence of ideas is useful far beyond Allen–Cahn. Interfaces are central in phase transitions, combustion, biological pattern formation, and materials science. The exact front gives a reference shape. The stability analysis tells us whether the shape has predictive power under perturbation and what kinds of motion remain possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `u_t=u_xx+u-u^3`, let `V(u)=(1-u^2)^2/4` and
\[
E[u]=\int_\mathbb R\left(\tfrac12u_x^2+V(u)\right)dx,\quad
\frac{dE}{dt}=-\int_\mathbb R u_t^2\,dx
\]
for sufficiently regular solutions with appropriate spatial decay and renormalized boundary conditions. The front `U(x)=tanh(x/sqrt(2))` solves `U''+U-U^3=0`. Its energy is `E[U]=2sqrt(2)/3` among heteroclinic maps from -1 to +1 (derive using `U'=(1-U^2)/sqrt(2)`).

Linearization `u=U+v` gives `v_t=Lv+O(v^2)` with
\[
L=\partial_x^2+1-3U^2=\partial_x^2-2+3\,\mathrm{sech}^2(x/\sqrt2),\quad LU'=0.
\]
On `L^2(R)` the spectrum is `(-infinity,-2] union {-3/2,0}`. The eigenvalue zero is simple and expresses translation symmetry; stability is *orbital*, modulo translations, not convergence to a preselected location. Claims of nonlinear orbital convergence require control of the nonlinear remainder and the modulation variable. For well-separated multi-front states, exponentially weak interactions can generate metastability.

### Exercises with answers

1. Differentiate the front equation to prove `LU'=0`. **Answer:** differentiate `U''+U-U^3=0` to obtain `U'''+(1-3U^2)U'=0`.
2. Why does an initial translated front not converge to the front centred at zero? **Answer:** it is already stationary at its new centre, so translation symmetry prevents restoring motion.
3. Compute the front energy. **Answer:** `E=integral_{-1}^1 sqrt(2V(s))ds=(1/sqrt2)integral_{-1}^1(1-s^2)ds=2sqrt2/3`.
4. Does a negative spectrum apart from a zero mode prove stability for every nonlinear perturbation size? **Answer:** no; the conclusion is local and requires nonlinear estimates.

### Reading and source notes

- [On the Metastability of the 1-d Allen–Cahn Equation](https://link.springer.com/article/10.1007/s10884-020-09874-z), front energy, spectral gap, and multi-front behavior.
- [Spectral Stability of Stationary Solutions of a Boussinesq System](https://www.researchgate.net/publication/220403043_Spectral_Stability_of_Stationary_Solutions_of_a_Boussinesq_System_Describing_Long_Waves_in_Dispersive_Media), Allen–Cahn spectral model in an appendix.
- [Sander and Wanner, Validated Saddle-Node Bifurcations and Applications to Lattice Dynamical Systems](https://epubs.siam.org/doi/10.1137/16M1061011), computationally verified pattern branches and pinning phenomena.
