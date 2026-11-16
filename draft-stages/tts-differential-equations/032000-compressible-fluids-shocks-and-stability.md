# 032000 — Compressible Fluids and Shock Stability: When Solutions Disagree on Smoothness

**Track:** Differential Equations and Dynamical Systems. **Background:** conservation laws, characteristics, weak solutions and entropy inequalities. **Central question:** what makes a discontinuity physically admissible and mathematically stable?

<!-- BEGIN SPOKEN LECTURE -->

# A wave that becomes a wall

Imagine traffic on a single lane. Cars move more slowly as density increases. When a dense region sits behind a light region, the density profile may steepen into a sharp transition. The same mathematical mechanism produces shocks in compressible fluids: waves with different local speeds overtake one another, so a smooth description cannot remain smooth forever.

A conservation law still makes sense after a shock forms. Mass cannot simply disappear at the discontinuity. But conservation alone is not enough to select the correct solution. Several discontinuous functions may satisfy the equation in the weak sense. We need an additional admissibility principle, usually an entropy condition, to distinguish shocks from nonphysical jumps.

The scalar Burgers equation is the most accessible setting for calculating all three ingredients: characteristic crossing, shock speed, and entropy selection. It is not a complete model of compressible gas dynamics, but it reveals why nonlinear conservation laws need more than classical derivatives.

# Characteristics carry information until they collide

Consider an equation in which the time derivative of u plus the spatial derivative of one half u squared equals zero. For a smooth solution, the equation can also be written as the time derivative of u plus u times its spatial derivative equals zero.

Along a characteristic curve moving with speed u, the value of u remains constant. So a point where u is large moves faster than one where u is small. If a larger value lies to the left of a smaller one, the faster left characteristic catches the slower right characteristic. Eventually the characteristics intersect, which would make the classical construction assign two values to the same point.

That does not mean the physical conservation law ceases to operate. It means the solution must be allowed to have a jump. We interpret the PDE weakly, by integrating it against smooth test functions. The jump travels at a speed determined by conservation across the moving interface.

# Rankine–Hugoniot determines speed

Suppose the state immediately to the left of a shock is two, and the state immediately to the right is zero. The flux for Burgers is one half u squared. The left flux is two and the right flux is zero.

The jump condition says that the shock speed times the jump in state equals the jump in flux. Divide the flux difference two by the state difference two: the shock speed is one. Left characteristics travel at speed two and right characteristics at speed zero, so both families run into the moving shock. This compression is exactly what we expect for an admissible shock.

More generally, Burgers gives a shock speed equal to the average of the two states. If the left state is larger than the right, the speed lies between the two characteristic speeds. This is the Lax compressivity condition in this scalar convex-flux example.

# Why a weak solution can be wrong

Reverse the jump: let the left state be zero and the right state be two. The same jump condition would permit a discontinuity traveling at speed one. It satisfies conservation in the distributional sense. But now characteristics on the left move at speed zero and those on the right move at speed two, so they move away from the discontinuity. The jump is trying to pull information out of an empty region between diverging characteristics.

The physically selected solution is instead a rarefaction fan. Between the rays moving at speeds zero and two, the solution is x divided by t. At the left edge it matches zero; at the right edge it matches two. The fan spreads as time increases instead of concentrating into a shock.

This is the clearest demonstration that weak solutions are not unique without additional admissibility conditions. Both the expansion shock and rarefaction satisfy the integral conservation law. The entropy inequality rejects the expansion shock.

# Entropy is not necessarily thermodynamic temperature

For a scalar conservation law, a convex entropy is a convex function of u accompanied by an entropy flux satisfying a compatibility equation with the original flux. Smooth solutions conserve each such entropy. At a shock, the physically admissible weak solution satisfies an inequality: entropy is allowed to dissipate in the mathematically appropriate direction.

For Burgers, one entropy is one half u squared, with the associated flux one third u cubed. Across the compressive shock from two to zero, this entropy inequality holds. Across the reversed discontinuity, it fails. An entropy condition selects the rarefaction instead.

For scalar conservation laws in one dimension, the Kružkov entropy framework gives uniqueness and an L-one contraction principle under standard flux and data hypotheses. Two entropy solutions do not grow farther apart in L-one distance. This gives a meaningful stability concept even when solutions contain shocks.

There is a crucial limit to this statement. It does not automatically carry over to every system of compressible fluid equations, especially in several spatial dimensions. Systems can contain several interacting characteristic families, contact discontinuities and vortices, and their weak-solution theories are substantially harder.

# Compressible Euler adds several waves

The compressible Euler equations conserve mass, momentum and energy. Pressure couples density to motion, so disturbances propagate along characteristic speeds given, in one dimension, by fluid velocity plus or minus sound speed and by the fluid velocity itself.

A Riemann problem starts with two constant states separated by a jump. Its solution can include shocks, rarefaction fans and contact discontinuities. Their arrangement depends on the equation of state and the initial states. The Rankine–Hugoniot conditions constrain every shock, but the admissible wave pattern requires thermodynamic entropy and characteristic information.

For a shock in a hyperbolic system, Lax conditions compare the shock speed with selected characteristic speeds on the two sides. They identify compressive behavior for a given characteristic family, but they are not a universal substitute for nonlinear stability analysis. Undercompressive shocks, phase transitions and other models may use different kinetic selection relations.

# What stability of a shock means

A shock solution is a moving object. Perturb its initial location slightly, and the shock location should shift. We should not demand that the shifted discontinuity remain close pointwise at every fixed spatial coordinate: even a tiny translation of a step function produces a large pointwise difference near the jump.

A useful stability statement must allow translation or modulation of the shock and measure perturbations in an appropriate norm. For scalar entropy solutions, the L-one contraction principle does this remarkably well. For systems, one studies linearized stability, Evans functions, Lopatinski determinants, and nonlinear energy estimates, with assumptions that vary by model.

The word stable has more than one technical meaning. Spectral stability asks whether a linearization has growing modes. Nonlinear orbital stability asks whether nearby solutions remain close to a family of translated shock profiles. Asymptotic stability asks whether the perturbation decays toward an appropriate member of that family. One should not claim the last from the first without the necessary analysis.

# Viscosity and the thin shock layer

Real fluids have viscosity and heat conduction, which smooth ideal discontinuities into thin transition layers. In a vanishing-viscosity limit, those smooth layers can select an entropy solution of the inviscid conservation law. For Burgers, adding a small positive diffusion term creates a regularized PDE whose shock profile has a finite width shrinking with the viscosity.

The limit explains why entropy conditions are physically meaningful rather than arbitrary algebraic restrictions. Nevertheless, not every hyperbolic system has one simple vanishing-viscosity selection theorem independent of how viscosity and boundary conditions are modeled.

The correct lesson is a chain of distinct claims: conservation determines shock speed, entropy selects admissibility, and stability requires its own estimates. A numerical solver that gets only the first claim right can still converge to an inadmissible solution.

# Conservation plus admissibility plus stability

For the jump from two to zero in Burgers, the speed is one and characteristics compress into the discontinuity. Reverse the states and the same speed is allowed by conservation, but entropy replaces the jump with a rarefaction fan. The calculation makes the need for admissibility impossible to overlook.

Compressible fluids inherit these principles and add several interacting wave families. Their shocks may be genuine physical structures, but understanding them means controlling weak formulations, entropy production, boundary and interface conditions, and perturbations. The discontinuity is not where mathematical analysis stops. It is where a more careful kind of analysis begins.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Determine Burgers shock speed for left three and right one. **Answer:** `(3+1)/2=2`.
2. Why does the jump from zero to two become a rarefaction? **Answer:** characteristics diverge, and the expansion shock violates the entropy inequality.
3. What makes a weak solution less restrictive than a classical solution? **Answer:** it satisfies an integrated distributional identity and may contain discontinuities.
4. Does a spectrally stable shock automatically converge nonlinearly to a translate of itself? **Answer:** no; nonlinear and asymptotic stability require additional estimates.

### Reading and source notes

- [Dafermos, Hyperbolic Conservation Laws in Continuum Physics](https://link.springer.com/book/10.1007/978-3-662-49451-6), entropy solutions and shock stability.
- [LeVeque, Numerical Methods for Conservation Laws](https://faculty.washington.edu/rjl/book.html), characteristic, shock and rarefaction calculations.
- [Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), weak solutions and scalar conservation laws.
