# 019000 — Hamiltonian Systems and Symplectic Flows

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order systems, gradients, differential forms, energy conservation. **Central question:** what dynamical structure survives in systems without dissipation?

<!-- BEGIN SPOKEN LECTURE -->

# Hamiltonian Systems and Symplectic Flows

Watch a pendulum swinging in a nearly frictionless room. It trades kinetic energy for potential energy and back again. In the simplest mathematical model, the total energy stays constant. That conservation law is familiar. What is less obvious is that the motion also preserves a geometric structure in the space of all possible positions and momenta.

Hamiltonian mechanics organizes a state using two kinds of coordinates. Position tells us where the system is; momentum tells us how it is moving. Together they form phase space. For one moving particle on a line, phase space is a plane with one position axis and one momentum axis. A whole trajectory draws a curve in that plane.

Instead of deriving the motion directly from forces, we begin with a function H of position and momentum, called the Hamiltonian. For familiar conservative mechanical systems it is total energy: kinetic plus potential. Hamilton's equations say that the time derivative of position is the derivative of H with respect to momentum, while the time derivative of momentum is minus the derivative of H with respect to position.

The minus sign is essential. It turns the gradient of H sideways in phase space. Rather than following the gradient downhill, a state moves along a level set of H when the Hamiltonian has no explicit time dependence.

## The oscillator as a phase-space curve

Take a mass attached to an ideal spring. Its Hamiltonian is momentum squared divided by twice the mass, plus spring stiffness times position squared divided by two. Hamilton's equations reproduce the familiar harmonic-oscillator equation.

In phase space, the conserved energy curves are ellipses. The moving state travels around one of them. There is no spiral toward the center, because the ideal model has no friction. If we add a velocity-dependent damping force, the trajectory can spiral inward, but we have changed the dynamical class. That damped flow is not the autonomous Hamiltonian flow of the original two-dimensional canonical phase space.

A conserved energy function already restricts the motion, but there is more. Consider a small region of initial states, a patch rather than one point. Follow every state in the patch forward by the same amount of time. Its shape may shear and stretch. Yet its area in canonical position-momentum coordinates is preserved.

This is Liouville's theorem in one degree of freedom. In several degrees of freedom it becomes preservation of phase-space volume. The reason is visible in the equations: the divergence of the Hamiltonian vector field is zero, since two mixed second derivatives of H cancel.

## Symplectic structure, not just area

A two-form called the symplectic form captures the oriented areas of position-momentum planes. In canonical coordinates, it is the sum of each position differential wedged with its matching momentum differential. Hamiltonian flow preserves that two-form, not merely its top-dimensional volume.

Volume preservation alone would be weaker. In a high-dimensional phase space, a map can keep overall volume constant while distorting the pairwise position-momentum geometry in ways a symplectic map cannot. Symplecticity is the stronger invariant that makes Hamiltonian dynamics a special branch of differential equations.

The preservation law has a concise proof. The Hamiltonian vector field is defined so that contracting it with the symplectic form gives the differential of H, up to the chosen sign convention. Taking an exterior derivative yields zero, since the exterior derivative applied twice vanishes. Cartan's formula for the Lie derivative then shows that the flow leaves the symplectic form unchanged.

This geometric argument works even in coordinates where the phase portrait is hard to draw. It also explains why symplectic numerical integrators are worth studying: an algorithm that respects the form can preserve qualitative phase-space behavior over long times better than a method chosen only for low local error.

## What is conserved, and what is not

For an autonomous Hamiltonian, energy remains constant along exact solutions. For a time-dependent Hamiltonian, the flow can remain symplectic while energy changes. Likewise, a symplectic numerical integrator does not generally preserve the exact Hamiltonian at every step. It preserves a discrete version of the geometric structure, often with favorable long-time energy behavior under additional hypotheses.

Nor does phase-volume preservation forbid every kind of complicated motion. Hamiltonian systems with enough degrees of freedom can exhibit chaotic trajectories. Symplecticity limits how volume can contract, but it does not require every orbit to be periodic or easy to predict.

We have now separated three facts that are often merged. A system can have a conserved energy. It can have an invariant symplectic form. It can preserve phase volume. In autonomous canonical Hamiltonian mechanics, all three occur, but they are logically different statements with different assumptions.

The main gain is structural. Hamilton's equations are not merely another notation for Newton's laws. They reveal which patterns remain intact while trajectories twist through phase space, and they give us a language for preserving those patterns in analysis and computation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(q,p\in\mathbf R^n\) and a smooth autonomous \(H(q,p)\), Hamilton's equations are
\[\dot q_i=\partial H/\partial p_i,\qquad \dot p_i=-\partial H/\partial q_i.\]
With \(\omega=\sum_i dq_i\wedge dp_i\), the convention \(\iota_{X_H}\omega=dH\) yields these equations. Since \(d\omega=0\), Cartan's formula gives \(\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)=d(dH)=0\), so \(\Phi_t^*\omega=\omega\). For autonomous H, \(dH/dt=dH(X_H)=\omega(X_H,X_H)=0\). For H depending explicitly on t, \(dH/dt=\partial_t H\) along the flow.

**Harmonic oscillator:** \(H=p^2/(2m)+kq^2/2\), so \(q'=p/m\), \(p'=-kq\), and \(q''+(k/m)q=0\). Energy shells are ellipses. The phase-space divergence equals \(\sum_i\partial_{q_i}\partial_{p_i}H-\partial_{p_i}\partial_{q_i}H=0\), yielding Liouville volume preservation for smooth canonical Hamiltonian flows.

**Caution:** volume preservation does not imply symplecticity in dimensions four and higher; exact energy conservation need not hold for time-dependent H, and a symplectic numerical map need not exactly conserve H.

### Exercises with answers

1. For H=(q²+p²)/2, find the trajectories. **Answer:** \(q'=p\), \(p'=-q\); circles oriented clockwise in the (q,p) plane, with fixed q²+p².
2. Why cannot an autonomous planar Hamiltonian flow have an asymptotically attracting equilibrium surrounded by a neighborhood of positive area? **Answer:** the flow preserves area and cannot contract the whole neighborhood to zero area.
3. Is \(H(q,p,t)=p^2/2+tq\) constant along a trajectory? **Answer:** generally no; \(dH/dt=\partial_tH=q\).
4. What is stronger than phase-volume preservation? **Answer:** preservation of the symplectic two-form, including oriented areas of canonical two-planes.

### Reading and source notes

- [MIT OpenCourseWare, Symplectic Geometry lecture 4](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/864a8cbd55d8d9696a717db38f8668a9_lect04.pdf), Hamiltonian vector fields and symplectic flows.
- [MIT Classical Mechanics II, Hamiltonian Mechanics](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/09ab68ae8e7987debc025892e00c0f1f_MIT8_223IAP17_Lec15.pdf), coordinates and energy.
- [MIT Classical Mechanics: A Computational Approach](https://ocw.mit.edu/courses/12-620j-classical-mechanics-a-computational-approach-fall-2008/pages/readings/), Liouville theorem and symplectic maps.
