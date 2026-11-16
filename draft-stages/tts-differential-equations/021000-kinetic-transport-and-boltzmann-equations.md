# 021000 — Kinetic Transport: From Particle Distributions to Fluid Equations

**Track:** Differential Equations and Dynamical Systems. **Background:** transport PDEs, conservation laws, integral equations, statistical mechanics basics. **Central question:** how can equations for the distribution of particles produce macroscopic conservation laws?

<!-- BEGIN SPOKEN LECTURE -->

# Kinetic Transport and Boltzmann-Type Equations

Imagine a gas filling a room. We could try to follow every molecule, recording its location and velocity as it collides with others. Even a small visible amount of gas contains vastly more particles than we can track individually. A different description asks how many particles occupy a small region of position-and-velocity space, rather than which named particle is there.

The resulting function is a kinetic distribution. It depends on time, position, and velocity. In three spatial dimensions, that is seven variables before we include any internal particle properties. A fluid model depends primarily on time and position, so the kinetic description may appear more complicated. Its advantage is that it remembers the velocity distribution out of which density, momentum, and temperature emerge.

## Free transport first

Begin with particles that do not collide and feel no external forces. Each particle moves at its current velocity. If a particle was at position x minus v times t at time zero, it is at x at time t. Therefore the distribution at the later time is the initial distribution evaluated at that earlier position, with the same velocity.

This is the solution of the free transport equation. Along each straight trajectory in phase space, the distribution remains constant. It is a higher-dimensional version of the method of characteristics used for first-order partial differential equations.

There is a useful distinction between individual trajectories and observed density. A localized packet with many different velocities spreads across physical space, even though each phase-space trajectory is perfectly reversible and no collisions occur. An observer who measures only position sees dispersion. That spreading should not automatically be identified with heat diffusion; the underlying equation is reversible transport, not a dissipative heat equation.

## Add forces and collisions

If an external force acts, the velocity itself changes along a characteristic. The transport equation acquires a term describing how the distribution moves through velocity space. In classical kinetic theory one then adds a collision operator, traditionally denoted Q, to account for particles scattering from one velocity to another.

The Boltzmann equation is a particularly important example. Its collision operator involves an integral over pairs of velocities and collision angles. It removes particles from some velocities and adds them at others according to the collision dynamics. A physical collision model requires assumptions about binary encounters, the cross section, and the statistical independence used in the molecular-chaos approximation.

We should not confuse this model with an exact deterministic law for all interacting particles. The Boltzmann equation is a kinetic approximation whose validity depends on a regime such as a dilute gas and a suitable limiting description.

## Moments create macroscopic variables

The simplest macroscopic variable is density: integrate the distribution over all velocities. Next is momentum density: integrate velocity multiplied by the distribution. Then kinetic energy: integrate the squared speed times one half the distribution.

Why these particular moments? Elastic collisions conserve particle number, total momentum, and total kinetic energy. The Boltzmann collision operator is designed so that its integrals against the corresponding test functions vanish. These are called collision invariants.

Integrate the Boltzmann equation over velocity. The collision term disappears by number conservation, and the transport term becomes the spatial divergence of momentum density. We obtain the continuity equation: the rate of change of density equals the negative divergence of particle flux. That conservation law does not require us to have solved the distribution function explicitly.

Multiply instead by velocity before integrating. We obtain the momentum balance equation. Now a second-order velocity moment appears: a tensor describing flux of momentum, often split into bulk flow and pressure or stress. This exposes the closure problem. The equation for the first moment depends on the second moment; an equation for the second moment depends on still higher moments.

Kinetic theory explains where fluid equations come from, but it does not produce a closed Euler or Navier–Stokes system merely by taking a few integrals. We need an additional constitutive assumption or an asymptotic analysis showing that the distribution stays near a suitable local equilibrium.

## Why the Maxwellian matters

For a classical dilute gas, a distinguished equilibrium distribution is Gaussian in velocity relative to the bulk velocity. It is called a Maxwellian. Its parameters encode density, average velocity, and temperature. At such an equilibrium, the collision operator vanishes: collisions reshuffle velocities without changing the distribution.

The Boltzmann H theorem describes a direction of evolution toward equilibrium under appropriate conditions. A quantity built from the integral of f times log f does not increase due to collisions in the spatially homogeneous setting. With the usual entropy sign convention, this corresponds to nondecreasing entropy.

The statement is not a promise that every solution in every domain converges smoothly to a Maxwellian. Boundary effects, conservation constraints, solution regularity, and global existence are substantial mathematical questions. The H theorem is a structural inequality, and its interpretation depends on the precise kinetic model.

## The path toward fluid mechanics

When collisions act on a much shorter time scale than macroscopic evolution, one expects the distribution to stay close to a local Maxwellian. Expanding around this equilibrium and following the slowly varying moments leads, in appropriate regimes, to compressible Euler or Navier–Stokes equations. The relevant limiting arguments are delicate because they must control the collision term, spatial gradients, and the size of deviations from equilibrium.

Kinetic theory is therefore more than a derivation trick. It explains both the success and the limitations of fluid models. Density, velocity, and temperature summarize a distribution, but different distributions can have the same first few moments and different higher-order stresses. Those differences matter when the gas is rarefied, far from equilibrium, or influenced by boundaries at small scales.

The central mathematical move is to work at two levels simultaneously. At the microscopic statistical level, a distribution evolves through transport and collisions. At the macroscopic level, its conserved moments obey balance laws. The bridge between them is an integration identity; the step from balance laws to a closed continuum model requires additional analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A kinetic density \(f(t,x,v)\ge0\) with \(x,v\in\mathbf R^d\) obeys a Boltzmann-type equation
\[\partial_t f+v\cdot\nabla_x f+F(t,x)\cdot\nabla_v f=Q(f,f).\]
For \(Q=0\) and \(F=0\), characteristics give \(f(t,x,v)=f_0(x-tv,v)\). Assuming decay/integrability sufficient for integration by parts and an elastic collision operator,
\[\int Q(f,f)(1,v,|v|^2/2)\,dv=0.\]
Define \(\rho=\int f\,dv\), \(j=\int vf\,dv\), and \(\Pi=\int v\otimes vf\,dv\). Then
\[\partial_t\rho+\nabla_x\cdot j=0,\qquad\partial_t j+\nabla_x\cdot\Pi=\rho F\]
under the stated force and boundary/decay assumptions. These equations are not *closed* without a law for \(\Pi\).

A normalized Maxwellian in d dimensions is
\[\mathcal M_{\rho,u,T}(v)=\frac{\rho}{(2\pi T)^{d/2}}\exp\!\left(-\frac{|v-u|^2}{2T}\right),\qquad T>0.\]
For suitable collision kernels, \(Q(\mathcal M,\mathcal M)=0\), and collision entropy production satisfies \(\int Q(f,f)\log f\,dv\le0\). Existence, smoothness and long-time convergence require additional hypotheses. The molecular-chaos approximation and appropriate scaling enter the physical derivation of the Boltzmann equation.

### Exercises with answers

1. Solve free transport for \(f_0(x,v)=e^{-x^2-v^2}\) in one dimension. **Answer:** \(f(t,x,v)=e^{-(x-tv)^2-v^2}\).
2. Why does collision conservation of number remove Q from the density equation? **Answer:** \(\int Q(f,f)\,dv=0\).
3. Why is the momentum equation not generally closed in \(\rho\) and j alone? **Answer:** it contains the independent second velocity moment \(\Pi\).
4. Does free transport automatically equal heat diffusion after integrating over velocities? **Answer:** no; a reversible velocity-mixing mechanism need not obey a closed heat equation.

### Reading and source notes

- [Cercignani, Illner and Pulvirenti, The Mathematical Theory of Dilute Gases](https://link.springer.com/book/10.1007/978-1-4419-8524-8), classical kinetic theory and the Boltzmann equation.
- [Lawrence C. Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), transport equations and PDE methods.
