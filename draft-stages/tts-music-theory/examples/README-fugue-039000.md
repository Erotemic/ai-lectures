# Lecture 039000 — Fugal entries and development: original listening laboratory

This companion belongs solely to Agent D's music-theory pack. It includes **no recorded audio, image assets, copied scores, MIDI from commercial pieces, or third-party samples**. All pitches and beat times in `fugue-lab-039000.json` are newly authored classroom studies. They are neither a reconstruction of Bach BWV 847 nor a claim of complete historical-style counterpoint.

## Run

From the `ai-lectures` repository root:

```bash
python draft-stages/tts-music-theory/examples/render_fugue_039000.py --check
python draft-stages/tts-music-theory/examples/render_fugue_039000.py \
  --output-dir /tmp/fugue-039000 --anonymous
```

The renderer uses the Python standard library and reuses the adjacent `render_listening_lab.py` synthesizer for the exact same PCM and note conventions. Rendering is optional; the scored events are independently readable as JSON. The script creates WAVs and an `answer_key.json` under the chosen **local output directory**; do not commit those generated files to the content source pack. At 44.1 kHz the complete miniature is approximately 65 seconds; no authored lecture-duration target is implied.

To generate only short examples for inspection:

```bash
python draft-stages/tts-music-theory/examples/render_fugue_039000.py \
  --output-dir /tmp/fugue-039000-small \
  --only subject_alone real_answer tonal_answer exposition stretto
```

## Study list and musical tests

| ID | Bars | Independent musical question |
| --- | ---: | --- |
| `subject_alone` | 2 | Recognize the original subject's initial leap and fast turn |
| `real_answer` | 2 | All pitches transpose up exactly seven semitones |
| `tonal_answer` | 2 | Adapt opening tonic–dominant emphasis without claiming a uniquely correct answer |
| `invertible_above` | 2 | Two independent lines; subject above counterline |
| `invertible_below` | 2 | Same internal note events after exchanging register |
| `exposition` | 6 | Alto subject at beat 0; soprano answer at beat 8; bass subject at beat 16 |
| `episode_sequence` | 4 | A short fragment appears by exact transposition at beats 0, 4, 8, 12 |
| `stretto` | 4 | A second full subject starts at beat 4, before the first ends at beat 8 |
| `complete_miniature` | 28 | Exposition, episodes, renewed entries, stretto, late return, closing G2–C3 bass |

### What gets mechanically checked

- The real answer is exactly the subject shifted seven semitones; the tonal answer matches the declared adapted phrase.
- The two registral inversion examples preserve **every event** of their respective lines. At the eight integer beats, selected vertical intervals remain thirds or sixths in both examples. This is not a complete strict-counterpoint proof.
- Each declared full subject or answer is present at the specified time and in the specified voice of the `complete_miniature` score.
- The episode extract consists of four exact head-motive transpositions, not a silent reappearance of the entire subject.
- No event overlaps the next event in its own declared voice, escapes the bar grid, or exceeds the supported pitch and gain bounds.

### What cannot be checked this way

The score checker does not evaluate full harmonic progressions, melodic craftsmanship, style-dependent dissonance rules, instrumental range, or perceptual response. A tonal answer in a historical fugue depends on its subject, bass, and harmonic design. Likewise, actual fugue analysis can be debatable where an entry is partial, buried, or transformed. The local study is an explanatory prototype for those questions, not an automated substitute for counterpoint or musicological analysis.

## Reproduce with DawDreamer / inspect in Ardour

Choose oscillator or sampled-instrument plugins in DawDreamer, match the note-event timing, and document versions and render settings. The pure-Python WAV files can be imported into Ardour as reference tracks. Preserve loudness when making A/B comparisons; do not treat louder as automatically more successful. If you want source-separated stems, modify the local renderer to output each voice separately in your personal experiment directory, not to a committed binary asset in this pack.

## Attribution

Terminology and external history are explicitly attributed in `039000-fugue-and-larger-counterpoint.md` and `metadata/039000.json`, which maps spoken claims to source locators. The note events, validator invariants, and listening instructions are original teaching material. The source examples in Open Music Theory and Robert Hutchinson's textbook are **references to consult**, not material copied into this example set.
