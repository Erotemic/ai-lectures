# Periodic Forcing, Resonance, and Damping: Why One Harmonic May Dominate

<!-- BEGIN SPOKEN LECTURE -->

# Periodic Forcing, Resonance, and Damping

A repeating force can sound or look harmless if we judge it by its average strength. But a motor does not shake a bridge, a machine mount, or a spring at only one frequency simply because the motor repeats at one rate. The shape of the repeating force matters. A force that switches on and off has harmonics, and any one of those harmonics might lie close to a system's natural frequency.

This lecture uses Fourier series to make that statement precise. We will start with an oscillator that has damping, calculate the response to each harmonic, and see why a weak third harmonic can produce a stronger response than the much larger fundamental. Then we will remove the damping and recover genuine resonant growth. Throughout, we will distinguish a steady periodic response from the full solution determined by initial conditions.

## A linear oscillator with a real source of energy

Write the equation as x double prime plus two beta x prime plus omega-zero squared times x equals f of t. The variable x is displacement; omega-zero is the natural angular frequency of the undamped system; beta is positive and describes viscous damping. We have divided the equation by mass so that f is an acceleration-like forcing term. In an unscaled model, mass multiplies acceleration, damping multiplies velocity, and stiffness multiplies displacement.

Without forcing, the oscillator loses energy. In the usual mass-one units, its energy is one half velocity squared plus one half omega-zero squared times displacement squared. Differentiate this energy and substitute the equation. The result is input force times velocity, minus two beta times velocity squared. The first term may add or remove energy depending on timing; the second always removes energy.

Now let the forcing be periodic. For a stable damped oscillator, the transients from initial displacement and velocity eventually decay, leaving a unique response with the same period as the input. That preferred response depends on all the harmonics in the force, not merely on the fundamental repetition rate.

## Solve one harmonic carefully

Take a single sinusoidal input: B times sine of n t, where n is a positive integer and we have chosen a two-pi-periodic time scale. Try x equal to A times sine of n t plus C times cosine of n t.

The second derivative contributes negative n squared times each term. The displacement term contributes omega-zero squared times each. The damping term converts sine to cosine and cosine to negative sine. So the coefficient of sine in the differential equation is omega-zero squared minus n squared, multiplied by A, then minus two beta n times C. The coefficient of cosine is two beta n times A plus omega-zero squared minus n squared times C.

Set the sine coefficient equal to B, and the cosine coefficient equal to zero. We have two linear equations for A and C. Their common denominator is the square of omega-zero squared minus n squared, plus the square of two beta n. The sine coefficient A equals B times omega-zero squared minus n squared, divided by that denominator. The cosine coefficient C equals negative B times two beta n, divided by the same denominator.

The output amplitude is the absolute input amplitude divided by the square root of that denominator. This formula contains the main physical story. When n is far from omega-zero, the stiffness and inertia terms do not nearly cancel and the response can remain modest. When n approaches omega-zero, their difference becomes small. If damping is weak, the denominator can be small and the response large.

There is also a phase shift. At exact frequency matching, the sine coefficient is zero and the particular response is a negative cosine. The displacement lags the sine forcing by a quarter cycle. That timing allows the force to do positive work over the cycle, while the damping dissipates the same amount in the eventual periodic regime.

## A small third harmonic that matters more

Here is an example worth calculating rather than just drawing. Consider an oscillator whose natural frequency is three radians per unit time. Give it a damping term equal to one third times velocity. Drive it with sine of t plus one third sine of three t. The second driving component is only a third as large as the first.

For the fundamental input, frequency one, the difference between the squared natural frequency and the squared driving frequency is eight. The damping contribution at this frequency is one third. The response has sine coefficient seventy-two divided by five hundred seventy-seven and cosine coefficient negative three divided by five hundred seventy-seven. Its amplitude is about one eighth.

Now examine the third harmonic. Its frequency is exactly three, equal to the natural frequency. The stiffness and inertia terms cancel. The remaining damping contribution has magnitude one. With input amplitude one third, the response is negative one third times cosine of three t. Its amplitude is one third, more than twice the fundamental response amplitude, even though it came from the smaller component of the force.

Add the two harmonic responses. That sum is the unique long-time periodic response of this damped system. We can verify it by differentiating both parts and applying the differential operator. The first produces sine of t, the second produces one third sine of three t. Any extra homogeneous solution decays, eventually leaving the same waveform regardless of how the oscillator started.

This example makes the phrase 'the fundamental frequency of the input' potentially misleading. The input's repetition period is two pi, and its fundamental frequency is one. But its third harmonic has angular frequency three, and the system selectively amplifies that component. Predicting vibration from the repetition frequency alone would miss the dominant mechanism.

## What changes if damping disappears?

Remove the velocity term while keeping the natural frequency equal to three. The equation becomes x double prime plus nine x equals sine of t plus one third sine of three t.

The first harmonic still has a bounded particular response: one eighth sine of t. But at frequency three we can no longer find a periodic particular solution by trying a constant sine-cosine combination. The differential operator kills sine of three t and cosine of three t because they solve the unforced oscillator equation. Dividing by the frequency difference would mean dividing by zero.

Instead try a term that grows linearly in time, multiplied by cosine of three t. Its second derivative plus nine times itself leaves a sine term. In fact, negative one eighteenth times t times cosine of three t supplies the required one third sine of three t.

The resulting particular solution contains a term whose amplitude grows without bound. We have found exact resonance of an ideal undamped oscillator. Even a small resonant harmonic eventually dominates because it supplies energy repeatedly without a damping mechanism to remove it. Homogeneous oscillations can adjust the initial conditions, but they cannot cancel that growing term for all time.

For a square-wave forcing, the third harmonic is present with a nonzero coefficient. An undamped oscillator with natural frequency three will therefore experience resonance, even though the square wave itself repeats at frequency one. The same reasoning applies to any harmonic with a nonzero coefficient that matches the natural frequency.

## A resonance peak is not an infinite spike when damping is positive

Bring damping back. The harmonic-response amplitude is finite for every real driving frequency when beta is positive and omega-zero is positive. Near frequency matching the response may be large, but it is not infinite. The actual frequency at which the amplitude is largest is not always exactly omega-zero. For sufficiently light damping, the displacement-response peak occurs at the square root of omega-zero squared minus two beta squared. If damping is sufficiently strong, there is no positive-frequency interior peak in displacement amplitude.

There is no contradiction. Natural frequency names the undamped oscillator's own rhythm. The displacement-resonance peak describes how a forced, damped system responds across a continuum of driving frequencies. They are related but not identical quantities.

For high harmonics, the acceleration term dominates: the amplitude response to a unit sinusoidal force shrinks roughly like one divided by the square of frequency. So a stable second-order oscillator suppresses high-frequency forcing more strongly than the stable first-order model we studied earlier. A square-wave input has harmonic coefficients roughly one divided by n, and the displacement response at high n consequently has amplitudes roughly one divided by n cubed. The output can be smooth even when the input is discontinuous.

The word 'smooth' here has limits. The forcing's jump can still show up in sufficiently high derivatives of displacement. We should not differentiate a Fourier series infinitely many times merely because its coefficients seem small.

## Where initial conditions fit

Suppose the oscillator begins with prescribed displacement and velocity. The Fourier calculation tells us a particular steady periodic response. Subtract its position and velocity at the initial time from the specified initial data. Solve the homogeneous equation with those differences. Add that transient to the periodic response.

If damping is positive, the transient decays and the periodic response takes over. If damping is zero, the homogeneous response persists as a natural oscillation, so even a bounded particular response need not describe the entire long-time motion. If a forcing harmonic resonates, no bounded periodic particular response exists in the first place.

This distinction also matters when switching is first turned on. A force that has been periodic forever and a force that begins at time zero might have identical formulas for all positive times but different prehistories. An initial-value problem explicitly specifies what the system was doing at the starting time. Fourier analysis organizes periodic steady behavior; initial conditions complete the physical story.

## The bigger bridge

Fourier series turn a repeating input into a family of frequency experiments. Linear differential equations tell us how to respond to each experiment, and superposition rebuilds the total response. A differential equation acts like a frequency-dependent filter, sometimes suppressing a harmonic, sometimes delaying it in phase, sometimes amplifying it strongly.

This idea leads in several directions. In heat and wave equations, spatial sine waves play a related role, but boundary conditions determine which modes are allowed. In signal processing, the same harmonic-response formula becomes a transfer function. In Laplace-transform methods, we organize initial conditions and forcing on the time half-line instead of beginning with a permanently periodic signal.

But the foundation is the calculation we have made here. A repeating force need not be a single sine wave. Its harmonics are measurable, its response is computable, and its initial state still matters. Those three observations are enough to connect elementary oscillators to a much larger world of analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Forced harmonic oscillators, Fourier coefficients, linear superposition, solving two-by-two linear equations. **Convention:** normalized mass-one form and period \(2\pi\).

### Harmonic transfer calculation

For \(x''+2\beta x'+\omega_0^2 x=B\sin(nt)\), \(\beta>0\), set \(\Delta_n=\omega_0^2-n^2\), \(d_n=2\beta n\), and \(D_n=\Delta_n^2+d_n^2\). Then
\[
 x_n(t)=A_n\sin nt+C_n\cos nt,
\quad A_n=\frac{B\Delta_n}{D_n},\quad C_n=-\frac{Bd_n}{D_n},\quad
 \mathrm{amp}(x_n)=\frac{|B|}{\sqrt{D_n}}.
\]
The complex transfer function is \(H(i\nu)=(\omega_0^2-\nu^2+2\beta i\nu)^{-1}\). A steady periodic solution for a Fourier series of forcing results from summing the harmonic responses (and the constant forcing response \(\bar f/\omega_0^2\) when present), provided convergence justifies the operations. For continuous positive damping and typical piecewise-smooth forcing, these harmonics converge absolutely with sufficient derivative control to solve the equation away from jump points.

### Exact worked two-harmonic resonance preference

Let \(2\beta=1/3\), \(\omega_0=3\), and \(f=\sin t+\frac13\sin3t\). Then
\[
 x''+\frac13 x'+9x=\sin t+\frac13\sin3t,
\qquad x_p(t)=\frac{72\sin t-3\cos t}{577}-\frac13\cos3t.
\]
Check the first harmonic: \(\Delta_1=8\), \(d_1=1/3\), \(D_1=64+1/9=577/9\), hence \(A_1=72/577\), \(C_1=-3/577\). For the third harmonic \(\Delta_3=0\), \(d_3=1\), \(D_3=1\), and \(B=1/3\), giving \(x_3=-(1/3)\cos3t\). The first-harmonic output amplitude is \(\sqrt{72^2+3^2}/577=1/\sqrt{577/9}\approx0.1249\), and the third-harmonic amplitude is \(1/3\).

With \(\beta=0\), a particular solution is
\[
 x_p(t)=\frac18\sin t-\frac1{18}t\cos3t,
\quad x_p''+9x_p=\sin t+\frac13\sin3t.
\]
Forcing energy balance with \(m=1\): \(E=\tfrac12(x')^2+\tfrac12\omega_0^2 x^2\) gives \(E'=f(t)x'-2\beta(x')^2\). For a periodic response, period-averaged \(E'\) is zero, so average power in equals average dissipation.

### Frequency of the displacement-response peak

For a unit-amplitude harmonic input at arbitrary \(\nu\ge0\), \(A(\nu)=\{(\omega_0^2-\nu^2)^2+(2\beta\nu)^2\}^{-1/2}\). Differentiate the squared denominator:
\[
 \frac{d}{d\nu}[(\omega_0^2-\nu^2)^2+4\beta^2\nu^2]
 =4\nu(\nu^2-\omega_0^2+2\beta^2).
\]
Thus the positive-frequency amplitude maximum is at \(\nu=\sqrt{\omega_0^2-2\beta^2}\) if \(\omega_0^2>2\beta^2\); otherwise the maximum occurs at \(\nu=0\).

### Exercises with answers

1. For \(x''+x'+4x=\sin(2t)\), find a steady periodic response. **Answer:** \(\Delta_2=0,d_2=2\), so \(x_p=-\frac12\cos2t\).
2. If the driving frequency is doubled from \(n\) to \(2n\) far above \(\omega_0\), how does a fixed-amplitude harmonic's steady displacement scale? **Answer:** Approximately one quarter as large, since the transfer amplitude is \(O(n^{-2})\).
3. In the worked example, which term determines the largest displacement harmonic, and why? **Answer:** The third harmonic, despite smaller forcing amplitude, because its forcing frequency matches the natural frequency and positive but small damping sets the denominator.
4. Is the sum of a periodic particular solution and an arbitrary homogeneous solution necessarily periodic? **Answer:** No; decaying transients are generally not periodic, and undamped natural oscillations may be incommensurate with the forcing period.
5. For \(x''+9x=(1/3)\sin3t\), verify the resonant term. **Answer:** \(x_p=-(t/18)\cos3t\) and \(x_p''+9x_p=(1/3)\sin3t\).

### Sources and additional reading

- MIT OpenCourseWare, *18.03SC*, ODEs with Periodic Input, Resonance: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/odes-with-periodic-input-resonance/
- MIT OpenCourseWare, *18.03SC*, Fourier Series: Basics: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/fourier-series-basics/
- Wikipedia: [Harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator), [Resonance](https://en.wikipedia.org/wiki/Resonance), [Frequency response](https://en.wikipedia.org/wiki/Frequency_response).
