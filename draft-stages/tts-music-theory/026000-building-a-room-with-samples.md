# 026000 — Building a Room with Samples: Delay, Reflections, Convolution, and Reverb

**Track:** Music Theory and Composition. **Audience:** composers and engineers with some experience of tracks and effects. **Prerequisites:** discrete samples, addition, and time delay. **Purpose:** explain how the feeling of space is produced, where the computation comes from, and why the same reverb can help or harm a mix.

<!-- BEGIN SPOKEN LECTURE -->

# Building a Room with Samples: Delay, Reflections, Convolution, and Reverb

A singer performs one note in a small dry room and the recording ends almost when the voice stops. The same performance, heard from the back of a stone hall, seems to continue after the singer has finished. We describe that continuation with the word reverberation. But a useful production question is more precise: what exactly is continuing, and could a computer reproduce it with ordinary arithmetic on samples?

Imagine first an impossible room containing only a source and an ear, with no boundaries to reflect sound. The direct sound travels to the listener and arrives once. Now add a flat wall. Some energy travels by a longer path, reflects, and arrives later. Add a floor, ceiling, rear wall, seats, curtains and thousands of small surfaces, and many reflection paths contribute. Their strengths depend on angle, frequency, material, source and receiver location. The room does not insert a single uniform delay after every note. It transforms the entire changing pressure waveform through a complicated set of paths.

An early reflection is not merely a quieter duplicate in every real case. Its path may selectively attenuate frequencies, and different reflections may combine constructively or destructively. But delayed copies are an excellent first mathematical model. Suppose the direct sound reaches a microphone immediately in our chosen timeline. One reflection arrives ten milliseconds later at half the direct amplitude. Another arrives twenty-three milliseconds later at one quarter the amplitude. Then the recorded sound, in a simplified linear model, is the original waveform plus a delayed half-amplitude copy plus a delayed quarter-amplitude copy. This is enough to suggest an acoustic space even before we attempt to simulate a complete room.

At forty-eight kilohertz, ten milliseconds corresponds to 480 samples. Twenty-three milliseconds corresponds to 1,104 samples. If we call the original digital signal x and the result y, the program can compute each output sample by taking x at the current index, adding half of x from 480 samples earlier, and adding a quarter of x from 1,104 samples earlier. Out-of-range source samples are treated as zero. These numbers are invented to illustrate the operation; they do not claim to reproduce a named hall.

The list of delayed impulses and their amplitudes is called an impulse response. Imagine supplying a very short idealized click as the input. The output of a linear time-invariant room model would be precisely that room's impulse response, including initial arrival, early reflections, and tail. A different input can then be transformed by the same response using convolution. The operation applies each delayed, weighted copy and adds all contributions. It is more general than our three-tap example: a response may contain tens or hundreds of thousands of samples per channel.

This theoretical relation has an important condition. Convolution with a fixed impulse response describes a system that is approximately linear and does not change with time. Moving singers, moving microphones, changing doors, nonlinear loudspeakers, and dynamically modulated reverbs do not all fit that simple model. A sampled impulse response is a record or model of one configuration. It is not a universal portable representation of every room under every circumstance.

How could the computer obtain an impulse response? One could create it by calculation, using a geometric acoustics model, or measure a real environment using a suitable test signal and recover the response through deconvolution. The details of measurement matter: the loudspeaker, microphone, placement, background noise, and time-varying conditions are part of what the measurement captures. Jont Allen and David Berkley's 1979 paper on the image method described a digital approach for rectangular rooms. They represented reflections using virtual sources, then computed an impulse response between two spatial points. That is a historically important constructive example; it does not imply that every concert hall is rectangular, that every surface is perfectly reflective, or that a basic image method includes every wave phenomenon.

There is a computational surprise hidden in that simple convolution sum. Suppose a stereo stem is sampled at forty-eight thousand frames each second, and a one-channel impulse response lasts two seconds. It has ninety-six thousand taps. The most literal direct convolution would perform roughly ninety-six thousand multiply-add contributions for each output sample—about 4.6 billion contributions for one output channel per second of audio. A modern machine can do an enormous number of arithmetic operations, but this naive approach is not a sensible assumption for every channel in a complex mix. Efficient implementations commonly exploit block convolution and Fourier transforms; partitioning a long response into chunks can make the workload manageable, at the cost of buffering, memory and scheduling complexity. The exact algorithm and costs depend on the implementation.

A subtle distinction matters here. Convolution is a mathematical description, but the details of a specific audio plug-in are software engineering choices. Some impulse-response reverbs use nonuniform partition lengths to balance latency and CPU use. Others are intended for offline rendering. The web audio standard defines a convolution effect through an impulse response and even specifies permitted mono and stereo channel layouts and optional normalization. Those rules establish one interoperable API, not the behavior of every Ardour plug-in or DawDreamer processor.

A second family of reverbs need not replay a fixed impulse response at all. They can use networks of delays, filters, feedback, and sometimes modulation to generate a dense tail. A delay line stores earlier samples; a feedback loop feeds part of an output back into the input of a delay. If the feedback amount is below one in a simple stable loop, each return tends to diminish. Add filters, multiple delay lengths, and cross-channel paths, and the repeated echoes can become a rich tail. This is an algorithmic reverberator. It can be designed to evolve in ways a fixed static impulse response cannot, although it might mimic a real acoustic space less literally. Not every reverberator fits neatly into these two labels, and hybrid designs exist.

Why does reverberation make independently generated parts seem to belong together? If four dry instruments were rendered in isolation with different synthesizer presets, each may have its own imagined distance and ambience. Sending a controlled amount of each to a shared room effect can create a consistent spatial cue. The mix then contains a common set of reflections, rather than four unrelated artificial rooms superimposed. This is a production strategy, not a law that all good music should sound like a real room. A deliberately intimate dry vocal against a vast synthetic pad can be a strong arrangement precisely because their spaces differ.

Consider two routing diagrams. In the first, the guitar, bass, and melody each contain a separate reverb inserted directly on the track. Each processor runs a separate algorithm and may use a different room. In the second, each dry signal sends a controlled amount to one common reverb bus, and the wet return is mixed alongside the dry direct sounds. The second diagram allows a common room and can reduce redundant processing if the design permits one instance. But that claim has a practical limit. A shared effect is a common processing node. In a real-time processing graph, it cannot finalize its current block until its input contributions are available. What is efficient in total CPU work may create a critical scheduling path through the shared bus. And changing its settings changes the apparent space of several instruments at once.

There is also a dangerous accounting error when exporting stems. Imagine that the dry lead and dry guitar both feed a shared hall. If you export the guitar alone with the entire shared return, then export the lead alone with the same shared return, and later sum those two files, you have counted part of the hall twice. A reverb on a common bus responds to the combined input. The correct way to preserve that particular mix is to export the original dry stems plus one separate effect return, or to define a consistent attribution scheme for printed effects, with careful attention to nonlinear processors that make decomposition harder. The choice must be documented because the file names alone do not say how many times the room has been rendered.

Decay time adds a musical dimension. A long tail from one phrase can remain audible under the next phrase. That may connect sections beautifully, or it may blur a rapid passage. Low-frequency reverberation can accumulate and obscure bass articulation; high-frequency decay can make a sparse sound sparkle or produce fatigue. It is reasonable to adjust the reverb differently at a major section change or automate send levels. A reverberation time described as the interval for a sixty-decibel reduction is one acoustic descriptor of decay, but real spaces have frequency-dependent behavior and may not follow a single tidy exponential. The numerical value does not tell us how compelling the sound will be in the arrangement.

Timing and space also interact with what musicians call pre-delay: an intentional pause between direct sound and the main reverb response. It can make the direct attack more intelligible while keeping a long tail. An echo timed to the tempo is a related but different effect: its repetitions may become a rhythmic participant, something listeners can count as part of the composition. At 120 beats per minute, a quarter note is half a second, or twenty-four thousand samples at forty-eight kilohertz. A dotted-eighth echo, three quarters of that duration, is 375 milliseconds, or eighteen thousand samples. Here the delay is not imitating a particular wall. It is making a rhythmic pattern.

The result suggests a simple creative experiment that requires no audio file to reason about. Write the onset times of a melody. Duplicate them at a quarter-note delay. Ask which echoes now overlap with new melody notes. If the echoes become a second rhythmic voice, the problem is musical, not merely acoustic. Then imagine a dense reverb whose thousands of little returns occupy the intervals between notes. A sound-design parameter has changed the counterpoint.

For an agentic production system, a useful handoff distinguishes the direct signal, the intended virtual room, and what will be printed into the output file. A stem marked dry should not quietly contain a hall reverb. If a particular room impulse is important, give it a stable identifier, source or license, channel arrangement, sample rate, and transformation history. If a processor's result depends on random modulation or time-varying state, record that too where reproducibility matters. A mix cannot be reconstructed merely by remembering a preset name, because external plug-in versions and routing details may change.

Convolution gives the mathematics of one kind of space, but it does not choose an aesthetically appropriate space. The composer's work is to decide how much of the source should remain close and immediate, where reflections help bind the ensemble, and when distance should become a musical event. Once those decisions are explicit, an offline engine can render them, a live DAW can audition them, and the same written score can survive both production paths.

<!-- END SPOKEN LECTURE -->

## Display-only companion: exact toy impulse response

An *original hypothetical* three-tap response at 48,000 Hz:

```text
h[0] = 1.0
h[480] = 0.50       # 10 ms reflection
h[1104] = 0.25      # 23 ms reflection
h[k] = 0 otherwise

y[n] = x[n] + 0.5*x[n-480] + 0.25*x[n-1104]
```

- This is a finite impulse response with no feedback and no physically calibrated room geometry.
- For `f_s=48000` and a 2-second response, `L=96000` taps; an illustrative direct convolution costs approximately `f_s * L = 4,608,000,000` multiply-add contributions/s per output channel. This is an **operation count for a naive implementation**, not a claimed DawDreamer or Ardour performance measurement.
- At 120 BPM, quarter-note delay = `0.5 s = 24,000` samples; dotted eighth = `0.375 s = 18,000` samples.

## Claim-to-source reading map

- **Impulse responses in a specific rectangular room model:** Jont B. Allen and David A. Berkley (1979), [“Image method for efficiently simulating small-room acoustics,” *Journal of the Acoustical Society of America* 65(4), 943–950](https://doi.org/10.1121/1.382599). Consult its model assumptions, not merely the abstract, before applying it to nonrectangular rooms; the lecture's three-tap impulse is **not** from this paper.
- **What a convolver computes and its channel configurations:** [W3C, *Web Audio API*, “ConvolverNode”](https://www.w3.org/TR/webaudio/#ConvolverNode). This is a normative description of the Web Audio API, **not** a specification of Ardour's reverbs.
- **Processing graph and mix-bus consequences:** [DawDreamer, *User Guide*](https://github.com/DBraun/DawDreamer/blob/main/docs/user_guide/index.rst), “Graph” and “Processor Types”; [Ardour, *Signal Flow*](https://manual.ardour.org/signal-routing/signal-flow/); [Ardour, *Stem Exports*](https://manual.ardour.org/working-with-sessions/interchange-with-other-daws/stem-exports/).
- **Delay filtering and comb responses:** Julius O. Smith III, [*Physical Audio Signal Processing*, “Comb Filters”](https://www.dsprelated.com/freebooks/pasp/Comb_Filters.html). For an independent account of exact finite-delay arithmetic.
- **Aesthetic choices about wet/dry levels and pre-delay:** identified as **production judgments and hypothetical examples**; no claim that the listed sources establish one optimal setting.

## Design exercises

1. Compare a shared effect-return export with four stems that contain independently printed reverb. Determine which signal components would be duplicated if every file were added later.
2. For an input stream of `N` samples and impulse of `L` samples, explain why the full linear convolution has `N + L - 1` samples in the absence of truncation. What happens to the last notes if export ends at input sample `N`?
3. Derive and draw impulse trains for quarter-note and dotted-eighth delays at 120 BPM. Predict the new note-onset times without pretending to know the sound's timbre.
