# 039000 — The Fugue as a Musical Argument: Entries, Episodes, Inversion, and Stretto

**Track:** Music Theory and Composition. **Audience:** listeners, composers, programmers making music-generating tools, and anyone trying to understand what makes a texture genuinely contrapuntal. **Background:** rhythm and tonal relationships, melodic imitation, canon, and motivic development; these are introduced again wherever necessary. **Purpose:** learn to hear and construct a fugue as an evolving relationship among independent musical voices, not a checklist of contrapuntal devices.

<!-- BEGIN SPOKEN LECTURE -->

# The Fugue as a Musical Argument

Imagine hearing a melody alone. It has a recognizable opening rhythm, a leap, a little turn, and an arrival. A second voice enters, not with a contrasting reply, but with the melody itself shifted to another pitch level. The first voice refuses to fall silent. It continues with new notes that fit around the incoming melody. A third voice takes up the theme while both earlier voices remain active. Later the theme disappears from the surface, yet fragments of it travel from register to register. Near the end, one statement starts before the last statement finishes. The listeners can hear that the same idea has returned, but now the voices compete for time.

This is a useful first image of a fugue: **a musical idea changing its meaning as different independent voices take responsibility for it**. The word *fugue* does not promise one universal architecture. It names a contrapuntal practice in which a characteristic subject and its later statements play a central organizing role. In the tonal fugues of the High Baroque, the first section commonly establishes those roles through an exposition. Subsequent music can alternate entries with passages that avoid a complete subject, sometimes making the subject harder to recognize and sometimes presenting it with extraordinary clarity. None of this means that a fugue is a mechanical exercise in which the composer simply duplicates a line at a fixed delay.

We will build a miniature in three voices. Our complete classroom work lasts twenty-eight four-beat bars, with a two-bar theme. The work and all its note events are original. It is an analytical study of the concepts, not a reconstruction of a Bach score or proof that it satisfies all eighteenth-century stylistic rules. The accompanying source files can render individual experiments as well as the complete miniature. That lets us make precise claims about what the generated notes actually do and distinguish them from judgments about how convincing the music sounds.

## How a fugue differs from a round, a canon, and a dialogue

Call-and-response alternates recognizable gestures or performing roles. The answer may deliberately differ from the call. A canon imposes a more exact imitative rule: a following voice reproduces a leader after some delay, sometimes with a pitch or rhythmic transformation. A simple round keeps that rule active across a repeating cycle. A fugue often uses exact or adapted imitation, but **a fugue is not merely a canon played for longer**. The answering voice may alter intervals, the first voice may continue with different counterpoint, and after the opening each voice can change its role independently. The subject may recur in other keys and registers, and there can be substantial passages without any complete statement.

The University of Kansas counterpoint competency materials list subject, answer, countersubject, episode, stretto, and invertible counterpoint as distinct ideas. The list is a vocabulary, not a mandatory inventory: not every fugue includes a recognizable countersubject, and not every fugue includes stretto. Open Music Theory likewise treats a fugue's exposition as an imitative process whose practical choices depend on the subject and the surrounding harmony. The same terminology can help us analyze a piece without requiring every piece of layered music to be a fugue.

Why does the distinction matter for composition agents? An instruction such as 'have instrument B repeat instrument A after two bars' may produce a canon-like passage. It does not automatically make the two lines harmonically compatible, give them independent continuation, or create a coherent large-scale progression. Conversely, a successful fugue is not necessarily valuable because an agent checked every textbook label. What matters is the relationship between recurrence, independent voice-leading, harmonic motion, and the timing of the entries.

## The subject: how little identity can a melody carry?

Our original two-bar subject begins in C major. Count four steady beats per bar. In the first bar it sings C, then G, then A for half a beat, G for half a beat, and E for one beat. In the second bar it sings F, then E for half a beat, D for half a beat, G, and finally C. All pitches here are in the octave around middle C, unless we explicitly say otherwise. The full score gives the exact durations and registers. Sing it before listening to the synthesizer. Try to remember two separate features: the opening leap from C to G, and the faster A–G figure. You may remember the opening leap more readily than the ending. That is a hypothesis to test with listening, not a laboratory finding.

A good subject gives the listener something to recognize after transposition and interruption. But 'good' is contextual. A short rhythmic signature may suffice in dense music. A longer, carefully differentiated subject might be needed when the entries are far apart. In the High Baroque exposition account in Open Music Theory, subjects are discussed in terms of head motive, continuation, and cadence, and also by stylistic character. That description is a way to ask where a subject gets its identity; it is not a universal recipe that every fugue must literally follow.

For our subject, the leap and fast turn form the head. The descent and return to C help signal completion. We should not confuse an audible landing on a tonic pitch with a demonstrated perfect authentic cadence. That latter label requires harmonic and voice-leading information, not just a melodic final note. Our miniature is deliberately designed so that the theme can be recognized under several simple transpositions. It leaves the stricter historical problem of tonal closure for a later, more demanding compositional exercise.

## A real answer, and why a tonal answer is not a mistake

After the first voice, another often states the theme near the dominant. In C major, the dominant pitch is G. There is a crucial distinction between copying the exact interval pattern and adapting it to support the tonal situation. A **real answer is an interval-preserving transposition** of the subject. If we raise every note of our C subject by a perfect fifth, its opening C–G becomes G–D. The next fast notes are E and D, and the answering phrase eventually arrives on G. We can verify that every pitch moves seven semitones and every duration remains the same.

But that opening G–D can immediately stress the dominant of G rather than the relationship between G and C that the exposition may want to preserve. A **tonal answer adjusts selected intervals rather than reproducing every one exactly**. For our teaching comparison, we begin on G and redirect the next pitch to C, then form a recognizably related line. The result preserves the head's rhetorical leap while giving tonic C a more immediate presence. Our particular adapted answer is an editorial construction, not a transcription of one of Bach's answers. There are multiple musically defensible solutions, and the fact that a note has been altered does not, by itself, prove that the resulting harmony is sound.

Open Music Theory describes the tonal-answer choice as especially relevant when a subject strongly emphasizes tonic–dominant relations or moves between keys. The University of Puget Sound's *Fugue Analysis* works through the first exposition of Bach's C-minor fugue from Book One of the *Well-Tempered Clavier*, BWV 847, noting its tonal answer and two recurring countersubjects. Those are claims about that particular documented score, not claims that our newly written example is historically identical.

Listen to three clips: subject alone; real answer alone; adapted tonal answer alone. At first, ignore timbre. Which retains the exact interval sequence? Which makes the opening relation to C more plausible to your ear? Now play the clip again with an unobtrusive low C beneath it. You may hear the interpretation change. We have not isolated 'the correct answer' by a blind test; we have exposed the musical decisions the answer forces you to make.

## The exposition: identity passes between voices

The opening exposition of a conventional three-voice tonal fugue introduces each voice in turn with the subject or answer. We can hear a well-documented model in BWV 847. Open Music Theory's exposition chapter identifies the exposition in measures one through eight, the alternation among three entries, the tonal answer, and two countersubjects; it also observes how an ensuing episode uses sequential material derived from the subject. The page supplies score-based analysis and not just a verbal definition. It is a useful external counterweight to our synthetic demonstration.

In our miniature the alto begins alone with the subject in C. Two bars later the soprano introduces the tonal answer beginning on G. The alto does not stop: it moves into accompanying material. After another two bars, the bass states the original subject an octave lower while upper voices can continue. The phrase 'three-voice fugue' describes three continuing musical lines, **not three audio tracks**. A single keyboard instrument can play three voices. Several layered instrument tracks might still amount to one perceptual line if they all double the same notes.

Mark the entry times on a grid: bar one for the alto subject, bar three for the soprano answer, bar five for the bass subject. You now know a structural fact about the opening without hearing a sound. But to hear three parts rather than a wash, the entries must be salient. Make each entry audible by rendering the other voices more quietly, then gradually restore them to their intended levels. An arranger might change timbres or registers; a keyboard player might alter articulation. Those are ways of exposing the structure, not substitutes for composing compatible lines.

A second lesson is that an exposition can include a link or codetta between entries. Such a link can smooth a harmonic transition or adjust the timing of the next entry. Its presence is not compulsory. Our compact opening has no intervening link: entries begin every eight beats. That simplification makes the events easy to inspect and keeps our first analytical task focused on imitation.

## The countersubject, and the more general problem of invertible counterpoint

When the first voice continues under the answer, its continuation may become a countersubject: a recognizable line that accompanies further subject entries. If an accompaniment does not recur as a stable pattern, calling it free counterpoint may be more accurate. The University of Puget Sound analysis explicitly distinguishes recurring countersubjects from other contrapuntal material. This matters because a fugue is not required to keep every accompaniment fixed forever. Continuous musical invention remains possible.

To understand why composers care about invertible counterpoint, write two melodies that sound together in one register arrangement, then exchange which lies above the other. The musical goal is not merely to avoid a software collision. If you want both arrangements to behave as coherent tonal counterpoint, the vertical intervals and the approaches to dissonance must survive the exchange. Some thirds become sixths at octave inversion. A perfect fifth, inverted at the octave, produces a perfect fourth; in some contrapuntal styles that can create a problematic consonance-to-dissonance change. Invertibility is therefore an actual design constraint, not just an instruction to swap MIDI track labels.

We provide a specific two-bar pair. The upper line states our subject an octave higher. The lower line moves on its own rhythmic pattern, mostly forming thirds or sixths at structurally prominent instants. The companion score then moves the subject down an octave and the other line up an octave without changing either line's internal notes or timings. The validator checks the exact swap and the selected structural intervals. It does **not** certify strict species counterpoint or a seamless Bach-style realization. The model intentionally includes a weak-position passing dissonance whose treatment must be judged in context, and the sound generator cannot tell us whether a performer would phrase the line convincingly.

David Rothfarb's University of California, Santa Barbara counterpoint course offers separate discussions and models for invertible counterpoint and the fugue. That pedagogical separation is useful: the two techniques overlap, but the contrapuntal feasibility of swapping voices is not the whole of fugue form. A countersubject that works under an answer may need adaptation when a subject appears in a very different tonal or registral situation. In our complete miniature, several entry accompaniments are freer than our fixed invertible pair. We identify them as such rather than claiming every continuation is one immutable countersubject.

## Episodes: keeping the argument alive when the theme is absent

After the first entries, the composer can let the full subject disappear. That absence need not halt development. In the score-based BWV 847 analysis, the music following the exposition uses material related to the subject in sequential motion. Episodes often derive their substance from small motives, including the head of the subject or a countersubject; they are not simply arbitrary filler between proper fugue sections. Still, a composer can make many different episode choices, and the amount of motivic relation varies among works.

Take our opening head: C, G, A, G, E. Remove the rest of the subject. Repeat just that fragment from new pitch levels and distribute the entries between voices. Because we removed the second bar, the complete theme is absent even though its opening identity remains audible. Now ask two separate questions. Where does the sequence go harmonically? And how long can it continue before the listener wishes for a fuller return? The first question has an analytical answer in terms of notes and harmonies; the second requires listening and musical judgment.

Our miniature has one short episode immediately after the exposition and another, longer, sequenced passage in its middle. The second changes more than just register: two voices pass a fragment back and forth while a lower line helps maintain continuity. For clarity the supplied rendering uses a simple, fixed-tempo harmonic oscillator. It cannot demonstrate the historical touch or expressive nuance of an organist, pianist, or small ensemble. It can demonstrate which notes belong to which fragment, where they enter, and whether the claimed complete-subject absence is true.

You should not equate the absence of a complete subject with the absence of compositional identity. A fragment may be the most memorable part of a theme. A sequence can be recognized as development precisely because it is both familiar and changed. Compare an episode built from the subject head with one made from an unrelated figure. A composer can choose either, but the two choices create different relationships to the listener's memory.

## Stretto: when entries stop politely taking turns

Now we can change the temporal relationship between the voices. In the original exposition, the next subject or answer begins after the previous full two-bar statement has ended. In a stretto, **the next subject entry begins before the previous statement is complete**. The word describes overlap among subject statements, not simply many notes sounding at the same time. Nor does it mean that any piece with overlapping melodies is a fugue. We must identify full or recognizable subject entries and verify their relative timing.

Our two-bar subject lasts eight beats. In a separate stretto study, the soprano begins at beat zero, and the alto begins at beat four. For the four beats between those points and the end of the first statement, two subject statements occur simultaneously. The first ends at beat eight; the second ends at beat twelve. The companion validator checks this timing. It does not say the texture is necessarily more exciting or historically idiomatic. We can produce a second version in which the following entry waits until beat eight, then compare them at the same loudness.

A composer can increase intensity through a stretto because recognizable material competes for the listener's attention while the musical space gets denser. But the effect is contingent. A slow, soft stretto might sound contemplative. An early overlap in an already crowded texture might make the subject harder to hear. Stretto is an option for shaping arrival and compression, not a mandatory final-chapter event. This is particularly important for agents that would otherwise place a stretto in every fugue-like piece simply because the technique has a famous name.

The larger miniature places a denser series of entries later: one voice starts a subject, a second enters one bar afterward, and a third begins another bar after that. The precise score distinguishes this from an accidental overlap of note tails. A composer still has to examine the resulting voice leading. The fact that the software verifies entry offsets is a necessary but very incomplete test of good counterpoint.

## Form is more than the sum of entries

We can now assemble a broad trajectory. Bars one through six introduce the voices. Bars seven and eight develop the head without the complete subject. Bars nine through twelve present further entries in changed registers. Bars thirteen through sixteen extend the episodic sequence. Bars seventeen through twenty concentrate subject entries into a stretto-like passage. Bars twenty-one through twenty-four work with shortened fragments and changing density. In bars twenty-five and twenty-six, the subject returns near home. Bars twenty-seven and twenty-eight establish a closing dominant-to-tonic bass motion.

This plan explains the classroom miniature's itinerary, not its quality. A final dominant-to-tonic bass motion does not by itself establish a perfectly written eighteenth-century cadence. And a plan with clear sections need not guarantee that the transitions between those sections feel inevitable. The listener should ask whether each entry changes the situation: does it return in a new register, alter the balance of voices, resolve a previous ambiguity, or change our expectation of what follows?

A useful connection comes from William Renwick's research on Bach's *Well-Tempered Clavier*. Renwick's 1987 dissertation argues that a fugue subject's voice-leading structure is related to recurring exposition patterns; its abstract makes that argument explicit. He is not claiming that the mere presence of an answer supplies structural coherence. He is interested in how imitative obligations interact with tonal voice-leading. We should treat that as a scholarly analytical thesis, not as proof that every fugue follows one generative algorithm. His 1991 *Music Theory Spectrum* article develops structural patterns in subjects and expositions, but the accessible article record provides an abstract rather than unrestricted full text. We should not claim to have inspected every page of that article on the strength of its abstract.

This helps explain why a fugal passage needs revision even when every entry is recognizable. Suppose the subject enters on a pitch the harmony has not prepared. Suppose a very low voice reaches beyond the selected instrument's practical range. Suppose each new entry repeats an accompaniment so literally that the music feels like a loop. These are different problems: one concerns tonal continuity, another instrumentation, a third formal development. No single score-level validator can solve them all.

## Reading a historical fugue without pretending we wrote it

The *Well-Tempered Clavier*, Book One, contains twenty-four prelude-and-fugue pairs in major and minor keys. Bach's C-minor fugue, BWV 847, provides an especially accessible three-voice case for identifying a tonal answer, countersubjects, a bridge, and an episode. The Open Music Theory exposition chapter identifies those events by measure. The International Music Score Library Project hosts bibliographic entries and public-domain source scores for Book One; those original documents should be kept distinct from modern pedagogical annotations and from any recorded interpretation of the work.

When you work from the historical score, write down an entry map before assigning emotional labels. Mark the start of each subject and answer; record the voice, key area, and register. Locate places where the complete subject is absent but a fragment remains. Then compare your map with a credible scholarly analysis. If the two disagree, first check whether you are counting a partial entry as a full one, and whether your score and the scholar's score have the same bar numbering. Only then ask whether a larger disagreement is interpretive.

Nothing in this method requires you to treat Bach as the origin of imitation. Fugal techniques have a history before and after the High Baroque, and their meanings change across repertories. A classroom discussion of the eighteenth-century tonal fugue should not silently become a global taxonomy for all polyphonic music. Our reference list focuses on the historical tradition we are analyzing, and it makes that limitation explicit. Broader contrapuntal practices deserve their own specialist sources and listening traditions.

## A listening and composition laboratory

We will compare several perspectives on the same original subject. Hear the bare melody. Hear the exact real answer against the adapted tonal answer. Hear the two invertible contrapuntal arrangements. Hear a successive three-voice exposition. Hear a sequence built from the subject's head while the full subject is absent. Finally hear the overlapped entries and the twenty-eight-bar composite. The accompanying exercises are not offered as famous compositions or as acoustically realistic samples of period instruments. They are controlled constructions whose note events, octave placements, and entrances you can inspect.

Use DawDreamer to replace the reference oscillators with chosen instrument or synthesizer plugins and render the stems offline. Save the plugin versions, parameter states, tempo, and source-event file if you want to reproduce an experiment. Import the resulting stems into Ardour. Mute all but one voice, then restore them one by one. Try moving an answer to a different instrument without touching its notes. Try reducing the episode's density while preserving its sequence. In a separate revision, make the stretto enter one beat later. You may find that the first rendering is more intelligible and the second more urgent, or vice versa. Those are hypotheses to test by listening, not properties established by the JSON validator.

For a stronger exercise, avoid beginning with a formula for the whole fugue. Start with a subject you actually want to hear again. Write its answer. Test the simultaneous counterpoint before constructing the rest of the exposition. Decide what the episode will *do*—move to a new harmonic area, increase energy, reduce density, or prepare a later register. Revisit the subject after enough change that its return matters. Only introduce a stretto if overlap serves a purpose. Then check the piece for its own musical priorities as well as for contrapuntal mistakes.

When evaluating an AI composition, I would rather ask five concrete questions than count devices. Can we recognize the recurring subject? Can we follow the other voices as genuine musical lines? Does each entry serve a new structural function? Is the harmony and register compatible with the intended ensemble? Does the music justify the moment when the subject returns, overlaps, or disappears? A piece can answer those questions convincingly without presenting the most elaborate possible fugue. A piece can also exhibit every named technique and still fail to communicate.

The deepest lesson is not a fixed formal recipe. **Independent voices create musical argument when their shared material is recognizable, their differences matter, and their encounters change the direction of the piece.** That is what distinguishes meaningful imitative development from merely repeating one melody on several tracks.

<!-- END SPOKEN LECTURE -->

---

## Analytical companion (not spoken)

### Scope and definitions

This lesson analyzes **tonal fugue and fugal writing in the European eighteenth-century pedagogical tradition**. Fugue conventions are not universal requirements for polyphony in other traditions. A *fugue* names a compositional process/genre rather than one fixed scheme. *Canon* denotes a stricter imitation rule. *Subject*, *answer*, *countersubject*, *free counterpoint*, *episode*, *stretto*, and *exposition* are defined by their roles in the analyzed score, not by arbitrary track labels.

### Original subject and two answers

At 104 beats/minute, in 4/4; `at`/`dur` in quarter-note beats. Register uses scientific pitch notation (C4 = middle C). Full score: [`examples/fugue-lab-039000.json`](examples/fugue-lab-039000.json).

| Bar | Subject (alto) | Real answer +7 semitones | Teaching tonal-answer adaptation |
| --- | --- | --- | --- |
| 1 | C4(1), G4(1), A4(.5), G4(.5), E4(1) | G4(1), D5(1), E5(.5), D5(.5), B4(1) | G4(1), C5(1), D5(.5), C5(.5), B4(1) |
| 2 | F4(1), E4(.5), D4(.5), G4(1), C4(1) | C5(1), B4(.5), A4(.5), D5(1), G4(1) | C5(1), B4(.5), A4(.5), D5(1), G4(1) |

The adapted answer is a **didactic choice**: it shows how initial tonic–dominant relations can be redirected but is not asserted to be the uniquely correct eighteenth-century tonal answer. Verify actual harmonic function through bass/voice-leading analysis before treating the demonstration as a model to imitate literally.

### Event-checked form of the original miniature

| Bars | Events | Question to ask |
| --- | --- | --- |
| 1–2 | Alto subject in C | What defines the head motive? |
| 3–4 | Soprano tonal answer, continuing alto | Can both voices remain identifiable? |
| 5–6 | Bass subject, upper counterlines | Is the identity maintained in a lower octave? |
| 7–8 | Episode 1, head fragments without full theme | Does fragmentation preserve memory? |
| 9–12 | Soprano subject, alto answer | How does register alter hierarchy? |
| 13–16 | Episode 2, longer sequential passage | Does continuation justify its space? |
| 17–20 | Stretto-like entries at beats 64, 68, 72 | Which full subject statements overlap? |
| 21–24 | Fragment development | What makes the subsequent return feel prepared? |
| 25–26 | Alto tonic subject, independent upper voice | Does the subject's return change the argument? |
| 27–28 | Cadential bass G2→C3 and upper resolution | Is the closure persuasive in the actual harmonic texture? |

The program checks structural facts (source pitch sequences, exact transpositions, key entry times, overlap, bar grid, and that the episodes do not silently contain full declared subject entries). It does not certify consonance on every beat, tonal modulation, playability, or artistic success.

### Claim-to-source reading map

**Primary score and source history.** [J. S. Bach, *Das wohltemperierte Klavier I*, BWV 846–869, IMSLP catalog/source scans](https://imslp.org/wiki/Well-Tempered_Clavier%2C_Book_1%2C_BWV_846-869_%28Bach%2C_Johann_Sebastian%29): list of twenty-four prelude-and-fugue pairs and links to manuscript copies/early prints. The source scores are a different evidence type from a modern annotated analysis. Specific modern score-reading example: BWV 847, Book I, C minor. This lecture does not reproduce that score or any copyrighted recording.

**Exposition and tonal answer.** [*Open Music Theory*, “High Baroque Fugal Exposition”](https://viva.pressbooks.pub/openmusictheory/chapter/high-baroque-fugal-exposition/), sections **Subject**, **Answer**, **Countersubject**, **Exposition**, and the annotated **BWV 847, mm. 1–9** illustration. It explicitly distinguishes real versus tonal answers, discusses altered tonic–dominant opening gestures, and marks the BWV 847 exposition (mm. 1–8), the intervening link, its two countersubjects, and an episode beginning in m. 9. Teaching scope is Western Baroque practice.

**Analysis of the historical work.** [Robert Hutchinson, *Music Theory for the 21st-Century Classroom*, “Fugue Analysis”](https://musictheory.pugetsound.edu/mt21c/FugueAnalysis.html), section **30.8**, Figure **30.8.1** and text following. Distinguishes countersubject from free counterpoint; maps the opening of BWV 847. This is Hutchinson's modern pedagogical analysis of Bach, not a primary source score; the lecture's paraphrases are not quotations.

**Invertible counterpoint and fugue in pedagogy.** [David Rothfarb, University of California Santa Barbara, Music 103 index](https://rothfarb.faculty.music.ucsb.edu/courses/103/index.html), headings **Invertible Counterpoint** and **Fugue**, with linked teaching notes and model expositions. [University of Kansas School of Music, “Counterpoint”](https://music.ku.edu/counterpoint), **Terminology** and **Fugues — Sample Questions**. These establish distinction and pedagogical scope; neither validates this lecture's invented note data.

**Composition exercise.** [University of Minnesota Libraries Publishing, “Composing a Fugue”](https://open.lib.umn.edu/musiccomposition/chapter/composing-a-fugue/), **The Exposition** and **Real/Tonal Answer** sections; an accessible search listing confirms the definitions, but the full page was inaccessible from this research environment. Use the freely accessible Open Music Theory exposition chapter above as the main corroborating source.

**Voice-leading research.** [William J. M. Renwick (1987), “Voice-Leading Patterns in the Fugal Expositions of J. S. Bach's Well-Tempered Clavier,” CUNY dissertation](https://academicworks.cuny.edu/gc_etds/2434/), **Abstract** (claims about patterns, imitative obligations, tonal voice-leading). [Renwick (1991), “Structural Patterns in Fugue Subjects and Fugal Expositions,” *Music Theory Spectrum* 13(2), 197–218, DOI 10.2307/745898](https://doi.org/10.2307/745898), **publisher abstract only** in this research pass. Do not cite an inaccessible page or a specific uninspected proof as though read.

**Study source.** `examples/fugue-lab-039000.json` is original teaching material. It is not the score of Bach BWV 847, Renwick's analytic examples, or any other cited work. All renderer output derives from these authored note events.

### How to use the source-only listening lab

```bash
python content/music-theory/examples/render_fugue_039000.py --check
python content/music-theory/examples/render_fugue_039000.py --output-dir /tmp/fugue-039000 --anonymous
```

The renderer uses Python's standard library and the pack's existing neutral PCM synthesizer. It writes optional WAVs only to the selected local output directory, never to the content overlay. Compare the generated studies by following the score; then optionally replace the synthetic instruments through a documented DawDreamer graph and inspect the rendered stems in Ardour. Musical quality, historical playing style and perceptual effects require listening, and the automatic checks do not purport to judge them.
