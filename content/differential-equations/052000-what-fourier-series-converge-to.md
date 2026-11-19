# What Fourier Series Converge To: Approximation, Energy, and Gibbs Oscillations

<!-- BEGIN SPOKEN LECTURE -->

# What Fourier Series Converge To

Suppose a periodic signal switches instantly from negative one to positive one. A Fourier series represents it using sine waves. But every finite sum of sine waves is continuous. No matter how many smooth waves you add, you cannot create a literal discontinuity with a finite sum. Does this mean the method is impossible, or merely that we are asking the wrong question about approximation?

The answer depends on what we want to measure. How close is the approximation at a particular time? How close is it on average? Does it capture the signal's total energy? And what happens near a jump, where the approximation develops little ripples? These are different questions. In differential equations, choosing the wrong one can make a correct calculation look like a mistake, or a plausible graph look more accurate than it is.

## A Fourier sum is a projection

Think of fitting a periodic signal by a finite collection of sine and cosine waves. If we choose up to the N-th harmonic, we have a finite-dimensional space of possible approximations. Any choice of coefficients puts us somewhere in that space.

We need a measure of fit. A natural one is the average squared difference between the signal and the proposed approximation over one full period. Large errors matter more than small errors, and positive and negative errors cannot cancel merely because their signs differ. For a two-pi-periodic signal, integrate the square of the error from negative pi to pi, then divide by two pi.

Now minimize that quantity with respect to every unknown coefficient. When you adjust the coefficient of, say, sine of three t, the derivative of squared error tells you that at the optimum the remaining error must average to zero against that sine wave. The same reasoning works for each cosine and for the constant function.

Those are exactly the orthogonality conditions used to compute Fourier coefficients. This gives the coefficients an interpretation beyond a clever integral formula: the first N Fourier harmonics are the best approximation, in average squared error, among all trigonometric polynomials with frequencies up to N.

A finite Fourier sum is therefore an orthogonal projection. The residual is perpendicular, in the function-space sense, to the entire set of harmonics we have included. More terms cannot make the best mean-square error worse, because the old approximation remains among the choices available when we enlarge the space.

## How much of the square wave is in the first sine?

Return to the square wave that is negative one for half the period and positive one for the other half. Its average square is one. That is a convenient normalization: the signal has unit mean-square size.

Its first Fourier coefficient is four divided by pi. If we use only the first sine harmonic, the approximation is four over pi times sine of t. The mean square of that sine wave is one half times the square of its amplitude. Thus the first harmonic accounts for eight divided by pi squared, or about eighty-one percent, of the square wave's total mean-square size.

That is quite a lot of the energy from one smooth wave. But the remaining nineteen percent contains the sharp switching behavior, precisely the feature most visible when we zoom in near the jumps.

Add the third harmonic. Its coefficient is four divided by three pi. Since the first and third harmonics are orthogonal, their contributions to mean-square size add without cross terms. The added fraction is eight divided by nine pi squared. The fifth contributes another eight divided by twenty-five pi squared. The first three nonzero harmonics together account for about ninety-three percent of the total mean square.

This calculation also tells us something about approximation error without plotting a graph. The residual mean square is one minus the sum of the energy fractions retained. As we add higher odd harmonics, this residual shrinks toward zero. The full statement is called convergence in mean square, or L-two convergence. It means the area under the squared error tends to zero over a period.

But mean-square convergence is not the same as uniform closeness at every instant. To see the difference, look at a switching time.

## At a jump, which value should a series choose?

At time zero our square wave changes from negative one on the left to positive one on the right. Every sine term in its Fourier series is zero at zero. Every partial sum is therefore zero there, regardless of how many harmonics we use.

That answer makes sense if we regard zero as the midpoint of the jump, but it will never equal the value positive one immediately to the right. No infinite sequence of these partial sums can converge uniformly across an interval containing the jump, because the uniform limit of continuous functions would itself be continuous.

For a sufficiently regular piecewise-smooth periodic function, the ordinary Fourier partial sums converge at each point to the average of the left and right limits. At points where the function is continuous, that average is just the function's value. At a jump, it is the midpoint. A value that we choose to assign exactly at the jump does not control the limit: one isolated value has no effect on the Fourier coefficients.

This result comes with hypotheses. For completely arbitrary integrable functions, pointwise convergence is a more delicate question. We are making a claim here for the well-behaved piecewise-smooth examples used in introductory differential equations.

## The ripples that refuse to disappear

Near each jump, Fourier partial sums show an overshoot and a small oscillation. As we add harmonics, the ripple occupies a narrower region, but its highest overshoot relative to the jump does not shrink to zero. In the classic square-wave example, the limiting overshoot is about nine percent of the total jump height. Since our jump height is two, the overshoot above positive one is about zero point one eight.

This is the Gibbs phenomenon. It is not numerical roundoff and does not prove that the coefficients are wrong. It is an intrinsic feature of sharply truncating a Fourier series for a function with a jump. The oscillations concentrate near the discontinuity; their width shrinks, so their contribution to average squared error tends to zero even though the peak remains visible when we zoom in at the appropriate scale.

A graph with only five harmonics may look surprisingly good across the flat regions and conspicuously bad at the edges. More harmonics make the transition steeper, not perfectly monotone. If an engineer cannot tolerate ringing, they may smooth the sharp frequency cutoff or model the system's actual response to the switching signal, which often filters high frequencies.

It is important not to confuse smoothing the display of a Fourier series with changing the signal itself. A truncated series, a filtered series, and a physical system's output are three different mathematical objects.

## Why smoother waveforms usually have smaller high harmonics

We can quantify a difference we already saw. The square wave has nonzero sine coefficients proportional to one divided by n. A continuous triangular wave with corners has nonzero cosine coefficients proportional to one divided by n squared.

Where does this pattern come from? Fourier coefficients are integrals of a function against a rapidly oscillating sine or cosine. Integrate by parts. The oscillating function gains a factor of one divided by n, while a derivative moves onto the original signal. If the signal and its periodic boundary values behave well enough, the boundary terms cancel. If a further derivative behaves well, you may integrate by parts again and gain another factor.

Jumps spoil that argument. A discontinuity introduces a boundary contribution that survives at order one divided by n. A continuous signal with a jump in its slope can exhibit faster decay, often one divided by n squared. Smoothness is therefore encoded in the tail of the frequency spectrum.

We have to state this carefully. A function being continuous by itself does not guarantee a particular rapid rate of Fourier-coefficient decay. For the broad principle to become a theorem, we must say which derivatives exist and are integrable or have bounded variation, and that the periodic endpoints match as needed.

## Why differentiating a Fourier series needs care

Suppose you know a series for a function and want the series for its derivative. Differentiating sine of n t multiplies it by n. That is dangerous because the original Fourier coefficients might have been small primarily because of a factor one divided by n.

For the triangular wave, the original cosine coefficients decrease like one divided by n squared. After formal differentiation, they decrease only like one divided by n. Away from its corners, the derivative exists and is a square-wave-like function; at its corners, the ordinary derivative does not exist. There is no single globally valid formula obtained by blindly differentiating the original series at every point.

The same caution applies to integration in the other direction, although integrating often makes coefficients decay faster and is easier to justify. In differential equations we will sometimes substitute Fourier series into an ODE term by term. We must do so under conditions that justify the operation, or first work with finitely many terms and then pass to a limit in an appropriate norm.

For a stable linear ODE, the solution operator itself often damps high-frequency inputs. That can make the output series substantially smoother than the forcing series, even if the forcing jumps. We will see this rather than assume it.

## A useful distinction between energy and pointwise shape

Fourier coefficients support two complementary ways to think. In the time domain, a signal has a shape, switching instants, peaks, and plateaus. In the frequency domain, the same signal has a list of harmonic amplitudes and phases. A finite frequency list cannot exactly reproduce a jump, but it can approximate the signal well in average square and can accurately predict the part of a linear system's response that depends most strongly on low harmonics.

The right question is not simply, does the series equal the function? It is: in what sense, at which points, and for which mathematical operation do we need equality? A pointwise argument, an energy estimate, and a differential equation may demand different kinds of control.

This distinction is one of the most important lessons on the way from elementary calculus to Fourier analysis and PDEs. It tells us how to use infinite sums responsibly, and why mathematical convergence is not a single yes-or-no property.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Fourier coefficient calculations, orthogonality, squared-error minimization, elementary integration. **Convention:** \(\langle f,g\rangle=(2\pi)^{-1}\int_{-\pi}^{\pi}f(t)g(t)\,dt\) for real functions.

### Optimal projection and energy

The finite Fourier projection is \(P_N f=a_0/2+\sum_{n=1}^N(a_n\cos nt+b_n\sin nt)\). For every trigonometric polynomial \(v\) of degree at most \(N\), \(\langle f-P_Nf,v\rangle=0\). Consequently,
\[
\|f-v\|_{2,\mathrm{avg}}^2=\|f-P_Nf\|_{2,\mathrm{avg}}^2+\|P_Nf-v\|_{2,\mathrm{avg}}^2.
\]
This proves optimality. By completeness of the trigonometric system in \(L^2(-\pi,\pi)\), \(P_Nf\to f\) in the mean-square norm. Parseval's identity gives
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|f|^2\,dt=\frac{a_0^2}{4}+\frac12\sum_{n=1}^\infty(a_n^2+b_n^2).
\]
For square wave \(s=\operatorname{sgn}(\sin t)\), \(\|s\|_{2,\mathrm{avg}}^2=1\), \(b_n=4/(\pi n)\) for odd \(n\), and 0 otherwise. Thus the first odd harmonics carry energy fractions
\[
 E_1=\frac8{\pi^2}\approx0.810569,
\quad E_{1,3,5}=\frac8{\pi^2}\left(1+\frac19+\frac1{25}\right)\approx0.93306.
\]
For truncation at the first \(M\) odd harmonics, the remaining mean-square error is \(1-\frac8{\pi^2}\sum_{k=0}^{M-1}(2k+1)^{-2}\).

### Pointwise and uniform convergence

For a piecewise \(C^1\), periodic function with finitely many breakpoints, under standard Dirichlet-type regularity (e.g. piecewise bounded-variation derivatives), Fourier partial sums converge at \(t\) to \(\tfrac12(f(t^-)+f(t^+))\). For \(s\), \(P_N s(0)=0\) for all \(N\), although \(s\) has lateral limits \(-1,+1\). Thus convergence cannot be uniform across a jump. The Gibbs overshoot tends to approximately \(0.08949\) times the jump height above the limiting side value; for a jump of size \(2\), the overshoot is approximately \(0.17898\).

For \(g(t)=|t|\) on \([-\pi,\pi]\), \(a_n=-4/(\pi n^2)\) for odd \(n\), and \(0\) otherwise. Its Fourier series converges uniformly and absolutely; after formal differentiation the coefficient decay is only \(O(1/n)\), and the derivative does not exist at corners.

### Exercises with answers

1. What fraction of square-wave energy is captured by the first harmonic? **Answer:** \(8/\pi^2\approx81.06\%\). The residual mean-square error is \(1-8/\pi^2\), not the square root of that number.
2. Compute the mean-square error after the first three nonzero odd harmonics. **Answer:** \(1-(8/\pi^2)(1+1/9+1/25)\approx0.06694\); RMS error is its square root, approximately \(0.2586\).
3. A square wave is defined to equal \(17\) precisely at a switching point. Does its Fourier series converge there to \(17\)? **Answer:** No. Its Fourier coefficients ignore changes on a set of measure zero; at the jump the partial sums converge to the midpoint, zero.
4. Why does convergence in mean square not imply uniform convergence? **Answer:** Errors can concentrate in narrower and narrower regions, making their squared integral small while their maximum remains significant. Gibbs ripples exhibit this behavior.

### Sources and additional reading

- MIT OpenCourseWare, *18.03SC*, Operations on Fourier Series (convergence, Gibbs phenomenon): https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/operations-on-fourier-series/
- MIT OpenCourseWare, *18.03SC*, Fourier Series: Basics: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/fourier-series-basics/
- Wikipedia: [Gibbs phenomenon](https://en.wikipedia.org/wiki/Gibbs_phenomenon), [Parseval's theorem](https://en.wikipedia.org/wiki/Parseval%27s_theorem), [Convergence of Fourier series](https://en.wikipedia.org/wiki/Convergence_of_Fourier_series).
