# 012000 - Concentration Beyond IID: Bounded Differences, Martingales, and Dependence

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** conditional expectation, martingales, independent variables, and elementary exponential inequalities. **Theme:** dependent outputs can concentrate when their dependence is controlled through the right representation, but large sample counts alone prove nothing.

<!-- BEGIN SPOKEN LECTURE -->

# Concentration Beyond IID: Bounded Differences, Martingales, and Dependence

Imagine a randomized scheduling algorithm that assigns tasks to workers. It draws thousands of random choices, produces one final schedule, and reports how many tasks finish on time. You would like to claim that the performance of the randomized schedule is usually close to its expected performance. But a schedule is not a sum of thousands of independent outcomes. One random choice may affect later assignments, and a single delayed task can change the result for several other tasks.

There is an important distinction here. The random inputs to an algorithm may be independent even when its outputs, intermediate states, and final performance are strongly dependent. Conversely, taking many readings from the same hidden environmental condition may produce data that are genuinely dependent at the input level. Different concentration theorems address these different situations.

Concentration means a quantitative bound on the probability that a random quantity deviates from a reference value, often its expectation. A law of large numbers tells us about a limit under certain assumptions. A concentration inequality tells us how a particular finite collection of randomness behaves at a chosen tolerance and confidence level. To make the latter claim, we need to know what perturbations the system can tolerate and what assumptions govern its dependence.

## An independent input can produce a dependent output

Suppose a scheduler receives one hundred independently generated random priority labels. From those labels it builds an entire schedule. Every task's start time depends on several labels, so the start times are not independent random variables. Nonetheless, the final total number of late tasks is a single function of the one hundred independent inputs.

Assume that changing one priority label while keeping all the others fixed can change the total number of late tasks by at most two. That is a stability property of the algorithm. It makes no claim that the final task outcomes are independent. It says only that the effect of perturbing one primitive random input is bounded.

The method of bounded differences turns such stability into a concentration inequality. For each independent input, provide a worst-case bound on how much changing that input can change the final numerical output. If these bounds are small compared with the total tolerance of interest, then large deviations of the output from its mean are exponentially unlikely.

This is already a useful conceptual extension. We are no longer averaging independent task-level observations. We are studying an arbitrary function of independent random ingredients. It might be a combinatorial optimum, a graph statistic, an algorithm's running cost, or a prediction score. Dependence among components of the output is allowed because the proof operates on the independent ingredients underneath them.

## Revealing inputs one at a time

How can we prove a statement about a complicated function without computing its full distribution? Reveal the random labels one by one. Before any labels are visible, the best prediction of the final score is its unconditional expectation. After the first label is revealed, update the expected score using that information. After the second, update again. Continue until all the labels are known. The final prediction is the actual score.

The sequence of these evolving conditional expectations is a martingale. At each step, the expected next prediction, given everything revealed so far, equals the current prediction. This is simply the defining property of conditional expectation applied to a growing information set.

Now consider the increment from one prediction to the next. It measures the effect of revealing one additional label on what we expect the final score to be. If changing the value of that label can alter the final score by at most two while the other inputs are fixed, and the unrevealed inputs remain independent of the revealed ones, then the conditional range of that martingale increment has width at most two.

That is the key bridge from algorithmic stability to probabilistic concentration. We do not bound the final score by analyzing all combinations of labels separately. We bound one increment at a time, and we use the martingale's zero conditional mean to control the accumulation of fluctuations.

For a general function of n independent inputs, let the bound for input i be called c sub i. The bounded-differences inequality says that the chance of the output exceeding its expectation by at least t is no more than the exponential of minus twice t squared divided by the sum of the squared c values. There is a corresponding lower-tail inequality, so a two-sided probability bound includes a factor of two.

The exact constants belong on the companion page, but the scale is intuitive. If each of a hundred independent random choices can change a score by at most two, the sum of the squared change bounds is four hundred. A deviation much larger than the square root of that total becomes increasingly improbable. The theorem makes this relationship explicit rather than leaving it as a heuristic.

## Why the exponential proof works

The proof combines the revealed-information martingale with an elementary fact about bounded, mean-zero random variables. If such a variable lies in an interval of length c, its conditional exponential moment can be bounded by an exponential whose exponent grows quadratically with the chosen scale and with c. This is a conditional form of Hoeffding's lemma.

Apply that bound to the first martingale increment. Then condition on the information available after the first reveal and apply it to the next increment. Repeat through all input variables. The conditional expectations telescope, leaving an upper bound on the exponential moment of the total difference between the final score and its mean.

Finally, Markov's inequality turns an exponential moment bound into a tail probability bound. We are free to choose the exponential scale. Optimizing that scale yields a negative exponent proportional to the square of the desired deviation divided by the sum of the squared sensitivity bounds.

There are three crucial ingredients, and each has a job. The conditional expectation sequence turns one complicated output into predictable increments. Independence of primitive inputs justifies the bounded conditional ranges from the replacement-stability assumption. The exponential inequality translates bounded increments into a probability tail. If we lose one ingredient, the theorem cannot simply be quoted unchanged.

## A counterexample to counting observations

Suppose a hundred sensor readings all copy one hidden binary variable. On a good day every sensor reports one; on a bad day every sensor reports zero. Assume good and bad days each occur with probability one half. The average of the hundred sensor reports equals that hidden variable exactly.

The average is therefore zero or one, each with probability one half. It never lies close to one half. Adding another hundred perfectly correlated sensors does nothing to improve the average. A claim that the average concentrates as the number of sensors grows would be false, because the number of independent sources of randomness has not grown.

Why can we not force this example into the bounded-differences theorem by calling the hundred observed sensor values one hundred inputs? Because those observed values are not independent. If we instead describe the true independent primitive input as the single hidden binary variable, changing that one variable changes the average by one. The theorem's scale correctly recognizes that there is effectively just one random choice.

This is a valuable modeling diagnostic. Many systems present a large number of correlated observations but only a small number of independent environmental conditions, subjects, shifts, sites, or experimental units. Statistical uncertainty should reflect the structure of replication, not merely the number of rows in a data table.

## Bounded differences versus martingale differences

There is another setting where the randomness is genuinely sequential. At time one a random decision changes the distribution of time two; time two changes time three; and so on. We may not be able to represent the observed states as independent primitive inputs with a simple coordinatewise stability bound. But we may still be able to write a martingale whose increments are bounded after conditioning on the past.

The Azuma–Hoeffding inequality applies to martingales with almost-surely bounded increments. It produces sub-Gaussian tails for the total martingale change. The word martingale matters: the increments must have conditional mean zero with respect to the specified filtration. Bounded random increments with an accumulating predictable drift are not automatically covered by the same centered result.

For a real process, we often separate each new observation into a predictable conditional mean and a mean-zero innovation. The sum of innovations forms a martingale under suitable integrability conditions. Concentration of that martingale controls the unpredictable part. It does not bound the drift unless the drift is separately controlled.

Consider a gambler who earns one unit per winning step and loses one per losing step, with conditional probabilities depending on the past. If the game is fair given the current information, cumulative gains form a martingale. If the game has a predictable advantage on every step, gains need not be centered, even though individual changes remain bounded. A concentration bound around the unconditional zero baseline would then be answering the wrong question.

The distinction also appears in learning systems. An adaptive algorithm may choose an action based on previous outcomes. The reward observation can be written as its conditional expectation plus noise. Martingale concentration can control the accumulated noise under appropriate boundedness and filtration hypotheses, while the choice-dependent conditional expectations remain part of the performance analysis.

## Variance-aware bounds and when scale improves

Worst-case increment sizes can be conservative. Imagine most random increments are almost always zero, with rare moderate changes. A bound based only on the maximum possible size ignores this structure. Variance-aware martingale inequalities, including Freedman's inequality, incorporate the sum of conditional variances along with a bound on positive increments.

The sum of conditional variances is predictable: at each time, its next contribution is determined from the information available before that increment occurs. That distinction matters because we are not allowed to replace an unknown variance process with a favorable random realization after the fact without accounting for the selection.

In the common one-sided version, the probability that a martingale reaches a threshold while its predictable quadratic variation stays below a given budget is controlled by an exponential bound involving both the variance budget and a maximum increment. In regimes with small conditional variance, that can be much sharper than a worst-case bound based only on increment magnitudes.

But sharper bounds still require the right process and hypotheses. They do not turn an arbitrary drifting or dependent sequence into a martingale. The proof has to identify the conditional mean-zero increments, the upper bound on their size, and the quantity used as the variance budget.

## Markov dependence and effective sample size

Return to a system where successive observations are states of a Markov chain. Even after the chain has reached a stationary distribution, adjacent states may be correlated. The variance of the average contains covariance terms involving every time lag. If these covariances decay slowly, the average can be much noisier than an average of independent samples of the same marginal distribution.

A mixing condition can control those covariance terms or support a concentration inequality, often with constants depending on a mixing time or spectral gap. The details vary across theorems: reversibility, state-space structure, bounded functions, starting distribution, and sometimes regularity assumptions all matter. It is unsafe to take an iid bound and quietly replace n by an informal guess of effective sample size without specifying what has been proved.

A long chain with a narrow transition bottleneck provides the intuition. It may produce thousands of near-identical observations inside one region before transitioning to another. Even if the stationary weights of the regions are balanced, short runs can be badly biased toward the starting region. The correct concentration rate depends on how readily the chain moves between regions.

This also explains why a stationary marginal distribution is not a certificate that time averages are accurate at a chosen finite duration. Stationarity describes the law at one time. Concentration of averages depends on the joint law over many times. The second contains much more information than the first.

## Many claims at once and the union bound

Suppose a researcher evaluates a thousand fixed candidate models on the same independent validation sample. Each model's empirical score may have a valid concentration bound. But if the researcher selects the model with the best observed score, a single-model bound is no longer automatically the right guarantee for that selected model.

One safe approach for a finite class is to guarantee that every fixed candidate's estimation error is small simultaneously. The union bound says that the probability of any one of the candidate-specific error events is no greater than the sum of their individual probabilities. This conclusion does not require independence between the events of model error. It only requires valid bounds for each event.

For the familiar bounded independent-loss setting, the result adds a logarithmic dependence on the number of candidates to the required sample size. If there are a thousand models, the penalty is not generally a thousandfold increase in the sample size; it appears through a logarithm. The exact tradeoff also depends on the tolerance and confidence level.

The class must be specified appropriately for this reasoning. If a researcher invents arbitrarily many new hypotheses after inspecting the validation outcomes, they cannot pretend that those choices were among a fixed small set all along. Adaptive data analysis has its own tools and assumptions, including fresh holdout data, stability, and privacy-based generalization results in some settings. A fixed-class union bound does not by itself solve arbitrary adaptive reuse.

## The last distinction: stability of inputs and stability of the claim

One might hear that bounded differences proves randomized algorithms are reliable. That is too broad. The theorem proves concentration around the algorithm's expected output under the specified independent-input model and sensitivity bounds. It does not say the expected output is good. An algorithm can perform terribly on average and concentrate very sharply around that bad performance.

Nor does it prove that the mathematical model matches deployment data. A scheduler may be stable under independent synthetic priorities and fail badly when real workloads contain coordinated surges. The concentration theorem survives intact as a statement about the synthetic random experiment. Its relevance to the real system depends on whether that experiment captured the important sources of variability.

There is a third issue: a small change in one input may have a small effect on a metric but a large effect on some unmeasured outcome. A bound on the number of late tasks does not automatically bound fairness across workers, safety of critical jobs, or worst-case delay. Sensitivity has to be proved for the quantity actually claimed.

The mathematics gives us a useful procedure. Identify the primitive random inputs and determine which are independent. Express the output as a function of them, or construct an adapted martingale. Derive bounds on how much a revelation can change a conditional expectation. Apply a theorem with those precise assumptions, and keep separate the expected quality of the system and the model's external validity.

The central lesson is that dependence is not a single obstacle that always destroys concentration. Some outputs are dependent because they share independent underlying causes, and bounded differences handles them elegantly. Some observations are dependent because they share one hidden cause, and counting more observations adds no information. Sequential processes need martingale or mixing arguments. By tracing the actual source of randomness, we can choose the appropriate theorem and know what its conclusion does—and does not—say.


## Interpreting the bound for one real algorithm

Let's make the scheduler's sensitivity calculation numerical. Suppose there are one hundred independent priority labels, and changing any one label can alter the final number of late tasks by at most two. The sum of the squared sensitivity bounds is then four hundred. The two-sided bounded-differences bound for a deviation of thirty tasks is twice the exponential of minus four and a half, a little over two percent.

That is a mathematically useful guarantee. But if we ask about a deviation of twenty tasks, the same calculation gives twice the exponential of minus two, more than one quarter. The bound is valid but not especially informative at that threshold. A concentration theorem can give a weak numerical result when the stability constants or sample size are not favorable. We should inspect the actual bound rather than celebrating the appearance of an exponential.

And the bound relies on a genuine global statement about changing one input while keeping the others fixed. A programmer may observe that, in a few test schedules, changing one priority label alters at most two tasks. That does not prove the sensitivity bound over every possible configuration. A carefully chosen adversarial arrangement could produce a cascade in which one change reorders dozens of jobs. If so, the claimed bound fails at its hypothesis, not at its conclusion.

It is often worth proving a weaker bound that is correct rather than importing an optimistic constant from experiments. Sometimes the algorithm can be redesigned to make a useful sensitivity theorem true. That is a direct connection between probabilistic guarantees and software or mechanism design: stability is not merely something we measure after implementation, but sometimes something we deliberately build into it.

## Dependence is more than pairwise correlation

A practical temptation is to calculate a correlation matrix and conclude that small pairwise correlations justify an independence-based concentration theorem. They do not. Pairwise independence is not, in general, mutual independence. And small linear correlations need not control nonlinear dependencies, common rare shocks, or the joint tails that matter for an extreme event.

For a simple illustration of pairwise independence without mutual independence, draw two independent fair bits and make a third bit their exclusive-or. Any pair is independent, but the three together satisfy a deterministic parity constraint. If we only inspect pairwise tables, the shared structural relation is invisible. Some estimates for the mean still work under pairwise independence, but a theorem requiring full independence of primitive coordinates cannot be invoked merely from pairwise checks.

In time series, a correlation that decays at the first few lags also does not automatically establish a sufficiently fast mixing condition. Rare regime switches, long memory, and nonstationarity can cause dependencies that a short correlation window misses. Concentration under dependence is therefore a structural question, not a single-number diagnostic.

## Variance and stopping under adaptive observation

Imagine that a team monitors a model's validation error and stops collecting data as soon as the reported confidence interval looks favorable. A fixed-sample concentration interval is not generally guaranteed to retain its advertised coverage under an arbitrary data-dependent stopping rule. The stopping decision has used the very random fluctuations being measured.

One response is to construct an anytime-valid process: for example, a nonnegative supermartingale designed so that a suitable maximal inequality controls the probability of ever crossing a threshold. Another response is to prespecify a fixed sampling plan or use independent holdout data. Which method is appropriate depends on the information revealed and the desired guarantee.

This is closely related to optional stopping, but it is not enough to say that a martingale stays fair. An expectation identity at a bounded stopping time and a simultaneous coverage guarantee over every possible stopping time are different mathematical statements. The second needs a maximal or time-uniform argument and often pays a price relative to a one-time bound.

The larger lesson is that a probability inequality describes an experiment, including its sampling and selection rules. Changing those rules after seeing data changes the experiment. Explicit filtrations and conditional expectations help us formulate what information the procedure is allowed to use, so that the chosen inequality answers the actual question.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(X_1,\dots,X_n\) be independent and \(f:\prod_i\mathcal X_i\to\mathbb R\) measurable. Suppose for every coordinate \(i\), every pair \(x,x'\) differing only in coordinate \(i\),
\[
|f(x)-f(x')|\le c_i.
\]
Then McDiarmid's bounded-differences inequality gives
\[
P(f(X)-Ef(X)\ge t)\le\exp\left(-\frac{2t^2}{\sum_i c_i^2}\right),
\quad
P(|f(X)-Ef(X)|\ge t)\le2\exp\left(-\frac{2t^2}{\sum_i c_i^2}\right).
\]

**Doob martingale construction.** Set \(M_i=E[f(X_1,\dots,X_n)\mid X_1,\dots,X_i]\), \(M_0=Ef(X)\). Then \(M_i\) is a martingale and, conditional on \(X_1,\dots,X_{i-1}\), the essential range of \(M_i-M_{i-1}\) has length at most \(c_i\). Conditional Hoeffding's lemma yields \(E[e^{\lambda(M_i-M_{i-1})}\mid\mathcal F_{i-1}]\le e^{\lambda^2c_i^2/8}\). Iterate and optimize Markov's exponential bound.

**Azuma–Hoeffding.** For martingale differences \(D_i\) with \(|D_i|\le b_i\) almost surely,
\[
P\!\left(\sum_iD_i\ge t\right)\le\exp\left(-\frac{t^2}{2\sum_i b_i^2}\right).
\]
If only the interval width is bounded, the sharper Hoeffding-lemma constant applies.

**Freedman (one-sided form).** If \(D_i\le b\) a.s., \(E[D_i\mid\mathcal F_{i-1}]=0\), and \(V_k=\sum_{i\le k} E[D_i^2\mid\mathcal F_{i-1}]\), then for \(t,v>0\),
\[
P(\exists k:\ M_k-M_0\ge t,\ V_k\le v)
\le\exp\!\left(-\frac{t^2}{2(v+bt/3)}\right)
\]
under the standard bounded-increment form.

**Perfect dependence counterexample.** For \(X_i=Z\sim\mathrm{Bernoulli}(1/2)\), \(n^{-1}\sum X_i=Z\). No shrinkage toward its expectation occurs with n.

**Finite model class.** For m fixed predictors with iid losses in [0,1], Hoeffding plus union bound gives
\[
P\!\left(\max_{h\in H}|\hat R(h)-R(h)|>\varepsilon\right)
\le2|H|e^{-2n\varepsilon^2}.
\]
This is a simultaneous bound over a fixed finite class, not an unrestricted adaptive-data-analysis result.

### Exercises with answers

1. **Bounded differences.** If changing any one of n independent inputs changes f by at most 1, give the two-sided tail bound. **Answer:** \(2\exp(-2t^2/n)\).
2. **Shared source.** Why do 10,000 identical copies of one fair bit not concentrate near one half? **Answer:** their average is exactly the original bit.
3. **Filtration.** For martingale differences, what does mean-zero require? **Answer:** zero conditional expectation given the past information, not merely zero unconditional mean.
4. **Selection.** Can two dependent candidate-error events still be union-bounded? **Answer:** yes; the union bound does not require independence among events.
5. **Performance.** Does concentration around expectation imply a high-performing algorithm? **Answer:** no; the expectation itself may be poor.

### References

- Colin McDiarmid, *Concentration* (1998), bounded differences and martingale method.
- Daniel Paulin, *Concentration Inequalities for Markov Chains by Marton Couplings and Spectral Methods* (2015), dependence and mixing assumptions.
- MIT OpenCourseWare 18.175, *Theory of Probability*, large deviations, martingales, and Markov chains.
