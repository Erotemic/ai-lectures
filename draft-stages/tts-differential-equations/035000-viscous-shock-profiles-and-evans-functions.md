# 035000 - Viscous Shock Profiles and the Evans Function

**Track:** Differential Equations and Dynamical Systems. **Background:** conservation laws, traveling waves, linearized operators, complex analysis, and spectral stability. **Central question:** how can one certify that a smooth viscous shock has no exponentially growing perturbation modes?

<!-- BEGIN SPOKEN LECTURE -->

# A discontinuity with internal structure

A shock in an ideal conservation law is a jump between two states. In a model with viscosity, the jump is replaced by a thin smooth transition layer. As viscosity becomes small, the layer narrows and approaches the discontinuity. Yet that narrow region contains important dynamics. Small perturbations can shift the shock, deform its profile, or in some systems grow into a genuine instability.

The first question is how to find the profile. The second is how to determine whether the profile is stable. The Evans function provides a powerful approach to the second question by translating a spectral boundary-value problem into the zeros of a complex analytic function.

We will start with Burgers' equation because its viscous shock can be written exactly. Then we will explain what survives for systems whose profiles have no closed form.

# A shock you can calculate

Burgers' equation combines transport with diffusion. The local transport speed is the state itself; viscosity smooths gradients. Choose a left state equal to one and a right state equal to negative one. The flux is one half times the square of the state, so both endpoint fluxes are equal. The Rankine-Hugoniot shock speed is therefore zero.

Look for a stationary profile connecting one at negative infinity to negative one at positive infinity. Integrate the profile equation once. The viscous derivative is equal to one half times the square of the profile minus one. The resulting scalar ordinary differential equation has a hyperbolic-tangent solution: negative hyperbolic tangent of position divided by twice the viscosity.

This formula has exactly the desired limits. Far to the left it approaches one; far to the right it approaches negative one. At the center it crosses zero. The derivative is negative, and the transition width is proportional to viscosity. As viscosity tends to zero, the profile approaches the entropy-admissible stationary shock.

Why entropy-admissible? The characteristic speed on the left is one and on the right is negative one, so characteristics flow into the stationary discontinuity from both sides. This is the compressive Lax shock configuration for the scalar convex flux.

# Linearize around the profile

Let the full solution equal the stationary profile plus a small perturbation. Substitute into Burgers' equation and retain the linear terms. The resulting linear operator combines a second spatial derivative from viscosity with the first derivative of the product of the background profile and the perturbation.

Seek perturbations that grow like an exponential in time. The growth rate is a complex number lambda. The spatial shape must solve an eigenvalue equation for the linearized operator. If there is an eigenvalue with positive real part, an exponentially growing linear mode exists and the profile is spectrally unstable.

The neutral case is unavoidable. Translate the shock a small distance. Because the equation is invariant under spatial translations, the shifted profile is also a solution. Differentiating that family with respect to the shift shows that the derivative of the shock profile lies in the kernel of the linearized operator. Lambda equal to zero is therefore a translation eigenvalue or resonance, depending on the chosen function space.

This neutral mode should not be mistaken for a physical instability. A shock displaced slightly in space can remain a shock. Stability must allow for a possible shift in position rather than demanding convergence to the original profile with the exact same center.

# Turning a spectral equation into a dynamical system

The eigenvalue equation for a viscous shock is usually a differential equation in the spatial variable. For systems of conservation laws it can be transformed into a first-order system in space, with coefficients approaching constant matrices as position tends to positive and negative infinity.

At negative infinity, we select solutions that decay as we move toward negative infinity. At positive infinity, we select solutions that decay in the opposite direction. A global eigenfunction exists only when these two families intersect in the middle.

We can transport bases of the stable and unstable spatial subspaces to a common point and take their determinant. With suitable analytic normalizations this determinant is an Evans function. Its zeros correspond to eigenvalues in the region where the construction is valid, including multiplicity under the relevant hypotheses.

This reduces a difficult search over functions to the zeros of a single complex analytic function. It does not make the problem elementary: numerically integrating growing and decaying subspaces without losing accuracy can require exterior products, continuous orthogonalization, or other stabilized representations.

# Counting zeros without finding each one

Suppose the Evans function is analytic on and inside a closed contour in the right half of the complex plane and never vanishes on the contour. As we traverse the contour, its complex argument changes by an integer multiple of two pi. By the argument principle, that integer is the number of zeros inside, counting multiplicity, provided there are no poles.

Thus a winding-number computation can certify that no unstable eigenvalues lie in the enclosed region. For a fully rigorous certificate, we must bound the numerical error and justify that the contour encloses every potentially unstable eigenvalue. A pretty plot of the Evans function is not automatically proof that no zero has been missed.

The translation mode at lambda zero requires special treatment because it lies on the stability boundary. Analysts often factor out its known zero, use integrated coordinates, or deform the contour to avoid it. Different types of shocks can also have essential spectrum touching the imaginary axis, so the phrase spectral gap must be used with care.

# Spectral stability is not yet nonlinear stability

Even if there are no eigenvalues with positive real part, a nonlinear stability theorem requires more. The linearized semigroup must have appropriate bounds; nonlinear terms must be controlled; and the neutral translation direction must be handled by allowing the shock location to modulate.

For scalar Burgers' equation, diffusion and the convex flux provide a favorable setting. For systems such as compressible Navier-Stokes equations, one must verify structural hypotheses involving hyperbolicity, viscosity, the shock family, and low-frequency behavior. Under suitable assumptions, Evans stability can be combined with pointwise Green-function estimates to prove nonlinear orbital stability.

The conclusion often involves algebraic decay toward a translated profile rather than exponential convergence. This is consistent with the diffusive nature of the far-field equations: even a stable linear heat equation on an unbounded line has slow low-frequency modes.

# The precise scope of the method

There are important limitations. The Evans function is not defined by an arbitrary determinant of solutions without analytic normalization. Degenerate shocks may require modified constructions. Embedded eigenvalues or essential spectral effects can complicate the zero count. Multidimensional perturbations introduce transverse Fourier frequencies and additional stability conditions.

Nor does an Evans calculation by itself prove that a viscous profile exists. A profile is a heteroclinic orbit of the traveling-wave ordinary differential equation. Existence and spectral stability are distinct parts of the analysis, even when both use dynamical systems techniques.

The value of the method lies in its separation of concerns. First construct the wave connecting the required endstates. Next linearize and identify the admissible decaying spatial solutions. Then form an analytic determinant, count its unstable zeros, and finally connect spectral information to the nonlinear evolution.

The exact Burgers shock provides a reference calculation. Its profile, translation mode, and characteristic directions are visible by hand. The Evans function extends that reasoning to systems where explicit formulas fail but the structure of the spatial dynamical system remains accessible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Verify the profile has the required endstates. **Answer:** `-tanh(-infty)=1` and `-tanh(+infty)=-1`.
2. Why does `U'` satisfy `L U'=0`? **Answer:** differentiate the stationary equation with respect to x, reflecting translation invariance.
3. What does a winding number of zero around a valid right-half-plane contour imply? **Answer:** no zeros of the analytic Evans function inside that contour.
4. Does this winding count alone prove nonlinear stability? **Answer:** no; it must be supplemented by appropriate linear decay and nonlinear estimates.

### Reading and source notes

- [Kevin Zumbrun, Stability and Dynamics of Viscous Shock Waves](https://applications.sciencesmaths-paris.fr/upload/Contenu/Fichiers_chaire/Zumbrun/ima_workshop_proc.pdf), Evans functions and stability mechanisms.
- [Howard and Zumbrun, The Evans Function and Stability Criteria for Degenerate Viscous Shock Waves](https://doi.org/10.3934/dcds.2004.10.837), analytic issues and degenerate shocks.
- [Mascia and Zumbrun, Stability of Small-Amplitude Shock Profiles](https://doi.org/10.1002/cpa.20023), nonlinear orbital stability from spectral and Green-function estimates.
