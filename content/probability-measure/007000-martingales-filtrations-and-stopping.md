# 007000 - Martingales, Filtrations, and the Limits of Stopping Rules

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** integrable random variables, conditional expectation and countable events. **Theme:** fair increments, information through time, and when stopping preserves expectation.

<!-- BEGIN SPOKEN LECTURE -->

# Martingales, Filtrations, and the Limits of Stopping Rules

Imagine walking along a number line. Each time a fair coin lands heads, you take one step to the right; each time it lands tails, one step to the left. You begin at zero. After a hundred steps your position could be positive or negative. You can watch your entire path and decide when to stop walking. Could a clever stopping rule make your final expected position positive even though the coin is fair?

One tempting rule is to stop the first time you reach plus one. It seems that you will eventually do so, and when you do, your final position is exactly plus one. Have we turned a fair game into a guaranteed gain? The answer exposes why probability must distinguish stopping at a fixed time, stopping at a random but bounded time, and stopping at an almost surely finite time that may have an enormous tail.

The language for this question is the language of martingales. A martingale is a random process whose conditional expected next value, given all information observed so far, equals its present value. It is a precise model of fair evolution with respect to an information history. We will construct that history, prove a bounded stopping theorem, and then examine a stopping rule that violates the extension one might be tempted to make.

## Begin with a fair random walk

Let each coin flip contribute plus one for heads and minus one for tails. Write the position after n flips as the sum of the first n increments. Its unconditional expected position is zero, because every increment has mean zero and expectation is additive. But an unconditional average alone does not tell us whether the walk is fair from the viewpoint of someone watching its history.

Suppose five flips have already happened. The current position might be three. The fair-coin assumption says the next increment is equally likely to be plus one or minus one, independently of the earlier flips. So the conditional expected next position is three. The path is not expected to return to zero in a single step. Its expected future position, given the present, is the current position.

The same argument holds at any fixed time. The observed past determines today's position, while the next increment has conditional mean zero. Add the two contributions and we obtain the martingale property. This is the key distinction: the process has no expected change, given what the observer has seen, not merely no average change over all possible paths.

Now change the coin so that heads appears with probability six tenths. The expected increment is positive two tenths. The position alone is no longer a martingale under the natural information history. If we subtract two tenths times the number of flips, however, the centered process is a martingale. This trick of subtracting predictable drift will reappear in time-series analysis and stochastic optimization.

Martingale does not mean constant, or nearly constant, or low variance. Our fair walk typically spreads farther from zero as time passes. The martingale condition controls the conditional mean of the next change, not the size of fluctuations. A fair game can be risky; a process with zero expected increment can still have very large outcomes.

## A filtration describes accumulating information

At time zero we know nothing about future flips. At time one we know the first flip. At time two we know the first two, and so on. Each time reveals more events that we can determine. Mathematically we represent this by a sequence of sigma algebras, each contained in the next. Such a sequence is called a filtration.

A process is adapted to the filtration when its value at each time can be determined from information available at that time. The walk's position after ten flips is adapted to the history of ten flips. Tomorrow's flip is not known from that history. An apparently excellent predictor that secretly reads tomorrow's flip is not adapted to today's information, so it cannot be treated as an admissible decision rule.

A discrete-time martingale must be adapted, each value must be integrable, and its next conditional expectation given the current information must equal the present value. A submartingale replaces equality with greater than or equal; a supermartingale replaces it with less than or equal. The names concern conditional drift rather than guaranteed monotonic paths.

If a gambler's wealth process is a supermartingale, the best conditional expected change is nonpositive. That does not rule out winning on a particular path. It says no systematic expected gain can be extracted from the past under the stated probability model and allowable strategy.

The filtration matters. A process could be a martingale relative to a limited observer but not relative to someone who has advance information. A fair-looking betting scheme can rely on the observer not noticing predictive variables. It is not enough to check marginal distributions without identifying what was known before each decision.

## Stopping times can depend on the past, not the future

A stopping time is a random time at which we choose to quit according to what has been observed so far. At time n, we must be able to decide from the information then available whether the procedure has already stopped. The rule “stop at the first heads” is a stopping time. The rule “stop at the last heads that occurs in the next hundred flips” is not a stopping time with respect to the natural filtration, because at an earlier head we do not yet know whether a later head will arrive.

Stopping times express an important operational restriction. A gambler may react to previous wins and losses and the current bankroll. They may not choose their earlier actions using unseen future outcomes. A mathematical argument that ignores this requirement can smuggle future information into a purported strategy.

Let T be the first time our fair walk reaches plus one. At each n we can tell whether this has happened, so T is a stopping time. Before examining it, consider a simpler rule: stop when the walk reaches plus one, or stop after at most one hundred flips, whichever occurs first. This rule is a bounded stopping time; it is never larger than one hundred.

We can ask for the expected position at this bounded stopping time. The optional stopping theorem tells us that for an integrable martingale and a bounded stopping time, the expected stopped value equals the initial expectation. In the random-walk example, the expected stopped position is zero.

This result may seem to conflict with the fact that some paths stop at plus one. The answer is that other paths hit the one-hundred-flip deadline without ever reaching plus one and can have negative positions. Those adverse outcomes balance the positive stopped paths in expectation.

## A bounded stopping theorem, proved from increments

We can prove this version without advanced machinery. Fix a deterministic upper bound N on the stopping time T. Express the stopped value as the starting value plus one term for every possible step up to N. At step k, include the process's increment only if the procedure has not stopped before that step.

The event “we have not stopped before step k” is determined by the information at time k minus one. That is exactly where the stopping-time hypothesis enters. The next increment of a martingale has conditional expectation zero given that information. Multiplying the increment by an indicator of an event known beforehand therefore gives a term with expectation zero.

There are only N such terms. We can sum their expectations without worrying about convergence of an infinite series. Every term has expected value zero, so the expected stopped process equals its starting expected value. This is optional stopping for bounded stopping times.

The proof reveals three ingredients. We cannot know the future when deciding whether to include an increment. We need the conditional mean-zero property relative to the relevant information. And we use a deterministic finite bound so we may interchange expectation with a finite sum without additional conditions.

If the stopping rule is not bounded, we can still analyze the truncated times, such as the smaller of T and N. Each truncated stopping time is bounded, so the same equality holds. But to pass to the limit as N goes to infinity, we need justification for exchanging a limit with expectation. That is precisely where the seemingly paradoxical stopping rule becomes interesting.

## The walk that eventually wins one unit

Return to T, the first time a simple symmetric random walk reaches plus one. This hitting time is finite with probability one. One way to understand the claim is to place a temporary lower boundary at negative k. Starting at zero, the probability of hitting plus one before negative k is k divided by k plus one. As k grows, that probability approaches one. Since finite intervals are exited almost surely, the event of ever reaching plus one has probability one.

At the stopping time T, the walk's position is plus one. So the expected stopped position is also plus one, provided we understand the stopped value as the almost-sure limit. Yet the initial expected position was zero. Why does this not refute optional stopping?

Because T is not bounded and does not have finite expectation. The walk may reach plus one quickly, but some paths spend a very long time far below zero before returning. The very rare, very long excursions matter to the expected number of steps and to the expectation of the truncated stopped positions.

For every finite N, the expected position at the earlier of T and N is zero. As N increases, the stopped position converges to plus one almost surely. But expectation does not commute with this limit here. Negative positions on paths that have not yet hit plus one compensate for the winning paths, and the contribution of those rare negative outcomes does not disappear in the way required for convergence in mean.

We have already seen this type of failure with narrow, tall spikes in measure theory. Here the rare tail events do not produce tall positive spikes; they produce sufficiently severe negative contributions. In both examples, pointwise or almost-sure convergence alone cannot justify passing an expectation through the limit.

## Why the expected stopping time must be infinite

We can verify the failure of integrability without computing the entire distribution of T. Suppose for contradiction that the expected number of steps until hitting plus one were finite. The walk's increments have absolute value one. The difference between the stopped value at T and the stopped value at the earlier of T and N is bounded in absolute value by the number of steps remaining after N, if any.

As N grows, that remaining number goes to zero on every path. It is bounded by T, which has finite expectation under the assumption. Dominated convergence would then imply convergence in expected absolute difference. Consequently the expected positions at truncated stopping times would converge to the expected position at T.

But all the truncated expectations equal zero by bounded optional stopping, whereas the expected position at T equals one. Contradiction. Therefore the expected hitting time cannot be finite, even though the hitting time is finite almost surely.

This proof is worth hearing twice in spirit, if not in words. The stopping time is finite on almost every path, but its mean is infinite. These are distinct claims. An operation may terminate almost surely and still have infinite expected running time. In randomized algorithms, this difference can be the difference between a theoretically terminating procedure and a procedure whose expected resource cost is unacceptable.

There is a complementary optional-stopping theorem: for a martingale with uniformly bounded increments and a stopping time with finite expectation, expected value is preserved. Our argument shows why both a moment condition on T and control over increments can be useful. More general hypotheses, such as uniform integrability of the stopped martingale family, can replace these sufficient conditions.

## A second proof technique: conditioning on the next step

There is another way to see why the martingale definition is useful. Suppose we care about the expected future value of a quantity after several additional flips. We could condition first on the information available just before the final flip, and replace the final value by its conditional expectation, which equals the value one step earlier. We then repeat this operation one step at a time. The successive replacements reduce the final expectation to the current value. This is an iteration of the tower property, and it works for every fixed finite horizon.

The argument resembles backward induction in a decision tree. At each node, the fair future increments average to zero. But a stopping rule that can continue for arbitrarily long does not present one finite tree of fixed depth. Even if each branch ends eventually with probability one, the limiting value may fail to preserve the expectation of finite truncations. The missing step is not a clever conditional calculation; it is a convergence theorem.

The example also distinguishes an ordinary prediction from a strategy. A bettor might know the entire distribution of the process and still have no ability to change its conditional mean, while an observer using a forecast can update their estimate as information grows. Both involve conditional expectations, but only a strategy that is adapted and meets suitable integrability constraints can be inserted into the optional-stopping argument.

## What strategies can and cannot guarantee

A gambler might propose varying the size of a bet after each loss, perhaps doubling until the first win. If there were no capital constraints, one could arrange a gain of one unit whenever a win eventually arrives. This does not create a free expected profit under a valid martingale model with the hypotheses required by optional stopping. Instead, exposure to rare enormous losses or unbounded borrowing breaks the conditions under which the naïve expectation calculation would be legitimate.

An important question is whether a strategy itself preserves the martingale property. If the wager at each time is determined by information already available, and the resulting wealth increments satisfy the necessary integrability conditions, multiplying a fair increment by the predetermined wager keeps its conditional mean zero. This is the basis of the discrete stochastic integral.

But integrability is not a formality. A strategy can choose enormous stakes, and one cannot simply assume the resulting wealth is integrable or that a limiting stopped wealth retains the expectation of its finite truncations. Practical constraints such as capital, position limits, and forced liquidation are also part of the correct model. A statement about an idealized infinite credit line is not a promise about a feasible trading strategy.

Martingales are used far beyond gambling. A statistical estimator may be updated after each observation. A randomized algorithm may reveal new data one step at a time. We can track the conditional expectation of a fixed final quantity as the information history grows; those successive forecasts form a martingale. This constructs a martingale from any integrable terminal random variable and a filtration.

Consider a hidden coin bias that is revealed only indirectly through observations. The conditional probability of a fixed event, such as “the bias exceeds one half,” changes as evidence arrives. If the underlying probabilistic model is coherent and we condition on nested information sets, these conditional probabilities form a bounded martingale. They fluctuate, sometimes upward and sometimes downward, but their conditional expected future value equals their present value. The tower property is the mathematical reason.

Bounded martingales also enjoy convergence theorems under appropriate conditions. Because conditional probabilities stay between zero and one, their trajectories have a much better-behaved limit than an unbounded random walk. This helps explain how sequential learning can update uncertainty without making any observed trajectory monotone.

## Where the argument depends on the model

The fairness claim is conditional on the probability law of the coin. If the coin has a changing bias, or the next flip is correlated with recent flips, an apparent mean-zero increment may no longer have zero conditional mean given the full history. In that case the original walk need not be a martingale. Subtracting an unconditional average drift may still be insufficient; we would need to subtract the conditional expected increment at each step.

This is why a martingale is not a synonym for a random sequence whose increments have average zero. Its definition contains an information structure and a conditional expectation. A model can pass a simple check of average increments while failing the test that matters for an adaptive observer. The distinction is particularly important when algorithms choose their future actions using previous outcomes.

## Stopping, selection, and statistical evidence

Sequential experimentation presents a related issue. Suppose an analyst repeatedly tests a hypothesis and stops collecting data as soon as an ordinary fixed-sample significance threshold is crossed. A calculation calibrated for one prespecified sample size may not control the probability of a false positive when the analyst is allowed to look repeatedly and stop opportunistically.

Martingale methods can construct statistics with guarantees under optional stopping, but those guarantees depend on the design of the statistic and the precise null model. A nonnegative test supermartingale started at one, for example, can yield an anytime-valid bound through a maximal inequality. That result is not permission to stop using arbitrary p-values without adjustment.

This also illustrates why adaptedness is not a technicality. A procedure designed using a future data point may seem calibrated when inspected retrospectively, while its proof assumes the data point was unavailable at the decision time. The filtration is a mathematical record of what information the procedure legitimately possessed.

The opening question now has a precise resolution. A fair walk remains fair at every bounded stopping time. A rule that stops the first time it reaches plus one succeeds almost surely, yet may require an infinite expected waiting time. The stopped values converge almost surely while their expectations fail to converge. There is no contradiction: the theorem for bounded stopping times never asserted that every almost-surely finite stopping rule preserves expectation.

Martingales teach a general discipline. Define what is observable, define the random time from that information, check integrability or uniform integrability before exchanging limits and expectations, and distinguish a successful outcome on almost every path from a finite expected cost. Fairness is an equation about conditional expectation. Whether a stopping strategy is legitimate depends on the conditions surrounding that equation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \((\mathcal F_n)_{n\ge0}\) be a filtration, \(M_n\in L^1(P)\), and \(M_n\) be \(\mathcal F_n\)-measurable. The martingale property is
\[
E[M_{n+1}\mid\mathcal F_n]=M_n\quad\text{a.s.}
\]
A stopping time \(T\) satisfies \(\{T\le n\}\in\mathcal F_n\) for every n. For \(T\le N\) a.s.,
\[
M_T=M_0+\sum_{k=1}^N\mathbf1_{\{T\ge k\}}(M_k-M_{k-1}),
\]
where the indicator is \(\mathcal F_{k-1}\)-measurable. Consequently \(E[M_T]=E[M_0]\).

**Hitting a level.** Let \(M_n=\sum_{i=1}^n\xi_i\), where \(P(\xi_i=1)=P(\xi_i=-1)=1/2\) independently, and \(T=\inf\{n\ge0:M_n=1\}\). For \(T_k=\inf\{n:M_n\in\{-k,1\}\}\), bounded optional stopping of \(T_k\wedge N\), followed by bounded-value dominated convergence as \(N\to\infty\), shows \(P(M_{T_k}=1)=k/(k+1)\). Hence \(P(T<\infty)=1\). But \(E[T]=\infty\), by contradiction using bounded increments, dominated convergence of \(M_{T\wedge N}\to M_T\), and the mismatch of expectations \(0\) and \(1\).

A useful sufficient condition: if \(|M_{n+1}-M_n|\le C\) a.s. for all n and \(E[T]<\infty\), then \(E[M_T]=E[M_0]\), by domination with \(CT\). Another sufficient condition is uniform integrability of the stopped martingale family plus almost-sure convergence.

**Conditional-probability martingale.** For fixed \(A\in\mathcal F\), \(M_n=P(A\mid\mathcal F_n)=E[\mathbf1_A\mid\mathcal F_n]\) is a bounded martingale by the tower property.

**Anytime-valid bound.** A nonnegative supermartingale \(E_n\) with \(E[E_0]\le1\) satisfies Ville's inequality:
\[
P\!\left(\sup_{n\ge0}E_n\ge 1/\alpha\right)\le\alpha
\quad(0<\alpha<1).
\]
The supermartingale and nonnegativity hypotheses are essential; this does not apply to arbitrary sequential test statistics.

### Exercises with answers

1. **Information.** Is “stop at the first head” a stopping time? **Answer:** yes; by time n, we know whether a head occurred.
2. **Future leak.** Is “stop at the last head among the first 100 tosses” a stopping time for the natural filtration? **Answer:** generally no; a future flip determines whether a head is the last.
3. **Fairness.** What is \(E[M_T]\) for a bounded stopping time applied to an integrable martingale starting at zero? **Answer:** zero.
4. **Counterexample.** Why is \(M_T=1\) compatible with \(E[M_{T\wedge N}]=0\) for every N? **Answer:** almost-sure convergence of stopped values does not imply convergence of their expectations; the family is not uniformly integrable.
5. **Learning.** Why are conditional probabilities of a fixed event a martingale as information accumulates? **Answer:** nested conditioning satisfies the tower property.

### References

- MIT OpenCourseWare 18.175, *Theory of Probability*, lectures on random walks and martingales.
- MIT 18.600, *Probability and Random Variables*, lectures on martingales and optional stopping.
- MIT 18.675, *Theory of Probability*, 2019 lecture topics on optional stopping and uniform integrability.
