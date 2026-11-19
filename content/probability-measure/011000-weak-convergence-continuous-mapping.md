# 011000 - Weak Convergence: When Distributions Approach a Limit

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** random variables, probability distributions, continuous functions, and laws of large numbers. **Theme:** convergence of distributions is not convergence of realizations, nor a guarantee about expectations of unbounded quantities.

<!-- BEGIN SPOKEN LECTURE -->

# Weak Convergence: When Distributions Approach a Limit

Suppose a simulator produces a random response time. As its numerical resolution increases, the histogram of response times settles into a familiar shape. What exactly has converged? Have individual simulated paths approached fixed paths? Have the averages converged? Can we safely pass the limit through every function of the response time? These sound like variations of one question, but probability theory answers them with different notions of convergence.

One of the most useful is convergence in distribution, also called weak convergence of probability laws. It is the language in which a central limit theorem is naturally stated. It also describes scaling limits, approximations to stochastic processes, and cases where two random quantities are not even defined on the same underlying probability space. But that flexibility comes with a price: weak convergence does less than many of its informal descriptions suggest.

To build intuition, imagine repeatedly adding smaller measurement noise to an instrument. At stage n the noise is always exactly one divided by n. The output is uncertain only if the underlying signal is uncertain; the noise itself is a deterministic shift that shrinks to zero. The distribution of the reported output moves closer to the distribution of the true signal. That is an example where several convergence notions agree. More instructive examples expose where they part company.

## Different convergence questions

If a sequence of random variables is defined on one common probability space, we might ask whether the actual outcomes get close. Convergence in probability says that, for every positive tolerance, the probability of an error exceeding that tolerance tends to zero. It does not insist on convergence along every sample path. Almost-sure convergence is stronger: with probability one, a typical path eventually remains within every specified tolerance.

Convergence in distribution asks something else. Each random variable has a probability law. We ask whether these laws converge, even if the random variables were generated in different experiments and share no sample path. A sequence of distributions can converge without a natural way to compare the individual outcomes one by one.

The standard real-valued definition says that the cumulative distribution functions converge at every continuity point of the limiting cumulative distribution function. The word continuity is not incidental. At a point where the limit law has a mass, the limiting distribution function can jump, and convergence of its approximate values exactly at that point need not hold.

For example, let every random variable at stage n be the deterministic number one divided by n, and let the limit be zero. For any fixed positive threshold, eventually the number lies below it, and for any negative threshold it never does. The laws converge to a point mass at zero. But at the threshold zero, the approximating probability of being at most zero is always zero, whereas the limiting probability is one. The definition deliberately does not demand agreement at this discontinuity.

That may seem like a picky exception, but it is telling us what distributions can and cannot reveal. A probability mass can approach a boundary from one side. Whether an event includes its exact boundary may then change discontinuously even though everything nearby behaves smoothly.

## A same-distribution counterexample

Here is a sharper distinction. Draw a fair coin and call the result X, with zero for tails and one for heads. Define a second random variable Y as one minus X. Whenever X is one, Y is zero; whenever X is zero, Y is one. Their distributions are identical. Both are fair binary variables.

Now set every member of a sequence equal to Y, and ask whether the sequence converges in distribution to X. It does, trivially, because every term and the proposed limit have exactly the same law. Yet the actual sequence never gets close to X: the difference between Y and X is exactly one on every outcome. There is no convergence in probability to X.

This example is intentionally stark. Weak convergence compares marginal distributions, not the coupling between a sequence and a proposed limit on a shared sample space. The random variables may be maximally opposed on every trial while remaining distributionally indistinguishable. A statement about laws cannot, by itself, recover how individual outcomes were paired.

There is an important positive implication. If random variables converge in probability to X on a common space, then they converge in distribution to the law of X. The reverse implication fails, as the coin example shows. Almost-sure convergence implies convergence in probability, but the converse also generally fails without additional hypotheses. These arrows should not be casually reversed.

## Testing laws with continuous observations

The distribution-function definition is efficient for a single real-valued variable. A more flexible definition uses test functions. A sequence of probability laws converges weakly to another law when the expected value of every bounded continuous test function under the sequence converges to its expected value under the limiting law.

Think of a bounded continuous test as a smooth sensor placed on the distribution. It assigns a number to each possible outcome, but its reading cannot jump abruptly when the outcome moves a tiny amount. Weak convergence says that all such averaged sensor readings approach their limiting readings. The boundedness prevents enormous contributions from rare extreme outcomes.

Why do we need every bounded continuous test, rather than only the mean? Because two very different distributions may have the same mean. One may concentrate at zero and another may place half its mass at minus one and half at plus one. Both average to zero, but a continuous function sensitive to squared magnitude distinguishes them. A sufficiently rich family of tests captures the law rather than one of its summaries.

Conversely, why not require convergence for every measurable test function? The threshold indicator at zero in our shrinking-deterministic example is measurable but discontinuous. Its expectation fails to converge. A definition demanding every measurable test would rule out a simple approximation that we want to recognize as distributional convergence.

These two descriptions, through distribution functions and bounded continuous tests, are equivalent for real-valued probability distributions. The equivalence is part of the portmanteau theorem, which also gives useful statements about open sets, closed sets, and events whose boundaries have zero limiting probability. The details of the boundary condition are what make the theorem safe to use.

## A proof by continuous composition

One of the most useful consequences is the continuous mapping theorem. If a sequence of real-valued random variables converges in distribution to X and a function g is continuous, then applying g to the sequence preserves convergence in distribution toward g of X. There are broader versions allowing discontinuities on a set that the limiting law gives probability zero, but continuity everywhere is a clean starting point.

The test-function definition explains the proof in a single idea. To inspect the distribution of g applied to the random variable, take any bounded continuous test function h on the output of g. Then the composition h of g is a bounded continuous test function on the original input, as long as g is continuous. Weak convergence of the original variables tells us that the expectations of these composed tests converge. That is exactly the definition of weak convergence for the transformed variables.

This proof is not a mechanical algebra trick. It shows why continuity is the correct interface between a distributional approximation and a downstream calculation. A continuous transformation cannot turn tiny shifts in the input into a sudden jump of the output. If the transformation can jump at a point that carries limiting probability, the theorem's simple reasoning no longer applies.

Take the deterministic variables one divided by n approaching zero. Define g to return one for a positive argument and zero otherwise. Every approximating input is positive, so the transformed output is always one. The limiting input is zero, so the transformed output is zero. The transformed laws do not converge to the proposed transformed limit. We have found the missing hypothesis: g is discontinuous at zero, precisely where the limit law is concentrated.

This matters in applied work. A smooth transformation of an approximate distribution is often legitimate. A hard threshold, optimizer's argmax, indicator of a rare event, or discontinuous decision rule may need a separate argument. A weak limit does not automatically validate every downstream yes-or-no decision.

## The central limit theorem in its proper language

Consider independent identically distributed observations with a finite mean and a finite, positive variance. Their sample average approaches the population mean, under the law of large numbers. But that only says the typical estimation error becomes small. It does not describe the shape of the remaining fluctuations.

The central limit theorem addresses those fluctuations. Center the sample sum by subtracting its expected total, then scale by the square root of the number of observations and the standard deviation. Under the usual assumptions, the resulting distribution approaches the standard normal distribution. This is weak convergence: the probability laws of the standardized errors approach a normal law.

An instructor may draw a bell curve and say the sample mean becomes approximately normal. That is a useful picture, but the exact theorem is not the claim that the underlying observations become normal, nor that individual standardized sums converge pathwise to one fixed normal random variable. It is an asymptotic statement about distributions of properly scaled sums.

It is also not a guarantee that a normal approximation is accurate at a particular sample size. That question requires a finite-sample error bound or other information about the tail shape. Heavy-tailed distributions can converge slowly, even when the variance exists. The central limit theorem gives an eventual limit under its hypotheses, not an automatic practical sample-size certificate.

The relationship between the law of large numbers and the central limit theorem is worth hearing clearly. The law of large numbers focuses on an average without amplifying its fluctuation; it says the average settles. The central limit theorem magnifies the remaining error by a square-root factor and describes its limiting distribution. They ask different questions of the same observations.

## When expectation refuses to follow the law

Now consider rare catastrophes. At stage n, a random loss is zero with probability one minus one divided by n and equals n squared with probability one divided by n. The chance of any positive loss tends to zero. So the random loss converges in probability, hence in distribution, to zero.

Yet its expected value is n, which grows without bound. The law is becoming concentrated at zero while a rarer and larger tail dominates the mean. Therefore weak convergence does not imply convergence of expectations for unbounded functions, and even convergence in probability does not repair that problem.

This is why the definition uses bounded continuous test functions. To extend convergence to unbounded observables, we need additional control over tails. One common condition is uniform integrability. Roughly speaking, it says that the expected contribution from very large values can be made uniformly small across the whole sequence.

For a family of integrable random variables, uniform integrability is not the same as bounded means. It specifically controls tail contributions. The rare-catastrophe example fails it spectacularly. The expected contribution from values beyond any fixed cutoff eventually becomes arbitrarily large.

A particularly useful result says that convergence in probability together with uniform integrability yields convergence in the first-mean sense, and therefore convergence of expectations. A related theorem states that weak convergence plus suitable uniform integrability and suitable moment control allows certain unbounded expectations to pass to the limit. The exact formulations matter; one should name the chosen functions and tail conditions rather than merely saying that the distributions converge nicely.

## Empirical distributions and the problem of inference

Weak convergence is not only a language for analytic limits. It appears whenever we approximate a population distribution from data. Suppose we observe independent draws from a fixed distribution. The empirical distribution assigns equal probability to each observed value. Its cumulative distribution function at a threshold is simply the fraction of observations at or below that threshold.

For a fixed threshold, this fraction is an average of independent binary indicators. The law of large numbers says it approaches the true probability of lying below that threshold. We can apply the strong law simultaneously to all rational thresholds because there are only countably many rational numbers. Monotonicity of distribution functions then lets us extend the conclusion to every continuity point of the true distribution function.

That is a route to almost-sure weak convergence of the empirical distribution toward the population distribution for independent identically distributed real-valued observations. The stronger Glivenko–Cantelli theorem gives uniform convergence of the empirical cumulative distribution function over all real thresholds. But the elementary proof idea already shows how integration, countability, and monotonicity work together.

There is a very important modeling boundary. The observations must represent the distribution that the theorem claims to estimate. If the experiment samples only working machines, it cannot discover the distribution of all machines by invoking a limit theorem. And if observations are highly dependent or the data-generating process changes over time, an iid theorem cannot be transferred unchanged.

Suppose a researcher draws one thousand images from a dataset whose collection process systematically excluded a category. The empirical distribution may be extremely close to the dataset's distribution and still poorly represent the world. Statistical convergence does not repair selection bias. It gives precise results conditional on the sampling model.

## What a probability limit cannot promise

Three classes of statements need separate treatment. A path statement asks what happens to coupled realizations. A distributional statement asks how laws compare. A numerical expectation statement asks whether integrals of a given function pass through a limit. One may support another under hypotheses, but they are not interchangeable.

The same distinction governs probabilistic algorithms. Suppose a randomized algorithm has outputs whose distributions converge to a target law as a tolerance shrinks. That does not guarantee that running the algorithm twice with shared randomness produces close outputs. Nor does it guarantee that an unbounded loss has the right expected value. To prove those extra properties, we need a coupling, moment control, or a different approximation theorem.

A common source of confusion is the phrase “convergence to a random variable.” Convergence in law is best heard as convergence to **the distribution** of that random variable. The particular representative of that distribution need not live on the same probability space, and any proposed pathwise relationship is extra structure. By contrast, convergence in probability requires the random variables to be jointly realized so their differences make sense.

The practical checklist is short. Which quantity converges: outcomes, probabilities of events, or expected losses? Does the event have a boundary where the limit law places mass? Is the downstream map continuous at the relevant points? Are unbounded tails controlled? And what assumptions tie the observed data to the proposed distribution?

Weak convergence is powerful precisely because it gives a clear answer to one of these questions without pretending to answer them all. It says that probability laws approach one another in the sense detected by bounded continuous observations. From there, further conclusions are possible, but each earns its own theorem and its own hypotheses.


## Characteristic functions as another way to recognize a limit

There is a useful analytic route to weak convergence that does not begin with cumulative distributions. Given a real random variable, take the expected value of a complex exponential whose phase is the random variable multiplied by a chosen frequency. The resulting function of frequency is called the characteristic function. It encodes the entire probability law, even though its values are complex numbers.

For independent random variables, the characteristic function of their sum is the product of their individual characteristic functions. This is the same factorization principle that makes convolution the natural operation for adding independent random quantities. It also creates a convenient proof strategy for the central limit theorem: rather than handling every possible threshold directly, analyze a product of functions near frequency zero.

After subtracting the mean and scaling to unit variance, the characteristic function of one observation has a quadratic approximation near zero. For a standardized sum of n independent identically distributed observations, the characteristic function is the n-th power of the individual characteristic function evaluated at a frequency divided by the square root of n. The second-order term survives in the limit, and the higher-order remainder vanishes under the theorem's regularity assumptions. The resulting characteristic function is the Gaussian one. A continuity theorem for characteristic functions turns that analytic limit into weak convergence of laws.

This argument explains why the Gaussian appears: independent summands turn the analytic object for the sum into a product, and finite variance determines the quadratic behavior around zero. It does not claim that every repeated sum is Gaussian. Infinite-variance distributions can have different stable limits; strong dependence and changing distributions can change the scaling or prevent a Gaussian limit entirely.

## Quantiles and decisions at a boundary

Suppose we use the ninety-fifth percentile of a response-time distribution as a service threshold. If approximate distributions converge weakly, does their ninety-fifth percentile necessarily converge to the target percentile? Not without assumptions near that quantile. The limiting distribution might have a flat portion or an atom, allowing small changes in the distribution to shift a selected quantile substantially or make it ambiguous under competing conventions.

Under suitable local conditions, such as a uniquely identified percentile where the limiting cumulative distribution crosses the desired probability level without a flat ambiguity, quantile consistency can be proved. But it is not a consequence of weak convergence in complete generality without checking those conditions. This is another example of a downstream functional that can be unstable at a special configuration of a distribution.

The same caution applies to probabilities of events. The portmanteau theorem guarantees convergence for events whose boundaries have zero probability under the limiting law. For an event defined by “response time is at most five seconds,” that boundary is the single threshold value. If the limiting distribution has no atom at five, weak convergence supports convergence of the event probability. If a positive amount of probability mass sits exactly at five, the approximation can approach the threshold from either side and the conclusion can fail.

These are not artificial exceptions. Discrete measurements, rounded scores, and hard classification thresholds create atoms and ties naturally. A validation pipeline that uses weak approximation to justify a binary operational decision must examine the decision boundary, not merely the smooth part of the histogram.

## What a stronger approximation would buy

Sometimes a proof constructs approximating random variables and the proposed limit on one common probability space in a way that yields almost-sure convergence. That kind of coupling provides far more pathwise information than weak convergence alone. On suitable metric spaces, representation theorems can sometimes construct such coupled copies from weakly converging laws, but the constructed copies need not be the original random variables on the original experimental probability spaces.

The distinction explains why coupling arguments are valuable in probability and simulation. They may turn a distributional approximation into a statement about discrepancies on a specifically constructed joint experiment. But one must report the coupling that was constructed and which quantity it controls. The fact that a coupling exists somewhere is not the claim that a user's original paired simulation outputs were close.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For random variables \(X_n,X\) defined on a common probability space, \(X_n\to X\) in probability means
\[
\forall\varepsilon>0:\ P(|X_n-X|>\varepsilon)\to0.
\]
Weak convergence \(X_n\Rightarrow X\) is equivalently characterized by
\[
E[h(X_n)]\to E[h(X)]\qquad\text{for every bounded continuous }h:\mathbb R\to\mathbb R,
\]
or by \(F_n(x)\to F(x)\) at continuity points of \(F\).

**Counterexamples.** With \(X\sim\operatorname{Bernoulli}(1/2)\) and \(X_n=1-X\), each \(X_n\overset d=X\), yet \(P(|X_n-X|>1/2)=1\). With \(X_n\equiv1/n\) and \(g(x)=\mathbf1_{x>0}\), \(X_n\Rightarrow0\) but \(g(X_n)\not\Rightarrow g(0)\).

**Continuous mapping.** For continuous \(g\), if \(X_n\Rightarrow X\), then for every bounded continuous \(h\), \(h\circ g\) is bounded continuous, so
\[
E[h(g(X_n))]\to E[h(g(X))].
\]
Thus \(g(X_n)\Rightarrow g(X)\). The broader theorem permits discontinuities on a set having \(P_X\)-measure zero.

**Means need tail control.** If \(P(X_n=n^2)=1/n\), \(P(X_n=0)=1-1/n\), then \(X_n\to0\) in probability while \(EX_n=n\to\infty\). Uniform integrability plus convergence in probability gives \(L^1\) convergence.

**Empirical CDF.** \(F_n(x)=n^{-1}\sum_{i=1}^n\mathbf1_{\{X_i\le x\}}\). For iid observations, the strong law on rational thresholds and monotonicity yield pointwise convergence at continuity points of \(F\); the Glivenko–Cantelli theorem strengthens this to \(\sup_x|F_n(x)-F(x)|\to0\) almost surely.

### Exercises with answers

1. **Jump point.** Why can \(F_n(0)\) fail to converge when \(X_n\equiv1/n\Rightarrow0\)? **Answer:** the limit CDF is discontinuous at zero.
2. **Coupling.** Can identical marginal laws imply two variables are close on the same sample space? **Answer:** no; a complementary Bernoulli pair differs everywhere.
3. **Tail risk.** Does convergence in probability to zero imply convergence of means? **Answer:** no; the rare \(n^2\)-valued example has mean n.
4. **Mapping.** State the sufficient condition used for mapping weak limits through \(g\). **Answer:** continuity of \(g\) everywhere (or almost everywhere under the limiting law in the general theorem).
5. **Sampling model.** Why can't an empirical CDF theorem fix a dataset with systematic exclusions? **Answer:** it converges to the sampled distribution, not an unobserved target population without additional assumptions.

### References

- MIT OpenCourseWare 18.175, *Theory of Probability*, lectures 12, 14–16 on weak convergence and central limit theory.
- Patrick Billingsley, *Convergence of Probability Measures*, second edition, for portmanteau and mapping theorems.
- Achim Klenke, *Probability Theory: A Comprehensive Course*, convergence in distribution and modes of convergence.
