# 007000 — Nonlinear Phase Planes: Energy, Equilibria, and the Pendulum

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order systems, linearization, uniqueness, and elementary mechanics. **Question:** how can we understand the geometry of a nonlinear differential equation without solving it explicitly?

<!-- BEGIN SPOKEN LECTURE -->

# Nonlinear Phase Planes: Energy, Equilibria, and the Pendulum

A linear differential equation can often be solved with exponentials and eigenvectors. Nonlinear equations are harder: the direction of motion may change in complicated ways as the state changes, and there may be no formula for the solution using elementary functions. But we can still learn a great deal by looking at the geometry of motion in state space.

Consider a pendulum without friction or an external force. Let theta be the angle from the downward vertical and let v be the angular velocity. The first equation says the rate of change of theta equals v. The second says the rate of change of v equals minus sine theta, after choosing units in which the gravitational coefficient is one. These are two first-order equations for the state consisting of angle and velocity.

The phase plane is the diagram whose horizontal coordinate is angle and whose vertical coordinate is angular velocity. At every state, the equations supply an arrow giving the instantaneous rate of change of the two coordinates. A solution is a curve that follows those arrows through time.

There is one subtlety about the picture: physically, angles differing by a whole revolution describe the same orientation. The true phase space is a cylinder. Drawing the angle on the entire real line repeats copies of the same physical states. The repeated phase portrait is still useful, provided we remember the identification.

## Equilibria from the equations

An equilibrium is a state where both derivatives vanish. For the pendulum, v must be zero and sine theta must be zero. So equilibria occur at integer multiples of pi with zero velocity.

The states with angle an even multiple of pi correspond to the pendulum hanging down. The states with angle an odd multiple correspond to the pendulum standing upright. Both are equilibria in the mathematical sense: if placed exactly there with zero velocity, the idealized pendulum stays there. That does not mean both resist disturbances.

A small displacement near the downward position creates a restoring acceleration. A small displacement near the upright position creates an acceleration farther from the top. To make those statements precise we can linearize near an equilibrium.

The derivative matrix of our vector field has zero and one in its first row, and minus cosine theta and zero in its second row. At the downward equilibrium, cosine theta is one. The eigenvalues are the imaginary pair positive and negative i. The linearized solutions oscillate, suggesting a center. At the upright equilibrium, cosine theta is negative one. The eigenvalues are positive one and negative one. One direction grows and another decays exponentially. That equilibrium is a saddle.

There is a limitation: purely imaginary eigenvalues do not by themselves guarantee that a nonlinear equilibrium is a center. Higher-order terms can cause slow inward or outward drift. For the pendulum we have a second tool, energy, that settles the issue.

## Energy creates level curves

Define the energy as one half of the angular velocity squared plus one minus cosine of the angle. The first term is kinetic energy in our chosen units. The second is potential energy measured relative to the downward position.

Differentiate this energy along a solution. The derivative of one half v squared is v times the derivative of v. The derivative of one minus cosine theta is sine theta times the derivative of theta. Substitute the equations: v times negative sine theta plus sine theta times v. They cancel exactly. The energy stays constant along every solution.

Consequently, each orbit is confined to a level set of the energy function. We have learned a global fact about solutions without integrating the equations. The pendulum cannot spontaneously move from one energy level to another.

Near the bottom, energy is approximately one half times v squared plus one half times theta squared, so low-energy level curves look like ellipses. They enclose the stable downward equilibrium. Exact level curves are not perfect ellipses as the angle grows, but the closed-loop structure persists for energies between zero and two.

At energy two, the level set passes through the upright equilibrium. This is the separatrix: a boundary between qualitatively different kinds of motion. On one side are librations, where the pendulum swings back and forth. Above that energy, there are rotations, where the pendulum turns continuously around its pivot. The separatrix takes infinite time to approach the exact upright equilibrium under ideal dynamics, even though the geometric curve reaches it in the phase portrait.

## Stability is not the same as attraction

We say an equilibrium is stable in the sense of Lyapunov if trajectories starting sufficiently close remain close for all future time. We say it is asymptotically stable if sufficiently close trajectories not only stay close but actually approach the equilibrium as time goes to infinity.

The downward position of the ideal pendulum is stable but not asymptotically stable. Small displacements produce closed orbits with positive energy. Those trajectories keep oscillating. Conservation of energy forbids them from losing all their motion and settling exactly to rest.

The upright equilibrium is unstable. The linearized system has a growing direction, and the nonlinear dynamics near that hyperbolic saddle retain this local instability.

This distinction is useful in many systems. An oscillatory mode with no damping need not decay. A small perturbation may remain bounded without ever vanishing. When we describe a system as stable, we should specify which notion of stability we mean.

## Add damping and repeat the energy calculation

Now add friction proportional to velocity, with positive damping coefficient gamma. The velocity equation becomes minus sine theta minus gamma times v. Differentiate the same energy. The conservative terms still cancel, leaving minus gamma times v squared.

Energy can no longer increase. It decreases whenever the pendulum has nonzero velocity. The phase portrait no longer consists of perpetual closed-energy loops: generic nearby oscillations decay toward the downward equilibrium. But the formula alone is not a complete proof that every possible initial state approaches that bottom. The upright equilibrium and its stable separatrix remain special possibilities, and establishing global long-time limits requires additional arguments.

A useful general form of this reasoning is Lyapunov's method. Find a scalar function V of the state that is positive relative to an equilibrium and whose derivative along trajectories is nonpositive. Such a function can establish stability without an explicit solution. A strictly negative derivative away from the equilibrium, under suitable assumptions, can establish asymptotic stability. If the derivative can vanish on a larger set, more analysis is needed.

## Why trajectories cannot arbitrarily cross

The phase portrait also contains information supplied by uniqueness. If the vector field is locally Lipschitz, two solutions cannot pass through the same state at the same time and then continue along different paths. For an autonomous equation, if two solution curves meet at a point, they agree up to a shift of their time parameters on their common interval. Ordinary distinct trajectories cannot cross transversely in the phase plane.

This makes the phase portrait a constrained geometry. Equilibria cannot be crossed by a nonconstant solution in finite time under the local uniqueness hypotheses. Closed orbits, separatrices, and stable or unstable directions organize the remaining trajectories into regions of qualitatively similar behavior.

The nonlinear pendulum is valuable because we have several complementary ways to understand it: linearize near equilibria, use conserved energy to describe global level curves, and use uniqueness to control how those curves fit together. No one tool replaces the others. Together they provide a picture that an explicit formula, even if available, might make harder to see.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The undamped pendulum in nondimensional time is
\[
\dot\theta=v,\qquad \dot v=-\sin\theta,\qquad H(\theta,v)=\tfrac12v^2+1-\cos\theta.
\]
Along trajectories, \(\dot H=v(-\sin\theta)+\sin\theta\,v=0\). The equilibria are \((k\pi,0)\); at even \(k\),
\[
Df=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\quad(\lambda=\pm i),
\]
and at odd \(k\),
\[
Df=\begin{pmatrix}0&1\\1&0\end{pmatrix}\quad(\lambda=\pm1).
\]
The energy at an upright equilibrium is \(H=2\). On the cylinder \(S^1\times\mathbb R\), energies \(0<H<2\) yield periodic librations, \(H=2\) includes separatrices, and \(H>2\) yields rotational periodic orbits (periodic modulo the angular identification).

**Lyapunov argument near the bottom.** \(H\ge0\), and near \((0,0)\), \(H\) is positive definite with a strict local minimum. Since \(\dot H=0\), sufficiently small sublevel sets are invariant, establishing Lyapunov stability but not attraction.

**Damped model.** For \(\gamma>0\), \(\dot v=-\sin\theta-\gamma v\) and \(\dot H=-\gamma v^2\le0\). This inequality alone should not be used to assert global convergence to a single equilibrium for all initial states.

### Exercises with answers

1. Locate the equilibria of the pendulum. **Answer:** \((k\pi,0)\), for integer \(k\).
2. What distinguishes the energy-two curves? **Answer:** they pass through upright saddles and separate librational from rotational motion.
3. Can an undamped small oscillation be asymptotically stable toward the bottom? **No.** Positive conserved energy cannot decay to zero.
4. Under damping, what is the derivative of \(H\)? **Answer:** \(-\gamma v^2\).

### Reading

MIT OCW, [Nonlinear Dynamics: Chaos lecture notes](https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/pages/lecture-notes/), lectures on pendulum, phase planes, and dissipation; Steven Strogatz, *Nonlinear Dynamics and Chaos*, phase portraits and conserved quantities.
