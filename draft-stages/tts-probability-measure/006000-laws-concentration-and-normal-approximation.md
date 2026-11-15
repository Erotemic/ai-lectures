# 006000 - Large Numbers, Concentration, and Normal Approximation

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** expectation, variance, independent samples, and probability limits. **Theme:** how averages stabilize; how strong, weak, finite-sample, and distributional claims differ.

<!-- BEGIN SPOKEN LECTURE -->

# Large Numbers, Concentration, and Normal Approximation

A manufacturing line produces components, and each component is either acceptable or defective. Management wants to know the defect rate. Inspecting every component would be expensive, so an engineer samples a hundred and finds six defects. Is the underlying rate six percent? How far might that estimate be from the truth? If the engineer samples a thousand, does the uncertainty become ten times smaller? And what if defective components arrive in bursts because a machine occasionally drifts out of calibration?

These questions belong to different theorems. A law of large numbers tells us whether an average approaches its expected value as the sample grows. A concentration inequality bounds the probability of a sizable error at a particular sample size. The central limit theorem describes a normalized distribution of errors under additional conditions. These results are related, but none should be substituted for the others without checking its assumptions.

To understand them, we will work with repeated binary measurements and then change the model deliberately. The same change that makes a formula easy to prove can also expose where it fails. The goal is not to memorize three slogans about large samples. It is to know what each theorem certifies and which features of the experiment make that certification credible.

## What an average is averaging

Let a component have an indicator X that equals one if defective and zero otherwise. Suppose each inspection has defect probability p. The expected value of X is p, and its variance is p times one minus p. For a sample of n inspections, the observed defect fraction is the sum of the indicators divided by n.

If the indicators are independent and identically distributed, the expectation of this average is p. Variance behaves differently. Independent fluctuations do not all move together, so their covariance terms vanish. The variance of the sample average is the variance of one indicator divided by n. The standard deviation is therefore the square root of p times one minus p divided by the square root of n.

Notice the square root. Increasing the sample size from one hundred to one thousand divides the standard deviation by the square root of ten, which is about three point two, not ten. To reduce a standard error by a factor of ten, under this simple model we need one hundred times as much independent data.

If p were six percent, the standard deviation of a defect fraction from one hundred independent inspections would be about two point four percentage points. That calculation treats six percent as if it were the true p. When p itself is unknown, plugging in the observed fraction gives an estimated standard error, not an exact uncertainty statement. A confidence procedure requires its own construction and coverage analysis, especially when the number of events is small.

Even before proving a theorem, we have exposed two assumptions: that the defect probability is stable and that each observation supplies a fresh independent contribution. If the manufacturing line spends half an hour in a defective state, nearby sampled components may be highly correlated. A thousand inspected pieces might then carry much less information than a thousand independent pieces.

## A probability bound from an average

Let us start with a fact that works for any nonnegative random variable with finite mean. Suppose Z is a nonnegative cost and we want to bound the probability that it exceeds a threshold a. Whenever that event happens, the cost is at least a. Therefore the average cost must be at least a times the probability of the event. Rearranging gives Markov's inequality: the probability of a cost at least a is at most the expected cost divided by a.

The argument is almost embarrassingly simple, which is why it is useful. It requires no normal distribution and no independence. It only requires nonnegativity and a finite expectation. Of course it may be loose. If expected cost is one and the threshold is two, the bound allows as much as one half probability even when the actual chance is a thousandth.

Now apply the same idea to the squared error of a random quantity. Squared error is nonnegative, and its expected value is variance when the center is the true mean. The event that an error exceeds epsilon in magnitude is precisely the event that squared error exceeds epsilon squared. Markov's inequality then gives Chebyshev's inequality: the chance of an error of magnitude at least epsilon is bounded by variance divided by epsilon squared.

This establishes a bridge from average squared fluctuation to tail probability. We have not assumed a bell-shaped distribution. We have used only a finite second moment. It follows that any random variable with small variance around its mean is unlikely to be far from that mean, though Chebyshev often gives a conservative numerical bound.

For the sample average of independent, identically distributed observations with finite variance, the variance shrinks like one divided by n. Thus the probability that the sample mean differs from its true mean by a fixed positive amount is at most a constant divided by n. The right-hand side goes to zero. That proves a weak law of large numbers under these assumptions.

The qualifier weak does not mean unreliable. It describes the mode of convergence: for every fixed error threshold, the chance that the sample mean misses by more than that threshold tends to zero. This is convergence in probability. It is a statement about probabilities at each sample size, not a claim that every realized infinite sequence eventually behaves well.

## The difference between a weak and a strong law

A strong law says something about entire sample paths. Under the classical assumption that observations are independent and identically distributed with finite absolute mean, the running sample average converges to the common expectation almost surely. Apart from a set of infinite sequences having probability zero, a single endless record eventually stays close to the target mean.

Almost sure convergence is stronger than convergence in probability. It does not say the sample average stops fluctuating after a universal number of observations, and it does not give a useful finite-sample threshold by itself. Different sample paths can take very different lengths of time before settling within a desired tolerance.

One reason the stronger theorem is more difficult is that we care about infinitely many sample sizes simultaneously. For a weak law, we bound error probability for a fixed n and let n grow. For a strong law, we ask whether large errors occur infinitely often along one realized sequence. Such a question involves countable intersections and unions of events and can depend on the accumulated probabilities across all sample sizes.

The Borel–Cantelli lemma offers a useful perspective. If the sum of the probabilities of a sequence of bad events is finite, then with probability one only finitely many of those bad events occur. Its proof uses a union bound on the probability that any bad event occurs after a chosen index, followed by a limit as that index grows. No independence is required for this direction.

Chebyshev's simple one-over-n bound does not by itself yield a summable series over every n, so it is not enough to prove the strong law directly by that route. There are more careful arguments, and stronger concentration bounds are available for bounded independent variables. This distinction is a good example of why proving each fixed-sample statement is not automatically equivalent to controlling all sample sizes at once.

The strong law relies on genuine integrability in its standard independent, identically distributed form. Having a formal expression for a population average is not enough if positive and negative contributions fail to give a finite absolute expectation. Heavy-tailed models can invalidate the conclusion or make conventional rates of convergence misleading.

## Concentration gives a finite-sample statement

Return to the defect indicators. They are bounded between zero and one, which provides information that Chebyshev does not fully exploit. For independent bounded observations, Hoeffding's inequality gives an exponentially decreasing upper bound on the probability that the sample average differs from its mean by at least epsilon.

For independent observations all between zero and one, the two-sided probability is at most twice the exponential of negative two times n times epsilon squared. The exact expression belongs in the mathematical companion, but its shape is easy to hear: increase the sample size linearly and the exponent becomes more negative linearly. Errors of a fixed size rapidly become improbable.

Consider a true defect rate of six percent and a hundred independent inspections. How unlikely is an observed fraction at least ten percentage points away from the truth? Hoeffding gives an upper bound of about twenty-seven percent for that two-sided deviation. The bound is guaranteed under its assumptions, but it is not tight here. For a thousand inspections the same ten-point deviation has bound roughly four billionths. The arithmetic describes the general growth of certainty with sample size; it does not certify a real manufacturing process until independence and the stated bounds are justified.

There are more specialized inequalities that use variance or the Bernoulli distribution to improve constants. But the central idea remains: a concentration theorem specifies an event, a probability bound, and the hypotheses under which the bound is valid. It does not assert that the observed data are representative in a sampling-design sense, or that the measured process stayed stationary over the experiment.

How would we choose a sample size in advance? Suppose we want the defect fraction to be within five percentage points of p with at least ninety-five percent probability, under the independent bounded model. Set Hoeffding's upper bound to at most five percent and solve for n. We need n at least about seven hundred thirty-eight. This is a worst-case sufficient condition, not an assertion that smaller samples must fail.

The useful lesson is that a confidence target can be turned into an explicit sample requirement, provided we state the target error and probability separately. A phrase such as “large enough sample” without either quantity does not determine a numerical guarantee.

## A worked planning comparison

We can use the defect example to see why different tools lead to different answers. Suppose the factory considers two designs for a validation study. In the first, it independently inspects one hundred units chosen across many production shifts. In the second, it inspects one thousand consecutive units from the same shift. The second dataset is larger but may be much more dependent. Under a model with common shift-level drift, the first design could give a more reliable estimate of the across-shift defect fraction. A theorem about independent trials cannot choose between the designs until the replication structure is specified.

Even within the independent design, different mathematical questions require different answers. If the objective is to detect whether the defect rate exceeds a regulatory limit, we may need a one-sided test with explicit false-alarm control. If the objective is a forecast for the next thousand products, parameter uncertainty and potential drift must both be represented. If the objective is a guaranteed maximum estimation error, a two-sided concentration bound may be appropriate. The sample average appears in every calculation, but the target event is different.

A reliable analysis therefore writes down the proposed error event before opening a table of probability inequalities. “Average is close to p” is not a complete specification until close has a numerical meaning, the sample size is fixed, and the event's probability is attached to a defended distributional model. That practice prevents the selection of a theorem merely because it produces the smallest-looking number.

## Normal approximation addresses a different question

A concentration bound tells us that a large deviation is rare. It does not describe the detailed shape of ordinary fluctuations. For independent, identically distributed observations with finite positive variance, the central limit theorem says that the centered sum, divided by its standard deviation, approaches the standard normal distribution in distribution.

If we instead study the sample average, we subtract the population mean and multiply its error by the square root of n divided by the population standard deviation. That standardized quantity becomes approximately normal as n grows. We can then use the normal curve to estimate the probability of landing in a range of standardized errors.

The normal approximation has a different logical form from a law of large numbers. Without standardization, the sample mean concentrates toward a point. After standardization, we magnify its shrinking fluctuations and study the nontrivial shape that remains. A central limit theorem explains approximate probabilities at this fluctuation scale; it is not merely another statement that the sample average approaches p.

For a Bernoulli defect indicator, the standardized sample mean is asymptotically normal whenever p is strictly between zero and one. At small sample sizes, especially when p is close to zero or one, its actual distribution is discrete and skewed. A normal approximation may then be inaccurate. The words as n grows are not a license to use a Gaussian formula after any arbitrary sample size.

One must also distinguish an asymptotic approximation from a guaranteed bound. A normal tail estimate can be much sharper than Chebyshev or Hoeffding when the approximation is valid. But the central limit theorem by itself does not provide a universal finite-n error. Quantitative refinements such as Berry–Esseen inequalities do provide error bounds, under additional moment assumptions, with constants and rates depending on the standardized third absolute moment.

## What dependence does to an average

We should now break independence deliberately. Let a machine be either healthy or unhealthy for an entire shift. If healthy, every component in the shift is acceptable. If unhealthy, every component is defective. Assume the two shift states are equally likely.

Inspect a thousand components from one shift. The observed defect fraction is either zero or one. Its expected value across hypothetical shifts is one half, but increasing the number inspected within that one shift does not make the observed fraction approach one half. All thousand pieces carry information about the same hidden shift state.

Mathematically, every indicator equals the same Bernoulli variable Z. The sample average equals Z, no matter how large n becomes. Its variance remains one quarter rather than shrinking like one divided by n. The weak law based on vanishing variance does not apply because the independence assumption is false.

The counterexample is extreme, but it captures the logic behind effective sample size. If observations share common shocks, common subjects, households, batches, or time periods, their covariance terms matter. The variance of an average involves not only individual variances but also the sum of pairwise covariances. Positive correlations can overwhelm the expected one-over-n improvement.

For dependent processes, there are laws of large numbers and central limit theorems under mixing, ergodicity, or other structural conditions. None follows from merely collecting more data points. A good statistical analysis asks what is independently replicated: individual components, shifts, machines, factories, or days. The experimental unit need not be the same as the row in a data table.

## What heavy tails do to an average

Dependence is not the only failure mode. Consider a symmetric Cauchy distribution, which has a tall center and tails so heavy that the absolute expectation is infinite. The average of independent Cauchy variables has the same Cauchy distribution as an individual variable, after accounting for the common scale. Thus collecting more observations does not concentrate the arithmetic mean around a finite population mean. Such a mean does not exist in the ordinary integrable sense.

This is not a paradox or an exception to a valid theorem. The usual finite-mean hypotheses do not hold. A mathematical model that permits sufficiently frequent enormous values can make the sample average an unstable measure of typical behavior.

Less extreme heavy-tailed distributions may have finite means but infinite variances. Strong laws can still apply for independent, identically distributed observations with finite absolute mean, while the simple Chebyshev variance proof and the ordinary finite-variance central limit theorem do not apply. Alternative stable limits or robust estimation methods may be relevant depending on the tail behavior.

There are also practical dangers in selecting a model only after inspecting the data. If a few extreme observations are discarded as mistakes without a defensible rule, the estimated distribution may be artificially narrowed. On the other hand, blindly averaging quantities with genuinely heavy tails can create enormous estimation error. The correct action is to understand the measurement process and the inferential question.

## Three promises, three assumptions

We can now state the differences in ordinary language. A weak law says the chance of a fixed error tends to zero. A strong law says that with probability one a realized running average eventually approaches the target. A concentration bound says how large an error probability can be at a specified finite n. A central limit theorem says how standardized fluctuations are distributed in the large-sample limit.

All four can be valid for independent bounded Bernoulli trials, but they serve different purposes. If we need a provable finite-n safety guarantee, an asymptotic normal approximation by itself is insufficient. If we need an approximate confidence interval under a well-tested model, a valid concentration bound may be too conservative. If observations are dependent or lack finite moments, the easy textbook versions may be inapplicable.

Return once more to the engineer who sees six defects in a hundred components. The sample fraction is a measurable result. Its interpretation as evidence about a stable p depends on how the components were sampled and how the process behaves. Independent, stable binary trials lead to shrinking variance, concentration inequalities, and normal approximations. Clustered defects require a different model. A change in the machine midway through the shift requires a model of changing probabilities. Large samples solve no problem that the sampling model has failed to describe.

Probability theory earns its power not by promising that every large sample becomes truth, but by letting us identify the exact conditions under which repeated measurements constrain uncertainty. The proof and the assumption are both part of the result.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(X_i\stackrel{\rm iid}{\sim}\operatorname{Bernoulli}(p)\), \(\bar X_n=n^{-1}\sum_{i=1}^n X_i\). Then
\[
E[\bar X_n]=p,\qquad \operatorname{Var}(\bar X_n)=\frac{p(1-p)}{n}.
\]

**Markov and Chebyshev.** For nonnegative integrable \(Z\), \(a>0\):
\[
P(Z\ge a)\le E[Z]/a.
\]
For square-integrable \(Y\),
\[
P(|Y-EY|\ge\varepsilon)\le\frac{\operatorname{Var}(Y)}{\varepsilon^2}.
\]
Applying Chebyshev to \(\bar X_n\) proves convergence in probability when independent identically distributed variables have finite variance.

**Hoeffding.** For independent \(X_i\in[a_i,b_i]\),
\[
P(|\bar X_n-E\bar X_n|\ge\varepsilon)
 \le 2\exp\left(-\frac{2n^2\varepsilon^2}{\sum_i(b_i-a_i)^2}\right).
\]
For all \(X_i\in[0,1]\), this is \(2e^{-2n\varepsilon^2}\), capped at 1. For \(\varepsilon=0.05\) and \(\delta=0.05\), a sufficient \(n\) is \(\left\lceil\log(2/\delta)/(2\varepsilon^2)\right\rceil=738\).

**Central limit theorem.** If \(X_i\) are iid with mean \(\mu\) and variance \(0<\sigma^2<\infty\), then
\[
\sqrt n\,(\bar X_n-\mu)/\sigma\ \Rightarrow\ N(0,1).
\]
Distributional convergence alone is not a finite-sample normal-approximation error certificate.

**Strong law.** If \(X_i\) are iid with \(E|X_1|<\infty\), then \(\bar X_n\to E[X_1]\) almost surely.

**Dependence counterexample.** If \(X_i=Z\) for every i and \(Z\sim\operatorname{Bernoulli}(1/2)\), then \(\bar X_n=Z\), so no concentration toward \(1/2\) occurs. In general,
\[
\operatorname{Var}(\bar X_n)=n^{-2}\left[\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)\right].
\]

### Exercises with answers

1. **Weak law.** If iid observations have variance nine, what is the Chebyshev bound for sample-mean error at least one with n=100? **Answer:** at most nine percent.
2. **Sampling.** How much independent data reduces standard error by a factor of three? **Answer:** nine times as many observations.
3. **Hoeffding.** For [0,1] independent observations and \(\varepsilon=0.05\), how does doubling n change the bound? **Answer:** it squares the exponential factor \(e^{-2n\varepsilon^2}\), with the leading factor two unchanged.
4. **Tail risk.** Does a CLT under finite variance imply a nonasymptotic two-sided 95% coverage interval at every n? **Answer:** no; it is asymptotic and needs finite-sample error control to certify any particular n.
5. **Clustering.** Why does sampling another thousand components from the same all-good or all-bad shift add little information about the across-shift defect probability? **Answer:** observations share one state and do not represent independent replications of that state.

### References

- MIT OpenCourseWare 18.175, *Theory of Probability*, laws of large numbers, Borel–Cantelli and central limit theory.
- MIT 18.600, *Probability and Random Variables*, lectures on weak/strong laws and central limit theorem.
- Wassily Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association (1963).
