# Nonlinear phase portraits, bifurcation, and stiffness

<!-- BEGIN SPOKEN LECTURE -->

# Nonlinear phase portraits, bifurcation, and stiffness

## Nonlinear Phase Planes: Energy, Equilibria, and the Pendulum

A linear differential equation can often be solved with exponentials and eigenvectors. Nonlinear equations are harder: the direction of motion may change in complicated ways as the state changes, and there may be no formula for the solution using elementary functions. But we can still learn a great deal by looking at the geometry of motion in state space.

Consider a pendulum without friction or an external force. Let theta be the angle from the downward vertical and let v be the angular velocity. The first equation says the rate of change of theta equals v. The second says the rate of change of v equals minus sine theta, after choosing units in which the gravitational coefficient is one. These are two first-order equations for the state consisting of angle and velocity.

The phase plane is the diagram whose horizontal coordinate is angle and whose vertical coordinate is angular velocity. At every state, the equations supply an arrow giving the instantaneous rate of change of the two coordinates. A solution is a curve that follows those arrows through time.

There is one subtlety about the picture: physically, angles differing by a whole revolution describe the same orientation. The true phase space is a cylinder. Drawing the angle on the entire real line repeats copies of the same physical states. The repeated phase portrait is still useful, provided we remember the identification.

### Equilibria from the equations

An equilibrium is a state where both derivatives vanish. For the pendulum, v must be zero and sine theta must be zero. So equilibria occur at integer multiples of pi with zero velocity.

The states with angle an even multiple of pi correspond to the pendulum hanging down. The states with angle an odd multiple correspond to the pendulum standing upright. Both are equilibria in the mathematical sense: if placed exactly there with zero velocity, the idealized pendulum stays there. That does not mean both resist disturbances.

A small displacement near the downward position creates a restoring acceleration. A small displacement near the upright position creates an acceleration farther from the top. To make those statements precise we can linearize near an equilibrium.

The derivative matrix of our vector field has zero and one in its first row, and minus cosine theta and zero in its second row. At the downward equilibrium, cosine theta is one. The eigenvalues are the imaginary pair positive and negative i. The linearized solutions oscillate, suggesting a center. At the upright equilibrium, cosine theta is negative one. The eigenvalues are positive one and negative one. One direction grows and another decays exponentially. That equilibrium is a saddle.

There is a limitation: purely imaginary eigenvalues do not by themselves guarantee that a nonlinear equilibrium is a center. Higher-order terms can cause slow inward or outward drift. For the pendulum we have a second tool, energy, that settles the issue.

### Energy creates level curves

Define the energy as one half of the angular velocity squared plus one minus cosine of the angle. The first term is kinetic energy in our chosen units. The second is potential energy measured relative to the downward position.

Differentiate this energy along a solution. The derivative of one half v squared is v times the derivative of v. The derivative of one minus cosine theta is sine theta times the derivative of theta. Substitute the equations: v times negative sine theta plus sine theta times v. They cancel exactly. The energy stays constant along every solution.

Consequently, each orbit is confined to a level set of the energy function. We have learned a global fact about solutions without integrating the equations. The pendulum cannot spontaneously move from one energy level to another.

Near the bottom, energy is approximately one half times v squared plus one half times theta squared, so low-energy level curves look like ellipses. They enclose the stable downward equilibrium. Exact level curves are not perfect ellipses as the angle grows, but the closed-loop structure persists for energies between zero and two.

At energy two, the level set passes through the upright equilibrium. This is the separatrix: a boundary between qualitatively different kinds of motion. On one side are librations, where the pendulum swings back and forth. Above that energy, there are rotations, where the pendulum turns continuously around its pivot. The separatrix takes infinite time to approach the exact upright equilibrium under ideal dynamics, even though the geometric curve reaches it in the phase portrait.

### Stability is not the same as attraction

We say an equilibrium is stable in the sense of Lyapunov if trajectories starting sufficiently close remain close for all future time. We say it is asymptotically stable if sufficiently close trajectories not only stay close but actually approach the equilibrium as time goes to infinity.

The downward position of the ideal pendulum is stable but not asymptotically stable. Small displacements produce closed orbits with positive energy. Those trajectories keep oscillating. Conservation of energy forbids them from losing all their motion and settling exactly to rest.

The upright equilibrium is unstable. The linearized system has a growing direction, and the nonlinear dynamics near that hyperbolic saddle retain this local instability.

This distinction is useful in many systems. An oscillatory mode with no damping need not decay. A small perturbation may remain bounded without ever vanishing. When we describe a system as stable, we should specify which notion of stability we mean.

### Add damping and repeat the energy calculation

Now add friction proportional to velocity, with positive damping coefficient gamma. The velocity equation becomes minus sine theta minus gamma times v. Differentiate the same energy. The conservative terms still cancel, leaving minus gamma times v squared.

Energy can no longer increase. It decreases whenever the pendulum has nonzero velocity. The phase portrait no longer consists of perpetual closed-energy loops: generic nearby oscillations decay toward the downward equilibrium. But the formula alone is not a complete proof that every possible initial state approaches that bottom. The upright equilibrium and its stable separatrix remain special possibilities, and establishing global long-time limits requires additional arguments.

A useful general form of this reasoning is Lyapunov's method. Find a scalar function V of the state that is positive relative to an equilibrium and whose derivative along trajectories is nonpositive. Such a function can establish stability without an explicit solution. A strictly negative derivative away from the equilibrium, under suitable assumptions, can establish asymptotic stability. If the derivative can vanish on a larger set, more analysis is needed.

### Why trajectories cannot arbitrarily cross

The phase portrait also contains information supplied by uniqueness. If the vector field is locally Lipschitz, two solutions cannot pass through the same state at the same time and then continue along different paths. For an autonomous equation, if two solution curves meet at a point, they agree up to a shift of their time parameters on their common interval. Ordinary distinct trajectories cannot cross transversely in the phase plane.

This makes the phase portrait a constrained geometry. Equilibria cannot be crossed by a nonconstant solution in finite time under the local uniqueness hypotheses. Closed orbits, separatrices, and stable or unstable directions organize the remaining trajectories into regions of qualitatively similar behavior.

The nonlinear pendulum is valuable because we have several complementary ways to understand it: linearize near equilibria, use conserved energy to describe global level curves, and use uniqueness to control how those curves fit together. No one tool replaces the others. Together they provide a picture that an explicit formula, even if available, might make harder to see.

## Bifurcations and Limit Cycles: When Dynamics Change Their Shape

A parameter may change the speed of a dynamical system without changing its basic behavior. But it may also cross a threshold where the geometry of the system changes: equilibria appear or disappear, stability changes hands, or a closed orbit emerges. Such a qualitative change is called a bifurcation.

We can study bifurcations with very small equations. Their simplicity is an advantage. By isolating the essential terms, we can see which conclusions follow from calculus and which depend on additional assumptions.

### A saddle-node creates two equilibria

Start with a scalar equation whose derivative equals a parameter, call it mu, minus the square of the state x. An equilibrium must satisfy x squared equals mu. For negative mu, there is no real equilibrium. At mu equal to zero, there is one equilibrium at x equals zero. For positive mu, two equilibria appear, one positive and one negative.

Stability comes from the derivative of the vector field with respect to x. That derivative is minus two x. At the positive equilibrium it is negative, so nearby states are pushed back toward the equilibrium. At the negative equilibrium it is positive, so nearby states are driven away. The two equilibria form a stable and unstable pair.

At the threshold itself, the derivative with respect to x vanishes, so linearization cannot decide the behavior. The equation becomes x-prime equals negative x squared. Positive states move toward zero, while negative states move farther negative. This equilibrium is stable from one side and unstable from the other. The change at mu equals zero is the saddle-node bifurcation.

A saddle-node is not a mysterious discontinuity in the equation. The vector field depends smoothly on mu. What changes discontinuously is the number and arrangement of its equilibria.

### A transcritical exchange of stability

Consider a different equation: x-prime equals mu times x minus x squared. It has two equilibrium branches for every mu: x equals zero and x equals mu. As the parameter passes through zero, the branches cross.

The derivative of the vector field at zero is mu. When mu is negative, the zero equilibrium is stable; when mu is positive, it is unstable. At the other equilibrium, x equals mu, the derivative is negative mu, so the stability is opposite. The two branches exchange their stability as they cross.

This is called a transcritical bifurcation. Compare it with the saddle-node. In a saddle-node, two equilibria appear from none. In a transcritical bifurcation, two branches already exist on both sides and swap stability. Their phase portraits may look similar near a picture of intersecting lines, but the algebra distinguishes them.

### A pitchfork depends on symmetry

Now let the derivative of x be mu times x minus x cubed. This equation is odd in x: changing x to its negative changes the sign of the right-hand side. The system has left-right symmetry.

At negative mu, only x equals zero is an equilibrium, and it is stable. At positive mu, zero becomes unstable and two new equilibria appear at positive and negative square root of mu. Both are stable because the derivative of the vector field there is minus two mu.

The resulting diagram looks like a pitchfork: one central branch splits into two symmetric stable branches. This is a supercritical pitchfork bifurcation. The symmetry explains why the two new branches arise together. Break the exact symmetry by adding a small constant forcing term and the diagram may unfold into a different pattern. A pitchfork usually requires structural conditions; it should not be assumed whenever an equation has a cubic term.

### What is a limit cycle?

In a two-dimensional autonomous system, a periodic orbit is a closed trajectory that repeats after some positive time. A limit cycle is an isolated periodic orbit: there are no other periodic trajectories arbitrarily close to it. This isolation separates a limit cycle from the family of closed energy curves around the center of an ideal undamped pendulum. Those energy curves form a continuum of periodic orbits, so none of the regular closed curves is isolated in that family.

A stable limit cycle attracts neighboring trajectories. It can describe sustained oscillation even when the equilibrium inside it is unstable. An unstable limit cycle repels nearby trajectories. Limit cycles are therefore not merely decorations on phase portraits; they encode self-sustained rhythms and thresholds.

We can construct a clean example by using polar coordinates. Let the radial speed equal mu times the radius minus its cube, and let the angle increase at a constant rate of one radian per unit time. Because the angular speed is constant, any trajectory with constant positive radius is a periodic orbit. The radial equation tells us which radii can remain constant.

When mu is negative, the radius tends toward zero. At mu equal to zero, the radius still decays toward zero, but the decay is slower and the linearized radial rate vanishes. When mu is positive, there are two radial equilibria: radius zero and radius equal to square root of mu. The origin is unstable in the radial direction. The nonzero radius attracts nearby positive radii.

Thus a stable limit cycle appears for positive mu. Its radius grows like the square root of the parameter, and its angular period is two pi. This is the normal-form picture of a supercritical Hopf bifurcation.

### Why the word Hopf needs hypotheses

In the corresponding Cartesian system, the linearization at the origin has eigenvalues mu plus and minus i. At mu equal to zero, they are purely imaginary. For negative mu, the linearized motion spirals inward, and for positive mu it spirals outward. But purely imaginary eigenvalues at a parameter value do not by themselves prove a Hopf bifurcation. We also need conditions ensuring the eigenvalues cross the imaginary axis rather than just touch it, and a nondegeneracy condition controlling the nonlinear terms.

Our polar model explicitly exhibits the nonlinear radial term and therefore makes the conclusion directly calculable. A general theorem uses normal forms and additional hypotheses to transfer this pattern to other systems.

### What a bifurcation diagram leaves out

The diagram of equilibrium locations versus parameter is useful, but it is not a full phase portrait. It may omit how quickly solutions approach an attractor, whether trajectories can escape to infinity, how large the basin of attraction is, or whether other periodic orbits exist far away. Nor does local bifurcation analysis automatically prove global behavior.

The practical method is to combine several levels of reasoning. First solve the equilibrium equations. Next use derivatives to classify hyperbolic equilibria. At parameter values where a derivative vanishes or eigenvalues become imaginary, examine the leading nonlinear terms. For periodic motion, analyze the radial dynamics or, in more complicated systems, a return map that records how trajectories cross a chosen section.

Bifurcation theory is the study of changes in the architecture of motion. Equilibria and cycles need not be solved in closed form to understand their creation and stability. A handful of normal forms already gives a vocabulary for transitions that occur in mechanics, biology, chemical kinetics, and feedback systems.

## Stiff Systems: Fast Transients and Slow Motion

Imagine a physical system that reaches a near-equilibrium state in a fraction of a second but then changes noticeably only over many minutes. A chemical reaction may contain a species that adjusts almost instantly to the concentration of another. An electrical circuit can contain a tiny capacitance whose transient dies away while the overall signal varies slowly. Such systems are natural examples of multiple timescales.

There is a numerical puzzle here. A time-stepping method may need to take extraordinarily small steps, even after the solution has become smooth and slowly varying. Increasing the step size makes the computed values oscillate or explode, although the actual physical motion is perfectly stable. This is a principal symptom of stiffness.

### A two-variable model

Let u decay at rate one. Let v rapidly adjust toward u, at rate one thousand. In words, u-prime is negative u, and v-prime is minus one thousand times the difference between v and u.

The u equation is easy: u decays as e to the negative t. The v equation is a linear forced equation. It has one component that follows the slow decay and another that decays at rate one thousand. With initial values u and v both equal to one, the exact v equals one thousand over nine hundred ninety-nine times e to the negative t, minus one over nine hundred ninety-nine times e to the negative one thousand t.

The rapidly decaying second term nearly disappears after a few thousandths of a time unit. Afterwards v follows the slow component, remaining very close to u. A scientist interested in the trajectory over several seconds would naturally choose a step size based on the slow variation, perhaps tenths of a second. Why might that fail?

### The eigenvalues explain the step restriction

Write the system as a matrix equation. Its two eigenvalues are negative one and negative one thousand. Both indicate stable decay. The slow eigenvalue governs long-term behavior; the fast eigenvalue governs how rapidly deviations toward the slow behavior disappear.

Apply explicit Euler. For a scalar decay with rate one thousand, one step multiplies the value by one minus one thousand times h, where h is the step size. For repeated steps to decay in magnitude, this multiplier must lie strictly between negative one and one. Thus h must be smaller than two thousandths.

A step of one tenth is fifty times too large for this fast component. The numerical method may amplify an error in the fast direction even though the true fast mode decays almost instantly. The actual solution's smooth appearance does not remove the unstable numerical mode. Floating-point rounding, inaccurate starting values, or coupling to the slow component can excite it.

In systems with eigenvalues spread over many orders of magnitude, an explicit stability restriction may therefore be far more severe than the step size required to resolve the behavior of interest. This is not a universal definition that fits every nonlinear problem, but it gives the central intuition of stiffness.

### Solve the new state implicitly

Backward Euler handles the scalar decay equation differently. Instead of evaluating the derivative at the old value, it evaluates the derivative at the unknown new value. For a decay rate of one thousand, the new value equals the old value divided by one plus one thousand h. This multiplier remains between zero and one for every positive h.

For a linear system with matrix A, backward Euler solves a linear system with coefficient matrix identity minus h times A. The new value is determined by an equation, not by a direct evaluation. That requires more work per step, especially for large problems. But when the fast mode would force thousands of explicit steps, a stable implicit step can be economical.

This illustrates a distinction between two words often confused in numerical simulation. Stability asks whether numerical perturbations are suppressed or amplified. Accuracy asks whether the numerical result is close to the desired solution. Backward Euler can be stable for a huge step and still inaccurate. A method may safely damp the fast transient while distorting the slow dynamics if the step is too large.

An implicit method is not automatically adequate for every stiff problem. Backward Euler is A-stable, meaning its linear stability region includes the entire left half of the complex plane. It is also L-stable, meaning its stability multiplier tends to zero for extremely fast decaying modes. The trapezoidal rule is A-stable but not L-stable; for very negative test-equation arguments its multiplier approaches negative one, so fast numerical components can persist as alternating artifacts. This is why the shape of a stability region, and not just the order of the method, matters.

### Fast and slow geometry

There is also a dynamical-systems interpretation. Write the second equation with a small parameter epsilon: epsilon times v-prime equals u minus v. When epsilon is small, v changes quickly whenever it differs from u. On the slower timescale, v stays near a relation determined by the other variables. Setting epsilon equal to zero suggests v equals u, a limiting algebraic constraint rather than a differential equation for v.

But the limiting relation is only a first approximation. For the actual model, the slow solution is v equals one thousand over nine hundred ninety-nine times u, so it differs slightly from u. The tiny difference compensates for the fact that u is itself moving. If we want a more accurate reduced model, we need to account for that drift.

This is the opening idea of singular perturbation and slow-manifold theory. A small parameter multiplying a derivative can change the type of the governing equation when set to zero. Initial conditions may create a thin, fast adjustment period called an initial layer, followed by motion near a lower-dimensional slow set.

Such reductions need hypotheses. Fast dynamics must genuinely attract nearby states in the relevant region, and a proposed slow manifold may lose validity near bifurcations or where timescale separation disappears. Simply deleting a fast variable because it seems unimportant can change the solution qualitatively.

### A numerical experiment worth reasoning through

Suppose we only wish to predict u after one unit of time. The exact answer is e to negative one. In this triangular model, u is unaffected by v, so an explicit solver could integrate u alone without caring about the fast mode. But if we integrate the full coupled system with a naive explicit fixed-step method, the fast eigenvalue still constrains its stable step size. This detail prevents a common overstatement: a stiff subsystem may be irrelevant to a selected output in a special decoupled model, even though it causes trouble for a straightforward full-state integration.

In real models, coupling may make the fast variables essential for the slow evolution, and eliminating them may require more care than it does here. The point of the example is to isolate the stability mechanism, not to claim every stiff system forces the same computational choice.

Stiffness sits at the intersection of mathematical modeling, dynamical systems, and numerical analysis. The equations contain fast decaying directions and slowly evolving behavior. An integrator must respect both the geometry of those directions and the region in which its numerical updates are stable. Good solvers do not simply take smaller steps forever; they choose methods and tolerances that match the structure of the dynamics.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Nonlinear Phase Planes: Energy, Equilibria, and the Pendulum

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order systems, linearization, uniqueness, and elementary mechanics. **Question:** how can we understand the geometry of a nonlinear differential equation without solving it explicitly?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Locate the equilibria of the pendulum. **Answer:** \((k\pi,0)\), for integer \(k\).
2. What distinguishes the energy-two curves? **Answer:** they pass through upright saddles and separate librational from rotational motion.
3. Can an undamped small oscillation be asymptotically stable toward the bottom? **No.** Positive conserved energy cannot decay to zero.
4. Under damping, what is the derivative of \(H\)? **Answer:** \(-\gamma v^2\).

##### Reading

MIT OCW, [Nonlinear Dynamics: Chaos lecture notes](https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/pages/lecture-notes/), lectures on pendulum, phase planes, and dissipation; Steven Strogatz, *Nonlinear Dynamics and Chaos*, phase portraits and conserved quantities.

### Bifurcations and Limit Cycles: When Dynamics Change Their Shape

**Track:** Differential Equations and Dynamical Systems. **Background:** nonlinear vector fields, equilibria, linear stability, and phase portraits. **Question:** what happens when changing a parameter creates new equilibria or a persistent oscillation?

#### Mathematical companion (not spoken)

**Saddle-node.** \(\dot x=\mu-x^2\). For \(\mu>0\), \(x_\pm=\pm\sqrt\mu\) with \(f'(x_+)=-2\sqrt\mu<0\) (stable) and \(f'(x_-)=2\sqrt\mu>0\) (unstable). For \(\mu<0\), no equilibria.

**Transcritical.** \(\dot x=\mu x-x^2=x(\mu-x)\). Equilibria \(x=0,\mu\), with derivatives \(\mu,-\mu\), exchange stability at \(\mu=0\).

**Supercritical pitchfork.** \(\dot x=\mu x-x^3\). At \(\mu<0\), only \(0\) (stable). At \(\mu>0\), \(0\) is unstable and \(\pm\sqrt\mu\) are stable (derivative \(-2\mu\)).

**Supercritical Hopf normal form.** In Cartesian coordinates,
\[
\dot x=\mu x-y-(x^2+y^2)x,\qquad
\dot y=x+\mu y-(x^2+y^2)y.
\]
For \(r>0\), this gives \(\dot r=\mu r-r^3\), \(\dot\theta=1\). At \(\mu>0\), \(r=\sqrt\mu\) is an attracting isolated periodic orbit. It has period \(2\pi\). The eigenvalues of the linearization at the origin are \(\mu\pm i\).

**Qualification.** A generic Hopf theorem requires a nonzero eigenvalue crossing speed and a nonzero first Lyapunov coefficient, alongside smoothness and spectral separation assumptions.

##### Exercises with answers

1. How many equilibria does \(\dot x=-1-x^2\) have? **Answer:** none.
2. For \(\dot x=2x-x^3\), where are stable equilibria? **Answer:** \(x=\pm\sqrt2\).
3. Why are the closed orbits of the undamped linear oscillator not isolated limit cycles? **Answer:** nearby energy levels also give periodic orbits.
4. What is the radius of the stable cycle when \(\mu=9\) in the Hopf normal form? **Answer:** three.

##### Reading

MIT OCW, [Nonlinear Dynamics and Chaos lecture notes](https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2014/pages/lecture-notes/), normal forms and Hopf bifurcations; Steven Strogatz, *Nonlinear Dynamics and Chaos*, bifurcations and limit cycles.

### Stiff Systems: Fast Transients and Slow Motion

**Track:** Differential Equations and Dynamical Systems. **Background:** linear systems, eigenvalues, phase planes, and numerical ODE stability. **Central question:** why can a solution evolve slowly while the equations contain a very fast timescale that cannot be ignored numerically?

#### Mathematical companion (not spoken)

Consider
\[
u'=-u,\qquad v'=-1000(v-u),\qquad u(0)=v(0)=1.
\]
Then \(u(t)=e^{-t}\) and
\[
v(t)=\frac{1000}{999}e^{-t}-\frac1{999}e^{-1000t}.
\]
The coefficient matrix \(A=\begin{psmallmatrix}-1&0\\1000&-1000\end{psmallmatrix}\) has eigenvalues \(-1,-1000\).

**Absolute stability for \(y'=\lambda y\).** Explicit Euler has multiplier \(R_E(z)=1+z\); for \(\lambda=-1000\), stability requires \(0<h<0.002\). Backward Euler has \(R_B(z)=1/(1-z)\) and \(|R_B(z)|\le1\) for \(\Re z\le0\). The trapezoidal rule has \(R_T(z)=(1+z/2)/(1-z/2)\); as \(z\to-\infty\), \(R_T(z)\to-1\), so it is A-stable but not L-stable.

**Fast-slow form.** Setting \(\varepsilon=0.001\) gives \(\varepsilon v'=u-v\), \(u'=-u\). The formal \(\varepsilon\to0\) limit imposes \(v=u\), but the exact attracting slow solution for fixed \(\varepsilon\) satisfies \(v=u/(1-\varepsilon)\) for this model. The initial layer carries the fast exponential term. This reduction should not be confused with an exact identity \(v=u\) at positive epsilon.

##### Exercises with answers

1. What is the explicit-Euler stability bound for \(y'=-500y\)? **Answer:** \(0<h<0.004\).
2. Why does backward Euler not guarantee high accuracy at arbitrary step size? **Answer:** absolute stability bounds amplification, not truncation error.
3. Which fast eigenvalue drives the step restriction in the two-variable example? **Answer:** \(-1000\).
4. What happens to \(R_T(z)\) for large negative real \(z\)? **Answer:** it tends to \(-1\), leaving slowly damped alternating numerical transients.

##### Reading and source notes

- Michael T. Heath, University of Illinois, [Stiff ODEs](https://heath.cs.illinois.edu/iem/ode/stiff/), explicit and implicit stability comparison.
- MIT OCW [Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2004/pages/lecture-notes/), numerical ODE stability.
