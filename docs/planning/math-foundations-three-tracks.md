# Three complementary mathematics foundations tracks

**Date:** 14 November 2026. **Status:** Three substantive lectures delivered in each track; remaining lectures are a prioritized curriculum proposal. **Existing courses:** category theory, advanced spectral/perturbation theory, historical portraits, World Reconsidered.

## Why these three

1. **Logic, Type Theory, and Constructive Mathematics** makes the interpretation of a formal proof, computational content, dependent specifications, and Lean's trusted kernel precise. This complements category theory's treatment of arrows and categorical logic. Use it when translating mathematics and algorithmic intent into formal statements, checking exact hypotheses, or deciding what data a certified algorithm returns.
2. **Optimization, Convexity, and Duality** develops a general language for optimizing algorithms, verifying numerical outputs, and proving bounds. Dual certificates, KKT hypotheses, linear and semidefinite relaxations connect naturally to spectral perturbation theory, combinatorial optimization, and practical engineering.
3. **Probability, Measure, and Statistical Reasoning** supplies the foundations for uncertainty, estimation, stochastic processes, statistical learning, and calibration. The measure-theoretic direction makes probability compatible with rigorous functional analysis and eventual formalization.

The nine lectures delivered across the three tracks are designed for a mathematically curious listener, with concept-first spoken explanations and substantive written companions. Together they answer distinct questions: **What constitutes a proof?** **What demonstrates that a solution is optimal?** **How can uncertainty be represented and updated?**

## Course inventories and intended progression

### Logic, Type Theory, and Constructive Mathematics

- 001000 (delivered): *Proofs as Objects: Why Propositions Can Be Types*. Functions as implications, conjunctions/disjunctions, quantifiers, `Prop` vs `Type`, dependent witnesses, and honest specification limits.
- 002000 (delivered): *Natural Deduction and Lambda Calculus: How Proofs Compute*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 003000 (delivered): *Dependent Functions and Quantifiers: What Does a Witness Contain?*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 004000: Inductive datatypes, recursion, and structural induction; how elimination rules enable proofs.
- 005000: Definitional/propositional equality, rewriting, transport, and quotient types.
- 006000: Classical axioms, excluded middle, choice, proof irrelevance, and what remains computational.
- 007000: Universes, consistency boundaries, and the small kernel.
- 008000: Connecting specifications to executable verified algorithms, refinement, and certified interfaces.

### Optimization, Convexity, and Duality

- 001000 (delivered): *When Is a Solution Truly Best? Optimization and Certificates*. Exact primal/dual LP solutions, convex quadratic and Lagrangian, weak versus strong duality.
- 002000 (delivered): *Convex Sets and Supporting Hyperplanes: Geometry That Proves Bounds*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 003000 (delivered): *Linear Programming and Duality: Two Answers That Certify Each Other*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 004000: Lagrangians, KKT and Slater conditions; counterexamples without qualifications.
- 005000: Gradient and accelerated methods; smoothness, conditioning and convergence bounds.
- 006000: Nonsmooth convexity; subgradients, proximal maps, Fenchel duality.
- 007000: Eigenvalue variational principles and semidefinite programming; spectral constraints.
- 008000: Integer optimization, relaxations, integrality gaps, combinatorial certificates.
- 009000: Verifying solver outputs with exact/rational or interval certificates; formalization stretch.

### Probability, Measure, and Statistical Reasoning

- 001000 (delivered): *Measuring Uncertainty: Events, Evidence, and Expectation*. Conditional probability, Bayes, independence, expected value, variance, and continuous measures.
- 002000 (delivered): *Counting, Conditioning, and Independence: How Evidence Changes the Sample Space*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 003000 (delivered): *Random Variables, Distributions, and Expectation: Turning Outcomes into Quantities*. Standalone spoken manuscript, mathematical companion, exercises, and source sidecar.
- 004000: Sigma algebras, measures, integration, null sets, convergence modes.
- 005000: Conditional expectation as integration, projection and information restriction.
- 006000: Laws of large numbers, concentration, central limit behavior and dependence assumptions.
- 007000: Martingales, filtrations, stopping times and optional-stopping qualifications.
- 008000: Bayesian inference, statistical identification, likelihood and calibration.
- 009000: Markov chains/processes, random algorithms, inference on dynamical systems.
- 010000: Formal probability spaces, measurable functions, and Lean/mathlib proof exercises.

## Authoring and acceptance principles

- Keep the existing standalone, evergreen audio style. Every lecture establishes its own objects and assumptions; avoid references to earlier lecture numbers in speech.
- Teach one problem in detail and prove at least one nontrivial result. Put dense notation, exact calculations, code and exercises in the display-only companion. Avoid spoken formulas that are hard to parse without a board.
- Do not substitute a list of theorem statements for a coherent intellectual path. Preserve failures and counterexamples as part of the explanation.
- Include specific, sourced historical scenes where they illuminate ideas; avoid invented dialogue and generalized historical moralizing.
- Source metadata refers to exact anchors in speech. Record external references with stable URLs; keep URLs out of narration.
- For proofs and algorithms, distinguish a theorem, its required hypotheses, a computational implementation, and external assumptions. For numerics, distinguish mathematical optimality from rounding and approximation.
- No fixed word target beyond substantive depth; add explanation when it improves the listener's reasoning rather than padding to a duration.
- Confirm each new transcript can be extracted with the canonical TTS extractor, that track manifests and metadata agree, and that the reader API can select all three tracks.

## Three-lecture launch milestone (14 November 2026)

Each track now has IDs 001000-003000 registered in the existing audio reader, with no additional routing code. Six new manuscripts add natural deduction and dependent quantifiers, convexity and LP duality, and conditioning and random variables. Their per-lecture reference sidecars and source catalogs record historical provenance. Future lectures should preserve the emphasis on explicit hypotheses, proof certificates, and carefully specified probabilistic models.

## Follow-on sequence

Highest-leverage next lectures: (a) inductive datatypes and recursion, (b) Lagrange multipliers and KKT conditions, and (c) sigma algebras and almost-sure reasoning. After those, deepen the tracks independently. Preserve the ability to take any lecture out of order; later lectures can state real prerequisites in metadata.

## Integration boundaries

Use new track IDs `logic-types`, `optimization-duality`, `probability-measure` and directories `draft-stages/tts-logic-types`, `draft-stages/tts-optimization-duality`, `draft-stages/tts-probability-measure`. Each now holds stable lecture IDs `001000`-`003000` within its track: cache and API keys are track-qualified. No change to historical tracks or category theory is required. Their initial audio reader registrations are already in place; continuation requires only manifest, transcript, reference, and test updates, not changes to shared synthesis behavior.
