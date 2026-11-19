# 036000 — From Sound to Score and Back: Transcribe, Reconstruct, Revise

**Track:** Music Theory and Composition. **Audience:** composers, analytical listeners, creators of generative-audio tools. **Background:** basic pitch, rhythm, harmony, and audio editing; all important operations are explained. **Purpose:** complete one original audio-to-score-to-audio cycle, understand its ambiguities, and make revisions that can be evaluated by listening.

<!-- BEGIN SPOKEN LECTURE -->

# From Sound to Score and Back: Transcribe, Reconstruct, Revise

Imagine receiving a short recording from a composing agent. It sounds finished enough to make sense as a tune. But the agent has lost the score, or perhaps never made one. You want to understand the phrase, change its seventh bar, and send it back to a renderer without destroying the timing and articulation that made the original interesting. This is not simply copying notes from a sound file. It is a problem of recovering a useful musical description from an acoustic event, deciding what information matters, and accepting what cannot be recovered uniquely.

A waveform is a time series of amplitude values. It does not contain a neat list of note names. Two notes played at the same time contribute to one pressure signal at the microphone or one set of samples in the export. A note's onset may include noise, and its sustained sound may have many partials. Reverberation can keep a previous note sounding after the performer has released it. A transcription process must infer the events behind those observations. That inference can be easier with a solo monophonic instrument and harder with dense polyphony, percussion, and expressive timing.

Emmanouil Benetos, Simon Dixon, Dimitrios Giannoulis, Holger Kirchhoff, and Anssi Klapuri surveyed automatic music transcription in a 2013 article, Automatic Music Transcription: Challenges and Future Directions. Their review explains why general-purpose transcription does not simply reduce to reading frequencies off a spectrogram. Instrument characteristics, musical context, note overlap, and task-specific assumptions matter. The paper is a review of techniques and challenges, not an experimental certification of this particular workshop. Our objective is to learn how to reason about an inference problem, with or without an automatic transcription model.

We will work with an original eight-bar study in common four-four. Its tempo reference is ninety-six quarter-note beats per minute. There is a melody line and a bass line. The harmonic plan is C major, F major, G dominant seventh, C major, A minor, D minor, G major, C major. This is a consciously simple tonal setting, chosen so that musical attention can go to contour, grouping, and revision rather than a large harmonic vocabulary. The specific notes are authored for this lecture; they are not transcribed from an existing song.

On the first bar, the melody plays E, G, A, G as four quarter notes. The bass holds C for the bar. On the second, the melody moves A, G, F, E over a sustained F. The third has D, F, G, B over a sustained G. The fourth rises to C above the staff, then falls to G, E, and G over C. That is the first four-bar phrase. It moves from a small rising gesture into a return, with one note of the dominant seventh chord providing color in bar three.

The second phrase begins A, C, B, A above an A-minor bass. In bar six, F, A, G, F sounds above D. Bar seven climbs D, G, B, D, moving into the upper register over G. Bar eight settles into C, G, E, C above a final C bass. There is no claim that this is the best melody a human could write. Its virtue is that we can specify it exactly and then ask what we actually hear. A listener can reconstruct its rhythm, note contour, bass motion, and broad harmonic direction without knowing its names in advance.

First listen to the combined audio, without a visible score. Do not attempt to name every note. Mark where the phrase seems to divide and whether the second half repeats, answers, or contrasts the first. Next tap a steady beat through the entire piece. If you are not sure where beat one begins, listen for bass changes and phrase entrances, but do not assume every bass event necessarily marks a downbeat in arbitrary music. Here it does by construction. In the answer data, each bass tone begins on beat one and lasts four quarter-note units.

Then listen to the melody alone. Write one symbol per attack, even if the symbol is just a dot. Place the dots at the attacks you hear on the beat grid. Do not assign pitches yet. You should find thirty-two melody attacks, four in every bar. If you find fewer, did you miss a repeated note? If you find more, did a sharp timbral transient sound like a second note? If you mishear the tempo at half or double its stated rate, your rhythm grid can still look consistent while representing a different meter. This shows why the pulse is a hypothesis to test, not a number guaranteed by the samples.

Next mark only contour: up, down, or same between adjacent attacks. The opening moves upward twice and then falls. The second bar mostly falls. In bar four the first note is much higher than the preceding bar's final B; later the line drops. When your contour is stable, use a reference pitch or a known bass note to assign actual names. An exact key-independent contour can still be reconstructed when absolute pitch is uncertain. That is useful information, not a failed transcription.

Samuel Brady, Chelsey Hamm, and Kris Shaffer's Open Music Theory chapter on sight-singing and dictation recommends intermediate representations such as contour lines, dot grids, and rhythmic notation. We are using the same general pedagogical idea: solve onset positions, relative heights, and context separately before committing to full notation. The source describes instruction in common-practice notation; the present eight-bar exercise and its answer key are new.

Now add the bass alone. The sustained bass roots are C, F, G, C, A, D, G, C. If you hear the bass reliably, it helps locate the harmonic progression, but the bass alone does not prove a full chord quality. A note G in the bass could support G major, G minor, G seventh, or another structure. In our source data, the harmony label is an intended composition annotation. It is not inferred from the bass signal as a mathematical necessity. Ask which melody notes support each chord and which act as passing or color tones.

The third bar is an especially useful question. Against a G bass, the melody moves D, F, G, B. D and B are chord tones of G major; F is the minor seventh, making the intended G dominant-seventh color audible when the underlying spectrum and context permit. In the seventh bar, the melody moves D, G, B, D, and the specified harmony is simply G major. A listener might hear a similar dominant function across both bars, but their foreground notes differ. A transcription that writes G major in both measures has lost one harmonic detail; a transcription that writes G seventh in both has invented one.

What does a spectrogram add? It can show approximate energy concentration by frequency and time. A pitched sound's harmonics often create several horizontal bands. It would be wrong to count every band as a separate performed note. The spacing and persistence of bands, the spectral shape of the source, and the time window all matter. An onset may be visible as a broadband transient, while its fundamental is weak or masked. A display can support or challenge a hypothesis; it cannot automatically tell you which musical gesture the performer intended.

A short-time Fourier transform asks which frequency components are present over successive analysis windows. Choose a very long window and you may distinguish close steady frequencies better while smearing rapid attacks. Choose a shorter window and you gain onset localization at the expense of frequency discrimination. Julius Smith's Spectral Audio Signal Processing develops the underlying time-frequency framework. In Ardour, a region's spectral analysis and loudness-analysis displays can be useful as inspection tools, but do not confuse a spectrogram with a transcription engine. A visualization is evidence, not an answer key.

We should also ask what note durations really mean. In an acoustic recording, the perceived end of a note may be its decay, the arrival of the next note, or a sudden interruption. Our original score is deterministic: each melodic note lasts one beat, and each bass note lasts a bar. But a real guitar may ring across note changes, and a singer may connect notes without releasing all energy. A practical transcript can specify note-on and note-off events, articulation marks, or a simpler symbolic duration depending on the intended use. Every choice discards some acoustic detail.

Here is a reconstruction challenge. Use only the inferred melody notes and a standard tuning reference. Render them through a plain oscillator at ninety-six beats per minute. If your result has the correct pitches and durations but sounds emotionally flat, what did you omit? Possibly the dynamics, timbral evolution, articulations, microscopic deviations from the grid, or room sound. This is why a symbolic score is a model rather than a total copy of a performance. The gap is not necessarily a transcription error. It may be information the model was never designed to retain.

If you have DawDreamer, create a reproducible rendering graph using the note events and a deliberately uncomplicated sound source. Keep the tempo, sample rate, plugin state, and any MIDI settings in the run record. DawDreamer's official documentation describes processor graphs and offline rendering; that capability is distinct from a guarantee that every synthesizer or plugin behaves identically across versions. The accompanying standard-library renderer gives a dependency-free reference for the note timings, not a professional instrumental sound. It creates audio only when you run it; the repository overlay contains text, not recordings.

Import the original and reconstruction into Ardour. Place them at the same start position, confirm their playback levels, and loop the identical eight-bar span. If you compare only their signal waveforms, they may look unrelated because the sounds differ. If you compare musical events, they may agree closely. Move between listening and inspection, and write down which property you're testing. A precise comparison of pitches does not require identical timbres; an evaluation of articulation does.

Now make a composition decision. The original seventh bar climbed D, G, B, high D over a G bass. In the revised version, keep the same bass, same chord, same tempo, and all other bars unchanged. Replace the seventh bar's melody with D, F, G, B. The phrase no longer reaches the high D before returning to C. It also adds F, the seventh of the G harmony, even though the underlying harmonic label was G major. Here we must be precise: if the new F sounds structurally important, the effective sonority may suggest G seventh rather than a pure G triad. A reader should not be told that the harmonic content is unchanged merely because a chord-label field was left untouched.

We have therefore changed at least two musical properties with one four-note substitution: melodic range and harmonic color. Listen to the versions separately. Which makes the last bar feel more conclusive? Which creates more anticipation? Which more strongly recalls the F from bar three? These are musical judgments and may vary by listener. The exact numerical statement is simply that bar seven's events changed from D, G, B, D to D, F, G, B. The artistic interpretation remains a question for ears.

Could we isolate the two causes? Yes. Make another version that changes only the final high D to B, preserving the original first three notes. Or add F to the original bar while retaining high D by using a different rhythm. Compare these as separate treatments. When an agent says that revision B improved cadence, we can ask whether it improved the contour, the harmony, the rhythmic placement, or a combination. Controlled variants do not eliminate musical ambiguity, but they let us name what was changed.

The final workshop is to perform the process in reverse. Write the revised note list, then predict its sonic effect before listening. Render the audio, check that only the specified events changed, and import both candidates into the same Ardour session. Listen once with the bass, once with the melody only, and once after changing the timbre to a contrasting sound. If the difference seems important only for one instrument, that may be a meaningful arrangement discovery. If the difference disappears entirely, check that you were comparing aligned versions and did not accidentally normalize, mute, or replace the same source in both routes.

An end-to-end system should preserve evidence of every stage: input audio and its rights, source note-event description, rendering configuration, software versions, timing conventions, and the version selected after review. For an automatic-transcription agent, record confidence or alternative hypotheses instead of quietly converting uncertain pitches into facts. For a generative composer, record which notes were deliberately authored and which were inferred. For a listening review, separate measurable differences from preference. This is how a content pipeline can become repeatable without claiming that musical judgment has been automated.

Nothing in this procedure requires a fixed lecture length, and nothing requires audio to be shipped inside a text-only content pack. The musical example itself determines how long the explanation must be. The completed loop is the real goal: hear a sound, describe its events, use the description to change something intentional, hear the new sound, and learn what your notation did and did not predict. That is the point where analysis and composition become one activity.

<!-- END SPOKEN LECTURE -->

---

## Original eight-bar score and answer key (not spoken)

All measures 4/4, quarter-note tempo **96 BPM**. Four quarter-note melody events per bar; one whole-note root in the bass. The harmonic labels are **intended annotations**, not harmonies asserted to be completely voiced by the bass line.

| Bar | Harmony | Bass (whole) | Melody (four quarters) |
|---:|---|---|---|
| 1 | C | C3 | E4 G4 A4 G4 |
| 2 | F | F3 | A4 G4 F4 E4 |
| 3 | G7 | G3 | D4 F4 G4 B4 |
| 4 | C | C3 | C5 G4 E4 G4 |
| 5 | Am | A2 | A4 C5 B4 A4 |
| 6 | Dm | D3 | F4 A4 G4 F4 |
| 7 | G | G2 | D4 G4 B4 D5 |
| 8 | C | C3 | C5 G4 E4 C5 |

**Revision B** replaces bar 7's melody with `D4 F4 G4 B4`; everything else is unchanged. Because `F4` is not a triad tone of G major, the new vertical color may reasonably be heard as dominant seventh; record this rather than claiming the harmonic surface is identical. The companion JSON defines both variants and their isolated stems, and the renderer can generate WAV previews for transcription exercises.

**Workflow:** listen to the anonymous version first; record pulse, number of attacks, rough contour and bass motion; check source event list only afterward. In Ardour, compare the two versions aligned with the same mix and level. With DawDreamer, map the note events to any authorized original synthesizer and preserve the processor graph and environment.

### Claim-to-source reading map

| Topic | Link and locator | What the reference actually establishes |
|---|---|---|
| Limits and assumptions of polyphonic automatic transcription | [Benetos, Dixon, Giannoulis, Kirchhoff & Klapuri (2013), *Automatic music transcription: challenges and future directions*, *Journal of Intelligent Information Systems*, DOI 10.1007/s10844-013-0258-3, abstract/introduction](https://openaccess.city.ac.uk/id/eprint/2524/) | Review of transcription limitations, not proof of success on this original example. |
| Contour-first and rhythm-grid dictation | [Brady, Hamm & Shaffer, *The Basics of Sight-Singing and Dictation*, Open Music Theory, “Key Takeaways” and dictation strategies](https://viva.pressbooks.pub/openmusictheory/chapter/the-basics-of-sight-singing-and-dictation/) | Pedagogical approach in a Western-notation curriculum, not a universal rule. |
| Spectral models and time-frequency analysis | [Julius O. Smith, *Spectral Audio Signal Processing*, W3K, 2011; section on the short-time Fourier transform](https://www.dsprelated.com/freebooks/sasp/) | The book treats STFT and spectral analysis; the publisher entry is a pointer to the underlying text, not a citation for the invented composition. |
| Ardour region inspection and analysis | [Ardour Manual, Region Menu, “Loudness Analysis,” “Spectral Analysis,” and “Loop”](https://manual.ardour.org/ardours-interface/main-menu/Region-menu/) | Tool actions, not proof of exact pitch transcription. |
| DawDreamer graph/rendering workflow | [DawDreamer User Guide, “Overview” and “Basic Workflow”](https://github.com/DBraun/DawDreamer/blob/main/docs/user_guide/index.rst) | Software interface, not a measured listening outcome. |

All eight bars and revisions are **new original musical material**. Numerical event counts derive from the authored score, and subjective judgments are left to listening.
