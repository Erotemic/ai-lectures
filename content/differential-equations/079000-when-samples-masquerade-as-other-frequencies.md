# When Samples Masquerade as Other Frequencies: Sampling and Aliasing

<!-- BEGIN SPOKEN LECTURE -->

# When Samples Masquerade as Other Frequencies

A spinning wheel can look as though it is turning backward in a video. Nothing has reversed in the mechanism. The camera sees the wheel only at isolated instants, and a different motion can put the spokes in the same positions at those instants. The camera has not made a bad measurement of an individual frame. It has discarded the information between frames.

Something similar happens when we record a sound, measure a vibrating string, or store a temperature sensor's readings in an array. Fourier analysis has taught us to describe a continuous signal as a combination of frequencies. A computer receives a finite sequence of numbers instead. The central question is what those numbers can tell us about the continuous motion that produced them. This is the problem of sampling, and its most important obstacle is aliasing.

We will work with actual sample values rather than begin by quoting a theorem. The calculations will also distinguish three quantities that are easy to confuse: the rate at which samples are taken, the length of the recording, and the number of samples.

## A recording taken eight times per second

Imagine that a sensor measures a periodic signal every one eighth of a second. There are eight equally spaced samples each second. We call eight samples per second its sampling rate. The samples occur at times zero, one eighth, two eighths, three eighths of a second, and so on. The spacing in time and the sampling rate are reciprocals.

Start with a cosine completing one cycle per second. At each sample time, the angle increases by one eighth of a full turn, or forty-five degrees. We see the values one, then approximately zero point seven zero seven, then zero, then negative zero point seven zero seven, then negative one, and the values rise again. Eight sample points trace the shape of one cycle.

Now replace the signal by a cosine completing nine cycles per second. Between two samples it advances by nine eighths of a full turn. But nine eighths is one full turn plus one eighth. A cosine does not change when we add a full turn. So every one of the nine-cycle samples agrees exactly with the corresponding one-cycle sample. The two continuous signals are different; their sampled sequences are identical.

There is a second surprise. A cosine completing seven cycles per second is also indistinguishable from the one-cycle cosine on this sampling grid. Seven eighths of a turn is one turn minus one eighth. Cosine has the same value at positive and negative angles. So seven forward cycles per second give the same sampled cosine values as one forward cycle per second. If we instead sample a sine wave, that reflection changes the sign. It is important not to generalize the equality of those two cosines to arbitrary signals with arbitrary phases. The correct statement is about frequencies considered modulo the sampling rate, together with the conjugate symmetry specific to real-valued cosines.

These examples are aliases. Two frequencies, or two combinations of frequencies, can produce the same sequence. No method operating only on those samples can prove which of the original signals was present. A more elaborate Fourier transform cannot recover information that was never measured.

## Why there is a highest unambiguous frequency

For our eight-sample-per-second grid, consider frequencies from zero upward. Frequencies below four cycles per second have distinct positive and negative oscillations on the grid, subject to the usual representation of a real signal as conjugate pairs. Four cycles per second is special. Each sample occurs half a cycle after the previous one. A cosine aligned with the first sample alternates between one and negative one. This is called the Nyquist frequency: half the sampling rate.

At exactly that frequency, an arbitrary sine component cannot be distinguished from zero if its sample times coincide with the sine's zeros. Changing the phase changes what the samples reveal. Consequently, the clean sampling theorem places the signal's frequency content strictly inside the Nyquist band, rather than treating the limiting frequency as harmless.

Above four cycles per second, frequencies fold back into the range below four. A five-cycle cosine looks like a three-cycle cosine, seven looks like one, and nine also looks like one. This is why frequency aliasing is often described as folding. A signal can be physically oscillating quickly while a plot of its samples suggests a much slower motion.

There is a general reason. Sampling a complex oscillation at regularly spaced times means evaluating an exponential at integer multiples of the sampling interval. If we increase its frequency by any integer multiple of the sampling rate, the phase at the nth sample changes by an integer number of complete turns. Nothing changes in the resulting sequence. For real cosines, the positive and negative frequency representatives also coincide. The sample array therefore identifies not an unrestricted continuous frequency but an equivalence class of frequencies.

## What the sampling theorem really promises

The sampling theorem is not a blanket statement that eight measurements per second reconstruct any motion with eight interesting details. It makes a promise under specific assumptions. If a continuous signal is truly bandlimited, meaning its Fourier transform has no content at or above a known limiting frequency, and the sampling rate is more than twice that limiting frequency, then the ideal infinite sequence of exact, regularly spaced samples uniquely determines the signal. In mathematical terms, the signal can be recovered from shifted sinc functions, one centered at each sample time.

The reconstruction function called sinc is not a small, local bump. It oscillates with tails extending in both directions. The ideal formula needs infinitely many samples in principle; in a finite recording we approximate it. It also presupposes that measurements are timed correctly and that the signal belongs to the class for which the reconstruction theorem applies. Noise, finite recording length, imperfect filters, and irregular sample times require additional analysis. None of those issues invalidates the theorem; they tell us what its hypotheses were doing.

A signal that starts suddenly or has a perfect discontinuity is not exactly bandlimited. A sharp corner contains arbitrarily high frequencies in its ideal mathematical description. That does not mean such signals are impossible to sample usefully. It means a finite-rate acquisition system cannot guarantee exact recovery of every feature. In practice, we choose a frequency band worth retaining, and we suppress higher frequencies before taking samples.

This suppression is anti-alias filtering. For audio, it is commonly a low-pass filter ahead of conversion or a suitable digital filter ahead of reducing an existing high-rate recording to a lower rate. Once sampling has mistaken a seven-cycle signal for a one-cycle signal, no filter applied afterward can reliably separate that alias from a real one-cycle signal. The distinction has already been lost in the low-frequency data.

## More samples or faster samples?

Suppose we take sixteen samples at sixteen per second. The recording lasts one second, with sample positions running from zero through fifteen sixteenths of a second. The Nyquist frequency is eight cycles per second. The natural separation between the Fourier frequencies associated with a one-second observation window is one cycle per second.

Now keep the sampling rate at sixteen per second but record for four seconds. We collect sixty-four samples. The Nyquist frequency stays eight cycles per second, because the time spacing has not changed. But a four-second interval has a natural Fourier-bin spacing of one quarter cycle per second. A longer record can distinguish close frequencies more clearly, provided the signal is reasonably stationary during that interval.

Try the opposite change: keep the duration at one second and raise the sampling rate to sixty-four samples per second. We now collect sixty-four samples, but the natural Fourier-bin separation is still one cycle per second. We have extended the available frequency range and improved the time resolution. We have not gained the same close-frequency discrimination as the four-second record. Both recordings contain sixty-four samples; they answer different questions.

This is a helpful way to think about resolution. The sampling interval determines the highest continuous frequency we can represent without aliasing under bandlimit assumptions. The observation duration determines the natural spacing of frequency samples in a finite Fourier analysis. Neither number by itself guarantees that two nearby noisy or time-varying tones will be separable; the signal and the analysis window matter as well.

## Where Fourier series meet measurements

You may remember the distinction between a Fourier series and the Fourier transform. A series decomposes a periodic function into discrete harmonics. A transform represents nonperiodic signals through a continuous range of frequencies. Sampling introduces another operation: we choose particular time points and store only the values there. Those values can be analyzed with a discrete Fourier transform, which we will construct directly from a finite set of oscillations.

It is tempting to say that the discrete transform merely evaluates the continuous Fourier transform at a few convenient frequencies. That is not generally true without careful qualifications. A finite record has been cut out by a time window. Regular sampling identifies frequencies that differ by multiples of the sampling rate. A discrete transform then analyzes the resulting finite sequence as one period of a periodic array. Cutting, sampling, and analyzing are three different operations, and their effects must not be confused.

This separation will save us from two common mistakes. A false low-frequency peak due to aliasing is not fixed by recording longer at the same insufficient sample rate. A smeared peak caused by cutting a sinusoid mid-cycle is not necessarily evidence that the original signal contained many separate tones. We need to know which operation produced the feature before trying to remove it.

Return to the spinning wheel. Watching the wheel for a longer time with the same frame rate may give us more repeated evidence of a misleading slow rotation. Increasing the frame rate can distinguish motions that the earlier frames could not, especially if exposure and motion blur are also handled correctly. The mathematical point is that observations have a geometry: they occur on a grid in time. A frequency that completes an integer number of extra turns between consecutive grid points is invisible to the grid.

Sampling is therefore a model of what we know, not a mere format for storing what we know. Before extracting a spectrum from real data, state the sample rate, the duration, and what was done to prevent unwanted high frequencies from folding down. Once these are clear, the discrete Fourier transform becomes a precise tool rather than a mysterious plot of peaks.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: sampling, aliases and reconstruction

With sample spacing \(\Delta t>0\) and rate \(f_s=1/\Delta t\), set \(x_n=x(n\Delta t)\). For a complex tone,
\[
 e^{2\pi i(f+m f_s)n\Delta t}=e^{2\pi i f n\Delta t},\qquad m\in\mathbb Z.
\]
For real cosines \(\cos(2\pi(f_s-f)n/f_s)=\cos(2\pi f n/f_s)\), while \(\sin(2\pi(f_s-f)n/f_s)=-\sin(2\pi f n/f_s)\). Therefore, at \(f_s=8\) Hz, one, seven and nine hertz cosines have identical samples; seven-hertz sine has the opposite sign of one-hertz sine.

At Nyquist frequency \(f_N=f_s/2\), \(\cos(2\pi f_Nn/f_s)=(-1)^n\), whereas \(\sin(2\pi f_Nn/f_s)=0\). At Nyquist a general sine/cosine phase is not uniquely represented by the samples.

For a suitably regular continuous signal bandlimited to frequencies \(|f|<B\) with \(f_s>2B\), ideal sinc reconstruction is
\[
 x(t)=\sum_{n\in\mathbb Z}x(n\Delta t)\,\operatorname{sinc}\!\left(\frac{t-n\Delta t}{\Delta t}\right),
 \quad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
\]
State the signal class and interpretation of convergence when applying this formula. For a finite recording of \(N\) samples, \(T=N\Delta t\), Nyquist equals \(1/(2\Delta t)\), and the natural DFT frequency spacing is \(1/T\); improving one does not necessarily improve the other.

### Exercises with worked answers

1. A recorder samples at 20 Hz. Which cosine frequencies in \([0,20]\) alias to a 3 Hz cosine? **Answer:** 3, 17 (and 23 Hz would also alias if the upper limit were removed).
2. At a sample rate of 12 Hz, what are the four samples of \(\cos(2\pi\cdot3t)\) beginning at \(t=0\)? **Answer:** \((1,0,-1,0)\).
3. With 128 samples at 64 Hz, calculate Nyquist, duration and DFT-bin spacing. **Answer:** 32 Hz, 2 s, and 0.5 Hz.
4. A record is doubled in duration without changing the sampling rate. What changes? **Answer:** Nyquist is unchanged; the natural DFT-bin spacing halves.
5. Why can't a low-pass filter applied after an inadequate sampling step identify an aliased high frequency? **Answer:** the high and low continuous-frequency candidates now produce identical arrays, so the data contain no discriminator.
6. Why does the usual clean reconstruction theorem use a strict spectral bound? **Answer:** the Nyquist edge can identify positive and negative frequencies and lose phase information; strict separation avoids this degeneracy.

### Sources and further reading

- [MIT OpenCourseWare, *Signals and Systems*, lecture on sampling](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/).
- [MIT OpenCourseWare, *Digital Signal Processing*, lecture on the discrete Fourier transform and aliasing](https://www.ocw.mit.edu/courses/res-6-008-digital-signal-processing-spring-2011/resources/lecture-9-the-discrete-fourier-transform/).
- [Wikipedia: Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) (supplementary orientation, not a substitute for hypotheses).
