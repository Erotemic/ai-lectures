# 034000 — Tuning, Temperament, and Intonation: When the Notes Refuse to Line Up

**Track:** Music Theory and Composition. **Audience:** composers, arrangers, sound designers, curious listeners. **Background:** pitches and frequency ratios; the calculations are explained from scratch. **Purpose:** understand why different tunings make different compromises, and how to design a controlled listening comparison without imposing one tuning system on every musical practice.

<!-- BEGIN SPOKEN LECTURE -->

# Tuning, Temperament, and Intonation: When the Notes Refuse to Line Up

Two instruments hold a chord. They agree on the notes as written, and neither player has made an obvious mistake. Yet the chord seems to shimmer. One musician adjusts the third of the chord down very slightly. The sound changes. Where did the extra roughness go? More importantly, what did the adjustment cost, and what will happen when the harmony moves to a new chord? Tuning is not simply a matter of finding a correct frequency. It is a choice about relationships among frequencies over time.

Begin with the simplest relation. A pure octave is a frequency ratio of two to one. If the lower oscillator runs at four hundred hertz, an octave above runs at eight hundred. The ratio is independent of the original frequency. A pure fifth corresponds to three to two; four hundred hertz becomes six hundred. A pure major third corresponds to five to four; four hundred becomes five hundred. The word pure here refers to an exact ratio under this numerical model, not to a musical judgment that the resulting interval is always preferable.

A harmonic tone is a sum of partials at approximate integer multiples of a fundamental, though real instruments vary in how closely their partials follow this rule. For the pair at four hundred and five hundred hertz, the fifth harmonic of the lower sound lies at two thousand hertz, and the fourth harmonic of the upper also lies there. If those partials have appreciable strength, they reinforce one another without a difference in frequency. Change the upper note and those two partials no longer coincide. We can calculate the new separation, but whether we hear it as beats, roughness, color, or almost nothing depends on the spectral envelopes, levels, registers, and listener.

For reference, much contemporary keyboard notation is implemented with twelve-tone equal temperament. Twelve equal semitone steps compose an octave. If the frequency ratio of a semitone is r, then multiplying by r twelve times must give two; r is the twelfth root of two. A rise of n equal-tempered semitones has frequency multiplier two raised to the power n over twelve. This gives a major third, four semitones, with ratio about one point two five nine nine two one. A pure five-to-four major third has ratio one point two five. The discrepancy looks small as a decimal. But it is a real tuning difference.

The University of New South Wales musical-acoustics explanations use this contrast directly: the equal-tempered major third is wider than the five-to-four interval, while the equal-tempered fifth lies much closer to a pure three-to-two fifth. Set the lower frequency to four hundred hertz. The pure major third is five hundred hertz. The equal-tempered major third is about five hundred three point nine seven hertz. If we render only simple sine tones, we should not confidently promise that everyone will hear a dramatic difference. With suitably chosen harmonic spectra, the upper sound's fourth partial moves from two thousand to approximately two thousand fifteen point nine hertz, while the lower sound's fifth partial remains at two thousand. The separation is about fifteen point nine hertz, creating a plausible perceptual contrast when those harmonics are audible.

Musicians often measure pitch differences in cents. One octave is divided logarithmically into twelve hundred cents. To measure a frequency ratio, take the base-two logarithm of that ratio and multiply by twelve hundred. A twelve-tone equal-tempered major third spans exactly four hundred cents. The five-to-four ratio spans approximately three hundred eighty-six point three one cents. Thus the equal-tempered third is about thirteen point six nine cents wider. A pure fifth spans about seven hundred one point nine six cents, while its equal-tempered counterpart spans seven hundred. These numbers are useful for comparing two conventions. They do not describe everyone's just-noticeable difference under all conditions.

Why not choose pure intervals everywhere? Because a tuning scheme must usually give pitches roles across many different chords. Tune a sequence of pure fifths, each one a factor of three halves. If twelve such fifths were to close exactly after seven octaves, the product of twelve copies of three halves would equal two to the seventh power. It does not. The ratio between them is five hundred thirty-one thousand four hundred forty-one divided by five hundred twenty-four thousand two hundred eighty-eight, approximately twenty-three point four six cents. This is the Pythagorean comma. No amount of careful arithmetic makes it vanish. A fixed set of twelve pitch classes cannot preserve every successive pure fifth and also close the circle of fifths.

Another discrepancy appears if we build a major third from four pure fifths and reduce the result into one octave. The resulting Pythagorean major third has ratio eighty-one to sixty-four. Compare that with five to four. Dividing one by the other gives eighty-one to eighty, the syntonic comma, about twenty-one point five one cents. The two ways of constructing a third disagree because the pure fifth and pure major-third ratios impose different constraints. The issue is not a bad tuning fork or careless performance. It is a property of the numerical system.

Temperaments distribute such discrepancies. Equal temperament spreads adjustments so that transposition by a semitone preserves the system's relative intervals. Various historical meantone and well-tempered solutions choose different compromises among thirds and fifths, and may make keys meaningfully different in color or usability. The details matter: a specific historical temperament is a set of actual tuning ratios or cent offsets, not just the label old tuning. Joseph Wolfe and collaborators at the University of New South Wales give musicians accessible explanations of how equal, just, and historical temperaments differ. William Sethares develops another central perspective: preferred relationships between tuning and timbre can depend on the spectrum of the sounds being combined. A scale designed for a harmonic string timbre need not behave the same way with a bell-like inharmonic timbre.

Do not turn that perspective into a blanket theorem that one spectrum mechanically determines a culture's music. Physical roughness is only part of musical consonance, and consonance itself has several meanings. Plomp and Levelt's 1965 paper, Tonal Consonance and Critical Bandwidth, is an important historical psychoacoustic study of interacting partials. Its existence and topic are well documented; a simplistic statement that it explains all consonance would overreach its scope. Learned familiarity, harmonic expectation, instrument technique, and musical context still matter.

We can make a modest controlled exercise. Render an original root tone at four hundred hertz and an upper tone at five hundred hertz. Then render the same root with the upper tone at five hundred three point nine seven hertz. Keep duration, levels, envelopes, and harmonic content the same. Record which upper tone you hear as smoother, if either, and describe the character of the difference without consulting the file names. Next repeat with pure sine tones rather than harmonic-rich tones. If the contrast changes, you have learned something about the role of spectrum. It would be a mistake to claim that one pair must be preferred, or that one trial establishes a universal psychophysical effect.

This also shows why a single note-grid is not enough to render an intonation experiment. A MIDI number or note name identifies a nominal pitch in a chosen system, but not necessarily the precise frequency performed. A piano sample may contain stretched tuning, and a singer may adapt pitch during a sustained chord. For reproducibility, specify hertz or cents offsets, the reference frequency, spectrum, amplitude envelope, and note timing. The companion's tuning exercise lists exact target frequencies; the original renderer can create identical sources with one altered interval. In Ardour, import those versions without independent loudness normalization so the controlled difference remains a change in pitch relation.

Now place the third in a harmonic progression. In one C-major chord, the note E can be tuned down relative to equal temperament to make a five-to-four third above C. When that E becomes the root of an E-minor chord, the desired pitches of the other chord members may impose a different set of ratios. If every new root is reconstructed from pure proportions, the absolute pitches of common tones may drift. This phenomenon is one reason adaptive just-intonation schemes must define how they choose reference notes, handle shared tones, and limit accumulated drift. It is not enough to advertise that every chord is pure without defining the transition between chords.

A fixed-pitch instrument and a flexible-pitch ensemble face different constraints. A piano normally has its pitches set before a performance, while a string quartet or unaccompanied choir can adjust notes in the moment. But even the flexible ensemble may choose not to eliminate every audible beat. The players might prioritize melodic motion, ensemble cohesion, an expressive inflection, or the harmonic identity of the phrase. In some contexts the beating itself is a deliberate color. Equal temperament is not a moral error, and pure ratios are not a complete account of musical meaning.

For music that uses pitch inflection as part of a melodic grammar, the limitation is deeper. A fixed grid of twelve notes, or even a fixed grid of twenty-four equally spaced notes, may fail to represent how a gesture moves through pitch. A slide, an ornament, a culturally specific tone inflection, or an intentionally varying interval is a trajectory, not just a frequency sampled once. Our synthetic comparison is therefore a lesson in a particular acoustic problem. It is not a model of all intonation traditions. Learning another tradition requires appropriate repertoire, specialist research, and contact with its sound and teaching methods.

A composer can use this knowledge without becoming a tuning-system historian. First ask what timbre you are using. A simple sine wave makes pitch ratios easy to specify but hides the interactions of partials. A saw-like wave adds harmonics and can reveal a different impression. A bell-like inharmonic sound may respond quite differently. Then ask whether the piece needs to modulate freely between keys, sustain a long stable triad, or feature a moving pitch gesture. Only then choose a tuning strategy. There is no single tuning that optimizes every goal.

For the engineer, calculations offer a useful validation layer. The renderer can check that an intended fifth is three halves within a specified tolerance, that note-on and note-off positions match the score, and that changing the upper note does not secretly change gain or duration. It cannot check whether the result feels expressive. For the listener, repeated comparisons can cultivate attention to a relationship that would otherwise pass unnoticed, but a perceptual result still depends on actual listening. Keep those forms of knowledge separate and let them inform each other.

The practical conclusion is that a note name is an instruction within a convention, not a complete physical description. Tuning is the act of choosing frequencies and how they move. Temperament is a set of compromises among possible relations. Intonation is the lived result in performance. When you hear two parts agree and yet change character as one bends a little, you are hearing the consequence of a choice that began as a ratio and ends as music.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and listening companion (not spoken)

The following numbers use **an authored numerical model** and may be independently recomputed; they are not measurements from listeners.

| Interval | Ratio | Cents | At 400 Hz root |
|---|---:|---:|---:|
| Octave | 2/1 | 1200.000 | 800 Hz |
| Just perfect fifth | 3/2 | 701.955 | 600 Hz |
| 12-TET perfect fifth | 2^(7/12) | 700 | about 599.323 Hz |
| Just major third | 5/4 | 386.314 | 500 Hz |
| 12-TET major third | 2^(4/12) | 400 | about 503.968 Hz |
| Syntonic comma | 81/80 | 21.506 | ratio only |
| Pythagorean comma | 531441/524288 | 23.460 | ratio only |

For an interval ratio `q`, cents = `1200 * log2(q)`. Note that these calculations presume harmonic **nominal** fundamentals; inharmonic instruments and performance tuning require additional specifications.

`examples/listening-lab-033000-036000.json` defines original pure/ET chord comparisons with controlled envelopes; `examples/render_listening_lab.py` renders those test files as generated WAVs. This material makes no claim that a listener will prefer one treatment.

### Claim-to-source reading map

| Claim | Source and locator | Qualification |
|---|---|---|
| Pure 5/4 thirds versus 12-TET thirds; harmonic interactions | [Joe Wolfe et al., UNSW Musical Acoustics, *Tuning* — “Chords and temperament”](https://phys.unsw.edu.au/jw/tuning.html) | University acoustics explanation; not a cross-cultural survey. |
| Semitone ratio and the practical compromise of temperaments | [UNSW Musical Acoustics FAQ, equal-tempered frequencies and harmonic fifth/third](https://phys.unsw.edu.au/jw/musFAQ.html) | Specific mathematical and instrument-tuning discussion. |
| Difference tones and a 400/500 Hz example | [UNSW Musical Acoustics, *Tartini tones and temperament*, embedded 400/500-Hz example](https://www.phys.unsw.edu.au/jw/tartini-temperament.html) | Illustrates possible sound examples; audibility depends on stimulus and listener. |
| Timbre and tuning interact | [William A. Sethares, *Tuning, Timbre, Spectrum, Scale*, 2nd ed., Springer 2005, chs. “The Science of Sound”, “Related Spectra and Scales”, “Adaptive Tunings”](https://link.springer.com/book/10.1007/b138848) | Publisher description and chapter list accessible; detailed arguments require consulting book itself. |
| Primary psychoacoustic work on tonal consonance | [Reinier Plomp and Willem Levelt, *Tonal consonance and critical bandwidth*, *JASA* 38(4):548–560 (1965), DOI 10.1121/1.1909741](https://pubmed.ncbi.nlm.nih.gov/5831012/) | Bibliographic record available; no public abstract there. The lecture does not attribute a specific numerical finding to the paper. |

**Historical scope:** “Pure,” “just,” and “equal” here name precisely described tuning choices. They should not be used to rank communities or to attribute techniques to a culture without specialist evidence.
