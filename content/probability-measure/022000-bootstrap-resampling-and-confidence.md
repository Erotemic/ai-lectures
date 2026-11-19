# 022000 - The Bootstrap: Learning About Sampling Error from One Sample

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** independent random samples, empirical averages, sample variance and standard errors. **Theme:** empirical distributions, bootstrap replicates, standard errors, confidence intervals and resampling failures.

<!-- BEGIN SPOKEN LECTURE -->

# The Bootstrap: Learning About Sampling Error from One Sample

You take a sample, calculate a statistic, and want to know how much that statistic would change if you ran the experiment again. Ideally, you could repeat the experiment a thousand times. But the original sample may have been expensive to collect, or the experiment may simply be over. We possess one dataset, and yet we want information about a whole distribution of possible estimates.

The bootstrap offers a computational answer. Instead of pretending that we can repeat the physical experiment, we construct an imitation of repetition from the data we have. We treat the observed sample as a small stand-in for the population, draw new samples from that stand-in, and recalculate the statistic many times. The scatter of those recalculated statistics estimates the scatter we care about.

The idea sounds almost suspicious. We use the data to imitate more data. What new information could possibly appear? None appears out of nowhere. What the bootstrap contributes is a way to propagate the variability represented in the observed sample through a possibly complicated calculation. It can reveal how sensitive a statistic is to the composition of a random sample. Its reliability depends on how faithfully the observed sample represents the population and on how the statistic responds to small changes in that population.

Let us work through the construction exactly on four observations, then extend it to procedures where no convenient standard-error formula is available.

## The population we can actually see

Suppose our observations are two, four, four and six. Their mean is four. We imagine that these four numbers came from independent draws from some unknown population distribution. What distribution could we use to simulate a replacement sample without guessing a parametric family such as Gaussian or exponential?

The simplest answer is the empirical distribution. Give each observed row probability one fourth. Because the value four appears twice, a draw from the empirical distribution gives two with probability one fourth, four with probability one half, and six with probability one fourth. This is a perfectly valid probability distribution: its probabilities sum to one, and its expected value is four.

A bootstrap sample has the same number of observations as the original sample. We draw four times independently from this empirical distribution, *with replacement*. That last phrase is essential. After drawing a row, we leave it eligible for the next draw. A bootstrap sample might be two, two, four, six. It might be four, four, four, four. It might contain the same original row several times and omit another row entirely.

Now compute the mean of the bootstrap sample. Repeat the entire four-draw procedure many times and record the resulting means. The collection of means is a simulated sampling distribution, conditional on the four data values we actually observed.

Why with replacement? If we drew four values without replacement from a collection of four, every resample would consist of exactly the original four values in some order. The mean would always equal four. We would have generated permutations, not an imitation of sampling variation. Replacement allows the proportions of the observed values to fluctuate, as real sample proportions do.

## An exact bootstrap calculation without a computer

For these four observations, we can calculate the bootstrap mean's variance directly. Under the empirical distribution, the mean of one draw is four. Its possible deviations from four are negative two, zero and positive two, with probabilities one fourth, one half and one fourth. Square those deviations and average. One fourth of four plus one fourth of four gives variance two.

Each bootstrap replicate mean averages four independent draws from that empirical distribution. Its variance is therefore two divided by four, or one half. Its standard deviation is the square root of one half, approximately point seven zero seven. That is the ideal nonparametric bootstrap standard error of the sample mean, conditional on this observed dataset, if we could enumerate or simulate arbitrarily many bootstrap samples.

Compare this with the classical estimated standard error using the unbiased sample variance. The original squared deviations from four add to eight. Divide by three to get a sample variance of eight thirds. Divide by four, then take the square root, to estimate the mean's standard error as the square root of two thirds, about point eight one six.

Why the difference? The ordinary nonparametric bootstrap uses the empirical distribution as the population. Its variance divides the squared deviations by four. The classical unbiased sample variance divides by three. The two methods therefore differ by a small finite-sample correction. In larger samples the ratio approaches one. The bootstrap is an approximation method, not an identity that must reproduce every textbook formula exactly for small n.

We can even understand the simulated sampling distribution without running a single random number generator. There are four choices for each of four bootstrap draws, so there are four to the fourth power, or two hundred fifty-six, equally likely choices of original row indices. Different index sequences can produce the same numerical sample, but the index sequences are equiprobable. Enumerating them gives the exact conditional bootstrap distribution. Simulation merely approximates that enumeration when the sample is too large or the statistic too complicated.

## The computational procedure

For a general statistic, the steps are straightforward. First decide what the independent sampling units were in the actual experiment. If each row is one independently sampled individual, the rows are the units. Draw n of those rows independently with replacement. Recompute the statistic on that new dataset. Repeat for many resamples. Finally, inspect the distribution of replicate statistics.

For the mean, the classical standard-error formula is easy. For a median, a ratio of two means, a fitted regression coefficient, or the output of a complicated scientific analysis, the sampling distribution may be harder to derive. Resampling lets us pass each artificial dataset through the same estimator, including its fitting steps. If the statistic is sensitive to which observations appear, that sensitivity is reflected in the variation among bootstrap replicates.

We should not report the number of bootstrap replicates as if it were the number of original observations. A thousand bootstrap replicates from four original people are still based on four original people. Increasing the number of replicates improves our numerical approximation to the *bootstrap distribution*. It does not make the empirical distribution a more faithful picture of the unknown population.

We should also make the sampling procedure reproducible. If a computer uses pseudorandom numbers, record the random seed and implementation choices. More importantly, record which units were resampled, which statistic was recomputed, and whether any model fitting, variable selection, or preprocessing was repeated inside each resample. A bootstrap estimate can be deceptively precise when the expensive or unstable parts of the analysis have been frozen outside the resampling loop.

## From bootstrap scatter to an interval

If we sort a large collection of bootstrap estimates, we can take the values near the two-and-a-half and ninety-seven-and-a-half percentiles. These endpoints form a basic kind of bootstrap confidence interval called a percentile interval. The procedure is intuitive: it uses the central ninety-five percent of the simulated estimator distribution as a proposed range for the unknown target.

But there is an important logical step here. The percentiles describe variation under the empirical distribution, with that distribution taken as known. A confidence interval requires a claim about how often the interval contains the *true population parameter* over repeated original samples. Those are not the same thing. For many sufficiently smooth statistics and sufficiently large independent samples, the bootstrap approximates the sampling distribution well enough to support a useful interval. For small or skewed samples, or statistics with difficult boundary behavior, a plain percentile interval can have poor coverage.

There are other bootstrap interval constructions. A basic bootstrap interval reflects bootstrap deviations around the observed estimate. A studentized interval rescales deviations by an estimated standard error. Bias-corrected and accelerated methods adjust for aspects of bias and skewness. None is a substitute for checking the sampling design, the target statistic, and whether the approximation is credible.

In our four-observation example, the exact distribution of bootstrap means is discrete and rather coarse. We could compute empirical percentiles, but there is no reason to expect a confidence interval drawn from them to have precisely ninety-five percent coverage for every possible underlying population. The meaning of the ninety-five percent label comes from a coverage argument, not simply from discarding five percent of a simulated distribution.

## Why the bootstrap can be confidently wrong

Consider a different dataset: four successes in four trials, with each trial modeled as an independent Bernoulli observation. The observed success fraction is one. The empirical distribution contains only successes. Every bootstrap sample also contains only successes, so every bootstrap success fraction equals one. The bootstrap standard error is zero.

Does the observation of four successes prove that the true success probability is exactly one? Of course not. A device that succeeds only seventy percent of the time can still achieve four successes in a row. The resampling scheme has no failures available to represent that possibility. It is estimating variation under a distribution that puts all its mass on success, which is especially misleading at the boundary.

This is not a coding bug. It exposes a statistical limitation. The empirical distribution cannot represent outcomes that were never observed. For certain small-sample or boundary problems, an exact binomial interval or a carefully justified model-based method is much more appropriate than a naive nonparametric bootstrap.

A related issue arises for rare events. Suppose a costly system failure occurs once in a million operations but we sample only a few hundred operations and see none. Resampling the observed operations will not invent the missing failure mechanism. Inference about such rare events needs other information, much larger samples, or explicit modeling assumptions.

## Dependence changes what must be resampled

Suppose we measure two readings on each person, one before and one after a treatment. The natural estimate may be the average of each person's after-minus-before difference. To bootstrap it, we should resample *people*, preserving the pair of measurements within each person. If we resample the before and after columns independently, we destroy the pairing that defines the estimate's variance.

The same principle applies to clustered experiments. If observations come from ten schools with many students in each, and schools are the independently sampled units, then resampling individual students as though everyone were independent can understate uncertainty. Resampling schools may be more appropriate. For a time series, adjacent observations depend on one another; resampling individual timestamps breaks that dependence. Block bootstraps or explicit time-series models try to preserve relevant dependence, but they require additional choices.

In every setting, ask what kind of world could have produced another dataset like this one. The resampling scheme must imitate *that experiment*, not merely shuffle a table of values.

## What the bootstrap teaches

The bootstrap was introduced by Bradley Efron in 1979 as a broadly reusable way to estimate sampling distributions through computation. Its basic move is simple: replace an unknown distribution with an empirical one, then repeat the statistic under that substitute. But its deepest lesson is about the relationship between computation and assumption.

A computer can evaluate a statistic on millions of resamples and return a number with many decimal places. The useful accuracy of that number still depends on the original sampling design, the amount of information in the data, and the mathematical behavior of the statistic. Resampling is a tool for propagating uncertainty we have represented, not a machine for discovering uncertainty the sample never contained.

Used carefully, it can turn a complicated estimator into a comprehensible distribution of possible estimates. Used carelessly, it can make four perfect successes look like certainty. Knowing the difference is the heart of bootstrap reasoning.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Empirical-distribution bootstrap

For observations \(x_1,\ldots,x_n\), define \(\widehat F_n=n^{-1}\sum_i\delta_{x_i}\). A nonparametric bootstrap sample \(X_1^*,\ldots,X_n^*\mid x\) is i.i.d. from \(\widehat F_n\). For statistic \(T\), \(T^*=T(X_1^*,\ldots,X_n^*)\) estimates the sampling distribution of \(T(X_1,\ldots,X_n)\) under suitable assumptions.

### Exact sample mean calculation

For \(x=(2,4,4,6)\), \(\bar x=4\). Under \(\widehat F_4\),
\[
P^*(X^*=2)=1/4,\quad P^*(X^*=4)=1/2,\quad P^*(X^*=6)=1/4,
\]
\[
E^*X^*=4,\quad \operatorname{Var}^*(X^*)=\frac14(2-4)^2+\frac12(4-4)^2+\frac14(6-4)^2=2,
\]
\[
E^*\bar X^*=4,\quad \operatorname{Var}^*(\bar X^*)=2/4=1/2,\quad
\operatorname{SE}_{\rm boot}(\bar x)=\sqrt{1/2}\approx0.70710678.
\]
The classical plug-in standard error from the unbiased variance estimator is \(s/\sqrt4=\sqrt{(8/3)/4}=\sqrt{2/3}\approx0.81649658\).

### Index implementation and percentile interval

With \(B\) replicate samples: for each \(b\), choose \(I_{b1},\ldots,I_{bn}\) independently and uniformly from \(\{1,\ldots,n\}\), then compute \(\hat\theta_b^*=T(x_{I_{b1}},\ldots,x_{I_{bn}})\). Estimate conditional standard error with the sample standard deviation of \(\hat\theta_b^*\). A percentile interval uses the empirical 0.025 and 0.975 quantiles of these values; its frequentist coverage is not automatically 95%.

### Bernoulli boundary failure

If \(x=(1,1,1,1)\) then \(\widehat F_4=\delta_1\) and \(\hat p^*\equiv1\), giving bootstrap standard error zero. Yet for true \(p=0.7\), \(P_p(X_1=\cdots=X_4=1)=0.7^4=0.2401>0\). A zero bootstrap SE does not imply a known success probability.

### Pairs and blocks

For independent sampling units \(Z_i=(X_i,Y_i)\), resample whole vectors \(Z_i\) to preserve within-pair covariance. For dependent time series, naive i.i.d. resampling does not preserve serial correlation; block methods introduce a block-length tuning problem.

### Exercises with worked answers

1. **With or without replacement?** If a bootstrap sample of size four is drawn without replacement from four rows, what is its mean? **Answer:** always the original mean; it contains no sampling variation of the mean.
2. **Empirical variance.** For \((1,3,3,5)\), calculate the conditional bootstrap variance of the mean. **Answer:** empirical draw variance \(2\); mean variance \(2/4=1/2\).
3. **Boundary case.** For six failures out of six Bernoulli trials, what standard error does ordinary nonparametric resampling assign the success fraction? **Answer:** zero, for the same misleading boundary reason as the all-successes case.
4. **Paired study.** For each of twenty people, there is a before and after reading. What should be resampled? **Answer:** twenty pairs of readings, not the two columns independently.
5. **Replicates.** Does increasing \(B\) from 1,000 to 100,000 increase the original sample's information about the population? **Answer:** no; it only reduces Monte Carlo error in approximating the conditional bootstrap distribution.

### Reading and attribution

- Bradley Efron, *Bootstrap Methods: Another Look at the Jackknife*, Annals of Statistics **7** (1979), 1–26, https://doi.org/10.1214/aos/1176344552.
- Penn State STAT 415, Lesson 8, *Asymptotic Distribution of MLE (Part II)*, bootstrap and interval construction, https://online.stat.psu.edu/stat415/Lesson08.
- Bradley Efron and Robert Tibshirani, *An Introduction to the Bootstrap* (1993), https://doi.org/10.1201/9780429246593.
