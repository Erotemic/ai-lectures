# 012000 — Poincaré Maps, Periodic Orbits, and Floquet Theory

**Track:** Differential Equations and Dynamical Systems. **Background:** planar systems, linearization, eigenvalues and stability. **Central question:** how can we decide whether a closed trajectory attracts nearby motions or merely sits among many closed trajectories?

<!-- BEGIN SPOKEN LECTURE -->

# Poincaré Maps, Periodic Orbits, and Floquet Theory

A pendulum with no friction can trace closed curves in phase space. A self-sustained oscillator can also trace a closed curve. The pictures may look similar, yet their dynamics are different. In the ideal undamped pendulum, many neighboring closed orbits coexist. In a stable self-sustained oscillator, nearby trajectories spiral toward one distinguished closed orbit. A picture of the curve alone does not tell us which situation we have.

To distinguish them, we turn a continuous flow into a return map. Instead of watching the trajectory at every instant, we record where it crosses a transverse section after each circuit. That reduces a periodic-orbit problem to a fixed-point problem.

## A transversal cut through the flow

Imagine drawing a short line segment crossing a periodic orbit, but not tangent to it. Take an initial point on this segment, follow the differential equation forward, and record the next crossing in the same direction. This defines a Poincaré return map, locally and under suitable regularity and transversality conditions.

The periodic orbit itself corresponds to a fixed point of the map. Every time it completes a circuit, it returns to the same position on the section. A nearby trajectory may return closer to that point, farther from it, or at the same distance. Those alternatives reveal the orbit's transverse stability.

The derivative of the return map at its fixed point gives the linear response to a small displacement along the section. If every eigenvalue of that derivative has modulus less than one, the periodic orbit is locally asymptotically stable in the transverse directions. If one has modulus greater than one, there is a transverse instability. Eigenvalues of modulus exactly one require additional analysis; linearization alone may not decide the outcome.

## A radial example we can solve by inspection

Use polar coordinates in the plane away from the origin. Let the radius satisfy r prime equals r times one minus r squared, and let the angle increase at unit speed. The angular motion completes a revolution every two pi time units. The radial equation has equilibria at r equals zero and r equals one, if we restrict attention to nonnegative radius.

For r between zero and one, the radial derivative is positive, so the radius grows. For r greater than one, it is negative, so the radius shrinks. Thus every positive starting radius approaches one as time advances. The circle r equals one is an attracting periodic orbit, and it is isolated among nearby periodic orbits. It is a stable limit cycle.

Now calculate the transverse rate. Differentiate the radial right-hand side r minus r cubed. At r equals one, the derivative is one minus three, or negative two. So a tiny radial error evolves to first order like exponential of negative two times time.

A return takes two pi time units on this orbit. Therefore the derivative of the radial return map at r equals one is the exponential of negative four pi. It is strictly between zero and one, giving quantitative contraction on each circuit. The phase shift along the cycle is not a transverse instability; moving slightly forward on the same orbit merely changes where the oscillation begins.

## Compare a center

Now change the radial equation to r prime equals zero while keeping the same angular equation. Every circle centered at the origin is a periodic orbit with period two pi. Choose a section at a fixed angle. The return map leaves the radius unchanged, so its derivative is one.

There is no attraction to a particular circle. If the initial radius is slightly too large, it remains slightly too large forever. Each periodic orbit belongs to a family of nearby periodic orbits. This is the idealized center situation.

Both models draw circular trajectories. The return map exposes the difference: the limit cycle contracts transverse errors, while the center retains them. This is why the existence of a periodic orbit and the stability of that orbit are separate questions.

## Linearization along a moving trajectory

For an equilibrium, linearization uses a constant Jacobian matrix evaluated at the equilibrium. Along a nonconstant periodic orbit, the Jacobian changes as the state moves. Let x star of time be a periodic solution with period T. A small perturbation satisfies, to first order, a linear differential equation whose coefficient matrix is the Jacobian of the vector field evaluated along x star. That matrix is periodic in time.

Floquet theory studies linear systems with periodic coefficients. Build a fundamental matrix solution starting from the identity. After one period, its value is the monodromy matrix. Its eigenvalues are Floquet multipliers. These multipliers describe how small disturbances change over a full cycle.

For an autonomous differential equation, one multiplier is always one along the direction tangent to a nonstationary periodic orbit: shifting the phase gives another solution on the same orbit. The other multipliers control transverse behavior and coincide, in the appropriate local sense, with eigenvalues of the Poincaré map derivative. So the neutral phase direction should not be misread as evidence of transverse instability.

## Exponents and their limitations

Floquet exponents encode multipliers through exponentiation over one period. Their real parts describe exponential growth or decay, with care about choices of complex logarithm. In a nonautonomous periodically driven system, the automatic neutral multiplier associated with time translation need not be present in the same way, because shifting a solution's phase does not necessarily preserve the forcing schedule.

There are also limitations to linear stability tests. A multiplier exactly on the unit circle can hide nonlinear attraction, repulsion, or neutral motion. A multiplier larger than one in modulus signals linear instability, but precise nonlinear conclusions require the relevant smoothness and hyperbolicity assumptions. Poincaré sections must be genuinely transverse and the return map must be defined in a suitable neighborhood; none of this follows simply from drawing a closed curve.

## Why this matters beyond pendulums

Periodic orbits appear in electronics, chemical reactions, biology, celestial dynamics, and feedback systems. They can be stable rhythms, fragile resonances, or boundaries separating different long-term behaviors. The Poincaré map turns one period of continuous motion into a discrete dynamical system. Floquet multipliers then give a compact summary of how perturbations behave over that period.

The key conceptual move is to remove the motion we already understand—the repeated trip around the orbit—and ask what happens to errors across successive trips. A limit cycle is not merely a closed path. It is a fixed point of a return process, with a stability structure that can be analyzed, computed, and compared across models.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a \(C^1\) autonomous system \(\dot x=f(x)\) with a nonstationary periodic solution \(x_*(t+T)=x_*(t)\), choose a local cross section \(\Sigma\) transverse to \(f(x_*(0))\). The Poincaré map \(P:\Sigma\to\Sigma\) sends a nearby point to its next return with compatible orientation. The periodic orbit corresponds to a fixed point \(P(x_*(0))=x_*(0)\). Eigenvalues of \(DP\) give transverse multipliers. Strictly inside the unit disk gives local asymptotic orbital stability; a multiplier outside gives instability under standard smoothness assumptions.

The variational equation and monodromy matrix are
\[
\dot\xi=A(t)\xi,\quad A(t)=Df(x_*(t)),\quad
\dot\Phi=A(t)\Phi,\ \Phi(0)=I,\quad M=\Phi(T).
\]
Eigenvalues of \(M\) are Floquet multipliers. For autonomous systems, \(\dot x_*(t)\) solves the variational equation and yields a multiplier \(1\) tangent to the orbit. The remaining multipliers correspond to transverse return-map eigenvalues, with the appropriate nondegeneracy and section assumptions.

**Example.** In polar coordinates \(\dot r=r(1-r^2)\), \(\dot\theta=1\), the periodic orbit \(r=1\) has \(T=2\pi\). The radial variational derivative is \(\partial_r[r-r^3]_{r=1}=-2\), so
\[
P'(1)=e^{-2T}=e^{-4\pi},
\]
which is attracting. For \(\dot r=0,\dot\theta=1\), the return map is \(P(r)=r\), so every radius is a periodic orbit and \(P'(r)=1\); no isolated attracting cycle occurs.

### Exercises with answers

1. What is the Poincaré multiplier of the attracting radial example? **Answer:** \(e^{-4\pi}\).
2. Is a multiplier of magnitude one alone enough to prove stability? **No:** nonlinear terms may decide the behavior.
3. Why is a Floquet multiplier equal to one expected in autonomous systems? **Answer:** infinitesimal time translation produces a tangent perturbation along the periodic orbit.
4. What geometric condition must a local Poincaré section satisfy? **Answer:** it must intersect the flow transversely, rather than tangent to the orbit.

### Reading and source notes

- Steven H. Strogatz, *Nonlinear Dynamics and Chaos*, second edition (Westview Press, 2015), limit cycles and Poincaré maps.
- Carmen Chicone, *Ordinary Differential Equations with Applications*, second edition (Springer, 2006), Poincaré maps and Floquet theory.
