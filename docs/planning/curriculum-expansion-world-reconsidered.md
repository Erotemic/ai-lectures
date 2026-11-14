# Curriculum expansion: ideas that change how we understand the world

Planning proposal — 13 November 2026. This is an editorial roadmap, not a set of
approved lecture titles, assigned IDs, or claims that the listed research has
already been completed.

## Purpose

Build a library of **substantive, self-contained lectures** about important
questions in mathematics, natural science, history, philosophy, literature,
psychology, and social life. The collection should help a curious listener do
more than acquire facts: it should give them better ways to understand evidence,
reason about causes, recognize mechanisms, evaluate competing explanations, and
make sense of other people's experiences.

The motivating question for expansion is:

> Which ideas are important enough, and understandable enough, that a careful
> lecture might change how a listener thinks about themselves, other people,
> or the world?

A change in perspective is an **ambition for the teaching**, not an outcome to
script in advance. Some familiar ideas survive careful scrutiny. Other ideas
become more conditional. A lecture earns its conclusion by investigating the
question, not by choosing a provocative answer and arranging the evidence around
it. The result should be intellectually challenging without presuming a
specialist audience, and it should remain useful years after publication.

This proposal extends the existing collection rather than redefining its
mathematical research origins. The [Davis–Kahan-centered project vision](lecture-project-vision-and-history.md)
remains the plan for that technical curriculum. The standards in
[LECTURE_STYLE_RULES.md](../../LECTURE_STYLE_RULES.md) remain authoritative for
narration, human biography, source handling, standalone structure, mathematical
explanation, and speech extraction.

## Existing library and gaps

The 13 November source snapshot includes:

| Existing surface | Current scope in `track.json` | Opportunity / boundary |
| --- | --- | --- |
| `draft-stages/tts-history/` | 42 substantial portraits of mathematicians, scientists, statisticians, and associated thinkers | Connect particular lives to broader questions; retain the human-centered portrait identity. |
| `draft-stages/tts-world-history/` | 105 lectures spanning archaeology, ancient societies, historical sources, and literary epics | Expand modern and comparative history without flattening the diverse societies already treated; do not reuse existing archaeology-series IDs. |
| `draft-stages/tts-paper/` | 32 specialized G3 paper lectures | Maintain precise technical prerequisites and rigorous proofs; general-audience offshoots should receive their own treatment rather than diluting G3. |
| G2 / other lecture and presentation surfaces | Mathematics foundations, technical proofs, slides, and broader learning material | Link foundational concepts where useful; verify the current index before deciding a subject is missing. |

The World History track already contains a **“How We Know” archaeology strand**.
A proposed broader series on causation and scientific reasoning should have a
different title and catalog identity, even if it connects to that strand.

Current coverage is especially strong in mathematical operator theory and
selected historical/literary narratives. Promising areas for expansion include
fundamental physics and biology, historical development of political ideas,
modern societies and institutions, economics, empirical psychology, causal
reasoning, and the mathematics of everyday decisions. These are editorial
opportunities, not a completed repository-wide topical census.

## What makes a lecture worth commissioning?

Prioritize subjects with the following properties. No numerical scoring rubric
is required; these questions should guide editorial judgment.

1. **An important question:** What is genuinely worth understanding, and who
   would use this understanding?
2. **Something to reason with:** Does the listener leave with a model,
   derivation, distinction, method, or body of evidence they can apply?
3. **Substance:** Can the question support a developed explanation, historical
   account, and meaningful limitations? An intriguing title alone is not enough.
4. **A human story where appropriate:** Who made the discovery or confronted the
   problem? What did they know, hope, fear, contest, or overlook according to
   surviving evidence? Who bore the consequences?
5. **A tractable evidence base:** Are there primary sources, reputable histories,
   empirical research, and clear ways to distinguish known facts from competing
   interpretations?
6. **A distinct contribution:** What would this lecture teach that neighboring
   lectures do not, even when they share people or examples?
7. **Evergreen value:** Will the central argument remain useful independently of
   this month's news? Current examples can illustrate a durable principle.

Do not force every question into a single moral lesson. A lecture can be valuable
because it exposes a tension, establishes a precise limit, or shows why the
available evidence does not justify the tempting simple answer.

## Proposed organizing architecture

Use two complementary ways to explore the library:

- **Tracks** group lectures that serve a common learning purpose. They set
  audience expectations and navigation, and may suggest a helpful order.
- **Themes / cross-links** connect lectures across tracks: evidence,
  uncertainty, freedom, cooperation, information, evolution, feedback, power,
  time, inequality, flourishing, and technology. These are browsing concepts,
  not a second set of canonical lecture copies.

Three legitimate lecture forms can coexist:

- **Person-centered:** a researched human life in which ideas emerge through
  working practices, relationships, conflicts, and circumstances; keep the
  complete intellectual contribution, as in the History portraits.
- **Question-centered:** begin with a problem and build a coherent explanation
  across disciplines, using appropriate historical people and scenes.
- **Event / work-centered:** investigate a revolution, institution, experiment,
  novel, engineering system, or other concrete object through relevant evidence.

Cross-disciplinary material should not collapse the disciplines into one.
Historical contingency, mathematical proof, experimental inference,
interpretive literary analysis, and moral reasoning answer different kinds of
questions. A strong lecture tells the listener which kind of argument it is
making and why that argument supports the conclusion.

### Four provisional umbrellas

These are **planning groups**, not immediate new manifest IDs. They consolidate
the earlier ten-series proposal into a manageable starting structure.

| Umbrella | Candidate strands | Guiding questions |
| --- | --- | --- |
| **Evidence and Explanation** | Causal inference; psychology and cognition; scientific methods; probability and statistics; philosophy of knowledge | How do we know, why do we disagree, and when does evidence change a belief? |
| **The Natural World** | Physics; life and evolution; medicine; Earth science; chemistry; discoveries that changed scientific models | What mechanisms explain the world, and how did people discover them? |
| **Civilizations and Institutions** | History of political ideas; power; comparative civilizations; money and economies; hidden systems; technology and infrastructure | How do social systems form, persist, transform, and sometimes fail? |
| **Meaning, Culture, and the Future** | Philosophy; literature; moral psychology; living well; AI and biotechnology; intergenerational questions | How do people interpret their lives, and what should they value or build? |

**Mathematics of everyday reasoning** is a proposed cross-cutting strand with
its own clear browsing identity, potentially within Evidence and Explanation.
It should teach actual calculations and their domains of applicability: base
rates, exponential growth, expected value, Bayes' rule, optimization,
compounding, feedback, networks, sampling, and Goodhart-type failure modes.
It can also support the other umbrellas without making them depend on prior
recordings.

## Proposed flagship: *The World Reconsidered*

Working subtitle: *Twelve ideas that change how we think*. A general-audience
entry point to the broader library; order supports a cumulative intellectual
journey, but **every recording must work by itself**. No opening should assume
that listeners heard another episode, and no ending should advertise a sequel
instead of completing its own question.

The twelve entries below are **commissioning briefs**, not final theses. Each
includes a concrete teaching mechanism, possible human or historical material,
and an important qualification or counterexample to investigate. Names and
examples identify research leads; they are not yet verified passage-level
citations.

### 1. How do you know what you know?

- **Question:** Why does a compelling observation sometimes fail to establish
  a cause?
- **Teach:** comparison groups, confounding, causal diagrams, counterfactuals,
  experiments and natural experiments. Work through a numerical case where an
  apparent treatment effect changes when a confounder is accounted for.
- **Human material:** John Snow and the London cholera investigations; the
  arguments around Semmelweis; Florence Nightingale's work with statistics and
  institutional reform. Research their different methods and constraints.
- **Test the easy answer:** randomized trials are powerful but not always
  possible, ethical, or automatically transportable to another population.
- **Boundary:** this is broader than the existing archaeology strand called
  “How We Know.”

### 2. Your mind is a reconstruction of the world

- **Question:** What is the relationship between sensory input, remembered
  experience, and what seems immediately real?
- **Teach:** perception under ambiguity, selective attention, constructive
  memory, and competing models of predictive processing. A worked perceptual
  example should be intelligible without slides.
- **Human material:** investigators of visual illusions and memory, and the
  history of psychological measurement. Find cases where the scientists
  revised their own hypotheses.
- **Test the easy answer:** a fallible perceptual system can still be highly
  effective; do not imply that nothing can be trusted because experience is
  constructed.

### 3. How rational are human beings?

- **Question:** When do judgments approximate good reasoning, and when do they
  break down?
- **Teach:** base rates and Bayesian updating, heuristics, bounded rationality,
  and ecological rationality. Use a transparent numerical example of a test
  result and prior probability.
- **Human material:** the development of experimental judgment research,
  disagreements among Kahneman, Tversky, Gigerenzer, and successors; document
  actual disagreements rather than staging a single winner.
- **Test the easy answer:** “people are irrational” is too broad; separate
  task design, statistical benchmarks, incentives, and real-world performance.

### 4. Why is cooperation possible?

- **Question:** How can cooperation arise when individuals have incentives to
  defect?
- **Teach:** the prisoner's dilemma with a payoff matrix, repetition,
  reciprocity, reputation, coordination, norms, and institutional enforcement.
  Explain why changing the game can change behavior.
- **Human material:** historical cases of collective management, mutual aid,
  research on social dilemmas, and institutional design.
- **Test the easy answer:** neither competition nor cooperation is universal;
  specify the assumptions under which a model predicts either.

### 5. How do ordinary people participate in harm?

- **Question:** How do institutions, incentives, obedience, and personal choices
  contribute to collective wrongdoing?
- **Teach:** distinguish conformity, obedience, diffusion of responsibility,
  organizational incentives, and ideology through documented historical cases.
- **Human material:** perpetrators, victims, bystanders, and resisters with
  attention to their actual choices and constraints.
- **Test the easy answer:** avoid portraying one dramatic psychology experiment
  as a complete explanation; review methodological criticism, replications,
  archival records, and variation in resistance. Preserve moral agency.

### 6. Who decides what is normal?

- **Question:** How do descriptive regularities become expectations, categories,
  and sometimes systems of exclusion?
- **Teach:** descriptive versus prescriptive norms, cultural variation,
  classification, institutional measurement, and historical change. Follow one
  category through a concrete change in law or professional practice.
- **Human material:** people who created, enforced, challenged, or lived under
  classifications; research the consequences in their own words when possible.
- **Test the easy answer:** the fact that categories have histories does not
  establish that every distinction is arbitrary or that no material facts
  constrain classification.

### 7. Why does the whole behave differently from its parts?

- **Question:** How can simple local actions create surprising collective
  outcomes?
- **Teach:** feedback loops, thresholds, networks, path dependence, and
  emergence. Work through at least one small quantitative model (for example,
  contagion on a network or a supply-and-demand feedback loop).
- **Human material:** scientists and engineers whose models changed after
  observing a real system, plus people affected by systems they could not
  individually control.
- **Test the easy answer:** “emergence” is a description to unpack, not an
  all-purpose explanation; show the mechanism and assumptions.

### 8. Why could history have been different?

- **Question:** What can historians responsibly say about alternative paths?
- **Teach:** contingency, structural pressures, path dependence, selection
  effects, and the evidence needed for counterfactual claims. Compare two
  possible explanations for one specific historical turning point.
- **Human material:** people making decisions under uncertainty, not characters
  who already knew the outcome.
- **Test the easy answer:** avoid the claim that civilizations follow a single
  universal rise-and-fall cycle; compare multiple cases and interpretations.

### 9. What is information, and why does it matter?

- **Question:** What does it mean to measure information independently of the
  specific message being sent?
- **Teach:** elementary coding, probability, Shannon entropy, a small
  numerical calculation, noisy channels, and the distinction between signal,
  meaning, and knowledge.
- **Human material:** Claude Shannon's life and work, engineering constraints
  at Bell Labs, and relevant collaborators; verify remembered anecdotes.
- **Test the easy answer:** do not equate information-theoretic entropy with
  meaning, intelligence, uncertainty in every sense, or thermodynamic entropy
  without explaining the mathematical relationship and limits.

### 10. Why does progress produce unintended consequences?

- **Question:** How can a genuine improvement generate new costs or risks?
- **Teach:** externalities, rebound effects, optimization targets, trade-offs,
  feedback, and institutional adaptation. Analyze a specific technology such as
  synthetic fertilizer, electrification, or urban transport with both benefits
  and costs.
- **Human material:** scientists, engineers, workers, communities, and
  policymakers making decisions with partial information.
- **Test the easy answer:** avoid a deterministic claim that improvements
  necessarily make things worse; distinguish preventable design failures from
  difficult trade-offs.

### 11. What makes a good life?

- **Question:** What can philosophical argument and empirical research say
  about flourishing, meaning, pleasure, friendship, and responsibility?
- **Teach:** compare several traditions by their claims and reasons; distinguish
  descriptive well-being research from normative judgments. Examine a concrete
  case where plausible values conflict.
- **Human material:** the lives and historical circumstances of relevant
  thinkers and the people their ideals addressed or excluded.
- **Test the easy answer:** cultural traditions are internally diverse; one
  survey measure of happiness is not a universal theory of value.

### 12. What do we owe the future?

- **Question:** How should present generations make decisions that affect
  people who cannot participate in them?
- **Teach:** intergenerational ethics, uncertainty, irreversible decisions,
  discounting, precaution, governance, and multiple moral frameworks. Work
  through one concrete long-term policy or engineering choice.
- **Human material:** real communities that bore the consequences of earlier
  infrastructure, environmental, medical, or technological decisions.
- **Test the easy answer:** distinguish empirical projections from moral
  commitments; represent multiple defensible ethical arguments and where they
  disagree.

### Gaps and overlaps to manage in the flagship

- Episodes **2 and 3** share cognitive science but do different work: perception
  and memory versus explicit judgment and decision-making.
- Episodes **4 and 5** share social psychology but separate constructive
  cooperation from harmful compliance and institutional wrongdoing.
- Episodes **6 and 8** share historical explanation but address norms versus
  contingency and counterfactual analysis.
- Episodes **7 and 10** share systems ideas but separate *mechanisms of
  emergent behavior* from *evaluating intervention consequences*.
- Episodes **11 and 12** share moral philosophy but separate individual and
  communal flourishing from duties across generations.
- The original titles “The Myth of the Rational Human” and “The Illusion of
  Independence” are better used as **questions to test**, not conclusions built
  into the title.

Do not make the entire flagship a psychology course. The stronger version has
real mathematics, scientific case studies, historical depth, and philosophical
reasoning as well as psychological research.

## Deep-dive tracks and initial slate

The flagship cannot substitute for full treatment of subjects that need
multiple examples, substantial derivations, or sustained historical accounts.
The following candidate tracks can be built independently and cross-linked to
it. Names are working titles and may be grouped differently when implementation
begins.

| Track / strand | Strong initial lecture candidates | Distinct teaching aim |
| --- | --- | --- |
| **History of Ideas** | What did freedom mean in different societies?; histories of rights and citizenship; justice and equality; democracy and representation; competing ideas of progress | Trace changing concepts through people, texts, practices, and institutions, rather than treating modern meanings as timeless. |
| **Psychology of Being Human** | Memory and testimony; belonging and group identity; judgment under uncertainty; motivation and habit; how social norms are learned | Explain findings, methods, replication disputes, and individual variation. |
| **Comparative Civilizations** | Roman transformations; Mongol empires and successor states; imperial China across different dynasties; Indian Ocean trade; the Black Death across regions | Examine specific causal accounts; replace “rise and fall” as a predetermined template with comparison of institutions and circumstances. |
| **Power and Institutions** | Legitimacy; propaganda and communication; bureaucracy; how coalitions form; resistance and reform; constitutional constraints | Make power observable through mechanisms, archives, competing interests, and actual outcomes. |
| **Philosophical Questions** | Free will and responsibility; consciousness; moral disagreement; skepticism; personal identity; duties to strangers | Present serious rival arguments and their strongest objections. |
| **Hidden Systems** | Money creation and bank balance sheets; supply chains; urban zoning and transport; public goods; environmental externalities | Teach mechanisms, simple models, and institutional design through concrete cases. |
| **Discoveries That Rewrote Reality** | Thermodynamics and time's arrow; natural selection; plate tectonics; germ theory; climate measurements; origins of modern physics | Reconstruct what investigators knew, how evidence accumulated, and the exact scientific ideas. |
| **Literature and the Human Condition** | Moral conflict in tragedy; ambition and self-deception; exile and belonging; mortality; narration and unreliable perspective | Read substantial passages and interpret them in literary and historical context, with room for multiple defensible readings. |
| **Future of Humanity** | AI and institutions; biotechnology and consent; demographic change; technological concentration; climate adaptation; long-term stewardship | Distinguish current evidence, credible scenarios, ethical disagreement, and conjecture. Avoid unstable predictions as the organizing content. |
| **Living Well** | Friendship; attention; resilience; virtue and habits; leisure and work; meaning across traditions | Treat traditions as arguments and practices, not a menu of unexamined life advice. |
| **Mathematics of Everyday Reasoning** | Bayes and base rates; exponential growth; expected value; feedback; network effects; optimization; Goodhart's law; sampling | Provide a reusable mathematical toolkit in accessible worked examples. |

### Especially promising stand-alone commissions

These topics could launch a track or serve as longer independent recordings:

1. **Why does time have a direction?** Carnot, Clausius, Maxwell, and
   Boltzmann; heat engines, entropy, microscopic reversibility, and statistical
   mechanics. Include a worked example, not just metaphors about disorder.
2. **How does evolution work?** Darwin, Wallace, natural selection, common
   descent, genetic inheritance, and what the historical investigators could
   reasonably infer from their evidence.
3. **How did humanity learn to fight infectious disease?** Germ theory,
   sanitation, vaccination, public health, and how different interventions were
   evaluated across time.
4. **How did we discover that continents move?** Wegener, Marie Tharp,
   seafloor evidence, magnetic measurements, and the development of plate
   tectonics.
5. **The Haitian Revolution.** Enslavement, revolution, political ideals,
   warfare, emancipation, independence, and the conflicting choices faced by
   participants. The story should be told on its own terms, not only as a
   footnote to European revolutions.
6. **The nitrogen revolution.** Synthetic ammonia, agricultural production,
   industrial chemistry, environmental consequences, and the difficult human
   history of Fritz Haber and Carl Bosch.
7. **What can a machine compute?** Church, Turing, formal computation,
   undecidability, and the practical machines developed in different contexts.
   Distinguish computability from computational feasibility.
8. **How do we know Earth's climate is changing?** Greenhouse physics,
   measurements, energy balance, attribution, and the history of scientific
   investigation, with explicit treatment of uncertainty and its boundaries.
9. **Where does money come from?** Credit, commercial-bank balance sheets,
   central banks, debt, and different monetary institutions across time.
10. **The Black Death across societies.** Disease evidence, trade networks,
    demographic effects, religion, labor, and where historians disagree.
11. **DNA and the molecular basis of inheritance.** Mendelian inheritance,
    chromosome studies, molecular evidence, experimental competition,
    collaboration, and scientific attribution.
12. **The electrical grid as an invention.** Faraday and Maxwell through
    generators, distribution, competing architectures, infrastructure,
    and social consequences.

## Commissioning and research practice

### Before drafting

For each prospective recording, prepare a short research brief recording:

- **Audience and scope:** what background is assumed, what precise question is
  answered, and what is intentionally left for another lecture?
- **Intellectual spine:** the central mechanism, argument, calculation,
  historical comparison, or interpretation the listener should be able to
  explain afterward.
- **Concrete cases:** one primary case to revisit throughout and, where
  helpful, a countercase that tests a tempting generalization.
- **Human record:** first-person testimony, relationships, material conditions,
  institutional structures, and documented disagreement where these help tell
  the story. Do not invent dialogue or inner lives.
- **Evidence:** primary publications, contemporary records, credible
  scholarly analysis, datasets or experiments when relevant, with pinpoint
  locators for claims that require them.
- **Disputes and limits:** which inferences remain contested, which results
  have replication problems, and what alternatives have been proposed?
- **Distinctness:** how the recording differs from existing coverage; links
  belong in non-spoken metadata rather than prerequisites embedded in speech.

Separate the **research bibliography** that supports claims from **further
learning** resources intended for listeners. Preserve linkable source notes and
historical claim anchors outside the spoken region, using the conventions of
existing track metadata rather than creating a new citation framework before
one is needed. Distinguish what a historical subject actually knew at the time
from what later discoveries established; the recent Darwin / Mary Leakey
correction is a useful example of this review question.

### Writing and narration

- Begin with a concrete problem, event, scene, or claim that can be examined.
  The opening should motivate an inquiry without requiring a sensational hook.
- Carry a single argumentative thread through the lecture. If a biographical
  scene appears, connect it to the question, experiment, calculation, or
  decision that follows.
- Explain important mathematics and science in sufficient depth to be
  reconstructed. Put dense expressions, derivations, timelines, and citations
  in a display-only companion when the spoken form would be hard to follow.
- Give opposing interpretations their fair evidential weight. Avoid both
  forced certainty and endless qualifications that prevent a conclusion.
- Use chronology coherently; distinguish testimony, later recollection,
  historical interpretation, and legend. Avoid artificial transitions and
  duplicate conclusions.
- Write for audio and out-of-order listening. No references to prompts,
  editorial instructions, repositories, future episodes, or the learner's
  supposed reactions.
- Make the result substantive. Do not fill time to meet a number; do not ship a
  short outline in place of a promised deep lecture. Split only when both
  resulting lectures can stand on their own and are worth hearing.
- Include a second example, failure case, disagreement, or limitation where
  it significantly improves the listener's understanding.

### Different methods need different evidence

| Domain | Typical evidence | Recurring failure to avoid |
| --- | --- | --- |
| Mathematics | Definitions, calculations, proofs, counterexamples | Treating intuition or an animation as a proof. |
| Experimental science | Methods, measurements, controls, independent results | Presenting an attractive demonstration as conclusive. |
| Psychology | Study design, sampling, replications, meta-analysis, cross-cultural validity | Building a universal account of people from one famous experiment. |
| History | Primary records, archaeology, dated sources, specialist historiography | Back-projecting modern knowledge or values onto past actors; treating one historical cause as sufficient. |
| Economics and policy | Models, institutional records, natural experiments, comparative cases | Confusing a model's prediction under assumptions with a universal law. |
| Philosophy and ethics | Clear premises, arguments, objections, conceptual distinctions | Hiding a value judgment inside a claimed scientific fact. |
| Literature | Close reading, textual history, historical setting, interpretive arguments | Reducing a work to one moral or treating all readings as equally supported. |
| Future-oriented analysis | Current evidence, scenarios, uncertainty, governance and values | Confusing a speculative possibility with a forecast. |

The purpose is intellectual precision without turning lectures into a running
commentary on citation procedure.

## Pilot sequence and practical next steps

Begin with **three independently useful pilots** that test different demands on
the proposed curriculum, rather than drafting all twelve flagship episodes at
once.

| Pilot | Why first | Required intellectual result | Likely companion |
| --- | --- | --- | --- |
| **How do you know what you know?** | Establishes the evidence standard for the rest of the library | A usable causal example contrasting observation and intervention | Small causal diagram, numerical comparison table, source case chronology |
| **Why does time have a direction?** | Tests whether an accessible lecture can also teach substantial physical mathematics | A heat-engine or multiplicity calculation, and an honest distinction between micro- and macroscopic statements | Entropy calculation, phase-space or multiplicity diagram, historical timeline |
| **Why is cooperation possible?** | Tests crossovers among mathematics, psychology, institutions, and history | Derive and interpret a small payoff matrix; explain how repeated interaction or enforcement changes incentives | Payoff table and repeated-game example |

Alternative first science pilot: **How does evolution work?** It would connect
strongly to existing Mary Leakey material and provide a different kind of
historical-evidence investigation than thermodynamics. The three-pilot choice
is a recommendation for exploration, not a fixed schedule.

**Pilot acceptance questions:**

1. Can a listener with the stated prerequisites reconstruct the central
   argument or model without looking at an appendix?
2. Does a real case materially shape the explanation rather than decorating it?
3. Are the human participants portrayed with historical and evidential care?
4. Is a substantial counterargument, counterexample, or limit explored where
   the topic requires it?
5. Does the recording stand alone, with a coherent chronological and logical
   progression and a satisfying conclusion?
6. Do its research notes substantiate important factual and historical claims?
7. Does it add a genuinely distinct use to the library instead of repeating a
   neighboring lecture at greater length?

### Implementation without premature infrastructure

1. Keep this roadmap in `docs/planning/`. It is proposal material, so do not
   register these entries as completed or create stub recordings in active
   browseable tracks.
2. Before implementation, inspect the **current** `track.json` files, metadata
   schemas, and reservation rules. Reserve stable IDs only for an approved
   actual batch. Do not assume today's ID ranges remain free, especially in
   World History where parallel contributions are active.
3. Start with briefs, sources, standalone transcripts, and non-spoken companion
   notes. Reuse existing authoring and validation mechanisms.
4. Decide whether the flagship merits a dedicated track after the pilots.
   Umbrella concepts may initially live as documentation and catalog links;
   no new taxonomy service is required to test them.
5. Develop displays, numerical examples, and credited images when a particular
   lecture benefits from them. The repository's existing asset/provenance policy
   applies. Do not add binary images to documentation overlays.
6. Validate actual generated and extracted narration, source anchors, and
   track inventories when material is promoted. Keep playback IDs stable.
7. Solicit specific listener feedback about confusion, pacing, and missing
   counterexamples, then refine lectures on the evidence from those reports.

## Decisions deliberately left open

- **Flagship identity:** one twelve-lecture track, a curated playlist across
  tracks, or a smaller introductory sequence?
- **Track granularity:** how many of the proposed strands deserve separate
  manifest identities after the first pilots?
- **Audience:** broadly curious adults by default, with per-lecture prerequisites;
  some advanced mathematical companions can serve deeper study.
- **Sequencing:** the proposed order is coherent but should be revised when
  pilots show which concepts listeners actually need first.
- **Titles:** working titles should survive a research brief only if they do
  not predetermine contested conclusions.
- **Scope:** a few subjects may require two or more fully developed lectures;
  length should follow intellectual substance rather than a fixed runtime.

## Editorial north star

A successful recording leaves the listener able to **state the question,
reconstruct the central argument, explain a concrete example, recognize its
limitations, and see the people or institutions involved as part of a real
history**. The library should make difficult ideas approachable while
preserving the difficulty that makes them worth learning.
