# 038000 - Sharp Thresholds, Influences, and the Tribes Function

**Track:** Discrete Mathematics. **Background:** monotone Boolean functions, product measures, derivatives of expectations, and Fourier influences. **Central question:** when does the probability of a property change abruptly as its input density changes?

<!-- BEGIN SPOKEN LECTURE -->

# A probability curve can turn into a cliff

Imagine a random graph that gradually receives more edges. At very low density it is almost certainly disconnected. At high density it is almost certainly connected. Somewhere in between, the probability of connectivity rises from near zero to near one. How narrow is that transition window?

The same question arises for reliability of networks, satisfiability of random formulas, and monotone Boolean functions whose inputs are independent biased bits. Such transitions are called thresholds. A sharp threshold means the passage from unlikely to likely occurs in a narrow region, once the appropriate scale is specified. A coarse threshold means a larger relative change in the parameter is needed.

We need care with language. For a threshold near zero, an interval whose absolute width tends to zero need not be sharp relative to the threshold location. The property that at least one of n bits is one has a transition near density one over n, but its relative transition window remains of constant order. Different threshold theorems formalize sharpness in different parameter regimes.

# The derivative is a count of pivotal coordinates

Consider a monotone Boolean function. A coordinate is pivotal for a given choice of the other coordinates when changing that coordinate changes the output from false to true. Its influence under a biased product measure is the probability that it is pivotal.

Russo's formula states that the derivative of the probability of a monotone event with respect to the input density equals the sum of these pivotal probabilities. The derivative is therefore not an unrelated analytic quantity. It measures how much influence the input coordinates collectively have over the event.

This identity gives a strategy for proving sharp transitions. Show that when the event's probability is bounded away from zero and one, its total influence must be large. Then the probability curve must have a large slope and cannot remain in the middle range for long.

But the strategy needs structural assumptions. A property depending only on one selected coordinate always has probability equal to the density. Its derivative is one, no matter how many irrelevant coordinates we add. There is no increasing collective influence. The function simply ignores most of its input.

# Symmetry limits the possibility of a dictator

One way to rule out a single dominant coordinate is symmetry. If a transitive group of coordinate permutations preserves a Boolean property, no coordinate is intrinsically distinguished. Influence inequalities then imply lower bounds on total influence in nontrivial probability regimes.

For monotone transitive properties under a product measure away from the extreme endpoints, these bounds can force transition windows to shrink as the number of coordinates grows. More general sharp-threshold theorems relate coarse thresholds to approximate dependence on only a few coordinates, called juntas.

This does not say every function with many inputs has a sharp threshold. The function may genuinely depend on only one of them. Nor does it automatically apply uniformly when the density goes to zero at a rate that changes the natural scale. The location and normalization of the threshold are part of the statement.

# Build the tribes function

A particularly illuminating example divides n input bits into disjoint groups, or tribes, each containing m bits. The function is true if at least one tribe consists entirely of ones. It is an OR of ANDs, and it is monotone.

Suppose there are k tribes. A given tribe is all ones with probability two to the negative m when the input bits are unbiased. The events for distinct tribes are independent, so the probability that no tribe is complete is one minus two to the negative m, raised to the kth power. Therefore the probability of the function being true is one minus that expression.

Choose k proportional to two to the m, with the constant chosen so the event probability is near one-half. Then the function is balanced: it is neither almost always true nor almost always false. Yet each individual bit has only a small influence, because changing it matters only when every other bit in its tribe is one and no other tribe is already complete.

The influence of a specific bit is two to the power minus m plus one, multiplied by the probability that the other tribes are incomplete. There are k times m bits, so multiplying by the total number of bits gives total influence on the order of m. Since n is about m times two to the m, m is on the order of log n.

This produces a balanced monotone function whose derivative with respect to the input density grows logarithmically with n, even though no individual bit has large influence. The threshold becomes sharper as the system expands.

# Tribes demonstrate a collective effect

The tribes example illustrates why influence is the right bridge between local decisions and global thresholds. Each coordinate is rarely pivotal, but there are many coordinates. Their contributions add to a large total derivative.

The calculation also shows that small individual influence does not imply stability of the event under changes in density. An individual bit barely matters, yet a modest coordinated increase in the bias can transform the event's overall probability.

This is different from asking how the function reacts to random noise that flips a small number of bits. Noise sensitivity depends on its Fourier spectrum and on the noise model. Threshold sharpness depends on changing the bias of the input distribution. The two subjects are related through influences and Fourier analysis, but they are not interchangeable definitions.

# The significance of the junta theorem

Friedgut's junta theorem gives another side of the story. Roughly, a Boolean function with bounded total influence can be approximated in probability by a function depending on relatively few coordinates, with the number of required coordinates controlled by influence and the desired approximation accuracy.

A function with low total influence therefore has a low-dimensional explanation at the chosen measure, even if its formal input list is enormous. This helps interpret coarse threshold behavior: failure of a sufficiently sharp transition may signal that a small amount of local information has disproportionate power.

Quantitative versions depend on the bias, approximation error, and influence definitions. One should not repeat an unbiased-cube junta bound unchanged at densities collapsing toward zero or one. The technical dependence is exactly what distinguishes a useful threshold theorem from a slogan.

# Apply the framework to a network

For a random graph, each possible edge is a Boolean input and the event of connectivity is monotone. Adding an edge cannot destroy connectivity. The coordinates are symmetric under relabeling of vertices, so influence inequalities are natural tools for understanding its transition.

A full proof of the graph-connectivity threshold uses additional combinatorics. In the classical independent-edge model, isolated vertices play a decisive role near the connectivity threshold. The threshold scale is roughly log n divided by n, not simply one over n. Understanding the precise limiting probability requires counting the relevant small obstructions and showing others become negligible.

The Boolean-influence viewpoint supplies a structural explanation for why a collective transition is possible, while the graph argument identifies the location and the dominant obstruction. Sharpness and threshold location are different questions, and a serious analysis addresses both.

# A reliable checklist

When someone claims a sharp threshold, ask four things. What parameter is changing? Which probability level defines the threshold location? Is width measured absolutely or relative to that location? And what symmetry or influence theorem makes a narrow window unavoidable?

Russo's identity answers how the probability changes. The tribes function demonstrates a balanced event with logarithmically growing total influence. Junta theory explains why low influence points toward dependence on a few coordinates. Together they turn the idea of a sudden transition into a quantitative study of who can change an event and how many such pivotal opportunities exist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `f:{0,1}^n -> {0,1}` be monotone and `mu_p` the independent Bernoulli-p measure. With `Inf_i^p(f)` defined as the `mu_p` probability over other coordinates that flipping bit `i` changes `f`, Russo's formula gives
\[
\frac{d}{dp}\mathbb E_p[f]=\sum_{i=1}^n \mathrm{Inf}_i^p(f).
\]
For tribes with `n=km`, `f=OR_{j=1}^k AND_{i in tribe j} x_i`,
\[
\mathbb P_p(f=1)=1-(1-p^m)^k,
\quad \mathrm{Inf}_i^p(f)=p^{m-1}(1-p^m)^{k-1}.
\]
At `p=1/2`, choose `k ~ (ln 2)2^m`; the event is balanced and total influence `km 2^{-(m-1)}(1-2^{-m})^{k-1}=Theta(m)=Theta(log n)`. This statement is asymptotic for large m and integer choices of k. For `OR_n` the critical density is `Theta(1/n)` and the relative window does not shrink; an absolutely small window alone is not the standard notion of sharpness near a vanishing threshold.

### Exercises with answers

1. What is the derivative of `P_p(OR_n=1)`? **Answer:** `n(1-p)^{n-1}`.
2. What makes a coordinate pivotal for a monotone function? **Answer:** setting that coordinate from zero to one changes the output, holding the others fixed.
3. Why can a function of one coordinate have a coarse threshold? **Answer:** its probability is exactly p and total influence is one.
4. For tribes, why does any one coordinate have small influence? **Answer:** all other bits in its tribe must be one and every other tribe incomplete.

### Reading and source notes

- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/boolean-analysis/), Russo's lemma, influence bounds, juntas, and tribes.
- [Friedgut, Boolean Functions with Low Average Sensitivity Depend on Few Coordinates](https://doi.org/10.1007/PL00009809), the junta theorem and structural meaning of low influence.
