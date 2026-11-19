# 017000 - Sampling Error: What an Estimate Actually Means

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** elementary expectation and variance; the central idea of an independent random sample. **Theme:** distributions of estimators, standard errors, law of large numbers, confidence and dependence.

<!-- BEGIN SPOKEN LECTURE -->

# Sampling Error: What an Estimate Actually Means

Imagine inspecting one hundred manufactured components and finding thirty-four defective ones. You report a defect rate of thirty-four percent. What does that number mean? It is certainly the fraction of defects in those one hundred inspected components. But if you want to say something about the underlying manufacturing process, you need an additional model of how those components were selected and what stays the same between inspections.

Suppose, for now, that each component independently has the same defect probability p. In that model, the observed fraction is a random variable, even though the unknown parameter p is a fixed number. A second inspection of one hundred components might find twenty-seven defects or forty-one. Different possible samples produce different estimates. The spread of those possible estimates is sampling error.

Understanding sampling error is the practical bridge from expectation and variance to Monte Carlo computation. In a simulation, we usually know exactly how samples are drawn, but we still do not know the exact expectation we seek. We estimate it with a random average, and then we must judge the uncertainty of that average.

## Two kinds of numbers

Let X stand for a defect indicator: one if a component is defective, zero otherwise. With defect probability p, its expectation is p, and its variance is p times one minus p. For n independently sampled components, the estimate of p is the average of their indicators. Its expected value is p, because expectation is linear. Such an estimator is called unbiased: across repeated samples drawn according to the stated model, its average result equals the target.

Unbiased does not mean that a particular estimate is correct. Even a fair coin flipped once gives an unbiased estimate of the probability of heads: the estimate is either zero or one. Neither outcome resembles a precise estimate of one half. Unbiasedness is a statement about repeated experiments, not a promise about a single result.

The variance of the average is p times one minus p divided by n. That result comes from the calculation we just made for independent measurements: add the variances and divide by the square of the sample size. Its square root is the standard error. For defect probability thirty percent and n equal to one hundred, the variance is point two one divided by one hundred, and the standard error is about four point six percentage points.

If the model really has p equal to thirty percent, we expect about thirty defects in a sample of one hundred, but a count a few defects above or below thirty is ordinary fluctuation. The count itself has standard deviation about four point six components. The fraction has standard deviation about point zero four six. They are the same uncertainty expressed in different units.

Notice that I used the true p to calculate that standard error, even though in an application p is exactly what we do not know. The usual estimate substitutes the observed fraction for p. With thirty-four defects, that gives a standard error of about four point seven percentage points. The estimate of our uncertainty is therefore random too.

## Why doubling the sample rarely halves the error

The standard error falls with the square root of the sample size. If you want a standard error half as large, you normally need four times as many independent observations with comparable variance. For the defect process, increasing n from one hundred to four hundred changes the idealized standard error from roughly four point six percentage points to roughly two point three, at p equal to thirty percent.

This is one reason numerical simulation can become expensive. Ten thousand independent samples are one hundred times as many as a hundred, but reduce a typical sampling error by a factor of ten, not a hundred. A million evaluations may be worth the expense when the integrand is complicated and a trustworthy estimate is needed. But the cost grows quickly if the desired tolerance keeps shrinking.

There are at least three different things we might try to improve. First, the sample count: evaluate the same sampling method more often. Second, the variability per sample: design a better estimator whose individual contributions fluctuate less. Third, bias: ask whether the average of the estimator even equals the target. Enlarging n only fixes the first problem automatically. A biased sampling process can confidently converge to the wrong answer.

## A confidence interval is a statement about a procedure

When p is neither very close to zero nor one and n is sufficiently large, the distribution of the sample fraction is approximately normal. Under appropriate conditions, about ninety-five percent of repeated sample fractions lie within roughly one point nine six standard errors of p. Turning that statement into an interval around the observed estimate gives a familiar approximate ninety-five percent confidence interval.

For thirty-four defects out of a hundred, the simple normal approximation gives roughly thirty-four percent plus or minus nine point three percentage points. Do not mistake this for an exact coverage guarantee. The approximation can behave badly with small counts or probabilities near zero or one, and more careful intervals such as the Wilson interval often perform better. The derivation also depends on the sampling model.

After data have been observed, the true p is not changing in a frequentist calculation. A particular interval either contains the true p or does not. The ninety-five percent claim concerns how frequently this interval-building procedure would succeed across repeated datasets generated under its assumptions. Bayesian credible intervals answer a different question by giving a probability distribution for the unknown p after assigning and updating a prior. Both can be useful, but their interpretations are not interchangeable.

An interval can also be narrow and wrong. Suppose a sensor consistently misses some defects, or the inspected components were drawn only from the best production shift. Repeating that same flawed inspection many times can make the estimate very precise for the wrong population. Sampling error is not the same as selection bias, measurement error, or model error.

## Finite-sample promises and asymptotic approximations

The central limit theorem explains why the normal approximation emerges when independent identically distributed observations have a finite, nonzero variance. It describes the limiting shape of the standardized average. By itself it does not say that any particular sample size is sufficient for a chosen accuracy.

Sometimes we can make a less sharp but rigorous promise. If individual observations lie between zero and one and are independent, Hoeffding's inequality bounds the probability that the sample average differs from its expectation by at least epsilon by two times an exponential term, with exponent negative two times n times epsilon squared. It does not require the distribution to be Bernoulli, only the stated bounds and independence.

Take an error tolerance of five percentage points and a failure probability no more than five percent. Solving that inequality gives a sufficient sample size of seven hundred thirty-eight. That does not mean seven hundred thirty-eight is the smallest sample size that could work for every distribution; it means this particular distribution-free bound certifies the target by that point. Its conservatism is the price paid for a guarantee that does not assume a precisely known p or rely on a large-sample Gaussian approximation.

Chebyshev's inequality uses only the variance, rather than the bounded range, and can be considerably looser. A normal approximation may be sharper, but is approximate. These are not three competing definitions of error. They are three distinct tools with distinct assumptions and conclusions.

## What happens when observations travel together

Return to the manufacturing example. Suppose all one hundred inspected components were produced during the same shift, and the defect probability varies dramatically from shift to shift. Perhaps a whole shift is either in a good state or a bad state. Then a hundred readings within one shift do not represent a hundred independent replications of the whole manufacturing process.

For a simple extreme model, let Z be either zero or one with equal probability, and suppose every component inspected during a shift has defect indicator Z. The sample fraction of defects equals Z for any sample size, even a million. Across shifts the mean is one half, but the observed fraction from a single shift remains either zero or one. Its variance does not shrink with n at all.

That is why the denominator in a standard error calculation must reflect the source of independent variation. The data table may have one million rows, yet only a small number of independent days, machines, households, or simulated trajectories. Covariance makes that distinction quantitative.

In an exchangeable idealization where all observations have variance sigma squared and every distinct pair has correlation rho, the variance of the average is sigma squared divided by n, times one plus n minus one times rho. If rho equals point one and n equals one hundred, the multiplier is ten point nine. The one hundred observations then have the same variance reduction as roughly nine independent observations, not one hundred. That is a simple model, not a universal formula for every time series; real dependencies need to be examined according to their structure.

## What repeatable simulation can and cannot give us

On a computer we often generate samples with a pseudorandom number generator. Choosing a fixed seed can make the same sequence of draws repeatable. That is useful for debugging, comparisons, and reproducing a numerical report. But repeating a computation with the exact same seed is not an independent replication and gives no new evidence of sampling uncertainty.

For error studies, we can run independent streams or seeds designed to avoid overlap and compare estimates. We can also compute a standard error from independent per-sample contributions. If we draw correlated samples, as in a Markov chain, the usual independent-sample variance formula does not apply without modification.

There are deeper distinctions, too. A simulation may estimate the expectation of an approximate model rather than the physical system. The sampling error can be tiny while the model bias is substantial. A numerical time step may distort a stochastic trajectory. A rare-event probability can remain badly underestimated because none of the simulated samples saw the rare event. A standard error computed from those zero event indicators is zero; it is not proof that the true event probability is zero.

The usable conclusion is simple. When you see an estimate, ask what is random, what is held fixed, what sampling rule was used, and what quantity the estimate targets. Ask whether the observations are independent, what controls their variance, and whether a normal approximation or a rigorous bound is being invoked. These questions do not make Monte Carlo calculations complicated for their own sake. They are the conditions under which a random answer can become a trustworthy numerical answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Binomial sampling and standard error

For \(X_i\stackrel{\rm iid}{\sim}\operatorname{Bernoulli}(p)\), \(S=\sum_{i=1}^n X_i\), \(\hat p=S/n\):
\[
E\hat p=p,\qquad \operatorname{Var}(\hat p)=\frac{p(1-p)}n,
\qquad\operatorname{SE}(\hat p)=\sqrt{\frac{p(1-p)}n}.
\]
With \(p=.3\), \(n=100\), this is \(\sqrt{.21/100}\approx0.045826\). At \(\hat p=.34\), the plug-in estimate is \(\sqrt{.34\cdot .66/100}\approx0.047371\). The naive Wald interval is \(.34\pm1.96(0.047371)\), about \([.2472,.4328]\); it is a large-sample approximation, not guaranteed coverage. For small n or extreme estimates, consider Wilson or exact binomial intervals.

### Two noninterchangeable claims

The central limit theorem (under iid and positive finite variance) states
\[
\frac{\sqrt n(\bar X_n-\mu)}\sigma\Rightarrow N(0,1).
\]
For independent bounded \(X_i\in[0,1]\), Hoeffding yields
\[
P(|\bar X_n-E\bar X_n|\ge\epsilon)\le 2e^{-2n\epsilon^2}.
\]
For \(\epsilon=.05\) and failure probability \(\delta=.05\), it suffices to take
\[
 n\ge\frac{\log(2/\delta)}{2\epsilon^2}\approx737.7759;
\quad n=738.
\]

### Correlated sample means

If \(\operatorname{Var} X_i=\sigma^2\) and \(\operatorname{Corr}(X_i,X_j)=\rho\) for all \(i\ne j\), then
\[
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}\,[1+(n-1)\rho],\quad
 n_{\rm eff}=\frac{n}{1+(n-1)\rho},
\]
where \(n_{\rm eff}\) is a variance-equivalent sample size, not the number of truly independent observations. For \(n=100\), \(\rho=.1\), it is about \(9.17\).

### Exercises with answers

1. **Precision.** To reduce an iid sample mean's standard error from 0.04 to 0.02 with unchanged one-observation variance, what multiplicative sample size increase is required? **Answer:** fourfold.
2. **Conditional guarantee.** What assumption would a normal-approximation confidence interval violate if all observations came from one latent all-good or all-bad shift? **Answer:** independence of the observed indicators (and possibly a common, stable Bernoulli parameter across the target population).
3. **Coverage meaning.** Does a frequentist 95% interval imply a 95% posterior probability that a fixed parameter lies in this particular interval? **Answer:** no; long-run procedure coverage is different from posterior probability.
4. **Perfect dependence.** Let \(X_i=Z\) for every i with \(Z\sim\operatorname{Bernoulli}(1/2)\). Find \(\operatorname{Var}(\bar X_n)\). **Answer:** \(1/4\) for all n.
5. **One-sided caution.** One hundred independent Bernoulli trials produce zero observed failures. Is the population failure probability exactly zero? **Answer:** no; zero observed events is compatible with positive probability. The plug-in standard error equals zero but fails as a useful uncertainty assessment at the boundary.

### Reading and attribution

- MIT OpenCourseWare 18.600, *Probability and Random Variables*, binomial sampling and probability approximations.
- Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables* (1963), bounded-sum concentration.
- Owen, *Monte Carlo Theory, Methods and Examples*, Chapter 2, numerical estimation and error assessment.
