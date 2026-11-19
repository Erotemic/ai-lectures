# 008000 - Bayesian Inference, Identification, and Calibration

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** Bayes' rule, likelihood, basic distributions, and expectation. **Theme:** inference under models, information that data cannot identify, and testing probability forecasts.

<!-- BEGIN SPOKEN LECTURE -->

# Bayesian Inference, Identification, and Calibration

A product team runs a new system on ten independent test cases. Seven pass and three fail. They ask: what is its true reliability? One colleague says seventy percent. Another says about sixty-seven percent. A third refuses to give a single number and asks whether the cases were representative, whether the failures were correlated, and how the next system will differ from the one tested.

All three reactions contain part of the problem. Seven tenths is an observed fraction, not a known population parameter. A number like sixty-seven percent can be the posterior average under a specific statistical model and prior. Questions about representativeness and model structure can invalidate either estimate as a predictor of future performance. Statistical inference is the process of connecting observations to uncertain quantities through explicit assumptions; a calculation inside the model cannot validate those assumptions by itself.

We will build a small Bayesian model that can be understood without numerical software, prove its update rule, and then examine two harder questions. First, can different underlying mechanisms produce exactly the same observations, so that no quantity of the available data identifies the mechanism? Second, how can we evaluate probability predictions when a single outcome is either success or failure? That leads to calibration and scoring rules.

## Separate outcomes from a parameter

Suppose each test case succeeds with the same unknown probability p. Conditional on p, the cases are independent and success or failure is described by a Bernoulli distribution. If we observe seven successes in ten cases, the likelihood of p is proportional to p raised to the seventh power times one minus p raised to the third power.

Why do we say proportional? If the observed data are only the total number of successes, there is a binomial coefficient counting which seven cases succeeded. That coefficient does not depend on p and therefore does not change the relative plausibility of candidate values of p. If we observe the complete sequence, the likelihood has the same p-dependent part without the binomial coefficient. In either representation, the update over p is the same.

A likelihood is a function of the parameter for fixed observed data. It is not, by itself, a probability distribution over parameters. We can compare how well p equals one half or three quarters explains the observed seven successes, but likelihood alone does not specify how to average across candidate values of p. A Bayesian analysis adds a prior distribution that describes uncertainty about p before seeing these cases.

That prior is part of the model. It might represent experience with similar systems, engineering constraints, or a deliberately weak starting distribution. It should not be smuggled into the calculation while claiming the result came purely from the data. Different legitimate priors can produce different posterior conclusions, especially with only ten observations.

The Bayesian rule is simple in form: posterior density is proportional to likelihood times prior density. The constant of proportionality is chosen so the posterior integrates to one. Computing this constant is easy in some families and demanding in others. The Beta distribution gives a useful exact example.

## A Beta prior and the meaning of its parameters

A Beta distribution is supported on probabilities between zero and one. Its density is proportional to p raised to a parameter a minus one times one minus p raised to a parameter b minus one. When a and b both equal one, the density is constant on the interval. This is a uniform prior on p.

The Beta family is convenient because multiplying by the Bernoulli likelihood preserves its form. Suppose the prior is Beta with parameters a and b. After s successes and f failures, multiply the prior factor by p raised to s and one minus p raised to f. The exponents become a plus s minus one and b plus f minus one. Once normalized, the posterior is Beta with parameters a plus s and b plus f.

This algebra is the entire reason the family is called conjugate for the Bernoulli model. No numerical approximation is needed. The same form can be updated repeatedly as new cases arrive, as long as the assumed data model and prior remain appropriate.

For a uniform Beta-one-one prior, seven successes and three failures produce a Beta-eight-four posterior. The posterior mean is eight divided by twelve, or two thirds. Compare this with the observed fraction seven tenths. The posterior mean is slightly closer to one half because the prior spreads some weight across the whole interval rather than concentrating all mass at the observed fraction.

It is sometimes useful to describe a and b as prior pseudo-counts, but this analogy has limits. A Beta-one-one prior is mathematically equivalent in the update formula to adding one to both observed counts. It does not mean we secretly observed one real success and one real failure. The prior is a probability distribution over a model parameter, not a historical data record unless it was explicitly constructed from such a record.

If the prior were instead Beta-ten-ten, the same ten test results would yield Beta-seventeen-thirteen, with mean seventeen thirtieths, about fifty-seven percent. If the prior were Beta-one-half-one-half, the posterior mean would be seven and a half divided by eleven, about sixty-eight percent. The data are identical, yet the answers differ. That is not a mathematical inconsistency; the analyses encode different prior uncertainty.

For larger, well-behaved independent samples, the data often dominate reasonable fixed priors. But a finite sample does not erase the importance of the prior, and models with poor identifiability can retain substantial prior dependence even when there are many observations.

## Prediction is not just estimation

We might care less about the parameter p than about whether the next test case will pass. Under the model, the probability of next-case success given p is p. But p is uncertain after observing the data. To predict the next case, average p over its posterior distribution.

For the Beta-eight-four posterior, that average is two thirds. Thus the posterior predictive probability of success for one new case is also two thirds. In this simple model, the parameter posterior mean and one-step predictive probability happen to coincide. That need not hold for nonlinear predictions or more elaborate models; generally we integrate the relevant outcome probability over the posterior, not merely plug a posterior mean into an arbitrary nonlinear expression.

This reveals two different sources of uncertainty. Even if p were known exactly, a new test case would still be random under a Bernoulli model. That is outcome variability. With ten observed cases, we also do not know p exactly. That is parameter uncertainty. Posterior predictive calculations account for both through averaging over possible parameter values.

If we predict the number of successes in a hundred new cases, simply substituting the posterior mean into a binomial distribution treats the estimated p as certain. The correct posterior predictive distribution under the shared unknown p model is beta-binomial. Its uncertainty is greater because possible future cases are dependent after integrating out their common uncertain p, even though they were conditionally independent given p.

This is a subtle lesson about dependence: observations can be independent conditional on a shared hidden parameter and dependent marginally when that parameter is not known. The model's structure matters as much as the formula for its mean.

## Credible intervals and confidence intervals answer different questions

A Bayesian credible interval assigns posterior probability to a range of p values, conditional on the observed data, prior, and likelihood model. For example, a 95 percent credible interval under the Beta-eight-four posterior contains 95 percent of the posterior mass. Its endpoints can be calculated from Beta quantiles.

A frequentist confidence procedure is calibrated over hypothetical repetitions of the entire sampling process, with a fixed unknown parameter. A 95 percent confidence procedure has coverage at least or approximately 95 percent under specified conditions: across repeated experiments, the resulting intervals contain the true fixed parameter with the advertised frequency.

These are different probabilistic statements, even when their numerical intervals are similar. A confidence interval computed for a particular dataset does not automatically assign a probability of 95 percent to the fixed parameter lying inside it. A credible interval's posterior probability is valid relative to its prior and likelihood; it does not automatically guarantee 95 percent long-run coverage across every parameter value.

Both approaches can be useful. The important discipline is to preserve the quantity being randomized in each argument. Is probability assigned to possible parameters after data? Or to possible data and intervals before repetition? Ambiguous language can make a technically correct formula sound as though it proves a different claim.

## An inference can be precise but not identifiable

Now consider a system with two stages. The first stage succeeds with probability a. If it succeeds, the second succeeds with probability b, and the overall case passes only if both stages succeed. Suppose the test reports only overall pass or fail. Then the observed pass probability is the product a times b.

Even with millions of independent overall tests, we may estimate that product very accurately. But those data alone cannot determine a and b separately. A value a of one half and b of four fifths produces the same overall success probability as a of four fifths and b of one half. Both give two fifths. Many other pairs produce the same product.

The two mechanisms have different engineering implications. If the first stage is unreliable, effort should focus there; if the second is unreliable, a different intervention is appropriate. But no analysis of only overall pass/fail data can reliably choose between the mechanisms without additional assumptions or measurements.

This is an identification problem. The observational model maps different underlying parameter values to the same observable distribution. More samples of the same measurements reduce sampling uncertainty about the identifiable product, but not uncertainty about how the product decomposes. A posterior for the individual factors may appear sharply concentrated if the prior strongly favors a particular decomposition, yet that concentration is supplied by assumptions rather than the pass/fail observations alone.

To resolve the problem we must change the experiment or use genuinely informative prior knowledge. Instrument the intermediate stage, inspect failure logs, or vary conditions in ways that give independent constraints. The mathematical criterion is that distinct parameter values should yield distinguishable probability laws for the observations relevant to the question.

An even more serious problem appears when some variables affect both system configuration and measured outcome. An observational comparison between two configurations may then reflect differences in which cases received them, not a causal effect of the configurations. Neither Bayes' theorem nor a large dataset removes confounding by itself. Causal conclusions require a design or assumptions that address the mechanism generating the data.

## What does calibration mean?

Suppose a forecasting system issues a probability of rain each day. On some days it announces twenty percent, on others seventy percent. A forecast is calibrated, in a standard binary sense, if among cases assigned probability q, the event occurs with conditional frequency q, in the ideal population interpretation. Events forecast at twenty percent should occur about one fifth of the time, and events forecast at seventy percent about seven tenths.

Calibration is a property of many predictions together with their outcomes. A single correct forecast cannot demonstrate calibration, and a single wrong outcome does not refute a probabilistic prediction. If a system assigns ten percent probability to an event and the event occurs, that outcome was possible under the stated forecast. We need repeated evaluation with appropriate grouping and attention to statistical uncertainty.

Calibration also depends on the population and conditions being evaluated. A model calibrated on one hospital, weather region, or manufacturing line may be miscalibrated on another. The base rate, measurement process, and conditional patterns may change. Good performance in a pooled dataset can hide serious subgroup errors, so calibration should be examined at the resolution relevant to decisions.

Calibration alone is not enough for useful forecasts. A forecaster who always announces the unconditional event frequency can be calibrated overall and still fail to discriminate easy from difficult cases. Sharpness or resolution describes how much the forecasts move away from an uninformative baseline in ways that correspond to real differences in risk.

A strong evaluation therefore considers whether stated probabilities match frequencies and whether the model meaningfully separates situations with different outcomes. It also asks how evaluation data were selected and whether there are enough observations in each forecast range to make the empirical comparison stable.

## A score for probabilistic predictions

One way to evaluate binary forecasts is the Brier score. If a model predicts q for an outcome Y that is either zero or one, the score is the square of q minus Y. A lower score is better. Predicting ninety percent when the event occurs receives a score of one hundredth. Predicting ninety percent when it does not occur receives a score of eighty-one hundredths.

Why is this a principled score rather than an arbitrary penalty? Let the true event probability for a particular information state be p. We can calculate the expected Brier score of announcing q. It equals the unavoidable variance p times one minus p, plus the square of q minus p. The first term is independent of the announced probability. The second is minimized uniquely when q equals p.

That short calculation proves the Brier score is strictly proper for binary events: if the true conditional probability is p, a forecaster minimizes expected score by honestly reporting p. This is an incentive property under the assumed outcome distribution, not a guarantee that every individual prediction will look good.

Consider a sequence of forecasts. A system that reports ninety percent on all cases it considers easy should see roughly ninety percent successes among those cases if it is calibrated there. Its average Brier score additionally depends on whether it separates those cases from a lower-probability group. Two systems can have similar pooled calibration and different resolution, leading to different predictive usefulness.

Scoring does not settle whether a system is fair, cost-effective, or appropriate for a particular application. In a high-stakes decision, false positives and false negatives may have different consequences. A properly calibrated probability forecast is an input to a decision rule. Choosing an action still requires a loss function, constraints, and sometimes a causal model of how actions change outcomes.

## A forecast can be calibrated yet miss critical structure

Imagine two groups of test cases, easy and hard, each occurring with probability one half. Suppose easy cases succeed nine times in ten and hard cases succeed only one time in ten. A model that always predicts fifty percent is perfectly calibrated overall because the pooled success rate is fifty percent. Yet a model that distinguishes the groups and predicts ninety percent for easy cases and ten percent for hard ones is also calibrated, and is far more useful for deciding where to allocate engineering effort.

Now suppose the pooled model is evaluated only on the same half-and-half mixture. It may appear calibrated indefinitely. If the deployment population changes to mostly hard cases, its fixed fifty-percent forecast becomes too optimistic. The issue is not that the mathematical definition of calibration was wrong. It is that calibration was assessed relative to a particular distribution of information states, and that distribution changed.

This example makes two directions of scrutiny concrete. Ask whether the forecasts condition on features relevant to the decision, and ask whether the evaluation population resembles the population on which the forecasts will be used. Good calibration is necessary for many probability-based decisions, but it cannot recover a hidden feature or repair a sampling design that excluded critical cases.

## Checking the model against the observations

The Beta-Bernoulli calculation is exact, but exact algebra does not make its data model realistic. Are all ten cases exchangeable in a useful sense? Are they drawn from the future deployment population? Was the system modified between tests? Does one failure cause others through shared infrastructure? Does a hidden subgroup have a much higher risk than another?

A model check asks whether observable features of the data resemble what the fitted model predicts. If all failures occur in a single cluster of related cases, the independent Bernoulli assumption may be untenable. If success rates drift over time, a fixed p may be a poor approximation. If the future deployment contains entirely different cases, the posterior predictive distribution can be miscalibrated even though the arithmetic under the training model was performed correctly.

Bayesian posterior predictive checking simulates replicated data from the fitted model and compares relevant summaries with what was observed. The procedure can reveal disagreement, but it does not establish the model as true when no disagreement is found. We may have checked the wrong summaries, lacked statistical power, or omitted plausible competitors. Model criticism is an ongoing empirical task.

There is a parallel issue in optimization and machine learning. A system may produce confident probabilities because its fitted model has low internal uncertainty, while the deployment environment differs from the training environment. Probability conditioned on a misspecified model is not the same thing as a robust guarantee about the physical world.

## Recover the meaning of seven out of ten

Return to the product team's ten test results. The observed fraction is seventy percent. Under an independent Bernoulli model and a uniform Beta prior, the posterior is Beta-eight-four, its mean is two thirds, and the predictive chance of success on one exchangeable new case is two thirds. These statements follow rigorously from the model.

But if the ten cases all exercise the same subsystem, they may reveal little about performance elsewhere. If success depends on two hidden stages, a precise overall success estimate need not identify either stage's reliability. If a system announces future success probabilities, their usefulness must be checked through repeated calibration, resolution, and a scoring rule appropriate to the task.

Bayesian inference supplies a coherent update of uncertainty given data and assumptions. Identification asks whether the observations can distinguish the quantities we wish to know. Calibration asks whether probabilities issued in practice correspond to event frequencies in the target setting. None of these three replaces the others.

The central lesson is that a probability distribution can be mathematically consistent and still be poorly supported as a description of reality. Good inference makes its assumptions inspectable, reports what the data actually identify, and invites predictions that can be tested against new observations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For \(Y_i\mid p\stackrel{\mathrm{iid}}\sim\operatorname{Bernoulli}(p)\), a \(\operatorname{Beta}(a,b)\) prior has density
\[
\pi(p)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}p^{a-1}(1-p)^{b-1},\qquad 0<p<1.
\]
After \(s\) successes and \(f\) failures,
\[
p\mid y\sim\operatorname{Beta}(a+s,b+f),\qquad
E[p\mid y]=\frac{a+s}{a+b+s+f}.
\]
With \((a,b)=(1,1)\) and \((s,f)=(7,3)\), posterior \(\operatorname{Beta}(8,4)\), mean \(8/12=2/3\). For one exchangeable new outcome,
\[
P(Y_{n+1}=1\mid y)=E[p\mid y]=2/3.
\]
For \(m\) new conditionally iid outcomes, the predictive success count has a beta-binomial distribution, not generally \(\operatorname{Binomial}(m,E[p\mid y])\).

**Identifiability counterexample.** If \(P(Y=1\mid a,b)=ab\), the mapping \((a,b)\mapsto P_{a,b}\) is not injective: \((1/2,4/5)\) and \((4/5,1/2)\) give the same law for observed overall outcomes.

**Binary calibration.** For a forecast \(Q\in[0,1]\) and outcome \(Y\in\{0,1\}\), ideal calibration means
\[
E[Y\mid Q]=Q\quad\text{a.s.}
\]
This condition alone need not ensure sharp forecasts or subgroup calibration given extra features.

**Brier propriety.** With \(Y\sim\operatorname{Bernoulli}(p)\),
\[
E[(q-Y)^2]=p(1-p)+(q-p)^2.
\]
The unique minimizer over \(q\in[0,1]\) is \(q=p\).

### Exercises with answers

1. **Conjugacy.** With a Beta(2,3) prior and 4 successes and 1 failure, what is the posterior? **Answer:** Beta(6,4).
2. **Prediction.** For that posterior, what is the predictive success probability on one new exchangeable trial? **Answer:** six tenths.
3. **Mechanisms.** Can observing only pass/fail data with success probability \(ab\) distinguish \((a,b)=(.2,.8)\) from \((.4,.4)\)? **Answer:** no; each has product .16.
4. **Calibration.** Is a single forecast assigning a 10% chance to an event refuted when the event happens? **Answer:** no; evaluation requires repeated outcomes and appropriate conditioning.
5. **Scoring.** Why should a forecaster using squared-error score report its true conditional probability? **Answer:** its expected score equals an irreducible term plus \((q-p)^2\).

### References

- Andrew Gelman, John Carlin, Hal Stern, David Dunson, Aki Vehtari and Donald Rubin, *Bayesian Data Analysis*, third edition.
- Glenn W. Brier, *Verification of Forecasts Expressed in Terms of Probability* (1950).
- Tilmann Gneiting and Adrian E. Raftery, *Strictly Proper Scoring Rules, Prediction, and Estimation* (2007).
- MIT OpenCourseWare 18.600, *Probability and Random Variables*, lectures on Bayes' rule and conditional distributions.
