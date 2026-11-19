# 019000 - More Accuracy from the Same Samples: Variance Reduction

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** integration as expectation, sample variance and standard error. **Theme:** antithetic sampling, control variates, stratification and importance sampling.

<!-- BEGIN SPOKEN LECTURE -->

# More Accuracy from the Same Samples: Variance Reduction

If you ask a computer for a Monte Carlo estimate of an integral, one obvious way to improve it is to draw more samples. But consider a second option. Instead of drawing more points, change how the points are chosen and how their function values are combined. You may get much more accuracy from the same number of expensive evaluations.

The idea is called variance reduction. It does not change the mathematical quantity we wish to estimate. It changes the random procedure used to estimate that quantity. In this lecture we will compare several such procedures on one deliberately simple integral: the integral of x squared between zero and one. We know the exact answer is one third, which allows us to check every calculation. The techniques apply just as well when the exact answer is unknown and each function evaluation requires an expensive simulation.

Our baseline is crude Monte Carlo. Draw n independent uniform values between zero and one and average their squares. The estimate is unbiased. The variance of one squared uniform value is four forty-fifths, so the variance of the average is four divided by forty-five n. We will keep track of the number of evaluations, not just the number of random numbers, when comparing improvements.

## First improvement: pair one point with its mirror

Suppose we sample U uniformly between zero and one, but instead of using only U, evaluate the function at U and at one minus U. Average those two function values. For the squared function, the pair gives the average of U squared and one minus U squared.

Why is the result still unbiased? Because one minus a uniform random variable is also uniformly distributed. Each function evaluation separately has expectation one third. The average of two quantities with that expectation also has expectation one third, even though the two evaluations are dependent.

Now notice their dependence. If U is close to zero, U squared is small but one minus U squared is large. If U is close to one, their roles reverse. The two values tend to balance each other. Instead of both fluctuating in the same direction, they frequently pull against each other. This is antithetic sampling.

Expand the pair average. It simplifies to U squared minus U plus one half. Its expectation is one third. Its variance is one one-hundred-eightieth. That is much smaller than the variance of two independent function evaluations averaged together, which is two forty-fifths. With the same two function calls, antithetic pairing reduces the estimator variance by a factor of eight in this particular example.

One pair at U equal to point two gives an estimate of point three four. Two independent random function evaluations might both land near zero and badly underestimate the integral; an antithetic pair cannot do that, because its second argument mirrors the first. The pair is not guaranteed to be closer in every draw. Variance reduction is a statement about the spread across repeated draws, not a claim that every possible output improves.

Antithetic sampling is especially natural when the function responds monotonically to a uniform input. Negative correlation between paired evaluations is what makes it effective. For a highly oscillatory or nonmonotone function, the pairing may be less useful or even fail to reduce variance. We must analyze the function, not merely apply a clever-sounding trick.

## Second improvement: divide the domain deliberately

A random sample from the entire interval may leave a region unvisited by chance. Instead, divide the interval into two halves. Draw one uniform point from the left half and another independent uniform point from the right half. Average their squared function values with the appropriate weights. Because the halves have equal length, those weights are each one half.

This is stratified sampling. We have forced the estimator to represent both halves of the domain. We are still sampling randomly within each half, so we can estimate uncertainty, but we no longer allow both points to land in the same half.

The estimator is unbiased because the integral over the whole interval is the sum of the integrals over the two halves. The expected contribution from each stratum equals its share of the original integral. We must retain the stratum-volume weights; simply averaging strata with unequal widths would generally be wrong.

For our squared function, a two-stratum calculation gives estimator variance nineteen over fourteen hundred forty. The two-independent-point baseline has variance two forty-fifths. Stratification therefore cuts the variance by a factor of about three point four for the same two evaluations. It improves the result because much of the variation in x squared across the interval comes from the large difference between the left and right halves. Stratification removes that between-half randomness while retaining the smaller within-half fluctuations.

With more strata, one can allocate more samples to regions with greater variability, provided the sample allocation and weighting are handled correctly. The best allocation may depend on unknown variances, which can be estimated using pilot samples. Stratification is a design principle: cover important subregions systematically while letting randomness work within each one.

## Third improvement: subtract something whose average we know

Suppose the expensive quantity is U squared, but we also know the exact average of U, which is one half. We can build a new random contribution by taking U squared, subtracting U, and adding back one half. The subtraction changes the fluctuation; the addition restores the correct mean.

This is a control variate. We subtract a variable whose expectation is known, multiplied by a coefficient, and add back its expectation times the same coefficient. No bias appears from this algebra if the coefficient is fixed independently of the estimation sample. The coefficient should be chosen to cancel as much correlated variation as possible.

For our example, a coefficient of one is optimal. It turns U squared into U squared minus U plus one half, exactly the same expression we saw in the antithetic pair calculation. But now, once U is drawn, only one expensive evaluation of U squared is needed, provided the value of U itself is cheap to compute. The one-sample variance falls from four forty-fifths to one one-hundred-eightieth: a factor of sixteen reduction for the expensive function evaluation.

We should not oversell this example. We calculated the optimal coefficient using the distribution of a function whose integral we already know. In a realistic computation, the optimal coefficient may be unknown. It can be estimated from independent pilot samples or handled with a careful statistical analysis if estimated from the same data. The lesson is not that all integrals become easy if we subtract a line. It is that a known, strongly correlated quantity can explain away substantial noise while leaving the target expectation unchanged.

## Fourth improvement: sample more often where the integrand matters

Our basic Monte Carlo algorithm samples U uniformly, so it spends equal effort in every equal-length part of the interval. But the function x squared contributes much more near one than near zero. Why not draw samples more often near one?

We can, but we must change the weights. Choose a new probability density q on the interval, positive wherever the original integrand contributes, and rewrite the integral as the expected value under q of the integrand divided by q. We now sample X from q and average the weighted values. This is importance sampling.

For a concrete example, choose q of x equal to two x on the unit interval. This density gives more weight to larger x. To generate a value from it, take the square root of a uniform random number. The cumulative probability up to x is x squared, so taking a square root inverts the cumulative function.

The new contribution is x squared divided by two x, which simplifies to x divided by two for positive x. The average of these weighted contributions still targets one third. Under the new density, the variance of a single contribution is one seventy-second. Compare that with the uniform-sampling variance four forty-fifths. We have reduced variance by a factor of six point four, without changing the number of expensive function evaluations.

But the weights are essential. If we sampled disproportionately near one and averaged the raw squares without correcting them, we would estimate the expectation under q, not the original integral. That would be a biased estimator for the target. Changing a sampling distribution without compensating for the change is not importance sampling; it is silently changing the problem.

## How importance sampling can fail spectacularly

It is possible for a weighted estimator to be unbiased but have infinite variance. Consider estimating the integral of the constant function one on the unit interval. The answer is exactly one. For no good reason, suppose we still sample from q of x equal to two x. The importance weight is now one divided by two x.

Its expectation under q is one, as required. But its squared expectation involves integrating one divided by x near zero, which diverges. The estimator has no finite variance, and the familiar finite-variance standard error formula is invalid. We have turned the easiest integral imaginable into a difficult random estimation problem just by choosing a bad sampling density.

This example makes the support and tail conditions concrete. A proposal density must not ignore a region where the integrand contributes. And even a proposal that is positive almost everywhere may be so small in an important region that its weights fluctuate violently. A sensible importance sampler gives enough probability to the important contributions without generating extreme inverse-density weights too often.

Rare-event estimation creates this tension in a practical form. If an event occurs only once in a million independent trials, crude simulation may draw thousands of samples without observing it. Deliberately oversampling the event region can make the computation possible, but only with correct weighting and careful control of weight variability.

## Choosing an estimator rather than just a sample size

We have now seen four different mechanisms. Antithetic sampling creates negatively related evaluations. Stratification forces coverage of separate regions. Control variates remove variation explained by a quantity with known mean. Importance sampling changes the sampling distribution and compensates with weights. All can preserve the same target expectation, and all need their own uncertainty calculation.

These methods can also be combined. But combinations introduce bookkeeping: which observations are independent, which are paired, how are strata weighted, and what random quantity is actually being averaged? If we naively treat all paired evaluations as independent, we will report the wrong standard error. If we count cheap algebraic operations as comparable to an expensive physical simulation, our cost comparison will be misleading. A fair benchmark measures accuracy against the real computational cost.

There is one more distinction worth keeping. Monte Carlo error arises from sampling randomness. A quadrature method may have deterministic approximation error. A simulation may also have time-step error, model error, and imperfectly estimated parameters. Variance reduction addresses one source of error: the sampling variance of a correctly specified estimator. It does not certify everything else.

The deeper skill is to start with the target quantity, then construct a random variable whose expectation equals it and whose variance is as small as is practical. Sampling is a tool for doing mathematics, not a replacement for deciding what mathematics the computation should represent. Once you can perform that construction, Monte Carlo becomes a family of designed estimators rather than a black box that returns a random-looking number.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Take \(I=\int_0^1 x^2\,dx=1/3\), \(U\sim\operatorname{Uniform}(0,1)\). Crude one-call Monte Carlo estimates \(I\) with \(U^2\) and variance \(4/45\).

### Antithetic pair: two evaluations

\[
A(U)=\frac{U^2+(1-U)^2}{2}=U^2-U+\frac12,
\quad EA=\frac13.
\]
Since \(E(U^2-U+1/2)^2=7/60\) and \((EA)^2=1/9\),
\[
\operatorname{Var}(A)=\frac7{60}-\frac19=\frac1{180}.
\]
For two independent crude draws, variance of their average is \((4/45)/2=2/45\), eight times \(1/180\).

### Two equal-width strata: two evaluations

Draw \(U_1\sim\operatorname{Uniform}(0,1/2)\), \(U_2\sim\operatorname{Uniform}(1/2,1)\) independently. Set \(S=(U_1^2+U_2^2)/2\). Then \(ES=I\). Direct integration yields
\[
\operatorname{Var}(U_1^2)=\frac1{180},\quad
\operatorname{Var}(U_2^2)=\frac{17}{360},\quad
\operatorname{Var}(S)=\frac14\left(\frac1{180}+\frac{17}{360}\right)=\frac{19}{1440}.
\]
The two-independent-point crude variance is \(2/45=64/1440\), so this stratification improves it by a factor \(64/19\approx3.37\).

### Control variate: one expensive function call

For known \(EU=1/2\), use
\[
C_\beta(U)=U^2-\beta(U-1/2),\qquad E[C_\beta]=I.
\]
The minimum-variance coefficient is
\[
\beta^*=\frac{\operatorname{Cov}(U^2,U)}{\operatorname{Var}(U)}
=\frac{1/12}{1/12}=1,
\]
so \(\operatorname{Var}(C_1)=1/180\), sixteen times smaller than \(\operatorname{Var}(U^2)=4/45\). If \(\beta\) is estimated from the same observations, exact finite-sample unbiasedness and standard-error formulas require fresh analysis; an independent pilot estimate keeps conditional unbiasedness.

### Importance sampling: one expensive function call

Take \(q(x)=2x\) on \((0,1)\), \(X=\sqrt U\) for \(U\sim\operatorname{Uniform}(0,1)\). Then
\[
I=E_q\left[\frac{X^2}{2X}\right]=E_q[X/2],\quad
E_q[X]=\frac23,\quad E_q[X^2]=\frac12,
\]
\[
\operatorname{Var}_q(X/2)=\frac14\cdot\frac12-\left(\frac13\right)^2
=\frac1{72}.
\]
The crude variance divided by importance variance is \((4/45)/(1/72)=6.4\).

**Bad importance distribution:** with target \(\int_0^1 1\,dx=1\) but the same \(q(x)=2x\), the weight is \(W=1/(2X)\). Then \(E_q W=1\) yet
\[
E_q W^2=\int_0^1\frac1{4x^2}(2x)\,dx=\frac12\int_0^1\frac{dx}{x}=\infty.
\]
The estimator is unbiased but has infinite variance.

### Exercises with worked answers

1. **Support.** Why is a proposal density equal to zero on a region with positive contribution invalid for ordinary importance sampling? **Answer:** the missing region cannot be sampled and the importance ratio cannot account for its contribution.
2. **Pairing.** If \(f(u)=u\), what is the antithetic pair estimate \([f(U)+f(1-U)]/2\)? **Answer:** exactly \(1/2\) for every U, zero variance.
3. **Stratum weights.** If strata have widths \(1/4\) and \(3/4\), and one observation is drawn from each, how do we combine the function values? **Answer:** with weights \(1/4\) and \(3/4\); their unweighted average generally targets the wrong integral.
4. **Cost.** How many times as many crude independent evaluations are needed to match a sixteenfold variance reduction? **Answer:** sixteen times as many, under equal cost per evaluation.
5. **Bad weights.** Explain why finite expected importance weight does not guarantee the validity of the usual Monte Carlo standard error. **Answer:** its second moment can diverge, as in the constant-function counterexample.

### Reading and attribution

- Art B. Owen, *Monte Carlo Theory, Methods and Examples*, Chapters 8–9: variance reduction and importance sampling (https://artowen.su.domains/mc/).
- MIT OpenCourseWare 15.450, *Analytics of Finance*, Lecture 3: Simulation Methods, including variance reduction.
- T. Budd, *Monte Carlo Techniques*, lecture 3: direct-sampling Monte Carlo integration and importance sampling (https://hef.ru.nl/~tbudd/mct/lectures/monte_carlo_integration.html).
