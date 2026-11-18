# A Fourier Transform You Can Calculate by Hand: The Discrete Fourier Transform

<!-- BEGIN SPOKEN LECTURE -->

# A Fourier Transform You Can Calculate by Hand

Take four measurements of a vibrating system: one, zero, negative one, zero. The values could have been read from a microphone or a position sensor. We want a way to decide which oscillations are present, but we do not want to guess a continuous curve between the measurements. We have only four numbers. Can we analyze them as they stand?

The discrete Fourier transform answers yes. It is a change of coordinates for a finite vector, not an approximation to be accepted on faith. Four numbers go in, four complex coefficients come out, and an inverse operation recovers the four numbers exactly in exact arithmetic. With a small example we can do every step by hand. From that calculation we will derive the general definition, discover why negative frequencies appear near the end of the output array, and obtain an energy identity that checks the answer.

There is also an important limitation. An exact representation of a finite array is not necessarily an exact reconstruction of the continuous physical signal that produced the array. Sampling can already have hidden high frequencies. The DFT faithfully analyzes what is in the array; it cannot undo that loss.

## Four samples and four oscillations

Suppose our measurement rate is four samples per second, and we take four samples over one second, at time zero, one quarter, one half, and three quarters. The values are one, zero, negative one, and zero. A one-cycle-per-second cosine hits those exact values. So we expect the frequency analysis to find a one-cycle component.

We must decide what frequencies to use when representing just four samples. We start with a constant pattern. Then use the complex oscillation that advances by one quarter of a turn between samples. Next use one that advances by two quarters of a turn. Finally use one that advances by three quarters. Those are four different patterns on the four-point grid, even though one and three quarters can be interpreted as opposite directions of rotation. Each has four values, and they form a basis of the space of four complex sample vectors.

To find how much of each pattern is present, multiply each sample by the opposite rotation at that frequency and add the results. For the zero-frequency pattern, this is just the sum of the samples: one plus zero minus one plus zero, which is zero. There is no constant offset.

For the one-cycle pattern, the opposite rotations at the four sample points are one, negative i, negative one, and positive i. Multiplying the sample values gives one, zero, positive one, and zero. Their sum is two. The next pattern, advancing by half a turn per sample, has opposite rotations one, negative one, one, negative one. Its weighted sum is zero. The final pattern gives a sum of two again.

The four Fourier coefficients are therefore zero, two, zero, two. Why two identical peaks? The original measurements are real numbers. A cosine is the average of a forward rotating complex oscillation and a backward rotating one. On a four-point grid, frequency index three describes the same samples as frequency minus one. The pair at indices one and three together represents our real cosine. We have not found two unrelated physical tones; we have found the conjugate pair that makes one real oscillation.

## Deriving the general formula

Now replace four by any positive number N. Label the samples from zero through N minus one. A candidate frequency index k produces a complex pattern that rotates through k complete turns across N sample positions. At sample n its value is an exponential whose angle is two pi times k times n divided by N. Think of it as cosine plus i times sine. The transform coefficient at index k is the sum of the samples multiplied by the complex conjugate of this pattern; that is, the exponential with the negative angle.

Why should this work? Imagine taking the weighted sum of two different candidate patterns. As n runs through the N sample points, their relative phase moves around the unit circle in equal steps. Unless their frequency indices are the same modulo N, those rotating contributions cancel. It is the discrete version of the orthogonality of sines and cosines over a full period.

If the indices do agree modulo N, each contribution is one and the sum is N. Therefore, dividing the weighted sum by N gives the coefficient of one basis pattern in the reconstruction. Our forward transform is the unnormalized sum, so our inverse transform divides by N. This is a convention, and other conventions move the factors, but the two operations must agree about their normalization.

Let us reconstruct our four samples. The inverse formula adds each Fourier coefficient times its positive-frequency pattern and divides by four. Only the coefficients at indices one and three are nonzero, and each equals two. At sample zero, the two patterns both equal one, giving four divided by four, or one. At sample one their values are i and negative i; their contributions cancel, giving zero. At sample two, both are negative one, so the result is negative one. At sample three they cancel again. We recover one, zero, negative one, zero exactly.

An experiment in reconstruction is often more educational than memorizing a transform table. It demonstrates that the DFT is a reversible linear coordinate change. If a software package transforms an array and then inversely transforms it, the result should agree with the original samples up to floating-point rounding, provided the transform sizes and normalization conventions match.

## What frequency does an index mean?

The index k is not by itself a frequency in hertz. To get physical frequency, we need the time spacing. Suppose we have N samples taken at a rate of f sub s samples per second. The sample window length is N divided by f sub s seconds. Its natural frequency-bin spacing is the reciprocal of that duration. Index one means one cycle across the observation window, index two means two cycles, and so on.

For eight samples taken at eight per second, the ordinary frequency labels in array order are zero, one, two, three, four, negative three, negative two, negative one cycles per second. The Nyquist position, index four, is its own negative-frequency partner on the sample grid. If the data are real, that coefficient must be real. The same is true of the zero-frequency coefficient.

At indices larger than half the array, we conventionally subtract N from the index before converting to physical frequency. Thus, index seven means negative one in an eight-point transform. Some plotting libraries reorder the result so negative frequencies appear to the left of zero. That is a display choice, not a change in the transform.

Consider eight samples of a two-cycle-per-second cosine recorded at eight per second. The array is one, zero, negative one, zero, one, zero, negative one, zero. The transform is zero at every index except two and six, where it equals four. Since N is eight, dividing by N tells us that each complex exponential contributes one half. Adding the pair gives a cosine of amplitude one. If you inspect only the magnitude of the raw coefficient, four, and call it the original amplitude, you are off by a factor of four. Scaling is part of the interpretation.

For a general real cosine that lands exactly on a nonzero, non-Nyquist DFT bin, its two conjugate coefficients each have magnitude N times the cosine amplitude divided by two. The coefficient at zero frequency instead represents the mean multiplied by N. An even-length array's Nyquist coefficient has no separate partner, so it must be treated on its own. A useful amplitude formula therefore needs to say whether it handles a paired positive-frequency bin, zero frequency, or Nyquist frequency.

## What complex coefficients remember

A transform coefficient generally has a magnitude and an angle, called phase. Magnitude measures the amount of that Fourier basis pattern; phase describes how it is aligned with the sample index. Suppose two measurements have the same oscillatory shape but one is shifted in time. Their transform magnitudes can be identical while their phases differ. For real data, the negative-frequency coefficient is the complex conjugate of its positive-frequency partner. This ensures that adding the pair yields real numbers.

Let's test that with four samples of a sine: zero, one, zero, negative one. The coefficient at the positive one-cycle index is negative two i; the conjugate coefficient at the negative one-cycle index is positive two i. The magnitudes are still two, just as they were for the cosine. But the phases differ by a quarter turn, which is exactly what distinguishes a sine from a cosine shifted in time. If we retain only the magnitudes, we cannot know where the oscillation began.

The same point holds for more complicated data. The DFT of a shifted pulse has a predictable change of phase. The pulse's location is encoded partly in that phase, even though its overall frequency magnitudes are unchanged by a circular shift. Phase is not ornamental information that can be discarded without consequence.

## A conservation law in frequency coordinates

There is a numerical check analogous to conservation of energy. Add the squares of the absolute values of the sample numbers. The DFT gives a related sum of squared coefficient magnitudes, scaled by one over N. The two sums agree exactly. This is the finite-dimensional version of Parseval's identity.

In our four-sample cosine example, the time-side squared sum is one squared plus zero plus negative one squared plus zero, which is two. On the frequency side the two nonzero coefficients have squared magnitude four each. Their sum is eight, and dividing by four gives two. The energy has not vanished or doubled; it has been expressed in different coordinates.

Why is this so useful? Suppose a numerical algorithm returns a Fourier spectrum with one surprising coefficient. Check the inverse reconstruction, conjugate symmetry for real data, the zero-frequency sum, and Parseval's identity. Each check tests a different structural fact. A plot may look plausible while a sign convention or normalization error goes unnoticed. These algebraic identities expose many such mistakes.

## An exact transform of samples is not an exact model of a signal

The DFT regards our N numbers as one period of a sequence that repeats forever. That periodic interpretation explains why its basis frequencies fit exactly around a finite grid. But the physical measurement need not really repeat. If it ends midway through a sinusoidal cycle, the periodic repetition of the recorded segment introduces a discontinuity at the join. A single physical tone may then occupy several DFT bins. This is called spectral leakage, and it is distinct from aliasing.

Nor does the DFT automatically compute the continuous Fourier transform of the original physical waveform. We have sampled in time, and we have restricted attention to a finite interval. Under smoothness and sampling assumptions, a suitably scaled DFT can approximate a Fourier integral over that finite interval at particular frequencies. But the exact discrete identity is simpler: it analyzes and reconstructs the finite sample vector.

That identity is already powerful. Every array has a unique expansion in these N frequency patterns. Their orthogonality gives the coefficients; the inverse formula gives the samples back; conjugate symmetry tells us how real data are stored; and Parseval lets us check the resulting arithmetic. The DFT is the frequency coordinate system of a finite-dimensional problem. Next we can use it without misreading a frequency peak as more information than the recorded data contain.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact DFT, inverse, orthogonality, and units

For \(x=(x_0,\dots,x_{N-1})\) define
\[
 X_k=\sum_{n=0}^{N-1}x_n e^{-2\pi i kn/N},\qquad
 x_n=\frac1N\sum_{k=0}^{N-1}X_k e^{2\pi i kn/N}.
\]
Orthogonality follows from a finite geometric series:
\[
\sum_{n=0}^{N-1}e^{2\pi i(k-\ell)n/N}=
\begin{cases}N,&k\equiv\ell\pmod N,\\0,&\text{otherwise}.\end{cases}
\]
Apply this identity to the inverse formula to prove exact reconstruction. The DFT matrix \(F\) satisfies \(F^*F=NI\), yielding Parseval:
\[
\sum_n |x_n|^2=\frac1N\sum_k |X_k|^2.
\]

For \(N=4\), \(x=(1,0,-1,0)\) gives \(X=(0,2,0,2)\); the sine sequence \(x=(0,1,0,-1)\) gives \(X=(0,-2i,0,2i)\). For \(N=8\), \(x_n=\cos(2\pi\cdot2n/8)\) gives \(X_2=X_6=4\), all other bins zero.

With physical sampling interval \(\Delta t\), \(T=N\Delta t\), \(f_s=1/\Delta t\), the bin spacing is \(\Delta f=1/T\). For \(0\le k<N\) the frequency label is \(k/T\) when \(k\le N/2\) and \((k-N)/T\) when \(k>N/2\), with the even-\(N\) Nyquist bin having two equivalent signs. For a smooth time-limited signal, \(\Delta t\,X_k\) is a Riemann-sum approximation to \(\int_0^T x(t)e^{-2\pi i kt/T}\,dt\); it is not automatically the whole-line Fourier transform of an unknown unsampled signal.

For a real sequence, \(X_{N-k}=\overline{X_k}\). The mean is \(X_0/N\). For a single real sinusoidal component at an exact integer bin \(k\) with \(0<k<N/2\), the two-sided coefficient has magnitude \(NA/2\) for amplitude \(A\); the one-sided amplitude is \(2|X_k|/N\). At DC and Nyquist (even \(N\)), do not double.

### Exercises with worked answers

1. Calculate the four-point DFT of \((1,1,1,1)\). **Answer:** \((4,0,0,0)\).
2. Calculate the DFT of \((1,2,3,4)\). **Answer:** \((10,-2+2i,-2,-2-2i)\). Inverting yields the original sequence.
3. For eight samples recorded at 16 Hz, give the frequency represented by index seven. **Answer:** \((7-8)/(8/16)=-2\) Hz.
4. Check Parseval for \(x=(1,0,-1,0)\). **Answer:** sample energy \(2\); transform energy \((0+4+0+4)/4=2\).
5. What is the mean of \(x=(2,2,4,0)\)? What is \(X_0\)? **Answer:** mean \(2\); \(X_0=8\).
6. For eight real samples, how many independent complex-positive-frequency bins lie strictly between DC and Nyquist? **Answer:** three: indices one, two, and three. Each has a conjugate at indices seven, six, and five.

### Sources and further reading

- [FFTW User Manual, *The 1d Discrete Fourier Transform*](https://fftw.org/fftw3_doc/The-1d-Discrete-Fourier-Transform-_0028DFT_0029.html).
- [NumPy FFT documentation: conventions and discrete Fourier transform](https://numpy.org/doc/stable/reference/routines.fft.html).
- [MIT OpenCourseWare, *Digital Signal Processing*, lecture on the discrete Fourier transform](https://www.ocw.mit.edu/courses/res-6-008-digital-signal-processing-spring-2011/resources/lecture-9-the-discrete-fourier-transform/).
