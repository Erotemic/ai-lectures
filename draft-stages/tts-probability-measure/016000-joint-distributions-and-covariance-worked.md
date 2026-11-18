# 016000 - Joint Distributions and Covariance, Calculated Rather Than Memorized

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** elementary probability, fractions, expectation and variance. **Theme:** dependence, joint laws, conditional distributions, covariance and uncertainty in sums.

<!-- BEGIN SPOKEN LECTURE -->

# Joint Distributions and Covariance, Calculated Rather Than Memorized

Imagine measuring a machine twice, using two instruments that report either a warning or no warning. One instrument has a fifty percent warning rate. So does the other. Does that tell us the probability that both will warn? Not at all. Their warnings might almost always happen together, might rarely happen together, or might be completely unrelated. Two individual probability distributions do not determine how their outcomes are paired.

That missing information is what a joint distribution describes. We will calculate one from the ground up, then use it to understand covariance, conditional probability, and the uncertainty of sums and averages. None of this requires a theorem about infinitely many measurements. We need only the arithmetic of a four-cell table, followed by a careful reading of what those four numbers mean.

## One experiment, two measurements

Suppose we watch two warning lights on randomly selected operating cycles. Record a one for a warning and a zero for no warning. Name the measurements X and Y. Their joint distribution is described by four possible pairs. The probability of no warning on either light is three eighths. The probability that only Y warns is one eighth. The probability that only X warns is also one eighth. The probability that both warn is three eighths.

First check the total. Three eighths plus one eighth plus one eighth plus three eighths equals one. These are probabilities of mutually exclusive and exhaustive possibilities, so their sum must be one.

The probability that X warns is the probability of the two pairs where X equals one. That is one eighth plus three eighths, or one half. By symmetry, Y warns half the time as well. These are the marginal distributions: we add over the value of the variable we are not currently studying.

But the chance of both warnings is three eighths, not one quarter. If X and Y were independent, half times half would give one quarter. Our table says simultaneous warnings occur more often than independence predicts. Knowing that one light has warned genuinely changes the probability of the other.

Condition on X being one. Among those cycles, the probability that Y is also one is three eighths divided by one half: three quarters. Condition instead on X being zero. Then Y warns with probability one eighth divided by one half: one quarter. The same light, Y, has two very different warning probabilities depending on which information we have. Conditional probability is not an extra kind of randomness. It is probability restricted to the part of the experiment that is known.

## The distribution of a sum

Now define T to be X plus Y: the number of warning lights. T can be zero, one, or two. Zero occurs with probability three eighths. One occurs in either of the off-diagonal cases, for a total probability of one quarter. Two occurs with probability three eighths.

Its expectation is zero times three eighths, plus one times one quarter, plus two times three eighths. That makes one warning per cycle on average. We could have obtained this more quickly: the expectation of X plus Y is the expectation of X plus the expectation of Y, or one half plus one half. Linearity of expectation never required independence.

But consider the variance of T. The mean is one. Relative to that mean, zero warnings is one below, one warning is exactly at the mean, and two warnings is one above. Squared deviations are one, zero, and one. Their weighted average is three eighths plus three eighths, or three quarters.

If we had incorrectly treated the lights as independent, we would have added their separate variances, each one quarter, to obtain one half. That would underestimate the variability of the total. The missing term is covariance.

## Covariance from the table

Covariance asks whether two quantities tend to be above their means at the same time, or whether a high value of one tends to accompany a low value of the other. We subtract each mean and multiply the two centered values. Then we take the expectation of that product.

There is a useful shortcut. The covariance equals the expectation of the product X times Y, minus the product of their expectations. In our binary example, X times Y equals one only when both lights warn. So the expectation of their product is three eighths. The product of their means is one quarter. Subtracting gives one eighth.

That positive one-eighth covariance accounts exactly for the extra variance in the warning count. The variance of X plus Y is the variance of X plus the variance of Y plus twice their covariance. One quarter plus one quarter plus twice one eighth equals three quarters, matching the direct distribution of T.

To distinguish the size of a covariance from the units used to measure variables, we divide by the product of their standard deviations. This gives correlation. Each Bernoulli indicator here has variance one quarter and standard deviation one half. Their standard deviations multiply to one quarter. Covariance one eighth divided by one quarter gives correlation one half.

A correlation of one half describes a positive linear association, not a fifty percent chance of some particular event. The probability of both warnings is three eighths, and the probability of Y warning given X warns is three quarters. These are different quantities. Correlation is a standardized covariance, not a conditional probability.

## Subtraction makes the opposite pattern visible

What if we cared about disagreement between the instruments, not their total? Define D as X minus Y. The possible values are negative one, zero, and positive one. The lights disagree with total probability one quarter: one eighth for each direction. Therefore D has mean zero and variance one quarter.

We can recover that variance without making another distribution table. The variance of X minus Y equals the two individual variances minus twice the covariance. One quarter plus one quarter minus one quarter leaves one quarter. The same positive covariance that made the sum variable makes the difference relatively stable. If two measurements respond to a shared disturbance, adding them amplifies some of that shared variation while subtracting can cancel it.

You will encounter this principle when comparing before-and-after measurements on the same person, differences between nearby sensors, and paired randomized experiments. Pairing is useful not because we have magically made measurements independent, but because the dependence can be exploited to remove shared noise. Whether that helps depends on the sign and strength of the covariance.

## What zero covariance does not tell us

It is tempting to reverse the implication. Independent square-integrable variables have covariance zero, so perhaps zero covariance means independence. That is false.

Choose X uniformly from negative one, zero, and positive one. Now define Y to be X squared. If X is zero, Y is zero. If X is either negative one or positive one, Y is one. Y is completely determined by X, so the variables certainly are not independent.

Nevertheless, X has mean zero. The product X times Y equals X cubed, whose average is also zero by symmetry. Therefore the covariance of X and Y is zero. The relationship is nonlinear: Y changes with the magnitude of X, not its signed direction. Ordinary covariance cannot see that pattern. A scatter plot or the full joint distribution will reveal it immediately.

This distinction matters whenever a statistical method relies on uncorrelatedness. A method may have removed linear relationships while retaining more complicated dependence. Conversely, two variables can have a nonzero covariance without one causing the other. A common hidden influence can move both.

## The variance of an average

Suppose instead that we observe n measurements of the same quantity, each with variance sigma squared. The variance of their average is the variance of their sum divided by n squared. When the measurements are independent, all cross-covariances vanish, leaving n copies of sigma squared. The variance of the average becomes sigma squared divided by n. Its standard deviation, called the standard error, falls as one divided by the square root of n.

But the independence qualification is the whole story. If every pair of distinct measurements has the same covariance c, then the variance of the average is sigma squared divided by n, plus c times the fraction n minus one over n. For a positive persistent covariance, collecting more measurements may leave an appreciable uncertainty floor.

Imagine measuring the temperature of a room a hundred times in a minute using the same miscalibrated thermometer. Repeated readings may reduce the independent electronic noise, but they cannot average away an unknown calibration offset shared by every reading. An average is reliable only to the extent that its sources of error really vary across observations.

The general lesson is that random variables belong to joint experiments. Their separate averages and spreads are useful summaries, but not a substitute for knowing how they interact. Joint distributions let us calculate exact combined probabilities. Covariance tells us how linear dependence alters a sum, a difference, or an average. When we later estimate an integral by randomly sampling many inputs, these same calculations will determine whether more samples truly buy us more precision.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### The complete joint experiment

For binary indicators \(X,Y\), write

| \(X\) | \(Y\) | Probability |
|---:|---:|---:|
| 0 | 0 | \(3/8\) |
| 0 | 1 | \(1/8\) |
| 1 | 0 | \(1/8\) |
| 1 | 1 | \(3/8\) |

\[
E[X]=E[Y]=\tfrac12,\quad E[XY]=\tfrac38,\quad
\operatorname{Cov}(X,Y)=\tfrac38-\tfrac14=\tfrac18,
\quad \operatorname{Corr}(X,Y)=\tfrac12.
\]

\[P(Y=1\mid X=1)=\frac{3/8}{1/2}=\frac34,\quad
P(Y=1\mid X=0)=\frac{1/8}{1/2}=\frac14.\]

If \(T=X+Y\), then \(P(T=0)=3/8\), \(P(T=1)=1/4\), \(P(T=2)=3/8\); \(ET=1\), \(\operatorname{Var}(T)=3/4\). Meanwhile \(D=X-Y\) satisfies \(ED=0\) and \(\operatorname{Var}(D)=1/4\).

### Deriving the variance identity

For square-integrable variables,
\[
\begin{aligned}
\operatorname{Var}(X+Y)&=E[((X-EX)+(Y-EY))^2]\\
&=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y),\\
\operatorname{Var}(X-Y)&=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y).
\end{aligned}
\]
For \(\bar X=n^{-1}\sum_i X_i\), without independence:
\[
\operatorname{Var}(\bar X)=\frac1{n^2}\left(\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)\right).
\]
For common variance \(\sigma^2\) and common pairwise correlation \(\rho\), this becomes
\[\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}(1+(n-1)\rho).\]
Positive semidefiniteness limits admissible \(\rho\): an equicorrelation matrix for \(n\) variables requires \(-1/(n-1)\le \rho\le 1\).

### Exercises with worked answers

1. **Reweighting.** Keep the same marginals, but assign independent cell probabilities \(1/4\) each. What happens to the variance of \(X+Y\)? **Answer:** covariance is zero; \(\operatorname{Var}(X+Y)=1/2\).
2. **Paired difference.** If \(\operatorname{Var}(A)=9\), \(\operatorname{Var}(B)=4\), and \(\operatorname{Cov}(A,B)=3\), compute \(\operatorname{Var}(A-B)\). **Answer:** \(9+4-6=7\).
3. **Uncorrelated is not independent.** For \(X\) uniform on \(\{-1,0,1\}\) and \(Y=X^2\), calculate \(E[XY]\), \(EX\), \(EY\). **Answer:** \(E[XY]=0\), \(EX=0\), \(EY=2/3\); covariance is zero though \(Y\) is determined by \(X\).
4. **Repeated measures.** With \(n=20\), \(\sigma^2=1\), \(\rho=0.1\), find the variance of the average. **Answer:** \((1/20)(1+19/10)=0.145\), not \(0.05\).

### Reading and attribution

- MIT OpenCourseWare 18.600, *Probability and Random Variables*, joint distributions and expectation.
- Blitzstein and Hwang, *Introduction to Probability*, joint distributions, covariance, independence and conditional probabilities.
- The preceding probability track manuscripts 003000 and 006000 introduce expectation and the distinction between independence and concentration; this lecture supplies worked joint-law computations.
