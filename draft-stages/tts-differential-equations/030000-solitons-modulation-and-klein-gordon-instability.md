# 030000 — Solitons and Modulation: A Klein–Gordon Wave that Can Become Unstable

**Track:** Differential Equations. **Background:** semilinear wave equations, conserved energies, Sturm–Liouville theory, and linearization. **Central question:** how can a localized stationary wave be both an exact nonlinear solution and unstable under small perturbations?

<!-- BEGIN SPOKEN LECTURE -->

# A wave that stays in one place

Many wave equations spread disturbances across space. But some nonlinear equations admit localized shapes that persist without dispersing. These structures are called solitary waves. They can travel at a constant speed or remain stationary in a suitable reference frame.

The existence of an exact localized shape does not automatically mean that the shape is stable. A pencil balanced on its tip is an exact equilibrium, but small perturbations can move it away. Nonlinear waves can have the same distinction between existence and stability, and their geometry is often more subtle because shifts in position create a whole family of equivalent solutions.

We will study an explicit example from a one-dimensional focusing cubic Klein–Gordon equation. The special feature is that we can write down its stationary wave, its linearized operator, and even an exponentially growing perturbation mode using elementary functions.

# A nonlinear Klein–Gordon equation

The equation has a second time derivative, a negative second spatial derivative, a linear restoring term, and a cubic focusing term. The cubic term has the sign that competes with the linear restoring force rather than strengthening it.

To find a stationary wave, set the time derivatives to zero. We obtain an ordinary differential equation for the spatial profile. We want a smooth function that approaches zero as the spatial coordinate tends to either positive or negative infinity.

A remarkable solution is the square root of two times the hyperbolic secant of the spatial coordinate. The hyperbolic secant is the reciprocal of the hyperbolic cosine, so it has a bell shape. It is largest at zero and decays exponentially in both directions.

Substitute this profile into the stationary differential equation, differentiate twice, and the terms cancel exactly. Thus this wave is not a numerical approximation or a perturbative guess. It is an exact nonlinear stationary solution on the whole real line.

# Translation produces a neutral direction

The equation is unchanged if we shift the spatial coordinate. If the bell-shaped profile centered at zero is a stationary solution, then the same profile centered at any other position is also a stationary solution.

Differentiate this family with respect to the center position. The result is proportional to the spatial derivative of the profile. It turns out to lie in the kernel of the linearized spatial operator.

This zero eigenvalue is geometrically necessary. A tiny shift of the center does not represent the same kind of departure as a deformation that changes the shape. It simply moves us along a family of exact solutions. Any stability analysis should recognize that neutral symmetry direction rather than treating it as a decay failure.

# Linearize the equation

Now perturb the stationary solution by adding a small function of time and space. Expand the cubic nonlinearity and retain only terms linear in that perturbation. We get a second-order evolution equation with a spatial Schrödinger-type operator.

That operator is minus the second spatial derivative plus one, minus three times the square of our stationary profile. Because the profile is the square root of two times the hyperbolic secant, the potential is one minus six times the square of the hyperbolic secant.

One eigenfunction is the spatial derivative of the profile, with eigenvalue zero. But there is another important eigenfunction: the square of the hyperbolic secant. Substitution shows that its eigenvalue is negative three.

A negative spatial eigenvalue produces a very different time behavior. Along that eigenfunction, the linearized wave amplitude satisfies an ordinary differential equation whose second derivative is three times the amplitude. Its solutions include an exponential growing like the exponential of the square root of three times time.

This is a genuine linear instability mode. Small perturbations with a component in that direction grow rather than disperse. The existence of the stationary wave does not protect it from that growth.

# Why simply tracking the center is not enough

A common way to study solitary waves is called modulation. We allow the center of the profile to depend slowly on time and write the actual solution as a shifted profile plus a remainder. We then impose an orthogonality condition on the remainder so that the decomposition selects a unique center, at least while the solution remains close to the family.

For our example, we can require the remainder to be orthogonal to the translation mode, the spatial derivative of the profile. This removes the ambiguity of whether a small difference came from an actual shape change or just a slight shift.

But the orthogonality condition does not remove the unstable eigenfunction. The unstable mode is distinct from the translation mode. Therefore modulation of the center alone is insufficient to prove that every nearby solution remains near the solitary wave forever.

A full dynamical analysis may require restricting initial data to a stable or center-stable manifold, accounting for the unstable direction, and controlling the nonlinear remainder. Different nonlinear equations can have solitary waves with very different spectral structures.

# Energy is conserved but instability remains

This Klein–Gordon equation has a conserved energy combining kinetic energy, spatial-gradient energy, a positive quadratic potential term, and a negative quartic potential term.

The negative quartic contribution is characteristic of the focusing case. It means that the energy is not globally a positive quadratic measure of distance from the origin or from the solitary wave. Conservation of this energy does not imply that every perturbation is controlled by a positive norm.

Near a stationary solution, the second variation of the energy is related to the linearized operator. A negative direction in this quadratic form is an indication of a potential instability, and in this explicit example the negative eigenvalue produces an actual exponentially growing linear mode.

# What the example teaches

This single model separates several statements that are often compressed into the word stable. A solitary wave exists exactly. Translation symmetry supplies a zero mode. The linearized operator supplies a negative mode. Modulation can account for the neutral shift without eliminating the unstable growth.

The resulting picture is more informative than simply saying nonlinear waves can form solitons. It tells us what must be examined to predict their behavior: conserved quantities, the spectrum of the linearized operator, the symmetry modes, and the nonlinear coupling among them. An exact coherent shape is only the beginning of the stability question.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Consider the focusing cubic Klein–Gordon equation on R:
\[
u_{tt}-u_{xx}+u-u^3=0.
\]
Its stationary profile `Q(x)=sqrt(2) sech(x)` satisfies `-Q''+Q-Q^3=0`, or equivalently `Q''=Q-Q^3`. The translated profiles `Q(x-y)` are also stationary.

Write `u=Q+eta`. Linearization yields `eta_tt+L eta = nonlinear higher-order terms`, where
\[
L=-\partial_x^2+1-3Q^2=-\partial_x^2+1-6\operatorname{sech}^2 x.
\]
Differentiating the stationary equation gives `L Q'=0`. Direct differentiation also gives
\[
L(\operatorname{sech}^2 x)=-3\operatorname{sech}^2 x.
\]
Thus a linear perturbation `eta(t,x)=a(t)sech^2(x)` obeys `a''-3a=0` and has a growing solution `a(t)=exp(sqrt(3)*t)`. The negative eigenvalue is a *linear instability*, not a theorem that every small nonlinear perturbation blows up.

The conserved energy for sufficiently regular decaying solutions is
\[
\mathcal E(u,u_t)=\int_\mathbb R\left[\tfrac12 u_t^2+\tfrac12 u_x^2+
\tfrac12 u^2-\tfrac14 u^4\right]dx.
\]
A modulated decomposition is `u(t,x)=Q(x-y(t))+eta(t,x)` with orthogonality `int eta(t,x) Q'(x-y(t)) dx=0`. Fixing the translation coordinate does not remove the negative eigendirection. For this explicit operator the unique negative discrete eigenvalue is -3, the zero eigenvalue corresponds to translation, and the continuous spectrum starts at 1, under the usual L2 realization.

### Exercises with answers

1. Verify the stationary equation from `Q''=Q-Q^3`. **Answer:** substitute to obtain `-Q''+Q-Q^3=0`.
2. Why is `Q'` a zero eigenfunction? **Answer:** differentiate the stationary profile equation with respect to x.
3. Solve `a''-3a=0`. **Answer:** `a(t)=A e^(sqrt(3)t)+B e^(-sqrt(3)t)`.
4. Does an orthogonality condition against Q' remove an unstable sech-squared mode? **Answer:** no; the two modes correspond to different eigenvalues and the negative mode must be controlled separately.

### Reading and source notes

- [The Cubic Klein–Gordon Equation with Damping (lecture notes)](https://lmv.math.cnrs.fr/wp-content/uploads/2025/02/M2_2025.pdf), explicit profile, linearized spectral structure and modulation estimates.
- [Terence Tao, PDE preprints on wave and dispersive equations](https://www.math.ucla.edu/~tao/preprints/pde.html), nonlinear Klein–Gordon dynamics and stability contexts.
- [Keel and Tao, Endpoint Strichartz Estimates](https://doi.org/10.1353/ajm.1998.0039), tools for perturbative dispersive analysis beyond the elementary spectral model.
