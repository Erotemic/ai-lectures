# 003000 - Random Variables, Distributions, and Expectation: Turning Outcomes into Quantities

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** events, fractions, elementary functions. **Theme:** random variables as measurable functions, pushforward distributions, expectation, variance, indicator variables, and bounds.

<!-- BEGIN SPOKEN LECTURE -->

# Random Variables, Distributions, and Expectation: Turning Outcomes into Quantities

Suppose two people examine the same roll of two dice. One cares about their sum. Another cares only about whether the sum exceeds eight. A third cares about the square of the first die. Each person watches the same underlying experiment but extracts a different number from it. In probability, those extracted quantities are random variables. The name can be misleading: a random variable is a function, and once the underlying outcome is fixed, its value is fixed too.

This distinction is the foundation for a great deal of statistics and applied mathematics. We start with a probability model over possible outcomes. We define a function that measures some feature of the outcome. The probabilities of the resulting values form a distribution. From that distribution we can calculate averages, uncertainties, tail risks, and comparisons between decisions.

Our goal is to understand these constructions as mathematical objects rather than memorized formulas. We will develop discrete and continuous examples, explain why expectation is a weighted average and more generally an integral, and prove a useful inequality that turns an average into a bound on a rare event. Along the way we will see why independent variables are convenient, but not required for many of the most important calculations.

## Outcomes and measurements are different things

Let the sample space for two fair dice contain the thirty-six ordered pairs. An outcome might be first die two and second die five. That outcome is a complete record of the experiment, as far as our simple model is concerned.

Now define X to be the sum of the dice. For the outcome two and five, X equals seven. Define Y to be the indicator that the sum exceeds eight. For the same outcome, Y equals zero. Define Z to be the first die squared. For that outcome, Z equals four. X, Y, and Z are different functions on the same sample space.

We call them random variables because their values vary across possible random outcomes. We need not pretend that the mathematical functions themselves are wandering unpredictably. The probability is on the underlying outcomes; the functions carry it forward to their outputs.

For X, several outcomes may produce the same sum. There is one ordered pair producing sum two, two pairs producing sum three, and six pairs producing sum seven. The distribution of X records the total probability of all outcomes mapped to each possible sum. For sum seven, there are six favorable ordered pairs among thirty-six, so the probability is one-sixth.

This distribution is a new description of the original experiment. It forgets which pair of dice produced the sum. If the only question we ever ask is about sums, that loss of information is harmless. If we later care about the first die specifically, the sum alone may not contain enough information. A random variable extracts exactly the feature its definition names.

## The probability mass function

For a discrete random variable, a probability mass function assigns a probability to each possible value. For a single fair die, the mass at each integer from one through six is one-sixth. Outside those six values, the mass is zero. The masses must be nonnegative and sum to one.

We can compute the probability of a set of values by adding their masses. For the die, the event that the result is at least five has probability one-sixth plus one-sixth, or one-third. For the sum of two dice, the probability of seven is one-sixth even though the individual outcomes were each one-thirty-sixth. The distribution has aggregated all outcomes with the same measured value.

In a mathematical notation, the distribution of X assigns to each set B the probability that X lands in B. This may be called the pushforward of the original probability measure along X. The phrase sounds abstract, but the construction is simple: look backward through the function to find which underlying outcomes yield outputs in B, then take the probability of that event.

This perspective will be useful when distributions become continuous. We will not need to invent a new meaning of probability for values of real-valued variables. We will still measure the probability of the underlying outcomes whose mapped values lie in a set. The function and the probability measure work together.

## A cumulative account of the distribution

There is another way to describe a random variable: ask for the probability that it is at most a given threshold. This is the cumulative distribution function. It exists for every real-valued random variable, regardless of whether the variable is discrete, continuous, or mixed.

For a fair die, the cumulative probability is zero below one. Between one and two it is one-sixth. Between two and three it is two-sixths, and so on, until it reaches one at six. The graph is a staircase. The jumps have sizes equal to the probability masses at the corresponding values.

For a continuous uniform variable on the interval from zero to one, the cumulative function rises linearly from zero to one. At a threshold of one-quarter, the probability of being at most that threshold is one-quarter. At three-quarters, it is three-quarters. Here there are no point masses; the probability of any one exact real number is zero.

That last point is often surprising. An outcome still takes some value, but no individual real number has positive probability under this continuous model. Probability resides in intervals and other measurable sets. Saying that each exact value has probability zero does not say that no value occurs. It says that the mass is distributed continuously across infinitely many possibilities.

The cumulative distribution function can also handle cases that are neither purely discrete nor smoothly continuous. For example, a device may report exactly zero with positive probability because it is turned off, and otherwise produce a continuous reading. The cumulative function has a jump at zero and a continuous part elsewhere. This versatility is why it is a foundational representation rather than merely a plotting convenience.

## Expected value is a weighted average

For a fair die X, the expected value is the average of one, two, three, four, five, and six, each weighted by probability one-sixth. The result is three and a half. This does not predict that a single roll will produce three and a half. It is the mean value under the probability distribution, the center of mass of the six possible numerical outcomes.

Imagine placing a small weight at each possible value on a number line. The weight is proportional to the probability of that value. The expected value is the balancing point. For a discrete random variable, we calculate it by multiplying each possible value by its probability and adding the products. This is a weighted sum, with the ordinary arithmetic average as the special case of equal weights.

For a continuous variable with a density, the sum becomes an integral. We multiply the possible value by its density and integrate across the domain. More generally, expectation is integration with respect to the variable's probability distribution. The mathematical framework can accommodate distributions without densities, provided the relevant integral is defined.

One caution is needed: a random variable need not have a finite expectation. The positive and negative parts of an integral must be handled appropriately. Some heavy-tailed distributions assign enough probability to extreme values that the positive expectation diverges. For variables with both positive and negative tails, an expression resembling infinity minus infinity is not a valid finite expected value. The existence of a distribution does not guarantee that every average we wish to compute exists.

## What an average can and cannot tell us

Consider two games. In the first, you receive ten units with certainty. In the second, you receive one hundred units with probability one-tenth and zero otherwise. Both have expected value ten. Yet the second is far more variable. Someone who must pay a bill tomorrow may reasonably prefer the certain ten, even though the expected values match.

Expectation summarizes one aspect of a distribution. It does not describe the whole pattern of possible outcomes. To quantify dispersion around the mean, we can calculate variance: the expected squared distance from the mean. Squaring makes large deviations count more and prevents positive and negative deviations from cancelling.

For a fair die, the mean is three and a half. The variance is thirty-five twelfths, about two point nine two. Its square root, the standard deviation, is roughly one point seven one. These numbers describe how spread out the outcomes are around their mean. They do not tell us that the distribution is bell-shaped or that deviations beyond a certain threshold are impossible.

The squared distance also provides an algebraic formula: variance equals expected square minus the square of expected value, when these quantities are finite. For a fair die, the expected square is ninety-one sixths. Subtract three and a half squared and we obtain thirty-five twelfths.

There is a modeling choice in how we use variance. Financial risk, engineering failure risk, and prediction uncertainty may care more about one tail than the other, or about rare catastrophic outcomes rather than typical fluctuations. A small variance does not automatically certify safety. A distributional summary is useful when it answers the decision question we actually have.

## A function of a random variable

Suppose we are charged according to the square of a die roll. The cost is no longer X; it is X squared. We could find the distribution of X squared and average its values, but that is unnecessary. The law of the unconscious statistician, a memorable name for a simple principle, says we can compute the expected cost directly by averaging the function of X over the distribution of X.

For the fair die, square the six possible results: one, four, nine, sixteen, twenty-five, and thirty-six. Their average is ninety-one sixths, or about fifteen point one seven. Notice that this is not the square of the average roll, which would be twelve point two five. A nonlinear function and an average generally do not commute.

The difference is not a numerical accident. Squaring is convex. Large deviations increase the squared value more than small deviations decrease it. Jensen's inequality tells us that for a convex function, the function of the mean is at most the mean of the function, under the conditions required for the expectations to be defined. Here the inequality says the square of three and a half cannot exceed the mean squared die roll.

This connection to convexity is useful in optimization under uncertainty. If cost rises nonlinearly with load, designing around the mean load may underestimate average cost. We need to average the cost across the distribution of possible loads. The correct order of operations is determined by the model, not by convenience.

## Linearity does not need independence

One of the most useful facts in probability is that expectation is linear. For random variables X and Y with finite expectations, the expected value of X plus Y is the expected value of X plus the expected value of Y. Multiplying a variable by a constant multiplies its expectation by that constant. These rules hold whether X and Y are independent, positively correlated, negatively correlated, or even identical.

Suppose a service experiences a failure on some number of days in a month. Let I of day one be one when there is a failure that day and zero otherwise. Define one such indicator for each day. The total number of failure days is the sum of these indicators. Because the expectation of an indicator is the probability of its event, the expected number of failure days is the sum of the daily failure probabilities.

This remains true when failures on successive days are correlated. The correlation may affect the variability of the monthly count, but not the linearity of its expectation. If every one of thirty days has failure probability one-tenth, the expected number of failure days is three, even if failures tend to arrive in clusters.

The variance of a sum behaves differently. In general, the variance of X plus Y includes twice their covariance. If the variables are independent, the covariance is zero and the variances add. But zero covariance alone does not establish full independence. Dependence can exist in nonlinear patterns that covariance misses.

This distinction is essential in statistical algorithms. Expected loss over many examples may decompose into a sum even when the examples are dependent, provided the relevant expectations exist. Concentration bounds and variance calculations may require additional assumptions. We should separate what linearity gives for free from what independence adds.

## From averages to probability bounds

Can we use an average to say something about the probability of a large value? Yes, if the variable is nonnegative. Suppose X is a nonnegative random quantity with finite expectation. If X reaches or exceeds a positive threshold a, it contributes at least a to its expectation on that event. Therefore the expected value is at least a times the probability of that event. Rearranging gives Markov's inequality: probability of X at least a is no greater than expected X divided by a.

The proof is almost embarrassingly simple. But it is general. We need no assumption about the shape of the distribution, no independence of component variables, and no normal approximation. Nonnegativity and a finite expectation are enough.

As an example, suppose the expected number of system failures in a week is two. Then the chance of at least ten failures is at most one-fifth. This is a weak bound when we know the complete distribution, but it is still a mathematically valid statement under very limited information. A stronger answer needs more assumptions or more data.

There is a related reasoning pattern behind Chebyshev's inequality. Apply Markov's inequality to the nonnegative squared deviation from the mean. The resulting bound says the probability of being at least a fixed distance from the mean is at most variance divided by the square of that distance. This turns a second-moment calculation into a probability guarantee without assuming a bell-shaped distribution.

These inequalities explain why expectations are useful beyond their interpretation as averages. They can furnish rigorous risk bounds for systems whose full distributions are difficult to calculate. Of course, the bounds may be conservative. We should not confuse a guaranteed upper bound with the actual tail probability.

## Continuous variables and the meaning of density

Return to a variable uniformly distributed between zero and one. Its density is one inside the interval and zero outside. The probability that the variable falls between one-quarter and one-half is the area under the density over that interval, or one-quarter.

A density is not itself a probability of an exact value. A density can even be greater than one, provided the total area under it is one. If a variable is uniform on the interval from zero to one-tenth, its density is ten on that short interval. The probability of an interval is its length times ten, so the entire interval still receives probability one.

This removes a common confusion between the height of a density curve and probability. Probability is assigned to sets, represented by area or integration when a density exists. An individual point's probability remains zero in a continuous distribution even when the density at that point is large.

If we transform a continuous variable, its density may change in a way that includes the stretching or compressing of intervals. For a smooth one-to-one transformation, the change-of-variables formula uses the absolute derivative of the inverse transformation. The adjustment is necessary because an interval of output values may correspond to a longer or shorter interval of input values. Simply evaluating the old density at a new coordinate would generally give the wrong probabilities.

For example, let X be uniform between zero and one, and set Y equal to X squared. The event Y at most y, for y between zero and one, is the same as X at most the square root of y. So the cumulative probability is the square root of y. Where the density exists, differentiating gives one over twice the square root of y. The density becomes large near zero yet integrates to one. This transformation is a useful example of why a function changes both values and the way probability is distributed among them.

## Mathematical history and the language of distributions

The modern idea of a probability distribution did not appear at once. Early calculations involved games, counting, and particular numerical chances. Later analysts developed tools for summing and integrating possible outcomes. Questions about measurement errors, scientific observations, insurance, and repeated trials created practical reasons to understand averages and variability.

The work of mathematicians such as Jacob Bernoulli, Pierre-Simon Laplace, and Pafnuty Chebyshev helped shape probabilistic reasoning across different centuries and institutions. Chebyshev's inequality is associated with a nineteenth-century effort to obtain robust statements without specifying every detail of a distribution. In the twentieth century, Andrey Kolmogorov's axiomatic formulation placed probability within measure theory, giving a consistent language for both discrete and continuous random variables.

It is easy to tell this history as though every generation was merely preparing for the next textbook. The questions were not identical. Gambling problems, astronomical errors, insurance calculations, and abstract measure theory put different demands on the mathematical framework. Their eventual combination explains why expectation can now be taught as an integral and used for everything from a fair die to a stochastic numerical algorithm.

The historical lesson supports the mathematical one. A probability model becomes more useful when we separate the underlying outcomes, the measurements we take from them, and the properties of those measurements we wish to control. Each layer can be examined, tested, and generalized without changing the meaning of the others.

## A practical test of understanding

Suppose a colleague reports that an AI service has an average latency of two seconds. What can you conclude? If the average is a genuine finite expectation of a nonnegative latency variable, Markov's inequality says the chance of latency at least twenty seconds is no greater than one-tenth. That is something. But it does not tell you the true fraction of slow requests, and it does not describe whether a few extreme responses dominate the mean.

Now suppose the colleague adds that the variance is small. With an appropriate variance estimate and relevant assumptions, Chebyshev's inequality gives a stronger statement about deviations from the mean. If the distribution has a heavy right tail, quantiles might communicate the user experience more directly. If requests are dependent across time, a prediction for a future interval may require an explicit model of that dependence.

Notice what changes as we ask better questions. First we need to know the random variable: is latency measured from request arrival to the first byte, or to the final answer? Then we need its distribution or a defensible summary. Finally we need a risk criterion: average cost, probability of exceeding a deadline, or worst-case behavior. Probability calculations cannot choose the engineering objective for us.

## The structure to remember

A random experiment has outcomes. A random variable is a function of those outcomes. Its distribution records how much probability the function assigns to sets of values. Expectation integrates the variable against that distribution. Variance measures squared deviation from its mean. Linearity lets us calculate expectations of sums without independence. Inequalities such as Markov's turn moment information into bounds on events.

The most useful shift in perspective is to stop treating a random variable as a mysterious number that has not been selected yet. Treat it as a well-defined measurement function applied to a probabilistic world. Then ask which mathematical operation answers your question: push probability forward to obtain a distribution, integrate a function to obtain an expectation, or bound an event using known moments. Those are distinct operations with distinct assumptions. Their separation is what makes the subject precise and extensible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Distributions as pushforwards

For probability space `(Omega,F,P)` and measurable `X : Omega -> R`, its law is `mu_X(B)=P(X^{-1}(B))` for Borel sets `B`. Its cumulative distribution is `F_X(x)=P(X<=x)`.

### Die statistics

For a fair die `X`, `E[X]=(1+2+3+4+5+6)/6=7/2`, `E[X^2]=(1+4+9+16+25+36)/6=91/6`, and `Var(X)=91/6-(7/2)^2=35/12`.

For `X~Uniform(0,1)` and `Y=X^2`, `F_Y(y)=sqrt(y)` for `0<=y<=1` and density `f_Y(y)=1/(2 sqrt(y))` on `(0,1)`.

### Bounds

If `X>=0` almost surely and `E[X]<infinity`, for `a>0`: `P(X>=a)<=E[X]/a` (Markov). If `Var(X)<infinity`, `P(|X-E[X]|>=a)<=Var(X)/a^2` (Chebyshev).

### Exercises and answers

1. **Expected square:** Is `E[X^2]` equal to `(E[X])^2` for a fair die? **Answer:** No; `91/6` versus `49/4`.
2. **Indicators:** Thirty daily indicator variables each have expectation 0.1. What is the expected total count? **Answer:** 3 without any independence assumption.
3. **CDF:** For `X~Uniform(0,1)`, find `P(X<=0.3)`. **Answer:** 0.3.
4. **Markov:** For a nonnegative latency variable with mean two seconds, bound `P(X>=20)`. **Answer:** At most 0.1.

### References

- Joseph Blitzstein and Jessica Hwang, *Introduction to Probability*, Harvard Stat 110: https://stat110.hsites.harvard.edu/
- MIT OpenCourseWare, Probability and Random Variables 18.600: https://ocw.mit.edu/courses/18-600-probability-and-random-variables-fall-2019/
- Achim Klenke, *Probability Theory: A Comprehensive Course* (3rd ed. 2020).
- V. Vovk and G. Shafer, "Kolmogorov's Contributions to the Foundations of Probability" (2003): https://glennshafer.com/assets/downloads/articles/article68.pdf
