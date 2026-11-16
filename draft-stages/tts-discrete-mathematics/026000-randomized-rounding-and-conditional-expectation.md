# 026000 — Randomized Rounding: From Fractional Answers to Reliable Discrete Choices

**Track:** Discrete Mathematics. **Background:** linear programming, probability, conditional expectation, combinatorial optimization. **Central question:** how can a probability argument be turned into an explicit discrete solution?

<!-- BEGIN SPOKEN LECTURE -->

# A fractional answer is not yet a decision

Imagine a network design problem in which each edge must either be installed or omitted. A linear programming relaxation may assign a value of one half to an edge. That fractional result can be useful: it may give a lower bound on the best possible cost, or an upper bound for maximization. But we still need a genuine yes-or-no decision.

One strategy is randomized rounding. Interpret each fractional value as a probability, draw a random discrete solution, and analyze its expected quality. The expectation may show that some good discrete solution exists. But several questions remain. Does the random draw obey the constraints? Does it produce a sufficiently good objective value with useful probability? And can we remove the randomness while keeping the guarantee?

We will begin with a case where the analysis is exact: maximum cut in a graph.

## Cutting a graph with coin flips

A cut divides a graph's vertices into two groups. An edge contributes to the cut when its endpoints lie on different sides. Suppose every edge has a nonnegative weight, and we want the total weight of crossing edges to be large.

Place each vertex independently on the left or right with equal probability. For any particular edge, there are four equally likely assignments of its endpoints, and exactly two cross the cut. So each edge crosses with probability one half. By linearity of expectation, the expected cut weight is one half the total weight of all edges.

This proves that a cut of at least half the total edge weight exists. No search was needed to prove existence. The expectation cannot be greater than every outcome, so at least one realization meets or exceeds it.

But a random construction may be inconvenient. We might want the same result every time, or need to produce a certificate for a pipeline. The method of conditional expectation turns this random argument into a deterministic algorithm.

## Choosing bits without losing the expectation

Order the vertices. Before assigning any, calculate the expected cut weight under uniform random choices. Now choose the first vertex's side. There are two conditional expectations: one if we place it left, one if we place it right. The average of these two values equals the current expectation, so at least one choice does not decrease it. Fix that choice and move to the next vertex.

Repeat until no randomness remains. At every step, the conditional expectation never decreases. When the last vertex is placed, the expectation is simply the weight of the actual cut. Thus the final cut weighs at least half the total edge weight.

For a path of three vertices with two unit-weight edges, the initial expectation is one. Put the first vertex on the left. We may then put the second vertex on the right, guaranteeing that the first edge crosses. Choose the third vertex on the left, and the second edge crosses as well. The resulting cut has weight two. The guarantee said at least one; in this small example the conditional choices can do better.

The key computational question is whether the conditional expectations can be evaluated efficiently. For maximum cut they can. An edge with both endpoints assigned is either certainly cut or certainly not. An edge with one or both endpoints still random contributes its weight times one half. Adding these contributions is straightforward.

## When independence breaks feasibility

Return to fractional optimization. Suppose the relaxation has two variables, each equal to one half, and imposes the requirement that exactly one object be selected. If we round the two variables independently, there is a one-quarter chance that we select both, and another one-quarter chance that we select neither. The expected number selected is one, but the constraint is violated in half the outcomes.

This is a common error: preserving a constraint in expectation is not the same as satisfying it for every sample. Randomized rounding is not a complete algorithm until feasibility is controlled.

Sometimes a concentration inequality shows that violations are small and can be repaired. Sometimes we need dependent rounding, which coordinates the choices so a sum or matroid constraint remains intact. In other cases the relaxation itself must be strengthened.

One elegant technique is pipage rounding for certain submodular objectives. Instead of changing one variable independently, increase one fractional coordinate while decreasing another, preserving their sum. Move along this line until at least one coordinate becomes integral. For the multilinear extension of a submodular set function, the objective has a useful convexity property along these swap directions. Choosing the better endpoint never decreases the objective. Repeating the operation eventually produces an integral point in a suitable polytope.

This is why the form of a relaxation matters. A matroid base polytope has exchange directions adapted to such rounding. A random vector of independent coin flips does not respect those same structural constraints.

## Proof of existence, algorithm, certificate

There are three different achievements to keep separate. An expectation bound proves that some good outcome exists. A randomized algorithm samples an outcome and may require a probability-of-success argument. A derandomized algorithm constructs a good outcome by making choices that maintain a potential, such as a conditional expectation.

And a performance guarantee is not the same as proof of optimality. A cut weighing at least half the total edge weight may be far below the maximum cut. It is still a mathematically certified approximation, because its objective value meets a proven bound independent of which random outcome happened to occur.

Randomness is useful here not because we want to surrender control to chance, but because expectation can reveal structure that is hard to see in a direct search. Conditional expectation and dependent rounding then convert that structural information into concrete decisions while preserving the conditions the problem actually imposes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For weighted Max-Cut with nonnegative `w_e`, choose independent fair labels `X_v in {0,1}`. Each edge contributes `w_e 1_{X_u != X_v}`, whose expectation is `w_e/2`. Therefore `E[C]=W/2` where `W=sum_e w_e`, proving `OPT >= W/2`.

For the conditional expectation method, after assigning some vertices let `Phi` be the expected final objective over unassigned uniform labels. By the tower property, `Phi=(Phi_left+Phi_right)/2` for the next vertex, so choosing the larger term maintains `Phi`. When all assignments are fixed, `Phi=C`, a deterministic bound `C>=W/2`.

Independent rounding `X_1,X_2 ~ Bernoulli(1/2)` violates `X_1+X_2=1` with probability `1/2`. Expectation preservation is not almost-sure feasibility. For a submodular set function f with multilinear extension F, the mixed derivative `partial^2 F / partial x_i partial x_j <= 0` for `i != j`. Along `x+t(e_i-e_j)`, the second derivative is `-2 partial^2_ij F >=0`; thus the restriction is convex. One endpoint of a feasible swap segment has at least the current F value, permitting deterministic pipage steps where the polytope's exchange geometry supports them.

### Exercises with answers

1. A weighted graph has total edge weight 26. What does the uniform random-cut argument guarantee? **Answer:** a cut of weight at least 13.
2. Why can conditional expectation yield a deterministic cut? **Answer:** the average of the two conditioned expectations is the current one, so at least one choice preserves it.
3. For two independent Bernoulli halves, what is the probability exactly one is chosen? **Answer:** one half.
4. Why is pipage rounding not the same as independent rounding? **Answer:** it moves fractional coordinates together along feasible exchange directions, preserving constraints such as a fixed sum.

### Reading and source notes

- [Motwani and Raghavan, Randomized Algorithms](https://doi.org/10.1017/CBO9780511814075), method of conditional expectations and randomized rounding.
- [Chekuri, Vondrák, and Zenklusen, Dependent Randomized Rounding via Exchange Properties of Combinatorial Structures](https://arxiv.org/abs/0909.4348), exchange rounding and negative dependence.
- [Vondrák, Optimal Approximation for the Submodular Welfare Problem](https://doi.org/10.1145/1374376.1374381), multilinear extensions and rounding methods.
