# From Fourier Series to Continuous Frequencies: Building the Fourier Transform

<!-- BEGIN SPOKEN LECTURE -->

# From Fourier Series to Continuous Frequencies

A vibrating string fixed at both ends has a countable set of pitches. A periodic signal can be decomposed into its fundamental frequency and integer multiples of that frequency. We learned to find those Fourier coefficients by multiplying by a sine or cosine and integrating over a period. But a brief sound, such as a handclap, does not repeat every few seconds. A temperature disturbance in a long rod is not naturally confined to a small repeating cell. Should such a signal really have a lowest nonzero frequency and an exact set of harmonics?

There is a way to answer without inventing a new idea. Start with the Fourier series we already understand, make its period larger and larger, and watch the spacing between the allowable frequencies shrink. In the limit, the list of frequency coefficients becomes a continuous function of frequency, and the sum of harmonics becomes an integral. That limiting construction is the Fourier transform.

The distinction matters: the Fourier transform is not a Fourier series with its symbols renamed. We have changed the domain, the frequency set, the normalization, and sometimes the meaning of convergence. We will derive all four changes, transform a rectangular pulse and a Gaussian, and explain why the transform is especially useful for differential equations.

## Stretching the period

Take a well-behaved signal concentrated near the origin. Pretend it repeats with period L. The allowed angular spatial frequencies are zero, plus and minus two pi divided by L, plus and minus four pi divided by L, and so on. Call the nth frequency k sub n. The gap between neighboring frequencies is two pi over L. A period of ten units has gaps five times smaller than a period of two units.

The complex version of the Fourier series expresses the signal as a sum of coefficients times oscillations of the form e to the i k sub n x. The coefficient at a given frequency comes from integrating the signal times the opposite oscillation over one period, then dividing by L. The complex exponential is shorthand for a cosine and a sine. We need not regard the signal itself as complex; the positive and negative frequency coefficients fit together to produce a real-valued answer when the original signal is real.

Now look at the factor one over L in a coefficient. Since the frequency spacing is two pi over L, one over L is the frequency spacing divided by two pi. That observation converts the series into a sum whose individual terms each include a tiny frequency interval. As L grows, the frequency grid becomes fine. The integral over one period approaches an integral over the whole real line, provided our signal is integrable and the limiting argument is justified. The sum of frequency-grid contributions then becomes an integral over all real frequencies.

We have reached a consistent pair of rules. To analyze a signal, multiply it by e to the minus i k x and integrate over all x. The resulting function of k is its Fourier transform. To reconstruct the signal, integrate that frequency function against e to the plus i k x, and divide by two pi. In this convention the forward transform carries no normalization and the inverse carries the factor one over two pi. Other books distribute the factors differently. Nothing physical changes, but every calculation has to use one convention consistently.

Imagine why this is useful. The pulse no longer needs a repeating background. Its frequency content is now defined on a continuous line of frequencies. A frequency can be one point seven in the chosen units; it need not be the third harmonic of anything. On the other hand, a single frequency is only a small part of a general localized signal. The inverse integral assembles the entire continuum of oscillations to reconstruct the pulse.

## What the frequency variable measures

If x is a position in meters, then k is a spatial angular frequency measured in radians per meter. A spatial oscillation e to the i k x repeats when x increases by two pi divided by the absolute value of k. If x instead denotes time, k is an angular temporal frequency in radians per second. The mathematics is the same, but the units tell us what phenomenon is being decomposed.

The transform of a narrow feature tends to spread over a broad range of frequencies. The transform of a wide and slowly varying feature tends to concentrate closer to zero frequency. This is not just an analogy to pitch. We can calculate it exactly.

Consider a rectangular pulse of height one between minus a and a, zero outside. Multiply this pulse by the negative-frequency oscillation and integrate. The positive and negative imaginary parts cancel, leaving twice the integral of cosine from zero to a. The result is two times sine of a k divided by k. At k equal to zero, do not divide by zero; take the limit. The transform there equals two a, precisely the area under the original pulse.

This is a useful consistency check. The zero-frequency transform of an integrable signal is its integral. A pulse twice as wide has twice the total area, and the lobes of its transform become narrower. The transform has zeros where a k is a nonzero integer multiple of pi. A finite pulse is therefore not a single frequency, nor is its transform a featureless blur. Its sharp edges leave an oscillatory signature across frequencies.

What happens when we use the inverse transform to recover the discontinuity at either edge? For the usual symmetric inversion at a jump, we obtain the midpoint of the left and right limits, or one half for this unit pulse. That does not mean the original physical pulse has somehow acquired a half-height boundary layer. Changing a function at an isolated point does not change its integrals, and Fourier reconstruction has a precise convention for a jump. Away from the two edges, it recovers the pulse's ordinary value.

## A Gaussian that stays a Gaussian

Now choose a smoother profile: e to the negative a x squared, for positive a. This bell-shaped function has no corners. Its Fourier transform turns out to be the square root of pi divided by a, times e to the negative k squared divided by four a. That is another Gaussian, now in frequency.

There is an elegant derivation that avoids guessing the answer. Differentiate the transformed integral with respect to k, which brings down minus i x. The spatial derivative of the original Gaussian is minus two a x times the Gaussian. Use that identity and integrate by parts, with vanishing boundary terms. The derivative of the transform with respect to k equals minus k over two a times the transform. We have converted the transform calculation into an elementary first-order differential equation. Its solution is a Gaussian in k. Evaluating at zero frequency determines the constant from the familiar Gaussian integral.

Suppose a is large. Then e to the negative a x squared is narrow in space. In the formula for its transform, the frequency exponent has a denominator four a, so it decays more slowly as k increases. Narrow in position, broad in frequency. If a is small, the original profile is broad and the transform is concentrated near zero. The relation follows directly from the two widths, not from a vague rule about waves.

This example is particularly valuable for diffusion. Heat spreading smooths a spatial profile. Because a Gaussian is easy to transform and invert, we can follow its width and height exactly as it evolves. That calculation will also tell us what the heat equation does to a concentrated point source.

## What information is kept?

The transform generally has both magnitude and phase. Magnitude tells us how strongly each frequency is represented. Phase tells us how those oscillations line up to build the original profile. If we shift a pulse to the right by a distance b, its Fourier transform is multiplied by a complex oscillation e to the minus i k b. Its magnitude does not change. Its phase does. Two signals can therefore have identical transform magnitudes but different locations.

Differentiation has an especially simple frequency description. For a smooth, decaying signal, integrate by parts in the transform of its first spatial derivative. The boundary term vanishes, and the result is i k times the transform of the original signal. Differentiating a second time multiplies by negative k squared. A differential operation that mixes nearby x values has become multiplication by a function of one frequency.

This is why Fourier transforms appear naturally in equations of motion and diffusion. An equation involving a spatial second derivative can become a separate ordinary differential equation for each frequency. Nothing mysterious happened to the original equation. The transform simply chose coordinates in which constant-coefficient differentiation is easy to compute.

Convolution, another operation we encountered with Laplace transforms, simplifies as well. Convolution means adding contributions from many shifted copies of a fixed response kernel. Under the usual integrability conditions, its Fourier transform is the product of the two Fourier transforms. Differentiation becomes multiplication by i k, and convolution becomes multiplication by a frequency response. These identities are useful because differential equations and response kernels repeatedly generate both operations.

## How carefully must we interpret inversion?

We should not claim every function has an ordinary, absolutely convergent Fourier integral. An integrable function has a well-defined continuous transform, but the inverse formula may need an additional condition or a limiting interpretation. For sufficiently smooth, rapidly decaying signals such as the Gaussian, both formulas work directly. For a finite-width rectangular pulse, inversion works at ordinary continuity points and approaches the midpoint at a jump. For square-integrable signals, a broader theory reconstructs the function in a mean-square sense. Those are related statements, not interchangeable ones.

There is also a familiar idealization. A constant signal extends infinitely far in both directions and is not integrable. Its transform is not an ordinary function obtained by the same integral. Physicists and engineers describe it using a Dirac delta concentrated at zero frequency. That language is meaningful in the theory of distributions, but we must not quietly insert it into a formula whose assumptions required integrability.

Remember the difference between a Fourier series and a transform. A finite interval with periodic boundary conditions selects a discrete set of frequencies, and each coefficient occupies one entry in a sum. The whole line admits a continuum, and reconstruction requires an integral. A bounded interval with fixed endpoints may instead select sine modes through its boundary-value problem. There is no universal reason to replace a legitimate sine series by a transform if the physical domain still has fixed ends.

The transition is nevertheless simple enough to remember. Increase the period, shrink the frequency spacing, and observe the sum become an integral. The rectangular pulse shows that localized edges require many frequencies. The Gaussian shows how smoothness and width appear in the transform. The derivative identity shows how spatial calculus becomes algebra in frequency. We have prepared the tools to solve diffusion on an unbounded domain—and to understand why its solution is a spreading Gaussian rather than a collection of decaying sine waves.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: transform conventions and exact calculations

Use the angular-frequency convention
\[
\widehat f(k)=\int_{-\infty}^{\infty}f(x)e^{-ikx}\,dx,\qquad
f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\widehat f(k)e^{ikx}\,dk,
\]
under suitable inversion hypotheses. If an \(L\)-periodic extension has coefficients
\[
c_n=\frac1L\int_{-L/2}^{L/2}f(x)e^{-ik_nx}\,dx,\quad
k_n=\frac{2\pi n}{L},\quad \Delta k=\frac{2\pi}{L},
\]
then \(c_n=\frac{\Delta k}{2\pi}\widehat f_L(k_n)\). For a smooth compactly supported \(f\), increasing \(L\) leads to the inverse-integral Riemann sum.

For \(f=\mathbf1_{[-a,a]}\), \(a>0\):
\[
\widehat f(k)=\begin{cases}\frac{2\sin(ak)}{k},&k\ne0,\\2a,&k=0.\end{cases}
\]
The symmetric Fourier inversion at \(x=\pm a\) yields \(1/2\), and elsewhere agrees with the rectangular pulse.

For \(a>0\),
\[
\widehat{e^{-ax^2}}(k)=\sqrt{\frac{\pi}{a}}e^{-k^2/(4a)}.
\]
Derivation: with \(F(k)=\int e^{-ax^2}e^{-ikx}dx\) and \((e^{-ax^2})'=-2axe^{-ax^2}\), integration by parts gives \(F'(k)=-kF(k)/(2a)\); \(F(0)=\sqrt{\pi/a}\).

For appropriately decaying differentiable \(f\),
\[
\widehat{f'}=ik\widehat f,\qquad\widehat{f''}=-k^2\widehat f,\qquad
\widehat{f(\cdot-b)}=e^{-ikb}\widehat f.
\]
For integrable \(f,g\), \(\widehat{f*g}=\widehat f\,\widehat g\). Plancherel extends to \(L^2\) signals:
\[
\int|f(x)|^2dx=\frac1{2\pi}\int|\widehat f(k)|^2dk.
\]

### Exercises with worked answers

1. A box has height three and width four, centered at zero. **Answer:** \(\widehat f(k)=6\sin(2k)/k\) for \(k\ne0\), with \(\widehat f(0)=12\).
2. Shift the unit box on \([-1,1]\) to the right by five. **Answer:** multiply its transform \(2\sin k/k\) by \(e^{-5ik}\); the magnitude remains unchanged.
3. Compute the transform of \(f'(x)\) if \(\widehat f(k)=e^{-k^2}\) and the relevant derivative rules hold. **Answer:** \(ik e^{-k^2}\).
4. What are the frequency units for a profile over distances measured in centimeters? **Answer:** angular spatial frequency has units of inverse centimeters (radians per centimeter).
5. Why is it incorrect to insert \(f(x)=1\) into the ordinary \(L^1\) transform definition? **Answer:** the integral over the real line does not converge absolutely; a zero-frequency delta is a distributional extension, not an ordinary integral value.

### Sources and further reading

- [MIT OpenCourseWare, 18.152 Introduction to PDE, lectures 16–18 on Fourier transform, inversion and Plancherel](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/pages/lecture-notes/).
- [MIT OpenCourseWare, 18.085 Computational Science and Engineering I, Fourier transform and applications](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-summer-2020/).
- [Wikipedia, Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform), for transform conventions and standard examples.
