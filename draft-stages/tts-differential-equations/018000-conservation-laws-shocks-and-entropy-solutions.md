# 018000 — Conservation Laws, Shocks, and Entropy Solutions

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives, characteristics, wave propagation, weak PDE solutions. **Central question:** how do conservation laws remain meaningful when smooth solutions develop jumps?

<!-- BEGIN SPOKEN LECTURE -->

# Conservation Laws, Shocks, and Entropy Solutions

A traffic jam may begin as a smooth variation in car density. Cars in the denser region move more slowly, and the density profile can sharpen until it resembles a moving wall. Fluid flow can do something similar: smooth initial data develop a discontinuity in finite time. If our equation is written using derivatives, what does it mean after the derivative no longer exists at the jump?

The solution is to take conservation seriously. Rather than insisting that the original differential equation hold pointwise everywhere, we require the integral balance law to hold. This creates weak solutions, which can include shocks. But there is a catch: weak solutions may not be unique. A further entropy condition selects the physically appropriate evolution.

## What conservation says before anything becomes singular

Consider a quantity u that is conserved as it moves along a line. Its flux, written f of u, gives the rate at which it passes through a point. A conservation law states that the time derivative of u plus the spatial derivative of the flux is zero.

The equation means that the total amount inside any interval changes only because of what enters and leaves through the endpoints. For smooth functions, integrate over an interval, apply the fundamental theorem of calculus, and recover the endpoint fluxes. This integral statement remains meaningful even if u has a sudden jump.

A particularly simple model is inviscid Burgers' equation. Here the flux is half the square of u, so the local characteristic speed is u itself. A location with a larger positive value of u moves information faster than one with a smaller value. If the faster part lies behind the slower part, characteristics collide. The smooth description must break down.

## Characteristics predict the collision

For a smooth conservation law, differentiate the flux by the chain rule. Along a curve whose speed equals the derivative of the flux, the value of u is constant. These curves are characteristics. For Burgers' equation, a point carrying value u travels at speed u, as long as the solution remains smooth.

Imagine initial values that decrease from left to right. The characteristics starting on the left travel faster than those on the right. They catch up and attempt to assign different values of u to the same position. A single-valued smooth solution cannot continue this construction beyond the collision.

The failure is not a failure of conservation. The correct continuation may contain a shock: a moving jump with one constant state immediately to its left and another to its right.

## How fast must a shock move?

Take a narrow interval around a moving discontinuity. Apply conservation to that interval, then shrink it toward the jump. The rate at which the jump sweeps through material must exactly balance the difference in flux across it. The result is the Rankine–Hugoniot condition.

In words, shock speed multiplied by the jump in the conserved quantity equals the jump in the flux. For Burgers' equation, this simplifies to shock speed equal to the average of the values on the two sides.

Suppose the left state is three and the right state is one. The shock moves at speed two. The characteristics on the left move at speed three and catch the shock; those on the right move at speed one and are overtaken by the shock. Characteristics converge toward the discontinuity. This is the compressive shock configuration selected by the entropy condition for this convex flux.

The Rankine–Hugoniot condition guarantees conservation across a jump. It does not, by itself, say whether the jump is physically admissible.

## The wrong shock that still conserves

Reverse the arrangement. Suppose the left value is minus one and the right value is plus one. The Rankine–Hugoniot formula gives a stationary jump, because the average speed is zero. That discontinuous function is a weak solution of Burgers' equation.

Yet characteristics move away from the jump on both sides. The left characteristic speed is minus one, and the right characteristic speed is plus one. The jump appears to create a gap in which information emerges from nowhere. The physically selected entropy solution is not the stationary jump. It is a rarefaction fan, a continuous spread of intermediate values whose characteristics fill the gap.

For the chosen states, the rarefaction is minus one to the left of the expanding region, plus one to the right, and position divided by time inside the region. A finite-width fan replaces the inadmissible discontinuity.

This example proves a decisive point. Conservation alone does not ensure uniqueness. Both the stationary expansion shock and the rarefaction satisfy the weak integral equation with the same initial jump data. We need an additional admissibility principle.

## What entropy means here

An entropy pair is a function of the state, often convex, together with a companion flux related by differentiation. Smooth solutions satisfy an additional conservation identity for the entropy. At shocks, physically admissible weak solutions satisfy a one-sided inequality instead. For Burgers' equation the standard family of convex entropies selects compressive shocks and excludes expansion shocks.

The word entropy is broader than thermodynamic disorder in this mathematical setting. It names a family of inequalities that enforce an admissible direction of information flow and select a unique solution class under suitable assumptions. For a scalar conservation law with a sufficiently regular flux, the Kruzhkov entropy framework supplies a well-posed initial-value theory for bounded data.

Another route to the same selection is vanishing viscosity. Add a small positive diffusion term to Burgers' equation. The diffusive equation has a smoothed transition rather than an abrupt shock. As the viscosity tends to zero, suitable solutions converge to the entropy solution of the inviscid equation. The small diffusion has identified which weak limit should be kept.

One must not assume that every numerical method, every regularization, or every system of conservation laws automatically yields the same selection. Scalar convex-flux examples are the clean starting point. Systems can have multiple characteristic families and more complicated shock admissibility conditions.

## Why the weak formulation is stronger than it looks

It may seem that allowing nonsmooth solutions weakens the equation so much that almost anything becomes possible. The opposite is true if we retain the correct structure. The integral conservation law encodes exact flux balance across shocks. The entropy inequalities control which discontinuities are allowed. Together they describe an evolution that a pointwise derivative formula could not express after smoothness fails.

Shocks are not mathematical defects to be erased. They are intrinsic solutions of hyperbolic conservation laws, and the right solution concept is designed to include them. The conceptual move is to preserve the physical conservation principle while replacing classical differentiability by an integral identity plus admissibility conditions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(u_t+f(u)_x=0\), a weak solution with initial data \(u_0\) satisfies, for every smooth compactly supported test function \(\phi\) on space-time including time zero,
\[\int_0^\infty\!\int_{\mathbb R}(u\phi_t+f(u)\phi_x)\,dx\,dt+\int_{\mathbb R}u_0(x)\phi(x,0)\,dx=0.\]
A shock separating \(u_L,u_R\) and moving with speed s satisfies the **Rankine–Hugoniot** condition
\[s(u_R-u_L)=f(u_R)-f(u_L).\]
For Burgers \(f(u)=u^2/2\), \(s=(u_L+u_R)/2\). For a strictly convex flux, the compressive/Lax condition is \(f'(u_L)>s>f'(u_R)\) (for a shock with \(u_L>u_R\)).

For Riemann data \(u_L<u_R\) in Burgers, the entropy solution is the rarefaction
\[u(x,t)=\begin{cases}u_L,&x/t\le u_L,\\x/t,&u_L<x/t<u_R,\\u_R,&x/t\ge u_R.\end{cases}\]
The stationary jump \(u_L=-1,u_R=1\) satisfies Rankine–Hugoniot but violates entropy admissibility. Convex entropy pairs \((\eta,q)\) satisfy \(q'(u)=\eta'(u)f'(u)\), and entropy solutions satisfy \(\eta(u)_t+q(u)_x\le0\) in distributions. Vanishing positive viscosity, \(u_t+f(u)_x=\varepsilon u_{xx}\), selects entropy solutions under standard scalar hypotheses.

### Exercises with answers

1. Compute shock speed for Burgers with \(u_L=3,u_R=1\). **Answer:** 2.
2. Why does \(u_L=-1,u_R=1\) not have an entropy shock? **Answer:** the characteristics diverge; the entropy solution is a rarefaction fan.
3. Does Rankine–Hugoniot alone guarantee uniqueness? **Answer:** no; expansion shocks can satisfy it but violate entropy conditions.
4. What does the weak formulation retain after differentiability fails? **Answer:** the integral conservation law, including exact flux balance across jumps.

### Reading and source notes

- Lawrence C. Evans, [*Partial Differential Equations*](https://bookstore.ams.org/gsm-19-r), conservation laws and weak solutions.
- [MIT OpenCourseWare, Advanced Partial Differential Equations](https://ocw.mit.edu/courses/18-306-advanced-partial-differential-equations-with-applications-fall-2009/), hyperbolic equations and shocks.
- [Stanford PDE notes](https://web.stanford.edu/class/math220a/lecturenotes.html), entropy admissibility and scalar conservation laws.
