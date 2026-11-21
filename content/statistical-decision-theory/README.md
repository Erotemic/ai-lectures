# Statistical Decision Theory and Bayesian Computation

Six complete audio-first mathematics lectures connect probabilistic inference to action under loss, risk comparisons between estimators, shrinkage, predictive model checks, and the computational machinery needed to approximate posterior expectations. The sequence complements the existing `probability-measure` track rather than replacing its probability, inference and Markov-chain introductions.

## Listening order

- `statistical-decision-theory:001000` — **A Probability Is Not Yet a Decision**: Derives posterior expected loss, cost-sensitive thresholds and the expected value of a diagnostic test, distinguishing observational forecasts from intervention decisions.
- `statistical-decision-theory:002000` — **Risk, Admissibility, and the Minimax Choice**: Develops the frequentist risk function, dominance, admissibility, Bayes average risk and minimax worst-case risk with a coin estimator and a complete two-state game.
- `statistical-decision-theory:003000` — **The Advantage of Shrinking Several Estimates**: Derives conjugate normal shrinkage and partial pooling, then proves the James–Stein risk improvement via Stein’s identity while keeping Bayesian and frequentist guarantees separate.
- `statistical-decision-theory:004000` — **When the Model Predicts the Wrong Pattern**: Uses a twelve-test ordering counterexample to develop prior and posterior predictive checking, then distinguishes model criticism from out-of-sample predictive validation.
- `statistical-decision-theory:005000` — **A Chain That Samples the Posterior**: Builds a three-state Metropolis chain, verifies detailed balance, derives Metropolis–Hastings and separates stationarity from mixing and Monte Carlo accuracy.
- `statistical-decision-theory:006000` — **From Gibbs Updates to Hamiltonian Trajectories**: Derives bivariate-normal Gibbs persistence, introduces HMC leapfrog and Metropolis correction, and explains practical multi-chain, effective-sample-size and divergence diagnostics.

## Preparation and listening routes

The default route follows all six lectures. The `decisions-and-risk` route covers decision-theoretic mathematics; `bayesian-workflow` combines decisions with predictive checking and computation; `computational-foundations` isolates the two MCMC lectures.

Relevant earlier lectures:

- `probability-measure:003000` — random variables and expectation.
- `probability-measure:008000` — Bayesian inference, identifiability and calibration.
- `probability-measure:009000` — Markov-chain stationarity and mixing.
- `probability-measure:021000` — estimator bias, variance and precision.
- `probability-measure:022000` — bootstrap sampling.
- `probability-measure:036000` — conditional expectation as projection.

Every manuscript contains one continuous spoken region and a separate mathematical companion with exact equations, exercises and bibliographic references. No media or binaries are included. All six lectures and their prose are new; no previously published track files are replaced.

## Mathematical boundaries

- Posterior Bayes optimality minimizes loss under the stated model and prior; it is not the same claim as frequentist risk dominance.
- James–Stein risk improvement assumes at least three normal-mean coordinates under total squared-error loss with known common variance.
- Posterior predictive checks assess selected features and cannot prove that a model is true. LOO evaluates a particular out-of-sample prediction task.
- Correct MCMC stationary distributions do not establish that any finite run has mixed adequately, nor that the statistical model is appropriate.
