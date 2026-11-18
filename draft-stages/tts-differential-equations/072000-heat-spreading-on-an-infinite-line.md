# Heat Spreading on an Infinite Line: Solving a PDE with Fourier Transforms

<!-- BEGIN SPOKEN LECTURE -->

# Heat Spreading on an Infinite Line

Imagine a long metal wire lying along an effectively infinite straight line. At the start, a short stretch near the origin is warm. Everywhere else the wire is near a reference temperature. As time passes, the warm stretch spreads and its highest point falls. There are no fixed ends forcing the temperature to zero, and no repeating period that would single out integer harmonics. How should we calculate the whole temperature profile?

The heat equation is the same local law we used on a finite rod: the rate of change of temperature equals a positive diffusion constant times the second derivative with respect to position. But the domain is now the whole real line. We can use the Fourier transform to separate spatial frequencies without pretending there are endpoints. The result will be a precise spreading Gaussian, and from it we will recover the solution for any sufficiently well-behaved initial profile.

The derivation also explains three physical facts that deserve more than a passing mention. Heat flow conserves total heat in the infinite-line model if none escapes to infinity. It suppresses sharp spatial oscillations faster than gentle ones. And the mathematical heat kernel has a tiny positive tail at every distance as soon as time becomes positive, despite looking very localized when time is small.

## Every spatial frequency has its own clock

Write the temperature above background as u of x and t. Let kappa be a positive diffusion constant, with units of length squared per unit time. The equation says u sub t equals kappa times u sub x x. At time zero, the temperature profile is a prescribed function f of x. Assume f is smooth and decays rapidly enough, at first, that the transforms and integrations by parts are justified.

Take the Fourier transform in x, not in time. Time is still an ordinary variable in the transformed equation. A spatial first derivative transforms to i k times the transformed function; the second derivative transforms to negative k squared times that function. Thus the heat equation becomes, for each fixed real frequency k, an ordinary differential equation: the time derivative of the transformed temperature equals minus kappa k squared times the transformed temperature.

We already know how to solve this ODE. Its value at time t is its initial value multiplied by e to the negative kappa k squared t. The initial transformed value is simply the Fourier transform of f. Every frequency evolves independently, and its multiplier is explicit.

Consider what that multiplier means. At k equal to zero, it equals one. The total area under the temperature profile is unchanged, because zero frequency measures total heat. At a low nonzero frequency it decays slowly. At twice that spatial frequency, k squared is four times as large, so the decay rate is four times faster. The sharp changes in a temperature profile are assembled from high frequencies. Diffusion erases those quickly, leaving smoother, broader variations.

Compare this with the fixed-end heat rod. There the allowed sine frequencies were integer multiples of pi over the rod length. Here k may take any real value. The decay law for a mode is identical in form, but the sum over discrete sine modes has become an inverse Fourier integral. The domain changed the frequency bookkeeping, not the local diffusion mechanism.

## A point of heat as an ideal starting condition

First solve an idealized problem: all the initial heat is concentrated at the origin with total amount one. This is not an ordinary continuous temperature profile. It is a point-source idealization, represented by a Dirac delta in space. Its Fourier transform, in the distributional sense, is the constant one. Therefore the transformed temperature at time t is just e to the negative kappa k squared t.

Take the inverse transform. The calculation is a Gaussian integral. For positive t, the spatial profile is one divided by the square root of four pi kappa t, multiplied by the exponential of negative x squared over four kappa t. This is called the heat kernel or fundamental solution on the real line.

The exponent is the key to its width. The distance at which x squared is comparable to kappa t grows like the square root of t. Double the elapsed time and the typical spread increases by a factor of the square root of two, not by a factor of two. Meanwhile the maximum at the origin falls like one over the square root of t. The peak becomes lower while the profile becomes wider.

These two changes balance. Integrate the Gaussian over all x. The answer is one for every positive t. The initial point source has not lost total heat. It has spread its amount over a larger region. If we start with a total amount Q instead, the entire kernel is multiplied by Q.

The formula also gives the mean and the variance when interpreted as a probability density. The mean position is zero, and the variance is two kappa t. This does not mean the temperature itself is a random variable. Rather, the same normalized kernel describes the distribution of a random walk's displacement in its diffusion limit. That is a useful physical connection, but our heat-equation derivation required no probability theory.

There is a subtle mathematical point about the initial instant. At t equal to zero, the formula is singular: the height has no finite limit at the origin. Yet if we integrate it against a smooth test function and let t approach zero, the result tends to that test function's value at zero. This is the precise sense in which the kernel approaches the point source. Do not treat the delta as a very tall ordinary function at t equal to zero; it is a limit object that represents a concentrated total amount.

## From one point source to an arbitrary temperature profile

Now suppose the initial temperature is f of x, an ordinary integrable profile rather than a delta. Imagine splitting f into many tiny pieces of heat located at different positions. The contribution from a tiny piece at location y is a copy of the heat kernel shifted from the origin to y and weighted by the initial amount there. Add all such contributions. In the limit the sum is an integral over y.

That integral is the convolution of f with the heat kernel. In words, the temperature at x and time t equals the integral of the initial temperature at y multiplied by the Gaussian kernel evaluated at x minus y. This is not a guess. In frequency space, convolution becomes multiplication, and multiplication by the Gaussian transform is exactly the evolution factor we found from the differential equation.

This representation makes positivity transparent. The Gaussian kernel is positive. If the initial temperature is nonnegative, the later temperature is nonnegative. It also makes the maximum principle intuitive: each new value is a weighted average of initial values, with nonnegative weights that integrate to one. With a bounded initial profile, it cannot exceed the initial maximum or fall below the initial minimum.

There is no mysterious boundary heat supply on the whole line. Heat moves from neighboring locations, and all of those exchanges cancel when we add over the whole line. The integral formula preserves total heat for integrable initial data. In a finite rod with prescribed cold endpoint temperatures, heat may leave the domain, so the total need not be conserved. Conservation depends on the domain and boundary conditions as well as on the differential equation.

## Follow a Gaussian all the way through

Take a specific initial profile: e to the negative x squared divided by twice sigma squared, where sigma is a positive length. It has maximum one at the origin. Its width is described by sigma, and its total integral is sigma times the square root of two pi. This choice is particularly convenient because its Fourier transform is also Gaussian.

The initial transformed profile is sigma times the square root of two pi multiplied by e to the negative sigma squared k squared divided by two. Heat evolution adds the exponent negative kappa k squared t. Combine the exponents and we find another Gaussian in frequency whose width parameter contains sigma squared plus two kappa t.

When we invert, the physical temperature becomes a Gaussian with that enlarged squared width. The exact formula has two features: its denominator inside the exponent is twice the sum sigma squared plus two kappa t, and its peak amplitude is sigma divided by the square root of the same sum. At t equal to zero, the peak is one and the original profile is recovered. At later times the width grows and the peak falls.

Put sigma equal to one and kappa equal to one half. At time t equal to three, the squared width is one plus three, or four. The new width parameter is two, and the peak amplitude is one half. In other words, the profile that began as e to the negative x squared over two becomes one half times e to the negative x squared over eight. It is twice as wide according to sigma, and half as tall at its center. Its total integral remains the square root of two pi.

This example lets us verify the PDE directly. The time derivative of the amplitude and the changing width exactly match kappa times the second spatial derivative. We can also check the initial condition and total integral without relying on the transform derivation. Several independent checks point to the same formula.

## Why heat and transport behave differently

The Fourier transform can also make a useful comparison. Replace the heat equation with the constant-speed transport equation: u sub t plus c times u sub x equals zero. Transform in space. The frequency equation now has the multiplier negative i c k, which is purely imaginary. Its solution is a phase factor e to the negative i c k t, not a decaying factor.

Upon inversion, this phase means the entire initial profile moves rigidly to the right at speed c, provided c is positive. The answer is f of x minus c t. Its height and shape do not change. In frequency space the magnitude of each Fourier coefficient is preserved; only the phase changes. For heat, the magnitude is reduced by e to the negative kappa k squared t.

This gives a compact diagnosis of two evolution laws. A first spatial derivative generates translation. A second spatial derivative with a positive diffusion constant generates smoothing. The physical picture—carrying a shape versus spreading it—appears already in the transform multipliers.

For real heat transfer, the Fourier-law diffusion model is an approximation. Its Gaussian kernel is positive at every distance for any positive time, which mathematically means infinite propagation speed. At a large distance and small time that value is exceedingly tiny, but it is not exactly zero. More microscopic models can have finite signal speeds, and no claim about actual instantaneous communication should be inferred from this simplified PDE.

## Energy, regularity, and the limits of the calculation

There is another check on smoothing. Multiply the heat equation by u and integrate over the real line. After an integration by parts with vanishing boundary terms, the time derivative of one half the integral of u squared equals negative kappa times the integral of the squared spatial derivative. The right side is nonpositive. The squared-size measure decreases, even though the total signed integral is conserved.

Frequency space tells the same story: by the Fourier version of Parseval's identity, the squared-size integral is an integral of squared transform magnitudes. Every nonzero frequency acquires a decaying factor. One method sees the gradient dissipate energy; the other sees high frequencies attenuated rapidly. They are two views of the same mathematical operation.

Our direct calculations began with smooth, decaying profiles. The solution formula extends much farther, including many integrable and square-integrable initial conditions. But extending the class of initial data requires being precise about the sense in which the initial condition is recovered: pointwise at continuity points, in an integral norm, or in distributions for a point source. Not every initial function produces a classical solution at time zero, though the Gaussian kernel typically makes the solution smooth for any positive time.

The main construction is now complete. Transform only the spatial variable, solve a simple ODE for every continuous frequency, and invert. The inverse multiplier produces a Gaussian kernel; convolution combines copies of that kernel for general initial data. We can now turn back to bounded domains and numerical computation. When we cannot carry out the inverse transform or eigenfunction sum exactly, we will approximate spatial derivatives by nearby grid values and let familiar ODE integrators advance the resulting numerical system in time.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: heat kernel, convolution and transport

For \(\kappa>0\), the Cauchy problem on \(\mathbb R\) is
\[
u_t=\kappa u_{xx},\quad u(x,0)=f(x),\quad \widehat u(k,t)=e^{-\kappa k^2t}\widehat f(k).
\]
The heat kernel, for \(t>0\), is
\[
G_t(x)=\frac{1}{\sqrt{4\pi\kappa t}}\exp\!\left(-\frac{x^2}{4\kappa t}\right),\quad
u(x,t)=(G_t*f)(x)=\int_{\mathbb R}G_t(x-y)f(y)\,dy.
\]
Note \(\int G_t=1\), \(\int xG_t(x)dx=0\), and \(\int x^2G_t(x)dx=2\kappa t\). The family \(G_t\) approximates the delta distribution as \(t\downarrow0\).

For \(f(x)=e^{-x^2/(2\sigma^2)}\), \(\sigma>0\),
\[
u(x,t)=\frac{\sigma}{\sqrt{\sigma^2+2\kappa t}}
\exp\!\left(-\frac{x^2}{2(\sigma^2+2\kappa t)}\right).
\]
Taking \(\sigma=1,\kappa=1/2,t=3\) yields \(u(x,3)=\frac12e^{-x^2/8}\). The conserved integral equals \(\sigma\sqrt{2\pi}\).

For \(u_t+cu_x=0\), \(\widehat u(k,t)=e^{-ickt}\widehat f(k)\) and \(u(x,t)=f(x-ct)\). For sufficiently decaying smooth heat solutions,
\[
\frac{d}{dt}\frac12\int_{\mathbb R}u(x,t)^2\,dx=-\kappa\int_{\mathbb R}|u_x|^2\,dx\le0,
\quad\int_{\mathbb R}u(x,t)\,dx=\int_{\mathbb R}f(x)\,dx.
\]

### Exercises with worked answers

1. How fast does the heat kernel's standard deviation grow? **Answer:** \(\sqrt{2\kappa t}\); it scales like the square root of time.
2. For the heat equation with \(\kappa=2\), what multiplier affects frequency \(k=3\) after time \(t=1/4\)? **Answer:** \(e^{-2\cdot9\cdot1/4}=e^{-9/2}\).
3. If the initial profile is \(5G_{t_0}(x-a)\) for positive \(t_0\), what is the later solution? **Answer:** \(5G_{t+t_0}(x-a)\), by Gaussian convolution or multiplier composition.
4. For transport speed \(c=-2\), where does a pulse originally centered at zero sit at time three? **Answer:** at \(x=-6\), with unchanged shape.
5. If an integrable initial temperature is everywhere nonnegative, can the whole-line heat solution become negative later? **Answer:** no; its convolution kernel is nonnegative.

### Sources and further reading

- [MIT OpenCourseWare, 18.152 PDE lecture notes, heat equation and fundamental solution](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/pages/lecture-notes/).
- [MIT OpenCourseWare, 18.085 Computational Science and Engineering I, Fourier transform and heat equation applications](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-summer-2020/).
- [Wikipedia, Heat kernel](https://en.wikipedia.org/wiki/Heat_kernel), for the Gaussian fundamental solution and convolution semigroup.
