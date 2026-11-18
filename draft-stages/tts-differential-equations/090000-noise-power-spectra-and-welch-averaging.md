# Noise, Power Spectral Density, and Welch Averaging

<!-- BEGIN SPOKEN LECTURE -->

# Noise, Power Spectral Density, and Welch Averaging

A spectrogram of a clean tone can look reassuringly simple: a bright narrow band with darkness elsewhere. Real measurements are rarely that tidy. A microphone hears the room and its own electronics. A sensor measures not only the process of interest but fluctuations in the detector and environment. In a single Fourier spectrum, those fluctuations can create dramatic peaks that disappear when you repeat the measurement. We need a way to distinguish a reproducible oscillation from the random variation of noise.

The right tool begins with power spectral density. The phrase has three parts: power tells us about squared signal amplitude, spectrum tells us how that power is distributed over frequency, and density means per unit of frequency. We will derive the normalization using discrete white noise, then see why averaging periodograms makes estimates steadier, and finally return to a subtle question: what information is lost when the underlying signal changes with time?

## Variance is a total, density is a distribution

Suppose a voltage sensor reads a value in volts. The variance of its fluctuations has units volts squared. If we distribute that variance across a frequency axis measured in hertz, we need a power spectral density with units volts squared per hertz. Integrating the density over the measured frequency band should recover the variance, under the appropriate normalization and stationarity assumptions.

This already gives us a way to catch an error. If someone says a noise spectral density is simply five volts squared without specifying the frequency bandwidth, they may be reporting power rather than density. If they double the number of displayed FFT bins by adding zeros, the total noise variance cannot have magically doubled. A correct density normalization keeps track of the bandwidth represented by each bin.

For a finite sampled signal, a periodogram is a common estimate of spectral density. We window a record, compute the squared magnitude of its discrete Fourier transform, and divide by factors involving sampling rate and window energy. The precise formula depends on one-sided or two-sided conventions. It is worth deriving one case fully instead of relying on whichever default happens to be in a software library.

## White noise as a controlled example

Consider discrete noise samples with mean zero, variance one quarter, and no correlation between distinct sample times. Independent samples are one example. The name white noise means that its ideal power spectrum is flat across the available frequencies. For real sampled data at one hundred samples per second, the Nyquist interval runs from negative fifty to positive fifty hertz. Its width is one hundred hertz.

If the variance is one quarter and the two-sided density is flat across this interval, that density must be one quarter divided by one hundred, or zero point zero zero two five, in squared signal units per hertz. The integral of this constant over a hundred-hertz band gives back one quarter.

For a real signal, a one-sided spectrum folds the negative-frequency power onto the positive side. Away from zero and the Nyquist endpoint, the one-sided density is twice the two-sided density. So our ideal noise floor is zero point zero zero five squared units per hertz on the positive-frequency interior. The special endpoint bins are not doubled because they have no distinct negative-frequency partners in an even-length real DFT.

These numbers are not arbitrary plotting choices. They follow from preservation of total variance under Fourier analysis and the one-sided convention. Their interpretation still depends on the signal units and the sampled bandwidth. The noise before sampling might not be flat above Nyquist, and an analog anti-alias filter matters for what variance actually enters the sampled band.

## Why a single periodogram is noisy

Take a rectangular block of one hundred samples. Let its discrete Fourier transform be X at each frequency bin, using an unnormalized forward transform. For a two-sided density estimate, divide the squared magnitude at each bin by the product of sampling rate and block length. For a real one-sided periodogram, double the positive interior values.

Why that denominator? With independent mean-zero noise of variance one quarter, the expected squared magnitude of each Fourier coefficient is the number of samples times the variance: one hundred times one quarter, or twenty-five. Divide twenty-five by one hundred times one hundred, and the expected two-sided periodogram is zero point zero zero two five. Fold the positive and negative bins together, and the interior mean becomes zero point zero zero five, as predicted from the total variance.

Now comes the surprise. Even though the expected periodogram is correct for white noise, one particular periodogram can be extremely jagged. At one frequency it may be much higher than the expected level, and at another much lower. Increasing the record length gives us more closely spaced bins, but it does not automatically make the relative random fluctuation at each individual raw periodogram bin disappear. A single prominent narrow spike can be just a fluctuation. We cannot declare it a physical tone on height alone.

In the ideal Gaussian white-noise model, a nonendpoint complex Fourier coefficient has approximately independent real and imaginary Gaussian parts. Its squared magnitude fluctuates strongly around its expectation, with a variance comparable to the square of its mean. The raw periodogram is therefore an inconsistent estimate at a fixed underlying frequency without additional smoothing or averaging, even though it has a well-behaved expectation in this idealized case.

This is the motivation for averaging several modified periodograms rather than trusting one.

## Welch's construction

Peter Welch described a practical method in 1967. Divide a long record into shorter pieces, optionally with overlap. Apply a window to each piece. Compute a periodogram of each windowed piece, with normalization by the window's squared weights. Average the periodograms at each frequency. The result is commonly called Welch's power spectral density estimate.

The word average is the crucial one. If the pieces are independent and follow the same stationary noise law, averaging M periodograms reduces the variance of the estimate roughly in proportion to one divided by M. The standard deviation falls roughly like one divided by the square root of M. Thus ten times more effectively independent pieces give roughly a square-root-of-ten improvement in the size of relative random fluctuations, not a tenfold improvement.

Overlapping pieces are not independent. Two windows that share half their samples may have substantially correlated noise estimates. Overlap can improve use of the record and interact helpfully with a taper, but it does not create independent evidence by copying measurements into additional windows. The actual variance reduction depends on overlap, window shape, and the noise process.

Averaging also costs frequency resolution. If the full record has ten thousand samples but each Welch segment uses only one thousand, the unpadded frequency spacing comes from one thousand samples, not ten thousand. We gain a steadier spectrum by giving up some ability to resolve closely spaced narrow components. This is another compromise, but it is not the same mathematical tradeoff as time–frequency uncertainty: here the trade involves estimator variance, bias, segment length, and spectral leakage.

## A tone sitting on a noise floor

Put a one-hertz-amplitude cosine at twenty hertz into the white noise example. Sample at one hundred hertz, and take a block of one hundred samples, exactly one second long. In the absence of noise, the cosine completes twenty cycles and lies exactly on a DFT frequency bin. Its one-sided periodogram value at twenty hertz is one half, in squared units per hertz, because the tone's mean squared amplitude is one half and the natural bin width is one hertz.

The ideal noise contributes an expected floor of zero point zero zero five at that same interior bin. So the expected periodogram at the tone bin is about zero point five zero five, while at other interior bins without the tone it is zero point zero zero five. This makes a striking contrast in expectation. A real finite noisy record will fluctuate around those figures, especially if the noise is not exactly stationary or independent.

Do not call the tone's peak height a universal physical spectral density of a pure mathematical cosine independent of record length. An infinite-duration pure tone has a spectral line, represented by a delta contribution in ideal spectral measures. A finite-window periodogram spreads that line across a width determined by the window. Doubling the segment duration changes the peak height of the density estimate because the same integrated tone power is concentrated into a narrower frequency region. Integrated power and peak density are different quantities.

The units expose the distinction. The underlying cosine has amplitude one. Its mean squared amplitude is one half. The one-second, one-hertz-wide periodogram bin happens to have density one half per hertz. With a two-second rectangular observation and a half-hertz-wide bin, the on-bin density peak doubles while the integrated tone power stays one half. That is exactly what a density should do when the same amount is concentrated into half as much width.

## Window normalization matters

A tapered window reduces spectral leakage but also changes the energy of the time-domain block. If we kept dividing by the number of samples as though every window weight were one, the noise floor would change just because we chose a different taper. The appropriate two-sided windowed density divides by the sampling rate times the sum of the squared window weights. For white noise, the expectation of the normalized density remains the same, regardless of window shape, provided the assumptions about the noise hold.

One-sided doubling still has to be handled correctly. Zero and the Nyquist endpoint of an even-length real transform are not doubled. The density scale must also be distinguished from a spectrum scale that is normalized to report amplitude or power per spectral line rather than per hertz. Software often offers both. Checking the documentation is part of interpreting the measurement.

## Stationary noise is not the same as a transient

Welch averaging assumes that the same relevant statistical properties persist across the pieces being averaged, at least approximately. If a motor changes speed halfway through a measurement, the averaged spectrum may show peaks corresponding to both speeds without telling us when either occurred. If a click happens only once, averaging it with many quiet segments weakens its apparent prominence. That may be useful for estimating the stationary background but poor for detecting the click.

A spectrogram keeps the time axis and therefore exposes a changing tone or localized burst. A Welch spectrum deliberately collapses the time axis in exchange for reduced statistical fluctuation. Both calculations use windowed Fourier transforms, but they answer different questions. One asks what happened when. The other asks what average power distribution characterizes a reasonably stationary interval.

The underlying noise itself can be colored. A sensor may have stronger low-frequency fluctuations than high-frequency fluctuations. Interference may produce narrow peaks, periodic machinery may contribute harmonics, and the recording device may impose a frequency-dependent transfer function. A bright line is evidence of spectral concentration, not by itself proof of a biological, mechanical, or electrical source. The experiment and instrument must supply that interpretation.

## What a credible spectral claim looks like

If you want to claim a twenty-hertz oscillation in noisy data, begin by stating the sampling frequency and the relevant anti-alias conditions. Identify whether you removed a mean or trend. Choose the window and segment duration with enough cycles to separate twenty hertz from plausible alternatives. State whether you show one periodogram, a spectrogram, or a Welch average. Include the units: squared signal units per hertz for density. Ask whether a large peak persists across separate parts of the record and whether it changes when you alter the window or segment length. A persistent tone should survive reasonable analytic choices, although its exact peak height and width will change with them.

For a transient or chirp, preserve the time axis instead of interpreting a global average as a narrative of events. For stationary noise, average enough data to reduce the jaggedness of a single estimate without pretending the overlapped segments are independent. If you need confidence intervals, you must account for the estimator's degrees of freedom and the statistical model; an attractive smooth curve is not a substitute.

The Fourier transform is deterministic. Noise estimation is statistical. Those two facts belong together but should not be confused. A transform tells us exactly what coefficients a particular finite record has. A spectral estimator tells us what those coefficients suggest about an underlying random process. Learning the distinction is what turns a colorful spectral plot into a quantitative scientific argument.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: white-noise periodograms and Welch normalization

Let \(\epsilon_n\) be real, zero-mean, uncorrelated noise with \(\mathbb E[\epsilon_n\epsilon_m]=\sigma^2\delta_{nm}\). For the unnormalized DFT \(X_k=\sum_{n=0}^{L-1}\epsilon_n e^{-2\pi i kn/L}\),
\[
\mathbb E|X_k|^2=\sum_{n,m}\mathbb E[\epsilon_n\epsilon_m]e^{-2\pi ik(n-m)/L}=L\sigma^2.
\]
The rectangular-window two-sided periodogram is \(P_2(f_k)=|X_k|^2/(f_sL)\), with \(\mathbb E[P_2]=\sigma^2/f_s\). For even \(L\) and real data, the one-sided version doubles the interior bins \(1\le k<L/2\), and does not double \(k=0\) or \(k=L/2\). The expected one-sided interior level is \(2\sigma^2/f_s\).

For a general real analysis window \(w[n]\), define \(U=\sum_{n=0}^{L-1}w[n]^2\) and \(X_w[k]=\sum_n w[n]x[n]e^{-2\pi i kn/L}\). The two-sided windowed density estimator is
\[
P_w(f_k)=\frac{|X_w[k]|^2}{f_s U}.
\]
For white noise, \(\mathbb E|X_w[k]|^2=\sigma^2 U\) and thus \(\mathbb E P_w=\sigma^2/f_s\). Welch's estimate averages these windowed periodograms over \(M\) segments: \(\hat S(f_k)=M^{-1}\sum_{m=1}^M P_{w,m}(f_k)\), with one-sided corrections when appropriate. Correlated overlapping windows reduce the effective independent count.

For \(f_s=100\) Hz, \(\sigma^2=1/4\), the two-sided PSD is 0.0025 units\(^2\)/Hz and the positive-frequency interior one-sided PSD is 0.005 units\(^2\)/Hz. For a pure \(A\cos(2\pi f_0 n/f_s)\) exactly on a nonendpoint bin of a rectangular length-100 record with \(A=1\), \(f_0=20\) Hz, \(P_1(f_0)=A^2 L/(2f_s)=0.5\) units\(^2\)/Hz. With independent zero-mean white noise, the *expected* corresponding bin estimate is 0.505, not a guarantee for any one record.

### Exercises and worked answers

1. Variance \(\sigma^2=0.36\) at \(f_s=120\) Hz: what is the two-sided flat density? **Answer:** 0.003 units\(^2\)/Hz.
2. What is the positive-frequency interior one-sided density in that example? **Answer:** 0.006 units\(^2\)/Hz.
3. For independent unit-variance samples and length \(L=80\), what is \(\mathbb E|X_k|^2\)? **Answer:** 80 for every DFT bin.
4. For a rectangular window of length 100 and sample rate 100 Hz, what is the one-sided periodogram peak of an exactly on-bin unit-amplitude interior cosine? **Answer:** 0.5 units\(^2\)/Hz.
5. Why is the denominator \(f_s\sum_nw[n]^2\), rather than always \(f_sL\), used for a tapered-window PSD? **Answer:** it compensates for the window's changed noise energy and gives the correct white-noise expectation.
6. If ten periodograms share most of their samples, can we treat them as ten independent estimates? **Answer:** no; their statistical dependence reduces effective averaging.
7. What information does Welch averaging discard that a spectrogram retains? **Answer:** the order and time locations of spectral changes.
8. Does a taller line-density peak in a longer record imply that the underlying cosine became more powerful? **Answer:** no; the integrated line power may be the same while the frequency concentration gets narrower.

### Sources and further reading

- [Peter D. Welch, *The Use of Fast Fourier Transform for the Estimation of Power Spectra* (IEEE Transactions on Audio and Electroacoustics, 1967)](https://doi.org/10.1109/TAU.1967.1161901).
- [SciPy `signal.welch`: density scaling, windowing, overlap, and averaging](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html).
- [SciPy `signal.csd`: cross-spectral density and normalization](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.csd.html).
- [SciPy `ShortTimeFFT.spectrogram`: retained time axis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ShortTimeFFT.spectrogram.html).
- [Wikipedia: Spectral density](https://en.wikipedia.org/wiki/Spectral_density).
