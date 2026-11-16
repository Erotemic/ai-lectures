# Dispersion, semilinear waves, and Strichartz estimates

<!-- BEGIN SPOKEN LECTURE -->

# Dispersion, semilinear waves, and Strichartz estimates

## Dispersive Equations, Strichartz Bounds, and Scattering

Imagine a localized pulse. Some evolution equations keep it sharply localized as it moves. Others cause it to spread: its peak becomes lower while the disturbance occupies a wider region. Dispersive equations describe this second behavior. They are not necessarily dissipative. The energy or total squared amplitude can remain constant while the spatial pattern spreads out.

The free Schrodinger equation gives a clean example. Its state is a complex-valued function of space and time. Under its evolution, the square-integrable norm stays exactly constant. But if the initial state is both integrable and square-integrable, the maximum amplitude decreases with time at a rate determined by the spatial dimension.

At first this sounds contradictory. How can the peak decay without losing norm? Because the solution is not disappearing. Its amplitude is being redistributed across space. The distinction between spreading and dissipation is central to dispersive PDE.

### Fourier modes carry different phases

Take the free Schrodinger equation with the Laplacian multiplied by one half. Apply the Fourier transform in space. Each frequency now satisfies an ordinary differential equation whose solution rotates its complex phase at a rate proportional to the square of the frequency.

Higher and lower frequencies accumulate different phases. When we transform back to physical space, those rotating phases interfere. A localized packet spreads because its constituent frequencies do not move in lockstep.

This gives an immediate proof of conservation of the square-integrable norm. In Fourier space the evolution multiplier has absolute value one at every frequency. Multiplying by a unit complex number changes phase but not magnitude, so Parseval's identity preserves the total squared norm.

The same argument does not preserve the maximum value at one location. The Fourier components can interfere constructively at one time and spread their contributions over many locations at another.

### An explicit Gaussian example

Start with a Gaussian centered at the origin. Under the free one-dimensional Schrodinger evolution, the solution remains a complex Gaussian. Its width grows with the square root of one plus time squared, while its peak magnitude falls like one plus time squared to the minus one quarter.

At large times, that peak falls like time to the minus one half. The total squared amplitude remains constant because the widening of the pulse compensates for its shrinking height. This calculation offers a visual explanation of a general dispersive estimate.

For the free equation in n spatial dimensions, the propagator has an oscillatory integral kernel whose absolute value scales like time to the minus n halves. As a result, its action maps integrable initial data to a bounded solution with a norm estimate proportional to the inverse of time to the n halves. More dimensions allow faster spatial spreading.

The estimate does not hold uniformly at time zero, where the kernel becomes singular and the initial function need not be bounded. It also requires the correct input norm. A square-integrable initial state alone does not give the same maximum-amplitude bound.

### Why a pointwise estimate is not enough

When a nonlinear term is present, an estimate on the peak amplitude at each time may be insufficient. We need to control the solution across both space and time. Strichartz estimates provide such mixed space-time bounds for free evolution and, in suitable forms, for forced equations.

The admissible exponent pairs arise from the scaling of the Schrodinger equation. Informally, the time integrability and space integrability must balance the way length and time scale under the equation. Certain endpoint cases are excluded, and the exact statement depends on dimension and chosen norms.

These estimates become useful after writing a forced or nonlinear problem in its integral form. The free propagator evolves the initial data. Each later forcing contribution is evolved forward from the moment it occurred and integrated over time. This is Duhamel's formula.

### From dispersion to scattering

In a nonlinear dispersive equation, the wave can interact with itself as it spreads. One question is whether those interactions eventually become negligible. If the solution approaches some freely evolving state in an appropriate norm as time tends to infinity, we say it scatters.

Scattering is not automatic. Some equations admit coherent structures such as solitons that remain localized. Others have solutions that blow up, or behave differently depending on dimension, nonlinearity, and initial size. A statement about scattering must include its assumptions.

The conceptual route is nevertheless clear. The linear propagator tells us how waves disperse. Space-time estimates control accumulated nonlinear interaction. Conservation laws limit how much certain norms can change. Together, these tools can sometimes prove global existence and scattering.

### What the estimates really measure

A conservation law and a dispersive estimate describe different aspects of the same solution. Conservation controls a global quantity. Dispersion controls redistribution. Neither one by itself settles every nonlinear problem.

The important new idea is that time can improve spatial behavior without destroying total norm. Phase cancellation creates decay at individual locations, and the right mixed norms let us exploit that decay across a whole evolution. This is the analytic foundation of much of modern dispersive PDE theory.

## Semilinear Waves: When Propagation Meets Nonlinearity

A taut string supports waves because a displacement produces a restoring force related to spatial curvature. The linear wave equation describes this through a second time derivative and a spatial Laplacian. We know many ways to analyze that equation: characteristics in one dimension, Fourier decomposition, conserved energy, and linear solution operators.

Now imagine that the restoring force depends nonlinearly on displacement. A simple model adds a power of the unknown function to the wave equation. The highest-order derivatives remain linear, so the equation is semilinear. But the wave's amplitude now affects how it evolves. Linear superposition no longer holds. Two solutions cannot simply be added to obtain a third.

The essential questions are familiar: Does a solution exist? Is it unique? Can it be continued for all time? Can disturbances propagate faster than the underlying linear wave speed? The answers depend on the nonlinearity, dimension, regularity, and sign of the equation.

## The linear propagator remains useful

Let us consider a wave on Euclidean space whose equation is the linear wave operator applied to u equals a forcing term that depends on u. If the forcing were already known, Duhamel's principle would express the solution as the free wave generated by the initial data plus the accumulated response to the forcing over past times.

For a semilinear equation, the forcing is not known in advance: it is a function of the solution itself. We therefore put u into Duhamel's formula on both sides. This gives an integral equation. We start with a candidate function, evaluate its nonlinear forcing, propagate that forcing with the linear solution operator, and obtain a new candidate.

If this map is a contraction on a suitable function space for a short interval of time, the Banach fixed-point theorem produces a unique local solution. The word suitable is important. The needed function space and nonlinear estimates depend on spatial dimension, the power of the nonlinearity, and how much regularity the initial data possess.

One should not infer that every power nonlinearity is locally well posed for every initial datum in every Sobolev space. The contraction estimate must be established in a space where the nonlinear product is controlled.

## Two signs, two energy landscapes

Take an equation whose restoring force is a positive power of displacement with a sign that drives the wave back toward zero. The energy contains kinetic energy, spatial-gradient energy, and a positive potential term. For a sufficiently regular solution on a domain with appropriate boundary or decay conditions, this energy is conserved.

A positive conserved energy gives useful bounds on the speed and gradient of the solution and on its nonlinear potential. This is the defocusing sign. It does not automatically prove global smooth solutions at every regularity and every exponent, but it supplies the coercive quantity around which global arguments are built.

Reverse the sign of the nonlinear potential. Now the potential term can be negative, and conserved energy may fail to control the size of the solution. This is the focusing sign. It can support concentration, instability, and finite-time blow-up. We should not confuse 'energy is conserved' with 'energy bounds every relevant norm.' Conservation alone can coexist with singular behavior when the energy is not coercive.

## A simple finite-time blow-up mechanism

To understand the focusing danger, look at a spatially homogeneous equation for a scalar function y of time. Let its acceleration equal a positive power of y. Start with positive displacement and positive velocity. The acceleration is positive, so the velocity grows, which makes the displacement grow, which increases the acceleration again.

Multiplying the equation by the velocity gives an energy identity. The velocity squared grows approximately like a higher power of displacement. For a power greater than one, the time needed for displacement to reach arbitrarily large values is finite. So the scalar equation blows up in finite time.

This calculation captures a nonlinear amplification mechanism. A constant-in-space function on the whole of Euclidean space, however, has infinite wave energy unless it is zero. We must not present it as a finite-energy blow-up solution on the whole space. It is an instructive model, and on suitable bounded or periodic domains it may directly represent a spatially homogeneous solution.

## Finite propagation still matters

The nonlinear term is local in space: the forcing at a point depends on the value of the wave at that point, not instantaneously on distant values. In a semilinear wave equation with the usual wave operator and a local nonlinearity, a domain-of-dependence principle persists as long as the relevant solution exists and sufficient regularity or uniqueness hypotheses hold.

If two solutions begin with identical initial data inside a ball, they agree in the shrinking cone where the linear wave's finite-speed principle says those data determine the solution. The nonlinearity can change the amplitude and shape of the wave, but it does not automatically grant the solution an infinite information speed.

This is a significant contrast with the heat equation, where smoothing leads to immediate nonzero tails in many common settings. The underlying type of the highest-order differential operator matters even after a nonlinear force is added.

## Local control versus global behavior

Local well-posedness provides an interval of existence whose length depends on some norm of the initial data. A continuation criterion says, roughly, that as long as the norms used by the local theory remain controlled, the solution can be restarted and extended. Blow-up occurs when a necessary control quantity becomes unbounded, not merely because the formula looks nonlinear.

For defocusing equations, positive energy estimates and dispersive inequalities can sometimes ensure the needed control for all time. For focusing equations, some initial data are still globally regular, while other data may blow up. The energy sign is an important guide but is not a complete classification by itself.

The interaction of spatial dimension and nonlinear power becomes clearer under scaling. Critical exponents then sharpen the distinction between local theory, global existence, blow-up, and scattering.

## Strichartz Estimates: Measuring the Spreading of Waves

Imagine striking a small drum or disturbing the surface of a pond. A disturbance moves away from its origin. At any one location its amplitude may weaken as the disturbance spreads across a larger region, even while the total energy of the system remains conserved.

There are two kinds of mathematical statement hidden in that picture. Energy conservation controls a spatial norm at each time. Dispersion concerns the way a solution is distributed across both space and time. The second kind of control is often essential when the wave equation contains a nonlinear forcing term.

Strichartz estimates are inequalities that measure the spreading of free waves in combined time-and-space norms. They are particularly valuable because they allow a nonlinear problem to be treated as a perturbation of its linear counterpart, without asking that the solution remain pointwise small everywhere.

## Separate energy from space-time integrability

Consider a free wave in three-dimensional space. Its displacement depends on time and three spatial coordinates, and it satisfies the equation in which the second time derivative equals the spatial Laplacian.

The conserved energy is the integral of the squares of the time derivative and spatial gradient. If the initial energy is finite, it remains constant. This is a powerful stability statement, but it does not by itself measure how many times the solution can be large in a particular space-time region.

A Strichartz estimate instead combines a spatial norm with a time norm. For example, we might take the fourth power of the solution, integrate over all space and all time, and then take the fourth root. This asks whether the wave can persistently concentrate in space-time, not just whether its derivative energy is bounded at each instant.

## Why dimension matters

The rate at which waves disperse depends on the number of spatial dimensions. In three dimensions, the propagation is concentrated near expanding spherical shells. In one dimension, left-moving and right-moving waves can retain their shapes without the same kind of geometric spreading. The estimates therefore differ with dimension.

They also depend on which frequency derivatives of the initial data are controlled. When an equation is invariant under rescaling, we can calculate what derivative order a proposed inequality must require. A bound with the wrong scaling cannot be true with a constant independent of the data scale.

For the three-dimensional free wave, an important estimate controls the fourth-power space-time norm of displacement using one half of a derivative of the initial displacement and minus one half of a derivative of the initial velocity, in the appropriate homogeneous Sobolev norms.

This may sound strange. Why a negative derivative on velocity? Because velocity enters the free-wave formula divided by the magnitude of frequency. The exponents track exactly how the two pieces of Cauchy data generate a solution at the same scaling level.

## What the Fourier formula reveals

A free wave can be decomposed into two traveling frequency components, one oscillating forward in time and the other backward. The Fourier multiplier for these components has an oscillatory phase tied to the magnitude of spatial frequency.

When we integrate such oscillations, many frequencies cancel. This cancellation is the analytic source of dispersive decay. More systematic arguments combine dispersive estimates with conservation in square-integrable norms and a duality method, often called T T star.

The resulting family of Strichartz estimates permits several combinations of time and space exponents. They obey an admissibility condition that reflects the geometry of the wave cone. For the three-dimensional wave, the pair consisting of fourth power in time and fourth power in space is admissible.

## Why an endpoint can fail

It is tempting to keep strengthening one exponent until the spatial norm becomes an essential supremum. One might hope to control a wave in the square-integrable time norm of its spatial maximum using just the scaling-predicted Sobolev norms of the initial data.

For the general three-dimensional free wave, that endpoint pair, square-integrable in time and essentially bounded in space, fails as a standard global Strichartz estimate. Certain waves can concentrate along directions strongly enough to defeat it. The problem is not a missing constant in a proof; the proposed bound is false without additional conditions.

There are special situations, for example particular radial data or modified function spaces, where related stronger estimates can hold. Those are distinct theorems. An endpoint failure in the general theorem should not be silently repaired by adding an assumption that was never stated.

## How nonlinear equations use the estimate

A semilinear wave equation has the same linear propagation on its left side but adds a nonlinear term depending on the solution. We can rewrite it using Duhamel's principle: the solution is the free evolution of its initial data plus the linear propagation of forcing produced at earlier times.

The strategy for proving local existence is to choose a space-time function space in which the nonlinear forcing can be estimated. A Strichartz inequality controls the linear propagator in that space. If the nonlinear map is locally Lipschitz there and the relevant norm is small on a short time interval, a fixed-point argument may construct a solution.

Every step needs the right exponents. The nonlinear power, the spatial dimension, the Sobolev regularity, and the interval length determine whether the contraction works. An estimate for one admissible pair is not an all-purpose guarantee of global existence, and a local solution need not scatter as time tends to infinity.

## Three different conclusions

Energy conservation bounds a quantity at every time. Strichartz estimates control integrated space-time behavior and can support perturbative nonlinear analysis. Scattering is a further conclusion saying that the nonlinear solution approaches an appropriate free wave asymptotically.

These are related but different statements. A wave may have finite energy without meeting the hypotheses for a particular endpoint estimate. A nonlinear solution may exist locally without existing globally. Global existence may hold without scattering.

The point of Strichartz theory is to capture a geometric feature of propagation in a rigorous analytic inequality. When the estimate is correctly matched to the dimension, exponents, and derivative regularity, it becomes one of the most effective tools for studying nonlinear waves.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Dispersive Equations, Strichartz Bounds, and Scattering

**Track:** Differential Equations and Dynamical Systems. **Background:** Fourier transforms, wave equations, conservation of energy, functional norms. **Central question:** how can a solution spread out in space even while a global norm stays exactly constant?

#### Mathematical companion (not spoken)

For `i u_t +(1/2) Delta u=0` on `R^n`, let `U(t)=exp(i t Delta/2)`. Fourier transform gives `hat(u)(t,xi)=exp(-i t |xi|^2/2) hat(u_0)(xi)` and consequently `||u(t)||_2=||u_0||_2` for `u_0 in L^2`.

For `t!=0`, the kernel has absolute value `(2 pi |t|)^(-n/2)` under the stated normalization:
\[
(U(t)f)(x)=(2\pi i t)^{-n/2}\int_{\mathbf R^n}e^{i|x-y|^2/(2t)}f(y)\,dy,
\qquad\|U(t)f\|_\infty\le (2\pi|t|)^{-n/2}\|f\|_1.
\]
For `u_0(x)=exp(-x^2/2)` in one dimension, `u(t,x)=(1+it)^(-1/2) exp(-x^2/[2(1+it)])`; thus `|u(t,0)|=(1+t^2)^(-1/4)`.

For the forcing equation `i u_t+(1/2)Delta u=F`, Duhamel's formula is `u(t)=U(t)u_0-i integral_0^t U(t-s)F(s) ds`. Homogeneous Strichartz estimates take the form `||U(t)u_0||_{L_t^q L_x^r} <= C ||u_0||_2` for admissible exponents satisfying `2/q+n/r=n/2`, `2<=q,r<=infinity`, excluding the standard `(q,r,n)=(2,infinity,2)` endpoint. State additional hypotheses for nonlinear scattering; the linear bound alone does not imply it.

##### Exercises with answers

1. Why is the L2 norm conserved under free Schrodinger evolution? **Answer:** the Fourier multiplier has modulus one and Parseval's theorem applies.
2. What is the large-time peak decay rate for the Gaussian in one dimension? **Answer:** proportional to `|t|^(-1/2)`.
3. Does a dispersive maximum norm bound hold uniformly as `t->0` for arbitrary L1 data? **Answer:** no; its right side becomes singular.
4. What is scattering? **Answer:** asymptotic closeness in a specified norm to a freely evolving state, under stated equation and data hypotheses.

##### Reading and source notes

- [Colliander, Keel, Staffilani, Takaoka and Tao, Global well-posedness and scattering lectures](https://math.mit.edu/~gigliola/allethlectures.pdf), free Schrodinger estimates and Duhamel formula.
- [Terence Tao, Nonlinear Dispersive Equations: Local and Global Analysis](https://terrytao.wordpress.com/books/nonlinear-dispersive-equations-local-and-global-analysis/), dispersive and Strichartz theory.
- [Lawrence Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), Fourier analytic PDE foundations.

### Semilinear Waves: When Propagation Meets Nonlinearity

**Track:** Differential Equations. **Background:** the linear wave equation, Duhamel's principle, Sobolev spaces, energy identities and fixed-point methods. **Central question:** how does a nonlinear restoring or amplifying force change the existence, energy, and propagation of waves?

#### Mathematical companion (not spoken)

For `p>1`, consider the defocusing and focusing equations on `R^d`:
\[
u_{tt}-\Delta u+\sigma |u|^{p-1}u=0,
\qquad \sigma=+1\ \text{(defocusing)},\quad \sigma=-1\ \text{(focusing)}.
\]
For sufficiently regular, decaying solutions,
\[
E(u,u_t)=\int_{\mathbb R^d}\left(\frac12|u_t|^2+\frac12|\nabla u|^2
+\frac{\sigma}{p+1}|u|^{p+1}\right)\,dx
\]
is conserved, as follows by multiplying the PDE by `u_t` and integrating by parts. For the defocusing sign, the displayed energy is nonnegative; for the focusing sign it need not control the underlying norms.

Write `D=\sqrt{-\Delta}`. The mild formulation is
\[
u(t)=\cos(tD)u_0+\frac{\sin(tD)}D u_1
-\sigma\int_0^t\frac{\sin((t-s)D)}D
\big(|u(s)|^{p-1}u(s)\big)\,ds.
\]
Its fixed-point treatment requires appropriate Banach-space nonlinear estimates; do not infer unconditional local well-posedness in an arbitrary Sobolev class.

For the ODE `y''=y^p`, `y(0)>0`, `y'(0)>0`, multiplying by `y'` yields
\[
\tfrac12 (y')^2-\tfrac1{p+1}y^{p+1}=C.
\]
For large y, `y'` grows at least on the order of `y^{(p+1)/2}`. Since `\int^\infty y^{-(p+1)/2}dy<\infty` when `p>1`, blow-up occurs in finite time. This does not itself produce a finite-energy solution on the whole of `R^d`.

##### Exercises with answers

1. What makes the equation semilinear? **Answer:** its highest derivatives enter linearly, while the lower-order forcing depends nonlinearly on u.
2. How does Duhamel's formula help? **Answer:** it turns the PDE into a fixed-point equation using the known linear wave propagator.
3. Why does negative potential energy complicate global estimates? **Answer:** the conserved energy may no longer dominate positive norms of the solution.
4. Does finite-time blow-up of a spatially homogeneous ODE prove finite-energy blow-up on all of `R^d`? **Answer:** not by itself, because nonzero spatially constant states have infinite energy there.

##### Reading and source notes

- [Duyckaerts, Dynamics of Semilinear Wave Equations](https://www.math.univ-paris13.fr/~duyckaer/enseignement/CoursOndes2025_02_04.pdf), Duhamel formula, energy and nonlinear wave dynamics.
- [Shatah and Struwe, Geometric Wave Equations](https://www.ams.org/books/cln/002/), nonlinear wave equations and energy methods.
- [Tao, Nonlinear Dispersive Equations: Local and Global Analysis](https://www.math.ucla.edu/~tao/preprints/chapter.pdf), local solution theory and dispersive estimates.

### Strichartz Estimates: Measuring the Spreading of Waves

**Track:** Differential Equations. **Background:** Fourier analysis, Sobolev norms, linear wave equations, and energy estimates. **Central question:** how can dispersion give bounds on a wave over both space and time that energy conservation alone does not provide?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. What scaling Sobolev exponent corresponds to `(q,r)=(4,4)` for three-dimensional free waves? **Answer:** `s=3/2-1/4-3/4=1/2`.
2. Is `(q,r)=(2,infinity)` a standard general three-dimensional wave Strichartz pair? **Answer:** no, it is an excluded endpoint.
3. Does finite conserved energy alone imply scattering of a semilinear wave? **Answer:** no; further nonlinear estimates and structural hypotheses are needed.
4. Why does Duhamel's formula help with a nonlinear term? **Answer:** it expresses the nonlinear solution as free evolution plus a linear operator applied to the forcing, enabling a fixed-point argument.

##### Reading and source notes

- [Keel and Tao, Endpoint Strichartz Estimates](https://doi.org/10.1353/ajm.1998.0039), the abstract dispersive estimate and its wave-equation applications.
- [Terence Tao, PDE preprints and references on dispersive/wave equations](https://www.math.ucla.edu/~tao/preprints/pde.html), free-wave estimates and nonlinear Cauchy problems.
- [Keel–Tao, Endpoint Strichartz Estimates (author-hosted PDF)](https://www-users.cse.umn.edu/~keel/endpoint.pdf), detailed admissibility and endpoint analysis.
