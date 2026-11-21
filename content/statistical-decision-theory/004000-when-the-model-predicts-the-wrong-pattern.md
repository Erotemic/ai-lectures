# 004000 — When the Model Predicts the Wrong Pattern

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** conditional probability, sampling distributions and basic Bayesian inference. **Theme:** a posterior can be computed correctly under a model that describes the observed data badly.

<!-- BEGIN SPOKEN LECTURE -->

# When the Model Predicts the Wrong Pattern

Suppose a system passes exactly six of twelve tests. We could place a Beta prior on its success probability, update with the six successes and six failures, and report a posterior concentrated around one half. All the arithmetic could be correct. But now imagine that the results occurred in this order: six failures in a row, followed by six successes in a row.

That pattern should make us curious. Were the tests performed in two different environments? Did the system change halfway through? Is there a warm-up effect? Did a single hidden cause govern several tests at a time? A binomial model of twelve independent, exchangeable outcomes discards the ordering, so it cannot answer these questions by the count alone. Our fitted model can summarize the success rate and still miss a feature of the process that is important for prediction or decision-making.

Bayesian model checking asks a simple question: if our model were used to generate data like the data we observed, what patterns would we see? The work is a combination of probability, simulation, and criticism. It starts before fitting, continues after fitting, and can motivate a new model without pretending that a single diagnostic certifies truth.

## A conditional surprise hidden by the count

Begin with a fact we can calculate exactly. Under independent Bernoulli trials with a shared success probability p, every particular sequence with six successes and six failures has probability p to the sixth times one minus p to the sixth. Conditional on the total count being six, all such sequences are therefore equally likely, regardless of p.

How many are there? Choose the six positions of the successes among twelve: twelve choose six, or nine hundred twenty-four sequences. Exactly two of those sequences have just two runs, one run of failures and one of successes: all failures then all successes, or the reverse. Therefore, conditional on six successes and six failures, the probability of exactly two runs is two divided by nine hundred twenty-four, about two tenths of one percent.

We have found a striking conflict between the observed ordering and the simplest exchangeable model. Notice what we did not do. We did not compute a posterior probability that the model is false. We computed the probability of a particular kind of pattern conditional on the observed count, under one model. If we selected the pattern after seeing the data and tried many possible surprises, the apparent extremeness needs its own interpretation. But it is still a strong reason to inspect dependence, time trends, and differences among the tests.

This calculation also teaches us how to choose useful discrepancy statistics. If we only compare overall success counts, the model may fit reasonably. If we compare the number of runs, the longest consecutive failure streak, or separate success rates before and after the midpoint, a defect in the exchangeability assumption becomes visible. The diagnostic should reflect the scientific question, not just a generic goodness-of-fit number.

## Prior predictive checks: before fitting anything

Bayesian analysis introduces a prior distribution over model parameters. A prior predictive check draws a parameter from that prior and then draws a hypothetical dataset from the likelihood. Repeating the process shows what the complete model regards as plausible before seeing the observations.

Take a simple example. Suppose we use a Beta distribution with both shape parameters equal to one as a prior for a Bernoulli success probability. That is a uniform prior on p between zero and one. If we draw p once and then simulate twelve Bernoulli observations at that p, the distribution of the success count is uniform over zero through twelve. The claim follows from the beta-binomial calculation: each count has probability one thirteenth.

That is very different from the binomial distribution with p fixed at one half, which is most concentrated around six. The prior predictive model generates more all-success and all-failure datasets than a fixed-fifty-percent model because it allows p itself to vary from one simulated dataset to another.

This distinction helps prevent a common confusion. A hierarchical or Bayesian mixture model may create dependence among observations marginally, even when they are conditionally independent given a parameter. In the Beta–Bernoulli example, knowing that several outcomes were successes increases our posterior expectation of p and thereby raises the predictive success probability for later outcomes. The correct predictive check must respect the full generative process, including the prior and which parameters are redrawn at which level.

A prior predictive check can reveal a prior that assigns implausible weight to enormous counts, impossible physical values, near-perfect forecasts, or other artifacts. It cannot be calibrated by the observed data because it is deliberately conducted without conditioning on them. That is its advantage: a prior predictive check can catch problems before the data bend the posterior toward a small region of the parameter space.

## Posterior predictive checks: after fitting

Now fit the model and obtain a posterior distribution for its parameters. To generate one posterior predictive replication, first draw a parameter from the posterior, then draw a new dataset from the likelihood conditional on that parameter. Repeat many times. Compare a statistic of these replicated datasets with the same statistic of the observed dataset.

For a simple binomial outcome count, we might ask whether the observed number of successes lies near the center of the replicated counts. For the ordered-test example, we might compare the longest run of identical results. For a regression model, we might look at residual tails, heteroscedasticity, the relationship between residuals and fitted values, or patterns in time. A good diagnostic statistic must be sensitive to a feature that the model could plausibly get wrong.

The replicated datasets are not generated from a parameter fixed at its posterior mean. They average over parameter uncertainty by drawing a fresh parameter from the posterior each time. If we replace every parameter by a single point estimate, we may underestimate the variability the model predicts. This becomes especially important in small samples or hierarchical models.

One sometimes summarizes a posterior predictive check by the fraction of replicates for which a discrepancy statistic is as extreme as the observed discrepancy. It is often called a posterior predictive p-value. It is not generally a uniform frequentist p-value under the null model. The observed data were used to form the posterior and are compared against predictions informed by those same data. That double use often makes the procedure conservative for some discrepancies, though its behavior depends on the setup. The graph of observed and replicated patterns can be more informative than treating the resulting fraction as a universal accept-or-reject threshold.

A model can pass the checks we perform while remaining wrong in ways we did not test. There is no finite collection of discrepancy statistics that proves a complex model is true. The point of checking is to look for consequential mismatch and improve our understanding of the data-generating process.

## Checking the model is not selecting the model

Suppose two models both fit the observed data, but one predicts future data better. We need another notion of evaluation: out-of-sample predictive performance. In Bayesian analysis, a useful quantity is the log probability the model assigns to a held-out observation, after fitting on the training data. Summing such scores gives a measure of predictive performance, with higher values indicating better predictive density assigned to observations that were not used to fit that particular prediction.

Leave-one-out cross-validation repeats this idea: fit on all observations except one and evaluate the omitted observation, then aggregate across omissions. For a moderate dataset this might require many full posterior fits. Approximate methods such as Pareto-smoothed importance sampling reuse the original posterior draws and correct their weights. They are computational devices, not magic identities. Influential observations can produce unstable weights, which is why the tail diagnostic and possible refitting are part of the method.

What is the difference between this and a posterior predictive check? A posterior predictive check asks whether the fitted model reproduces chosen structural features of the data. Cross-validation asks how well the model predicts observations it did not fit. A model can outperform its competitors predictively and still have a conspicuous structural defect. Conversely, a model that reproduces several hand-picked summaries may predict poorly on genuinely new data.

Both assessments are conditioned on the modeling purpose. If the goal is to forecast tomorrow's demand, we should validate predictions in a way that resembles forecasting tomorrow, perhaps holding out future time blocks instead of randomly chosen individual observations. If the goal is to understand an intervention, ordinary predictive accuracy may not establish causal validity. When data are clustered, holding out one row may leak information from the same cluster through other rows; holding out whole clusters may be the appropriate target.

## Monte Carlo error versus model error

Predictive checking is often implemented by simulation. This introduces another source of uncertainty. If we generate only a small number of replicated datasets, a displayed tail proportion may fluctuate noticeably simply because we did not simulate enough. Increasing the simulation count reduces Monte Carlo error. It does not remove errors in the likelihood, prior, data collection mechanism, or choice of diagnostic statistic.

Likewise, uncertainty in posterior sampling is distinct from uncertainty due to misspecification. A beautifully converged Markov chain can sample the wrong model with extreme numerical accuracy. A broken sampler can produce plausible-looking plots for a good model. These two failure modes require different tests. In future lectures, we will examine simulation algorithms and their diagnostics separately from posterior predictive criticism.

The difference between parameter uncertainty and model uncertainty is equally important. A narrow posterior interval conditional on a model can coexist with substantial uncertainty about whether the model should have been used. One can place priors over alternative models, average predictions, or compare predictive performance. But the set of models under consideration may itself omit the true process, and model averaging over an incomplete list does not create it.

## Revisiting twelve tests

Return to our twelve observations, six failures followed by six successes. Under a binomial model with a fixed success probability, their count looks ordinary when p is around one half. Under that same model, conditional on the count, the two-run ordering is rare. That tension points toward a question about temporal dependence or changing conditions.

We could propose a two-regime model, a hidden-state Markov model, a random effect shared by adjacent tests, or a drift in success probability. Which is appropriate depends on how the tests were run and what future prediction or action is needed. We should not select a complicated mechanism solely because it can recreate one surprising sample. We should ask for independent evidence, meaningful covariates, and predictive checks designed for the resulting model.

The lesson is not to distrust Bayesian inference. It is to understand the scope of what inference proves. Given a prior and likelihood, the posterior follows by probability calculus. Whether that posterior describes the physical process depends on the plausibility of the model and whether it survives relevant empirical challenges. Posterior predictive checking supplies one disciplined way to ask those challenges, and cross-validation supplies another. Neither replaces the other.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Prior and posterior prediction.** For prior \(\pi(\theta)\) and likelihood \(p(y\mid\theta)\),
\[
p(y^{rep})=\int p(y^{rep}\mid\theta)\pi(d\theta),\quad
p(y^{rep}\mid y)=\int p(y^{rep}\mid\theta)\pi(d\theta\mid y).
\]
The replication has the same design as the original data; in a hierarchical model define exactly which latent variables or groups are newly drawn.

**Ordered twelve-trial example.** Under iid Bernoulli with fixed \(p\in(0,1)\), conditional on \(S=6\), each of the \(\binom{12}{6}=924\) sequences is equally likely. Exactly two sequences have \(2\) runs: \(000000111111\) and its reverse. Thus
\[
P(R=2\mid S=6)=\frac2{924}=\frac1{462}\approx0.0021645.
\]
This is a *conditional arrangement probability*, not automatically a posterior predictive p-value or a probability that the model is false.

**Beta(1,1) prior predictive.** For \(S\mid p\sim\mathrm{Binom}(n,p)\) and \(p\sim\mathrm{Beta}(1,1)\), integration yields \(P(S=s)=1/(n+1)\), for \(s=0,\ldots,n\).

**Posterior predictive checks and LOO.** A discrepancy \(T(y,\theta)\) may depend on the parameter. A typical posterior predictive tail quantity is \(E_{\theta\mid y}[P(T(Y^{rep},\theta)\ge T(y,\theta)\mid\theta)]\), not generally Uniform(0,1) under repeated sampling. A leave-one-out log score is \(\sum_i\log p(y_i\mid y_{-i})\) under the actual validation design.

**Exercises and solutions.** (1) Conditional on six successes and six failures, are all sequences equally likely under a fixed-p Bernoulli model? *Yes.* (2) What does a posterior predictive check that compares only total successes fail to inspect? *Ordering and dependence.* (3) Why can full-data log likelihood exaggerate predictive accuracy? *The evaluated data helped fit the model.* (4) Does a sampler convergence diagnostic test the likelihood's scientific adequacy? *No.*

### Sources and further reading

- Gelman, Meng and Stern, *Posterior Predictive Assessment of Model Fitness via Realized Discrepancies* (1996): https://www.cs.columbia.edu/~blei/fogm/2019F/readings/GelmanMengStern1996.pdf
- Stan User's Guide, *Posterior and Prior Predictive Checks*: https://mc-stan.org/docs/2_27/stan-users-guide/ppcs-chapter.html
- Vehtari, Gelman and Gabry, *Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC* (2017): https://stat.columbia.edu/~gelman/research/published/loo_stan.pdf
- Related existing lecture: `probability-measure:008000` (Bayesian inference and calibration).
