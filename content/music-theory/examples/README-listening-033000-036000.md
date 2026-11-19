# Original listening lab for lectures 033000–036000

This is a **source-only** set of reproducible exercises. No binary recordings,
licensed sample packs, models, or copyrighted composition excerpts are included.
All notes and examples were newly authored for this teaching material.

The score and renderer live entirely in the music-theory pack:

- `listening-lab-033000-036000.json`: 18 named, precisely specified original
  renderings spanning interval recognition, triads, just-versus-equal tuning,
  counterpoint, suspensions, a short canon, and an 8-bar transcription workshop.
- `render_listening_lab.py`: optional standalone, deterministic *text-only*
  Python audio generator using `math`, `array`, `wave`, and the standard library.

## Render locally

From the repository root:

```bash
python content/music-theory/examples/render_listening_lab.py --check
python content/music-theory/examples/render_listening_lab.py \
  --output-dir /tmp/agent-d-listening-lab --anonymous
```

This generates stereo 16-bit PCM WAV files (default 44.1 kHz), plus a separate
`answer_key.json` identifying the original pitches and treatments. The `--anonymous`
option uses a deterministic shuffle and generic file names so a student can
avoid reading the answer while listening. To render one score quickly:

```bash
python content/music-theory/examples/render_listening_lab.py \
  --only tuning_5to4 tuning_12tet \
  --output-dir /tmp/agent-d-tuning
```

The output directory is **outside the repository**. Do not add the generated
WAVs to content ZIPs or assume they belong in Git. The renderer deliberately
uses an uncomplicated oscillator with either a single sine or up to five
integer harmonics; it is a controlled auditory reference, **not** a professional
instrument simulation, a scientifically validated listener study, or a model of
any specific non-Western performance practice. All note starts/durations are
specified in quarter-note beats, and every rendering explicitly sets its tempo.

## DawDreamer and Ardour

DawDreamer can load the generated waveform into a playback processor or render
these **same original note events** using an explicitly configured synthesizer
and processing graph. When comparing two cases, keep the processor graph,
plugin state, sample rate, amplitude, and timing the same unless a change is
**part of the controlled treatment**. Do not assume an unrelated plugin preset
will reproduce the waveform from this standard-library oscillator.

Import the generated files into Ardour as regions, align the starts of each
comparison, and listen through the same monitor chain. Use region looping for
short comparisons. Avoid applying normalization independently to the two
versions when the controlled variable is level or intonation. The original
transcription and revised files can be imported as separate takes or tracks.

Official documentation (these sources establish software capabilities,
not pedagogical efficacy):

- [DawDreamer User Guide — RenderEngine, processors, graphs, rendering](https://github.com/DBraun/DawDreamer/blob/main/docs/user_guide/index.rst)
- [Ardour Manual — Region Menu, Loop, Play Selected Regions, Spectral Analysis](https://manual.ardour.org/ardours-interface/main-menu/Region-menu/)

## Hearing tasks and expected answers

| Group | Files | Task | Score answer |
|---|---|---|---|
| 033 intervals | `ear_7semis`, `ear_8semis`, `ear_octave` | Hear rise, size and transposition potential | A4→E5 is 7 equal semitones, A4→F5 is 8, A4→A5 is an octave |
| 033 chords | `ear_triad_major`, `ear_triad_minor` | Separate chord quality from timbre | C–E–G versus C–E-flat–G |
| 034 tuning | `tuning_5to4`, `tuning_12tet` | Hear or fail to hear an *identically controlled* tuning difference | 400:500 Hz vs 400:503.968… Hz; no mandated preference |
| 035 first-species-inspired | `counterpoint_cantus`, `counterpoint_upper`, `counterpoint_duet` | Follow two independent lines | P5, m3, m3, M3, M3, M3, M6, P8 |
| 035 suspension | `suspension_4_3` | Hear a held note change status as bass changes | A3/F4 sixth → C4/F4 fourth → C4/E4 third |
| 035 canon | `canon_leader`, `canon_follower`, `canon_duet` | Identify the imitation and delay | Octave-down follower exactly four beats later |
| 036 transcription | `transcription_melody`, `transcription_bass`, `transcription_original`, `transcription_revision_b` | Transcribe, re-render, compare | Original eight bars; revision changes only bar 7's final three pitches |

## What can and cannot be validated

The script's `--check` mode validates numeric event bounds, pitch spelling,
rendering IDs, and the transcription revision's deliberately limited change.
The PCM renderer fails if it would exceed the permitted audio level, rather
than silently normalizing comparison files. It cannot establish that a listener
will hear an intended difference or make a particular artistic judgment.

The source JSON includes the answer and is not a secrecy mechanism. The
`--anonymous` option is for convenience in a self-administered exercise, not a
validated double-blind procedure. The `answer_key.json` is generated alongside
WAVs, so hide or move it before the audition. The script's MIDI-derived equal
frequencies assume 12-TET with A4=440 Hz; the two tuning files explicitly
supply Hz values instead.
