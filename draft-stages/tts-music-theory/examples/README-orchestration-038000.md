# Lecture 038000: Orchestration as composition — six original studies

This study holds only source text. It **does not** contain audio recordings,
commercial samples, any composer's score, or a software instrument. The event
file `orchestration-lab-038000.json` encodes an original eight-bar tune and six
ways to layer or allocate that material, with a fixed 96 BPM, four-beat grid.

The renderer is a **small, deliberately crude oscillator reference**. It models
neither acoustic instrument technique nor real-world timbre. Its central
purpose is to give a stable representation of pitches, entrances and timing
before repeating the experiment with real performances or sampled instruments.

## Validate the authored claims about the score

From the repository root:

```bash
python draft-stages/tts-music-theory/examples/render_orchestration_038000.py --check
```

This checks the unchanged 32-event melody and eight-event C2 reference in
every version, the unison copy's identical attacks, the exact octave relation
between the two arpeggios, entrances at bars 3 and 5, the two distinct
foreground timbres at the bar-5 handoff, time bounds and supported pitches.
It checks neither musical value nor the claimed perceptual effects. In
particular, a score cannot prove that two synthesized voices are heard as
one stream or that moving an accompaniment down an octave improves clarity.

## Generate the six WAV comparisons

```bash
python draft-stages/tts-music-theory/examples/render_orchestration_038000.py \
    --output-dir /tmp/orchestration-studies-038000 \
    --anonymous
```

This generates uncompressed stereo PCM reference WAVs and `answer_key.json`.
Files prefixed `trial_` are in a deterministic shuffled order; **do not open
the answer key before listening**. For a single labeled version:

```bash
python draft-stages/tts-music-theory/examples/render_orchestration_038000.py \
    --only spaced_background --output-dir /tmp/spaced-038000
```

It is fine to generate 44.1 kHz stereo locally, but **do not commit generated
WAVs**. The only artifact for collaboration is text-defined source.

## Experiments in Ardour and DawDreamer

1. Import the six WAVs as separate Ardour tracks and align their starts. Use
   identical monitor settings. For loudness-sensitive comparisons, match
   playback levels manually: the studies have different numbers of voices,
   and they are not research-grade loudness-matched stimuli.
2. With `crowded_background` and `spaced_background`, inspect the event JSON
   alongside listening. The two middle voices have the same attack times and
   pitch classes; only their octave differs. Describe which line you can
   actually follow, rather than declaring one arrangement objectively better.
3. Make a second arrangement in DawDreamer using instrument plugins. Record
   plugin name/version, soundfont/sample rights, preset, pitch maps, articulation,
   envelope, render sample rate and output hash. Separate acoustic claims from
   claims that apply only to a particular virtual instrument.
4. Compare the orchestra/arrangement fix with a mix-only fix. For example, keep
   crowded notes but lower the secondary fader in Ardour. Compare that with
   moving the secondary part down an octave, with fader unchanged. Ask which
   musical information each intervention preserves.
5. Reverse the `staged_entrances` arrangement so the layers *leave* instead of
   arriving. Keep the melody; listen for the formal effect of subtraction.

## What is—and is not—derived from publications

The author-created scores are not transcriptions. McAdams, Goodchild and
Soden (2022) supply the general concurrent/sequential/segmental framework;
see `metadata/038000.json` and the direct links in the lecture companion.
Philharmonia instrument guides are sources for acoustic playing techniques
and ranges, **not** for the synthetic event data. Rimsky-Korsakov's 1922 text
is a historically situated treatise rather than a rule for all instruments or
styles. DawDreamer and Ardour references document available software
operations, not the artistic results of this exercise.

## Study index

| ID | Authored change | Key score condition |
|---|---|---|
| `skeleton` | Leave only foreground melody + bass reference | 32 foreground + 8 bass events |
| `synchronous_doubling` | Add a second synchronized unison source | Secondary pitch and timing exactly copy all 32 melody events |
| `crowded_background` | Add C4 E4 G4 E4 accompaniment | Four 1-beat events in each of eight bars |
| `spaced_background` | Same accompaniment down one octave | Exact time and pitch-class correspondence with crowded version |
| `staged_entrances` | Accompaniment starts bar 3; sustained E5 starts bar 5 | Additional sources at beats 8 and 16 |
| `timbral_handoff` | Switch melody carrier at bar 5 | Two voices partition the same 32 melody events at beat 16 |

No timings or sounds in this companion are intended as historical evidence
about an acoustic ensemble. The purpose is a reproducible arrangement thought
experiment to supplement listening to real performers.
