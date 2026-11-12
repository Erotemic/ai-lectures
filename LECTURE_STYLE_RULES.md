# Lecture style rules

These rules collect preferences Jon has directly expressed while reviewing the
lectures. They are not a general style guide or a place for new agent
suggestions. Technical mechanics belong in the
[authoring guide](dkvis/learning/README.md) and the
[slide implementation notes](briefs/slide-authoring.md).

The rules were consolidated on 12 November 2026. Earlier versions had grown
through repeated audits and, applied together, produced uniform, cautious
lectures. Fewer, clearer rules are intended. When a rule here conflicts with
good mathematical teaching, raise the conflict rather than writing around it.

Sections 1–7 govern the spoken mathematics tracks (G2 and G3). Sections 8–10
cover visual versions, history lectures and track bookkeeping.

## 1. What the mathematics lectures are for (12 November 2026)

The G2 and G3 audio tracks have two purposes:

1. help a serious reader understand the Davis–Kahan theory as formalized in the
   journal paper: its definitions, hypotheses, constructions and proofs,
   well enough to read the paper and its proofs with confidence; and
2. serve as an evergreen, careful course in the operator theory those results
   depend on. The course is meant to be more than an introduction.

The lectures are **text-to-speech first**. They must not rely on visuals. A
listener who is paying attention and working to internalize the ideas should
come away with a usable mental model *and* with the details: exact
definitions, real hypotheses, the steps of the proofs, and the examples that
show why each hypothesis is there. At minimum, a lecture should make the
corresponding written mathematics noticeably easier to read afterwards.

The lectures are mathematical content. They do not refer to the repositories in
which the formalization was developed or to the lineage of its code. When
visual versions are made, Lean receives real treatment there, as independently
checkable grounding for the statements and their dependencies (Section 8).

Revise slowly, one lecture at a time. A lecture that has been rethought from the
mathematics is worth more than many lightly edited ones.

## 2. Length

**There is no duration target.** A lecture is as long as it needs to be to
convey its mathematics reliably and correctly. Ten minutes is generally too
short for this material; longer lectures are welcome. Do not compress a proof,
drop a hypothesis, skip a calculation or omit an example to save time.

Length must come from substance: a fuller argument, a second example, a slower
pass through a hard inference. Do not pad with recaps, generic transitions or
restatements. Split a recording only when it contains genuinely separate
subjects, not to meet a length.

## 3. Teaching method

The aim is **to develop understanding at the speed at which a listener can
build a mental model**. A reader can pause and look back at symbols; a listener
follows the argument in real time. A sequence of correct statements is not by
itself a teachable lecture.

**Build the explanation before the abstraction.** Plan a learning path, not a
theorem outline:

1. Start from a problem or observation the audience can already reason about,
   and give a concrete reason to care. Do not open with an inventory of named
   maps and spaces.
2. Work a small, audible example. When it fails or leaves a question, make the
   obstacle explicit; that obstacle motivates the next definition.
3. Introduce the general construction once the listener has a referent for it.
   Return to the example to interpret the definition and to show which
   features were special to the example.
4. Before a substantial proof, say what it concludes and the idea of the
   argument. At each key step, say what is now established and what remains.
   Slow down at domain restrictions, changes of space, and implications that
   do not reverse.
5. Consolidate with a second use of the example, a meaningful failure case, or
   a calculation the listener can reconstruct. End with the actual result and
   its important limitation.

This is a reasoning pattern, not a section template. Sometimes the theorem is
the right opening; sometimes a physical model or an immediate calculation is.
What is required is an intelligible thread of *why this step comes next*.

> “Start with the high level true statements we are going to learn.”
> “It turns out that <true statement>, let's think about why.”

Early on, state the true conclusions the lecture will reach, in accessible
terms, then use them as the roadmap. Do not withhold the destination to create
suspense.

> “Good intros / motivations / a small bit of historical context / summaries.”
> “The important information is very abrupt, and we are failing to establish a coherent thread that ties the entire lecture together.”

Give the concept's motivation and a little historical context where it helps.
Write the lecture as one connected explanation: carry the current question and
what has been established into each new section, give important information a
lead-in, and explain its consequence before moving on. Generic transition
phrases do not supply this thread. End by returning to the opening claims so
the listener can see what has now been justified.

**Control the number of active objects.** Give a new map's input, output and
role before naming the next one. When a new space, projection, residual,
spectral cluster, gap or domain appears, place it relative to the objects
already in use. If a theorem needs several constructions, preview their jobs in
words before giving the notation.

**Explain notation and jargon at the point of use.**

> “It's the jargon and shorthand for concepts viewers are not familiar with.”
> “It's not enough to just say what it is ... the context ... is primed.”

Describe an operation in plain language before naming it, for example show how
small coefficients describe a vector in the big space before calling it a
“lift”. Unpack shorthand such as “normal-to-normal action” into which input and
output components are meant. Replace “by symmetry” with the particular symmetry
and why it gives the relation, unless that step is already familiar.

**Spoken proof pacing.** At a difficult inference, give a concrete picture,
perform one operation, and say what it established before starting the next.
Keep a projection, its complement, a displacement operator and its Gram
operator distinct in the narration; their symbols look alike, but their roles
differ. Prefer short interpretive sentences to several identities recited in
one breath.

**Make calculations speakable.** For a matrix with many entries, first say what
it *does*: which subspace it preserves, which direction moves, what property is
being tested. Work one representative entry or vector aloud and explain how the
rest follow; put the full array in the companion. State radicals and eigenvalue
lists in intelligible chunks, with approximations supporting the exact values.

**Work from the mathematics, not from the existing paragraphs.** In a deep
revision, first write down the definitions, exact hypotheses, proof steps,
examples and conclusions. Design the teaching order independently of the old
draft and rewrite the spoken region to match. Keep the mathematical coverage,
exact conditions and counterexamples, or record a deliberate curriculum change.

## 4. Mathematical precision

**State hypotheses in content, not by pointer.** A theorem's hypotheses are
spoken as conditions the listener can check: “every eigenvalue of A zero lies
in the interval from a to b, and every eigenvalue of Lambda one lies at least
delta outside it”, rather than “under one of the supported separation
conditions” or “assuming the relevant Sylvester theorem applies”. If an exact
condition is too intricate to speak, explain its shape and why it is needed,
and give the precise form in the companion.

**Mathematical qualifications stay.** Say what was proved, what remains open,
and why the hypotheses matter. Distinguish a theorem from an unsupported
extension, and an explicit counterexample from a failed proof. Retain
finite/infinite-dimensional, real/complex, domain, operator-ideal and
spectral-gap constraints. For perturbation results, keep apart the source and
target subspaces, spectral clusters, residual, gap hypothesis, domain
conditions, angle branch, scalar field and norm class. A statement about squared
displacement does not by itself give the unsquared one.

**Use the paper's notation.** Lectures that prepare the reader for the
Davis–Kahan paper use its names, spoken naturally: A, A hat, E zero, A zero,
F zero, F one, Lambda one, R, delta, Theta zero. See the canonical notation in
[AGENTS.md](AGENTS.md#canonical-sine-theta-notation). Where another source's
notation is genuinely the subject, say so and translate.

> “We don't need to explain the difference between transpose and conjugate transpose ... every time.”

State the scalar field and adjoint convention once per lecture and use it.
Return to the real/complex distinction only where an argument depends on it.

**Numerical examples carry their data.** A reused example states its matrix,
vectors, parameters, boundary conditions and assumptions in the present
recording, and recomputes at least one defining step rather than quoting a
result.

## 5. Continuity across the course (12 November 2026)

Some chronology is acceptable. The course has a real order, and a careful
course may build on itself:

- A lecture may say that a fact has been established or will be developed,
  such as “we have seen that a bounded linear map is continuous” or “this
  becomes essential once operators are unbounded”, provided the fact itself is
  stated.
- Running examples may recur across lectures with consistent names and numbers.
  Each recording restates the data it uses.
- Course-level orientation (where a topic sits, why it is coming now) is fine
  in moderation.

Limits that remain:

- Do not let a callback stand in for mathematics. If the argument uses a
  hypothesis, matrix, computation or theorem, state it in this recording.
  Listeners skip around, and must be able to follow with the stated
  prerequisites.
- Do not refer to episodes by number or by production title (“lecture
  seventy-two”, “our pinching unit”).
- End on what this lecture established, not on an announcement of the next
  one.

G2 begins from basic linear algebra and calculus; later lectures assume the
material listed as their prerequisites. G3 has its own, more advanced baseline.
Do not flatten the two tracks into one prerequisite level, and do not re-teach a
whole dependency chain in every recording.

## 6. Voice

The spoken region should sound like a mathematician developing an argument,
not like an assistant reporting on its work.

**Keep production out of the narration.** Leave prompting, authoring
instructions, curriculum planning, provenance, repository details,
proof-assistant implementation, compilation status and validation disclaimers
out of the spoken text. Mathematical history belongs in the narration when it
explains the result; project history does not. Do not answer the authoring
conversation (“your displacement intuition is useful”); explain the idea
directly.

**Contrast constructions: allowed, used sparingly and with care.** The
“not X, but Y” pattern and its variants are no longer banned, because some of
the most important facts in this subject are contrasts: sine versus doubled
sine, ordered versus distance gaps, squared versus unsquared displacement.
LLM-drafted prose overuses the pattern, though, and overuse makes a lecture
distracting and unnatural. Variants include “X, not Y”; “this is not X; it is
Y”; “not just X but Y”; “rather than”; and “we did not ask X; we asked Y”.

- Use a contrast when the two things are ones a listener could plausibly
  confuse, and the difference is mathematical content. Example: “Bounded does
  not mean the outputs fit in one ball; it means output size grows at most in
  proportion to input size.”
- Do not use it for emphasis, to set up a point nobody doubted, or to sound
  decisive. Example to avoid: “This is not a mere technicality; it is the heart
  of the argument.”
- First try stating Y alone. Keep the contrast only if Y alone would leave a
  likely misreading in place.
- Expect a handful per lecture, not one per paragraph. Never stack two in
  succession. Reread the whole lecture for them before finishing.

**Avoid other recurring LLM habits.** Watch for ritual qualifiers (“we are not
claiming”, “it would be wrong to say”), stock phrases (“what matters”, “the
lesson is”, “quietly”, “the payoff”, “the machinery”), triads of near-synonyms,
and formulaic openings and closings (“Today we will…”, a closing “lesson”, a
recurring “Reconstruct the argument” section). These are prompts for an edit,
not forbidden words; keep one when it really helps.

**Questions where there is real investigation.**

> “It would be better to start these sort of sections off with a question.”
> “It feels like everything starts with a question now.”
> “Statements of fact can also be pedagogical.”

Use a question when it sets up a real investigation: what if we try this, what
would it tell us, does it answer the larger question? State established facts
directly. Mix questions, observations and deductions so the lecture does not
sound like a quiz. Do not open sections with commands to the listener (“Keep
the same trial plane.”).

**Speak equations naturally.** No raw LaTeX, Lean or code in the spoken region.
Exact formulas go in the companion when speech would obscure them.

## 7. Companions, references and review

**Display-only companion.** Below `<!-- END SPOKEN LECTURE -->`, a mathematical
lecture gives the exact statements, the displayed computations, and
correspondence to actual Lean declarations, including namespace and typeclass
assumptions. Use real identifiers. Record current location and original
provenance as separate facts. The course introduction is exempt.

> “The symbolic math facts that you learned here and can use in a proof.”
> “Have these correspond to Lean statements.”

Close prerequisite lectures' companions with the reusable symbolic facts and
their Lean statements, with the symbolic statement beside each.

**Citations stay out of speech.** Claims about publications (authorship, date,
theorem number, printed hypotheses, priority, errata) go in the non-spoken
sidecar with an exact spoken-text anchor and an audit status. Ordinary
mathematics is supported by its proof and the Lean companion. The schema is in
`draft-stages/tts-lectures/metadata/README.md`.

**Learning resources.**

> “Focused external sources like a Wikipedia page, not a sprawling textbook or a dense paper.”
> “Lecture notes from universities or presentations, or YouTube videos on the topic.”

Each lecture's sidecar lists focused, free resources with a short note on what
each teaches and where to focus. Include a directly relevant Wikipedia article
when one exists. For advanced material, note where the article's scope differs.
Do not add weakly related links to fill a quota. Check the references when
revising a lecture.

**Review is feedback-driven.** Self-edit for clarity, mathematical fidelity and
clean extraction, then publish and use listener feedback to target the next
pass. There is no required A/B comparison or audio acceptance gate; synthesize
and listen when a specific pronunciation or pacing problem needs testing. After
any edit, reread the whole paragraph and its neighbors: a deleted sentence can
strand a pronoun, strengthen a claim, or leave an abrupt definition.

**Reports.** In audits, READMEs and summaries, state what changed, the result,
and the specific remaining work, e.g. “27 narration files pass extraction;
Lean compilation was not run.” Do not append paragraphs about what a review
does not prove unless a reader's decision depends on it.

## 8. Visual versions and slides

These apply to Manim and companion-slide versions of lectures. The spoken
lecture must already work without them.

**Lean in visual versions.** Use Lean to ground the mathematics in something
independently checkable: show the symbolic statement beside its Lean statement,
in a readable highlighted code font, with the relevant part emphasized. Show
how a theorem's hypotheses and dependencies appear in the formal statement.

> “Grant might also explain notation too. Like I have no idea what fancy L is.”
> “These slides are all lacking in visualization, animation, and color coding.”
> “There is no visual cue to tell the student which part of the slide they should be paying attention to wrt to the narration.”

Build pictures that explain the construction. Connect colors and motion to the
narration and keep colors consistent across related graphs, equations and
geometric quantities. Make the current referent visible with a highlight,
pointer or staged calculation. Introduce formulas as the explanation reaches
them rather than displaying a whole derivation at once. A visual event does not
need its own voice clip; keep coherent spoken passages.

> “Make sure the slide says it's an example and highlight the general tool.”

Label worked examples and distinguish their values from the reusable statement;
box or otherwise emphasize the general tool.

> “It looks like we applied TTS rules to the slides themselves.”

Typeset mathematics normally on slides, for example $P=QQ^T$. Spoken renderings
belong only in narration.

> “Numeric considerations should always be an extra bonus slide.”

Put how a computation is done in practice on a separate bonus slide.

**Title slides.** Name the main concept briefly in narration. Show a robot
marker and the recorded model name to disclose LLM generation, and track slide
and transcript model provenance. Git is sufficient history.

**Study questions.**

> “The questions at the end of each lecture have been too easy, or contrived.”
> “Questions should always be very clear about what object they are referring to.”

End a video with four multiple-choice questions: two may check attention and
terminology; two should test understanding by applying an idea, predicting a
change, or distinguishing claims in a new situation. State the objects and
assumptions each question needs. Avoid distractors answerable by phrase
recognition. Use a five-second thinking pause.

For the matrix-exponential introduction specifically, show scalar and matrix
output graphs for a small (for example two-by-two) matrix and highlight the same
time t in both views; explain the pure mathematical viewpoint as well as the
velocity interpretation.

## 9. History lectures and images

> “Always use images with attribution in slides.”
> “Do not check images into the repo. We check the logic to access the images into the repo.”

Use openly licensed portraits and images with visible attribution. Keep
downloaded images out of Git, with the records needed to fetch them.

A person-focused lecture must earn its place: verified biographical context,
the person's actual mathematical contributions, a developed example, the later
use of the ideas, and the limits of the attribution. Such lectures are
long-form, generally 25–35 minutes. Do not pad; keep an underdeveloped draft in
`tts-history/stubs/` until it is ready, and check actual spoken word counts
before promoting it.

## 10. Course tracks

G1 presents the Manim material. G2 is the comprehensive mathematical audio
course. G3 is the shorter, paper-focused audio course: it assumes linear
algebra, singular values and elementary measure theory, presents the four angle
theorems together, and closes with the Section 4 transport sequence through
Proposition 4.3, the Proposition 4.4 counterexample and the real transport
matching theorem. For G3, prioritize the hypotheses needed for the 1970
paper-facing results, and keep ordered gaps, distance gaps, self-adjoint
domains, operator ideals and squared versus unsquared displacement distinct.

Keep each track's identifiers, transcripts, sidecars and audio caches
independent. Record G2 material reused in G3 in G3's `track.json`; edit G3
narration separately.
