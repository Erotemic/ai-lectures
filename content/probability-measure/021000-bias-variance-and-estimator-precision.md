# 021000 - Bias, Variance, and How Precise an Estimate Can Be

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** sample means, variance, likelihood and elementary derivatives. **Theme:** sampling distributions, estimator bias, mean squared error, information and confidence intervals.

<!-- BEGIN SPOKEN LECTURE -->

# Bias, Variance, and How Precise an Estimate Can Be

Imagine that we have measured the temperature of a room four times and obtained eight, nine, twelve and eleven degrees. Their average is ten. We could now announce that the room's true temperature is ten degrees. But four more measurements, made under the same conditions, would probably give a different average. To understand the estimate, we must imagine repeating the whole experiment, not merely examine the four numbers in front of us.

This distinction separates a point estimate from its sampling distribution. An estimate is the number calculated from one dataset. An estimator is the rule that takes a possible dataset and produces that number. Because the future dataset is random, the estimator is a random variable. It has an expectation, a variance, and often a distribution we can derive or approximate.

A central question of statistical inference is not just where the estimate landed, but how the rule behaves when the experiment is repeated. Does it systematically miss the target? How widely does it vary? If we design a new rule that reduces the variation, what bias might we introduce? And how much information about an unknown parameter did the observations actually contain?

## The spread of the sample mean

Suppose every measurement is the true temperature, called mu, plus a random error. Assume the errors have mean zero, variance four squared degrees, and are independent from one measurement to the next. The sample mean is still centered at mu. This follows from linearity of expectation. But what is its variance?

Each of the four errors has variance four. When we average four independent errors, the variance of their sum is sixteen, and dividing the sum by four divides the variance by sixteen. Thus the sample mean has variance one, and standard deviation one degree. This standard deviation of an estimator is its standard error.

More generally, for n independent observations of common variance sigma squared, the sample mean has variance sigma squared divided by n, and standard error sigma divided by the square root of n. If we want to cut the standard error in half, we need four times as many independent observations, assuming the measurement noise and sampling scheme do not change. Doubling the number only multiplies the standard error by one over the square root of two.

We are relying on independence. If each reading is affected by a slowly drifting sensor bias shared across the experiment, the average may not become arbitrarily precise. The covariance calculation determines how much the variation shrinks. Recording a thousand rows is not equivalent to conducting a thousand independent experiments.

## Bias is an average across repetitions

Suppose an estimator tends to report a slightly low value. Its bias is the expected value of the estimator minus the true parameter. A negative bias means that, over repeated samples, it tends to underestimate. An unbiased estimator has zero bias, but any particular estimate may still be far from the truth.

Why not always insist on unbiasedness? Because systematic offset is only one part of error. The mean squared error of an estimator is its variance plus the square of its bias. This identity is exact: expand the squared difference between the estimate and the true parameter around the estimator's mean. The cross term vanishes because deviations around a mean have expectation zero.

An estimator with a small bias and greatly reduced variance can have a smaller mean squared error than an unbiased one. Whether that compromise is worthwhile depends on what parameter values are plausible, what errors cost, and what assumptions we are prepared to defend.

To see this, suppose each observation is normally distributed with unknown mean mu and known variance one, and we have four independent measurements. The sample mean then has variance one quarter. Consider a rule that shrinks the sample mean toward zero by multiplying it by four fifths.

The new estimator has expected value four fifths of mu. Its bias is therefore minus one fifth of mu. Its variance is sixteen twenty-fifths of one quarter, which equals sixteen hundredths. Its mean squared error is sixteen hundredths plus one twenty-fifth of mu squared.

If the true mean were point two, the squared bias would be point zero zero one six, so the mean squared error would be point one six one six, better than the sample mean's point two five. But if the true mean were three, the squared bias would be point three six and the mean squared error would be point five two, worse than point two five. The shrinkage rule helps near its target and hurts farther away. We cannot declare a universal winner from one example.

There is a subtle circularity here. If we knew mu in advance, we could choose the shrinkage strength using mu. But mu is what we are trying to estimate. Data-driven shrinkage, hierarchical models, and cross-validation try to learn useful structure without that knowledge. Each introduces its own assumptions or variability. The little calculation tells us why the tradeoff exists, not how to resolve it in every problem.

## Why sample variance has two familiar denominators

The four temperature observations from our opening have mean ten, and their squared deviations from that mean are four, one, four and one. The sum is ten. In the Gaussian likelihood calculation, the fitted population variance was ten divided by four, or two and a half. But introductory statistics often divides by n minus one, giving ten divided by three.

Why does this correction appear? The sample mean was estimated from the same data. Once the four observations have been centered by their own average, their four deviations must sum to zero. They cannot vary independently: specifying three determines the fourth. This reduces the expected residual sum of squares.

The precise identity is worth understanding. Take the sum of squared differences from the sample mean. It equals the sum of squared differences from the true mean, minus n times the squared error of the sample mean. Across repeated independent samples, the first term has expectation n times sigma squared, and the second term has expectation sigma squared. The expected residual sum is therefore n minus one times sigma squared.

Dividing that sum by n minus one makes the sample variance unbiased. Dividing by n makes the Gaussian maximum-likelihood estimate, which is biased downward by the factor n minus one over n. As n grows, the difference becomes smaller. There is no contradiction: maximum likelihood and unbiasedness are different mathematical criteria.

## How sharply does a likelihood locate a parameter?

Think back to the likelihood curve for a coin's success rate. If the log-likelihood is very steep near its maximum, moving the parameter a little reduces the modeled fit quickly. If the curve is flat, many parameter values explain the observations almost equally well. This local curvature motivates the idea of information.

For independent Bernoulli observations with success probability p, the expected negative second derivative of the log-likelihood is n divided by p times one minus p. This is called Fisher information under the usual regularity assumptions. Its reciprocal is p times one minus p divided by n, exactly the variance of the sample proportion.

That agreement is not accidental. In many regular models, information limits how precisely an unbiased estimator can estimate a parameter. A result called the Cramér–Rao inequality states, under specific differentiability and interchange-of-expectation assumptions, that the variance of a regular unbiased estimator is at least the reciprocal of Fisher information. The Bernoulli sample proportion achieves that bound at interior parameter values.

But the inequality is not a universal law for every estimator and every model. Biased estimators need a different analysis. Boundaries can behave differently, and parameters that alter the support of the distribution can violate the familiar regularity hypotheses. Nor does large curvature rescue a model that is simply wrong.

## From a standard error to a confidence interval

A point estimate with a standard error suggests a range, but we need a probability statement to justify the range. Assume our measurements are independent normal observations with unknown mean mu and known standard deviation two degrees. With four measurements, their average is normally distributed around mu with standard deviation one degree.

The standardized difference between the average and mu has a standard normal distribution. About ninety-five percent of its values lie between negative one point nine six and positive one point nine six. Rearranging that event, we obtain an interval centered at the observed average and extending one point nine six standard errors in each direction. For our observed mean of ten, the interval runs from approximately eight point zero four to eleven point nine six degrees.

The coverage claim applies to the procedure across hypothetical repetitions of the experiment. If we repeated the same four-measurement procedure indefinitely, approximately ninety-five percent of the resulting intervals would contain the fixed true mu. Once this particular interval is calculated, the frequentist model treats mu as fixed, so a statement that it has a ninety-five percent probability of lying in this already-observed interval is not the conventional interpretation. A Bayesian credible interval answers a related but different probability question by putting a probability model on the unknown parameter.

Our interval was exact under its assumptions because the observation errors were normal and the standard deviation was known. If the standard deviation must be estimated from four observations, substituting a normal critical value and pretending it is known does not give the same coverage. For normal samples with unknown variance, Student's t distribution gives the classical correction. For nonnormal observations, approximate normal intervals may be justified by large-sample theory, but four observations usually do not support that approximation automatically.

## An interval cannot repair a bad sampling design

We have calculated what uncertainty looks like when data follow the stipulated model. But uncertainty about the sampling model itself is a separate problem. If every measurement was made with a miscalibrated thermometer, a very narrow interval might precisely estimate the wrong temperature. If we select only the hottest minutes of the day, additional observations can make our biased answer look increasingly precise.

Similarly, a narrow confidence interval does not tell us whether a device will behave the same way tomorrow under different conditions. A sample from a stable population supports a statement about that population under the assumed design. Extrapolation and causal claims require additional arguments.

Estimation is therefore a layered activity. We choose a target, establish how observations relate to it, construct an estimator, calculate its bias and variation, and finally examine whether those conclusions survive the realities of sampling. The formulas are not merely corrections to a reported number. They tell us what sort of claim the number can support.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Bias–variance identity

For \(\hat\theta\) with finite second moment and fixed \(\theta\),
\[
\mathbb E(\hat\theta-\theta)^2
=\operatorname{Var}(\hat\theta)+\big(\mathbb E\hat\theta-\theta\big)^2.
\]
Write \(\hat\theta-\theta=(\hat\theta-\mathbb E\hat\theta)+(\mathbb E\hat\theta-\theta)\) and expand; the mixed expectation is zero.

### Mean and variance estimators

If \(X_1,\ldots,X_n\) are independent, identically distributed with mean \(\mu\) and finite variance \(\sigma^2\), then
\[
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad
\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2.
\]
Taking expectations gives \(\mathbb E\sum_i(X_i-\bar X)^2=(n-1)\sigma^2\), so \(s^2=(n-1)^{-1}\sum_i(X_i-\bar X)^2\) is unbiased for \(n\ge 2\). In the Gaussian model, the MLE \(\hat\sigma^2_{\rm ML}=n^{-1}\sum_i(X_i-\bar X)^2\) has expectation \((n-1)\sigma^2/n\).

### A simple shrinkage calculation

For \(X_i\overset{\mathrm{iid}}\sim N(\mu,1)\), \(n=4\), \(\hat\mu_a=a\bar X\):
\[
\operatorname{Bias}(\hat\mu_a)=(a-1)\mu,\quad
\operatorname{Var}(\hat\mu_a)=\frac{a^2}{4},\quad
\operatorname{MSE}(\hat\mu_a)=\frac{a^2}{4}+(a-1)^2\mu^2.
\]
For \(a=4/5\), variance \(4/25=.16\). At \(\mu=1/5\), MSE \(4/25+1/625=101/625=.1616\); at \(\mu=3\), MSE \(.16+.36=.52\).

### Bernoulli Fisher information

For \(S=\sum_i X_i\) with \(X_i\sim\operatorname{Bernoulli}(p)\), \(0<p<1\):
\[
\ell'(p)=\frac Sp-\frac{n-S}{1-p},\quad
-\mathbb E\ell''(p)=\frac{n}{p(1-p)}=:I_n(p),\quad
\operatorname{Var}(S/n)=\frac{p(1-p)}{n}=I_n(p)^{-1}.
\]
The standard Cramér–Rao lower bound assumes regularity, including a parameter-independent support and justified differentiation under the integral/sign of expectation.

### Confidence interval for known normal variance

For \(X_i\overset{\mathrm{iid}}\sim N(\mu,\sigma^2)\) with *known* \(\sigma\),
\[
P_\mu\left(\bar X-1.9599639845\frac\sigma{\sqrt n}\le\mu\le\bar X+1.9599639845\frac\sigma{\sqrt n}\right)=.95.
\]
For \(\bar x=10,n=4,\sigma=2\), this is \([8.0400,11.9600]\) rounded to four decimals. With unknown \(\sigma\) and normal observations replace \(1.96\) by the appropriate t critical value and \(\sigma\) by \(s\).

### Exercises with worked answers

1. **More readings.** How many independent readings are needed to reduce a mean's standard error by a factor of three? **Answer:** nine times as many.
2. **Variance denominator.** For \(2,2,6\), calculate MLE and unbiased sample variance. **Answer:** squared residual sum \(32/3\); MLE \(32/9\), unbiased \(16/3\).
3. **Shrinkage.** In the example above with \(a=4/5\), at what absolute \(\mu\) does its MSE equal that of \(\bar X\)? **Answer:** solve \(.16+.04\mu^2=.25\), giving \(|\mu|=1.5\).
4. **Interpretation.** What does a 95% confidence procedure guarantee under the stated model? **Answer:** repeated-sampling coverage of 95%, not a model-free probability about a fixed parameter after observing this particular interval.
5. **Dependence.** If all four errors are the same random error, what is the standard error of their average when each error has standard deviation 2? **Answer:** 2, not 1; averaging identical errors does not reduce variation.

### Reading and attribution

- Penn State STAT 415, Lesson 2, *Estimation (Part I)*, https://online.stat.psu.edu/stat415/Lesson02.
- Penn State STAT 415, Lesson 7, *Asymptotic Distribution of MLE (Part I)*, https://online.stat.psu.edu/stat415/Lesson07.
- Penn State STAT 415, Lesson 6, *Confidence Intervals*, https://online.stat.psu.edu/stat415/Lesson06.
