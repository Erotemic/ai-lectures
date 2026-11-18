# 020000 - Likelihood: From Observed Data to Unknown Parameters

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** elementary probability, functions, logarithms and one-variable differentiation. **Theme:** statistical models, likelihood, maximum likelihood and the meaning of fitting.

<!-- BEGIN SPOKEN LECTURE -->

# Likelihood: From Observed Data to Unknown Parameters

Suppose we are testing a device that sometimes succeeds and sometimes fails. We run ten trials and see eight successes. How likely is it that the device succeeds eighty percent of the time? The wording sounds straightforward, but there is a trap. Probability describes possible data when a model is specified. Here the data have already happened, and the unknown success rate is what we want to learn. To reason about that unknown rate, we first need a way to compare how well different rates explain the observed trials.

That comparison is called likelihood. It is closely related to probability, but it reverses which quantity we hold fixed. A probability model starts with a parameter and assigns probabilities to outcomes. A likelihood calculation starts with an outcome and treats the same formula as a function of the parameter. The formula may be identical; the question is different.

We will build this distinction from ten trials, find the parameter that maximizes the likelihood, connect the same calculation to the method of least squares, and see why not every likelihood can be optimized by differentiating a formula. Along the way we will keep the difference between fitting a parameter and quantifying uncertainty about it.

## The ten trials

Let p denote the device's success probability. For now, assume that every trial is independent and has the same probability p of success. The assumptions matter. If the device heats up, if successive trials interfere with one another, or if the test conditions change, one common p and independence may be a poor model. But with those assumptions, the calculation is simple.

Imagine that we recorded all ten results in order. Each success contributes a factor of p to the probability of that sequence; each failure contributes a factor of one minus p. Eight successes and two failures give the product p to the eighth power times one minus p squared. If instead we recorded only the count of successes, we multiply by the number of ways to arrange eight successes among ten trials. There are forty-five such arrangements. That factor changes the probability of the count, but it does not depend on p, so it will not change which p maximizes the likelihood.

Let's compare two explanations for our eight successes. One says the true success rate is one half. The other says it is four fifths. The ratio of their likelihoods is the ratio of eight factors of four fifths to eight factors of one half, multiplied by the ratio of two factors of one fifth to two factors of one half. The common arrangement factor cancels. Numerically, the data are about six point nine times as likely under the eighty-percent model as under the fifty-percent model.

This is a meaningful comparison, but not a probability that the eighty-percent model is true. To assign probabilities to competing parameter values, we would need additional ingredients, such as prior probabilities and a Bayesian updating rule. A likelihood ratio alone says how the observed data favor one specified model over another, under the sampling assumptions.

## Finding the best-fitting rate

We need not compare just two candidate values. Let p range from zero to one and look for the maximum of eight successes' likelihood: p to the eighth times one minus p squared.

Multiplying many small probabilities can be awkward, and differentiating a long product is tedious. The natural logarithm is strictly increasing, so the value that maximizes a positive likelihood also maximizes its logarithm. The log-likelihood here is eight times log p plus two times log of one minus p, plus a constant if we are working with the count.

Its derivative is eight divided by p, minus two divided by one minus p. Setting this derivative to zero gives eight times one minus p equals two p. Thus eight equals ten p, and the fitted rate is eight tenths. The second derivative is negative for every p strictly between zero and one, so this interior critical point is the unique maximum.

The estimate is simply the observed fraction of successes. That may seem inevitable after we see the answer, but the calculation has given us a reusable method: define a sampling model, write the likelihood of the actual data, take its logarithm where convenient, and optimize over the allowable parameters.

Now consider a dataset in which all ten trials failed. There is no interior solution to the score equation. Instead, the likelihood is one minus p raised to the tenth power, and its maximum on the closed parameter interval occurs at p equal to zero. Boundary maxima are legitimate solutions. Blindly dividing by p or one minus p can discard them. If the model restricts p strictly between zero and one, the likelihood has a supremum approached as p tends to zero, but no maximizer inside that open parameter space. Which parameter values are allowed is part of the problem.

## Poisson counts and the role of exposure

The same pattern appears in count data. Suppose we observe numbers of arrivals during four equal time intervals: two, zero, three, and one. Assume independent Poisson counts with a common expected count lambda per interval. The probability formula for each count contains an exponential term involving minus lambda, a power of lambda, and a factorial. Multiply four copies. Terms depending only on the observed counts can be set aside when maximizing over lambda.

The log-likelihood relevant to the parameter is minus four lambda plus the sum of the counts times log lambda. Our counts add to six. Differentiating gives minus four plus six divided by lambda, so the fitted expected count is six divided by four, or one and a half arrivals per interval.

Notice the units. If the intervals were five minutes long, this parameter would mean expected arrivals per five minutes, not per minute. We could model an arrival rate per minute by including each interval's duration as an exposure. That would change the likelihood and the interpretation of the parameter. Statistical models are descriptions of measurements, and the measurement design belongs inside them.

## Why least squares comes from a probability model

Now imagine measuring a constant temperature with a sensor. Four readings are eight, nine, twelve and eleven degrees. You suspect that each reading is a fixed unknown mean plus an independent, zero-mean Gaussian measurement error. Assume for the moment that the error variance is known and the same for each reading.

The normal density of each observation contains an exponential of minus the squared distance from the unknown mean, divided by twice the variance. Multiplying four densities makes the exponent a sum of squared distances. Taking the logarithm and discarding constants leaves a negative multiple of that sum.

To maximize the likelihood, we must therefore minimize the sum of squared deviations from the candidate mean. This is least squares, not as an arbitrary taste for squared errors but as a consequence of this particular measurement-error model.

The sum of squared deviations is minimized at the sample mean. In our example, the readings add to forty, so the fitted mean is ten degrees. To see why, write each reading minus a candidate value as its deviation from the sample mean plus the sample mean minus the candidate. Expand the squares. The cross terms cancel because the deviations from the sample mean add to zero. What remains is the minimum squared error at the sample mean, plus four times the square of the distance from that sample mean.

This connection also warns us about the assumption. With different noise distributions, the best-fitting center may change. For independent Laplace errors with common scale, maximizing likelihood instead minimizes absolute deviations, whose minimizers are medians. If there are extreme outliers, the difference between these error models can matter enormously. A fitted parameter cannot be interpreted independently of the likelihood model used to fit it.

## Fitting a variance is a different calculation

Suppose the Gaussian mean and variance are both unknown. After estimating the mean by ten, the four squared residuals are four, one, four and one. They add to ten. Maximizing the normal likelihood over the variance gives ten divided by four, or two and a half squared degrees. That is the maximum-likelihood estimate of the variance in this model.

You may have previously met a different denominator, three rather than four. That denominator gives the familiar unbiased sample variance, ten divided by three. Both formulas can be correct, because they optimize different criteria. Maximum likelihood asks which parameter gives the observed sample the largest modeled density. Unbiased estimation asks for a statistic whose expectation, across repeated samples, equals the true parameter. A good method for one objective need not automatically be best for another.

In particular, a parameter fitted from data is not known exactly. A ten-trial estimate of eighty percent may fluctuate substantially if the experiment is repeated. The curvature of a likelihood can tell us something about that variability, but it needs a sampling argument. We should not mistake the location of a maximum for a guarantee of precision.

## When the support moves with the parameter

For a final example, imagine a variable selected uniformly between zero and an unknown positive upper limit a. We observe three values whose largest is four. For any candidate a smaller than four, the likelihood is zero: that candidate model would make our largest observation impossible. For any a at least four, the joint density is one divided by a cubed. As a grows, that density decreases. The best-fitting value, under the model with endpoints included, is therefore exactly the sample maximum, four.

There is no useful interior derivative equation to solve. The support of the density itself depends on a. If the uniform model is defined on an open interval below a, the maximum is approached as a decreases toward four from above but is not attained. Again, the permitted parameter set matters.

This example also reminds us that likelihood is not a free-standing universal score. For continuous observations, we compare densities under a specified measurement convention; a density value is not the probability of observing an exact real number. Parameter-dependent support and transformations of data require care when comparing likelihoods.

## What the likelihood has, and has not, delivered

We can now take real data and turn a model into an estimate. For binary trials, the success fraction maximizes the Bernoulli likelihood. For equal-exposure Poisson counts, the sample average maximizes the rate likelihood. With independent Gaussian noise of common variance, least squares is maximum likelihood for the mean. With a uniform upper endpoint, the largest observation determines the fit by a support constraint.

But the act of maximizing does not establish that our model is right, that the observations are independent, or that the fitted parameter is stable. A flexible model can fit noise. Two different parameter values can sometimes produce almost the same observations. And a maximum may lie on a boundary where familiar large-sample approximations need modification.

Statistical inference begins with this separation: the data supply evidence through a model; estimation extracts a candidate parameter; uncertainty analysis asks how that extraction behaves over repeated samples. We have done the first two. The next task is to assess how much an estimate can move, and how to choose among estimators that make different compromises.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Bernoulli likelihood and likelihood ratio

For independent Bernoulli observations with observed success count \(s\),
\[
L(p)=p^s(1-p)^{n-s},\quad
\ell(p)=s\log p+(n-s)\log(1-p),\quad
\ell'(p)=\frac{s}{p}-\frac{n-s}{1-p}.
\]
If \(0<s<n\), \(\hat p=s/n\) and \(\ell''(p)=-s/p^2-(n-s)/(1-p)^2<0\). At \(s=0\) or \(n\), consider the boundary. For \(n=10,s=8\),
\[
\frac{L(.8)}{L(.5)}=\left(\frac{.8}{.5}\right)^8\left(\frac{.2}{.5}\right)^2
=6.8719476736.
\]
If the observed summary is the count instead of the ordered sequence, multiply both likelihoods by \(\binom{10}{8}\), which cancels in the ratio.

### Poisson arrivals

With \(X_i\overset{\mathrm{iid}}\sim\operatorname{Pois}(\lambda)\),
\[
\ell(\lambda)=-n\lambda+\left(\sum_i x_i\right)\log\lambda-\sum_i\log(x_i!),\quad
\hat\lambda=\bar x
\]
for positive total count; when all counts are zero and \(\lambda\ge0\), the maximum is at \(\lambda=0\). With duration \(t_i\) and rate \(r\), \(X_i\sim\operatorname{Pois}(rt_i)\) gives \(\hat r=\sum_i x_i/\sum_i t_i\).

### Gaussian likelihood and least squares

For \(X_i\overset{\mathrm{iid}}\sim N(\mu,\sigma^2)\),
\[
\ell(\mu,\sigma^2)= -\frac n2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_i(x_i-\mu)^2.
\]
The identity
\[
\sum_i(x_i-a)^2=\sum_i(x_i-\bar x)^2+n(a-\bar x)^2
\]
shows \(\hat\mu=\bar x\), then \(\widehat{\sigma^2}_{\mathrm{MLE}}=n^{-1}\sum_i(x_i-\bar x)^2\). For readings \(8,9,12,11\), this gives \(\bar x=10\) and \(\widehat{\sigma^2}_{\mathrm{MLE}}=2.5\). The unbiased variance is \(s^2=10/3\).

### Support-dependent likelihood

For i.i.d. uniform observations on \([0,a]\), \(a>0\),
\[
L(a)=a^{-n}\mathbf 1\{a\ge m\},\qquad m=\max_i x_i.
\]
For observations with \(m>0\), the maximizing value on this closed-endpoint parametrization is \(\hat a=m\). With open support \([0,a)\), the supremum occurs in the limit \(a\downarrow m\) but is not attained.

### Exercises with answers

1. **Nine trials, three successes.** Find the Bernoulli MLE. **Answer:** \(3/9=1/3\).
2. **Rate and exposure.** Counts \(2,4,3\) over exposures \(1,2,1\) hours. Find the Poisson rate MLE. **Answer:** \(9/4=2.25\) arrivals per hour.
3. **Same density, different question.** Does \(L(.8)>L(.5)\) mean the probability that \(p=.8\) is greater than one half? **Answer:** no; probabilities over parameters require an explicit additional model, such as a prior.
4. **Gaussian reading.** For \(2,2,6\), find mean and Gaussian MLE variance. **Answer:** mean \(10/3\), squared residual sum \(32/3\), MLE variance \(32/9\).
5. **Boundary maximum.** Ten failures: why is \(\ell'(p)=0\) the wrong starting point? **Answer:** the maximum is at the allowed endpoint \(p=0\), not an interior stationary point.

### Reading and attribution

- Penn State STAT 415, Lesson 4, *Maximum Likelihood Estimation*, https://online.stat.psu.edu/stat415/Lesson04.
- Penn State STAT 415, Lesson 3, *Estimation (Part II)*, for method-of-moments and Gaussian estimators, https://online.stat.psu.edu/stat415/Lesson03.
- Harvard Stat 110, *Introduction to Probability*, course materials, https://stat110.hsites.harvard.edu/.
