# 001000 — Measuring Uncertainty: Events, Evidence, and Expectation

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** fractions, sets, and arithmetic; elementary algebra helpful. **Theme:** event spaces, conditional probability, independence, expectation, and why measure theory becomes necessary.

<!-- BEGIN SPOKEN LECTURE -->

# Measuring Uncertainty: Events, Evidence, and Expectation

A laboratory has a test for a rare condition. The test is good at detecting the condition when it is present and usually gives a negative result when the condition is absent. One morning, someone receives a positive result. How likely is it that the condition is actually present?

We cannot answer from the test's accuracy alone. We also need to know how common the condition is in the population being tested. This surprises people because the positive result feels like direct evidence about a particular individual. It is evidence, but its meaning depends on the possibilities that existed before the measurement. Probability gives us a disciplined way to combine these pieces.

Today we will construct probability from events, see why conditioning changes the question being asked, and learn how expectation turns uncertain outcomes into a quantity we can calculate. We will also meet an apparent paradox: an event can have probability zero without being impossible. By the end, that paradox will explain why probability theory eventually needed ideas from measure theory.

## Begin with a finite world

Suppose you roll a fair six-sided die. The possible outcomes are one, two, three, four, five, and six. If the die is fair, each has probability one sixth. The event 'the result is even' contains the outcomes two, four, and six, so its probability is three sixths, or one half. The event 'the result is greater than four' contains five and six, with probability one third.

An event is a set of possible outcomes. That formulation may sound unnecessarily formal when we have a single die. It becomes valuable as soon as events overlap. The two events just described intersect at the outcome six, because six is both even and greater than four. The event that at least one happens contains two, four, five, and six, with probability four sixths, or two thirds.

If we simply added the probability of even, one half, to the probability of greater than four, one third, we would get five sixths. That double-counts the outcome six. The correct rule is: probability of A or B equals probability of A plus probability of B minus probability of both. The subtraction accounts for overlap.

This is the first advantage of talking about sets. Our intuition about 'or' can be ambiguous, especially in everyday language. In probability, A or B ordinarily means at least one of them occurs. If the events are mutually exclusive, they never occur together, and the overlap term is zero. Only then does simple addition apply without correction.

The possible outcomes form a sample space, often called omega. Events are selected subsets of that space. A probability measure assigns a number between zero and one to each allowable event, gives the full sample space probability one, and adds the probabilities of disjoint events appropriately. In a finite sample space, this means we can assign nonnegative weights to outcomes summing to one and obtain event probabilities by adding the weights of contained outcomes.

Notice that fairness was an assumption, not a law of probability. If a die is biased, the event definitions remain the same but the weights change. Probability separates the logical structure of possible events from the empirical question of which probability model describes a physical object.

## What changes when you learn something?

Suppose the die is rolled and a friend tells you the result is even. You now restrict attention to two, four, and six. Under the fair-die model, each of these outcomes is equally likely given the new information. The probability that the result is greater than four becomes one third, because only six among the three remaining outcomes meets the condition.

Before hearing 'even,' the probability of greater than four was also one third. That equality happens in this example, but it is not a universal rule. If instead the friend told you the result was at least four, the possible outcomes would be four, five, and six, and the probability of greater than four would be two thirds. The new information can change the probabilities of events even though it does not change which outcome physically occurred.

Conditional probability formalizes this restriction. The probability of A given B is the probability of both A and B divided by the probability of B, as long as B has positive probability. The numerator counts how much of B also lies in A. The denominator renormalizes the restricted world so that B becomes the new whole.

For the even-die example, A is 'greater than four' and B is 'even.' Their intersection is the single outcome six, with probability one sixth. B has probability one half. Divide one sixth by one half and obtain one third. The computation is not a mysterious update rule. It is ordinary counting within a smaller set of permitted outcomes.

But what does it mean to condition on something that has probability zero, or on a continuous measurement observed to many decimal places? The simple fraction is no longer enough. That question will return when we discuss measure theory. For now, our finite examples keep every denominator visible.

## A positive test in a population of one thousand

Return to the laboratory. Imagine a population of one thousand people. Exactly ten have the condition, so the prevalence is one percent. Let the test detect ninety percent of people who have it. Among the ten affected people, nine test positive and one tests negative.

The test also correctly returns a negative result for ninety percent of people who do not have the condition. There are nine hundred ninety unaffected people, so eight hundred ninety-one test negative, while ninety-nine test positive despite being unaffected. We have two kinds of positive results: nine true positives and ninety-nine false positives. A total of one hundred eight people test positive.

Now suppose we select at random from the people who received a positive result. What fraction actually have the condition? Nine out of one hundred eight. Divide numerator and denominator by nine: one out of twelve, or about eight point three percent. That is very different from the ninety-percent sensitivity of the test.

The sensitivity answers a conditional question: if the condition is present, how often does the test say positive? The positive predictive value answers the reverse conditional question: if the test says positive, how often is the condition present? Reversing a condition changes the denominator. These two probabilities are not interchangeable.

This is the base-rate problem. When a condition is rare, even a fairly specific test can produce more false positives than true positives. The calculation does not say the test is useless. It tells us how to interpret a result under specified assumptions. In a high-prevalence setting, the same test can have a much higher predictive value. In real medicine, test performance may also depend on disease stage, population, threshold, and other factors; the numbers here are deliberately simplified to expose the reasoning.

What if prevalence were ten percent rather than one percent, with the same sensitivity and specificity? Among a thousand people, one hundred would have the condition, ninety of whom would test positive. Among nine hundred unaffected people, ninety would test positive falsely. So a positive test would correspond to a ninety out of one hundred eighty chance, or one half. The test has not changed, but the interpretation of a positive result has changed dramatically.

## Bayes' rule is careful bookkeeping

Bayes' rule is often presented as a formula to memorize. Its simplest derivation is worth understanding. Probability of A and B can be written as probability of A given B times probability of B. We can also write the same joint probability as probability of B given A times probability of A. Set the expressions equal and solve for the conditional probability of A given B.

We obtain: probability of A given B equals probability of B given A times probability of A, divided by probability of B. The numerator combines the likelihood of the observed evidence under hypothesis A with the prior probability of A. The denominator accounts for how likely the evidence is under all the considered possibilities.

Applied to the test, A is 'the condition is present' and B is 'the result is positive.' The prior probability of A is one percent. The likelihood of B when A holds is ninety percent. The overall probability of a positive result is one hundred eight out of one thousand, or ten point eight percent. Multiplying ninety percent by one percent gives zero point nine percent; dividing by ten point eight percent gives one twelfth.

The arithmetic agrees with our count of people. This is no accident: the table of one thousand was simply Bayes' rule made concrete. For teaching, natural frequencies can be better than a row of abstract percentages because the relevant denominator stays visible.

Bayes' rule does not tell us which prior is appropriate. Nor does it guarantee the likelihood model is correct. It shows the coherent update once those ingredients have been specified. Serious probabilistic reasoning requires both valid mathematics and a defensible model of the situation.

## Independence is a claim, not a feeling

Two events are independent when learning one does not change the probability of the other. Formally, their joint probability equals the product of their individual probabilities. Under positive-probability conditions, this means probability of A given B equals probability of A.

Consider two flips of a fair coin. Let A be 'the first flip is heads' and B be 'the second flip is heads.' If the flips are independent, both have probability one half, and both occur with probability one quarter. Observing the first heads does not change the chance of heads on the second.

Now replace the experiment with a single fair flip observed twice. A means 'the coin was heads at the first observation' and B means 'it was heads at the second observation.' The two events are now identical. Their joint probability is one half, not one quarter. Describing them as two observations does not make them independent. The sampling mechanism determines the dependence.

Even pairwise independence can be misleading. Imagine two independent fair bits, and a third bit that records whether the first two agree. Any pair of the three bits is independent: knowing one does not change the balance of the other. But if you know the first two, you know the third exactly. The three are not jointly independent. This small example shows why technical definitions matter when we study many random variables.

For algorithms, the point is immediate. A randomized procedure may rely on independent samples to justify error bounds. If the samples share a hidden random seed or a common source of bias, the mathematical guarantee may fail. An assertion of independence must come from the construction or the model, not merely from how unpredictable each sample appears in isolation.

## A game show and the rules of observation

Consider three closed doors. A prize is behind one. You pick a door, but do not open it. A host who knows where the prize is then opens a different door that has no prize and offers you the chance to switch to the remaining unopened door. Assume the host always follows these rules and that your original choice does not use information about the prize.

Your first choice wins with probability one third. It loses with probability two thirds. Whenever your first choice loses, the prize is behind one of the two other doors. The host deliberately exposes the losing one, leaving the prize behind the other unopened door. Therefore switching wins on the original two-thirds chance that your first choice was wrong.

People sometimes say that once two doors remain, each must have probability one half. But the door was not opened at random without regard to its contents. The host's action was selected using knowledge. The observed information and the selection mechanism jointly determine the probabilities.

The assumptions about the host are essential. If the host sometimes declines to offer a switch, chooses what to reveal using a different rule, or does not know where the prize is, the probabilities can change. Even in the standard game, if we condition on the identity of a particular door the host opened, further details of the host's tie-breaking rule may become relevant. The simple switching strategy succeeds with probability two thirds under the standard always-offer, always-reveal-a-goat rules.

This is more than a recreational puzzle. Selection mechanisms appear in scientific studies, surveys, recommendation systems, missing data, and experiments. We do not observe everything. We observe what the system permits us to see. Probability must model that selection when it affects the evidence.

## Expectation: an average before the experiment

So far we have assigned probabilities to events. Often we want to associate a numerical quantity with an outcome. A random variable is a function from outcomes to numbers. The name can be confusing: the function is fixed, while the outcome selected by the experiment is uncertain.

Suppose a fair coin game pays three dollars if the coin lands heads and costs you one dollar if it lands tails. The random variable X is three on heads and negative one on tails. Its expected value is one half times three plus one half times negative one, which equals one dollar.

Expected value is a weighted average of possible outcomes. It does not mean we expect to receive exactly one dollar on a single play; neither outcome pays one dollar. If independent copies of the game are repeated many times, the average payoff tends toward one dollar under the relevant law of large numbers. The expectation describes the distribution's center, not a promise about individual results.

What about risk? Both a guaranteed payment of one dollar and this coin game have expected value one dollar. But their uncertainty differs. In the coin game the payoff deviates from its mean by two dollars in either direction. Square those deviations, weight them by their probabilities, and add: the variance is four square dollars. The standard deviation is two dollars. For the guaranteed payment, variance is zero.

The distinction between expectation and variability is fundamental in optimization and statistical decision-making. A strategy with a higher expected payoff can still be unsuitable if it carries unacceptable downside risk. Risk preferences and constraints belong in the model rather than being hidden inside the word 'best.'

## Why expectations add even when outcomes depend

Suppose X is the payoff from one game and Y the payoff from another. The expected total payoff equals expected X plus expected Y. This statement is linearity of expectation. It does not require independence. Even if the two payoffs are perfectly correlated, the mean of their sum remains the sum of their means, provided the expectations are well-defined.

Try an example. A coin lands heads or tails. Let X be one on heads and zero on tails. Let Y be the opposite: zero on heads and one on tails. Then X plus Y is always one. Its expected value is one. Separately, X and Y each have expectation one half, also summing to one. The variables are maximally dependent, but linearity still holds.

Independence becomes important for other rules. Under suitable integrability conditions, independent variables satisfy expected X times Y equals expected X multiplied by expected Y. Variance of a sum is the sum of variances when covariance vanishes, as it does for independent variables with finite variances. Without those conditions, blindly adding variances can badly misstate uncertainty.

This separation is valuable in complex systems. Sometimes we can compute the expected number of events without finding the full distribution and without assuming independence. For example, the expected number of heads in one hundred fair coin flips is fifty: write the count as a sum of indicator variables, each equal to one for heads and zero otherwise. Each indicator has expectation one half. The expected sum is one hundred times one half. Independence would be necessary for some concentration results, but not for this expectation calculation itself.

## Why a probability measure is needed

A finite sample space is easy. Assign weights to outcomes and add. But many experiments have a continuous range of outcomes. The position where a dart lands on a board, the time until a radioactive decay, or an instrument reading may be modeled with real-valued random variables. We cannot assign a positive probability to each exact real number while maintaining the ordinary probability rules on an interval.

Consider selecting a number uniformly from the interval between zero and one. The probability of landing between zero and one half is one half. The probability of landing between one quarter and three quarters is also one half. Any interval's probability equals its length. What is the probability of landing on exactly one half? Zero. Yet a selected real number must have some exact value in the mathematical model.

Here is the apparent paradox. Every individual point has probability zero. The entire interval consists of points. Why does the interval have probability one? Because additivity is only required for countable collections of disjoint events, not arbitrary uncountable collections. There is no rule saying the probability of an uncountable union must equal the sum of the probabilities of its individual singletons. We should not add an uncountable collection of zeros as though we were doing an ordinary finite or countable sum.

This brings us to measure theory. A measure assigns sizes to a suitable collection of sets, with countable additivity. A probability measure is a measure whose total size is one. For continuous probability, events are often chosen from a sigma-algebra, a collection of subsets closed under complements and countable unions. This structure is designed so that the operations we need preserve measurability and probabilities remain consistent.

Why not assign probabilities to every imaginable subset of the real numbers? In standard set-theoretic foundations, sufficiently pathological sets prevent the existence of a translation-invariant, countably additive length measure on all subsets of the real line that extends ordinary interval length. The usual theory therefore works with an appropriate sigma-algebra, such as the Borel sets or their completion under Lebesgue measure. The technical machinery serves an understandable goal: extending finite-event reasoning to continuous spaces without contradictions.

## Kolmogorov's foundation and its reach

In 1933, Andrey Kolmogorov published a systematic axiomatic foundation of probability using measure theory. Earlier researchers had developed many of the relevant tools and ideas; Kolmogorov's achievement was to place probability within a framework that could handle discrete and continuous phenomena under common rules. Its value has extended far beyond the particular questions motivating probability in the early twentieth century.

The abstraction does not tell us what probability fundamentally means in every philosophical setting. A probability might be interpreted as a long-run frequency, a measure of rational belief, or a component of a physical model, depending on the application. The axioms constrain how probabilities behave once a model is specified. They do not by themselves determine which empirical assumptions are correct.

This is a familiar pattern in foundations. An axiomatic system makes reasoning precise, while the interpretation and application of the axioms remain substantive work. The same formal framework can represent coin flips, uncertain parameters, random processes, measurement noise, and repeated algorithms. The mathematics provides reliable deductions conditional on the model; science and engineering must investigate the adequacy of the model.

## Conditional expectation is a further step

Our conditional probability examples asked how likely an event is after learning something. We can ask the same question for numerical outcomes. If you know a student's prior performance, what is your best prediction of a later score? If you observe part of a random process, what can you predict about the next step? Conditional expectation captures the expected value of a random variable given available information.

In a finite setting, the calculation is straightforward. Suppose an outcome can be low, medium, or high, and you learn that it lies in the medium-or-high group. To compute the conditional expected value, renormalize the probabilities within that group and take the weighted average. Nothing more mysterious is happening than conditioning followed by expectation.

In a general probability space, the information available is represented by a sigma-algebra, and conditional expectation becomes a random variable measurable with respect to that information. Its defining property is that it matches the original variable's integrals over every event expressible using the information. This construction is powerful enough to underpin martingales, stochastic processes, Bayesian filtering, and much of modern statistical reasoning.

There is a geometric interpretation too. For square-integrable variables, conditional expectation is the best mean-square prediction using the specified information. The prediction error is orthogonal, in the appropriate inner-product sense, to every square-integrable quantity determined by that information. So probability connects to projection geometry and optimization, not merely to counting possible outcomes.

That connection will matter whenever we construct probabilistic models, compare forecasts, or develop algorithms that estimate hidden quantities from observations. The words 'what can I know from what I have observed?' become a precise mathematical problem.

## What probability can and cannot promise

The positive-test example taught us to keep denominators straight. Independence taught us to distinguish a sampling assumption from the mere existence of multiple observations. Expectation taught us to separate averages from individual outcomes, and linearity from independence. Measure theory showed us how those ideas survive when the outcome space becomes continuous.

A mathematically correct probability statement can still mislead if the population, sampling process, or decision context differs from the model. A perfectly calculated posterior based on the wrong prevalence is not the probability we actually needed. A forecast based on dependent data may be overconfident if independence was assumed. And an expected value can hide severe risk if we ignore the distribution around it.

The discipline is to specify the outcome space, the events, the probability model, the information observed, and the quantity we are trying to predict or decide. Then ask what follows from those commitments. Probability does not eliminate uncertainty. It makes uncertainty an object of mathematical reasoning, with rules strong enough to catch contradictions and flexible enough to describe the cases where certainty is unavailable.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Events and conditioning

A probability space is a triple \((\Omega,\mathcal F,\mathbb P)\), where \(\mathcal F\) is a sigma-algebra and \(\mathbb P(\Omega)=1\) with countable additivity on pairwise disjoint measurable events. For \(\mathbb P(B)>0\),

\[
\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)},\qquad
\mathbb P(A\cap B)=\mathbb P(B\mid A)\mathbb P(A).
\]

Hence Bayes' theorem:

\[
\mathbb P(A\mid B)=\frac{\mathbb P(B\mid A)\mathbb P(A)}{\mathbb P(B)}.
\]

### Screening example

For prevalence \(0.01\), sensitivity \(0.9\), specificity \(0.9\):

\[
\mathbb P(\mathrm{condition}\mid +)=\frac{0.9\cdot0.01}{0.9\cdot0.01+0.1\cdot0.99}=
\frac{0.009}{0.108}=\frac1{12}.
\]

Out of 1,000: 9 true positives, 99 false positives, 891 true negatives, 1 false negative.

### Expectation and variance

For a discrete random variable \(X\),

\[
\mathbb E[X]=\sum_x x\,\mathbb P(X=x),\quad
\operatorname{Var}(X)=\mathbb E[(X-\mathbb E X)^2].
\]

For fair-coin payoffs \(X\in\{3,-1\}\) with equal probability, \(\mathbb E X=1\), \(\operatorname{Var}(X)=4\). Linearity \(\mathbb E[X+Y]=\mathbb E X+\mathbb E Y\) requires integrability but not independence.

### Countability caution

For a uniform random variable on \([0,1]\), \(\mathbb P(X=x)=0\) for every fixed \(x\), while \(\mathbb P(X\in[0,1])=1\). Countable additivity does **not** assert arbitrary uncountable additivity.

### Exercises and answers

1. **Exercise:** For a fair die, find \(\mathbb P(\text{even}\mid >3)\). **Answer:** The possible outcomes are 4,5,6; even ones 4 and 6, so \(2/3\).
2. **Exercise:** If prevalence rises from 1% to 10% with 90% sensitivity and 90% specificity, what is the positive predictive value? **Answer:** \(1/2\).
3. **Exercise:** If \(Y=1-X\) for a fair Bernoulli \(X\), are X and Y independent? **Answer:** No; \(\mathbb P(X=1,Y=1)=0\neq1/4\).
4. **Exercise:** Does \(\mathbb E[X+Y]=\mathbb EX+\mathbb EY\) require independence? **Answer:** No, only well-defined integrable expectations in this elementary setting.

### References

- MIT OpenCourseWare, *Probability and Random Variables* (18.600), course notes, https://ocw.mit.edu/courses/18-600-probability-and-random-variables-fall-2019/pages/lecture-notes/
- Vladimir Vovk and Glenn Shafer, “Kolmogorov's Contributions to the Foundations of Probability” (2003), https://glennshafer.com/assets/downloads/articles/article68.pdf
- Joseph K. Blitzstein and Jessica Hwang, *Introduction to Probability*, 2nd ed. (2019), https://projects.iq.harvard.edu/stat110/home
- Achim Klenke, *Probability Theory: A Comprehensive Course*, 3rd ed., Springer (2020).
