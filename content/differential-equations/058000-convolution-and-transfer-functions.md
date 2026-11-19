# Convolution and Transfer Functions: How a System Remembers an Input

<!-- BEGIN SPOKEN LECTURE -->

# Convolution and Transfer Functions

A burst of heat raises the temperature of a room, but its influence fades. A tap on a spring sends it into motion, and that motion changes with time. Suppose we know exactly how a system responds to one brief push. Can we use that knowledge to predict its response to a force that varies every moment?

For a linear system whose rules do not change with time, the answer is yes. We treat a complicated input as a continuous accumulation of small impulses. We shift each impulse response to the instant its piece of the input arrives, scale it by that piece, and add all those responses. The resulting integral is convolution.

Convolution is also the operation that explains why a product of Laplace transforms can represent the output of a differential equation. It turns the algebra of transforms into an account of what a system remembers.

## First solve the response to a single input

Consider y prime plus two y equals f of t, with y at zero equal to zero. The number two sets the rate at which the system forgets its past. If we stop the forcing, its state decays as the exponential of negative two times elapsed time.

We could solve this equation with a Laplace transform. The transform of the derivative gives s Y because y starts at zero. Adding two Y leaves s plus two times Y. If F is the transform of the forcing, we obtain Y equal to F divided by s plus two.

But before using that formula, let us find the time-domain solution directly. Multiply the differential equation by the integrating factor exponential of two t. The left-hand side becomes the derivative of that exponential times y. Integrate from zero to the current time t. The initial condition contributes zero. What remains is the integral of exponential of two tau times f of tau, from zero to t. Multiply by exponential of negative two t.

The result is the integral from zero to t of the exponential of negative two times t minus tau, multiplied by f of tau, with respect to tau. Each past input at time tau contributes to the current state, but its effect is reduced according to how long ago it occurred.

That is convolution in its most practical form. The argument t minus tau is the age of an old input. The factor exponential of negative two times that age tells us how much survives. The input f of tau tells us what arrived at that past instant.

## Define the impulse response

Now return to a unit impulse delivered at time zero, understood as an idealization with an appropriate post-impulse convention. It jumps y from zero to one, after which the homogeneous equation makes y decay as exponential of negative two t. For nonnegative time, this causal impulse response is h of t equal to the exponential of negative two t. For negative time the causal response is zero.

With that function h, our integral becomes the integral from zero to t of h of t minus tau times f of tau. We write it as h convolved with f. We could equally integrate h of tau times f of t minus tau; a substitution shows the two descriptions agree when both integrals exist.

The impulse response is a property of the system, not of a particular input. Once we know h, we can respond to a pulse, a ramp, a square wave, or many other inputs by the same operation. The special simplification relies on linearity and time invariance. If the system's parameters change with time, a pulse today need not decay in exactly the same way as a pulse delivered yesterday, even after shifting the clock. If the system is nonlinear, adding two separate responses need not give the response to the sum of their inputs.

A causal system cannot respond before an input arrives. Here the integral runs only over the time interval from zero to the current time. In a model with no initial stored state, all the output comes from earlier inputs, not from the future. That is the physical meaning of the causal limits.

## Work through a ramp rather than quoting a theorem

Let the forcing increase steadily: f of t equals t, starting at zero. We seek the solution to y prime plus two y equals t, with y at zero equal to zero.

From convolution, y of t is the integral from zero to t of the exponential of negative two times t minus tau, multiplied by tau. Change variables if you like, or integrate by parts. Either way, the result is t over two, minus one quarter, plus one quarter times the exponential of negative two t.

Check the initial value: at t equals zero, we have zero minus one quarter plus one quarter, so y starts at zero. Differentiate the result: y prime equals one half minus one half times exponential of negative two t. Twice y equals t minus one half plus one half times that exponential. Add them and every non-input term cancels. The result is t.

The long-time behavior also makes sense. The output grows roughly as one half t, but stays about one quarter below that leading trend. The forcing keeps rising, so the system can never settle at a constant equilibrium. The exponential correction handles the initial adjustment.

The same result follows from transforms. The forcing t has transform one over s squared. Our differential equation says Y is F divided by s plus two. Therefore Y equals one over s squared times s plus two. Partial fractions produce one half over s squared, minus one quarter over s, plus one quarter over s plus two. Inverting gives exactly the same answer.

This pair of derivations is important. The transform is not magic. The product of transforms is encoding a familiar weighted accumulation over time.

## Why convolution becomes multiplication

Let f and g be causal functions for which the relevant integrals converge absolutely in a common half-plane. Their convolution is the integral from zero to t of f of tau times g of t minus tau.

Take the Laplace transform of this convolution. We now have a double integral over all pairs of nonnegative numbers tau and r whose sum is the observation time t. Changing variables to tau and r, and interchanging integration in the region where the integrals are absolutely convergent, separates the exponential of negative s times tau plus r into a product: one exponential depending only on tau, another depending only on r.

The double integral factors into the transform of f multiplied by the transform of g. In symbols, the Laplace transform of f convolved with g equals F times G. This is the convolution theorem.

Notice what it does not say. The transform of the pointwise product f of t times g of t is not generally F times G. Multiplication after transforming corresponds to convolution before transforming. Confusing those two products is one of the easiest ways to make a plausible but false calculation.

The convolution theorem is useful because many differential equations yield a transformed output Y equal to a function H times the transformed input F. Instead of struggling with inverse transforms for every input separately, we can first invert H. Its inverse is the impulse response h. Then the time-domain output is h convolved with f.

## The transfer function and zero initial state

For our example, H of s equals one over s plus two. It is called the transfer function. Its denominator tells us how the system's free response decays, and its value as a function of s tells us how an exponential-like input is modified.

There is a necessary phrase here: the transfer function describes the input-to-output relation with zero initial state. If y begins at a nonzero value y-zero, the transform equation is s Y minus y-zero plus two Y equals F. Therefore Y equals F over s plus two, plus y-zero over s plus two. Back in time, the solution is convolution with the forcing plus y-zero times exponential of negative two t.

That extra term is not a correction to H. It is the free response generated by stored initial state. In the Fourier lectures we separated periodic particular solutions from transients. Here the same distinction appears as zero-state response plus zero-input response.

The pole of H at negative two corresponds to an exponentially decaying mode. For a stable scalar first-order system like ours, this is enough to describe stability. For more general systems, especially when internal modes cancel from an input-output transfer function, poles visible in H may not tell the whole story of internal stability. One should not apply the simplest pole rule without knowing what the transfer function represents.

## Building a system from two smaller systems

Suppose the input goes through one first-order stage with equation z prime plus z equals f, starting from zero. Its output z then drives a second stage, y prime plus two y equals z, also starting from zero.

The first stage has transfer function one over s plus one. The second has transfer function one over s plus two. Because the stages are connected in series, the output transform is the input transform times both stage factors. The combined transfer function is one over s plus one times s plus two.

Using partial fractions, the combined impulse response is exponential of negative t minus exponential of negative two t. Notice that at time zero this impulse response is zero. A delta at the first stage immediately changes z, but y needs time to respond to z. The cascade has one extra layer of smoothing.

Feed a permanent unit step into the cascade. The output is the integral of the combined impulse response from zero to t. Integrating gives one half minus exponential of negative t plus one half exponential of negative two t. At time zero that is zero. Its initial slope is zero as well. At long times it approaches one half, as expected: the first stage tends toward one, and the second stage tends toward one half of its constant input.

This example demonstrates two useful rules at once. Convolution of impulse responses describes the cascade in time, while multiplication of transfer functions describes it after transforming. A complicated model can sometimes be understood by building it from simpler parts.

## The bridge back to Fourier forcing

Our first-order transfer function was one over s plus two. If a stable system is driven for a long time by a sinusoid of angular frequency omega, its steady response is connected to the transfer function evaluated at s equal to i times omega, provided that evaluation is meaningful from the convergence side. For this first-order system, the magnitude is one over the square root of four plus omega squared.

That is exactly the amplitude attenuation we derived earlier by trying a sine-and-cosine solution directly. At low frequency the gain approaches one half. At high frequency it shrinks. The complex value also records the phase lag. Fourier harmonic response and Laplace transfer functions are not competing descriptions; they illuminate the same linear system from different directions.

The real difference is what the one-sided transform handles naturally. It begins at a specified initial time, carries initial conditions through derivative rules, and can represent single switches, pulses, and other nonperiodic inputs. Convolution then translates the resulting transform products into a history of delayed responses.

What should remain after the algebra is the physical mechanism: the present state is built from earlier inputs, with each contribution shaped by the same impulse-response rule. Laplace transforms compress that accumulation into multiplication. Inverse transforms return us to time. And checking the original differential equation keeps every abstract operation tied to the problem we intended to solve.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Prerequisites:** 055000–057000; integrating factors, linearity, proper integrals and basic partial fractions. All systems below are causal and linear time-invariant unless stated otherwise.

### The Green formula and causal convolution

For \(y'+ay=f(t)\), \(a>0\), multiply by \(e^{at}\):
\[
y(t)=e^{-at}y(0)+\int_0^t e^{-a(t-\tau)}f(\tau)\,d\tau.
\]
The causal impulse response is \(h(t)=u(t)e^{-at}\), and for zero initial state
\[
y(t)=(h*f)(t)=\int_0^t h(t-\tau)f(\tau)\,d\tau,
\quad H(s)=\frac1{s+a},\quad Y(s)=H(s)F(s).
\]
For locally integrable causal \(f,g\) of suitable exponential order, and \(s\) in a half-plane of absolute convergence,
\[
\mathcal L\{f*g\}(s)=F(s)G(s).
\]
Proof: write \(t=r+\tau\), justify the change in integration order (e.g. by Fubini under absolute convergence), and factor \(e^{-s(r+\tau)}\) into \(e^{-sr}e^{-s\tau}\).

### Worked ramp input

For \(y'+2y=t\), \(y(0)=0\):
\[
Y=\frac1{s^2(s+2)}=\frac1{2s^2}-\frac1{4s}+\frac1{4(s+2)},
\]
\[
y(t)=\int_0^t e^{-2(t-\tau)}\tau\,d\tau
=\frac t2-\frac14+\frac{e^{-2t}}4.
\]
Then \(y(0)=0\), \(y'=\frac12-\frac12e^{-2t}\), and \(y'+2y=t\).

### Two-stage cascade

Let \(z'+z=f\), \(y'+2y=z\), with \(z(0)=y(0)=0\). Then
\[
H(s)=\frac1{(s+1)(s+2)}=\frac1{s+1}-\frac1{s+2},\quad
h(t)=u(t)(e^{-t}-e^{-2t}).
\]
For \(f(t)=1\) on \(t\ge0\):
\[
y(t)=\int_0^t h(r)\,dr=\frac12-e^{-t}+\frac12e^{-2t}.
\]
This satisfies \(y(0)=y'(0)=0\) and \(\lim_{t\to\infty}y(t)=1/2=H(0)\).

### Transfer function versus full response

For \(y'+2y=f\) and \(y(0)=y_0\),
\[
Y(s)=H(s)F(s)+\frac{y_0}{s+2},\quad
 y(t)=(h*f)(t)+y_0e^{-2t}.
\]
Thus \(Y=HF\) alone expresses **zero-initial-state** input-output dynamics. For a stable rational transfer function with suitable internal realization, \(|H(i\omega)|\) gives the steady-state amplitude gain for complex sinusoidal forcing; internal hidden modes require separate stability analysis.

### Exercises with answers

1. For \(h(t)=e^{-3t}u(t)\), compute the response to a unit step. **Answer:** \(\int_0^t e^{-3r}dr=(1-e^{-3t})/3\), for \(t\ge0\).
2. Evaluate \((e^{-t}*e^{-2t})(t)\) for \(t\ge0\). **Answer:** \(e^{-t}-e^{-2t}\); its Laplace transform is \(1/[(s+1)(s+2)]\).
3. Solve \(y'+2y=t\), \(y(0)=1\). **Answer:** \(y(t)=t/2-1/4+(5/4)e^{-2t}\), the zero-state ramp response plus \(e^{-2t}\).
4. Find the long-time response of a cascade \(z'+z=1\), \(y'+2y=z\), both starting at zero. **Answer:** \(y(t)\to1/2\); explicitly \(y(t)=1/2-e^{-t}+(1/2)e^{-2t}\).
5. Does \(\mathcal L\{f(t)g(t)\}=F(s)G(s)\) follow from the convolution theorem? **Answer:** No. The theorem concerns \(f*g\), not pointwise multiplication.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Convolution](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/convolution/).
- MIT OpenCourseWare, *18.03SC*, [Transfer (System) and Weight Functions, Green's Formula](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/transfer-system-and-weight-functions-greens-formula/).
- MIT OpenCourseWare, *18.03SC*, [Poles, Amplitude Response](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/poles-amplitude-response-connection-to-erf/).
- Wikipedia: [Convolution](https://en.wikipedia.org/wiki/Convolution), [Transfer function](https://en.wikipedia.org/wiki/Transfer_function), [Linear time-invariant system](https://en.wikipedia.org/wiki/Linear_time-invariant_system).
