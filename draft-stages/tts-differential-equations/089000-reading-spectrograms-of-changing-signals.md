# Reading Spectrograms of Changing Signals: Chirps, Impacts, and Phase

<!-- BEGIN SPOKEN LECTURE -->

# Reading Spectrograms of Changing Signals

Think of a spectrogram as a map with time across the page and frequency up the page. A ridge might tell us that a tone persists. A sloping ridge might tell us its pitch is changing. A brief vertical streak might mark a click. This description is easy to say and useful as a first approximation, but it can become misleading if we forget how the map was constructed. Every feature passes through a window, a Fourier transform, a magnitude or power convention, and a display scale. The plot is an analysis of the signal, not a direct photograph of sound.

We will learn to read this map using four signals that are simple enough to describe mathematically: a steady tone, a chirp whose frequency increases, an abrupt impulse, and two groups of notes played in opposite orders. The last example will show exactly what the magnitude of a Fourier transform loses. The goal is not to memorize the appearance of a handful of pictures. It is to infer what the calculation can and cannot support.

## A horizontal ridge is a sustained oscillation

Start with a cosine at fifty hertz. Over a second, it completes fifty cycles. Analyze this recording using a window two hundred milliseconds long. In the ideal case of a steady cosine, every window entirely inside the recording contains essentially the same pattern of oscillation, differing only in phase according to the window's position. The Fourier magnitude of each window is therefore nearly the same. If we make time the horizontal axis and frequency the vertical axis, a horizontal bright region appears near fifty hertz.

Why a region, rather than a perfectly thin line? Because a finite window has its own Fourier response. Multiplying the signal by the window convolves its ideal frequency lines with that response. A taper gives us a central spectral lobe and usually smaller sidelobes. A rectangular cutoff gives us a different lobe and sidelobe structure. The exact height and width depend on the window and the normalization. Neither is a new oscillation that was present in the physical signal.

If the tone fades steadily in amplitude, the horizontal feature dims as time proceeds. But watch the scaling. A power spectrogram uses squared magnitude. Halving the signal amplitude divides the plotted power by four, a reduction of about six decibels. A log magnitude plot uses twenty times the base-ten logarithm of an amplitude ratio; a log power plot uses ten times the logarithm of a power ratio. Both report about six decibels for that amplitude change when their reference and normalization are consistent. They are not the same raw numerical quantity.

This matters when comparing figures. The same recording can look richly textured on a logarithmic display and almost blank on a linear display dominated by one strong peak. A changed color limit can make a barely detectable component look bright or make a real low-level component vanish. Always check the colorbar, its units, and its reference.

## A chirp: a tone with a moving frequency

Now construct a signal whose instantaneous frequency starts at fifty hertz and climbs by twenty hertz each second. After two seconds, the frequency is ninety hertz. This is a linear chirp: the frequency is fifty plus twenty times time, in hertz. The corresponding phase is two pi times the sum of fifty times time and ten times time squared. Why the time-squared term? Because frequency is the rate at which phase accumulates cycles. Integrating a steadily increasing frequency produces a quadratic phase.

Take a window centered at the one-second mark. Its central instantaneous frequency is seventy hertz. If the window is two hundred milliseconds long, the frequency changes by about four hertz from its beginning to its end. Even before accounting for the window's own spectral width, the segment does not contain one perfectly constant-frequency cosine. The local Fourier transform collects a range of nearby oscillatory behavior. The spectrogram shows a diagonal ridge that thickens or bends according to both the signal and the window.

At a sampling rate of five hundred samples per second, a two-hundred-millisecond window contains one hundred samples. Its natural unpadded DFT grid is spaced five hertz apart. Thus a four-hertz frequency change within one window is already comparable to that grid spacing. If we halve the window length, the chirp changes by only two hertz within the window, but the grid spacing grows to ten hertz. If we double its length, the grid spacing improves to two point five hertz but the chirp sweeps through eight hertz inside that window. A beautifully smooth display cannot remove this underlying compromise.

For rapidly changing pitch, the ridge may curve or blur enough that reading a single bin as the exact instantaneous frequency is not justified. More sophisticated methods estimate phase derivatives or fit chirp models, but the ordinary spectrogram remains a good first diagnostic if we state what it measures. A displayed ridge is an estimate of concentrated local frequency content, not an exact time-indexed list of the signal's mathematical instantaneous frequency.

## An impulse: localized in time, broad in frequency

Imagine tapping a metal object with a sharp striker, or a digital sequence that is zero everywhere except for one sample. The ideal single-sample impulse has equal-magnitude DFT coefficients at every frequency bin. That is easy to verify: the Fourier transform of a sequence with one nonzero entry contains one complex exponential in each bin, and the magnitude of a unit complex exponential is one.

In a sliding-window spectrogram, only windows that include the impulse see that energy. A rectangular window at the impulse's sample gives a frequency spectrum with flat magnitude across bins. A tapered window gives an overall amplitude determined by its weight at that sample, but the magnitude remains flat across the local frequency bins in that frame. As the window slides over the impulse, the brightness changes according to the weight assigned to the impulse sample. A spectrogram therefore displays the brief event over the entire set of overlapping windows that touch it.

The streak is broad in frequency and localized in time, as the uncertainty principle predicts. Yet its apparent duration can be longer than the physical impulse: a two-hundred-millisecond window touching the impulse at many offsets may make the event appear spread across a substantial fraction of two hundred milliseconds. A hop of ten milliseconds places many columns under the event, but it does not shrink the physical span each column analyzes.

A real impact is not an ideal one-sample impulse. Its contact force lasts some time, and the object may ring afterward at resonant frequencies. A spectrogram might show a vertical-ish burst followed by decaying horizontal ridges. That structure is meaningful, but it is not an exact spectroscopic fingerprint without accounting for microphone response, sampling, room acoustics, noise, and window length.

## Two recordings with identical global Fourier magnitudes

Return to the eight samples from the first time-frequency lecture. The first four form the two-hertz sampled sine zero, one, zero, negative one. The last four alternate one, negative one, one, negative one, representing the four-hertz Nyquist-frequency pattern. In recording A the two-hertz segment comes first. In recording B the four-hertz segment comes first.

Recording B is recording A circularly shifted by four samples. The eight-point Fourier transform of a circular shift is the original Fourier transform multiplied, bin by bin, by a phase factor. With a shift by half the record length, that factor is simply plus or minus one depending on the bin. Its magnitude is always one. The two complete-record Fourier magnitudes are exactly identical.

Yet a four-sample-window spectrogram of recording A begins with a two-hertz component and ends with four hertz. The same analysis of recording B has the order reversed. This is a rigorous example of what global Fourier magnitude cannot preserve. The global complex transform has enough information to reconstruct either recording, but dropping its phase removes timing structure. The local transform retains some of that structure by reporting when each frequency appears.

There is also a caution. The local magnitude spectrogram is not always enough to reconstruct an arbitrary signal uniquely either. The windowing may give many overlapping constraints, but phase retrieval is a separate inverse problem. We can use a spectrogram to detect a reversed order without claiming that every detail of the waveform is recoverable from brightness values alone.

## What overlapping windows do to interpretation

Suppose two short tones occur one hundred milliseconds apart. A window two hundred fifty milliseconds long can contain portions of both simultaneously. The corresponding spectrogram columns may show both frequencies at once, creating the impression of an overlap that was not present as simultaneous tones in the original timeline. Shortening the window can separate the onsets, but the local frequencies may become harder to distinguish. This is not a software bug. It is what each window was asked to include.

Overlap between consecutive analysis windows adds another subtlety. Closely spaced columns are not independent measurements. If the hop is one quarter of the window length, neighboring frames share three quarters of their samples. A sudden change therefore affects several neighboring columns in a strongly correlated pattern. A bright shape spanning four columns does not mean four independent events.

Padding at a recording's edges can create yet another artifact. If the algorithm pretends that the signal is zero outside the observed interval, the first and last windows may see an artificial onset or cutoff. Reflection padding avoids some abruptness but assumes a mirrored continuation. These are choices in the analysis, not discovered facts about what happened outside the recorded interval.

## Reading phase without becoming lost in it

The Fourier coefficient is complex because a sine wave has both strength and phase. If a tone is shifted in time, its phase changes. A spectrogram based only on squared magnitude hides that distinction. For some goals, such as finding energy at particular frequencies, this is fine. For timing precision, waveform reconstruction, interference, and coherent addition of signals, phase matters.

One subtle point is that the phase of a local Fourier coefficient also depends on where we put the origin of the window's time coordinate. Shifting a window through a steady tone changes the reported complex phase even though the amplitude pattern stays the same. That makes a raw phase heatmap hard to interpret without conventions. Frequency and phase differences can be informative, but they must be defined relative to a consistent coordinate system.

In audio, the audible consequences of removing phase depend on the signal and the nature of the manipulation. It would be wrong to say that phase is always irrelevant just because a magnitude spectrogram is often useful. Similarly, a bright horizontal ridge does not prove the sound came from a single source. Several sources, an instrument harmonic, or electrical interference can produce energy at the same frequency.

## A reproducible reading procedure

Here is a practical order for analyzing a changing signal. First identify the sampling rate and check whether aliasing could already have occurred during acquisition. No subsequent window fixes missing high-frequency information. Second, choose a window long enough for the frequency distinctions you care about and short enough for the timing distinctions you care about. Third, record the window type, length, hop, FFT length, padding, and one-sided or two-sided convention. Fourth, label the plotted quantity accurately: magnitude, squared magnitude, or power spectral density. Fifth, compare with a second window length if a key claim depends on whether two tones overlap or a transient lasts a particular time.

Finally, resist overinterpretation. In a chirp, the ridge traces changing frequency. In an impulse, broad frequency content marks a brief event. In a steady tone, a horizontal ridge marks sustained oscillation. But every picture is the product of both the signal and an analysis choice. If you can predict how the picture would change when the window length doubles, you are beginning to read spectrograms mathematically rather than only visually.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact moving-frequency and shift examples

A linear chirp with initial frequency \(f_0\) and sweep rate \(a\) has phase and signal
\[
\phi(t)=2\pi\left(f_0t+\tfrac12 a t^2\right),\qquad
x(t)=\cos\phi(t),\qquad
f_{\mathrm{inst}}(t)=\phi'(t)/(2\pi)=f_0+at.
\]
For \(f_0=50\) Hz, \(a=20\) Hz/s, the instantaneous frequency at \(t=1\) s is 70 Hz. A centered window of duration 0.2 s covers the interval 0.9–1.1 s, where frequencies range from 68 to 72 Hz. At \(f_s=500\) Hz this window has \(L=100\) samples and unpadded bin spacing 5 Hz.

For \(N=8\), let \(x=(0,1,0,-1,1,-1,1,-1)\) and let \(y[n]=x[(n+4)\bmod8]\). Then
\[
Y[k]=e^{2\pi i(4k)/8}X[k]=(-1)^kX[k],\qquad |Y[k]|=|X[k]|.
\]
The sign of the exponent depends on the chosen positive/negative shift convention, but for half-record shifts the equality and factor \((-1)^k\) are the same. Four-point local DFT magnitudes show the blocks in reversed order.

For amplitude ratio \(A_2/A_1=1/2\), the change in decibels is \(20\log_{10}(1/2)\approx-6.0206\) dB. Equivalently, for power ratio \(P_2/P_1=1/4\), \(10\log_{10}(1/4)\approx-6.0206\) dB. A spectrogram defined as \(|X|^2\) need not have the same physical calibration as a properly normalized power spectral density.

### Exercises with answers

1. A chirp begins at 30 Hz and increases at 15 Hz per second. What is its frequency at 2 seconds? **Answer:** 60 Hz.
2. A window of duration 0.4 seconds observes this chirp centered at 2 seconds. What instantaneous-frequency range lies across its support? **Answer:** 57–63 Hz, a sweep of 6 Hz.
3. How does a full-record Fourier magnitude change under a circular shift? **Answer:** it does not; only the complex phases change.
4. A sinusoid's amplitude is halved. By how many decibels does its consistent power or magnitude level change? **Answer:** approximately negative 6.02 dB.
5. A 0.2-second window is shifted every 0.01 seconds. Does its blur become 0.01 seconds? **Answer:** no. Adjacent frames overlap heavily but each still analyzes 0.2 seconds.
6. Why might an apparent two-tone overlap be caused by analysis rather than the source? **Answer:** a window can include portions of two distinct events that never occurred at the same instant.

### Sources and further reading

- [SciPy `ShortTimeFFT`: window positions, frequency bins, phase conventions](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ShortTimeFFT.html).
- [SciPy `ShortTimeFFT.spectrogram`: power from squared magnitude](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ShortTimeFFT.spectrogram.html).
- [NumPy DFT definitions and normalization](https://numpy.org/doc/stable/reference/routines.fft.html).
- [Wikipedia: Chirp](https://en.wikipedia.org/wiki/Chirp).
