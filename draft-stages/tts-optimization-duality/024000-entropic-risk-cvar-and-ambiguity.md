# 024000 - Entropic Risk, CVaR, and Distributional Ambiguity

**Track:** Optimization and Duality. **Background:** convex risk measures, probability distributions, expectation constraints, and distributionally robust optimization. **Central question:** what changes when uncertainty concerns the probability law itself, not just the random loss under one fixed law?

<!-- BEGIN SPOKEN LECTURE -->

# A mean can hide an expensive tail

Suppose a machine failure causes a loss of ten units and happens with probability one tenth. Otherwise the loss is zero. The expected loss is one unit. That average is correct, but it says little about what happens in the most expensive outcomes.

Risk measures summarize different aspects of this distribution. Conditional value at risk asks about the average loss in the worst specified fraction of outcomes. Entropic risk uses an exponential weighting that amplifies high losses. Both can be convex in the underlying loss, under their standard conditions, but they encode different attitudes to the tail.

Now add a second uncertainty: perhaps the failure probability is not known exactly. Historical data suggest it is somewhere between five percent and twenty percent. The decision maker wants protection against every probability law in this ambiguity set. This is distributionally robust risk optimization.

The distinction between ordinary and distributionally robust risk is fundamental. One evaluates a risk functional under a fixed distribution; the other takes its worst value across a family of plausible distributions.

# Conditional value at risk as an optimization problem

For a loss L and confidence level alpha, upper-tail conditional value at risk can be written as a minimum over a threshold t. The objective is t plus the expected excess loss above t, divided by one minus alpha.

This variational formula handles both continuous and discrete distributions without needing to invent a unique quantile inside an atom. It also makes CVaR suitable for convex optimization: when the loss is convex in a decision variable, the positive-part construction preserves convexity under standard integrability conditions.

At confidence level ninety percent, we average the worst ten percent of outcomes, with fractional treatment of atoms when necessary. For our two-point loss distribution with failure probability ten percent, that worst ten percent consists entirely of failures. CVaR is therefore ten, even though the mean is one.

If failure probability were only five percent, the worst ten percent would contain five percent failures and five percent zero-loss outcomes. CVaR would then be five. The tail confidence level and the mass in the high-loss atom both matter.

# Entropic risk weights differently

For a positive risk-aversion parameter eta, entropic risk takes the logarithm of the expected exponential of eta times the loss, then divides by eta. Its exponential emphasis on large losses makes it sensitive to rare severe outcomes.

For our two-point distribution, the expectation inside the logarithm is one minus the failure probability, plus the failure probability times the exponential of ten eta.

As eta approaches zero, entropic risk approaches the ordinary expected loss, assuming sufficient integrability. As eta grows without bound for a bounded discrete loss, entropic risk approaches the largest possible loss with positive probability. For intermediate eta, it interpolates between those behaviors in a precise nonlinear way.

Unlike CVaR, entropic risk need not remain finite for every heavy-tailed distribution. If the exponential moment is infinite, the risk value is infinite. A robust ambiguity set containing such a distribution may make the worst-case entropic risk infinite even when every candidate has a finite mean.

# Add ambiguity about the probability

Let the failure probability vary between five percent and twenty percent. What is the worst expected loss? It is ten times the largest failure probability, or two.

What is the worst ninety-percent CVaR? When the failure probability is at least ten percent, the worst ten percent contains only ten-unit failures, so the CVaR equals ten. The worst-case value over our ambiguity interval is therefore ten.

For entropic risk with positive eta, increasing the failure probability increases the expected exponential because ten is the high outcome. The worst distribution uses failure probability twenty percent. Its entropic risk is one over eta times the logarithm of point eight plus point two times the exponential of ten eta.

We have three different numbers or functions from the same ambiguity set: worst mean two, worst ninety-percent CVaR ten, and a parameter-dependent worst entropic risk. None is incorrect. They answer different questions about uncertain losses.

# Why the ambiguity set matters

Our interval of possible failure probabilities is a very small distributional ambiguity set. In applications, the set may be defined by moment constraints, statistical confidence regions, an f-divergence, or a Wasserstein distance around an empirical distribution.

Each choice restricts which alternative probability laws the adversary is allowed to use. A Wasserstein ball constrains the transport cost of moving probability mass; a divergence ball restricts changes in weights relative to a reference law. These models are not interchangeable, and their behavior depends on the support assumptions and choice of distance or divergence.

For example, a Wasserstein ball on an unbounded outcome space may allow a small amount of probability to be moved very far. For a sufficiently rapidly growing loss, that can make a worst-case expectation infinite. A claim of robustness must therefore include the growth of the loss, the geometry of the support, and the radius of the ambiguity set.

# The order of optimization is an issue

Distributionally robust CVaR can be written as the supremum over distributions of CVaR under that distribution. Inside each CVaR is an infimum over a threshold t. It is tempting to exchange the supremum and infimum and solve one simpler-looking problem.

That exchange is a minimax step. It requires conditions such as appropriate convexity, concavity, compactness, and continuity, or another valid duality theorem. We should not silently commute the operations merely because both involve optimization.

In our finite two-point example, it is easy to check the worst case directly. For a large continuous ambiguity set, establishing a tractable and exact reformulation is part of the mathematical work.

# Robust decisions and certificates

If a decision variable changes the loss distribution, the objective might minimize worst-case CVaR, worst-case entropic risk, or a weighted combination with expected cost. Convexity can permit efficient solution methods, while duality can sometimes convert the adversarial distribution search into finite-dimensional constraints.

But a solver's output still needs interpretation. It may certify an optimum of a chosen ambiguity model, not that the model contains the true data-generating distribution. Statistical coverage of the ambiguity set is a separate question. A risk value also says nothing about individual losses beyond the properties guaranteed by that risk functional.

Distributionally robust risk is useful precisely because it makes two assumptions visible: what kinds of bad outcomes matter, and what probability laws are considered plausible. CVaR emphasizes upper-tail averages; entropic risk emphasizes exponential moments; the ambiguity set formalizes uncertainty about the law itself. Clear mathematics keeps those choices distinct instead of hiding them in one phrase such as “conservative optimization.”

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an integrable loss `L` and `alpha in (0,1)`,
\[
\operatorname{CVaR}_\alpha^P(L)
=\inf_{t\in\mathbb R}\left\{t+\frac{1}{1-\alpha}\mathbb E_P[(L-t)_+]\right\}.
\]
For `eta>0` with finite exponential moment,
\[
\rho_\eta^P(L)=\frac1\eta\log\mathbb E_P[e^{\eta L}].
\]
Let `L=10` with probability `p`, else `0`, with `p in [0.05,0.20]`. Then
\[
\sup_p\mathbb E[L]=2,\quad
\operatorname{CVaR}_{0.9}(L)=10\min(1,p/0.1),\quad
\sup_p\operatorname{CVaR}_{0.9}(L)=10,
\]
and
\[
\sup_p\rho_\eta^p(L)=\frac1\eta\log\left(0.8+0.2e^{10\eta}\right).
\]
The supremum of `inf_t` is not automatically `inf_t` of the supremum; any interchange needs a minimax theorem or direct verification. General distributional ambiguity sets can give infinite worst-case entropic risk when exponential moments are uncontrolled.

### Exercises with answers

1. What is mean loss at `p=0.1`? **Answer:** one.
2. What is `CVaR_0.9` at `p=0.05`? **Answer:** five.
3. Which probability maximizes entropic risk over the interval for `eta>0`? **Answer:** `p=0.20`.
4. Does a worst-case optimum prove the ambiguity set contains the true law? **Answer:** No; statistical coverage is a separate claim.

### Reading and source notes

- [Rockafellar and Uryasev, Optimization of Conditional Value-at-Risk](https://doi.org/10.21314/JOR.2000.038), variational CVaR formulation.
- [Cherukuri and Hota, Consistency of Distributionally Robust Risk- and Chance-Constrained Optimization](https://arxiv.org/abs/2012.08850), risk constraints under Wasserstein ambiguity.
- [Esfahani and Kuhn, Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric](https://arxiv.org/abs/1505.05116), tractable DRO principles and assumptions.
