# Reading a Spectrum without Being Fooled: Phase, Leakage, and Windows

<!-- BEGIN SPOKEN LECTURE -->

# Reading a Spectrum without Being Fooled

Suppose an instrument produces a plot with one tall spectral peak. What have we learned? Perhaps it detected a periodic tone. Perhaps it observed a short burst whose energy happens to concentrate near that frequency. Perhaps the original signal contained a higher tone that aliased to a lower one. Or perhaps a slightly off-grid tone has spread its energy among several plotted bins. A spectrum is a calculation about data. It becomes a statement about the physical world only after we account for how those data were acquired and interpreted.

We have derived the discrete Fourier transform as an exact change of coordinates for an array. Now we will learn to read those coordinates. We need the sample rate to label the horizontal axis, the transform normalization to label the vertical axis, and the complex phase to understand timing. We will also examine what happens when we cut a record out of a longer signal. That cut creates a window, whether or not we deliberately chose one.

## Recovering a signal from its coefficients

Consider a sensor that records eight samples in one second, one sample every eighth of a second. Suppose the measured values are five, three, negative one, one, and then the same four values again. The sequence looks somewhat lopsided, but it has a simple description. Its mean is two. Above that mean, it contains three times a cosine of two cycles per second plus one times a sine of the same frequency.

We can verify the claim without a transform library. At time zero, cosine is one and sine is zero, so the value is two plus three, or five. One sample later, cosine has advanced by a quarter cycle and is zero, while sine is one, giving two plus one, or three. At the next sample cosine is negative one and sine is zero, giving negative one. Another quarter cycle gives sine negative one and brings the value to one. Then the pattern repeats.

What does the eight-point DFT produce? The zero-frequency coefficient is sixteen, because the sum of the eight measurements is eight times their mean of two. At positive frequency index two it produces twelve minus four i. At the conjugate negative frequency index six it produces twelve plus four i. All other coefficients vanish in exact arithmetic. These three nonzero coefficients are sufficient to reconstruct all eight numbers.

The magnitude of the coefficient at index two is four times the square root of ten. That is not the physical sinusoidal amplitude. Since this is a paired, non-Nyquist bin, divide the magnitude by four, which is half our sample count. The physical amplitude is the square root of ten, about three point one six. The phase tells us how the cosine and sine components combine. In fact, three cosine plus one sine is a cosine of amplitude square root ten shifted by a small fraction of a cycle. A plot of coefficient magnitudes alone would not tell us that shift.

This example provides a practical recipe. Read the zero-frequency coefficient as the sum, not the mean. Convert its value to a mean by dividing by the sample count. Pair positive and negative frequencies for real data. Scale ordinary paired-bin magnitudes by two divided by N to recover an amplitude when the tone exactly occupies a bin. Treat the Nyquist bin separately when N is even. Finally, keep the phase if timing or reconstruction matters.

## Why a single tone can occupy several bins

Our example was exceptionally tidy because exactly two cycles fit in the one-second record. Change the physical frequency from two to two and a half cycles per second while keeping the same sample rate and observation duration. The tone now completes two and a half cycles in the window. A discrete Fourier transform still uses basis functions that complete integer numbers of turns across the N-point period. No one basis function matches the measured samples of this tone in general.

The DFT therefore distributes the signal among several frequency bins. This is spectral leakage. It is not necessarily multiple physical oscillations. It occurs because the finite record is analyzed as if its samples repeated periodically. When the record ends in a phase that does not join smoothly to its beginning, that artificial periodic continuation has a mismatch, and representing the mismatch requires additional Fourier modes.

The distinction between leakage and aliasing is worth fixing in your memory. Aliasing happens at the sampling stage: different continuous frequencies can give identical samples. Leakage happens when a finite set of samples is decomposed using the discrete frequency grid: a component that is not centered on one of those frequencies generally contributes to several bins. We can often reduce leakage by changing our analysis window. We cannot recover an unmeasured high frequency merely by changing a window after sampling.

A finite-length recording is already a windowed signal. In mathematical language, we multiplied the long signal by a rectangular window: one during the chosen time interval, zero outside. Multiplication in time corresponds to mixing nearby frequency components through convolution. A rectangular window has pronounced sidelobes in frequency, so a strong off-bin tone can contaminate several weaker bins. You may see a row of smaller peaks and mistake them for additional physical tones.

## Tapering the endpoints

One remedy is to give the first and last samples less weight. A Hann window, for example, rises smoothly from zero, reaches its largest weight near the middle, and falls back to zero. Applied before the DFT, it reduces the abrupt jump where the repeated record joins. This usually reduces distant spectral sidelobes substantially for an isolated sinusoid that is not exactly bin-centered.

There is a tradeoff. A smooth taper broadens the central lobe around a tone. Two nearby tones may become harder to distinguish in the tapered spectrum, even while distant leakage is less distracting. Also, multiplying by a window reduces the total signal amplitude. If you want a quantitative amplitude estimate rather than a qualitative plot, you must account for the window's gain. Some software handles this correction when asked for an amplitude spectrum; some leaves the normalization to you. We should never transfer the simple two-over-N amplitude rule blindly to arbitrary windows.

There is no single window that is best for every measurement. If we need to detect a weak frequency near a much stronger one, sidelobe suppression matters. If we need to resolve two tones of nearly equal strength and nearby frequencies, mainlobe width matters. If the signal is a brief event, a window chosen for steady sinusoids may distort the event's shape. State what question the spectrum is intended to answer before choosing the window.

## Zero padding and the meaning of resolution

Another common operation is to append zeros to the array before taking the DFT. Suppose we have one second of measurements and add three seconds' worth of zeros. The resulting longer array has a more closely spaced set of DFT frequencies. The plotted spectrum looks smoother, and a peak may be located more conveniently between the original bins. But the original observation interval was still one second long. No new physical measurements have been created.

Zero padding interpolates the frequency sampling of the finite windowed record. It does not supply the information that would have been obtained by observing the system for four actual seconds. If two tones are too close to separate reliably using the original one-second data, adding zeros is not equivalent to collecting four seconds of new data. We may obtain a prettier picture without overcoming the fundamental limit imposed by recording duration, noise, and the chosen window.

We should be similarly careful with the word resolution. Frequency-bin spacing is the distance between labels used by a particular DFT. The ability to resolve physical tones depends on that spacing but also on the window, duration, relative amplitudes, signal model and noise. Zero padding makes the bin spacing smaller. It does not, by itself, improve the underlying resolving power of the actual observation.

## A spectrum is more than a picture of amplitude

For real data, the DFT coefficients on the second half of the array repeat the information from the first half by complex conjugation. This lets software show a one-sided spectrum, including the zero-frequency component and, for even N, the Nyquist component. It is convenient but it creates a common plotting error: doubling every bin indiscriminately. The paired interior bins need a factor of two when converting two-sided coefficients to a one-sided amplitude; zero and Nyquist do not.

Magnitude squared is often called spectral energy or, after choosing suitable units and normalization, spectral power. These are not interchangeable labels without definitions. Parseval's identity tells us how the sum of squared sample values corresponds to the sum of squared Fourier coefficients. It does not automatically prescribe a physical power spectral density in units per hertz. A density intended for comparing recordings of different lengths or windows needs explicit conventions and, for random signals, statistical choices.

The complex phase can be just as important as the magnitude. Moving a pulse around a periodic array multiplies each frequency coefficient by a phase factor. Its magnitudes do not change, yet the pulse appears in a different place. In imaging, communication, and solving PDEs, discarding phase can therefore discard the geometry or timing of the object we want to reconstruct.

## Multiplying transforms and the danger of wraparound

There is a useful reward for learning these conventions. Convolution, the operation that builds a filtered signal from shifted copies of an impulse response, becomes multiplication of discrete Fourier coefficients. But there is a catch. The DFT views both arrays as periodic. The multiplication therefore corresponds to circular convolution, in which the part of a shifted response that extends beyond the array's right edge wraps around to the left.

For a tiny example, take the two-point arrays one, one and one, one. Their ordinary linear convolution is one, two, one: there are three output positions because two finite pulses overlap and then separate. Their two-point circular convolution is two, two. The first and last contributions from linear convolution have wrapped to the same position. There is no arithmetic error, only a different boundary condition on the array.

If we want ordinary linear convolution from Fourier multiplication, we can pad both sequences with zeros until the transform length is at least the sum of their lengths minus one. For our two-point example, a transform length of three or more suffices. This zero padding has a different role from padding merely to smooth a spectrum plot: here it prevents unwanted circular wraparound in a computation.

This matters directly for differential equations. A heat kernel represents smoothing by convolution; a transfer function represents a system's response to forcing. When we implement these ideas numerically with transforms, we must distinguish a periodic model from an interval with open or fixed boundaries. An FFT does not decide the physical boundary conditions for us.

## What a trustworthy interpretation includes

A careful spectrum report needs more than the largest peak. It should give the sampling rate and sample interval, the number of actual measurements, and the duration represented. It should say whether the input was filtered before sampling or downsampling, and whether a window or zero padding was used before the transform. It should declare whether the vertical axis shows raw coefficient magnitude, one-sided amplitude, energy, power, or a density. Where possible, inspect phase and reconstruct the data as a check.

In return, we gain a remarkably flexible way to reason about signals. An exact small DFT tells us how a finite record decomposes. Window analysis tells us which features of its spectrum may result from measurement choices. Convolution connects frequency multiplication to physical responses. Once we keep these distinctions straight, the spectrum becomes an instrument we can question rather than a verdict we must accept.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: windowing, scaling, and circular convolution

Eight data values \(x_n=2+3\cos(\pi n/2)+\sin(\pi n/2)\) give
\[
(x_0,\ldots,x_7)=(5,3,-1,1,5,3,-1,1),\quad
X_0=16,\ X_2=12-4i,\ X_6=12+4i.
\]
The physical sinusoidal amplitude is \(2|X_2|/8=\sqrt{10}\); its cosine-representation phase is \(\arg X_2=-\arctan(1/3)\). A bin-centered real tone \(A\cos(2\pi k n/N+\phi)\) has \(X_k=(AN/2)e^{i\phi}\) and \(X_{N-k}=\overline{X_k}\) when \(0<k<N/2\).

A symmetric Hann window of length \(N>1\) is
\[
 w_n=\frac12\left(1-\cos\frac{2\pi n}{N-1}\right),\qquad n=0,\ldots,N-1.
\]
For a bin-centered sinusoid with negligible negative-frequency cross-term under a sufficiently long/tailored window, the typical coherent-gain amplitude correction uses \(\sum w_n\) instead of \(N\); this heuristic is not exact for all short sequences, arbitrary phases or non-bin-centered tones. Window choice trades spectral sidelobes for mainlobe width. Zero-padding \(x\) before a DFT samples its finite-length discrete-time Fourier polynomial on a denser frequency grid; it does not extend the measured time interval.

For two length-\(N\) sequences, circular convolution is
\[
(x\circledast h)_n=\sum_{m=0}^{N-1}x_m h_{(n-m)\bmod N},\qquad
\mathcal D_N(x\circledast h)_k=X_kH_k.
\]
A linear convolution of lengths \(L\) and \(M\) has support of at most \(L+M-1\) entries, so padding each input to a common transform length \(N\ge L+M-1\) prevents circular wraparound. Example: \((1,1)*(1,1)=(1,2,1)\), whereas length-two circular convolution is \((2,2)\).

A finite record of duration \(T\) naturally has bins spaced by \(1/T\). Replacing the rectangular window by a taper changes the spectrum through convolution with the window's frequency response; the side-lobe/main-lobe tradeoff is not a correction for aliasing at acquisition.

### Exercises with worked answers

1. For the eight-sample example, what is the mean and what is the positive two-hertz coefficient? **Answer:** mean \(2\); \(X_2=12-4i\).
2. Find the one-sided amplitude at the two-hertz bin, assuming the unwindowed DFT convention. **Answer:** \(2\sqrt{12^2+4^2}/8=\sqrt{10}\).
3. If a sinusoid fills two and a half cycles of a one-second rectangular record, is a spread-out DFT peak necessarily evidence of several tones? **Answer:** no. The finite-record periodic continuation generally produces spectral leakage.
4. Why can't zero padding a one-second recording deliver the discrimination of four seconds of actual measurements? **Answer:** it does not add independent observations of the original signal.
5. What transform length is sufficient for a linear convolution of arrays of lengths seven and five? **Answer:** at least eleven.
6. When plotting a one-sided amplitude spectrum of real even-length data, which bins should not be doubled? **Answer:** the DC bin and the Nyquist bin.
7. Suppose two equal-length records have different sampling rates but both have duration \(T\). Which feature is the same? **Answer:** their natural bin spacing \(1/T\), although Nyquist frequencies differ.

### Sources and further reading

- [NumPy FFT conventions, real-input transforms, and normalization](https://numpy.org/doc/stable/reference/routines.fft.html).
- [NumPy FFT frequency labels for real-input transforms](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html).
- [FFTW User Manual, *Complex One-Dimensional DFTs*](https://www.fftw.org/doc/Complex-One_002dDimensional-DFTs.html).
- [Wikipedia: Window function](https://en.wikipedia.org/wiki/Window_function).
