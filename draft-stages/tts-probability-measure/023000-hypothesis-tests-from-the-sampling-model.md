# 023000 - Hypothesis Tests: Evidence, Error Rates, and Power

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** Bernoulli probabilities, sampling distributions and confidence intervals. **Theme:** null hypotheses, exact p-values, type-I error, power, randomization and interpretation.

<!-- BEGIN SPOKEN LECTURE -->

# Hypothesis Tests: Evidence, Error Rates, and Power

A device is supposed to succeed on half its attempts. You test it ten times, and it succeeds eight times. Has the device improved? Eight out of ten sounds impressive compared with half. On the other hand, ten attempts is a small number, and a perfectly ordinary fifty-percent device sometimes produces a run of good luck. How should we decide what the data say?

We can answer a precise question before deciding whether the device is worth using. Assume, for the sake of calculation, that each attempt is independent and has success probability one half. Under that hypothesis, how often would ten attempts produce eight or more successes? If the event is sufficiently rare under the proposed model, we may decide that the data are difficult to reconcile with it.

That is the core of a hypothesis test. We specify a model under which to calculate probabilities, choose a statistic that captures the discrepancy we care about, and compare the observed statistic with its distribution under that model. This procedure is not a direct probability calculation about the hypothesis itself. It is a statement about how the observations behave *if* the hypothesis and its assumptions hold.

## Start with the sampling model, not a threshold

Let S count successes in ten independent trials, and suppose the null hypothesis says the success probability is one half. Under this model, S has a binomial distribution. The probability of exactly k successes is the number of ways to arrange k successes among ten trials, multiplied by one half raised to the tenth power. Every particular ten-trial success-failure sequence has the same probability, one over one thousand twenty-four.

Our observed value is eight. If the proposed improvement would make successes *more* common, then results at least as favorable to improvement are eight, nine and ten successes. There are forty-five sequences with exactly eight successes, ten with nine, and one with ten. Adding gives fifty-six sequences out of one thousand twenty-four, or about five point four seven percent.

That fraction is the one-sided p-value for this pre-specified test. It answers: if the device really had a fifty-percent success rate, and if our independence and identical-trial assumptions were right, what fraction of ten-trial datasets would have a success count at least as large as the eight we saw? Approximately five point four seven percent.

It does not say there is a five point four seven percent chance that the device is unchanged. That would be a probability about a hypothesis, which requires different statistical machinery. Nor does it say that there is a five point four seven percent chance that the observed data were caused by randomness. The sampling model always involves random outcomes; the test asks how surprising a particular statistic would be under a specified model.

## What if we had not predicted the direction?

Suppose we had a different question: is the success probability *different* from one half, either higher or lower? Then a dataset with only two successes is just as incompatible with a fair device as one with eight. Under the symmetric null model, the probability of two or fewer successes is also fifty-six over one thousand twenty-four. The total probability of counts at least as far from five in either direction is one hundred twelve over one thousand twenty-four, about ten point nine four percent.

That is the exact two-sided p-value for this symmetric binomial test. Notice that it is twice the one-sided value here because the two tails are equal and do not overlap. For asymmetric discrete distributions, there are several possible conventions for defining a two-sided tail, and simply doubling a one-sided value need not give the same result as summing outcomes whose probabilities are no larger than that of the observed outcome.

Choosing one-sided or two-sided after seeing the data changes the experiment we are claiming to analyze. If we expected improvement but would also publicize strong evidence of deterioration, we should think carefully about the appropriate two-sided question before looking. A test is meaningful only in relation to a specified sampling and decision procedure.

## A rejection rule has an error rate

Perhaps we want a rule that rejects the fifty-percent model no more than five percent of the time when it is actually true. This is a type-I error guarantee: the probability of rejecting the null under the null should be at most the chosen level, often called alpha.

For our ten-trial one-sided binomial test, rejecting when we see eight or more successes gives a null rejection probability of about five point four seven percent. That slightly exceeds five percent. Rejecting only when we see nine or ten successes gives eleven out of one thousand twenty-four, about one point zero seven percent. With this small discrete experiment, there is no nonrandomized success-count threshold whose false-positive probability is exactly five percent. We choose the largest threshold region that stays below the bound. If we permit an additional randomized decision when the count is eight, we can calibrate the rejection rate to exactly five percent, but that is usually not an appealing practice for a routine device test.

This distinction between a desired maximum error rate and the actual achievable rate is important. Declaring a nominal five-percent test does not force a discrete procedure to have exactly five-percent size. The size of a test is the maximum null rejection probability over the hypotheses allowed by the null, and here the null consists of one specified probability, one half.

The procedure controls how often it can incorrectly reject a true null, under its assumptions. It cannot guarantee that a rejected null was false in this particular dataset. Nor does it prevent other errors, such as biased sampling, unrecorded trials, or choosing the rule after looking at the result.

## Power: what happens when the device really improves?

Now suppose the success probability is actually eighty percent, and we use the conservative rule that rejects the fifty-percent null at nine or ten successes. How often does that rule detect improvement?

Under an eighty-percent model, the probability of exactly nine successes is ten times point eight to the ninth power times point two. The probability of ten successes is point eight to the tenth power. Add them. The result is about thirty-seven point six percent. That is the power of this test against the specific alternative of eighty-percent success.

This is a sobering calculation. A device may truly have improved from fifty to eighty percent, but a test with ten trials and a strict five-percent false-positive limit will detect it in fewer than four out of ten repetitions. Failing to reject the null cannot be interpreted as proving that the two devices are equivalent.

There is a tradeoff. If we rejected at eight or more successes, the power against eighty percent would be about sixty-seven point eight percent, but the false-positive rate under the fifty-percent model would rise above five percent. We could instead increase the number of trials, choose a more informative measurement, or change the design. A responsible study plans not only how frequently it may make a false claim but also how likely it is to detect an effect of practical importance.

The alternative probability of eighty percent is not an arbitrary magic number. It should represent an effect that matters to the application. An improvement from fifty percent to fifty-one percent might be scientifically real but practically negligible in one setting, while a one-percent difference in a safety-critical failure rate might be consequential in another. A p-value does not measure the size or importance of an effect. Report the observed effect and a suitable uncertainty interval as well.

## An interval and a test are two views of a sampling procedure

Confidence intervals and hypothesis tests are closely linked. Under suitable constructions, a two-sided test of a candidate parameter value at level five percent rejects precisely those values that lie outside a corresponding ninety-five percent confidence interval. This is called inverting the test: instead of asking whether one hypothesized value is incompatible with the data, ask which candidate values remain compatible.

The resulting interval describes a range of parameter values with a stated repeated-sampling coverage property. The interval is usually more informative than a lone rejection flag because it shows both the scale of an effect and the uncertainty around it. But the exact relationship depends on using compatible test and interval procedures. A Wald interval, an exact binomial test, and a bootstrap percentile interval may not produce identical decisions, especially in small or boundary samples.

There is also a distinction between statistical and practical uncertainty. If a hospital needs to know whether a treatment reduces complication risk by at least a clinically meaningful amount, then excluding zero difference is not enough. We need to compare the interval with that substantive threshold. The test should answer the actual decision question, not merely the easiest null hypothesis to write down.

## Random assignment provides a different route to a test

So far we have assumed a probability model for the data, such as independent Bernoulli trials. Randomized experiments offer another source of randomness: the assignment mechanism itself.

Imagine four experimental units with recorded outcomes two, four, six and eight. Exactly two units were assigned treatment by a fair random choice among all pairs, and the treated units happened to be the ones with outcomes six and eight. The treated mean is seven; the control mean is three; the observed difference is four.

Consider the sharp null hypothesis that treatment had no effect on any of these four units. Under that null, each unit's outcome would be the same regardless of assignment. We can keep the four observed outcomes fixed and enumerate the six equally likely choices of which two units could have received treatment. The largest possible treated-minus-control difference is four, achieved by assigning treatment to six and eight. The smallest is negative four, achieved by assigning treatment to two and four.

Thus a one-sided randomization test for improvement gives one extreme assignment out of six, a p-value of one sixth. If we count both positive and negative effects at least as extreme, there are two assignments out of six, giving a two-sided p-value of one third.

These numbers are not tiny, because with only four units the randomization distribution is coarse. More importantly, the logic does not depend on assuming Gaussian errors or estimating a population variance. It depends on the assignment being genuinely randomized and on the sharp no-effect null. If treatment assignment was observational and confounded with which units were likely to perform well, shuffling labels as if they were randomized would not have this justification.

## Multiple chances to find something

A final trap appears when we run many tests and report only the most exciting result. Suppose twenty independent tests each have a five-percent false-positive rate and all twenty null hypotheses are true. The probability that none produces a false positive is point nine five to the twentieth power, about thirty-five point eight percent. Therefore the probability of at least one false positive is about sixty-four point two percent.

Real tests are often dependent, so that exact calculation may not apply. But the logic is clear. Searching across many endpoints, subgroups, analysis choices, or time points changes the opportunity to obtain an impressive-looking p-value by chance. There are methods for controlling familywise error or false discovery rates, and there is also a simple discipline: report how the analysis was selected and which comparisons were made.

The American Statistical Association has emphasized that responsible scientific conclusions should not rest on passing a single significance threshold. Statistical inference requires attention to design, substantive magnitude, assumptions, and transparency.

## What a test can responsibly conclude

Our ten-trial example has now given us several different, precise answers. Eight successes yields a one-sided p-value of about five point four seven percent against the fifty-percent null. A two-sided question gives about ten point nine four percent. A nonrandomized five-percent one-sided decision rule with ten trials would require at least nine successes, and that rule has only about thirty-seven point six percent power against a true success rate of eighty percent.

Each number answers a different question. None by itself tells us the probability that the device improved, and none tells us whether the device is worth adopting. Statistical reasoning works when the question, the model, the decision rule, and the possible errors are kept connected. The arithmetic then becomes interpretable evidence, rather than a label attached to a surprising dataset.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Exact binomial example

For \(S\sim\operatorname{Bin}(10,p)\), under \(H_0:p=1/2\),
\[
P_{1/2}(S\ge8)=\frac{\binom{10}{8}+\binom{10}{9}+\binom{10}{10}}{2^{10}}
=\frac{56}{1024}=0.0546875.
\]
The symmetric two-sided tail is
\[
P_{1/2}(|S-5|\ge3)=\frac{112}{1024}=0.109375.
\]
Rejection region \(R=\{9,10\}\) has size \(P_{1/2}(S\in R)=11/1024=0.0107421875\le0.05\). Rejection at eight or above has size \(56/1024>0.05\).

### Power at a specified alternative

For \(p=0.8\),
\[
P_{.8}(S\ge9)=10(0.8)^9(0.2)+(0.8)^{10}=0.3758096384,
\]
\[
P_{.8}(S\ge8)=45(0.8)^8(0.2)^2+P_{.8}(S\ge9)=0.6777995264.
\]
The first is power under the level-0.05 rule; the second is power for a different, more liberal rule with size 0.0546875.

### Exact four-unit randomization

Observed fixed outcomes \((2,4,6,8)\) and equal-probability assignment of two treated units among four. Under the *sharp* null of no individual treatment effect, the six treatment-group choices and differences \(\bar Y_T-\bar Y_C\) are
\[
\{2,4\}:-4,\quad \{2,6\}:-2,\quad \{2,8\}:0,\quad
\{4,6\}:0,\quad \{4,8\}:2,\quad \{6,8\}:4.
\]
If treated units are \(\{6,8\}\), the one-sided randomization p-value is \(1/6\); two-sided absolute-difference p-value is \(2/6=1/3\).

### Multiplicity under independence

With twenty independent true-null tests, each false-rejecting with probability \(0.05\),
\[
P(\text{at least one false positive})=1-(1-0.05)^{20}\approx0.64151408.
\]
Dependence changes this number; the calculation illustrates the opportunity created by multiple independent tests.

### Exercises with worked answers

1. **Threshold calculation.** For a fair coin tossed ten times, what is \(P(S\ge9)\)? **Answer:** \((10+1)/1024=11/1024\).
2. **One- versus two-sided.** For eight successes, why is the symmetric two-sided p-value larger? **Answer:** it also counts outcomes two or fewer successes, which are equally extreme in the opposite direction under \(p=1/2\).
3. **Power.** If a null is false but a test does not reject it, has the null been proved? **Answer:** no; the test can have low power against that alternative.
4. **Assignment test.** Why does permuting labels require an argument about assignment or exchangeability? **Answer:** otherwise the rearranged datasets may not represent outcomes possible under the experimental design and null model.
5. **Interpretation.** Is a p-value of .03 the probability that the null hypothesis is true? **Answer:** no; it is a model-based probability of a statistic at least as extreme as observed, conditional on the null and the relevant testing rule.

### Reading and attribution

- Penn State STAT 415, Lesson 9, *Hypothesis Tests (Part I)*, https://online.stat.psu.edu/stat415/Lesson09.
- Penn State STAT 415, Lesson 10, *Hypothesis Tests (Part II)*, https://online.stat.psu.edu/stat415/Lesson10.
- American Statistical Association, *Statement on Statistical Significance and P-Values* (2016), https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf.
