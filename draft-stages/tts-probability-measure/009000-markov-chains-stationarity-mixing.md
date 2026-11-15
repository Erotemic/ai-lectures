# 009000 - Markov Chains: Stationarity, Mixing, and Randomized Computation

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** conditional probability, finite matrices, expectation, and elementary limits. **Theme:** a dynamic system can forget its starting state without becoming independent over time.

<!-- BEGIN SPOKEN LECTURE -->

# Markov Chains: Stationarity, Mixing, and Randomized Computation

Imagine inspecting a machine once a day. Some days it runs normally; on others it is under repair. You want to predict whether it will be running tomorrow, then next week, and eventually at a randomly selected time far in the future. Yesterday's condition surely matters. But perhaps the exact sequence of events last month does not matter once today's condition is known. That possibility gives us a Markov model.

A Markov chain is a random process with a particular rule for how its state evolves. Conditioned on the present state, the distribution of the next state does not depend on the earlier states. This is not a claim that the past is irrelevant in reality. It is a modeling decision about what the word state contains. If the probability of repair depends on how long a component has been broken, then a state that says only broken or working may not be sufficient. We might need to include repair age, hidden damage, or the technician's queue.

The power of the Markov idea comes from keeping those two matters apart. One matter is the definition of a stochastic process with memory summarized by its present state. The other is whether that definition approximates a particular physical or computational system. Mathematics can establish exactly what follows from the first. Data and judgment are needed for the second.

## Two states and a forecast that changes with time

Take a device with two states, working and broken. When it is working today, it will still be working tomorrow with probability eight tenths; with probability two tenths it breaks. When it is broken today, it returns to service tomorrow with probability three tenths and stays broken with probability seven tenths. These four numbers completely specify a time-homogeneous, two-state Markov chain. Time-homogeneous simply means the rule remains the same from one day to the next.

Suppose the machine is definitely working this morning. Tomorrow it has an eighty percent chance of working. What about the day after? There are two routes to a working machine: it works tomorrow and stays working, or it is broken tomorrow and gets repaired. Their probabilities are eight tenths times eight tenths, and two tenths times three tenths. Adding them gives seven tenths. The probability has fallen from one today to eight tenths tomorrow to seven tenths after two days.

The calculation illustrates why matrix multiplication enters naturally. One transition describes one day's movement; applying the same transition rule a second time describes two days. The two-day probability is a sum over possible intermediate states. This is an application of the ordinary law of total probability, not a new independence claim. The machine's conditions on consecutive days are generally dependent.

Let the probability of working today be called p. Tomorrow's probability is eight tenths of p, plus three tenths of the probability that it is broken. The broken probability is one minus p. Collecting terms gives the simple rule: tomorrow's working probability is three tenths plus one half of today's working probability.

That affine rule has a fixed point. If the working probability is six tenths, the next day's working probability is also six tenths. Such a distribution is called stationary. It is an equilibrium for the distribution of states, not a claim that an individual machine freezes in one condition. Even at equilibrium, machines continually fail and are repaired.

A stationary fraction of six tenths makes another prediction. In a long stable simulation, we might expect the proportion of days spent working to be near sixty percent. For this finite, irreducible chain, that long-run frequency statement can be justified by an ergodic theorem. It is a separate theorem from merely solving the stationary-distribution equation. One does not get a law of large numbers for every arbitrary dependent sequence by finding a fixed point in one calculation.

## The proof of forgetting a starting distribution

We can prove more than the existence of the fixed point in this particular model. Subtract six tenths from tomorrow's working probability. The result is exactly one half of today's difference from six tenths. If today's forecast is above equilibrium, the discrepancy shrinks by half in one day; if it is below equilibrium, the discrepancy also shrinks by half.

Repeat that argument. After two days the discrepancy is one quarter as large. After three days it is one eighth as large. After t days it is the original discrepancy multiplied by one half raised to the power t. In this example, the distribution approaches the stationary distribution geometrically fast. This conclusion has a transparent reason: the transition rule contracts differences between alternative starting distributions.

Starting from certainty that the machine works, the difference from six tenths is initially four tenths. After one day the difference is two tenths, which yields eight tenths. After two days it is one tenth, which yields seven tenths. After a week, the difference is a small fraction of one percent. There is no need to invoke a vague idea that the chain has been running a long time. We have an explicit quantitative bound.

An interesting consequence is that tomorrow may still be strongly affected by today, even when the distribution at a distant time barely depends on the starting condition. The first is a statement about dependence between adjacent random states. The second is a statement about how distributions from different starts approach one another. They are related, but not identical.

To compare whole distributions, probabilists often use total variation distance. Think of two probability models assigning probabilities to the same collection of possible events. Their total variation distance is the largest disagreement they can have about the probability of any one event. For a two-state model, this is just the absolute difference between the probabilities of one of the states. So the half-per-day calculation we just made is also an exact total variation contraction.

A useful interpretation is that we have forgotten our starting conditions to a specified tolerance when even the most favorable event cannot tell those starting distributions apart by much. This description is stronger than saying that the expected number of working machines has stabilized; it controls every event that can be defined from the single present state. It does not say that the entire trajectory has forgotten its history.

## Coupling: making two random histories meet

The same idea can be proved without solving a recurrence. Imagine running two copies of the chain, one initially working and the other initially broken. We are allowed to correlate their randomness, provided each copy separately follows the correct transition probabilities. This construction is called a coupling.

One way to couple the copies is to generate the next states from the same uniform random number. Give each copy its appropriate probability of being working. With our transition rule, there is a shared range of random numbers that makes both copies working, another range that makes both broken, and a middle range where they disagree. If they initially disagree, their chance of continuing to disagree after one step is one half. Once they agree, we can use the same randomness for both and keep them together forever.

Why does this help? On every outcome where the two copies have met, their present states agree. Therefore any event that distinguishes the copies can occur only on an outcome where they have not met. The difference in the probabilities of any event is no larger than the probability of nonmeeting. In our example, that probability is at most one half to the power t.

This is the coupling inequality. The proof's central move is a comparison of events: if the coupled states agree, a proposed event cannot occur for one and fail for the other. The only disagreements arise on the exceptional set where they differ. Taking the largest possible disagreement over all events yields the total variation bound.

Coupling is useful when a system has many states and its transition matrix is too large to diagonalize. We can sometimes reason about the chance that two copies of a queue, shuffle, network state, or random algorithm become identical. Yet coupling is only a technique, not a guarantee of fast convergence. A badly chosen coupling can fail to meet quickly even when the chain mixes fast. Conversely, a slow chain may really preserve information about its starting point for a very long time.

## Three different obstructions

Consider a chain in which working always turns into broken and broken always turns into working. Its state alternates deterministically. There is a stationary distribution assigning one half to each state, because beginning with equal chances leaves equal chances after the swap. But if we start working, then at even times we are certainly working and at odd times certainly broken. The distribution never converges to the stationary one.

This is the obstruction called periodicity. Having a stationary distribution alone does not imply convergence from every starting state. In a finite irreducible chain, aperiodicity is the additional hypothesis needed for ordinary convergence to the unique stationary distribution. A small probability of staying in place often removes this particular obstruction, which is why algorithms sometimes make a random walk lazy.

Now consider a system with two disconnected regions of states. From a state in one region there is no transition to the other. The transition law can have several stationary distributions, including ones concentrated entirely in either region. We cannot expect to forget which region we started in. This is reducibility: the state space is not one communicating class.

Finally consider a chain that is irreducible and aperiodic but has two large clusters connected by a very narrow bridge. It can eventually visit everything and converge to a unique stationary distribution. Still, it may spend an enormous time inside its initial cluster before crossing the bridge. The asymptotic convergence theorem promises eventual mixing, not mixing in a convenient number of steps. The transition geometry matters to practical computation.

Those examples separate three claims that are frequently conflated: a stationary distribution exists, it is unique, and a simulation approaches it rapidly. Each claim has its own hypotheses or quantitative proof. The fact that a computer emits apparently varied samples is not evidence for all three.

## Reversibility and the balance of flow

There is another attractive way to establish stationarity. Suppose a proposed stationary distribution places some weight on each state. If the probability flow from state A to state B equals the reverse flow from B to A for every pair, then the distribution is stationary. This condition is detailed balance.

In the two-state machine, the stationary chance of working is six tenths and the chance of broken is four tenths. The fraction expected to flow from working to broken in a step is six tenths times two tenths, or twelve hundredths. The reverse flow is four tenths times three tenths, also twelve hundredths. They match. The detailed balance condition explains why the proportions can remain constant even as individual machines change state.

A chain satisfying detailed balance is called reversible with respect to that distribution. It has a kind of statistical symmetry under reversal of time when begun at stationarity. But stationarity itself does not require detailed balance. A chain moving predominantly around a directed cycle can be stationary while maintaining a net probability current. Reversibility is a sufficient and often convenient structural property, not the definition of equilibrium.

Why would a computational scientist care? Many sampling methods, including the classical Metropolis construction, are designed so that the desired distribution obeys detailed balance. This can make it relatively simple to verify that a specified probability distribution is stationary for the algorithm. Verifying that it is the desired stationary distribution is not yet verifying that a finite run has sampled it accurately.

## Sampling, random algorithms, and the meaning of burn-in

Suppose the goal is not forecasting a broken machine but drawing samples from a complicated distribution: possible arrangements of particles, candidate solutions to an optimization problem, or posterior parameter values in a statistical model. It may be easy to propose a local modification to a state and hard to draw a completely independent state from the target distribution. Markov chain Monte Carlo turns the easy local changes into a sequence whose stationary distribution is the target.

That design raises two distinct questions. First, does the transition mechanism preserve the target distribution? We may prove that using detailed balance or another invariance argument. Second, how long does it take to approach the target from the initialization we actually use? Answering the second may require coupling, spectral gaps, conductance, or problem-specific geometry. Proving the first does not answer the second.

A program often discards early states as burn-in. That can reduce initialization bias if the chain truly approaches stationarity. But the word burn-in is not a mathematical certificate. For a distribution with separated modes, a sampler can look stable for a long time while remaining trapped in one region. Several chains can even agree if they all start in the same basin. The observed time series needs model-specific diagnostics and, where possible, theoretical bounds.

There is a further trap. Samples drawn from adjacent states of a chain are correlated. If we compute their average and treat the sample count as though every draw were independent, we may substantially underestimate uncertainty. A stationary chain does not automatically produce independent data. Its covariance structure and mixing behavior determine how the variance of an average decreases. In slow mixing systems, a million updates can contain far less information than a million independent samples.

## What changes for infinite spaces and physical systems

The statements about irreducibility and aperiodicity have been deliberately framed for finite-state chains. For countably infinite or continuous state spaces, recurrence, positive recurrence, invariant probability measures, and stronger accessibility conditions demand more care. A biased random walk on an infinite line, for example, may drift away and have no stationary probability distribution, even though its one-step transitions are well defined.

A practical physical model adds another question: are the transitions time-homogeneous? Seasonal demand, aging equipment, changing policies, and learning agents can modify the transition probabilities. A stationary distribution for yesterday's transition rule need not predict tomorrow's operating regime. And hidden state can make a projected observation process non-Markov even when a more complete underlying process is Markov.

The finite calculation still supplies a powerful pattern for reasoning. Specify the state and the transition law. Compute or characterize stationary distributions. Prove whether and how fast the process forgets its initialization. Then distinguish those mathematical conclusions from claims that the transition model adequately describes the real system.

## A final diagnostic

Suppose a colleague says, “We simulated for ten thousand steps, so the samples are stationary.” What is missing? We need to know the transition rule, whether the target distribution is invariant, whether the chain can reach relevant states, and what its mixing time might be. If the process has a bottleneck, ten thousand steps may be too few. If it alternates periodically, merely waiting longer may never fix the oscillation.

Now suppose the colleague says, “The algorithm satisfies detailed balance, so every sample is independent.” That too is wrong. Detailed balance is a symmetry of probability flow under stationarity, not independence between successive states. A reversible chain can be extremely persistent.

The central lesson is more precise than the slogan that stochastic systems forget their past. Under suitable conditions, their **one-time distributions** forget where they started, and coupling or other tools can quantify that loss of information. The same process can preserve strong short-term dependence, mix slowly across barriers, or fail to converge because of periodicity. We understand a Markov model only when those possibilities have been separated.


## Hitting times, return times, and another meaning of typical

The stationary fraction of working days can be checked in a different way, using how long the machine typically remains in each state. Suppose it is working. Each morning there is a two-tenths chance that it breaks on the next transition. As long as it remains working, the next-day breaking probability stays the same. The number of working-to-working transitions before the first breakdown follows a geometric waiting-time law. Counting the transition that finally causes the breakdown, the expected length of a working run is five days.

The broken state is similar but with a three-tenths probability of repair on every transition. Counting the transition that repairs it, the expected length of a broken run is ten thirds of a day. The successive runs can be analyzed as a sequence of random cycles, one working run and one broken run. The expected proportion of working time in a cycle is the mean working-run length divided by the sum of the two mean run lengths. That calculation gives five divided by five plus ten thirds, or three fifths. It agrees with the stationary probability we derived from the transition matrix.

This agreement is instructive because it arrives from a different angle. The matrix proof asks which distribution remains unchanged under one step. The run-length argument asks how a typical long trajectory allocates its time. In a finite irreducible chain, the ergodic theorem connects those pictures. But the ratio of the expectations is not, in general, the expectation of the ratio for an individual short cycle. We use a long-run renewal argument, not a casual replacement of random quotients by quotients of averages.

There are two clocks here. One clock counts the number of days until the first transition of a particular kind, such as the next breakdown. The other measures how long it takes a distribution to become hard to distinguish from equilibrium. A process can have a moderate typical waiting time for some event and still mix slowly because of another region it rarely visits. A single expected hitting time is not a full description of mixing.

In the special two-state example, both clocks are tractable. But in a large network, a random walker might revisit a nearby node repeatedly and take a huge time to reach a distant bottleneck. The mean time to hit one designated state, the mean time to return to a starting state, and the time needed to sample approximately from stationarity are different quantities. Markov-chain analysis uses all three, depending on what the application is trying to guarantee.

This also gives us a more careful interpretation of simulation averages. When the system has reached its stationary regime and the usual ergodic hypotheses hold, its time average estimates a stationary expectation. A finite run still has fluctuations, and the amount of uncertainty depends on the chain's temporal correlations. We can learn the long-run mean from one sufficiently representative trajectory without pretending its observations were independent. The theorem justifying that learning is not the same theorem that establishes stationarity.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let the row-stochastic matrix, in state order (working, broken), be
\[
P=\begin{pmatrix}0.8&0.2\\0.3&0.7\end{pmatrix},\qquad
\pi=(0.6,0.4),\quad \pi P=\pi.
\]
If \(p_t=P(X_t=\text{working})\), then
\[
p_{t+1}=0.3+0.5p_t,\qquad p_t=0.6+(p_0-0.6)2^{-t}.
\]
Thus \(\|\mathcal L(X_t)-\pi\|_{\mathrm{TV}}=|p_0-0.6|2^{-t}\).

**Finite-state convergence theorem.** If a finite chain is irreducible and aperiodic, it has a unique stationary distribution \(\pi\), and \(\|P^t(x,\cdot)-\pi\|_{\rm TV}\to0\) for every state \(x\). Irreducibility alone is insufficient (the alternating chain). No universal small mixing time is implied.

**Detailed balance.** \(\pi(i)P(i,j)=\pi(j)P(j,i)\) for all \(i,j\) implies \(\pi P=\pi\) by summation. The example satisfies \(0.6(0.2)=0.4(0.3)\).

**Coupling inequality.** For a coupling \((X_t,Y_t)\) of two laws,
\[
\|\mathcal L(X_t)-\mathcal L(Y_t)\|_{\mathrm{TV}}\le P(X_t\neq Y_t).
\]
Under the shared-uniform coupling of the two-state kernel, initially different states remain different with conditional probability \(0.5\) until meeting; once equal, remain equal. Hence \(P(X_t\neq Y_t)\le2^{-t}\).

**Stationarity versus independence.** For a stationary trajectory,
\[
\operatorname{Var}\bigg(\frac1n\sum_{t=1}^n f(X_t)\bigg)
=\frac1{n^2}\left(n\gamma(0)+2\sum_{k=1}^{n-1}(n-k)\gamma(k)\right),
\]
where \(\gamma(k)=\operatorname{Cov}(f(X_0),f(X_k))\). The iid formula drops the covariance terms only when they vanish.

### Exercises with answers

1. **Two-day transition.** Starting working, find the chance of working two days later. **Answer:** \(0.8^2+0.2(0.3)=0.70\).
2. **Stationarity.** Solve \(p=0.3+0.5p\). **Answer:** \(p=0.6\).
3. **Periodicity.** Why does the deterministic two-state alternator have a stationary distribution but fail to converge from a fixed state? **Answer:** equal mixing is invariant, but the state distribution alternates between two point masses.
4. **Detail versus marginal.** Does detailed balance force independent successive samples? **Answer:** no; it guarantees reversibility under stationarity, not independence.
5. **Coupling.** Why does meeting of coupled chains bound total variation? **Answer:** whenever the coupled outcomes match, every event has the same indicator for both; probabilities can differ only on nonmeeting outcomes.

### References

- David A. Levin and Yuval Peres, *Markov Chains and Mixing Times*, second edition, with contributions by Elizabeth L. Wilmer. Chapters 1–5 and 12.
- MIT OpenCourseWare 18.175, *Theory of Probability*, lectures on Markov chains and martingales.
- Achim Klenke, *Probability Theory: A Comprehensive Course*, Markov process foundations.
