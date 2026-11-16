# 057000 — The Fourier Transform: Plancherel, Derivatives, and the Heat Equation

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, L-two Hilbert geometry, and Fourier series. **Central question:** What replaces a list of integer frequencies for a signal that does not repeat?

<!-- BEGIN SPOKEN LECTURE -->

# The Fourier Transform: Plancherel, Derivatives, and the Heat Equation

Periodic sounds invite Fourier series because their frequencies come in integer multiples of one fundamental rhythm. What about a single clap, a pulse of light, or a temperature profile on an entire line? Those signals do not repeat. Their frequency description must be continuous rather than a list of integer coefficients.

The Fourier transform provides that description. Given a rapidly decaying function, multiply it by a complex oscillation of frequency xi running backward, then integrate over the entire line. The result is a function of xi. Large values mean that the original signal contains a strong component at that frequency; the complex phase remembers how those components line up in physical space.

A narrow pulse illustrates the trade-off between location and frequency. Consider a bell-shaped Gaussian. Its Fourier transform is another Gaussian. Make the pulse very narrow in space, and its transform becomes broad in frequency. Make the pulse broad in space, and its transform becomes narrow. This is not a numerical artifact. It is a structural constraint: pinpointing a signal in one domain spreads it in the other.

The inverse transform rebuilds the original function by integrating all frequencies with the matching forward phase. Exact constants depend on our convention. If we define the transform without a normalization factor in the forward integral, the inverse has a factor of one divided by two pi in one dimension. Consistency is the important point, because the derivative and convolution rules inherit those constants.

Take a smooth function that decays sufficiently rapidly. What happens to its derivative under the Fourier transform? Integrate by parts. The boundary term disappears because the function decays. A derivative in physical space becomes multiplication by imaginary frequency in transform space. A second derivative becomes multiplication by minus frequency squared.

This single rule explains why Fourier analysis is so natural for differential equations. The heat equation says that the time derivative equals the second spatial derivative. After taking the Fourier transform in space, the differential equation becomes a separate ordinary equation for each frequency. Each frequency decays exponentially at a rate proportional to its square. Inverting the transform yields the evolving temperature profile.

The transformation also changes convolution into multiplication. If an input signal is blurred by averaging it against a kernel, the output's transform is the input transform times the kernel transform. Conversely, multiplying by a frequency filter corresponds to convolution with a spatial kernel when the required integrability holds. The same two operations can look complicated in one representation and simple in another.

So far our integrals seem to require functions that are integrable over the line. But an energy signal may be square integrable without being absolutely integrable. What should its Fourier transform mean if the defining integral does not converge in the usual sense?

Plancherel's theorem gives the answer. Begin with smooth rapidly decaying functions, where all the formulas are safe. Their Fourier transforms preserve squared L two energy up to the normalization constant. Since those functions are dense in L two, the transform extends uniquely by continuity to every L two function. We no longer need to interpret the transform as a pointwise integral for arbitrary inputs. It is an operator defined by a convergent sequence in the L two norm.

This is a powerful conceptual step. Mathematics often extends a formula from a well-behaved dense class to a larger space by showing it preserves or controls the relevant norm. The same idea built continuous functional calculus from polynomial approximations and now builds the Fourier transform for finite-energy signals.

Plancherel also reveals an elegant form of the spectral theorem. On the line, differentiation is not a bounded operator on L two; its domain contains functions with square-integrable weak derivatives. But the Fourier transform turns the derivative into multiplication by imaginary frequency. The negative second derivative becomes multiplication by nonnegative frequency squared. If we know how to apply a scalar function to multiplication by frequency squared, we can apply that function to the spatial differential operator. That recovers heat filters, wave propagators, and fractional powers of the Laplacian.

There is a catch. When a multiplier grows with frequency, not every L two signal remains in L two after multiplication. The operator has a domain: those inputs whose frequency content decays enough to counter the growth. This is exactly the domain condition from unbounded functional calculus, expressed in concrete frequency language.

For example, a function may have finite energy while its gradient does not. Squared energy only measures the integral of the magnitude squared of the function. Gradient energy weights the high frequencies by frequency squared. Such a function lies in L two but not in the first-order Sobolev space. We are approaching the need for weak derivatives and Sobolev spaces, where the Fourier picture will give both precise definitions and estimates.

Fourier transforms are therefore not simply a change of coordinates for signals. They turn translation-invariant differential operators into multipliers, make energy preservation transparent through Plancherel, and give a practical way to measure regularity by examining how much high-frequency energy a function carries.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(\mathbb R\), for Schwartz \(f\), set \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx\) and \(f(x)=(2\pi)^{-1}\int\widehat f(\xi)e^{ix\xi}\,d\xi\). Then
\[\widehat{f'}(\xi)=i\xi\widehat f(\xi),\quad\widehat{f''}(\xi)=-\xi^2\widehat f(\xi),\quad\widehat{f*g}=\widehat f\,\widehat g.\]
Plancherel extends this to a unitary \(\mathcal F:L^2(dx)\to L^2(d\xi/(2\pi))\):
\[\int |f(x)|^2dx=\frac1{2\pi}\int|\widehat f(\xi)|^2d\xi.\]

For \(u_t=u_{xx}\) with suitable L2 initial data, \(\widehat u(t,\xi)=e^{-t\xi^2}\widehat u_0(\xi)\). Its inverse is convolution with \(G_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}\), \(t>0\). For Schwartz \(f(x)=e^{-x^2/(2\sigma^2)}\), \(\widehat f(\xi)=\sqrt{2\pi}\sigma e^{-\sigma^2\xi^2/2}\).

The operator \(-\partial_x^2\) is the multiplier \(\xi^2\) with domain \(\{f\in L^2:\xi^2\widehat f\in L^2\}\), equal to \(H^2(\mathbb R)\) under standard conventions.

### Exercises with answers

1. **Derivative.** What Fourier multiplier corresponds to \(-u''\)? **Answer:** \(\xi^2\).
2. **Widening.** What happens to the Fourier transform of a Gaussian when its spatial width \(\sigma\) decreases? **Answer:** Its characteristic frequency width grows like \(1/\sigma\).
3. **Heat norm.** Why does heat evolution not increase L2 norm? **Answer:** \(|e^{-t\xi^2}|\le1\) and Plancherel.

### Reading and source notes

- [MIT OpenCourseWare, 18.103 Fourier Analysis, lecture notes](https://ocw.mit.edu/courses/18-103-fourier-analysis-fall-2013/resources/lecture-notes/)
- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
