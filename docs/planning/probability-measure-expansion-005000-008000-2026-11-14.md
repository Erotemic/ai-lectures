# Probability and Measure: continuation and expansion

**14 November 2026. Status:** lectures `005000`–`008000` authored and source-tagged. The original `001000`–`004000` remain unchanged. This addendum explains the progression, mathematics, and follow-on curriculum; it does not replace the existing three-track overview.

## Editorial direction

This track should transition from elementary events, integrals, and sigma algebras to *probabilistic claims one can inspect*. A theorem belongs with its assumptions and a meaningful failure case. Prefer a repeated concrete example, a proof with a visible idea, and an explanation of what a theorem does **not** establish. Lecture narration should remain audio-first, without references to earlier episode numbers. Dense notation is reserved for the companion section.

## New lectures

| ID | Title | Principal result | Deliberate limitation |
|---|---|---|---|
| `005000` | Conditional Expectation: Information, Averages, and Projection | Finite partition construction; tower property via defining balance; conditional expectation as the unique least-squares projection in \(L^2\) | Measurable versions only a.s.; conditioning on probability-zero values needs appropriate regular versions; square-loss optimality differs from absolute loss |
| `006000` | Large Numbers, Concentration, and Normal Approximation | Markov and Chebyshev; variance proof of weak LLN; bounded-sum Hoeffding; CLT statement; Borel–Cantelli perspective | Dependence, nonstationarity, and heavy tails; asymptotic normality is not a finite-n guarantee |
| `007000` | Martingales, Filtrations, and the Limits of Stopping Rules | Bounded optional-stopping proof from predictable increments; conditional-probability martingale; stopped fair walk | A.s.-finite hitting time with infinite expectation; stopping limit may fail to exchange with expectation |
| `008000` | Bayesian Inference, Identification, and Calibration | Beta–Bernoulli conjugacy; Bayesian predictive averaging; likelihood non-identification example; proper Brier score proof | Prior dependence, model misspecification, pooled versus subgroup calibration, confounding |

### Mathematical editorial checks

- `005000`: The Radon–Nikodym existence argument requires \(X\in L^1\); the geometric identity requires \(X\in L^2\) and \(Z\in L^2(\mathcal G)\). Projection is a square-loss claim. The ordinary event-quotient formula is not applied to zero-probability conditioning events.
- `006000`: The displayed Hoeffding bound uses independence and bounded intervals; the strong law is stated for iid variables with finite absolute mean. Weak law proof from Chebyshev assumes finite variance. The CLT statement assumes finite nonzero variance. The perfect-correlation example contradicts an unqualified sample-size claim, not the theorems.
- `007000`: The stopping proof first handles \(T\le N\), where each indicator \(\mathbf1_{\{T\ge k\}}\) is known at time \(k-1\). The hitting-time counterexample uses an almost-surely finite, nonintegrable stopping time. Bounded increments plus finite expected stopping time is stated only as a sufficient condition.
- `008000`: Conjugate calculations are performed conditional on a fixed common Bernoulli rate and iid observations. The predictive count is beta-binomial after integrating out the common rate. Identification means injectivity of the observable law in the target parameter. The binary Brier score's expected value decomposes as irreducible Bernoulli variance plus squared miscalibration at a fixed true \(p\).

## Longer-term curriculum after `008000`

The original plan proposed Markov processes and probability formalization. A more developed ladder is:

1. **`009000` Markov Chains and Stationary Distributions:** transition matrices, detailed balance, irreducibility and aperiodicity in finite state spaces, convergence and coupling. Include reducible and periodic counterexamples. Connect to randomized algorithms without assuming all chains mix rapidly.
2. **`010000` Product Measures, Fubini, and Conditional Distributions:** independent random variables on product spaces; Tonelli for nonnegative functions, Fubini for integrable functions; density-based conditional formulas as a special case. Include a non-absolutely-integrable warning for interchange of integration order.
3. **`011000` Weak Convergence and Continuous Mapping:** distributional versus probabilistic convergence, portmanteau intuition, empirical distribution functions and a worked continuous mapping argument. Explain why convergence in law does not imply convergence in probability on an arbitrary shared space.
4. **`012000` Concentration Beyond IID:** bounded differences, martingale concentration, variance-aware inequalities and dependence structure; distinguish union bounds from uniform-over-hypothesis claims.
5. **`013000` Statistical Decision Theory and Risk:** bias and variance, prediction risk, proper scores, decision thresholds and distribution shift; relate optimization objectives to the data generating assumptions.
6. **`014000` Probability in Lean and Mathlib:** formal probability spaces, measurable functions, conditional expectation, finite measures, pushforwards and elementary concentration proofs. Begin with small theorem wrappers and explicit interfaces before attempting fully formalized stochastic algorithms.
7. **`015000` Brownian Motion and Continuous-Time Modeling:** finite-dimensional distributions, independent increments, continuity, hitting times and qualitative links to diffusion; do not use stochastic integration before its separate prerequisites are supplied.

These are proposals, not yet authored manuscripts. Each should be independently listenable with prerequisites expressed in metadata rather than spoken chronological references.

## Reading and source map

- MIT 18.125 and 18.175: measure theory, laws of large numbers, martingales and probability limits.
- MIT 18.675: proof-oriented integration, conditional expectation, optional stopping and uniform integrability.
- Hoeffding (1963): independent bounded-sum tail bounds.
- Gelman et al., *Bayesian Data Analysis*: priors, likelihoods, posterior prediction and model checks.
- Brier (1950), Gneiting and Raftery (2007): probabilistic forecast evaluation and proper scores.

The source records are in `draft-stages/tts-probability-measure/metadata/sources.json`, with per-lecture claim anchors and references. No audio generation or listening audit is implied by registering text manuscripts.
