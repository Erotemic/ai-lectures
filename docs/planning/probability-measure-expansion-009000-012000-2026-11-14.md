# Probability and Measure: Markov, Product, Limits, and Dependence

**Date:** 14 November 2026. **Status:** Lectures `009000`–`012000` authored and registered as an additive continuation of the existing `001000`–`008000` track. This document is an editorial/math scope map, not a replacement for the three-track overview or the 005000–008000 addendum.

## Reason for this sequence

The prior batch established conditional expectation, laws of large numbers, martingales, and Bayesian inference. The next bottleneck is understanding how **joint laws evolve**, how **integrals over joint laws** can be rearranged, how **laws themselves converge**, and how to get **finite-sample bounds when dependence exists**. This sequence is deliberately not a random survey: each lecture develops a different interface between modeling assumptions and the claims they permit.

| ID | Manuscript | Principal mathematical argument | Failure case / boundary |
|---|---|---|---|
| 009000 | *Markov Chains: Stationarity, Mixing, and Randomized Computation* | Explicit two-state contraction; total-variation coupling; detailed-balance verification | Periodic alternator has stationary law without convergence; reducible classes; bottleneck means slow mixing |
| 010000 | *Product Measures, Fubini, and Conditional Distributions* | Rectangle-to-simple-function-to-monotone-limit construction; Tonelli/Fubini; conditional-kernel factorization | Signed non-absolutely-convergent double series gives different iterated sums; shared marginals do not determine dependence |
| 011000 | *Weak Convergence: When Distributions Approach a Limit* | Bounded-continuous test characterization; continuous mapping proof by composition; empirical CDF via SLLN and monotonicity | Equal laws need not mean outcomes are close; discontinuous threshold maps may fail; rare extreme events break expectation convergence |
| 012000 | *Concentration Beyond IID: Bounded Differences, Martingales, and Dependence* | Reveal-independent-input Doob martingale and conditional Hoeffding lemma; Azuma/Freedman comparison | Perfectly correlated copies; pairwise independence without mutual independence; fixed-class bounds do not cover arbitrary adaptive reuse |

## Mathematical audit notes

### 009000 — finite-state hypotheses and coupling

- Row-stochastic transition matrix `[[.8,.2],[.3,.7]]` has stationary row distribution `(.6,.4)`. If `p_t=P(X_t=working)`, then `p_{t+1}=.3+.5 p_t` and `p_t=.6+(p_0-.6)2^{-t}`.
- A shared-uniform coupling of the two state transitions succeeds in matching an initially different pair with probability one half per step, and keeps matched copies together. The total variation coupling inequality is a bound on marginal laws, not an independence assertion.
- The finite-state theorem needs irreducibility and aperiodicity for convergence from every start. Detailed balance suffices for stationarity but is not necessary; even reversible chains may mix slowly.
- A stationary time series can have autocorrelation. For Monte Carlo accuracy, an invariant target and an actual finite mixing bound are distinct proof obligations. Infinite-state chains need different recurrence/accessibility hypotheses.
- The geometric waiting-time example counts the transition that leaves the current state. Mean run lengths are five working transitions and ten-thirds broken transitions. The long-run fraction is their ratio of mean cycle durations, not the expectation of a random ratio.

### 010000 — theorems are about a specified measure

- Construct product sigma algebra from measurable rectangles. On sigma-finite spaces, extend the rectangle rule to a unique product measure; independence of variables is equivalent to the joint law being the product of marginals.
- Tonelli applies to product-measurable `f>=0`; both iterated integrals equal the joint integral in the extended nonnegative reals and may be infinite.
- Fubini gives equality of finite iterated integrals for integrable signed functions, requiring `∫|f|<∞` as the clean sufficient condition.
- On `N×N` with counting measure, `a(i,j)=[j=i]-[j=i+1]` has row-first sum 0 and column-first sum 1 while `Σ|a(i,j)|=∞`. Do not infer absolute convergence from one finite iterated integral.
- Conditional density quotient needs positive conditioning marginal. Regular conditional probability kernels are guaranteed in standard Borel settings; they are not promised on arbitrary measurable spaces. A kernel factorization does not by itself impose causality.

### 011000 — topology and moments are different

- Weak convergence of real laws is determined by bounded continuous tests, or CDF convergence at continuity points of the limit. The proof of continuous mapping uses composition of bounded continuous functions.
- The complementary Bernoulli coupling has identical marginal laws and distance one almost surely, so weak convergence cannot imply convergence in probability to a particular representative on the same space.
- `X_n=1/n -> 0` in probability, but applying `1_{x>0}` fails to preserve the limit. Portmanteau bounds yield event-probability convergence only when the limit gives zero mass to the event boundary.
- A rare value `n^2` with probability `1/n` gives `X_n -> 0` in probability and `E[X_n]=n`. Convergence of unbounded moments needs additional tail control, e.g. uniform integrability in an appropriate convergence theorem.
- For iid real variables, strong laws at countably many rational thresholds and monotonicity yield weak convergence of the empirical CDF to the population distribution at continuity points. Uniform Glivenko–Cantelli is a separate stronger conclusion.

### 012000 — the independent objects must be identified

- McDiarmid is for a function of independent primitive inputs with a bounded effect of replacing each coordinate. Dependent derived components are allowed, but independent primitive coordinates are not optional.
- The Doob martingale `M_i=E[f|X_1,...,X_i]` has increments with conditional range at most `c_i` by the coordinate-replacement assumption and independence. Hoeffding's lemma yields the one-sided exponent `-2t^2/Σc_i²`.
- Azuma's common symmetric-increment form uses `|D_i|<=b_i`; the one-sided bound is `exp(-t²/(2Σb_i²))`. Freedman additionally tracks predictable conditional variance and an upper bound on increments. Different constants reflect different hypotheses.
- Perfectly dependent repeated bits give no concentration in the number of observed copies. A time-series average requires covariance or mixing control, not merely a stationary marginal.
- Union bounds over a fixed finite hypothesis class require valid per-hypothesis bounds, but do not require independent error events. Hypotheses chosen after adaptively inspecting the sample are not automatically covered by a bound computed for a previously fixed small class.
- A concentration guarantee concerns a deviation around a mean under a model. It proves neither a good mean nor the model's validity for deployment.

## Future sequence, not yet authored

- `013000`: **Statistical decision theory and risk** — Bayes acts, proper scores, risk decomposition, calibration under shift, decision thresholds and asymmetric losses. Distinguish conditional risk from evaluation under distribution shift.
- `014000`: **Probability in Lean and Mathlib** — measurable functions, pushforwards, conditional expectation, finite-state Markov models, basic integral theorems, and small exact theorem interfaces. Check current mathlib definitions before committing proof code; do not treat a lecture as an implementation claim.
- `015000`: **Brownian motion and continuous time** — Gaussian increments, finite-dimensional laws, path continuity, reflection principle, hitting times, and where stochastic integration requires further foundations.

A future measure-heavy expansion should also consider disintegration, Radon–Nikodym, uniform integrability, dominated convergence, and convergence of probability measures on general Polish spaces as their own lectures; this batch touches these but does not claim comprehensive coverage.

## Source census for this extension

- Levin and Peres, *Markov Chains and Mixing Times*, second edition (author-hosted): finite mixing, stationary distributions, coupling, randomized algorithms.
- MIT OpenCourseWare 18.125 lecture 20: product measures and Fubini; MIT 18.175: weak convergence, martingales, Markov chains.
- Klenke, *Probability Theory: A Comprehensive Course*: foundations of conditional distributions and measure-theoretic probability.
- Billingsley, *Convergence of Probability Measures*, second edition: portmanteau, mapping, and weak convergence.
- McDiarmid, *Concentration* (1998): bounded differences and martingales; Paulin, *Concentration inequalities for Markov chains by Marton couplings and spectral methods* (2015): dependence-sensitive bounds.

The per-lecture metadata in `content/probability-measure/metadata/` connects literal claim anchors to the source IDs. Manuscripts are text assets; no TTS synthesis, listening review, or Lean mechanization is claimed.
