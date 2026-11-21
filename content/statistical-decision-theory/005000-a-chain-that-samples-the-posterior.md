# 005000 — A Chain That Samples the Posterior

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** conditional probability, finite Markov chains, weighted averages. **Theme:** construct a Markov chain with a chosen target distribution without needing its normalizing constant.

<!-- BEGIN SPOKEN LECTURE -->

# A Chain That Samples the Posterior

Suppose we have a posterior distribution that can be evaluated up to an unknown constant, but from which we cannot easily draw independent samples. We want its expectation, credible intervals, perhaps the probability that one parameter exceeds another. The posterior is defined by multiplying a likelihood and a prior, yet integrating that product over all possible parameters is too difficult to do directly.

There is a way forward that initially sounds circular. Rather than drawing observations independently from the posterior, construct a random process whose long-run distribution is the posterior. Follow this process for many steps, and use the visited states to estimate posterior quantities. This is Markov chain Monte Carlo.

We already met Markov chains in the probability course. A transition rule determines the distribution of the next state from the present one. If the chain is appropriately ergodic, it can forget its starting point and spend time in states according to a stationary distribution. The new challenge is to design a transition rule whose stationary distribution is precisely the distribution we want. Metropolis–Hastings provides a broadly useful answer.

## Start with three states, not a large simulation

Imagine the parameter can take one of three values. We label them zero, one, and two, and assign unnormalized posterior weights one, two, and three. The target probabilities are therefore one sixth, one third, and one half. I am telling you the normalizing sum here only so we can verify every step. The algorithm we are about to construct will not require it.

We propose moving from the current state to one of the other two states, each with probability one half. This proposal is symmetric: the chance of proposing state two from state zero equals the chance of proposing state zero from state two. But if we accepted every proposal, the resulting random walk would spend equal time at all three states. We need to favor moves toward states with greater target weight, without forbidding occasional moves back.

The Metropolis rule says to accept a proposal with probability equal to the smaller of one and the ratio of target weight at the proposed state to target weight at the current state. Since our proposal is symmetric, no proposal correction is needed. If we propose going from weight one to weight three, accept for sure. If we propose going from weight three to weight one, accept with probability one third. A rejected move leaves us in the current state, so rejection creates a self-loop in the Markov chain.

Let's write out all three transition rows. From state zero, both destinations have higher weights, so we move to state one with probability one half and to state two with probability one half. From state one, proposing state zero happens with probability one half and is accepted with probability one half, yielding transition probability one quarter. Moving to state two has transition probability one half. The remaining one quarter is a self-loop. From state two, moving to zero happens with probability one half times one third, or one sixth. Moving to one happens with probability one half times two thirds, or one third. The remaining one half is a self-loop.

Each row sums to one. The resulting matrix is not symmetric, and it does not need to be. Instead, it satisfies a more important relationship between transitions in opposite directions.

## Detailed balance, checked pair by pair

For a target distribution pi, detailed balance says that the long-run probability mass flowing from state i to state j is equal to the mass flowing from j to i. In symbols, pi of i times the transition probability from i to j equals pi of j times the reverse transition probability.

Check zero and one. We have one sixth times one half, or one twelfth, flowing from zero to one. In the reverse direction, we have one third times one quarter, also one twelfth. For zero and two, the forward flow is one sixth times one half, again one twelfth. The reverse flow is one half times one sixth, equal to it. For one and two, the forward flow is one third times one half, or one sixth. The reverse is one half times one third, also one sixth.

That proves detailed balance for our three-state chain. Summing the balance equation over all possible previous states shows that pi is stationary. The intuition is that every pair exchanges exactly the same mass in both directions, so the total mass at each state remains unchanged after one transition.

Detailed balance is sufficient for stationarity, but it is not necessary. Some useful Markov chains are not reversible. We use detailed balance here because it offers an easily checked construction. To claim convergence from arbitrary starting states, we also need suitable communication and recurrence conditions. Our finite chain is irreducible: every state can reach every other. It is aperiodic, because states one and two have self-loops and the chain communicates. Therefore its distribution approaches pi as the number of transitions grows.

The target expectation of our numerical state is zero times one sixth, plus one times one third, plus two times one half, which is four thirds. If we run the chain long enough and average the visited states, the ergodic theorem tells us that this average approaches four thirds under the usual conditions. It is an average of dependent samples, not an average of independent draws, but dependence need not prevent consistent estimation.

## Why the normalizing constant disappears

In realistic Bayesian problems the target density is proportional to likelihood times prior, perhaps evaluated in hundreds of dimensions. Write the unnormalized posterior as w of theta, and suppose the normalizing constant Z is an integral that we do not know. The probability density is w divided by Z.

In the Metropolis acceptance ratio, the target value at the proposal is divided by the target value at the current state. The factor one over Z appears in numerator and denominator and cancels. We only need to evaluate the relative target weights. This cancellation is a major source of the method's generality.

If our proposal distribution is not symmetric, we must also correct for how likely it was to propose the move in each direction. The Metropolis–Hastings acceptance probability is the smaller of one and the target weight at the proposed state times the probability of proposing the current state from the proposed one, divided by the target weight at the current state times the probability of proposing the proposed state from the current one.

Think of it as correcting two potential biases. The posterior-weight ratio favors high-probability states, while the proposal ratio cancels an imbalance in how candidate moves are generated. The result satisfies detailed balance where the transitions are mutually accessible and the usual support assumptions hold.

Why does the formula work? For two distinct states x and y, the probability flow from x to y is the target weight at x times the proposal probability from x to y times the smaller of one and the reverse weighted-proposal ratio. Algebraically this equals the smaller of the two directed weighted-proposal quantities. That expression is symmetric when x and y are exchanged. Pairwise equality follows immediately.

This is the core correctness proof of Metropolis–Hastings. It is not a proof that a particular chain mixes quickly. Stationarity, convergence, and computational efficiency are separate results.

## How a valid chain can be a bad numerical method

Suppose our posterior has two narrow, distant peaks, separated by a valley where the target density is extremely small. A random-walk proposal that makes only tiny changes can explore one peak beautifully and never cross the valley during the available computation. The output may look stable while omitting half the important posterior mass. We have not violated detailed balance: the chain might eventually cross. We have chosen a transition rule with a terrible finite-time behavior.

There is a second failure mode at the opposite scale. If proposals are enormous, they may land in regions with negligible posterior density and be rejected almost every time. The chain then repeats the same value for long stretches. Both a proposal that is too small and one that is too large can produce highly correlated samples, albeit for different reasons.

The chain's acceptance rate alone does not settle efficiency. A high acceptance rate can occur because proposed movements are minuscule. A low rate can occur because a proposal distribution is poorly matched to the target. The quantity of real interest is how much independent information the chain provides about the functions we want to estimate per unit of computation.

For a stationary chain and a function f, the Monte Carlo average of f has an asymptotic variance involving the sum of temporal autocorrelations of f along the chain. If the lag-one and subsequent correlations remain positive for a long time, one hundred thousand draws may contain far less information than one hundred thousand independent draws. Under appropriate regularity, the effective sample size summarizes that reduction for the particular function being estimated.

This function-specific qualification is essential. A chain might estimate a posterior mean reasonably well while poorly exploring a rare tail event. One effective-sample-size number cannot certify every possible posterior quantity.

## Burn-in, warm-up, and multiple chains

Because we do not start our chain from the stationary distribution, early draws may reflect the starting state. One response is to discard an initial segment, often called burn-in or warm-up. That can reduce initialization bias, but throwing away the first thousand iterations does not establish convergence. A chain trapped in one mode can remain trapped after discarding a million iterations.

Running several chains from dispersed starting points offers stronger practical diagnostics. If the chains produce visibly different distributions or remain in different modes, we know something is wrong. Agreement is more reassuring, but not conclusive: multiple chains can all miss the same region, especially if their initialization mechanism has the same blind spot.

More demanding modern diagnostics examine rank-normalized between-chain and within-chain variation, effective sample sizes, and for gradient-based methods certain numerical pathologies. We will study these in a later lecture. The point here is conceptual: the theorem that the desired distribution is stationary does not tell us how close the finite run is to that distribution.

For some simple finite chains, transition-matrix powers let us calculate convergence exactly. For a complex continuous posterior, we rarely know the mixing rate at the necessary precision. This is why diagnostics, model reparameterization, and independent reasoning about the geometry of the target are indispensable parts of computation.

## A posterior calculation is a layered claim

When someone reports a Bayesian credible interval obtained by MCMC, several arguments are being combined. The likelihood and prior define a posterior distribution. The MCMC transition is intended to preserve that posterior. The finite simulation is intended to approximate expectations under that distribution. Finally, the model is supposed to describe the application well enough that those expectations are useful.

An error at any layer can affect the reported interval. A wrong likelihood can give a perfectly sampled wrong posterior. A correct likelihood can be paired with a poorly mixing sampler. A well-mixed chain can produce a noisy estimate of a rare-event probability because there are too few effective draws in the tail. Even an accurate posterior interval may not justify a policy decision if the loss function or causal consequences are missing.

Our three-state example is small enough to keep these claims distinct. We designed a chain using unnormalized weights. We checked every detailed-balance equation. We verified irreducibility and aperiodicity. We know the target mean exactly, so we can compare a simulation with four thirds. Each step has a different role. The lesson is not that Monte Carlo makes integration easy by magic. It replaces an intractable direct calculation with a stochastic computation whose mathematical target and practical convergence must both be understood.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Target and transitions.** For target \(\pi=(1,2,3)/6\), propose either other state with probability \(1/2\). Symmetric Metropolis gives
\[
P=\begin{pmatrix}0&1/2&1/2\\1/4&1/4&1/2\\1/6&1/3&1/2\end{pmatrix},\quad
\pi P=\pi,\qquad\pi_iP_{ij}=\pi_jP_{ji}.
\]
The chain is finite, irreducible and aperiodic, so \(P^t(x,\cdot)\to\pi\). For \(f(0)=0,f(1)=1,f(2)=2\), \(E_\pi f=4/3\).

**Metropolis–Hastings.** With unnormalized target \(w(x)\), proposal \(q(y\mid x)\), and mutually supported proposals, define
\[
\alpha(x,y)=\min\left(1,\frac{w(y)q(x\mid y)}{w(x)q(y\mid x)}\right).
\]
Then \(w(x)q(y\mid x)\alpha(x,y)=\min\{w(x)q(y\mid x),w(y)q(x\mid y)\}\), symmetric in \(x,y\). The normalizing constant cancels. Additional irreducibility/ergodicity assumptions are needed for convergence.

**Effective sample size heuristic.** For a stationary, sufficiently mixing chain and square-integrable \(f\), with autocorrelations \(\rho_f(k)\) summable,
\[
\operatorname{Var}(\bar f_N)\approx\frac{\operatorname{Var}_\pi(f)}{N}\left(1+2\sum_{k=1}^\infty\rho_f(k)\right),\quad N_{eff,f}\approx\frac{N}{1+2\sum_{k\ge1}\rho_f(k)}.
\]
Estimate cautiously; nonstationarity and multimodality can invalidate naive correlation estimates.

**Exercises and solutions.** (1) If current state is two, what is the probability of moving to zero? *One sixth.* (2) Check the flow balance between states one and two. *Each direction carries mass one sixth.* (3) Does knowing \(\pi\) is stationary establish useful mixing speed? *No.* (4) Why is posterior normalization unnecessary for MH? *The unknown constant cancels in the ratio.*

### Sources and further reading

- W. K. Hastings, *Monte Carlo Sampling Methods Using Markov Chains and Their Applications* (1970).
- Charles J. Geyer, *Introduction to Markov Chain Monte Carlo*, in the *Handbook of Markov Chain Monte Carlo* (2011).
- Stan Reference Manual, *MCMC Sampling*: https://mc-stan.org/docs/2_37/reference-manual/mcmc.html
- Related existing lecture: `probability-measure:009000` (Markov chains and stationarity).
