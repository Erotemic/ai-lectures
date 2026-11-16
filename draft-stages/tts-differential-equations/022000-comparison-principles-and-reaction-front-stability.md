# 022000 — Reaction Fronts: Comparison Principles and Selected Speeds

**Track:** Differential Equations and Dynamical Systems. **Background:** reaction–diffusion PDEs, traveling waves, linearization, maximum principles. **Central question:** how do local growth and diffusion determine whether a propagating front survives?

<!-- BEGIN SPOKEN LECTURE -->

# Comparison Principles and the Stability of Reaction Fronts

Suppose a population occupies part of a long habitat and gradually invades the empty region beside it. Local reproduction increases population density; diffusion spreads individuals into nearby space. Under suitable assumptions, the boundary between occupied and unoccupied regions moves at a nearly constant speed, forming a traveling front.

A standard model is the Fisher–KPP equation. It has a diffusion term and a logistic reaction term: growth is approximately proportional to density when the population is rare, but decreases as density approaches a carrying capacity. The simple equation already raises three different questions. Does a front-shaped solution exist? How fast can it travel? And if the front is perturbed, does it recover its shape?

Those questions are related but not identical. Finding a wave profile does not prove that an arbitrary initial population approaches that profile. Linear analysis near an empty state can predict a candidate speed, but that calculation alone does not establish the full nonlinear existence theorem.

## Why two constant solutions matter

The logistic reaction has two equilibria: density zero and density one after normalizing carrying capacity. The constant one solution represents the populated state, while zero represents the empty state. With nonnegative initial density at most one, the parabolic comparison principle ensures the solution stays between these two bounds under the usual regularity assumptions.

The comparison principle says that if one solution begins below another and the appropriate differential inequalities hold, their ordering is preserved. For scalar reaction–diffusion equations, this is a powerful replacement for explicit solution formulas. We can build simple upper and lower solutions and trap the true evolution between them.

The principle should not be used indiscriminately on systems of coupled equations. Comparison for scalar parabolic equations relies on order-preserving structure; a multi-species reaction system may lack it unless special quasimonotonicity conditions are satisfied.

## The leading edge selects a speed

Seek a right-moving profile that depends on position minus speed times time. Far ahead of the advancing front, the population is very small. The nonlinear logistic term is then approximately a linear growth term. Suppose the leading edge decays exponentially with distance from the moving front.

Substituting an exponential decay into the linearized equation gives a quadratic relation among the decay rate, the diffusion coefficient, the growth rate, and the speed. For the decay rate to be real and positive, the speed must be at least twice the square root of diffusion times growth.

This is the characteristic minimal speed of a Fisher–KPP front. The algebra is revealing: stronger diffusion spreads the leading edge more quickly, while faster reproduction amplifies the tiny population at that leading edge. Both effects increase the invasion speed.

But we must not elevate the quadratic calculation into a complete theorem by itself. It is a necessary leading-edge condition for a monotone exponential tail. Establishing existence of traveling waves at and above that speed, and excluding waves below it, uses nonlinear ODE and comparison arguments. The equation's special KPP structure matters.

## Building a barrier

An exponential moving profile can also be used as an upper barrier. Choose a speed sufficiently large relative to a positive decay rate. The exponential then satisfies the appropriate supersolution inequality for the logistic PDE. A comparison argument shows that sufficiently localized initial data cannot send a significant amount of population arbitrarily far ahead of such a moving barrier.

By optimizing over the decay rate, we recover the same critical speed. A matching lower-spreading result requires a different construction, using subsolutions and the nonlinear dynamics behind the leading edge. Together the upper and lower results explain why localized nontrivial populations spread asymptotically at the characteristic Fisher–KPP speed.

That statement still needs its assumptions. Initial data with a very slowly decaying tail can select faster propagation, and other reaction laws can support pushed fronts whose speed is not determined solely by the linear growth rate at zero.

## What does front stability mean?

There is one unavoidable complication when asking whether a traveling front is stable. If U of z is a profile, then U of z minus a constant shift is also a profile. The equation does not privilege a particular origin of the moving coordinate. A small perturbation may change the front's position permanently while leaving its shape intact.

Therefore convergence to exactly the original translated profile is generally too strong a demand. A more appropriate notion is orbital stability: the perturbed solution stays near the family of translated fronts, perhaps converging toward a member with a shifted phase.

In spectral language, translation produces a neutral mode. Differentiating the wave profile with respect to its position gives a direction in which the linearized operator has zero eigenvalue. Seeing this zero mode is not a sign that the front is unstable. It reflects a symmetry that must be handled correctly in any stability theorem.

The position of a spreading front can also have slow corrections beyond its leading speed. For the classical Fisher–KPP equation and sufficiently localized initial data, a logarithmic delay appears in the front location. Thus statements about convergence and speed should specify the norm, the reference frame, and the class of initial data.

## The broader method

Reaction fronts appear in combustion, ecology, chemical kinetics, and phase transitions. The same basic tools recur: identify equilibria, construct traveling waves, analyze their leading and trailing edges, use maximum or comparison principles to control solutions, and account for symmetry when defining stability.

Not every medium is scalar, homogeneous, or one-dimensional. Heterogeneous diffusion, systems of reacting species, and nonlocal dispersal can change both the existence theory and the selected speed. Yet the Fisher–KPP model remains a useful training ground because each mathematical mechanism is visible separately.

The key lesson is to resist collapsing three theorems into one. A wave profile exists under specified conditions. A population spreads at a speed under specified initial conditions. And a wave is stable under a specified perturbation notion. Comparison principles, leading-edge analysis, and spectral methods answer different parts of that story.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Consider
\[u_t=D u_{xx}+r u(1-u),\qquad D,r>0,\quad x\in\mathbf R.\]
For bounded regular initial data \(0\le u_0\le1\), the comparison principle with stationary sub/supersolutions 0 and 1 gives \(0\le u(t,x)\le1\). A traveling wave \(u(t,x)=U(z)\), \(z=x-ct\), satisfies
\[D U''+cU'+rU(1-U)=0,\quad U(-\infty)=1,\ U(+\infty)=0.\]
At the leading edge take \(U\sim e^{-\lambda z}\), \(\lambda>0\). The linearized dispersion relation is \(D\lambda^2-c\lambda+r=0\), so a positive real rate requires \(c\ge2\sqrt{Dr}\). For the classical KPP nonlinearity, monotone waves exist for all \(c\ge2\sqrt{Dr}\); rigorous existence is not established by linearization alone.

For \(w=e^{-\lambda(x-ct)}\),
\[w_t-Dw_{xx}-rw(1-w)=(c\lambda-D\lambda^2-r)w+rw^2.\]
Thus if \(c\ge D\lambda+r/\lambda\), w is a positive supersolution; comparison and suitable bounded barriers yield upper-spreading estimates. The minimizer \(\lambda=\sqrt{r/D}\) gives \(c_*=2\sqrt{Dr}\). Linearizing in the moving frame around U yields an operator L with \(L U'=0\) due to translation invariance, so stability is formulated modulo translations. Statements about asymptotic speed, phase shifts, and logarithmic corrections require their own assumptions on initial tails.

### Exercises with answers

1. Compute the minimal wave speed for \(D=4,r=9\). **Answer:** \(2\sqrt{36}=12\).
2. Why does a constant zero solution act as a lower barrier for nonnegative initial data? **Answer:** it solves the PDE and comparison preserves ordering.
3. Explain the zero eigenvalue in the linearization around a wave. **Answer:** translating the wave is a symmetry; its derivative \(U'\) is a neutral direction.
4. Does the dispersion relation alone prove convergence of any initial condition to a wave? **Answer:** no; existence, speed selection, and nonlinear stability are distinct.

### Reading and source notes

- [Classical Fisher–KPP wave theory reviewed in Genetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3914622/), leading-edge analysis and speed selection.
- [Lawrence C. Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), scalar parabolic comparison and maximum principles.
