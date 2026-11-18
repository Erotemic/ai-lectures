# Time–Frequency Resolution and the Gaussian Uncertainty Bound

<!-- BEGIN SPOKEN LECTURE -->

# Time–Frequency Resolution and the Gaussian Uncertainty Bound

A microphone records a short click at a known time. A long, steady tone announces a sharply defined pitch. Now try to make the click as brief as possible while making its spectrum as sharply concentrated as the steady tone's. Something prevents us. The click needs many frequencies to build its abrupt change. The pure tone needs many cycles to display one clean frequency. Time localization and frequency localization pull in different directions.

This is not merely a defect of one Fourier program. It is a property of Fourier analysis. We can make it precise by defining what we mean by the width of a signal in time, what we mean by the width of its spectrum, and proving that their product cannot be arbitrarily small.

Before proving anything, it is worth removing a common misconception. The spacing of Fourier bins, the actual ability to separate nearby tones, and the spread of a window's Fourier energy are three related but different quantities. A zero-padded transform may have many very closely spaced numerical bins while the signal still occupies the same short interval. We cannot buy frequency information by adding zeros.

## A window is a choice about time

Suppose a measurement is sampled eight thousand times per second. A window of two hundred fifty-six samples contains thirty-two milliseconds of data. Its ordinary unpadded Fourier grid has spacing thirty-one point two five hertz. A window of two thousand forty-eight samples contains two hundred fifty-six milliseconds and has grid spacing about three point nine hertz. The second window includes eight times as much observation time and therefore has eight times more finely spaced natural frequency bins.

Imagine two tones at four hundred forty and four hundred forty-five hertz. In the short window they make only a small difference in phase accumulation over the measured interval. Their patterns are difficult to separate by an ordinary windowed Fourier spectrum. The longer window lets them drift apart in relative phase over more cycles and gives a substantially better chance of resolving two peaks. This does not make the longer window universally preferable. If the second tone starts fifty milliseconds after the first, the long window may cover the onset and blend the two events. The short window may show the order more clearly while failing to separate their close frequencies.

This is a limitation of the information the window contains, but the precise separation threshold depends on noise, the window shape, and the analysis method. Under strong parametric assumptions, such as knowing in advance that there are exactly two pure sinusoids, one may infer closely spaced frequencies from short clean data. That is a different statistical problem from ordinary nonparametric Fourier resolution. Our uncertainty result concerns the simultaneous concentration of a signal and its transform, not an absolute rule that every possible estimator must have bins of a particular width.

## Width means more than interval length

A rectangular window has a definite start and end. A Gaussian window does not: it is largest at the center and decays smoothly away from it. How should we compare the widths of such different shapes? A useful answer is to treat the squared magnitude as an energy distribution. Normalize the energy so that it totals one. Compute its mean time and the square root of its mean squared distance from that center. Call this spread delta t.

Do the analogous calculation in frequency. Fourier transform the window, square the magnitude, normalize, and calculate the standard deviation of frequency about its center. Call that delta f. These are not arbitrary labels. They are ordinary standard deviations applied to continuous distributions of signal energy. A window may have a mathematical support interval that is infinite, yet have a finite standard deviation. Conversely, a sharp rectangular cutoff has a Fourier transform with slowly decaying sidelobes, and its frequency variance is infinite under this standard-deviation definition. Finite bin spacing does not contradict that fact.

We will use frequency measured in cycles per second rather than radians per second. That choice determines a factor of two pi in the theorem. For every sufficiently regular nonzero signal with finite time and frequency variances, delta t times delta f is at least one divided by four pi. That number is approximately zero point zero seven nine six, in dimensionless units.

The bound is surprisingly strict. If we force delta t toward zero for a sequence of windows, their delta f cannot stay bounded. If we force the frequency spread toward zero, the window must spread in time. No clever taper can break the inequality while retaining those definitions.

## Where the inequality comes from

The proof is a compact use of calculus and the Cauchy–Schwarz inequality. First move the window in time and modulate it in frequency so that its energy centers are both zero. Neither operation changes the two widths. Then rescale the window so that the integral of its squared magnitude is one.

Consider the derivative of time multiplied by squared window magnitude. Integrate that derivative over the whole real line. If the window decays sufficiently rapidly, the boundary terms vanish, so the integral is zero. Expanding the derivative gives one plus twice the real part of an integral involving time times the window times its derivative. Consequently the absolute value of that integral must be at least one half.

Cauchy–Schwarz bounds the same absolute integral by the time standard deviation multiplied by the square root of the integral of the squared derivative. Fourier differentiation tells us what that derivative norm means: differentiating in time multiplies the Fourier transform by two pi times frequency. Parseval's identity then converts the derivative norm to two pi times the frequency standard deviation. Put the two bounds together and one half is at most two pi times delta t times delta f. Divide by two pi, and we have the claimed lower bound of one divided by four pi.

The calculation has assumptions. We need enough decay and differentiability for integration by parts and Parseval to apply; more general formulations extend the conclusion. A discontinuous rectangular window does not satisfy the simplest derivative argument and does not secretly defeat it. Its spectrum has too much high-frequency energy for a finite frequency variance.

## Why Gaussian windows are special

A Gaussian is a bell-shaped curve whose decay is controlled by a scale sigma. Let the window be the exponential of negative time squared divided by twice sigma squared. Its squared magnitude is another Gaussian, with a time standard deviation equal to sigma divided by the square root of two. Its Fourier transform is also Gaussian. Under our cycles-per-second convention, the Fourier-energy standard deviation is one divided by twice the square root of two times pi times sigma.

Multiply them. Sigma cancels, and the product is precisely one divided by four pi. The Gaussian attains equality. This is the exact sense in which it is optimally concentrated in time and frequency under the standard-deviation criterion.

A wider Gaussian multiplies delta t by the width factor and divides delta f by the same factor. A narrower Gaussian does the reverse. It cannot improve both spreads at once. Notice also that a Gaussian never truly ends. A finite implementation truncates it, creating a small change to the ideal formula. We should distinguish the mathematical optimum on the entire real line from a finite array of window weights.

This result is sometimes called the time–frequency uncertainty principle, or the Gabor uncertainty relation. Its mathematical kinship with the quantum uncertainty principle is real, but our argument concerns a classical signal and a Fourier transform. No assumption about particles or measurements was needed.

## What the window shape changes

The Gaussian minimizes the product of variance-based spreads, but other criteria can favor other windows. In a spectrum with a very strong tone next to a faint one, sidelobe suppression may matter more than minimum variance. Hann and related tapers lower far-out leakage at the cost of broadening the main spectral lobe. A rectangular window has a narrow central lobe but more substantial sidelobes. Nothing about the Gaussian theorem says every engineering task should use a Gaussian window.

Consider an abrupt pulse. A long window can show its broad spectrum very well, but it spreads the pulse visually across every local spectrum that overlaps it. A short window confines that burst to fewer neighboring time columns, yet the local frequency plot gets broader and less detailed. For a sustained pair of close tones, the balance reverses: long windows give better ordinary spectral separation, while precise onset localization may be less important.

The hop length adds a second design decision. We may compute a spectrum every ten milliseconds even with a two-hundred-millisecond window. That supplies many overlapping frames and makes a smooth display, but each frame still uses two hundred milliseconds of data. A ten-millisecond hop does not mean ten-millisecond intrinsic time resolution. Similarly, an FFT padded to sixteen thousand points still cannot distinguish frequencies for which the original short window supplied too little evidence.

## Frequency drift inside a window

Suppose the pitch climbs continuously, like a whistle being slowly raised. A window centered at a particular time contains slightly lower frequencies near its beginning and slightly higher frequencies near its end. The local spectrum therefore spreads across the frequencies swept during that interval, in addition to the spreading caused by the window itself. Making the window shorter reduces this within-window drift but widens the window's own Fourier response. We can select a useful compromise by comparing the expected rate of frequency change with the expected separation of distinct components.

There is no perfect compromise for every moment of every signal. Multi-resolution methods use different window sizes for different frequencies or circumstances; a wavelet transform is one familiar example. Those methods shift the tradeoff rather than eliminate it. Different mathematical questions call for different definitions of localization and different analysis bases.

## How to choose a window deliberately

Before drawing a spectrogram, decide what event you are trying to discover. To detect the arrival time of a brief impact, start with a short window and inspect the expected time smearing. To distinguish two sustained neighboring notes, start with a longer window and inspect the main-lobe width. To follow a moving ridge, choose a window short enough that the frequency does not sweep too far inside each frame, but long enough that the ridge remains spectrally meaningful. Test the result with more than one window length when your conclusion depends on that choice.

The uncertainty inequality tells us why these decisions are unavoidable. A signal cannot be arbitrarily concentrated in both time and frequency under the usual energy-spread measurements. The Gaussian tells us what the mathematically optimal compromise looks like for that criterion. Everything else—tapers, hop lengths, zero padding, and the details of a frequency plot—must be interpreted in light of that fundamental limit.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: an exact Fourier uncertainty proof

Use the cycles-per-second convention \(\widehat g(f)=\int_{\mathbb R}g(t)e^{-2\pi i ft}\,dt\), with \(\|g\|_2=1\). After shifting time and modulating frequency to center both energy distributions, define
\[
(\Delta t)^2=\int t^2|g(t)|^2\,dt,\qquad
(\Delta f)^2=\int f^2|\widehat g(f)|^2\,df.
\]
For a sufficiently smooth, decaying \(g\),
\[
0=\int (t|g(t)|^2)'\,dt
 =1+2\operatorname{Re}\int t g'(t)\overline{g(t)}\,dt.
\]
Cauchy–Schwarz and Plancherel give
\[
\frac12\leq \left|\int t g'\bar g\,dt\right|
 \leq \Delta t\,\|g'\|_2
 =2\pi\Delta t\,\Delta f,
\]
so \(\boxed{\Delta t\,\Delta f\ge1/(4\pi)}\).

For \(g(t)=C e^{-t^2/(2\sigma^2)}\), its energy density is proportional to \(e^{-t^2/\sigma^2}\), so \(\Delta t=\sigma/\sqrt2\). The Fourier transform is \(C\sigma\sqrt{2\pi}\,e^{-2\pi^2\sigma^2 f^2}\), whose squared magnitude is proportional to \(e^{-4\pi^2\sigma^2 f^2}\), giving \(\Delta f=1/(2\sqrt2\pi\sigma)\). Equality follows.

At sample rate \(f_s=8000\) Hz, window lengths 256 and 2048 samples correspond to durations 0.032 and 0.256 s. Their unpadded FFT grids have spacings \(f_s/L=31.25\) and \(3.90625\) Hz. These are **grid spacings**, not a universal theorem about frequency estimation accuracy. A rectangular window's Fourier-energy variance is infinite due to its nonsquare-integrable derivative; this does not make its finite sample DFT undefined.

### Exercises with worked answers

1. What is the unpadded DFT bin spacing for 800 samples at 8000 samples per second? **Answer:** ten hertz.
2. If a Gaussian window's time spread doubles, what happens to its spectral spread? **Answer:** it halves, keeping the product at \(1/(4\pi)\).
3. A 256-sample window is analyzed with a 4096-point FFT. How much more observed signal was supplied? **Answer:** none. The extra points are zeros, supplying a denser frequency grid but not longer observation.
4. Why is a rectangular window not a counterexample to the standard-deviation uncertainty relation? **Answer:** its continuous Fourier-energy second moment diverges because of its sharp edges.
5. What physical event favors a shorter window: distinguishing two long stable tones five hertz apart, or locating a quick impact? **Answer:** the impact; spectral separation of nearby sustained tones generally favors a longer window.
6. Why does reducing the hop size not remove the blur of a long window? **Answer:** the hop samples the resulting time-frequency distribution more often, but each transform still averages over the long window.

### Sources and further reading

- [Wikipedia: Gabor limit](https://en.wikipedia.org/wiki/Gabor_limit).
- [Wikipedia: Short-time Fourier transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform).
- [SciPy `ShortTimeFFT`: window and hop definitions](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ShortTimeFFT.html).
- [NumPy Fourier transforms and frequency bins](https://numpy.org/doc/stable/reference/routines.fft.html).
