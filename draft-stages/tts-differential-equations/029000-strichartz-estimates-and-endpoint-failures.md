# 029000 — Strichartz Estimates: Measuring the Spreading of Waves

**Track:** Differential Equations. **Background:** Fourier analysis, Sobolev norms, linear wave equations, and energy estimates. **Central question:** how can dispersion give bounds on a wave over both space and time that energy conservation alone does not provide?

<!-- BEGIN SPOKEN LECTURE -->

# The wave spreads but its energy remains

Imagine striking a small drum or disturbing the surface of a pond. A disturbance moves away from its origin. At any one location its amplitude may weaken as the disturbance spreads across a larger region, even while the total energy of the system remains conserved.

There are two kinds of mathematical statement hidden in that picture. Energy conservation controls a spatial norm at each time. Dispersion concerns the way a solution is distributed across both space and time. The second kind of control is often essential when the wave equation contains a nonlinear forcing term.

Strichartz estimates are inequalities that measure the spreading of free waves in combined time-and-space norms. They are particularly valuable because they allow a nonlinear problem to be treated as a perturbation of its linear counterpart, without asking that the solution remain pointwise small everywhere.

# Separate energy from space-time integrability

Consider a free wave in three-dimensional space. Its displacement depends on time and three spatial coordinates, and it satisfies the equation in which the second time derivative equals the spatial Laplacian.

The conserved energy is the integral of the squares of the time derivative and spatial gradient. If the initial energy is finite, it remains constant. This is a powerful stability statement, but it does not by itself measure how many times the solution can be large in a particular space-time region.

A Strichartz estimate instead combines a spatial norm with a time norm. For example, we might take the fourth power of the solution, integrate over all space and all time, and then take the fourth root. This asks whether the wave can persistently concentrate in space-time, not just whether its derivative energy is bounded at each instant.

# Why dimension matters

The rate at which waves disperse depends on the number of spatial dimensions. In three dimensions, the propagation is concentrated near expanding spherical shells. In one dimension, left-moving and right-moving waves can retain their shapes without the same kind of geometric spreading. The estimates therefore differ with dimension.

They also depend on which frequency derivatives of the initial data are controlled. When an equation is invariant under rescaling, we can calculate what derivative order a proposed inequality must require. A bound with the wrong scaling cannot be true with a constant independent of the data scale.

For the three-dimensional free wave, an important estimate controls the fourth-power space-time norm of displacement using one half of a derivative of the initial displacement and minus one half of a derivative of the initial velocity, in the appropriate homogeneous Sobolev norms.

This may sound strange. Why a negative derivative on velocity? Because velocity enters the free-wave formula divided by the magnitude of frequency. The exponents track exactly how the two pieces of Cauchy data generate a solution at the same scaling level.

# What the Fourier formula reveals

A free wave can be decomposed into two traveling frequency components, one oscillating forward in time and the other backward. The Fourier multiplier for these components has an oscillatory phase tied to the magnitude of spatial frequency.

When we integrate such oscillations, many frequencies cancel. This cancellation is the analytic source of dispersive decay. More systematic arguments combine dispersive estimates with conservation in square-integrable norms and a duality method, often called T T star.

The resulting family of Strichartz estimates permits several combinations of time and space exponents. They obey an admissibility condition that reflects the geometry of the wave cone. For the three-dimensional wave, the pair consisting of fourth power in time and fourth power in space is admissible.

# Why an endpoint can fail

It is tempting to keep strengthening one exponent until the spatial norm becomes an essential supremum. One might hope to control a wave in the square-integrable time norm of its spatial maximum using just the scaling-predicted Sobolev norms of the initial data.

For the general three-dimensional free wave, that endpoint pair, square-integrable in time and essentially bounded in space, fails as a standard global Strichartz estimate. Certain waves can concentrate along directions strongly enough to defeat it. The problem is not a missing constant in a proof; the proposed bound is false without additional conditions.

There are special situations, for example particular radial data or modified function spaces, where related stronger estimates can hold. Those are distinct theorems. An endpoint failure in the general theorem should not be silently repaired by adding an assumption that was never stated.

# How nonlinear equations use the estimate

A semilinear wave equation has the same linear propagation on its left side but adds a nonlinear term depending on the solution. We can rewrite it using Duhamel's principle: the solution is the free evolution of its initial data plus the linear propagation of forcing produced at earlier times.

The strategy for proving local existence is to choose a space-time function space in which the nonlinear forcing can be estimated. A Strichartz inequality controls the linear propagator in that space. If the nonlinear map is locally Lipschitz there and the relevant norm is small on a short time interval, a fixed-point argument may construct a solution.

Every step needs the right exponents. The nonlinear power, the spatial dimension, the Sobolev regularity, and the interval length determine whether the contraction works. An estimate for one admissible pair is not an all-purpose guarantee of global existence, and a local solution need not scatter as time tends to infinity.

# Three different conclusions

Energy conservation bounds a quantity at every time. Strichartz estimates control integrated space-time behavior and can support perturbative nonlinear analysis. Scattering is a further conclusion saying that the nonlinear solution approaches an appropriate free wave asymptotically.

These are related but different statements. A wave may have finite energy without meeting the hypotheses for a particular endpoint estimate. A nonlinear solution may exist locally without existing globally. Global existence may hold without scattering.

The point of Strichartz theory is to capture a geometric feature of propagation in a rigorous analytic inequality. When the estimate is correctly matched to the dimension, exponents, and derivative regularity, it becomes one of the most effective tools for studying nonlinear waves.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the free wave on `R^{1+3}`,
\[
u_{tt}-\Delta u=0,\quad
u(t)=\cos(t|D|)f+\frac{\sin(t|D|)}{|D|}g,
\]
a standard global homogeneous Strichartz estimate is
\[
\|u\|_{L_t^4(\mathbb R;L_x^4(\mathbb R^3))}
\le C\bigl(\|f\|_{\dot H^{1/2}(\mathbb R^3)}+
\|g\|_{\dot H^{-1/2}(\mathbb R^3)}\bigr),
\]
for suitable data interpreted in the natural completion. Scaling check: `u_lambda(t,x)=u(lambda t,lambda x)` has `L^4_{t,x}` norm scaling like `lambda^-1`; the two Sobolev data norms on the right scale like `lambda^(1/2-3/2)=lambda^-1` and `lambda*lambda^(-1/2-3/2)=lambda^-1` respectively.

For three-dimensional waves, the standard mixed-norm admissibility condition is `q,r>=2`, `1/q+1/r<=1/2`, with `(q,r)=(2,infinity)` excluded as a general endpoint. The exact derivative regularity for a homogeneous estimate follows the scaling relation `s=3/2-1/q-3/r`; for the time-derivative datum the corresponding exponent is `s-1`. Further restrictions or formulations apply at low frequencies and inhomogeneous estimates.

Duhamel's formula for `u_tt-Delta u=F(u)` is
\[
u(t)=S(t)(f,g)+\int_0^t\frac{\sin((t-s)|D|)}{|D|}F(u(s))\,ds.
\]
An inhomogeneous Strichartz estimate together with nonlinear Hölder and contraction estimates can yield local solutions when the function space, power, and regularity are compatible. An estimate of the free propagator is not by itself a global theorem for the nonlinear PDE.

### Exercises with answers

1. What scaling Sobolev exponent corresponds to `(q,r)=(4,4)` for three-dimensional free waves? **Answer:** `s=3/2-1/4-3/4=1/2`.
2. Is `(q,r)=(2,infinity)` a standard general three-dimensional wave Strichartz pair? **Answer:** no, it is an excluded endpoint.
3. Does finite conserved energy alone imply scattering of a semilinear wave? **Answer:** no; further nonlinear estimates and structural hypotheses are needed.
4. Why does Duhamel's formula help with a nonlinear term? **Answer:** it expresses the nonlinear solution as free evolution plus a linear operator applied to the forcing, enabling a fixed-point argument.

### Reading and source notes

- [Keel and Tao, Endpoint Strichartz Estimates](https://doi.org/10.1353/ajm.1998.0039), the abstract dispersive estimate and its wave-equation applications.
- [Terence Tao, PDE preprints and references on dispersive/wave equations](https://www.math.ucla.edu/~tao/preprints/pde.html), free-wave estimates and nonlinear Cauchy problems.
- [Keel–Tao, Endpoint Strichartz Estimates (author-hosted PDF)](https://www-users.cse.umn.edu/~keel/endpoint.pdf), detailed admissibility and endpoint analysis.
