# 008000 — Bifurcations and Limit Cycles: When Dynamics Change Their Shape

**Track:** Differential Equations and Dynamical Systems. **Background:** nonlinear vector fields, equilibria, linear stability, and phase portraits. **Question:** what happens when changing a parameter creates new equilibria or a persistent oscillation?

<!-- BEGIN SPOKEN LECTURE -->

# Bifurcations and Limit Cycles: When Dynamics Change Their Shape

A parameter may change the speed of a dynamical system without changing its basic behavior. But it may also cross a threshold where the geometry of the system changes: equilibria appear or disappear, stability changes hands, or a closed orbit emerges. Such a qualitative change is called a bifurcation.

We can study bifurcations with very small equations. Their simplicity is an advantage. By isolating the essential terms, we can see which conclusions follow from calculus and which depend on additional assumptions.

## A saddle-node creates two equilibria

Start with a scalar equation whose derivative equals a parameter, call it mu, minus the square of the state x. An equilibrium must satisfy x squared equals mu. For negative mu, there is no real equilibrium. At mu equal to zero, there is one equilibrium at x equals zero. For positive mu, two equilibria appear, one positive and one negative.

Stability comes from the derivative of the vector field with respect to x. That derivative is minus two x. At the positive equilibrium it is negative, so nearby states are pushed back toward the equilibrium. At the negative equilibrium it is positive, so nearby states are driven away. The two equilibria form a stable and unstable pair.

At the threshold itself, the derivative with respect to x vanishes, so linearization cannot decide the behavior. The equation becomes x-prime equals negative x squared. Positive states move toward zero, while negative states move farther negative. This equilibrium is stable from one side and unstable from the other. The change at mu equals zero is the saddle-node bifurcation.

A saddle-node is not a mysterious discontinuity in the equation. The vector field depends smoothly on mu. What changes discontinuously is the number and arrangement of its equilibria.

## A transcritical exchange of stability

Consider a different equation: x-prime equals mu times x minus x squared. It has two equilibrium branches for every mu: x equals zero and x equals mu. As the parameter passes through zero, the branches cross.

The derivative of the vector field at zero is mu. When mu is negative, the zero equilibrium is stable; when mu is positive, it is unstable. At the other equilibrium, x equals mu, the derivative is negative mu, so the stability is opposite. The two branches exchange their stability as they cross.

This is called a transcritical bifurcation. Compare it with the saddle-node. In a saddle-node, two equilibria appear from none. In a transcritical bifurcation, two branches already exist on both sides and swap stability. Their phase portraits may look similar near a picture of intersecting lines, but the algebra distinguishes them.

## A pitchfork depends on symmetry

Now let the derivative of x be mu times x minus x cubed. This equation is odd in x: changing x to its negative changes the sign of the right-hand side. The system has left-right symmetry.

At negative mu, only x equals zero is an equilibrium, and it is stable. At positive mu, zero becomes unstable and two new equilibria appear at positive and negative square root of mu. Both are stable because the derivative of the vector field there is minus two mu.

The resulting diagram looks like a pitchfork: one central branch splits into two symmetric stable branches. This is a supercritical pitchfork bifurcation. The symmetry explains why the two new branches arise together. Break the exact symmetry by adding a small constant forcing term and the diagram may unfold into a different pattern. A pitchfork usually requires structural conditions; it should not be assumed whenever an equation has a cubic term.

## What is a limit cycle?

In a two-dimensional autonomous system, a periodic orbit is a closed trajectory that repeats after some positive time. A limit cycle is an isolated periodic orbit: there are no other periodic trajectories arbitrarily close to it. This isolation separates a limit cycle from the family of closed energy curves around the center of an ideal undamped pendulum. Those energy curves form a continuum of periodic orbits, so none of the regular closed curves is isolated in that family.

A stable limit cycle attracts neighboring trajectories. It can describe sustained oscillation even when the equilibrium inside it is unstable. An unstable limit cycle repels nearby trajectories. Limit cycles are therefore not merely decorations on phase portraits; they encode self-sustained rhythms and thresholds.

We can construct a clean example by using polar coordinates. Let the radial speed equal mu times the radius minus its cube, and let the angle increase at a constant rate of one radian per unit time. Because the angular speed is constant, any trajectory with constant positive radius is a periodic orbit. The radial equation tells us which radii can remain constant.

When mu is negative, the radius tends toward zero. At mu equal to zero, the radius still decays toward zero, but the decay is slower and the linearized radial rate vanishes. When mu is positive, there are two radial equilibria: radius zero and radius equal to square root of mu. The origin is unstable in the radial direction. The nonzero radius attracts nearby positive radii.

Thus a stable limit cycle appears for positive mu. Its radius grows like the square root of the parameter, and its angular period is two pi. This is the normal-form picture of a supercritical Hopf bifurcation.

## Why the word Hopf needs hypotheses

In the corresponding Cartesian system, the linearization at the origin has eigenvalues mu plus and minus i. At mu equal to zero, they are purely imaginary. For negative mu, the linearized motion spirals inward, and for positive mu it spirals outward. But purely imaginary eigenvalues at a parameter value do not by themselves prove a Hopf bifurcation. We also need conditions ensuring the eigenvalues cross the imaginary axis rather than just touch it, and a nondegeneracy condition controlling the nonlinear terms.

Our polar model explicitly exhibits the nonlinear radial term and therefore makes the conclusion directly calculable. A general theorem uses normal forms and additional hypotheses to transfer this pattern to other systems.

## What a bifurcation diagram leaves out

The diagram of equilibrium locations versus parameter is useful, but it is not a full phase portrait. It may omit how quickly solutions approach an attractor, whether trajectories can escape to infinity, how large the basin of attraction is, or whether other periodic orbits exist far away. Nor does local bifurcation analysis automatically prove global behavior.

The practical method is to combine several levels of reasoning. First solve the equilibrium equations. Next use derivatives to classify hyperbolic equilibria. At parameter values where a derivative vanishes or eigenvalues become imaginary, examine the leading nonlinear terms. For periodic motion, analyze the radial dynamics or, in more complicated systems, a return map that records how trajectories cross a chosen section.

Bifurcation theory is the study of changes in the architecture of motion. Equilibria and cycles need not be solved in closed form to understand their creation and stability. A handful of normal forms already gives a vocabulary for transitions that occur in mechanics, biology, chemical kinetics, and feedback systems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. How many equilibria does \(\dot x=-1-x^2\) have? **Answer:** none.
2. For \(\dot x=2x-x^3\), where are stable equilibria? **Answer:** \(x=\pm\sqrt2\).
3. Why are the closed orbits of the undamped linear oscillator not isolated limit cycles? **Answer:** nearby energy levels also give periodic orbits.
4. What is the radius of the stable cycle when \(\mu=9\) in the Hopf normal form? **Answer:** three.

### Reading

MIT OCW, [Nonlinear Dynamics and Chaos lecture notes](https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2014/pages/lecture-notes/), normal forms and Hopf bifurcations; Steven Strogatz, *Nonlinear Dynamics and Chaos*, bifurcations and limit cycles.
