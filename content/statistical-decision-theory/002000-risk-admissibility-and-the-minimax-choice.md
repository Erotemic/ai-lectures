# 002000 — Risk, Admissibility, and the Minimax Choice

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** expected loss, conditional probability, basic estimation. **Theme:** compare entire procedures before knowing which parameter value is true.

<!-- BEGIN SPOKEN LECTURE -->

# Risk, Admissibility, and the Minimax Choice

Suppose a statistician must choose one estimator before the data arrive. She can analyze yesterday's observations, compare formulas, and think about plausible values for the unknown parameter. But she cannot make the estimator depend on the true parameter, because that is exactly the quantity she does not know. How should she choose among procedures that each work well in some circumstances and poorly in others?

This is a different question from choosing an action after seeing data. It forces us to evaluate a rule across the collection of worlds in which the unknown parameter might take different values. The primary object is the risk function: the expected loss of a decision rule when the true parameter is fixed at a particular value.

To see why a single error score is insufficient, imagine flipping a coin four times. Its unknown probability of heads is p. Our data are the number of observed heads, divided by four. The natural estimator is the sample fraction. It is unbiased. Its mean squared error, conditional on the true value p, is p times one minus p divided by four. Now compare it with an estimator that ignores all observations and always announces one half.

The constant estimator has exactly zero error if p truly equals one half. The sample fraction fluctuates with the data even when the coin is fair, giving expected squared error one sixteenth. Near p equal to zero, however, the sample fraction becomes excellent: it is zero with overwhelming probability, and at p exactly zero it is always correct. The constant estimate remains half a unit away, so its squared error is one quarter.

Neither procedure is universally best. To claim that one is better, we must specify how we compare the whole curve of risks across all p between zero and one. Frequentist decision theory is built around this question, and it allows genuinely different answers depending on the criterion we select.

## The whole curve, not a single number

The formal risk of a rule delta at parameter theta is the expectation, under the sampling distribution determined by theta, of the loss produced by delta of the data. Theta is fixed for this expectation. We imagine repeated samples from that fixed world. If we use squared error and theta is a probability, the risk is simply mean squared estimation error.

A procedure can be biased and still have smaller mean squared error over a region of parameter values. That is why unbiasedness alone cannot settle this comparison. The earlier statistical-inference lectures introduced the bias-variance identity; decision theory turns it into a question about which tradeoffs we accept. Reducing variance by shrinking an estimate can help near a plausible center while introducing substantial bias far from it.

One way to eliminate some procedures without choosing an arbitrary compromise is dominance. Suppose rule A has risk no greater than rule B at every possible parameter value and strictly smaller at least somewhere. Then B is inadmissible: there is a competitor that is never worse under the chosen loss and sometimes better. An admissible rule is one that no other available rule dominates in this sense.

Here is a clean example of strict dominance. Suppose theta is known to lie between zero and one, but an unconstrained estimator based on a noisy measurement can produce numbers outside that interval. Replace its output by zero if it falls below zero, by one if it rises above one, and leave it alone otherwise. For every theta in the permitted interval, projecting an estimate onto the interval cannot increase its distance from theta. Under squared-error loss, it cannot increase loss for any observed data. If out-of-range outputs can occur with positive probability, it strictly improves expected loss. The original unprojected rule is therefore inadmissible in such a model.

Notice the logic: this is stronger than finding one dataset on which clipping helps. The pointwise geometric inequality proves improvement simultaneously for every possible true theta. An inadmissibility proof must supply that uniform comparison, not merely an average improvement on a chosen collection of examples.

Admissibility is a filter, not a complete ranking. There can be many admissible estimators, just as our coin example suggests. Two risk curves may cross. Decision theory offers two particularly important ways to summarize those curves without pretending the crossing has disappeared.

## Bayes risk: average before the sample

The first summary averages risk across parameter values using a prior distribution. This is called Bayes risk. If a prior assigns probabilities to plausible theta values, then integrating the frequentist risk function against the prior gives the expected loss of the procedure before the data arrive.

There is a useful equivalence here. We can first average loss across sampling outcomes at each fixed theta and then average across the prior. Or we can first draw the data from the joint prior-predictive distribution, compute a posterior, and choose a posterior-loss-minimizing action for each observation. Under standard integrability conditions, the two orders give the same overall expectation. That is the sense in which choosing a posterior Bayes action at each possible observation yields a Bayes decision rule before observing data.

Consider again the coin with four flips. Give p a uniform prior on zero to one. If the sample has three heads and one tail, the posterior is Beta four, two. Under squared-error loss the Bayes estimate is its mean, four sixths, or two thirds. It lies closer to one half than the raw sample fraction three quarters. The shift reflects averaging uncertainty about p under the prior, not an algebraic correction demanded by unbiasedness.

Another prior would give another Bayes estimate. This is not a defect in the derivation. A prior is part of the average-risk criterion and changes how risks at different parameter values are weighted. For squared-error loss with a Beta alpha, beta prior and n Bernoulli observations, the posterior mean is s plus alpha divided by n plus alpha plus beta. We can verify this from conjugacy, but its decision-theoretic significance is that it minimizes average mean squared error under the specified joint model.

The word Bayes here does not require a philosophical commitment about whether a parameter is physically random. A frequentist may use a prior distribution as a mathematical weighting device for risk comparisons or as a way of constructing candidate procedures. Whether that weighting is appropriate to a real application is a separate question.

## Minimax: guard against the worst parameter

A second criterion asks how badly a rule could perform at the least favorable parameter value. Its worst-case risk is the supremum of the risk curve across theta. A minimax rule minimizes that supremum. Instead of weighting worlds by a prior, we refuse to give one world a free pass because we believe it unlikely.

We can solve a complete minimax problem without any observed data. There are two equally possible states, call them A and B, and two actions, also A and B. Choosing the wrong action incurs loss one. Suppose we are allowed to randomize: choose action A with probability q and B with probability one minus q.

If the true state is A, we are wrong with probability one minus q, so the risk is one minus q. If the true state is B, we are wrong with probability q, so the risk is q. The worst-case risk is the larger of these two numbers. It is minimized when they are equal, at q equal to one half. The minimax value is one half. By contrast, any deterministic choice has worst-case risk one.

This is a legitimate use of randomization: not to improve posterior expected loss for a fixed known posterior, but to balance risk across states before the adversarially least favorable state is known. It is the same mathematics that connects minimax theory to zero-sum games.

Now give the two states equal prior probability. Whatever randomized action we take, the average error probability is one half. Hence the Bayes risk under that uniform prior is one half. Since every rule has worst-case risk at least its average risk under any prior, no rule can have worst-case risk below one half. Our fair randomized rule attains one half. The Bayes lower bound and the achievable upper bound meet, certifying minimax optimality.

That proof method generalizes. An arbitrary prior gives a lower bound on the minimax risk, because an average cannot exceed a supremum. A particularly useful prior for which the lower bound is sharp is called least favorable. Finding one can prove a minimax theorem, though in more difficult models it may require a limiting sequence of priors rather than one ordinary finite distribution.

## A subtle relationship with admissibility

Bayes rules and admissibility are related but not synonymous. In many finite problems, a Bayes rule with respect to a prior that places positive weight on every state, and with finite risk, is admissible: if another rule improved risk somewhere without worsening it anywhere, the prior average would strictly improve, contradicting Bayes optimality. In a continuous parameter space, the same one-line argument is not automatic, because a strict improvement at a single point can have prior probability zero. Additional regularity or a stronger theorem is needed.

Conversely, being minimax does not automatically make a rule admissible. One rule can have the smallest possible worst-case risk and still be dominated by another that lowers risk in some easier worlds without raising the maximum. There is no contradiction: the minimax criterion only records the height of the highest point of the risk curve, whereas admissibility inspects the whole curve.

Imagine a minimax rule whose risk equals one unit at one parameter value and is one half everywhere else. If we find another rule with risk still one at that troublesome value but less than one half elsewhere, it has the same worst-case risk and dominates the original. The numbers illustrate the logical possibility; whether such risk profiles arise depends on the statistical model. The distinction between scalar optimality and full-function comparison is general.

## Prior robustness and the question we actually face

Which criterion should an analyst use? An average-risk criterion is suited to settings where a prior model reasonably describes the relative importance or prevalence of parameter values. A minimax criterion is attractive when worst-case guarantees are central. Admissibility prevents avoidable inefficiency but may leave a large collection of candidate rules. Reporting several risk curves can be more informative than announcing that one estimator has a single best label.

There are also competing losses. Squared error gives very different weight to a rare large mistake than absolute error. A procedure that is good for point estimation need not be good for predicting new observations, selecting a policy, or estimating a tail probability. In applications, a defensible loss function is as essential as a defensible probability model.

The coin example illustrates the result. The sample fraction has low risk near the extremes. The constant one-half estimator has zero risk at its center. A Bayes estimator uses a chosen prior to trade those strengths against each other. A minimax estimator controls the largest risk over all allowed p. And admissibility tells us whether one rule is simply wasted effort because another is no worse anywhere.

Statistical decision theory does not erase value judgments by hiding them in mathematics. It makes them visible. We choose what errors cost, how worlds are weighted or protected, and which observations are available. Once these choices are made, mathematics can prove that a rule meets the stated criterion. The hard part of using the result is being precise about which criterion we meant to optimize.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a decision rule \(\delta:\mathcal Y\to A\) and loss \(L\):
\[
R(\theta,\delta)=\mathbb E_\theta L(\theta,\delta(Y)),\quad
r_\pi(\delta)=\int R(\theta,\delta)\,\pi(d\theta),\quad
R^*(\delta)=\sup_{\theta\in\Theta}R(\theta,\delta).
\]
An admissible rule is not dominated: there exists no \(\delta'\) with \(R(\theta,\delta')\le R(\theta,\delta)\) for every \(\theta\), and strict inequality at some \(\theta\).

**Coin with four trials.** For \(S\sim\mathrm{Binom}(4,p)\):
\[
R(p,S/4)=p(1-p)/4,\qquad R(p,1/2)=(p-1/2)^2.
\]
At \(p=1/2\), risks are \(1/16\) and \(0\); at \(p=0\), they are \(0\) and \(1/4\). For a \(\mathrm{Beta}(\alpha,\beta)\) prior, squared-error Bayes rule is \(\delta(S)=(S+\alpha)/(4+\alpha+\beta)\).

**Clipping and domination.** For \(\Theta=[0,1]\), \(\Pi_{[0,1]}(x)=\min(1,\max(0,x))\). For any \(\theta\in\Theta\), \(|\Pi_{[0,1]}(x)-\theta|\le|x-\theta|\). Squared loss improves pointwise; strict risk improvement requires positive probability of a strict pointwise improvement.

**Two-state minimax.** With no data and zero-one mismatch loss, mixed rule \(\delta_q\) that chooses action A with probability \(q\) has risks \((1-q,q)\). Thus \(\min_{q\in[0,1]}\max(q,1-q)=1/2\). For every prior \(\pi\), \(\inf_\delta \sup_\theta R(\theta,\delta)\ge\inf_\delta\int R(\theta,\delta)\pi(d\theta)\); equality holds for uniform prior and fair randomized rule here.

**Exercises and solutions.** (1) If \(p=1/4\), compare the sample-fraction and constant-one-half risks. *Sample: \(3/64\); constant: \(1/16\). The sample wins.* (2) In the two-state problem what is worst-case risk for \(q=.7\)? *Seven tenths.* (3) Does being minimax prove that no rule dominates yours? *No. Several rules may share the same maximal risk.* (4) Does one example of smaller observed error establish dominance? *No. Dominance compares expected risk for every permitted parameter value.*

### Sources and further reading

- William Fithian, Berkeley STAT 210A, *Statistical Decision Theory*: https://www.stat.berkeley.edu/~wfithian/courses/stat210a/models.html
- Lawrence D. Brown and others, standard decision-theoretic treatment in *Theory of Point Estimation* by Lehmann and Casella.
- Related existing lectures: `probability-measure:021000` (estimator bias and variance); `game-theory:001000` (minimax strategies, when installed).
