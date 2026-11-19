# Lecture 040000 — The Returning Line: complete-work laboratory

The lesson's entire 40-bar composition is original to this course. Everything required to reconstruct its pitches, section plan, first draft, revisions, and alternate mix is provided as **UTF-8 source text**, not a fixed recording or a sampled performance.

## What is provided

- `complete-work-040000.json`: 40 numbered bars with the harmonic and melodic plan, five eight-bar sections, 2 specific melodic edits, and 6 explicit alternative rendering event lists.
- `render_complete_work_040000.py`: validates each event, the motif repetitions/transposition, the two note edits, the controlled arrangement changes, and the distinction between note changes and mix-only changes. Uses the track's existing `render_listening_lab.py` oscillator routine to render stereo WAVs when requested.
- `040000-from-motif-to-finished-piece.md`: spoken analysis and non-spoken score/source companion.
- `metadata/040000.json`: per-claim attribution, with exact spoken passage anchors and cited-source locators.

No WAV, MIDI, instrument-sample, plugin binary, or third-party musical score is shipped. Sound is generated locally from the new note events. No claim of historical-instrument simulation or production-ready artistic success is made.

## Verify the original score

Run from the repository root:

```bash
python content/music-theory/examples/render_complete_work_040000.py --check
python content/music-theory/citations/validate.py 040000
```

The validation tests structural invariants, *not aesthetic conclusions*. In particular:

1. Forty 4/4 melody bars use valid, non-overlapping notes totaling exactly four beats each.
2. Bars 1, 9, and 25 repeat the opening head with the same pitches and rhythm; bar 17 transposes it exactly seven semitones higher.
3. `dense_first_draft` and `texture_revision` keep the exact same lead notes. The former has forty padded bars; the latter has twenty, and eight short secondary figures (32 events).
4. `texture_revision` and `revised_score` differ **only** in lead pitch at bar 20 beat 4 (`F5 → F#5`) and bar 40 beat 4 (`G4 → C5`); all supporting event lists are identical.
5. `revised_score` and `alternate_mix` contain exactly equal note-event lists and differ in fixed per-voice gains/panning. The validator does not measure the perceptual outcome.

## Generate audio locally (optional)

A quick, low-cost 4-bar excerpt from two versions, so you can test your audio setup first:

```bash
python content/music-theory/examples/render_complete_work_040000.py \
  --only dense_first_draft revised_score \
  --bar-range 17 20 \
  --output-dir /tmp/complete-work-040000-excerpt
```

To render the six studies in their entirety:

```bash
python content/music-theory/examples/render_complete_work_040000.py \
  --output-dir /tmp/complete-work-040000
```

To make an anonymous **exploratory** comparison and keep an answer key:

```bash
python content/music-theory/examples/render_complete_work_040000.py \
  --only dense_first_draft texture_revision revised_score alternate_mix \
  --anonymous \
  --bar-range 17 24 \
  --output-dir /tmp/complete-work-040000-anonymous
```

The output directory contains `.wav` files and `answer_key.json` with content hashes and labels. The anonymous mode randomizes presentation order deterministically but is **not** a full double-blind listening study. Its answer key is written into the same directory, so an experimenter must separate it before testing participants.

The oscillator renderer is computationally simple in design but pure Python; long full-length renderings can still take time. WAVs are 16-bit stereo with a fixed (non-normalizing) master scale. Changing sample rates, gains, panning, or source patches affects audible output and hashes. Full versions span 40 bars (approximately 92.3 seconds at 104 quarter beats per minute); length is a property of the original score, **not** a lecture-runtime target.

## Compare one variable at a time

- **Composition and harmony:** `lead_only` versus the supporting arrangements; describe how the harmonic floor changes our hearing of the repeated head.
- **Arrangement:** `dense_first_draft` versus `texture_revision` (lead is unchanged). Secondary figures are deliberately not presented as strict species counterpoint.
- **Melody revision:** `texture_revision` versus `revised_score` (two pitches differ, not tempo, bass or pads). Does the F-sharp at bar 20 help signal the D7/G area? Does a final C feel more settled than G?
- **Mix:** `revised_score` versus `alternate_mix` (identical note data). These two versions are intentionally **not loudness-matched**. Compare once as provided, then match levels in Ardour and compare again before attributing a difference to artistic quality.

All voices are schematic tone generators (`sine`/`harmonic`), not physical models of violins, guitar, singers, or room acoustics. You can import WAVs in Ardour for alignment, basic gain/panning checks, and optional processing. For alternate instruments and reproducible plugin graphs, use DawDreamer separately; the lecture does not promise its results will be byte-for-byte identical to the included standard-library renderer.

## Evidence and attribution limits

See the manuscript's non-spoken bibliography and `metadata/040000.json` for external source titles, authors, publication data, chapter/section locators, direct HTTPS links, and evidence access limitations. The `claim_evidence` entries explicitly classify **source-backed theory**, **original mathematical calculations**, **original authored score facts**, and **interpretive production proposals**. The original score is its own evidence for literal notes and timing. It is *not* evidence that real listeners prefer a revision or that a historical theorist would classify a cadence in a particular way.
