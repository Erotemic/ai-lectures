# 023000 — Dispersive Equations, Strichartz Bounds, and Scattering

**Track:** Differential Equations and Dynamical Systems. **Background:** Fourier transforms, wave equations, conservation of energy, functional norms. **Central question:** how can a solution spread out in space even while a global norm stays exactly constant?

<!-- BEGIN SPOKEN LECTURE -->

# A wave that spreads without losing its total size

Imagine a localized pulse. Some evolution equations keep it sharply localized as it moves. Others cause it to spread: its peak becomes lower while the disturbance occupies a wider region. Dispersive equations describe this second behavior. They are not necessarily dissipative. The energy or total squared amplitude can remain constant while the spatial pattern spreads out.

The free Schrodinger equation gives a clean example. Its state is a complex-valued function of space and time. Under its evolution, the square-integrable norm stays exactly constant. But if the initial state is both integrable and square-integrable, the maximum amplitude decreases with time at a rate determined by the spatial dimension.

At first this sounds contradictory. How can the peak decay without losing norm? Because the solution is not disappearing. Its amplitude is being redistributed across space. The distinction between spreading and dissipation is central to dispersive PDE.

## Fourier modes carry different phases

Take the free Schrodinger equation with the Laplacian multiplied by one half. Apply the Fourier transform in space. Each frequency now satisfies an ordinary differential equation whose solution rotates its complex phase at a rate proportional to the square of the frequency.

Higher and lower frequencies accumulate different phases. When we transform back to physical space, those rotating phases interfere. A localized packet spreads because its constituent frequencies do not move in lockstep.

This gives an immediate proof of conservation of the square-integrable norm. In Fourier space the evolution multiplier has absolute value one at every frequency. Multiplying by a unit complex number changes phase but not magnitude, so Parseval's identity preserves the total squared norm.

The same argument does not preserve the maximum value at one location. The Fourier components can interfere constructively at one time and spread their contributions over many locations at another.

## An explicit Gaussian example

Start with a Gaussian centered at the origin. Under the free one-dimensional Schrodinger evolution, the solution remains a complex Gaussian. Its width grows with the square root of one plus time squared, while its peak magnitude falls like one plus time squared to the minus one quarter.

At large times, that peak falls like time to the minus one half. The total squared amplitude remains constant because the widening of the pulse compensates for its shrinking height. This calculation offers a visual explanation of a general dispersive estimate.

For the free equation in n spatial dimensions, the propagator has an oscillatory integral kernel whose absolute value scales like time to the minus n halves. As a result, its action maps integrable initial data to a bounded solution with a norm estimate proportional to the inverse of time to the n halves. More dimensions allow faster spatial spreading.

The estimate does not hold uniformly at time zero, where the kernel becomes singular and the initial function need not be bounded. It also requires the correct input norm. A square-integrable initial state alone does not give the same maximum-amplitude bound.

## Why a pointwise estimate is not enough

When a nonlinear term is present, an estimate on the peak amplitude at each time may be insufficient. We need to control the solution across both space and time. Strichartz estimates provide such mixed space-time bounds for free evolution and, in suitable forms, for forced equations.

The admissible exponent pairs arise from the scaling of the Schrodinger equation. Informally, the time integrability and space integrability must balance the way length and time scale under the equation. Certain endpoint cases are excluded, and the exact statement depends on dimension and chosen norms.

These estimates become useful after writing a forced or nonlinear problem in its integral form. The free propagator evolves the initial data. Each later forcing contribution is evolved forward from the moment it occurred and integrated over time. This is Duhamel's formula.

## From dispersion to scattering

In a nonlinear dispersive equation, the wave can interact with itself as it spreads. One question is whether those interactions eventually become negligible. If the solution approaches some freely evolving state in an appropriate norm as time tends to infinity, we say it scatters.

Scattering is not automatic. Some equations admit coherent structures such as solitons that remain localized. Others have solutions that blow up, or behave differently depending on dimension, nonlinearity, and initial size. A statement about scattering must include its assumptions.

The conceptual route is nevertheless clear. The linear propagator tells us how waves disperse. Space-time estimates control accumulated nonlinear interaction. Conservation laws limit how much certain norms can change. Together, these tools can sometimes prove global existence and scattering.

## What the estimates really measure

A conservation law and a dispersive estimate describe different aspects of the same solution. Conservation controls a global quantity. Dispersion controls redistribution. Neither one by itself settles every nonlinear problem.

The important new idea is that time can improve spatial behavior without destroying total norm. Phase cancellation creates decay at individual locations, and the right mixed norms let us exploit that decay across a whole evolution. This is the analytic foundation of much of modern dispersive PDE theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `i u_t +(1/2) Delta u=0` on `R^n`, let `U(t)=exp(i t Delta/2)`. Fourier transform gives `hat(u)(t,xi)=exp(-i t |xi|^2/2) hat(u_0)(xi)` and consequently `||u(t)||_2=||u_0||_2` for `u_0 in L^2`.

For `t!=0`, the kernel has absolute value `(2 pi |t|)^(-n/2)` under the stated normalization:
\[
(U(t)f)(x)=(2\pi i t)^{-n/2}\int_{\mathbf R^n}e^{i|x-y|^2/(2t)}f(y)\,dy,
\qquad\|U(t)f\|_\infty\le (2\pi|t|)^{-n/2}\|f\|_1.
\]
For `u_0(x)=exp(-x^2/2)` in one dimension, `u(t,x)=(1+it)^(-1/2) exp(-x^2/[2(1+it)])`; thus `|u(t,0)|=(1+t^2)^(-1/4)`.

For the forcing equation `i u_t+(1/2)Delta u=F`, Duhamel's formula is `u(t)=U(t)u_0-i integral_0^t U(t-s)F(s) ds`. Homogeneous Strichartz estimates take the form `||U(t)u_0||_{L_t^q L_x^r} <= C ||u_0||_2` for admissible exponents satisfying `2/q+n/r=n/2`, `2<=q,r<=infinity`, excluding the standard `(q,r,n)=(2,infinity,2)` endpoint. State additional hypotheses for nonlinear scattering; the linear bound alone does not imply it.

### Exercises with answers

1. Why is the L2 norm conserved under free Schrodinger evolution? **Answer:** the Fourier multiplier has modulus one and Parseval's theorem applies.
2. What is the large-time peak decay rate for the Gaussian in one dimension? **Answer:** proportional to `|t|^(-1/2)`.
3. Does a dispersive maximum norm bound hold uniformly as `t->0` for arbitrary L1 data? **Answer:** no; its right side becomes singular.
4. What is scattering? **Answer:** asymptotic closeness in a specified norm to a freely evolving state, under stated equation and data hypotheses.

### Reading and source notes

- [Colliander, Keel, Staffilani, Takaoka and Tao, Global well-posedness and scattering lectures](https://math.mit.edu/~gigliola/allethlectures.pdf), free Schrodinger estimates and Duhamel formula.
- [Terence Tao, Nonlinear Dispersive Equations: Local and Global Analysis](https://terrytao.wordpress.com/books/nonlinear-dispersive-equations-local-and-global-analysis/), dispersive and Strichartz theory.
- [Lawrence Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), Fourier analytic PDE foundations.
