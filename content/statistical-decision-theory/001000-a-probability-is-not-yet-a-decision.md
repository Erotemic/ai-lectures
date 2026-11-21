# 001000 — A Probability Is Not Yet a Decision

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** conditional probability, expectations, basic algebra. **Theme:** forecasting an event and choosing an action are different mathematical tasks.

<!-- BEGIN SPOKEN LECTURE -->

# A Probability Is Not Yet a Decision

A monitoring system assigns an eighteen percent probability to an impending failure. Should an engineer stop the machine? An eighteen percent probability is a description of uncertainty. It is not an instruction. The decision depends on what a stop costs, what a missed failure costs, and whether the action actually prevents the outcome. Two engineers may agree completely about the probability and choose different actions without either making a mathematical mistake.

Statistical decision theory begins by making that separation explicit. There is an uncertain state, an observation that supplies evidence about the state, a set of possible actions, and a loss for choosing an action when the state is what it is. From those ingredients we can derive a decision. The mathematics also reveals which assumptions, rather than which arithmetic, caused that decision.

Let the state be either failure or no failure. Suppose we are choosing whether to raise an alarm. We will initially treat this as a classification decision. A false alarm costs one unit, missing an actual failure costs five units, and a correct classification has loss zero. Our number eighteen percent is a posterior probability: it is the probability of failure after conditioning on the observations available at the moment of choice. We can obtain it through Bayes' rule, a calibrated predictive model, or another justified inference procedure. For this lesson, suppose the eighteen percent figure is already supported.

If we raise an alarm, the only possible classification loss arises when there is no failure. That happens with probability eighty-two percent, so the expected loss is zero point eight two. If we stay quiet, the loss is five units whenever failure occurs. Five times zero point one eight is zero point nine. Under our assumptions, raising the alarm wins, despite failure being the less likely outcome. Choosing the most likely state would have made the wrong decision because the two mistakes have unequal consequences.

We can do the calculation without plugging in any numbers. Let p be the posterior failure probability, let C be the cost of a false alarm, and let M be the cost of a missed failure. The expected loss of raising an alarm is C times one minus p. The expected loss of staying quiet is M times p. Raise the alarm precisely when C times one minus p is less than M times p. Rearranging gives p greater than C divided by C plus M. With our costs, the threshold is one sixth, about sixteen point seven percent. Eighteen percent just clears it.

This is a derivation, not a universal safety threshold. If stopping a machine is expensive, the threshold rises. If a missed failure is catastrophic, it falls. A general Bayesian decision rule minimizes posterior expected loss among the available actions. It does not simply choose the state with highest posterior probability.

## Loss is a model, too

There is something easy to miss in that calculation. We treated the alarm as a declaration about what will happen. Real interventions can change what happens. If stopping the machine prevents the failure, we need losses that describe each action's consequences, including downtime and remaining risk. The probability of failure under the intervention may differ from the probability of failure if the machine continues operating. We cannot put the observed failure probability into both action branches without an argument that this is legitimate.

That is where decision theory meets causal inference. Forecasting asks what will occur under a specified observational regime. Policy choice often asks what would occur if we intervene. A model of how actions affect outcomes is then part of the problem. Our classification example is useful because it shows the expected-loss algebra cleanly, but a production control policy would need a richer state and action model.

The same issue appears when there are more than two actions. Perhaps we can inspect the machine, slow it down, shut it off, or continue normally. Each action has its own possible losses across failure states. If the action is a real intervention, its associated outcome distribution may also change. A decision rule is a mapping from observed information to an action, not merely a number written on a dashboard.

## What is an observation worth?

Suppose we can purchase a diagnostic test before choosing whether to raise the alarm. The test has eighty percent sensitivity: when a failure is truly present, it reports positive eighty percent of the time. It has ninety percent specificity: when no failure is present, it reports negative ninety percent of the time. Suppose the test costs zero point one two loss units. Is the information worth buying?

Let's do this without approximating the intermediate probabilities. Before testing, the failure probability is zero point one eight. The joint probability of failure and a positive result is zero point one eight times zero point eight, which is zero point one four four. The joint probability of no failure and a false positive result is zero point eight two times zero point one, which is zero point zero eight two. Positive results therefore occur with probability zero point two two six. Of those results, about sixty-four percent arise from genuine failures.

A negative result has a different composition. Failure with a false negative result has probability zero point one eight times zero point two, or zero point zero three six. No failure with a true negative result has probability zero point eight two times zero point nine, or zero point seven three eight. The posterior probability of failure after a negative result is thus about four point seven percent. It falls below our one-sixth alarm threshold, while the positive-result posterior lies well above it.

Our optimal test-based policy is therefore to raise an alarm on a positive result and stay quiet on a negative result. Now calculate its expected loss by following the mistakes. False positives occur with joint probability zero point zero eight two and cost one unit each, contributing zero point zero eight two. False negatives occur with probability zero point zero three six and cost five, contributing zero point one eight. The classification loss after using the test is zero point two six two. Adding the test cost gives zero point three eight two.

Without the test, our optimal expected loss was zero point eight two. With it, expected loss is zero point three eight two. The net expected improvement is zero point four three eight units. This is the expected value of sample information minus its acquisition cost, under the stipulated model. The test is useful, not merely because it is accurate, but because its results can change the selected action in ways that reduce expected loss.

Here is a general theorem hiding in this numerical exercise. If information can be observed for free and the decision maker can always ignore it, the minimum achievable expected loss cannot increase. A policy that ignores the new observation reproduces the old decision exactly; allowing additional policies can only preserve or improve the optimum. This does not mean information is always valuable. An observation that never changes the optimal action may have zero decision value. An expensive test can have negative net value even if the raw information is useful.

The assumption that information can be ignored is important. An organization might be obligated to act once an adverse finding is known; an information-gathering process might itself damage a system; or it might change the distribution of future events. In those cases, the original decision problem has changed and the simple theorem needs to be restated with the new action set and consequences.

## Why the posterior expectation is the right object

We can derive the Bayesian rule from a more general perspective. Let theta denote the unknown state, y the observed data, a an action, and L of theta and a the loss. Bayes' rule gives a posterior distribution over theta after observing y. For each available action, integrate its loss against that posterior. Choose the action with the smallest integral.

The integration is the same operation whether theta is a binary event, a continuous regression coefficient, a vector of engineering parameters, or an unknown probability distribution. What changes is the action space and the loss function. Under squared-error loss, when an action is a numerical estimate of theta, the posterior mean is optimal. Under absolute-error loss, a posterior median is optimal. If the action is a binary decision with unequal error costs, the rule is a probability threshold. These results are different faces of the same minimization principle.

For squared error, the reason is especially transparent. The posterior expected square of a minus theta can be decomposed into the posterior variance of theta plus the square of a minus the posterior mean. The variance is fixed once the data are known. Only the second term depends on our chosen estimate. It is minimized when a equals the posterior mean. If our interest is instead in the absolute size of errors, the median emerges because moving the estimate trades probability mass to its left against probability mass to its right.

We should distinguish a posterior action from a posterior prediction. The posterior mean is not always the most probable parameter value, and neither need be the best action under asymmetric costs. Indeed, if a forecast is used to make a sequence of distinct decisions, a full probability distribution can be more useful than any single optimal point estimate. The same posterior can support a repair decision today and an inventory decision tomorrow with entirely different loss functions.

## Proper forecasts, optimal decisions

Earlier probability lectures developed proper scoring rules, such as the Brier score, for evaluating probabilistic predictions. Why should we care about proper forecasting if decisions ultimately involve costs? Because truthful, calibrated probabilities are reusable. A forecast scored under a strictly proper rule is incentivized, in expectation, to report the actual conditional probability. A decision maker can then apply a loss model suited to the particular situation.

But a good probability score does not prove a good policy. A model might be well calibrated for observed outcomes while the policy changes those outcomes. A loss matrix might omit a cost that stakeholders would regard as decisive. A diagnosis might be accurate for one deployment population and poorly calibrated for another. Good decision-making demands both credible probabilities and defensible consequences.

One may also ask whether randomized decisions are ever worthwhile. In a finite, unconstrained Bayesian problem, randomizing among actions cannot improve on the lowest conditional expected loss, because a random mixture of losses is a weighted average of the constituent losses. At a tie, a randomized decision may be equally good. Under worst-case objectives or strategic interactions, randomization can have a different role, as we will encounter in minimax theory.

## The calculation to take away

A forecast of eighteen percent led us through several choices. With equal error costs, it would not trigger an alarm. With a five-to-one miss cost, it did. With an informative test, it became worthwhile to delay the classification decision until the extra observation arrived. None of these changes required us to alter the original probability. They came from making the decision problem explicit.

This is why probability is not yet policy. A decision combines evidence with objectives and consequences. Once those ingredients are written down, the resulting rule can be derived, criticized, and improved. And when the evidence or objectives change, we can see exactly which part of the argument needs to change with them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let state \(\theta\in\Theta\), observed data \(Y\), action \(a\in A\), likelihood \(p(y\mid\theta)\), prior \(\pi(\theta)\), and loss \(L(\theta,a)\). A Bayes action given \(y\) solves
\[
 a^*(y)\in\operatorname*{argmin}_{a\in A}\int_\Theta L(\theta,a)\,\pi(d\theta\mid y).
\]
The unrestricted binary classification example gives
\[
\begin{array}{c|cc}
 & \theta=0 & \theta=1\\ \hline
 a=\text{alarm} & C & 0\\
 a=\text{quiet} & 0 & M
\end{array},\quad
 a^*=\text{alarm}\iff p(\theta=1\mid y)>\frac{C}{C+M},
\]
with either action optimal at equality.

**Value of the diagnostic.** Prior failure probability \(p=.18\); sensitivity \(.8\); specificity \(.9\). Joint probabilities \(P(\theta=1,T=+)=.144\), \(P(\theta=0,T=+)=.082\), \(P(\theta=1,T=-)=.036\), \(P(\theta=0,T=-)=.738\). With \(C=1\), \(M=5\), optimal no-test loss \(\min(.82,.9)=.82\). Optimal loss after test, before test cost, \(.082+5(.036)=.262\). Net value with test cost \(.12\) is \(.82-(.262+.12)=.438\).

**Posterior means and medians.** With finite second moment,
\[
 E[(a-\theta)^2\mid y]=\operatorname{Var}(\theta\mid y)+(a-E[\theta\mid y])^2.
\]
With absolute loss and a posterior CDF \(F\), any posterior median (\(F(a)\ge1/2\) and \(F(a^-)\le1/2\)) minimizes \(E[|a-\theta|\mid y]\).

**Exercises and solutions.** (1) With false-alarm cost two and missed-failure cost eight, threshold? *One fifth.* (2) With posterior failure probability .18 under those costs, alert? *No: .18 is below .2.* (3) Why is cost-free optional information never harmful under the same decision model? *A policy can ignore the information, so the available policy class has expanded.* (4) Could a calibrated probability justify an intervention that changes the event being forecast? *Not without causal assumptions about intervention-specific outcomes.*

### Sources and further reading

- William Fithian, *Statistical Decision Theory*, Berkeley STAT 210A: https://www.stat.berkeley.edu/~wfithian/courses/stat210a/models.html
- Robert L. Winkler, *Introduction to Bayesian Inference and Decision*, second edition.
- Related existing lecture: `probability-measure:008000` (Bayesian inference, identification and calibration).
