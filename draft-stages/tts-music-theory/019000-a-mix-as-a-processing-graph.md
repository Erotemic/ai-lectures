# 019000 — A Mix Is a Processing Graph: DawDreamer, Ardour, and the CPU Budget

**Track:** Music Theory and Composition. **Audience:** Listeners and makers who want to understand a DAW as software rather than a collection of mysterious knobs. **Prerequisites:** No coding required for the spoken lecture; the companion includes a reproducible Python demonstration. **Example:** Four original, hypothetical stems arranged into a dependency graph.

<!-- BEGIN SPOKEN LECTURE -->

# A Mix Is a Processing Graph: DawDreamer, Ardour, and the CPU Budget

You open a digital audio workstation and see tracks arranged in horizontal lanes. They look like independent files, and if you have a programmer's eye, you may imagine a simple loop: read the next block of samples from each lane, add everything into two numbers for the left and right speakers, repeat. Then a plugin makes the audio engine crackle, even though your desktop reports plenty of unused CPU. Has mixing suddenly become difficult arithmetic? Usually not. You have run into the difference between a list of tracks and a graph of computations.

A track is a place to keep material and control how it is processed. A processing graph is a map of what must be computed before what else. In the simplest possible graph, guitar, bass, drums, and melody are four inputs to a summing point. Each may pass through a gain control, and the sum feeds an output. In a more elaborate graph, the guitar passes through an amplifier model, the bass through a compressor, and the drums through a transient shaper. Several tracks send copies to one reverb bus. That bus and the dry tracks feed a master compressor, followed by the output. Every arrow is a dependency. The output cannot be finalized until the inputs it depends upon are available.

There are two helpful ways to explore this idea. One is an interactive workstation such as Ardour. Its mixer presents tracks, bus strips, processing chains, sends, and a master bus. You can put a processor before or after the fader, route several tracks to a subgroup, or send only a portion of their signal to a shared reverb. The other is a programmable offline engine such as DawDreamer. You describe processors and a graph in Python, render it, and inspect the resulting audio arrays. These tools do not have identical interfaces or responsibilities, but they expose the same underlying principle: audio flows through a specified network of operations.

To understand that network, imagine a twenty-second composition: a dry guitar recording, a bass line, a drum stem, and a synthetic melody. Suppose all four begin at the same absolute time, have the same sample rate, and contain the same number of samples, including their intended silences. We can send the four into a mixer using four gain factors. We could initially set every factor to one quarter. That is not an endorsement of those levels; it is merely an experiment that gives us simple arithmetic. If the four samples happen to be zero point eight each at the same instant, their weighted sum is zero point eight. If we had used unity gain, the sum would be three point two, well above a conventional fixed-point output ceiling.

Now put a filter on the guitar before mixing. Mathematically, that filter changes only the guitar contribution. Put the same type of filter after the sum, and it changes the bass, drums, and melody as well. With one linear, time-invariant filter and precisely the same settings, filtering before and after summing can be algebraically equivalent if every branch passes through that filter and if startup state and routing agree. But the moment only one source gets the filter, or the processor is nonlinear, the equivalence disappears. Order and location matter. A compressor triggered by the combined mix responds to interactions that an individually applied compressor never sees.

Consider a compressor whose detection circuit becomes active when the input level rises above a threshold. A kick drum by itself may remain below that threshold. A bass note by itself may also remain below it. Combined, they may cross it and cause the compressor to reduce both. This can make the bass seem to dip on each kick. It could be a useful musical pulse or an unwanted side effect. Moving the compressor from the master to the bass branch changes what it hears. Sending the kick to a sidechain detector while compressing only the bass produces yet another relationship. All three arrangements may use the same kind of plugin, but their dependency graphs express different decisions.

There is a second distinction: the graph of audio samples is not necessarily the graph of musical intention. In a live performance, the musician changes the notes, accents, phrasing, and timbre. In a recorded session, the audio file has already frozen many of those choices. A fader cannot unplay an overlapping guitar note. An equalizer can reduce part of its spectrum but cannot guarantee the restoration of a hidden melody. The processing graph can improve balance; the arrangement itself may need editing. This is why a tool for mixing is not a complete substitute for musical judgment, even if all processing is automated.

Let us calculate the CPU budget rather than treating it as folklore. At a sample rate of forty-eight thousand samples per second and a buffer of two hundred fifty-six frames, each buffer represents about five point three three milliseconds of sound. If the interface requires one buffer on that schedule, the engine must make progress within that interval. At one hundred twenty-eight frames, the interval is about two point six seven milliseconds. The smaller buffer reduces latency, but also halves the time allowed for each callback and generally increases scheduling overhead. That does not mean every instruction has half as many CPU cycles available in an absolute sense; the processing overhead and implementation matter. The point is that the real-time deadline has tightened.

Suppose the melody branch takes one millisecond to compute, the guitar branch two, the bass branch one, and the drums branch one. If those branches can execute concurrently on separate cores, their joint wall-clock time could approach two milliseconds, plus dispatch and synchronization overhead. Now suppose their shared bus takes another one and a half milliseconds, and the master processing chain takes another two milliseconds. Even perfect parallelism cannot make the result arrive faster than roughly five and a half milliseconds in this hypothetical schedule: the bus and master come after the slowest branch. For a five point three three millisecond buffer, that estimate already misses the deadline. It would be misleading to report only the sum of branch CPU times or the percentage of idle cores. What matters to the playback callback is the longest dependent route to the output, with overhead included.

In a real DAW, graphs are more complicated than our arithmetic exercise. Plugins may require internal buffering and report processing latency. A look-ahead limiter intentionally delays audio so it can examine incoming material before controlling its output. A linear-phase equalizer may add delay. The workstation can compensate other paths so that sounds meant to coincide remain aligned. Ardour calls this latency compensation. Compensation solves an alignment problem, not the CPU cost of the plugin, and it does not eliminate all forms of hardware monitoring latency. Delay compensation can even add waiting time so multiple branches arrive together at a summing node.

Offline rendering changes the time constraint. In DawDreamer, a RenderEngine receives a processing graph and computes a duration of audio. You might render ten seconds of a computationally expensive synth through reverb in twenty seconds of wall-clock time. The render is slow, but the resulting file can still be correct and glitch-free if all required state, buffers, and tails are handled. In Ardour, you might instead freeze, bounce, or export a processed track, then import the result. That replaces an expensive calculation during playback with a file-read operation. The musical decision is preserved in the rendered waveform, but you lose some immediate freedom to change the upstream processor settings without rerendering.

This leads to a useful question: why don't we always put everything on separate cores and sum at the end? Sometimes we can. But shared processing requires a point of synchronization. Some instruments have shared internal state, such as a global reverb fed by many voices. Plugin instances can be non-thread-safe, and running several may multiply memory use. Some paths use feedback or mutually dependent signals, requiring deliberate delay and cycle-breaking rules. The operating system may also move work across cores, page in memory, or handle other interrupts. A theoretically parallel graph is not a guarantee of real-time performance.

For someone writing a generator for many pieces, the natural pattern is often different from interactive mixing. Use DawDreamer to render independent synthetic instruments or alternative arrangements offline, with one isolated engine per worker when parallelizing. Save the rendered assets and enough metadata to reproduce their timing and plugin settings. Then bring the stems into Ardour to judge balance and relationships. If the mixer finds that the bass enters on the wrong subdivision, the arrangement generator can revise the event schedule. If it finds a level problem, the mixer can alter the gain. This division of labor avoids asking an equalizer to solve a compositional error.

A practical experiment can make the graph visible even without hearing anything. Construct a four-node input layer and a one-node summing layer. Add a filter between the guitar node and the summing node. Write down the output for one instant before and after changing the guitar gain. Then move the filter after the sum, and ask which sources are affected. Finally replace the filter with a thresholded processor. At that point, changing one source may alter the gain applied to every other source. That is a causal effect of the graph, not a mysterious property of audio software.

A final caution concerns benchmarks. If a render appears slow, isolate where the time goes. Check whether the instrument itself takes most of the time before blaming the summing operation. Compare rendering with processors bypassed, with fewer polyphonic voices, with a larger offline block where supported, or without oversampling. Measure real wall-clock time and the CPU load of individual paths when possible. Do not assume that a bigger buffer must make an arbitrary plugin faster, and do not assume a graph that renders offline will satisfy real-time constraints unchanged. Different workloads reveal different bottlenecks.

So a workstation is doing several things at once: preserving musical time, executing a signal graph, maintaining timing across branches, providing a controlled place to make artistic decisions, and scheduling computation under a deadline when the result is played live. Simply adding tracks is cheap. Deciding what to add, where to add it, and how to calculate it in time is where production becomes an engineering discipline. DawDreamer lets you make that computation explicit in code. Ardour lets you interrogate it with your ears, your eyes, and a timeline. Understanding both makes their limits easier to reason about.

<!-- END SPOKEN LECTURE -->

## Display-only companion: graph arithmetic and dependency timing

For gain factors `g_i` and samples `x_i[n]`, simple summation is:

\[
y[n] = \sum_{i=1}^{k} g_i x_i[n].
\]

A mixing graph might be represented as:

```text
melody ------------------------------\
guitar -> amp model -> EQ -----------+--> sum --> master compressor --> output
bass -> compressor ------------------+
drums --------------------------------/
                 ^                     \
                 |                      +--> optional reverb routing (depending on sends)
                 +-- optional sidechain detector from kick
```

The graph is conceptual: actual sends, buses and reverb returns must be connected without an accidental feedback loop.

The illustrative schedule in the narration:

| Branch or serial stage | Duration | Earliest completion with ideal branch parallelism |
|---|---:|---:|
| Guitar | 2.0 ms | 2.0 ms |
| Melody, bass, drums | 1.0 ms each | 1.0 ms each |
| Summing bus / shared effect | 1.5 ms | 3.5 ms |
| Master processing | 2.0 ms | 5.5 ms |

At 48 kHz, 256 frames correspond to `256 / 48000 s = 5.333... ms`. The estimated **5.5 ms** critical path fails this simplified budget, ignoring overhead. At 128 frames the budget is `2.666... ms`. These are *invented exercise timings*, not benchmark results for either application.

### DawDreamer graph sketch, based on its published API

The example uses four artificial oscillators so it needs no audio assets. It renders one second; it is **not** a benchmark, and the plugin/engine has not been executed in this archive-building environment. The documented methods are `RenderEngine`, `make_oscillator_processor`, `make_add_processor`, `load_graph`, `render`, and `get_audio`.

```python
import dawdreamer as daw

engine = daw.RenderEngine(48000, 512)
frequencies = [110.0, 165.0, 220.0, 330.0]
parts = [engine.make_oscillator_processor(f"part_{i}", hz)
         for i, hz in enumerate(frequencies)]
mix = engine.make_add_processor("sum", [0.1] * len(parts))
engine.load_graph(
    [(part, []) for part in parts]
    + [(mix, [part.get_name() for part in parts])]
)
engine.render(1.0)
audio = engine.get_audio()   # documented shape: (channels, samples)
print(audio.shape)
```

For an actual audio file rather than test oscillators, the official reference uses `make_playback_processor(...)`; load source channels at a common sample rate, align their first samples explicitly, and route them into the AddProcessor.

### Ardour experiment

1. Import four synchronized stems starting at the same session time.
2. Route the stems to a bus; compare direct track-to-master routing with subgroup routing, avoiding double routing.
3. Place an effect on one track, then move it onto the bus; note which signals the effect receives.
4. Observe processor position relative to fader/panner and use the latency display when relevant.
5. Export dry stems and processed stems separately, retaining their full timeline length; compare whether the original and printed versions null when aligned and routed identically.

**References:** [DawDreamer built-in processors](https://github.com/DBraun/DawDreamer/blob/main/docs/user_guide/other_processors.rst), [DawDreamer multithreading](https://github.com/DBraun/DawDreamer/blob/main/docs/user_guide/threading.rst), [Ardour signal flow](https://manual.ardour.org/signal-routing/signal-flow/), [Ardour latency compensation](https://manual.ardour.org/synchronization/latency-and-latency-compensation/).
