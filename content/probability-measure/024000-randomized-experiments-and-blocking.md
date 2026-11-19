# 024000 - Designing an Experiment Before Measuring Its Result

**Track:** Probability, Measure, and Statistical Reasoning. **Background:** elementary averages, random assignment, and basic probability. **Theme:** experimental units, treatments, estimands, randomization, blocking, and the scope of causal conclusions.

<!-- BEGIN SPOKEN LECTURE -->

# Designing an Experiment Before Measuring Its Result

Imagine that a laboratory has invented a new procedure for growing crystals. The new procedure looks promising. The next batch produces crystals that are, on average, two millimeters longer than those in an old notebook. Has the procedure caused a two-millimeter improvement?

Not yet. Perhaps the room was warmer. Perhaps the materials were from a different shipment. Perhaps the notebook records only the best crystals. To find out what changed the growth, we must think about the experiment before we think about the calculation.

Statistics is often presented as something we do after collecting data. But the most consequential statistical decision may come earlier: which units get which conditions, how do we choose them, and what exactly do we mean by an effect? No clever test applied afterward can recover information that the design never made available.

## What is the experimental unit?

Suppose we have twenty growth chambers. We can give ten chambers the old procedure and ten the new one. Each chamber grows several crystals, and we measure every crystal. Is the sample size twenty, or hundreds?

For the causal comparison, it depends on where we apply the intervention. If the growth procedure is assigned independently to chambers, the chamber is the experimental unit. Crystals grown within one chamber share temperature, airflow, and the same treatment assignment. Recording ten crystals per chamber may improve the precision with which we measure a chamber's response. It does not create ten independently randomized chambers.

This is the distinction between an observational unit and an experimental unit. An observational unit is where we measure something. An experimental unit is the smallest object to which the treatment can be independently assigned. Confusing the two can make an analysis report confidence intervals that are much narrower than the design justifies.

We also have to say what outcome we will analyze. Average length per chamber? Total mass of crystals? The proportion passing a quality threshold? Each gives a different estimand, which is the quantity the study seeks to estimate. It may be tempting to select whichever outcome looks most exciting after seeing the data, but that changes the question and introduces further uncertainty that a single standard error does not capture.

## The two outcomes we cannot both see

Let us imagine a fixed chamber, labeled chamber seven. It has one potential result if we use the old procedure and another potential result if we use the new one. These are two answers to two different questions about the same chamber under otherwise comparable conditions. The causal effect for that chamber is the new-procedure outcome minus the old-procedure outcome.

We can observe one of those outcomes, not both, for the same chamber at the same time. This missing counterfactual is the basic difficulty of causal inference. If a chamber grows a crystal of twelve millimeters after treatment, that does not tell us whether it would have grown eleven, twelve, or fifteen millimeters without treatment.

With many chambers, we can define the average causal effect as the average of the chamber-level differences. Although we cannot inspect both potential outcomes for any single chamber, random assignment gives us a way to estimate that average.

In the simplest design, choose exactly ten of the twenty chambers at random for the new procedure, with the other ten as controls. Every set of ten is equally likely. We then subtract the mean outcome among control chambers from the mean among treatment chambers.

The result of that subtraction is random because the assignment was random. Some assignments put naturally productive chambers in the treatment group; others do the opposite. The power of the design is not that every realized assignment is perfectly balanced. It is that the assignment mechanism itself does not systematically favor one potential-outcome profile over another.

## What randomization actually guarantees

Consider an experiment with four units. Suppose their outcomes under the old treatment would be one, two, three, and four, and suppose the new treatment adds exactly two units of outcome to each. The true average effect is two.

Now assign treatment to the first and fourth units. We observe treated outcomes three and six, averaging four and a half. We observe control outcomes two and three, averaging two and a half. The difference is two, precisely the true effect.

But another valid assignment treats the third and fourth units. The treated outcomes would be five and six, averaging five and a half. The controls would be one and two, averaging one and a half. The observed difference would be four, even though every individual effect is still two.

Randomization did not make either assignment estimate exact. Instead, if we averaged the treated-minus-control difference over all six possible assignments of two treated units among four, the result would be two. For a completely randomized fixed-size design, the difference in sample means is unbiased for the finite-population average treatment effect. Its randomization distribution tells us how variable the estimate can be.

That statement has conditions. We must have well-defined interventions. Outcomes for one chamber should not depend on what treatments other chambers receive, unless we explicitly model such spillovers. Assignment must really follow the design. And an analysis that changes treatment definitions after observing outcomes is no longer the same randomized comparison.

Random assignment is not the same thing as random sampling. The first helps compare treatments causally for the experimental units. The second helps us make claims about a larger population. We can have a well-randomized experiment on a highly selected group of chambers and still need evidence before claiming that its effect applies to every factory.

## Blocking: use what you already know

Suppose the laboratory runs experiments in two rooms, one warmer than the other. Temperature has a strong effect on crystal growth. If all treated chambers happen to be in the warm room, the final comparison will be needlessly noisy or misleading.

We can improve the design by blocking. Before assignment, separate the chambers into warm-room and cool-room blocks. Randomly assign half of the chambers in each room to the new procedure and half to the old one. This ensures that treatment and control comparisons can be made within each room.

For a small, transparent example, imagine two blocks containing two units apiece. In the first room, a treated chamber has outcome eleven and a control chamber has outcome nine. In the second room, the treated chamber has outcome twenty-one and the control has nineteen. Each room's observed difference is two. Averaging those two differences gives two, even though the baseline levels differ by ten between rooms.

The arithmetic does not by itself prove a causal effect: the assignment mechanism matters. Under random assignment within blocks, however, each block's treated-control contrast is an unbiased estimate of its block-average causal effect. Weighting the block contrasts by the numbers of experimental units targets the overall average effect, provided the within-block allocations and estimators are appropriate. With equally sized blocks, the simple average is the natural choice.

Blocking is not a way to manufacture more data. It is a way to use a known, pre-treatment source of variation so that the random comparison focuses more sharply on the treatment. Pairing before randomization is an especially simple kind of blocking: match similar units, then randomly treat one unit from each pair.

## Randomization is not a magic eraser

Randomization protects against systematic selection into treatment, but it does not guarantee perfect compliance, prevent missing measurements, or remove interference between units. Imagine that treated chambers become warmer and heat neighboring controls. The treatment of one chamber has changed another chamber's potential outcome. The elementary independent-unit interpretation now fails, even though the original assignment was random.

Or imagine that chambers with weak growth are more likely to have their final measurements discarded. If that dropout differs by treatment, comparing only the observed chambers may reintroduce bias. The original randomization cannot force selectively missing data to be harmless.

We also need to distinguish treatment assignment from treatment received. If some chambers assigned to the new procedure did not actually receive it, comparing groups by their original assignment estimates an intention-to-treat effect: what changes when the laboratory adopts the assignment policy. Comparing only chambers that complied is a different question and can be confounded by the reasons for compliance.

A practical analysis plan records the intended outcome, the treatment and control definitions, the unit of randomization, the assignment method, how blocks will be combined, and what to do about missing observations. This does not prohibit exploration. It separates questions specified before seeing outcomes from interesting patterns discovered afterward.

## Choosing between designs

A completely randomized experiment is straightforward when experimental units are comparable. A blocked design is attractive when a few pre-treatment characteristics predict much of the outcome. A paired design is useful when units naturally come in matched pairs or when the same object can genuinely be measured under both conditions without carryover. A cluster-randomized design is sometimes necessary when a treatment is delivered to an entire classroom, village, chamber, or clinic, but the effective number of independent assignments is then the number of randomized clusters, not the number of observations inside them.

The design should be chosen according to the scientific question and the practical mechanism of treatment, not simply the statistical formula we hope to apply later. There may be several valid estimands: the effect for the experimental units, the effect of offering treatment, or an effect for a target population with a different mix of unit types. They require different arguments.

Return to the crystal laboratory. An observed two-millimeter difference is a measurement. A randomized, properly analyzed two-millimeter difference is evidence about a treatment contrast. A causal claim about the new procedure also requires an intervention that was applied as intended and an outcome that was measured fairly. A claim about future factories requires yet another step, because the factories may differ from the experimental chambers.

Good experiments do not eliminate uncertainty. They decide which uncertainty will remain after the data arrive. That is why designing the comparison is already part of doing the mathematics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — potential outcomes, assignment and blocking

### Finite-population treatment effect

For fixed units \(i=1,\ldots,N\), let \(Y_i(1)\) and \(Y_i(0)\) be the two potential outcomes. Under consistency and no interference,
\[
\tau_N=\frac1N\sum_{i=1}^N\{Y_i(1)-Y_i(0)\}.
\]
In a completely randomized design with exactly \(n_1\) treated and \(n_0=N-n_1\) controls, define \(Z_i\in\{0,1\}\), \(\sum Z_i=n_1\), and observed \(Y_i=Z_iY_i(1)+(1-Z_i)Y_i(0)\). Then
\[
\widehat\tau=\frac1{n_1}\sum_i Z_iY_i-\frac1{n_0}\sum_i(1-Z_i)Y_i.
\]
Since \(E_Z[Z_i]=n_1/N\), linearity of expectation proves \(E_Z[\widehat\tau]=\tau_N\). This is an expectation over assignment, not a statement that each assignment is exactly balanced.

For finite-population variances \(S_1^2,S_0^2\), and the variance of individual effects \(S_\tau^2\), the Neyman randomization variance is
\[
\mathrm{Var}_Z(\widehat\tau)=\frac{S_1^2}{n_1}+\frac{S_0^2}{n_0}-\frac{S_\tau^2}{N}.
\]
The last term generally cannot be identified from one realized experiment because both potential outcomes are never observed for the same unit.

### Four-unit enumeration

Take \(Y(0)=(1,2,3,4)\) and \(Y(1)=(3,4,5,6)\). With two treated units there are \({4\choose2}=6\) equally likely assignments. The contrasts can be enumerated explicitly:

| Treated indices | Treated mean | Control mean | Difference |
|---|---:|---:|---:|
| (1,2) | 3.5 | 3.5 | 0 |
| (1,3) | 4 | 3 | 1 |
| (1,4) | 4.5 | 2.5 | 2 |
| (2,3) | 4.5 | 2.5 | 2 |
| (2,4) | 5 | 2 | 3 |
| (3,4) | 5.5 | 1.5 | 4 |

Average \((0+1+2+2+3+4)/6=2\). The explicit table supersedes the unordered illustrative list above.

### Blocks and weighting

For block \(b\) containing \(N_b\) units, estimate its within-block effect \(\widehat\tau_b\). Under independent within-block random assignment and a fixed partition into blocks,
\[
\widehat\tau_{\mathrm{strat}}=\sum_b\frac{N_b}{N}\widehat\tau_b,
\qquad E[\widehat\tau_{\mathrm{strat}}]=\tau_N.
\]
Block-specific precision depends on block sizes and treated/control allocations, and blocking does not always reduce variance for every possible outcome configuration.

### Exercises with worked answers

1. **Experimental unit.** Ten chambers are independently randomized. Each yields eight crystals. What is the number of independently randomized units? **Answer:** ten; the eighty measurements are nested observations.
2. **Unbiasedness.** The six contrasts in the table above average to what value? **Answer:** two, equal to the fixed average of the individual treatment effects.
3. **Blocking.** In equally sized blocks A and B, within-block contrasts are three and one. Estimate the average treatment effect. **Answer:** two; for unequal block sizes use block-size weights.
4. **Generalization.** Does assigning treatment at random also make a convenience sample representative of all laboratories? **Answer:** no; assignment and sampling answer different questions.
5. **Interference.** What breaks if treated chambers warm neighboring controls? **Answer:** the elementary potential-outcome notation \(Y_i(z_i)\) is inadequate because unit \(i\)'s response can depend on other units' assignments.

### Reading and attribution

- Penn State STAT 503, *Design of Experiments*, https://online.stat.psu.edu/statprogram/stat503.
- Penn State STAT 503, Lesson 4, *Blocking*, https://online.stat.psu.edu/stat503/Lesson04.
- National Institute of Standards and Technology, *Engineering Statistics Handbook*, https://www.itl.nist.gov/div898/handbook/.
