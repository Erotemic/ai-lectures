# 042000 — constrained composition, revision, and listening lab

This is the **plain-text** companion to lecture `042000-rules-that-help-and-rules-that-trap.md`. All eight sixteen-bar pieces, their note events, and their auditable constraints are original classroom examples, not transcriptions or soundalikes of published music. No copyrighted audio, instrument patches, voices, or WAV binaries are shipped.

The experiment distinguishes four possible functions of a rule: restricting source material, restricting rhythmic position, specifying an imitation process, and delegating local choices to a reproducible procedure. Every comparison changes something observable in event data. It does **not** demonstrate that any change is superior, that the audience hears the difference, or that a procedure produces creativity.

## Files

- `constraints-042000.json`: eight complete source-event scores, four pair identities, the six-cell original candidate bank, exact pseudorandom draw selections and three explicitly documented editorial replacements.
- `render_constraints_042000.py`: validation of event bounds, pair controls and claimed changes; optional standard-library WAV rendering via the existing `render_listening_lab.py` module.
- `042000-rules-that-help-and-rules-that-trap.md`: standalone spoken lecture and non-spoken claim map.
- `../metadata/042000.json`: precise claim-level attribution, with original score facts distinguished from historical sources.

## The eight complete pieces

Each work is 16 bars, 4/4, 100 BPM. All eight use exactly the same two-note-per-bar bass and held inner voice. The lead oscillator waveform, source gain, and pan settings remain constant, and the corresponding accompaniment voice settings remain constant. The imitation pair includes a fourth, separately configured follower voice.

| Pair | Original work IDs | Exact question |
|---|---|---|
| Pitch material | `palette_closed`, `palette_released` | What changes if four notes in the second half are allowed to leave the five-pitch-class C D E G A palette? |
| Rhythmic placement | `rhythm_grid`, `rhythm_shifted` | What changes when two onbeat attacks per bar move to the offbeats in bars 9–16, without changing pitch order? |
| Delayed imitation | `echo_exact`, `echo_broken` | Can local independence at bars 11–12 make sense within a mostly exact imitation? |
| Pseudorandom selection | `draw_fixed`, `draw_revised` | What is the difference between using a deterministic candidate draw and editing three of its bar choices? |

**Score-specific controls:** all 16-bar versions begin with E4 G4 A4 G4 as quarter notes. The bass alternates C3-G3, A2-E3, F2-C3, G2-D3 per four bars. One constant held inner note accompanies each bar. Accompaniment is held exactly event-for-event even in the rhythm and pitch studies. The closed palette is C D E G A as **pitch classes**, not a limit of five absolute pitches. The released version changes exactly four notes: at bars 10 and 14 C5 becomes B4, and at bars 11 and 15 E4 becomes F4. Every substitution is one semitone.

The rhythmic comparison keeps the melody pitches unchanged but after bar eight uses each bar's onset offsets `[0, 1.5, 2, 3.5]` and durations `[1, 0.5, 1, 0.5]` in quarter-note beats. The imitative comparison shifts the lead by four beats and lowers it one octave, omitting source bar 16 because there is no room for its echo. It changes only the follower's bars 11–12 from eight quarter-note attacks to four half-note attacks. This is **not** a baroque contrapuntal-correctness checker.

The bounded-draw example has six four-note cells. Its first bar is fixed. Bars 2–16 follow `random.Random(42000).randrange(6)` and are also stored as explicit selected indices. The edited version replaces the selected cells in bars 8, 12, and 16. The raw last bar is D4 F4 E4 D4; the edited last bar is D4 E4 G4 C4. This is **not** a Cage-style chance score; the composer has restricted the bank, fixed the opening, and made three revisions afterward.

## Verify only the new scores

From the repository root:

```bash
python content/music-theory/examples/render_constraints_042000.py --check
python content/music-theory/citations/validate.py 042000
python tools/lecture_inventory.py
```

These are local checks on one authored pack, not a mandatory server-wide test suite. The score checker verifies exact event relationships; the citation checker verifies anchor/source structure, not the correctness of a research interpretation.

## Render corresponding excerpts

Render only bars 9–12 from the restricted/open pitch pair:

```bash
python content/music-theory/examples/render_constraints_042000.py \
  --pair pitch --bar-range 9 12 \
  --output-dir /tmp/music-constraints-042000-pitch
```

Other pair IDs are `rhythm`, `imitation`, and `choice`. To make the listening files anonymous in filename order, add `--anonymous`. The renderer then writes `trial_01.wav`, etc., and an `answer_key.json` **in the same output directory**; whoever administers the listening should hide the answer key from participants before they inspect the folder. Selecting a pair is a convenience for listening, not a rigorously blinded experiment.

For a complete pair, omit `--bar-range`. For a single version, use `--only palette_closed` or another version ID. The default sample rate is 22,050 Hz, and `--sample-rate` accepts the range supported by `render_listening_lab.py`. Rendering all eight full scores is slower than rendering short excerpts because the educational oscillator is implemented using the Python standard library.

The renderer does not independently loudness-normalize versions. That preserves source gains but does not guarantee equal perceived loudness: the number of overlapping notes can differ, especially in imitation. For formal perceptual comparison, control playback gain, order, and monitoring, and record which choices were made. No listener study was performed when preparing this lesson.

## DawDreamer and Ardour

All score data uses text-defined pitches and timings in quarter-beat units. The reference renderer is a simple sine/harmonic oscillator; it does not use DawDreamer, emulate acoustic instruments, or claim production-ready synthesis. If you want to compare timbres, translate the same events into a DawDreamer rendering graph using licensed plugins, keeping the note-event state and plugin settings reproducible. To listen and compare in a DAW, import the generated WAVs into Ardour, align them to bar one, and note any level changes, panning, effects, or channel differences.

Do not commit or include the resulting binary WAVs in Agent D's content ZIP.
