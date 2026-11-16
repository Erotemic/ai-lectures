# 037000 - Pointwise Green Kernels and Nonlinear Viscous-Shock Stability

**Track:** Differential Equations. **Background:** conservation laws, viscous shock profiles, linearized evolution, and heat kernels. **Central question:** how can a traveling shock be stable when translation creates a neutral direction?

<!-- BEGIN SPOKEN LECTURE -->

# Stability does not mean returning to the same location

A viscous shock is a smooth transition between two distinct constant states. It may travel at a fixed speed, but its shape can remain steady in a moving coordinate system. Suppose we perturb such a profile slightly. Even if the perturbation decays, the shock may settle into a copy of itself shifted a little to the left or right.

That behavior is called orbital stability. The solution approaches a family of translates of the shock, not necessarily the original profile at its original coordinate. Translation is an exact symmetry of a spatially homogeneous conservation law, and the stability analysis must respect it.

The difficulty is deeper than a removable zero eigenvalue. For viscous conservation laws on the infinite line, diffusive modes generally cause the essential spectrum of the linearized operator to reach the origin. There may be no spectral gap that lets us apply the simplest exponential-stability theorem. To understand the actual decay and motion of perturbations, we need information about the linearized Green function, often point by point in space and time.

# Burgers' equation gives an exact benchmark

Take viscous Burgers' equation: the time derivative of the velocity plus the spatial derivative of one-half its square equals the second spatial derivative. It is a scalar conservation law with diffusion.

There is a stationary shock connecting the value plus one far to the left to minus one far to the right. Its profile is minus the hyperbolic tangent of half the spatial coordinate. The function falls smoothly through zero and has a transition width of order one in these normalized units.

Differentiate the profile. Its derivative is negative one-half times the square of the hyperbolic secant of half the coordinate. This derivative is localized near the shock center. Now shift the shock slightly. To first order, the difference between the shifted and original profiles is the negative shift multiplied by the profile derivative.

Because every translate is an exact stationary solution, the linearized evolution operator sends the profile derivative to zero. Translation produces a neutral mode. It would be wrong to declare the shock unstable merely because this eigenvalue is not strictly negative, and equally wrong to pretend it is absent.

# Linearization and the Green function

Write the perturbed solution as the shock profile plus a small function v. Keeping the terms linear in v gives an equation with diffusion and a spatially variable transport coefficient determined by the shock. Its operator is the second derivative minus the derivative of the product of the shock profile with v.

The Green function describes how this linearized equation responds to a localized disturbance. For the ordinary heat equation, the Green function is a Gaussian that widens like the square root of time. Its peak falls like one over the square root of time. A viscous shock inherits diffusive features, but also has transport and a distinguished translation component.

Detailed pointwise estimates separate these mechanisms. One part tracks localized signals convected along characteristic directions. Another diffuses. A nondecaying neutral component captures the eventual positional shift of the shock. This decomposition matters because nonlinear perturbations feed back into all of these components.

The spectral Evans function gives information about eigenvalues and their multiplicities, but a spectral count alone does not provide every time-decay estimate. Pointwise Green bounds bridge that gap between spectral conditions and nonlinear behavior.

# Mass predicts the final shift

The Burgers shock example has a useful exact conservation law. Suppose the perturbation is integrable on the line. Integrating the conservation law shows that the spatial integral of the difference between the perturbed solution and the original stationary profile is conserved, under suitable decay assumptions.

Now compare two translated profiles. Shifting a profile with left state plus one and right state minus one by a distance alpha changes the integral of its difference from the original by twice alpha. The statement follows directly from integrating the derivative of the profile.

Consequently, if an integrable perturbation relaxes to a single translated profile and its remaining dispersive part loses mass appropriately, the asymptotic shift is half the initial perturbation mass. This is not merely a fitting parameter from a numerical plot. The conservation law fixes it.

The same simple formula is not universal for systems of conservation laws with several characteristic families or multiple neutral parameters. There one may require a vector of modulation equations and carefully defined projections. The scalar example teaches the mechanism without hiding it in matrix notation.

# Why nonlinear terms can still decay

The exact perturbation equation contains a quadratic remainder, involving the derivative of one-half v squared. A standard approach writes the solution using the linearized semigroup plus an integral of this nonlinear forcing over past times. This is Duhamel's principle.

If the Green function decays in appropriate norms, the integral equation can be used in a bootstrap argument. We assume a smallness-and-decay estimate, use the Green bounds to show the nonlinear term stays controlled, and close the estimate with suitable constants.

Translation must be handled separately. One chooses a time-dependent shock location so that the remaining perturbation is orthogonal to a neutral or adjoint mode, or satisfies an equivalent phase condition. The modulation equation absorbs the persistent translational component. Then the residual can decay, often at diffusion-driven algebraic rates rather than exponentially.

Such a proof needs assumptions on the shock type, the initial perturbation, the coefficient regularity, and the spectral structure. Small amplitude or scalar cases can be more tractable than general large-amplitude systems. An isolated Evans zero is not by itself a nonlinear stability theorem.

# Pointwise estimates reveal where a disturbance travels

Global energy estimates measure the total size of a disturbance. They are excellent for preventing blow-up, but they can hide where a localized signal goes. Pointwise Green bounds resolve the spatial distribution: convective Gaussian pulses, tails near the shock, and the component associated with positional drift.

That extra resolution can improve estimates in different norms and show how a disturbance propagates relative to the moving front. It can also clarify the asymptotic profile, not just an upper bound on its magnitude.

In multiple dimensions, transverse diffusion creates further complications. In systems, several characteristic speeds compete. In undercompressive shocks, the relation between shock location and incoming characteristics differs from the classical Lax case. Methods inspired by pointwise semigroup estimates extend into these regimes only with additional structural conditions.

# A statement worth proving

A rigorous nonlinear shock-stability result should specify a profile, function spaces for perturbations, a norm measuring their smallness, spectral assumptions, and a formula for the phase correction. It should say whether convergence is orbital, what rates are claimed, and whether those rates refer to localized or global norms.

For the normalized Burgers shock, the exact profile and its derivative expose every key feature. The translational mode cannot decay because it corresponds to a symmetry. The diffusive part can decay because viscosity spreads disturbances. Conservation of mass determines the eventual shift. Pointwise Green estimates and nonlinear iteration explain why those facts can coexist.

The lesson reaches far beyond this equation. Stability of a coherent structure often means stability modulo its symmetries. Recognizing those neutral directions is not a weakness in the theorem; it is what makes the theorem mathematically accurate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For Burgers `u_t+(u^2/2)_x=u_xx`, the stationary profile `U(x)=-tanh(x/2)` connects `u_-=1` to `u_+=-1`; it satisfies `U''-U U'=0`. Linearizing `u=U+v` gives
\[
v_t=Lv-\tfrac12(v^2)_x,\qquad Lv=v_{xx}-(Uv)_x.
\]
Differentiating the profile equation proves `LU'=0`. For a translate `U_\alpha(x)=U(x-\alpha)`,
\[
\int_{\mathbb R}(U_\alpha-U)\,dx=-\alpha\int U'\,dx=2\alpha.
\]
Thus if an integrable perturbation of mass `M` converges to a pure translate, the asymptotic phase satisfies `alpha=M/2`. The Green kernel contains a non-decaying translation component and diffusive components. Precise orbital stability and decay rates require specified spectral, localization, and regularity assumptions; no general claim follows merely from `LU'=0`.

### Exercises with answers

1. What is the neutral eigenfunction of the Burgers shock linearization? **Answer:** `U'`.
2. What would a conserved perturbation mass of `0.4` imply for an asymptotic pure translate? **Answer:** shift `0.2`.
3. Why are algebraic decay rates natural? **Answer:** diffusive essential spectrum can reach zero, as in the heat equation.
4. Does an Evans-function zero count alone establish nonlinear stability? **Answer:** no; semigroup estimates and control of nonlinear terms are additionally needed.

### Reading and source notes

- [Zumbrun and Howard, Pointwise Semigroup Methods and Stability of Viscous Shock Waves](https://iumj.org/article/459/), Green-function decomposition and nonlinear shock stability.
- [Mascia and Zumbrun, Stability of Small-Amplitude Shock Profiles](https://doi.org/10.1002/cpa.20023), spectral-to-nonlinear orbital stability under structural hypotheses.
