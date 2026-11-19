# Lecture 037000: Eight ways to develop one musical idea

This folder contains **original text-only note events** for eight eight-bar studies in
`development-lab-037000.json` and a standard-library WAV-rendering entrypoint.
No recordings, samples, soundfonts, music by other composers, or binary media are
included in the ZIP. No background processing is required to use the lecture.

## Try the score checker first

From the repository root:

```bash
python content/music-theory/examples/render_development_037000.py --check
```

The checker verifies 8 variants, their time bounds and rhythmic consistency, a
shared C2 reference drone, the specified chromatic transpositions, true
inversion around E4, a two-bar plus octave copy in the canon, additive note
counts, and the form of the repeat/return examples. It does **not** measure
perceived beauty, authentic call-and-response performance, or listener response.

## Generate comparisons

```bash
python content/music-theory/examples/render_development_037000.py \
  --output-dir /tmp/music-development-037000 --anonymous
```

Generated audio uses the same simple reference oscillator as the previous
033000–036000 listening lab. The shuffled filenames hide the technique label;
`answer_key.json` records the stable mapping and SHA-256 hashes. The script
**writes** an answer key, so do not open it before blind listening.

To preview one study while developing it:

```bash
python content/music-theory/examples/render_development_037000.py \
  --only octave_canon --output-dir /tmp/canon-study
```

Output is 16-bit stereo PCM WAV. Default rate is 44,100 samples/second. The
renderer accepts `--sample-rate`, which can be lowered for a fast technical
smoke test; the default better supports ordinary listening. Rendering is
**offline**. There is no TTS, plugin, or sound-card dependency.

## Listening protocol

1. Play all eight studies without seeing the answer key. Identify motif returns,
   density changes, alternation, overlaps, quiet stretches, and endings. Avoid
   calling any technique best before identifying its concrete effect.
2. Reveal the source labels; inspect `development-lab-037000.json` to test
   whether your first hearing matched the authored organization.
3. Import the resulting WAVs into **Ardour** and align their starts. Trim or
   compare playback gain as needed because simultaneous-note counts vary. The
   comparisons are **not** laboratory loudness-matched.
4. Optionally map the same event data to instruments and processing graphs in
   **DawDreamer**. Save the plugin, tempo and render configuration. The provided
   renderer remains the minimal reproducible timing reference.
5. Modify one structural rule at a time: delay an answer, interrupt a sequence,
   remove a layer, extend the ostinato, or move the return. Listen again and
   describe the difference without treating your own preference as a general
   psychoacoustic finding.

## Source and historical boundary

The performance practices described in the lecture are documented separately
by Smithsonian Folkways and music scholarship. These eight audio files are
**not** performances of the traditions discussed. The lesson's source-to-claim
reading map and `metadata/037000.json` give detailed attributions. The original
score events should never be misattributed to Reich, Caplin, Margulis, or any
tradition's practitioners.

## Study index

| ID | Device | Main data invariant |
|---|---|---|
| `dialogue` | Alternating calls and responses | Left bars 1/3/5/7, right bars 2/4/6/8 |
| `sentence_inspired` | Establish, repeat, continue | Bars 1/3 repeat a motif, bar 8 closes on C4 |
| `sequence` | Transposition | Exact chromatic shifts of 0,2,4,5,7,5,2,0 semitones |
| `variation` | Transformation | Exact inversion about E4 in bar 3; doubled rhythm in bar 4; original motif returns |
| `ostinato_layers` | Repeated ground and additions | E3 G3 A3 G3 in each bar of lower voice |
| `octave_canon` | Overlapping imitation | Follower equals leader at +8 beats, down 12 semitones |
| `additive_process` | Accumulation | Melody has 1,2,3,4,4,4,4,4 notes per successive bar |
| `contrast_return` | Leave and return | Melody silence in bar 6; motif in bars 1 and 7 |

All variants use four beats per bar, eight bars and 96 BPM, with a quiet C2
drone. Since sequences move against a fixed bass and the examples use no
functional chord progression, **none** of them asserts a textbook perfect
authentic cadence or an authentic period/sentence in full tonal detail.
