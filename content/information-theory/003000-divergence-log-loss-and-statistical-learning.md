# Why a Wrong Probability Costs Logarithmic Evidence

**Track:** Information Theory: From Questions to Communication  
**Lecture:** 003000  
**Preparation:** Probability distributions, logarithms, entropy, and averages.  
**Companion:** Cross-entropy, KL divergence, likelihood, and model misspecification.

<!-- BEGIN SPOKEN LECTURE -->

Two forecasters predict whether tomorrow will be rainy. The first assigns a rain probability of three quarters. The second assigns one half. It rains. Which forecaster did better on this prediction? The first gave the realized event a higher probability and therefore made a less surprising forecast. If it had not rained, we would instead favor the second, whose forecast assigned a larger probability to the event that occurred.

There are many ways to score forecasts. One particularly useful score is **log loss**: take the negative logarithm of the probability the forecaster assigned to the realized outcome. If we use natural logarithms, the unit is nats; if we use base-two logarithms, the unit is bits. A forecast assigning probability one to what happens gets zero loss. Assigning a tiny probability to what happens gets a large loss. Assigning probability zero to an event that occurs gets infinite log loss.

Why choose logarithms? Among other reasons, the log score is additive across independent predictions when probabilities factor. Predicting the joint probability of a sequence requires multiplying the probabilities of its observed outcomes; negative logarithms turn that product into a sum. That makes a run of observations easy to score and gives a direct connection to the likelihood methods used in statistics.

But what does it mean for one probability model to be better on average? Suppose the world actually produces rain with probability three quarters, independently from day to day, and suppose we are judging forecasts by their expected log loss over a long run of such days. One forecaster tells the truth: rain probability three quarters. Another keeps saying one half. How much extra average loss does the second incur?

The expected log loss of a forecast q, when the true probabilities are p, is called the **cross-entropy** of p relative to q. For our two-outcome example, using base-two logarithms, it is three quarters times minus log base two of q for rain, plus one quarter times minus log base two of one minus q for no rain. If q is one half, the expected loss is exactly one bit per day: every realized outcome had been given probability one half.

What if q correctly equals three quarters? The expected loss becomes the entropy of the true distribution. That is about point eight one one bits per day. We cannot ordinarily make this expected score zero, because the outcome itself is uncertain. The entropy is the irreducible average log loss for an ideal forecaster that knows the true distribution. The difference between any other model's cross-entropy and that entropy is called the **Kullback–Leibler divergence**, or relative entropy.

For the fair-coin forecast applied to a true three-quarter rain probability, the divergence is about point one eight nine bits per day. That number is the average extra log loss from using the wrong distribution. It is also the expected amount of statistical evidence, in log units, that observations accumulate in favor of the true model rather than the false one. Under the usual independent-sampling idealization, log likelihood ratios add across days.

The definition of divergence is a sum over possible outcomes: each true probability multiplied by the logarithm of the ratio of the true probability to the proposed probability. The proposed model must assign positive probability wherever the true model does, or the divergence is infinite. This is not a technical nuisance. If a model declares an actually possible event impossible, its failure can be decisive.

Divergence is always nonnegative. That is Gibbs' inequality, and it is an important theorem rather than a definition. One proof uses the fact that log z is at most z minus one. Average an appropriate logarithm under the true distribution and the nonnegative difference appears. Divergence is zero exactly when the two finite distributions agree on all outcomes of positive true probability, with the usual normalized-support qualification.

Despite the name, relative entropy is not a distance metric. It is generally **asymmetric**. The penalty for using q when p is true need not equal the penalty for using p when q is true. One divergence asks how badly q predicts observations drawn from p. Reversing p and q changes which observations are typical and which model is being judged. There is no reason those penalties should be equal.

Let's connect this to statistical estimation. Suppose we flip a coin four times and observe heads, heads, tails, heads. Under a model in which each flip is independent with unknown head probability theta, the likelihood of this ordered sequence is theta cubed times one minus theta. We can choose theta to maximize that likelihood. Taking its logarithm gives three times log theta plus log of one minus theta; maximizing it yields theta equal to three quarters. That is the **maximum-likelihood estimate**.

This is also an entropy calculation in disguise. The observed data have an empirical distribution with three quarters heads and one quarter tails. Minimizing the empirical average negative log probability assigned by a candidate Bernoulli model produces the same theta as maximizing likelihood. For independent categorical observations, likelihood fitting and empirical cross-entropy minimization are two descriptions of one optimization problem.

But the fitted estimate is not automatically a precise description of the true coin. Four flips give little information; repeating the experiment could produce a very different estimate. The optimization gives the best-fitting parameter according to the specified likelihood, not a guarantee that the assumed model family is correct or that the estimate has small sampling error. Statistical inference adds uncertainty calculations and model checks.

The framework also explains why a well-calibrated probabilistic forecast can be more valuable than a hard label. If a system always says 'rain' whenever the predicted probability exceeds one half, it discards whether it thought rain was barely more likely or almost certain. For some decisions, that hard label may be sufficient. But for combining forecasts, assessing risk, and making decisions with asymmetric costs, the probabilities contain important information that the label loses.

A log-loss objective can be misused. A finite training sample may contain mislabeled observations, distribution shifts, selection bias, or strong dependencies. A complex model can drive the training loss very low while performing poorly on new examples. A low loss is a useful numerical criterion under a declared sampling model, not a seal of universal truth. It is also possible for a model that is well calibrated on one population to be poorly calibrated on another.

We have returned to the idea of information as negative log probability, now used to judge and fit probabilistic models. Entropy measures the irreducible uncertainty of the outcomes. Cross-entropy measures the expected score under a proposed model. Divergence measures the extra average score paid for describing one distribution as though it were another. Likelihood turns a collection of observations into a mathematical objective. These quantities connect coding and communication to regression, machine learning, hypothesis testing, and scientific model comparison.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For finite distributions p and q with \(q(x)>0\) whenever \(p(x)>0\), define (base-two units)
\[
H(p)=-\sum_xp(x)\log_2p(x),\quad H(p,q)=-\sum_xp(x)\log_2q(x),\quad D_2(p\Vert q)=\sum_xp(x)\log_2\frac{p(x)}{q(x)}.
\]
Then \(H(p,q)=H(p)+D_2(p\Vert q)\). Gibbs' inequality \(D_2(p\Vert q)\ge0\) follows, for example, from concavity of log: \(\sum_x p(x)\ln(q(x)/p(x))\le\ln\sum_xq(x)\le0\), with standard support conventions.

For \(p=(3/4,1/4)\) and \(q=(1/2,1/2)\),
\[
D_2(p\Vert q)=\tfrac34\log_2(3/2)+\tfrac14\log_2(1/2)\approx0.188722.
\]
The reverse divergence is \(D_2(q\Vert p)=\tfrac12\log_2(2/3)+\tfrac12\log_2 2\approx0.207519\); this demonstrates asymmetry.

For independent Bernoulli observations \(x_1,\ldots,x_n\), the likelihood is \(L(\theta)=\theta^{s}(1-\theta)^{n-s}\), where \(s=\sum_i x_i\). Maximizing \(\ell(\theta)=s\ln\theta+(n-s)\ln(1-\theta)\) over \(0\le\theta\le1\) gives \(\hat\theta=s/n\), including boundary cases. The estimate minimizes empirical binary cross-entropy when the same model is used.

### Exercises and solutions

1. **Entropy versus cross-entropy.** What is \(H(p,q)\) for \(q=(1/2,1/2)\), regardless of the Bernoulli true distribution p? **Solution:** one bit.
2. **Nonnegativity.** When is \(D(p\Vert q)=0\) for finite probability mass functions? **Solution:** when p and q agree on all outcomes (under the standard normalized setting).
3. **Likelihood.** A coin gives 8 heads in 10 independent flips. What Bernoulli probability maximizes likelihood? **Solution:** 0.8.
4. **Zero probability.** What happens to expected log loss if q assigns probability zero to an outcome having positive true probability? **Solution:** expected log loss and KL divergence are infinite.

### Reading and attribution

- MIT OpenCourseWare, 6.441 *Information Theory* (2016), Chapter 1, entropy, divergence and cross-entropy: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- MIT OpenCourseWare, 6.441 (2016), Chapter 2, divergence and mutual information: https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/.
- The daily-rain forecast and four-flip likelihood example are original calculations.
