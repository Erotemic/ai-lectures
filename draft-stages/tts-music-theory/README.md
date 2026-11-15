# Music Theory and Composition

**Collection:** Twenty standalone, audio-first lecture manuscripts. The course is instrument-agnostic and its original text scores remain useful before audio demonstrations are available. Sound-producing examples are an eventual extension, not a requirement for understanding the descriptions.

## Completed and indexed lectures

| ID | Lecture | Spoken words | Approx. minutes at 145 wpm |
|---|---|---:|---:|
| 001000 | [Music as Pattern in Time: A Listener's Way into Composition](001000-music-as-pattern-in-time.md) | 2,214 | 15.3 |
| 002000 | [Pitch, Intervals, and the Shape of a Melody](002000-pitch-intervals-and-melodic-shape.md) | 2,554 | 17.6 |
| 003000 | [Rhythm, Meter, and Groove: How Music Organizes Time](003000-rhythm-meter-and-groove.md) | 2,674 | 18.4 |
| 004000 | [Scales, Chords, and Harmonic Direction: Compose a Four-Bar Phrase](004000-scales-chords-and-composing-a-phrase.md) | 2,895 | 20.0 |
| 005000 | [Voice Leading and Counterpoint: How Musical Lines Work Together](005000-voice-leading-and-independent-lines.md) | 2,409 | 16.6 |
| 006000 | [Phrases, Cadences, and Development: Making a Musical Idea Go Somewhere](006000-phrases-cadences-and-musical-development.md) | 2,401 | 16.6 |
| 007000 | [Chord Voicing, Inversions, and Harmonic Color](007000-chord-voicing-inversions-and-harmonic-color.md) | 2,663 | 18.4 |
| 008000 | [Form, Texture, and Arrangement: Turning an Idea into a Piece](008000-form-texture-and-arrangement.md) | 2,662 | 18.4 |
| 009000 | [Modes, Tonal Centers, and Pitch Collections: The Same Notes, a Different Home](009000-modes-tonal-centers-and-pitch-collections.md) | 1,739 | 12.0 |
| 010000 | [Chromatic Harmony: Borrowed Colors and Temporary Destinations](010000-chromatic-harmony-and-borrowed-colors.md) | 1,750 | 12.1 |
| 011000 | [Unequal Beats and Interlocking Cycles: Meter Beyond Four](011000-additive-meter-polyrhythm-and-rhythmic-cycles.md) | 1,881 | 13.0 |
| 012000 | [From Sketch to Piece: Variation, Contrast, and Musical Revision](012000-composition-workshop-variation-and-revision.md) | 2,414 | 16.6 |
| 013000 | [Changing Musical Home: Tonicization, Modulation, and the Return](013000-changing-musical-home-modulation.md) | 1,798 | 12.4 |
| 014000 | [Beyond a Scale: Musical Grammars, Rāga, Tāla, and Maqām](014000-musical-grammars-raga-tala-maqam.md) | 1,973 | 13.6 |
| 015000 | [Timbre as Composition: Arrangement, Sound Design, and a First Mix](015000-timbre-arrangement-and-production.md) | 2,001 | 13.8 |
| 016000 | [The Long Arc: Composing and Revising a Forty-Eight-Bar Work](016000-composing-a-forty-eight-bar-work.md) | 2,100 | 14.5 |

| 017000 | [What a DAW Computes: Samples, Tracks, Routing, and Real-Time Deadlines](017000-what-a-daw-computes.md) | 1,760 | 12.1 |
| 018000 | [Four Separate Tracks, One Musical Space: Why Mixing Matters](018000-why-independent-stems-need-mixing.md) | 2,011 | 13.9 |
| 019000 | [A Mix Is a Processing Graph: DawDreamer, Ardour, and the CPU Budget](019000-a-mix-as-a-processing-graph.md) | 1,765 | 12.2 |
| 020000 | [From Stems to a Finished Master: Monitoring, Loudness, and Reproducible Exports](020000-from-stems-to-a-finished-master.md) | 1,898 | 13.1 |

Word counts are descriptive: they use whitespace-separated words in the narration extractor output, matching the track inventory. Duration is only a rough read-through estimate, not an editorial target.

## Course approach

The first twelve lectures move from musical pattern, pitch and rhythm through harmonic and contrapuntal construction, phrase/form analysis, modal center, chromatic harmony, polyrhythms and revision of a sixteen-bar study. The next four lectures extend that foundation into changes of tonal home, **carefully scoped** cross-cultural comparison, timbre and production, and a complete 48-bar two-line study. Lectures 017000–020000 then explain PCM audio, DAW routing and scheduling, the musical problem of combining independent stems, the differences between offline DawDreamer processing and Ardour live mixing, and the decisions involved in mastering and delivery.

Examples in `examples/` are optional machine-readable companions to some earlier scores. There is no claim that written pitch grids capture the intonation, ornamentation, idiom, or artistic effect of every musical practice. For traditions best transmitted through performance and listening, further training and direct encounters with sound remain essential.

## Further work (not indexed as completed)

1. Ear-training and score-to-sound correspondence once a reproducible audio-demonstration mechanism exists; first add source-linked original examples and permissioned listening materials.
2. Comparative tuning, including temperaments and context-dependent microtonality, taught without forcing every musical system into fixed Western keyboard notes.
3. Deeper contrapuntal techniques, imitation, canon, and multi-voice arrangement.
4. Contemporary songwriting, production workflows and collaborating with performers, including feedback-led edits to actual sounding work.
5. Additional large-scale formal types and composition contexts beyond major/minor tonal writing.

## Reference and integrity conventions

- `track.json` lists **only existing** numbered manuscripts; each has one spoken marker pair and a corresponding `metadata/<id>.json` citation sidecar.
- `metadata/sources.json` records per-track references, including references to musical traditions by specialist sources rather than treating the original classroom exercises as transcriptions.
- Do not embed copyrighted music or binary audio in overlay ZIPs. Any future sound renderer should use authorized or original material and track the associated musical data and rights.
