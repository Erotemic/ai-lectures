# Lecture authoring: accuracy, clarity, and creative freedom

This file documents editorial intentions, **not a formula for writing lectures**.
It applies across subjects (mathematics, literary criticism, fiction craft,
history, music, and other courses). It should help authors teach, not suppress
what they can say or how they can say it.

## The governing principle

**The material determines the form and length.** No fixed duration, word-count
minimum or maximum, word-density quota, section count, mandatory opener,
mandatory exercise, canonical story arc, or required list of rhetorical devices.
A short, complete explanation and an expansive, necessary one are both valid.
Record spoken word counts and estimated duration as **measurements only**;
neither may be used to accept or reject a lecture. There is no stylistic
keyword blacklist.

For adult course organization, entries under roughly ten minutes deserve review:
combine neighboring pieces when they develop one coherent subject, rather than
presenting many five-minute parts as independent lectures. A single lecture can
comfortably run up to about 40–60 minutes when its content warrants it; beyond
that, look for meaningful partition points. These are editorial preferences,
with exceptions for the material, not automatic duration gates or instructions
to pad a complete explanation. Keep a short overview separate when it serves a
clear purpose and actually points to its deeper treatment. Children's stories
are exempt: their short episode lengths are intentional.

**Give the lecture a voice.** A writer can use vivid scenes, dialogue,
provocation, digressions, first person, humor, questions, statements,
recurrences, silence, changes of register, an essayistic argument, a
chronological account, nonlinear narration, or other appropriate devices.
Original fiction embedded in a writing lecture is free to use the techniques
being studied, including unreliable narrators, irony, metafiction, suspense,
multiple voices, and emotionally difficult material. Do not sterilize these
examples in the name of a uniform TTS style. The same freedom applies to
human portraits and mathematical exposition when it helps understanding.

A recurring example, a strong opening, a motivated transition, or an exercise
can be valuable. None is mandatory. Do not rewrite effective material simply
to satisfy a template or to avoid a particular phrase. Judge the actual
listener's experience and intellectual content. **Do not write automated tests
that enforce literary taste, prose structure, lexical preferences, episode
length, or arbitrary counts of examples.**

## What is worth protecting

- **Correctness:** Definitions, claims, mathematics, chronology, attributions,
  and source interpretations must be supportable. State substantive
  qualifications when they change the result; do not hide uncertainty or
  invent historical facts. Use primary sources and reliable scholarship when
  possible. Distinguish an author's documented view from the lecture's own
  synthesis or an invented example.
- **Comprehension:** Introduce the concepts and context the intended audience
  needs. For a difficult mathematical step, an example, derivation, analogy,
  proof strategy, or carefully paced explanation may help. Choose whichever
  is appropriate; there is no universal order of presentation. Preserve
  hypotheses, domains, distinctions between scalar fields and norms, and
  counterexamples when mathematically relevant.
- **Authentic narration:** Produce an intelligible spoken work, not a log of
  code-generation, prompt exchanges, compilation checks, Git operations, or
  reference bookkeeping. Natural acknowledgment of uncertainty, research
  methods, sources, or historical context is welcome when it adds meaning.
- **Evidence and ethics:** For biographies, portray people through
  documented relationships, temperament, work, conflict, and circumstances as
  evidence permits. Do not fabricate private thoughts or portray legends as
  established testimony. Let the mathematics and the human story develop
  together when that improves the account, without a trait checklist.
- **Reader choice:** A recording should be understandable to a listener with
  its declared prerequisites. Give it a real subject and conclusion rather
  than requiring knowledge of the authoring conversation. Connections to other
  recordings are useful when they make sense; avoid relying on an unexplained
  "last time" or "next lecture" to supply missing content. A series may
  still have meaningful prerequisites and continuity.

## Speech, display, and references are different surfaces

The extraction contract is mechanical: exactly one
`<!-- BEGIN SPOKEN LECTURE -->` and one
`<!-- END SPOKEN LECTURE -->` pair, with nonempty, extractable prose between.
That region is the actual TTS input. Keep markup that the extractor cannot
speak (raw fenced code, raw TeX environments, embedded scripts) outside it,
but **never** suppress an idea, formula, quotation, dramatic scene, or useful
technical nuance just because its natural written notation is difficult for
TTS. Explain it in speech and place exact equations, code, score notation,
images, and detailed tables in a non-spoken companion when beneficial.

Slides and visual companions are free to use correctly typeset mathematics,
notation, diagrams, color, and other expressive visual devices. Do not rewrite
visually readable mathematics into phonetic TTS spelling on a slide.
Pronunciation adaptations belong only in synthesis input as needed.

Record bibliographic sources and source-backed historical claims in the
track's metadata and companion notes. Attribution can also be spoken when it
helps the listener. Anchors and IDs must match the actual text; a descriptive
count in a manifest must match the extracted narration. Do not conflate
bibliographic completeness with an arbitrary minimum number of sources.

## Mathematical lectures

Teach the actual problem, definitions, construction, reasoning, and limits.
A theorem-centered opening, an application, a worked example, a historical
question, or a conceptual puzzle can each be effective. Explain unfamiliar
notation when needed, especially objects that change role across spaces;
avoid making experienced listeners repeatedly relearn standard prerequisites.
Deep proofs should retain the mathematical substance, not become lists of
claims or mechanically shortened summaries. Speak exact conclusions and
important counterexamples; retain corresponding equations in companions.

Historical details can illuminate why a mathematical question arose. Real
letters, recollections, work habits, struggles, friendships, and disputes can
humanize people, but source strength governs how confidently we tell them.
There is no universal ratio of biography to mathematics and **no special
runtime target for historical portraits**.

## Editorial review and automated checks

Read the narration as a whole. Ask whether its substance is sound, its flow
serves its audience, its evidence is honest, and its form carries its meaning.
If it works, leave it alone. If it fails, identify the passage and problem;
fix the specific issue instead of adding an instruction everyone must obey.
Listener feedback and optional synthesis spot checks can be useful, but do not
make repetitive review rituals a release gate without demonstrated benefit.

Automated tests may check functional invariants: stable identifiers,
registered files, valid spoken markers and extraction, structurally valid
metadata, source-ID resolution, correct audio routing, and descriptive count
accuracy. They must **not** impose minimum or maximum lecture duration,
mandatory paragraph shapes, minimum anecdote or reference counts, proscribed
vocabulary, or a theory of narrative style. Production audio safety and
technical chunking limits are implementation concerns, not constraints on
how a lecture is written.
