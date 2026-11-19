# Return maps, periodic stability, and invariant manifolds

<!-- BEGIN SPOKEN LECTURE -->

# Return maps, periodic stability, and invariant manifolds

## Poincaré Maps, Periodic Orbits, and Floquet Theory

A pendulum with no friction can trace closed curves in phase space. A self-sustained oscillator can also trace a closed curve. The pictures may look similar, yet their dynamics are different. In the ideal undamped pendulum, many neighboring closed orbits coexist. In a stable self-sustained oscillator, nearby trajectories spiral toward one distinguished closed orbit. A picture of the curve alone does not tell us which situation we have.

To distinguish them, we turn a continuous flow into a return map. Instead of watching the trajectory at every instant, we record where it crosses a transverse section after each circuit. That reduces a periodic-orbit problem to a fixed-point problem.

### A transversal cut through the flow

Imagine drawing a short line segment crossing a periodic orbit, but not tangent to it. Take an initial point on this segment, follow the differential equation forward, and record the next crossing in the same direction. This defines a Poincaré return map, locally and under suitable regularity and transversality conditions.

The periodic orbit itself corresponds to a fixed point of the map. Every time it completes a circuit, it returns to the same position on the section. A nearby trajectory may return closer to that point, farther from it, or at the same distance. Those alternatives reveal the orbit's transverse stability.

The derivative of the return map at its fixed point gives the linear response to a small displacement along the section. If every eigenvalue of that derivative has modulus less than one, the periodic orbit is locally asymptotically stable in the transverse directions. If one has modulus greater than one, there is a transverse instability. Eigenvalues of modulus exactly one require additional analysis; linearization alone may not decide the outcome.

### A radial example we can solve by inspection

Use polar coordinates in the plane away from the origin. Let the radius satisfy r prime equals r times one minus r squared, and let the angle increase at unit speed. The angular motion completes a revolution every two pi time units. The radial equation has equilibria at r equals zero and r equals one, if we restrict attention to nonnegative radius.

For r between zero and one, the radial derivative is positive, so the radius grows. For r greater than one, it is negative, so the radius shrinks. Thus every positive starting radius approaches one as time advances. The circle r equals one is an attracting periodic orbit, and it is isolated among nearby periodic orbits. It is a stable limit cycle.

Now calculate the transverse rate. Differentiate the radial right-hand side r minus r cubed. At r equals one, the derivative is one minus three, or negative two. So a tiny radial error evolves to first order like exponential of negative two times time.

A return takes two pi time units on this orbit. Therefore the derivative of the radial return map at r equals one is the exponential of negative four pi. It is strictly between zero and one, giving quantitative contraction on each circuit. The phase shift along the cycle is not a transverse instability; moving slightly forward on the same orbit merely changes where the oscillation begins.

### Compare a center

Now change the radial equation to r prime equals zero while keeping the same angular equation. Every circle centered at the origin is a periodic orbit with period two pi. Choose a section at a fixed angle. The return map leaves the radius unchanged, so its derivative is one.

There is no attraction to a particular circle. If the initial radius is slightly too large, it remains slightly too large forever. Each periodic orbit belongs to a family of nearby periodic orbits. This is the idealized center situation.

Both models draw circular trajectories. The return map exposes the difference: the limit cycle contracts transverse errors, while the center retains them. This is why the existence of a periodic orbit and the stability of that orbit are separate questions.

### Linearization along a moving trajectory

For an equilibrium, linearization uses a constant Jacobian matrix evaluated at the equilibrium. Along a nonconstant periodic orbit, the Jacobian changes as the state moves. Let x star of time be a periodic solution with period T. A small perturbation satisfies, to first order, a linear differential equation whose coefficient matrix is the Jacobian of the vector field evaluated along x star. That matrix is periodic in time.

Floquet theory studies linear systems with periodic coefficients. Build a fundamental matrix solution starting from the identity. After one period, its value is the monodromy matrix. Its eigenvalues are Floquet multipliers. These multipliers describe how small disturbances change over a full cycle.

For an autonomous differential equation, one multiplier is always one along the direction tangent to a nonstationary periodic orbit: shifting the phase gives another solution on the same orbit. The other multipliers control transverse behavior and coincide, in the appropriate local sense, with eigenvalues of the Poincaré map derivative. So the neutral phase direction should not be misread as evidence of transverse instability.

### Exponents and their limitations

Floquet exponents encode multipliers through exponentiation over one period. Their real parts describe exponential growth or decay, with care about choices of complex logarithm. In a nonautonomous periodically driven system, the automatic neutral multiplier associated with time translation need not be present in the same way, because shifting a solution's phase does not necessarily preserve the forcing schedule.

There are also limitations to linear stability tests. A multiplier exactly on the unit circle can hide nonlinear attraction, repulsion, or neutral motion. A multiplier larger than one in modulus signals linear instability, but precise nonlinear conclusions require the relevant smoothness and hyperbolicity assumptions. Poincaré sections must be genuinely transverse and the return map must be defined in a suitable neighborhood; none of this follows simply from drawing a closed curve.

### Why this matters beyond pendulums

Periodic orbits appear in electronics, chemical reactions, biology, celestial dynamics, and feedback systems. They can be stable rhythms, fragile resonances, or boundaries separating different long-term behaviors. The Poincaré map turns one period of continuous motion into a discrete dynamical system. Floquet multipliers then give a compact summary of how perturbations behave over that period.

The key conceptual move is to remove the motion we already understand—the repeated trip around the orbit—and ask what happens to errors across successive trips. A limit cycle is not merely a closed path. It is a fixed point of a return process, with a stability structure that can be analyzed, computed, and compared across models.

## Stable, Unstable, and Center Manifolds: The Geometry Near Equilibria

A small perturbation of an equilibrium may shrink, grow, or linger. For a linear differential equation, the eigenvalues of the system matrix explain much of what happens. Negative real parts indicate decay, positive real parts growth, and purely imaginary or zero real parts require additional thought.

Nonlinear equations complicate this picture. Trajectories need not travel along straight eigenspaces. Instead, under appropriate hypotheses, curved invariant surfaces emerge near an equilibrium. Stable, unstable, and center manifold theory gives a precise language for those surfaces.

### Begin with a saddle

Consider a two-variable linear system: the first coordinate grows at a rate proportional to itself, while the second decays at twice its own rate. Starting on the vertical axis, the solution approaches the origin exponentially. Starting on the horizontal axis, it moves away exponentially in forward time. Starting at almost any other point, it eventually escapes the neighborhood because of its growing horizontal component.

The stable eigenspace is the vertical axis. The unstable eigenspace is the horizontal axis. They have the dimensions of the subspaces associated with negative and positive real-part eigenvalues respectively.

Now add a nonlinear term to the second equation, for instance the square of the first coordinate. The origin remains an equilibrium, and its Jacobian is unchanged. But the line that captures backward-time approach to the origin bends into a parabola. The stable manifold remains the vertical axis, while the unstable manifold becomes a curved invariant graph.

The reason is simple enough to calculate explicitly. Along the unstable parabola, the second coordinate must change according to the differential equation at exactly the rate implied by its dependence on the first. Matching those two rates fixes the coefficient of the parabola. The nonlinear geometry is not arbitrary decoration; invariance determines it.

### The stable manifold theorem

Suppose a sufficiently smooth autonomous system has an equilibrium and its linearization is hyperbolic: no eigenvalue has zero real part. The stable manifold theorem says there is a local smooth stable manifold tangent at the equilibrium to the stable eigenspace. Points on it remain near the equilibrium in forward time and converge exponentially, with qualifications on the local neighborhood and rates. There is similarly an unstable manifold, defined using backward-time behavior and tangent to the unstable eigenspace.

For a hyperbolic fixed point, the number of stable and unstable directions is robust under small perturbations of the system. The geometric manifolds may curve and shift, but their dimensions do not jump unless eigenvalues cross the imaginary axis.

The theorem is local. It does not say every point in the whole state space has a simple fate, nor that the stable and unstable manifolds can be continued globally without complicated folds, intersections, or recurrent dynamics.

### Why hyperbolic equilibria are tractable

The rough picture follows from a competition between exponential expansion and exponential contraction. In a linear system, eigenvectors split the tangent space into stable and unstable parts. For a nonlinear system near the equilibrium, the higher-order terms are small relative to the linear part. One can search for an invariant manifold as a graph over one eigenspace and use a contraction or graph-transform argument to solve the invariance equation.

Another related result, Hartman–Grobman, says that near a hyperbolic equilibrium the nonlinear flow is locally topologically conjugate to its linearization. Trajectories have the same local qualitative organization, although the conjugacy need not preserve lengths, rates, or differentiability.

Stable manifold theory tells us about smooth invariant subsets. Hartman–Grobman tells us about the qualitative organization of the surrounding flow. These results cooperate, but they make different claims.

### Zero eigenvalues: a decision the Jacobian cannot make

Now examine the scalar equation in which the rate of change is minus the cube of the state. The equilibrium at zero has derivative zero, so its linearization is simply the zero equation. A linear approximation would predict no motion at all.

The nonlinear equation tells a different story. Positive states decrease toward zero and negative states increase toward zero. The equilibrium attracts from both sides, but the convergence is algebraic rather than exponential. A small initial displacement decreases roughly like one divided by the square root of time. Linearization did not detect this stability mechanism.

Change the sign of the cubic, and the equilibrium becomes repelling instead. Both equations have the same zero linearization. Therefore a zero eigenvalue does not determine stability. The nonlinear terms are decisive.

This is where a center manifold can help. When the Jacobian has eigenvalues on the imaginary axis as well as stable or unstable eigenvalues, a local center manifold is tangent to the center eigenspace and invariant under the flow. Under appropriate smoothness assumptions it exists, but it need not be unique. The dynamics restricted to it often capture the difficult long-term behavior that linearization cannot resolve.

### Reduction without pretending everything is stable

Consider a two-variable system where the first coordinate decays exponentially and the second satisfies the negative-cubic equation. The first direction is stable; the second has zero linear eigenvalue. The line where the first coordinate is zero is an exact center manifold. On that line, motion toward zero is slow and algebraic.

A nearby initial condition may first lose most of its stable-coordinate component quickly and then spend a long time drifting along the center direction. This explains why some systems have fast transients followed by slow evolution, even near a single equilibrium.

But a center manifold is not always attractive, and one must not infer a global reduced model from local existence. Its importance lies in reducing the dimension of the nonlinear analysis under explicit assumptions.

### Bifurcations emerge when eigenvalues cross zero

Consider the family of scalar equations whose rate is a parameter times the state minus the state cubed. When the parameter is negative, zero is stable. At parameter zero the linear eigenvalue vanishes, but the negative cubic still attracts. When the parameter becomes positive, zero is unstable and two new stable equilibria appear at the positive and negative square roots of the parameter.

This is the pitchfork bifurcation pattern under the stated symmetry. At the critical parameter, the stable manifold theorem in its hyperbolic form no longer applies at the origin. The center dynamics are the appropriate tool.

The same philosophy applies when a complex conjugate pair crosses the imaginary axis, leading to a Hopf bifurcation under additional nondegeneracy conditions. Center manifold reduction isolates the critical modes so that nonlinear terms can determine whether nearby periodic orbits emerge and what stability they have.

### What the geometry buys us

The Jacobian is still indispensable. It separates directions that expand or contract exponentially and identifies the center directions that need further investigation. But it is not the entire story. Stable and unstable manifolds are nonlinear continuations of hyperbolic eigenspaces. Center manifolds focus attention on directions where linearization cannot settle the question.

The main lesson is methodological. Use the linear system to organize the problem. Then ask whether the hypotheses for a hyperbolic theorem hold. If they do, exploit the robust invariant geometry. If they do not, retain the nonlinear terms on the center directions rather than making an unsupported stability claim. Near an equilibrium, a good reduction preserves exactly the part of the dynamics that matters.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Poincaré Maps, Periodic Orbits, and Floquet Theory

**Track:** Differential Equations and Dynamical Systems. **Background:** planar systems, linearization, eigenvalues and stability. **Central question:** how can we decide whether a closed trajectory attracts nearby motions or merely sits among many closed trajectories?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. What is the Poincaré multiplier of the attracting radial example? **Answer:** \(e^{-4\pi}\).
2. Is a multiplier of magnitude one alone enough to prove stability? **No:** nonlinear terms may decide the behavior.
3. Why is a Floquet multiplier equal to one expected in autonomous systems? **Answer:** infinitesimal time translation produces a tangent perturbation along the periodic orbit.
4. What geometric condition must a local Poincaré section satisfy? **Answer:** it must intersect the flow transversely, rather than tangent to the orbit.

##### Reading and source notes

- Steven H. Strogatz, *Nonlinear Dynamics and Chaos*, second edition (Westview Press, 2015), limit cycles and Poincaré maps.
- Carmen Chicone, *Ordinary Differential Equations with Applications*, second edition (Springer, 2006), Poincaré maps and Floquet theory.

### Stable, Unstable, and Center Manifolds: The Geometry Near Equilibria

**Track:** Differential Equations and Dynamical Systems. **Background:** linear systems, eigenvalues, nonlinear equilibria, phase portraits. **Central question:** which conclusions about nonlinear motion can be read from the Jacobian, and which require higher-order terms?

#### Mathematical companion (not spoken)

For \(\dot z=F(z)\), \(F(0)=0\), \(F\in C^r\) with \(r\ge1\), let \(A=DF(0)\). Hyperbolicity means \(\sigma(A)\cap i\mathbb R=\varnothing\). There are local \(C^r\) stable and unstable manifolds tangent to \(E^s\) and \(E^u\), respectively, with dimensions equal to the corresponding eigenspace dimensions. Near hyperbolic equilibria, Hartman–Grobman gives local topological equivalence to the linear flow, not generally a smooth conjugacy.

**Exact nonlinear saddle:** \(\dot x=x\), \(\dot y=-2y+x^2\). The stable manifold is \(x=0\); the unstable manifold is \(y=x^2/4\), because along \(y=h(x)\), \(h'(x)\dot x=-2h(x)+x^2\), and \(h(x)=x^2/4\) solves this. Explicitly
\[x(t)=x_0e^t,\quad y(t)=(y_0-x_0^2/4)e^{-2t}+(x_0^2/4)e^{2t}.\]

**Center example:** \(\dot x=-x\), \(\dot z=-z^3\). The center eigenspace is the \(z\)-axis; \(x=0\) is an invariant center manifold. For \(t\ge0\),
\[z(t)=\frac{z_0}{\sqrt{1+2z_0^2t}},\qquad x(t)=x_0e^{-t}.\]
The linearization has eigenvalues \(-1,0\) and does not predict the algebraic decay of \(z\). Center manifolds generally need not be unique, unlike the local stable/unstable manifolds under hyperbolicity.

##### Exercises with answers

1. For \(\dot x=x,\dot y=-2y+x^2\), where do solutions converge to zero as \(t\to+\infty\)? **Answer:** only along the stable manifold \(x=0\), where \(y(t)=y_0e^{-2t}\).
2. Why is \(y=x^2/4\) invariant? **Answer:** differentiating \(y=x^2/4\) gives \(\dot y=(x/2)\dot x=x^2/2\), agreeing with \(-2(x^2/4)+x^2=x^2/2\).
3. Can a zero eigenvalue determine asymptotic stability? **No:** \(\dot z=-z^3\) and \(\dot z=z^3\) have the same zero derivative and opposite stability.
4. Does Hartman–Grobman generally give a differentiable coordinate change? **No:** the standard conclusion is a local homeomorphism that conjugates qualitative flows.

##### Reading and source notes

- [MIT 18.385J Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/), invariant manifolds, linearization, and bifurcations.
- Lawrence Perko, [*Differential Equations and Dynamical Systems*](https://link.springer.com/book/10.1007/978-1-4613-0003-8), stable and unstable manifolds and center manifold analysis.
- [MIT 18.353J Nonlinear Dynamics I](https://ocw.mit.edu/courses/18-353j-nonlinear-dynamics-i-chaos-fall-2012/), nonlinear flow and local normal forms.
