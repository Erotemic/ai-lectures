# Machine-checkable examples for Music Theory and Composition

These files encode the **original instructional scores** in selected lectures as
UTF-8 JSON. They do **not** include recordings, MIDI files, audio playback,
notation software, audio synthesis, or a requirement to own an instrument.

- [`scores.json`](scores.json) contains seven examples from lectures 004000,
  005000, 006000, 008000, 010000, 011000, and 012000.
- [`validate.py`](validate.py) checks 53 source-table rows across the seven
  examples, including pitch spelling, exact event timing, bar boundaries,
  harmony labels, two-voice counterpoint, and simple rhythmic cycles.
- [`test_validate.py`](test_validate.py) checks the validator's arithmetic and
  that a changed event or an invalid duration fails validation.

All paths belong to the music track. Neither the central audio reader nor a
shared course registry needs to change.

## Run

From any working directory:

```sh
python draft-stages/tts-music-theory/examples/validate.py
python -m unittest discover -s draft-stages/tts-music-theory/examples -p 'test_*.py'
```

The validator reads the JSON and the live lecture markdown. It is intentionally
**not** a source code generator. If a manuscript's table changes without its
companion JSON changing, validation fails, preventing a stale demonstration from
being treated as authoritative. A changed JSON that departs from the manuscript
also fails. The source tables are the reference for content; the JSON is a
machine-usable second representation.

## Conventions

- A **bar index** is 1-based. Within a bar, `at` is a **zero-based** onset in
  quarter-note units. Thus `at: "2"` is beat **3** of a 4/4 bar.
- `dur` is a strictly positive duration in the same quarter-note units.
  Both are exact rational strings, such as `"1/2"` or `"3/2"`, not floating-point
  seconds. Tempo is deliberately unspecified.
- Pitches use scientific pitch notation, for example `C4`, `F#4`, `Bb3`.
  C4 is middle C. The validator can convert pitches to MIDI note *numbers*
  under a 12-tone equal-tempered mapping, but does not select a sound source
  or assert that equal temperament is appropriate for every musical tradition.
- `chord` specifies an intended harmonic label **without** implying that every
  chord tone is sounding. Where the original table gives only melody, the JSON
  contains only melody. It does not invent missing inner voices, bass notes,
  voicings, or instrumentation.
- `bass` is present only when the original score explicitly gives a bass line.
  In lecture 008000 a supplemental bar-7 `reply` is included to document the
  separate response against the held melodic D4.
- `nonchord` lists spelled pitch classes appearing in the melody but absent
  from the declared harmony. It is **not** a classification of their full
  contrapuntal role: that requires approach, departure, timing and other voices.
- The rhythm examples use eighth-note positions or a six-unit attack cycle.
  They are *attack grids*, not invented pitched percussion performances.

Example event from the workshop's bar 5 (beat 1, an eighth note):

```json
{"at": "0", "pitch": "D4", "dur": "1/2"}
```

The next event begins at `"1/2"`, and a four-quarter-note bar ends at `"4"`.
Different instruments, a voice, and a sequencer could all perform the same
abstract events. Future audio generation should add explicit tempo, tuning,
voice assignment, instrument definitions, articulation, loudness, overlap and
note-off policies in a *separate* layer. The current JSON makes no claims
about the listener's perceptual impression without a realized recording.

## Scope and limitations

The seven examples were selected because the manuscripts actually provide
reproducible note/timing tables. These are **not** the entire corpus of
12 lectures; examples involving only verbally specified impressions,
unspecified voicings, or alternative tunings have not been silently filled in.
The validator is for source consistency and elementary mathematical invariants,
not an automatic musical quality judge. It does not decide whether a cadence
sounds final, whether dissonance is desirable, or whether a guitar fingering
is physically possible.

The correction in lecture 008000 is verifiable without audio: the interval
between D4 and E4 is **two semitones (a major second)**, not one semitone
(a minor second). The subsequent D4–G4 interval is five semitones
(a perfect fourth).
