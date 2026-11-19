# Entropy shocks, viscous profiles, and nonlinear stability

<!-- BEGIN SPOKEN LECTURE -->

# Entropy shocks, viscous profiles, and nonlinear stability

## Conservation Laws, Shocks, and Entropy Solutions

A traffic jam may begin as a smooth variation in car density. Cars in the denser region move more slowly, and the density profile can sharpen until it resembles a moving wall. Fluid flow can do something similar: smooth initial data develop a discontinuity in finite time. If our equation is written using derivatives, what does it mean after the derivative no longer exists at the jump?

The solution is to take conservation seriously. Rather than insisting that the original differential equation hold pointwise everywhere, we require the integral balance law to hold. This creates weak solutions, which can include shocks. But there is a catch: weak solutions may not be unique. A further entropy condition selects the physically appropriate evolution.

### What conservation says before anything becomes singular

Consider a quantity u that is conserved as it moves along a line. Its flux, written f of u, gives the rate at which it passes through a point. A conservation law states that the time derivative of u plus the spatial derivative of the flux is zero.

The equation means that the total amount inside any interval changes only because of what enters and leaves through the endpoints. For smooth functions, integrate over an interval, apply the fundamental theorem of calculus, and recover the endpoint fluxes. This integral statement remains meaningful even if u has a sudden jump.

A particularly simple model is inviscid Burgers' equation. Here the flux is half the square of u, so the local characteristic speed is u itself. A location with a larger positive value of u moves information faster than one with a smaller value. If the faster part lies behind the slower part, characteristics collide. The smooth description must break down.

### Characteristics predict the collision

For a smooth conservation law, differentiate the flux by the chain rule. Along a curve whose speed equals the derivative of the flux, the value of u is constant. These curves are characteristics. For Burgers' equation, a point carrying value u travels at speed u, as long as the solution remains smooth.

Imagine initial values that decrease from left to right. The characteristics starting on the left travel faster than those on the right. They catch up and attempt to assign different values of u to the same position. A single-valued smooth solution cannot continue this construction beyond the collision.

The failure is not a failure of conservation. The correct continuation may contain a shock: a moving jump with one constant state immediately to its left and another to its right.

### How fast must a shock move?

Take a narrow interval around a moving discontinuity. Apply conservation to that interval, then shrink it toward the jump. The rate at which the jump sweeps through material must exactly balance the difference in flux across it. The result is the Rankine–Hugoniot condition.

In words, shock speed multiplied by the jump in the conserved quantity equals the jump in the flux. For Burgers' equation, this simplifies to shock speed equal to the average of the values on the two sides.

Suppose the left state is three and the right state is one. The shock moves at speed two. The characteristics on the left move at speed three and catch the shock; those on the right move at speed one and are overtaken by the shock. Characteristics converge toward the discontinuity. This is the compressive shock configuration selected by the entropy condition for this convex flux.

The Rankine–Hugoniot condition guarantees conservation across a jump. It does not, by itself, say whether the jump is physically admissible.

### The wrong shock that still conserves

Reverse the arrangement. Suppose the left value is minus one and the right value is plus one. The Rankine–Hugoniot formula gives a stationary jump, because the average speed is zero. That discontinuous function is a weak solution of Burgers' equation.

Yet characteristics move away from the jump on both sides. The left characteristic speed is minus one, and the right characteristic speed is plus one. The jump appears to create a gap in which information emerges from nowhere. The physically selected entropy solution is not the stationary jump. It is a rarefaction fan, a continuous spread of intermediate values whose characteristics fill the gap.

For the chosen states, the rarefaction is minus one to the left of the expanding region, plus one to the right, and position divided by time inside the region. A finite-width fan replaces the inadmissible discontinuity.

This example proves a decisive point. Conservation alone does not ensure uniqueness. Both the stationary expansion shock and the rarefaction satisfy the weak integral equation with the same initial jump data. We need an additional admissibility principle.

### What entropy means here

An entropy pair is a function of the state, often convex, together with a companion flux related by differentiation. Smooth solutions satisfy an additional conservation identity for the entropy. At shocks, physically admissible weak solutions satisfy a one-sided inequality instead. For Burgers' equation the standard family of convex entropies selects compressive shocks and excludes expansion shocks.

The word entropy is broader than thermodynamic disorder in this mathematical setting. It names a family of inequalities that enforce an admissible direction of information flow and select a unique solution class under suitable assumptions. For a scalar conservation law with a sufficiently regular flux, the Kruzhkov entropy framework supplies a well-posed initial-value theory for bounded data.

Another route to the same selection is vanishing viscosity. Add a small positive diffusion term to Burgers' equation. The diffusive equation has a smoothed transition rather than an abrupt shock. As the viscosity tends to zero, suitable solutions converge to the entropy solution of the inviscid equation. The small diffusion has identified which weak limit should be kept.

One must not assume that every numerical method, every regularization, or every system of conservation laws automatically yields the same selection. Scalar convex-flux examples are the clean starting point. Systems can have multiple characteristic families and more complicated shock admissibility conditions.

### Why the weak formulation is stronger than it looks

It may seem that allowing nonsmooth solutions weakens the equation so much that almost anything becomes possible. The opposite is true if we retain the correct structure. The integral conservation law encodes exact flux balance across shocks. The entropy inequalities control which discontinuities are allowed. Together they describe an evolution that a pointwise derivative formula could not express after smoothness fails.

Shocks are not mathematical defects to be erased. They are intrinsic solutions of hyperbolic conservation laws, and the right solution concept is designed to include them. The conceptual move is to preserve the physical conservation principle while replacing classical differentiability by an integral identity plus admissibility conditions.

Entropy conditions select an admissible weak shock. Stability asks whether a nearby evolution stays close to that shock, and viscous profiles provide a model in which we can study that question.

## Nonlinear shock stability and Green-kernel control

### Compressible Fluids and Shock Stability: When Solutions Disagree on Smoothness

Imagine traffic on a single lane. Cars move more slowly as density increases. When a dense region sits behind a light region, the density profile may steepen into a sharp transition. The same mathematical mechanism produces shocks in compressible fluids: waves with different local speeds overtake one another, so a smooth description cannot remain smooth forever.

A conservation law still makes sense after a shock forms. Mass cannot simply disappear at the discontinuity. But conservation alone is not enough to select the correct solution. Several discontinuous functions may satisfy the equation in the weak sense. We need an additional admissibility principle, usually an entropy condition, to distinguish shocks from nonphysical jumps.

The scalar Burgers equation is the most accessible setting for calculating all three ingredients: characteristic crossing, shock speed, and entropy selection. It is not a complete model of compressible gas dynamics, but it reveals why nonlinear conservation laws need more than classical derivatives.

### Characteristics carry information until they collide

Consider an equation in which the time derivative of u plus the spatial derivative of one half u squared equals zero. For a smooth solution, the equation can also be written as the time derivative of u plus u times its spatial derivative equals zero.

Along a characteristic curve moving with speed u, the value of u remains constant. So a point where u is large moves faster than one where u is small. If a larger value lies to the left of a smaller one, the faster left characteristic catches the slower right characteristic. Eventually the characteristics intersect, which would make the classical construction assign two values to the same point.

That does not mean the physical conservation law ceases to operate. It means the solution must be allowed to have a jump. We interpret the PDE weakly, by integrating it against smooth test functions. The jump travels at a speed determined by conservation across the moving interface.

### Rankine–Hugoniot determines speed

Suppose the state immediately to the left of a shock is two, and the state immediately to the right is zero. The flux for Burgers is one half u squared. The left flux is two and the right flux is zero.

The jump condition says that the shock speed times the jump in state equals the jump in flux. Divide the flux difference two by the state difference two: the shock speed is one. Left characteristics travel at speed two and right characteristics at speed zero, so both families run into the moving shock. This compression is exactly what we expect for an admissible shock.

More generally, Burgers gives a shock speed equal to the average of the two states. If the left state is larger than the right, the speed lies between the two characteristic speeds. This is the Lax compressivity condition in this scalar convex-flux example.

### Why a weak solution can be wrong

Reverse the jump: let the left state be zero and the right state be two. The same jump condition would permit a discontinuity traveling at speed one. It satisfies conservation in the distributional sense. But now characteristics on the left move at speed zero and those on the right move at speed two, so they move away from the discontinuity. The jump is trying to pull information out of an empty region between diverging characteristics.

The physically selected solution is instead a rarefaction fan. Between the rays moving at speeds zero and two, the solution is x divided by t. At the left edge it matches zero; at the right edge it matches two. The fan spreads as time increases instead of concentrating into a shock.

This is the clearest demonstration that weak solutions are not unique without additional admissibility conditions. Both the expansion shock and rarefaction satisfy the integral conservation law. The entropy inequality rejects the expansion shock.

### Entropy is not necessarily thermodynamic temperature

For a scalar conservation law, a convex entropy is a convex function of u accompanied by an entropy flux satisfying a compatibility equation with the original flux. Smooth solutions conserve each such entropy. At a shock, the physically admissible weak solution satisfies an inequality: entropy is allowed to dissipate in the mathematically appropriate direction.

For Burgers, one entropy is one half u squared, with the associated flux one third u cubed. Across the compressive shock from two to zero, this entropy inequality holds. Across the reversed discontinuity, it fails. An entropy condition selects the rarefaction instead.

For scalar conservation laws in one dimension, the Kružkov entropy framework gives uniqueness and an L-one contraction principle under standard flux and data hypotheses. Two entropy solutions do not grow farther apart in L-one distance. This gives a meaningful stability concept even when solutions contain shocks.

There is a crucial limit to this statement. It does not automatically carry over to every system of compressible fluid equations, especially in several spatial dimensions. Systems can contain several interacting characteristic families, contact discontinuities and vortices, and their weak-solution theories are substantially harder.

### Compressible Euler adds several waves

The compressible Euler equations conserve mass, momentum and energy. Pressure couples density to motion, so disturbances propagate along characteristic speeds given, in one dimension, by fluid velocity plus or minus sound speed and by the fluid velocity itself.

A Riemann problem starts with two constant states separated by a jump. Its solution can include shocks, rarefaction fans and contact discontinuities. Their arrangement depends on the equation of state and the initial states. The Rankine–Hugoniot conditions constrain every shock, but the admissible wave pattern requires thermodynamic entropy and characteristic information.

For a shock in a hyperbolic system, Lax conditions compare the shock speed with selected characteristic speeds on the two sides. They identify compressive behavior for a given characteristic family, but they are not a universal substitute for nonlinear stability analysis. Undercompressive shocks, phase transitions and other models may use different kinetic selection relations.

### What stability of a shock means

A shock solution is a moving object. Perturb its initial location slightly, and the shock location should shift. We should not demand that the shifted discontinuity remain close pointwise at every fixed spatial coordinate: even a tiny translation of a step function produces a large pointwise difference near the jump.

A useful stability statement must allow translation or modulation of the shock and measure perturbations in an appropriate norm. For scalar entropy solutions, the L-one contraction principle does this remarkably well. For systems, one studies linearized stability, Evans functions, Lopatinski determinants, and nonlinear energy estimates, with assumptions that vary by model.

The word stable has more than one technical meaning. Spectral stability asks whether a linearization has growing modes. Nonlinear orbital stability asks whether nearby solutions remain close to a family of translated shock profiles. Asymptotic stability asks whether the perturbation decays toward an appropriate member of that family. One should not claim the last from the first without the necessary analysis.

### Viscosity and the thin shock layer

Real fluids have viscosity and heat conduction, which smooth ideal discontinuities into thin transition layers. In a vanishing-viscosity limit, those smooth layers can select an entropy solution of the inviscid conservation law. For Burgers, adding a small positive diffusion term creates a regularized PDE whose shock profile has a finite width shrinking with the viscosity.

The limit explains why entropy conditions are physically meaningful rather than arbitrary algebraic restrictions. Nevertheless, not every hyperbolic system has one simple vanishing-viscosity selection theorem independent of how viscosity and boundary conditions are modeled.

The correct lesson is a chain of distinct claims: conservation determines shock speed, entropy selects admissibility, and stability requires its own estimates. A numerical solver that gets only the first claim right can still converge to an inadmissible solution.

### Conservation plus admissibility plus stability

For the jump from two to zero in Burgers, the speed is one and characteristics compress into the discontinuity. Reverse the states and the same speed is allowed by conservation, but entropy replaces the jump with a rarefaction fan. The calculation makes the need for admissibility impossible to overlook.

Compressible fluids inherit these principles and add several interacting wave families. Their shocks may be genuine physical structures, but understanding them means controlling weak formulations, entropy production, boundary and interface conditions, and perturbations. The discontinuity is not where mathematical analysis stops. It is where a more careful kind of analysis begins.

### Viscous Shock Profiles and the Evans Function

A shock in an ideal conservation law is a jump between two states. In a model with viscosity, the jump is replaced by a thin smooth transition layer. As viscosity becomes small, the layer narrows and approaches the discontinuity. Yet that narrow region contains important dynamics. Small perturbations can shift the shock, deform its profile, or in some systems grow into a genuine instability.

The first question is how to find the profile. The second is how to determine whether the profile is stable. The Evans function provides a powerful approach to the second question by translating a spectral boundary-value problem into the zeros of a complex analytic function.

We will start with Burgers' equation because its viscous shock can be written exactly. Then we will explain what survives for systems whose profiles have no closed form.

### A shock you can calculate

Burgers' equation combines transport with diffusion. The local transport speed is the state itself; viscosity smooths gradients. Choose a left state equal to one and a right state equal to negative one. The flux is one half times the square of the state, so both endpoint fluxes are equal. The Rankine-Hugoniot shock speed is therefore zero.

Look for a stationary profile connecting one at negative infinity to negative one at positive infinity. Integrate the profile equation once. The viscous derivative is equal to one half times the square of the profile minus one. The resulting scalar ordinary differential equation has a hyperbolic-tangent solution: negative hyperbolic tangent of position divided by twice the viscosity.

This formula has exactly the desired limits. Far to the left it approaches one; far to the right it approaches negative one. At the center it crosses zero. The derivative is negative, and the transition width is proportional to viscosity. As viscosity tends to zero, the profile approaches the entropy-admissible stationary shock.

Why entropy-admissible? The characteristic speed on the left is one and on the right is negative one, so characteristics flow into the stationary discontinuity from both sides. This is the compressive Lax shock configuration for the scalar convex flux.

### Linearize around the profile

Let the full solution equal the stationary profile plus a small perturbation. Substitute into Burgers' equation and retain the linear terms. The resulting linear operator combines a second spatial derivative from viscosity with the first derivative of the product of the background profile and the perturbation.

Seek perturbations that grow like an exponential in time. The growth rate is a complex number lambda. The spatial shape must solve an eigenvalue equation for the linearized operator. If there is an eigenvalue with positive real part, an exponentially growing linear mode exists and the profile is spectrally unstable.

The neutral case is unavoidable. Translate the shock a small distance. Because the equation is invariant under spatial translations, the shifted profile is also a solution. Differentiating that family with respect to the shift shows that the derivative of the shock profile lies in the kernel of the linearized operator. Lambda equal to zero is therefore a translation eigenvalue or resonance, depending on the chosen function space.

This neutral mode should not be mistaken for a physical instability. A shock displaced slightly in space can remain a shock. Stability must allow for a possible shift in position rather than demanding convergence to the original profile with the exact same center.

### Turning a spectral equation into a dynamical system

The eigenvalue equation for a viscous shock is usually a differential equation in the spatial variable. For systems of conservation laws it can be transformed into a first-order system in space, with coefficients approaching constant matrices as position tends to positive and negative infinity.

At negative infinity, we select solutions that decay as we move toward negative infinity. At positive infinity, we select solutions that decay in the opposite direction. A global eigenfunction exists only when these two families intersect in the middle.

We can transport bases of the stable and unstable spatial subspaces to a common point and take their determinant. With suitable analytic normalizations this determinant is an Evans function. Its zeros correspond to eigenvalues in the region where the construction is valid, including multiplicity under the relevant hypotheses.

This reduces a difficult search over functions to the zeros of a single complex analytic function. It does not make the problem elementary: numerically integrating growing and decaying subspaces without losing accuracy can require exterior products, continuous orthogonalization, or other stabilized representations.

### Counting zeros without finding each one

Suppose the Evans function is analytic on and inside a closed contour in the right half of the complex plane and never vanishes on the contour. As we traverse the contour, its complex argument changes by an integer multiple of two pi. By the argument principle, that integer is the number of zeros inside, counting multiplicity, provided there are no poles.

Thus a winding-number computation can certify that no unstable eigenvalues lie in the enclosed region. For a fully rigorous certificate, we must bound the numerical error and justify that the contour encloses every potentially unstable eigenvalue. A pretty plot of the Evans function is not automatically proof that no zero has been missed.

The translation mode at lambda zero requires special treatment because it lies on the stability boundary. Analysts often factor out its known zero, use integrated coordinates, or deform the contour to avoid it. Different types of shocks can also have essential spectrum touching the imaginary axis, so the phrase spectral gap must be used with care.

### Spectral stability is not yet nonlinear stability

Even if there are no eigenvalues with positive real part, a nonlinear stability theorem requires more. The linearized semigroup must have appropriate bounds; nonlinear terms must be controlled; and the neutral translation direction must be handled by allowing the shock location to modulate.

For scalar Burgers' equation, diffusion and the convex flux provide a favorable setting. For systems such as compressible Navier-Stokes equations, one must verify structural hypotheses involving hyperbolicity, viscosity, the shock family, and low-frequency behavior. Under suitable assumptions, Evans stability can be combined with pointwise Green-function estimates to prove nonlinear orbital stability.

The conclusion often involves algebraic decay toward a translated profile rather than exponential convergence. This is consistent with the diffusive nature of the far-field equations: even a stable linear heat equation on an unbounded line has slow low-frequency modes.

### The precise scope of the method

There are important limitations. The Evans function is not defined by an arbitrary determinant of solutions without analytic normalization. Degenerate shocks may require modified constructions. Embedded eigenvalues or essential spectral effects can complicate the zero count. Multidimensional perturbations introduce transverse Fourier frequencies and additional stability conditions.

Nor does an Evans calculation by itself prove that a viscous profile exists. A profile is a heteroclinic orbit of the traveling-wave ordinary differential equation. Existence and spectral stability are distinct parts of the analysis, even when both use dynamical systems techniques.

The value of the method lies in its separation of concerns. First construct the wave connecting the required endstates. Next linearize and identify the admissible decaying spatial solutions. Then form an analytic determinant, count its unstable zeros, and finally connect spectral information to the nonlinear evolution.

The exact Burgers shock provides a reference calculation. Its profile, translation mode, and characteristic directions are visible by hand. The Evans function extends that reasoning to systems where explicit formulas fail but the structure of the spatial dynamical system remains accessible.

### Pointwise Green Kernels and Nonlinear Viscous-Shock Stability

A viscous shock is a smooth transition between two distinct constant states. It may travel at a fixed speed, but its shape can remain steady in a moving coordinate system. Suppose we perturb such a profile slightly. Even if the perturbation decays, the shock may settle into a copy of itself shifted a little to the left or right.

That behavior is called orbital stability. The solution approaches a family of translates of the shock, not necessarily the original profile at its original coordinate. Translation is an exact symmetry of a spatially homogeneous conservation law, and the stability analysis must respect it.

The difficulty is deeper than a removable zero eigenvalue. For viscous conservation laws on the infinite line, diffusive modes generally cause the essential spectrum of the linearized operator to reach the origin. There may be no spectral gap that lets us apply the simplest exponential-stability theorem. To understand the actual decay and motion of perturbations, we need information about the linearized Green function, often point by point in space and time.

### Burgers' equation gives an exact benchmark

Take viscous Burgers' equation: the time derivative of the velocity plus the spatial derivative of one-half its square equals the second spatial derivative. It is a scalar conservation law with diffusion.

There is a stationary shock connecting the value plus one far to the left to minus one far to the right. Its profile is minus the hyperbolic tangent of half the spatial coordinate. The function falls smoothly through zero and has a transition width of order one in these normalized units.

Differentiate the profile. Its derivative is negative one-half times the square of the hyperbolic secant of half the coordinate. This derivative is localized near the shock center. Now shift the shock slightly. To first order, the difference between the shifted and original profiles is the negative shift multiplied by the profile derivative.

Because every translate is an exact stationary solution, the linearized evolution operator sends the profile derivative to zero. Translation produces a neutral mode. It would be wrong to declare the shock unstable merely because this eigenvalue is not strictly negative, and equally wrong to pretend it is absent.

### Linearization and the Green function

Write the perturbed solution as the shock profile plus a small function v. Keeping the terms linear in v gives an equation with diffusion and a spatially variable transport coefficient determined by the shock. Its operator is the second derivative minus the derivative of the product of the shock profile with v.

The Green function describes how this linearized equation responds to a localized disturbance. For the ordinary heat equation, the Green function is a Gaussian that widens like the square root of time. Its peak falls like one over the square root of time. A viscous shock inherits diffusive features, but also has transport and a distinguished translation component.

Detailed pointwise estimates separate these mechanisms. One part tracks localized signals convected along characteristic directions. Another diffuses. A nondecaying neutral component captures the eventual positional shift of the shock. This decomposition matters because nonlinear perturbations feed back into all of these components.

The spectral Evans function gives information about eigenvalues and their multiplicities, but a spectral count alone does not provide every time-decay estimate. Pointwise Green bounds bridge that gap between spectral conditions and nonlinear behavior.

### Mass predicts the final shift

The Burgers shock example has a useful exact conservation law. Suppose the perturbation is integrable on the line. Integrating the conservation law shows that the spatial integral of the difference between the perturbed solution and the original stationary profile is conserved, under suitable decay assumptions.

Now compare two translated profiles. Shifting a profile with left state plus one and right state minus one by a distance alpha changes the integral of its difference from the original by twice alpha. The statement follows directly from integrating the derivative of the profile.

Consequently, if an integrable perturbation relaxes to a single translated profile and its remaining dispersive part loses mass appropriately, the asymptotic shift is half the initial perturbation mass. This is not merely a fitting parameter from a numerical plot. The conservation law fixes it.

The same simple formula is not universal for systems of conservation laws with several characteristic families or multiple neutral parameters. There one may require a vector of modulation equations and carefully defined projections. The scalar example teaches the mechanism without hiding it in matrix notation.

### Why nonlinear terms can still decay

The exact perturbation equation contains a quadratic remainder, involving the derivative of one-half v squared. A standard approach writes the solution using the linearized semigroup plus an integral of this nonlinear forcing over past times. This is Duhamel's principle.

If the Green function decays in appropriate norms, the integral equation can be used in a bootstrap argument. We assume a smallness-and-decay estimate, use the Green bounds to show the nonlinear term stays controlled, and close the estimate with suitable constants.

Translation must be handled separately. One chooses a time-dependent shock location so that the remaining perturbation is orthogonal to a neutral or adjoint mode, or satisfies an equivalent phase condition. The modulation equation absorbs the persistent translational component. Then the residual can decay, often at diffusion-driven algebraic rates rather than exponentially.

Such a proof needs assumptions on the shock type, the initial perturbation, the coefficient regularity, and the spectral structure. Small amplitude or scalar cases can be more tractable than general large-amplitude systems. An isolated Evans zero is not by itself a nonlinear stability theorem.

### Pointwise estimates reveal where a disturbance travels

Global energy estimates measure the total size of a disturbance. They are excellent for preventing blow-up, but they can hide where a localized signal goes. Pointwise Green bounds resolve the spatial distribution: convective Gaussian pulses, tails near the shock, and the component associated with positional drift.

That extra resolution can improve estimates in different norms and show how a disturbance propagates relative to the moving front. It can also clarify the asymptotic profile, not just an upper bound on its magnitude.

In multiple dimensions, transverse diffusion creates further complications. In systems, several characteristic speeds compete. In undercompressive shocks, the relation between shock location and incoming characteristics differs from the classical Lax case. Methods inspired by pointwise semigroup estimates extend into these regimes only with additional structural conditions.

### A statement worth proving

A rigorous nonlinear shock-stability result should specify a profile, function spaces for perturbations, a norm measuring their smallness, spectral assumptions, and a formula for the phase correction. It should say whether convergence is orbital, what rates are claimed, and whether those rates refer to localized or global norms.

For the normalized Burgers shock, the exact profile and its derivative expose every key feature. The translational mode cannot decay because it corresponds to a symmetry. The diffusive part can decay because viscosity spreads disturbances. Conservation of mass determines the eventual shift. Pointwise Green estimates and nonlinear iteration explain why those facts can coexist.

The lesson reaches far beyond this equation. Stability of a coherent structure often means stability modulo its symmetries. Recognizing those neutral directions is not a weakness in the theorem; it is what makes the theorem mathematically accurate.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Conservation Laws, Shocks, and Entropy Solutions

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives, characteristics, wave propagation, weak PDE solutions. **Central question:** how do conservation laws remain meaningful when smooth solutions develop jumps?

#### Mathematical companion (not spoken)

For \(u_t+f(u)_x=0\), a weak solution with initial data \(u_0\) satisfies, for every smooth compactly supported test function \(\phi\) on space-time including time zero,
\[\int_0^\infty\!\int_{\mathbb R}(u\phi_t+f(u)\phi_x)\,dx\,dt+\int_{\mathbb R}u_0(x)\phi(x,0)\,dx=0.\]
A shock separating \(u_L,u_R\) and moving with speed s satisfies the **Rankine–Hugoniot** condition
\[s(u_R-u_L)=f(u_R)-f(u_L).\]
For Burgers \(f(u)=u^2/2\), \(s=(u_L+u_R)/2\). For a strictly convex flux, the compressive/Lax condition is \(f'(u_L)>s>f'(u_R)\) (for a shock with \(u_L>u_R\)).

For Riemann data \(u_L<u_R\) in Burgers, the entropy solution is the rarefaction
\[u(x,t)=\begin{cases}u_L,&x/t\le u_L,\\x/t,&u_L<x/t<u_R,\\u_R,&x/t\ge u_R.\end{cases}\]
The stationary jump \(u_L=-1,u_R=1\) satisfies Rankine–Hugoniot but violates entropy admissibility. Convex entropy pairs \((\eta,q)\) satisfy \(q'(u)=\eta'(u)f'(u)\), and entropy solutions satisfy \(\eta(u)_t+q(u)_x\le0\) in distributions. Vanishing positive viscosity, \(u_t+f(u)_x=\varepsilon u_{xx}\), selects entropy solutions under standard scalar hypotheses.

##### Exercises with answers

1. Compute shock speed for Burgers with \(u_L=3,u_R=1\). **Answer:** 2.
2. Why does \(u_L=-1,u_R=1\) not have an entropy shock? **Answer:** the characteristics diverge; the entropy solution is a rarefaction fan.
3. Does Rankine–Hugoniot alone guarantee uniqueness? **Answer:** no; expansion shocks can satisfy it but violate entropy conditions.
4. What does the weak formulation retain after differentiability fails? **Answer:** the integral conservation law, including exact flux balance across jumps.

##### Reading and source notes

- Lawrence C. Evans, [*Partial Differential Equations*](https://bookstore.ams.org/gsm-19-r), conservation laws and weak solutions.
- [MIT OpenCourseWare, Advanced Partial Differential Equations](https://ocw.mit.edu/courses/18-306-advanced-partial-differential-equations-with-applications-fall-2009/), hyperbolic equations and shocks.
- [Stanford PDE notes](https://web.stanford.edu/class/math220a/lecturenotes.html), entropy admissibility and scalar conservation laws.

### Nonlinear shock stability and Green-kernel control

### Nonlinear shock stability and Green-kernel control

#### Companions, sources, and study material (not spoken)

##### Compressible Fluids and Shock Stability: When Solutions Disagree on Smoothness

**Track:** Differential Equations and Dynamical Systems. **Background:** conservation laws, characteristics, weak solutions and entropy inequalities. **Central question:** what makes a discontinuity physically admissible and mathematically stable?

###### Mathematical companion (not spoken)

For scalar `u_t+f(u)_x=0` a discontinuity with left/right traces `u_L,u_R` moving at speed s must satisfy Rankine–Hugoniot:
\[
s(u_L-u_R)=f(u_L)-f(u_R).
\]
For Burgers `f(u)=u^2/2`, `s=(u_L+u_R)/2`. The shock from `u_L=2` to `u_R=0` has `s=1` and compressivity `f'(2)=2>s=1>0=f'(0)`. The reversed data `u_L=0,u_R=2` have entropy solution
\[
u(x,t)=\begin{cases}0&x/t\le0,\\x/t&0<x/t<2,\\2&x/t\ge2,\end{cases}\quad t>0,
\]
not a discontinuity of speed one.

For the convex entropy `eta(u)=u^2/2`, `q(u)=u^3/3` and an entropy solution, `eta(u)_t+q(u)_x<=0` in distributions. Across a single jump, the coefficient of its delta distribution is `[q]-s[eta]` for `[a]=a_R-a_L`; admissibility requires this coefficient `<=0`. For the 2-to-0 shock, `[q]=-8/3`, `[eta]=-2`, so `[q]-s[eta]=-2/3<=0`. For the 0-to-2 expansion shock, `[q]=8/3`, `[eta]=2`, giving `2/3>0`, which is forbidden. Scalar L1 contraction for Kružkov entropy solutions does not imply the same theorem for arbitrary multidimensional Euler systems.

##### Exercises with answers

1. Determine Burgers shock speed for left three and right one. **Answer:** `(3+1)/2=2`.
2. Why does the jump from zero to two become a rarefaction? **Answer:** characteristics diverge, and the expansion shock violates the entropy inequality.
3. What makes a weak solution less restrictive than a classical solution? **Answer:** it satisfies an integrated distributional identity and may contain discontinuities.
4. Does a spectrally stable shock automatically converge nonlinearly to a translate of itself? **Answer:** no; nonlinear and asymptotic stability require additional estimates.

##### Reading and source notes

- [Dafermos, Hyperbolic Conservation Laws in Continuum Physics](https://link.springer.com/book/10.1007/978-3-662-49451-6), entropy solutions and shock stability.
- [LeVeque, Numerical Methods for Conservation Laws](https://faculty.washington.edu/rjl/book.html), characteristic, shock and rarefaction calculations.
- [Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), weak solutions and scalar conservation laws.

##### Viscous Shock Profiles and the Evans Function

**Track:** Differential Equations and Dynamical Systems. **Background:** conservation laws, traveling waves, linearized operators, complex analysis, and spectral stability. **Central question:** how can one certify that a smooth viscous shock has no exponentially growing perturbation modes?

###### Mathematical companion (not spoken)

For viscous Burgers,
\[
 u_t+(u^2/2)_x=\nu u_{xx},\quad\nu>0,
\]
the endstates `u_-=1,u_+=-1` have Rankine-Hugoniot speed `s=(f(u_-)-f(u_+))/(u_--u_+)=0`. The profile `U(x)=-tanh(x/(2nu))` satisfies
\[
 \nu U'=(U^2-1)/2,\qquad U(-\infty)=1,\ U(+\infty)=-1.
\]
Set `u=U+v`: the linearized equation is `v_t=Lv`, `Lv=nu v_xx-(U v)_x`. Differentiating the stationary profile equation gives `L U'=0`, the neutral translation mode. In first-order spatial Evans formulations, stable/unstable spatial bases from infinity are matched by an analytic determinant `D(lambda)`. Zeros in the appropriate domain correspond to point spectrum. With contour nonvanishing and analytic hypotheses, `(1/(2pi i)) integral_(boundary Omega) D'/D d lambda` counts zeros. Avoid lambda=0 or remove the translation factor when counting unstable zeros.

For systems, spectral stability alone is **not** a nonlinear theorem: one needs Green-function/semigroup estimates, spectral assumptions, nonlinear control and phase modulation. Essential spectra may touch zero on the unweighted line.

##### Exercises with answers

1. Verify the profile has the required endstates. **Answer:** `-tanh(-infty)=1` and `-tanh(+infty)=-1`.
2. Why does `U'` satisfy `L U'=0`? **Answer:** differentiate the stationary equation with respect to x, reflecting translation invariance.
3. What does a winding number of zero around a valid right-half-plane contour imply? **Answer:** no zeros of the analytic Evans function inside that contour.
4. Does this winding count alone prove nonlinear stability? **Answer:** no; it must be supplemented by appropriate linear decay and nonlinear estimates.

##### Reading and source notes

- [Kevin Zumbrun, Stability and Dynamics of Viscous Shock Waves](https://applications.sciencesmaths-paris.fr/upload/Contenu/Fichiers_chaire/Zumbrun/ima_workshop_proc.pdf), Evans functions and stability mechanisms.
- [Howard and Zumbrun, The Evans Function and Stability Criteria for Degenerate Viscous Shock Waves](https://doi.org/10.3934/dcds.2004.10.837), analytic issues and degenerate shocks.
- [Mascia and Zumbrun, Stability of Small-Amplitude Shock Profiles](https://doi.org/10.1002/cpa.20023), nonlinear orbital stability from spectral and Green-function estimates.

##### Pointwise Green Kernels and Nonlinear Viscous-Shock Stability

**Track:** Differential Equations. **Background:** conservation laws, viscous shock profiles, linearized evolution, and heat kernels. **Central question:** how can a traveling shock be stable when translation creates a neutral direction?

###### Mathematical companion (not spoken)

For Burgers `u_t+(u^2/2)_x=u_xx`, the stationary profile `U(x)=-tanh(x/2)` connects `u_-=1` to `u_+=-1`; it satisfies `U''-U U'=0`. Linearizing `u=U+v` gives
\[
v_t=Lv-\tfrac12(v^2)_x,\qquad Lv=v_{xx}-(Uv)_x.
\]
Differentiating the profile equation proves `LU'=0`. For a translate `U_\alpha(x)=U(x-\alpha)`,
\[
\int_{\mathbb R}(U_\alpha-U)\,dx=-\alpha\int U'\,dx=2\alpha.
\]
Thus if an integrable perturbation of mass `M` converges to a pure translate, the asymptotic phase satisfies `alpha=M/2`. The Green kernel contains a non-decaying translation component and diffusive components. Precise orbital stability and decay rates require specified spectral, localization, and regularity assumptions; no general claim follows merely from `LU'=0`.

##### Exercises with answers

1. What is the neutral eigenfunction of the Burgers shock linearization? **Answer:** `U'`.
2. What would a conserved perturbation mass of `0.4` imply for an asymptotic pure translate? **Answer:** shift `0.2`.
3. Why are algebraic decay rates natural? **Answer:** diffusive essential spectrum can reach zero, as in the heat equation.
4. Does an Evans-function zero count alone establish nonlinear stability? **Answer:** no; semigroup estimates and control of nonlinear terms are additionally needed.

##### Reading and source notes

- [Zumbrun and Howard, Pointwise Semigroup Methods and Stability of Viscous Shock Waves](https://iumj.org/article/459/), Green-function decomposition and nonlinear shock stability.
- [Mascia and Zumbrun, Stability of Small-Amplitude Shock Profiles](https://doi.org/10.1002/cpa.20023), spectral-to-nonlinear orbital stability under structural hypotheses.
