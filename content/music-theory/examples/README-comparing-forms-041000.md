# Lecture 041000 - comparing three complete compositional principles

The examples are three **original**, complete 40-bar studies, each in 4/4 at 100 BPM. They begin with the same event-level four-note motif: E4 G4 A4 G4, each one quarter beat. All instruments are the track's schematic standard-library sine/harmonic oscillators, with the same per-voice synthesis parameters in each piece. They are not acoustic instrument simulations or transcriptions of third-party music.

## Included plain-text sources

- `comparing-forms-041000.json`: all 888 original note events for the three finished scores; their annotated formal plans; timing, gain and waveform settings.
- `render_comparing_forms_041000.py`: score/event checker and optional WAV generator. It uses the existing `render_listening_lab.py` in the same directory.
- `041000-three-works-three-organizational-principles.md`: TTS narration plus a non-spoken bibliography, score-to-claim map, and listening prompts.
- `metadata/041000.json`: claim-level provenance anchored to exact narration passages.

No binary audio, MIDI, licensed instrumental soundfonts, reference voice material, or media downloads are packaged.

## The three finished scores

| ID | Piece | Event-level invariant |
|---|---|---|
| `ground_wheel` | *The Wheel and the Window* | Every 4-bar bass cycle is identical, repeated **10** times (bass C3-G3, A2-E3, F2-C3, G2-D3); upper material changes. |
| `return_arch` | *The Gate and the Road* | Five 8-bar parts A-B-A-C-A. Lead bars 1-8 and 17-24 are identical. Final refrain changes only the last melodic bar; accompanying bass in A2 also changes note durations. |
| `continuous_road` | *The Unbroken Path* | The opening idea undergoes a continuous sequence of variations, and there is no verbatim complete 8-bar lead window elsewhere. Final bar holds lead C4 for 4 beats over C3 (3 beats) and G3 (1 beat) in the bass. |

The checker verifies **only** declared pitch/timing invariants and event validity. It does not prove form is perceptible to human listeners, identify true cadences, judge artistic quality, or certify a historical idiom. The word "continuous" here is a composer-selected analysis of this original study, not a claim that it implements Reich's audible process aesthetic or a canonical Schoenberg developing-variation method.

## Check without rendering

From the repository root:

```bash
python content/music-theory/examples/render_comparing_forms_041000.py --check
python content/music-theory/citations/validate.py 041000
python tools/lecture_inventory.py
```

The validator confirms the shared opening motif, duration and source voices, 10 exact bass cycles, ABACA refrain identity, distinct episodes, and absence of a duplicated 8-bar continuous-development lead window.

## Render comparable excerpts

Choose the same bar span in all three pieces (here bars 17-24), so you can hear each strategy after the material has had time to unfold:

```bash
python content/music-theory/examples/render_comparing_forms_041000.py \
  --bar-range 17 24 \
  --output-dir /tmp/music-041000-excerpts
```

For the complete three pieces, omit `--bar-range`:

```bash
python content/music-theory/examples/render_comparing_forms_041000.py \
  --output-dir /tmp/music-041000-complete
```

All works are 40 bars, which is 96 seconds per work at 100 quarter-note beats per minute. That is a property of the composition and **not** an editorial runtime target. The renderer uses the Python standard library and may be slow for complete pieces. `--sample-rate 16000` is a faster rough listening option; higher sample rates can be chosen explicitly. No sources are normalized independently, so timbre and peak level are not equalized across different note densities.

To conceal labels during a casual listening exercise:

```bash
python content/music-theory/examples/render_comparing_forms_041000.py \
  --anonymous --bar-range 9 16 \
  --output-dir /tmp/music-041000-anonymous
```

The files are named `trial_01.wav`, etc., and a deterministic `answer_key.json` is written **in the same folder**. An experimenter must hide or move this file before showing trials to listeners. This is not a double-blind procedure, does not match perceived loudness, and cannot establish population-level listening results.

The standard-library WAV files can be imported into **Ardour** for timing, gain matching, panning, and comparative playback. Use **DawDreamer** separately if you want to render the *same source note events* with original, licensed instrument patches or offline processing chains. Doing so changes timbre and may change listeners' impressions; record plugin versions, patches, sample rate, and loudness controls. The demonstration renderer itself requires no DawDreamer installation.

## What to hear, without over-interpreting a diagram

- **Bars 1-8:** all three begin E-G-A-G; listen for what establishes identity after that common first bar.
- **Bars 17-24:** the ground's bass returns exactly, the rondo's lead refrain returns exactly, and the continuous work has no full literal reprise.
- **Bars 33-40:** the ground keeps its bass even as its ending gesture changes; the rondo alters its final refrain bar; the continuous work approaches a sustained closing C without an exact opening-section return.

See the lecture's source map and `metadata/041000.json` for named authors, chapter locators, and explicit source-access limitations. The score data supports mechanical claims about these pieces; external authors do **not** vouch for their musical quality.
