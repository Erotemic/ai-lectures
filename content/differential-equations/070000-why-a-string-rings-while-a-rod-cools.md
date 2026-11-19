# Why a String Rings While a Rod Cools: Wave Equations by Fourier Modes

<!-- BEGIN SPOKEN LECTURE -->

# Why a String Rings While a Rod Cools

Imagine a string stretched tightly between two fixed supports. Pull its midpoint upward and release it. The string moves, overshoots, and vibrates. Now imagine a metal rod that starts warmer at its midpoint than at its two ends. If the ends are held cool, its temperature profile becomes flatter and eventually vanishes relative to the reservoir temperature.

Both experiments involve a spatial profile with fixed values at two endpoints. Both are governed by a differential equation containing a second derivative with respect to position. Yet one system oscillates while the other relaxes. What changes is the derivative with respect to time. Diffusion has one time derivative. An ideal vibrating string has two.

That difference is enough to change exponential decay into repeated motion. We can now derive the result from ideas we have already built: a boundary-value eigenproblem, Fourier sine coefficients, and ordinary differential equations for modal amplitudes. The goal is not only a formula. We will solve a plucked string, calculate how it returns to its starting shape, and use an energy identity to understand why the motion persists in the ideal model.

## A local force law for a string

Let y of x and t be a small transverse displacement of a string. Assume uniform tension, uniform mass per unit length, small slopes, and motion restricted to one transverse direction. Consider a short piece of string. Tension acts at both ends. Since the string may be tilted differently at the two ends, their vertical force components need not cancel. For small slopes, the difference in vertical tension is approximately the tension times the second spatial derivative of y times the segment length.

Newton's second law says mass times vertical acceleration equals the net vertical force. Divide by the segment length. The result is mass density per unit length times y sub t t equals tension times y sub x x. Define c squared as tension divided by mass per unit length. Then y sub t t equals c squared times y sub x x. The parameter c has units of distance divided by time and is the wave speed in this linear model.

The string is fixed at x equal to zero and at x equal to L, so y equals zero at both endpoints, at every time. Because the equation is second order in time, we also require an initial displacement profile and an initial velocity profile. Merely saying what the string looks like at release is not enough unless we also say whether and how fast it is already moving.

For a pluck and release from rest, the velocity is zero everywhere at the initial instant. For a struck string, the initial displacement may be nearly zero while the velocity is not. These are genuinely different initial conditions, even if both eventually excite a collection of standing-wave modes.

## The spatial part is familiar

Try y as a product X of x times T of t. Substitute into the wave equation, and divide where the product is nonzero. We obtain T double prime divided by c squared T equals X double prime divided by X. Each side must equal a common constant, conveniently negative lambda.

The spatial problem is once again negative X double prime equals lambda X, with X zero at both ends. We have solved this already. The allowed shapes are sine of n pi x over L, and their eigenvalues are n squared pi squared over L squared.

The new feature is the temporal equation. Instead of T prime equal to negative kappa lambda T, we have T double prime plus c squared lambda T equals zero. This is the elementary harmonic oscillator equation. Its solutions are a cosine and a sine in time, not a decaying exponential.

For spatial mode n, the angular frequency is c times n pi divided by L. The fundamental frequency has n equal to one. The second mode has twice that frequency, the third has three times, and so on. Each mode preserves its own amplitude in time in the absence of damping or external work, though its instantaneous displacement changes sign and passes through zero.

This gives the standing-wave picture. The first sine shape has one bulge between the supports. The second has a node in the middle and opposite displacements on the two halves. The third has two interior nodes. Each spatial shape is stationary as a pattern of nodes, while its amplitude oscillates in time. A general pluck is a sum of these patterns.

## The two pieces of initial data

To assemble a general solution, give each sine mode an amplitude that oscillates according to its own frequency. That amplitude has two constants, not one. The cosine coefficient is determined by the initial displacement. The sine coefficient is determined by the initial velocity, after division by the mode's angular frequency.

This is the same principle used for a simple oscillator. If q double prime plus omega squared q equals zero, then q of t is A times cosine of omega t plus B divided by omega times sine of omega t, where A is q at zero and B is q prime at zero. The division by omega matters for units as well as for the initial derivative.

Extract the spatial coefficients of the initial displacement by multiplying by sine of n pi x over L, integrating, and normalizing. Do the same for the initial velocity. The two lists supply the two constants for each modal oscillator. This is the entire construction for a sufficiently regular fixed-end initial-boundary value problem.

Notice the contrast with heat. The heat equation needs an initial displacement-like profile, namely temperature, and each coefficient obeys a first-order decay law. The wave equation needs both displacement and velocity, and each coefficient obeys a second-order oscillation law. We did not change the spatial eigenfunctions. We changed only their time equations.

## A plucked string with a triangular shape

Let the string length be one. Pull its midpoint up to height h while keeping both endpoints fixed, making a triangular tent: a straight segment rises from zero to h on the left half, and another straight segment falls back to zero on the right half. Release the string from rest. We will find its complete linear wave solution.

Because the triangle is symmetric about the midpoint, certain Fourier sine coefficients vanish. In particular, all even mode numbers disappear. Their sine waves change sign under reflection about the midpoint, whereas our triangle is symmetric; their positive and negative contributions cancel in the coefficient integral.

For an odd mode number n, integration gives a coefficient equal to eight h divided by n squared pi squared, multiplied by sine of n pi over two. That last sine alternates between positive one and negative one as n runs through one, three, five, and so on. The first coefficient is eight h over pi squared, about point eight one h. The third is negative eight h over nine pi squared, about negative point zero nine h. The fifth is positive eight h over twenty-five pi squared.

That alternating sequence reconstructs the pointed triangular profile from smooth sine waves. The coefficients shrink as one over n squared, reflecting the fact that the original profile is continuous but its slope jumps at the midpoint. There are infinitely many modes, but each successive odd mode contributes less to the displacement.

Because the string is released from rest, each temporal coefficient multiplies a cosine, not a time sine. The first spatial mode moves with cosine of c pi t. The third moves with cosine of three c pi t. The fifth moves with cosine of five c pi t. Add the modes using their calculated amplitudes, and we obtain the moving string.

There is a pleasing exact prediction. At time one divided by c, every odd mode's temporal cosine equals negative one: cosine of n pi with n odd. So the entire displacement profile is the negative of its initial value. The string is an inverted triangle, with its center at height negative h. At time two divided by c, every modal cosine returns to positive one, and the original upward triangle returns. This is the periodic motion of the ideal fixed string. No numerical simulation was needed to discover the return time.

We have to distinguish the displacement from the whole state. At time one divided by c the displacement is inverted and the velocity is again zero for this special release-from-rest example. At time two divided by c both displacement and velocity agree with their initial values. General initial data can be handled by the same modal formulas, with nonzero time-sine terms.

The model is idealized. Real strings have damping, imperfect supports, bending stiffness, and nonlinear effects for sufficiently large motion. Those change frequencies and amplitudes. Our derivation explains the baseline that more realistic models modify.

## Why the vibration does not simply die away

Heat diffusion lost energy from its temperature variation in a precise mathematical sense: the time derivative of the squared temperature norm was nonpositive. For the undamped wave equation the corresponding conserved quantity contains two parts. One measures motion through the squared velocity. The other measures deformation through the squared spatial slope, multiplied by c squared.

Call their sum, each with a factor one half, the wave energy. Differentiate it in time. The kinetic part produces the integral of velocity times acceleration. The deformation part produces the integral of slope times the time derivative of slope. Integrate that second term by parts in x. Because the endpoints are fixed, their velocities vanish there, eliminating the boundary term. The remaining integral is minus c squared times velocity times the second spatial derivative of displacement.

The wave equation says acceleration equals c squared times that second spatial derivative. The two integrals cancel. Therefore energy is constant in time. Energy can exchange between deformation and motion, but the total does not decay in the ideal fixed-end model.

Check one standing wave. At maximum displacement, its velocity is zero and its energy is stored in deformation. A quarter cycle later, its displacement is zero but its velocity is greatest, and the energy is kinetic. The energy moves back and forth between the two forms. That is why an undamped sine mode oscillates instead of acquiring the heat equation's exponential decay factor.

We do not need every solution to be twice continuously differentiable everywhere to understand the physical idea. A triangular initial profile has a corner. One can first calculate with smooth initial data, prove the energy identity there, and interpret the triangular case as a suitable energy-limit solution. What we must not do is pretend a slope jump has an ordinary second derivative at the initial instant.

## Damping and external forcing return us to familiar ODEs

Attach a weak linear damping mechanism. In the wave equation, include a term proportional to the time derivative of displacement. Each spatial sine mode then obeys a damped oscillator ODE. Its solutions can decay while oscillating, or decay without oscillating, depending on damping strength and frequency. Those are exactly the cases we studied for a single mass and spring. We now have one such oscillator for each spatial mode.

Drive the string with a force whose spatial shape is the first sine mode and whose time dependence is a cosine. Then only the first modal equation is forced, provided the initial conditions do not excite other modes. It becomes a familiar forced oscillator: q double prime plus the square of the fundamental frequency times q equals the forcing amplitude times cosine of the driving frequency times time.

If the driving frequency is different from the natural frequency, we can find a bounded sinusoidal particular solution in the undamped, nonresonant case. At exact resonance, a new factor of time appears. Starting from rest with zero displacement, the resonant response is proportional to time times sine of the natural frequency times time. Its envelope grows linearly in this ideal model because the external force continuously supplies energy at the matching frequency.

Real damping or nonlinear effects change that long-term growth. But the elementary oscillator calculation already predicts where amplification occurs. We did not need an entirely new PDE technique; we used the boundary eigenfunctions to isolate one ordinary differential equation.

## One more boundary comparison

If the ends are free in the sense that their spatial derivatives vanish, the standing-wave spatial shapes change to cosines. Just as in the insulated heat problem, a constant spatial mode appears with eigenvalue zero. But its temporal behavior is different. For heat, its amplitude remains constant. For a wave, the zero mode satisfies q double prime equals zero, so its amplitude can be a constant plus a multiple of time. A freely translating string can have uniform transverse velocity in the simplified free-end model. Zero spatial curvature produces no restoring force for that rigid displacement.

The same boundary eigenfunction is therefore not the same physical motion in every evolution equation. The boundary decides which spatial shapes are legal; the time equation decides whether their amplitudes remain, decay, oscillate, or drift.

Our method has boundaries and limits. On an infinite line, discrete sine frequencies give way to a continuous frequency variable, which leads toward Fourier transforms. With nonuniform tension or density, the spatial eigenproblem becomes a more general Sturm–Liouville problem. With nonlinear forces, separate modes can interact. But the basic procedure remains a valuable point of reference: identify the domain and boundaries, find the spatial modes, determine their initial amplitudes, and solve the time equation for each.

We can now account for two very different experiences—a rod cooling and a string ringing—using the same spatial mathematics. The sine waves do not dictate what the system does. They reveal the ways the system can move or change. Conservation, diffusion, and forcing determine what happens to each of those possibilities over time.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: wave modes and energy

### Fixed-end wave equation

For tension \(\mathcal T>0\) and mass per unit length \(\mu>0\), \(c^2=\mathcal T/\mu\). On \((0,L)\):
\[
y_{tt}=c^2 y_{xx},\qquad y(0,t)=y(L,t)=0,
\quad y(x,0)=f(x),\quad y_t(x,0)=g(x).
\]
The sine series solution (in the appropriate energy or classical sense) is
\[
y(x,t)=\sum_{n=1}^\infty\left[
 A_n\cos(\omega_n t)+\frac{B_n}{\omega_n}\sin(\omega_n t)
\right]\sin\frac{n\pi x}{L},\quad
\omega_n=\frac{c n\pi}{L},
\]
\[
A_n=\frac2L\int_0^L f(x)\sin\frac{n\pi x}{L}dx,
\quad B_n=\frac2L\int_0^L g(x)\sin\frac{n\pi x}{L}dx.
\]
The factor \(B_n/\omega_n\) ensures \(\partial_t y(x,0)=g(x)\).

### Triangular pluck

On \(L=1\), put
\[
f(x)=\begin{cases}2hx,&0\le x\le 1/2,\\2h(1-x),&1/2\le x\le1,\end{cases}\qquad g(x)=0.
\]
Integration by parts gives
\[
A_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}{2},\qquad
A_{2m}=0.
\]
Thus \(y(x,t)=\sum_{n\ge1}A_n\cos(cn\pi t)\sin(n\pi x)\). At \(t=1/c\), the cosine is \(-1\) for every nonzero (odd) mode, so \(y(x,1/c)=-f(x)\). At \(t=2/c\), \(y(x,2/c)=f(x)\) and \(y_t(x,2/c)=0\).

### Wave energy and forcing

For smooth solutions with fixed ends,
\[
E(t)=\frac12\int_0^L\left(y_t^2+c^2y_x^2\right)dx,
\qquad E'(t)=\left[c^2 y_t y_x\right]_0^L=0.
\]
For \(y_{tt}=c^2y_{xx}+F\sin(\pi x/L)\cos(\Omega t)\), zero initial conditions, and fixed ends, only the first mode is forced:
\[
q''+\omega_1^2q=F\cos(\Omega t),\quad q(0)=q'(0)=0.
\]
At resonance \(\Omega=\omega_1\),
\[
q(t)=\frac{F}{2\omega_1}t\sin(\omega_1t),\qquad
 y(x,t)=q(t)\sin(\pi x/L).
\]
With Neumann endpoints, the zero mode instead obeys \(q_0''=0\), allowing uniform drift.

### Exercises with answers

1. Find the first two angular frequencies for a fixed string of length two with wave speed three. **Answer:** \(\omega_1=3\pi/2\), \(\omega_2=3\pi\).
2. Solve the fixed-end wave equation on \((0,1)\) for \(f(x)=\sin(2\pi x)\) and zero initial velocity. **Answer:** \(y=\sin(2\pi x)\cos(2c\pi t)\).
3. Solve with zero displacement and initial velocity \(g(x)=5\sin(\pi x)\). **Answer:** \(y=\frac5{c\pi}\sin(c\pi t)\sin(\pi x)\).
4. For the triangular pluck, what fraction of the first-mode coefficient is the magnitude of the third-mode coefficient? **Answer:** \(1/9\); its sign is opposite.
5. For an insulated heat rod and a free-end wave string, what does the spatially constant eigenfunction do? **Answer:** heat amplitude stays constant without sources; wave amplitude is \(a+bt\) unless initial mean velocity is zero.

### Sources and further reading

- [MIT OpenCourseWare, ES.1803 Topic Notes, Topics 25–26](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/pages/topic-notes/).
- [MIT OpenCourseWare, 18.303 Linear PDE course outline](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/).
- [Robert Herman, *Partial Differential Equations*](https://people.uncw.edu/hermanr/pde1/PDEbook/PDE1_Main2021.pdf), introductory chapters on wave and heat equations.
