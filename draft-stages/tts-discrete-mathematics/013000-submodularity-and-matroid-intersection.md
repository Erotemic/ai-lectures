# 013000 — Submodularity, Matroid Intersection, and the Limits of Greedy Choice

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph matchings, matroid independence and rank, greedy proofs. **Central question:** when does adding an element become less valuable, and why can satisfying two independent systems break a greedy algorithm?

<!-- BEGIN SPOKEN LECTURE -->

# Submodularity, Matroid Intersection, and the Limits of Greedy Choice

We have already met a striking combinatorial fact: if a collection of feasible sets forms a matroid, choosing available elements in decreasing weight order produces a maximum-weight independent set. That theorem is about a very particular kind of structure. Today we meet a wider language for diminishing returns, and an important problem where two individually simple structures interact in a way that defeats ordinary greedy choice.

The two ideas are submodular functions and matroid intersection. Both connect counting and graph theory to optimization. They also illustrate why mathematical guarantees depend on the exact structure being assumed.

## Diminishing returns as an inequality

Imagine choosing locations for sensors. Each sensor observes a set of regions, and our objective is to maximize the number of regions covered. The first sensor may cover ten new regions. Later, after other sensors have already been installed, the same sensor may contribute only two new regions. Its value has decreased because some of its coverage overlaps what we already have.

Write f of S for the number of distinct regions covered by sensors in S. If A is a subset of B and sensor e is not in B, the new coverage obtained from adding e to A is at least the new coverage obtained from adding e to B. The larger collection has already covered everything A covered, and possibly more. This is the diminishing-returns property of a submodular set function.

There is an equivalent inequality for finite sets: f of A plus f of B is at least f of their union plus f of their intersection. It looks reminiscent of inclusion and exclusion, except that it is an inequality rather than necessarily an equality. For the function that counts the elements of S itself, equality holds. Such functions are called modular. Coverage functions usually have a strict inequality because overlapping observations lose value.

## Rank is submodular too

For a matroid, the rank of a set is the size of its largest independent subset. The rank function is nonnegative and monotone; adding elements cannot reduce the maximum independent-set size. It is also submodular.

Here is the intuition. A set of vectors may have dimension three. Add another vector and dimension rises by one only when that vector is outside the span already present. Once we have a larger span, fewer new vectors can add another dimension. Thus linear-algebra rank has diminishing returns. The matroid rank axioms abstract precisely this behavior beyond vector spaces.

For a graphical matroid, rank measures how many edges of a chosen set can be retained without cycles. Adding an edge that connects components can increase rank, but an edge whose endpoints are already connected contributes nothing. As more edges accumulate, connections become redundant. Again, marginal gains cannot increase.

## Greedy maximization: exact and approximate are different

Suppose f is normalized so the empty set has value zero, nonnegative, monotone, and submodular. We may choose at most k elements. A natural algorithm adds, at each step, the available element with the largest marginal gain.

Does it always find the optimum? No. Overlapping coverage can make an early attractive choice prevent a better combination of later choices. But the diminishing-returns inequality gives a strong guarantee: after k greedy choices, the value is at least one minus one divided by e times the optimal value, for positive integer k. The constant is about sixty-three percent.

The proof is worth hearing. Suppose the current greedy set is S, with value f of S, and an optimal set O uses at most k items. By monotonicity, the union of S and O has value at least the optimum. By submodularity, the total marginal contribution of all items of O, measured from S, is at least the gap from f of S to the optimum. Since O has at most k items, at least one of its available items has marginal gain at least that gap divided by k. Greedy chooses an item with at least as much gain. Therefore each step shrinks the remaining gap by a factor of at most one minus one over k. After k steps, the surviving gap is at most the k-th power of that factor, which is at most one over e.

Notice the hypotheses. The proof needs monotonicity and the cardinality constraint. Under a matroid constraint, the plain greedy rule for a general monotone submodular objective typically has a weaker one-half guarantee; stronger algorithms use additional ideas. The exact greedy theorem for linear weights on a matroid is a different result.

## Intersecting two matroids

Now imagine we have two matroids on the same ground set E. We want a set independent in both. An immediate application is a bipartite matching. Treat each graph edge as an element. The first matroid allows at most one chosen edge at every left-side vertex. The second matroid allows at most one at every right-side vertex. Each constraint system is a partition matroid, and a set independent in both is exactly a matching.

But the common independent sets need not themselves form a matroid. Greedy choice can fail. Picture two left vertices, a and b, and two right vertices, one and two. There are three available edges: a to one has weight three, a to two has weight two, and b to one has weight two. Greedy takes the edge of weight three first. Now both remaining edges conflict with it, leaving total weight three. But taking the two edges of weight two forms a matching of total weight four.

There is no contradiction with the matroid greedy theorem. Each individual matroid behaves well; their intersection need not satisfy the exchange axiom needed for a single greedy solution.

## An exact min-max theorem

Despite greedy failure, there is a beautiful structural formula for the *maximum cardinality* common independent set. Let r one and r two be the rank functions of our two matroids. The largest size of a set independent in both equals the minimum, over all subsets A of the ground set, of r one of A plus r two of the complement of A.

One direction is easy. Take any common independent set I and any A. Split I into the elements inside A and those outside. The first part has size at most the first matroid's rank on A. The second part has size at most the second matroid's rank on the complement. Thus the size of I is bounded above by that sum, for every A.

The reverse direction is the substance of the matroid intersection theorem, developed by Jack Edmonds. It can be proved through exchange paths and an augmenting argument that generalizes matching algorithms. The theorem is not merely a numerical identity; its proof leads to efficient algorithms given suitable independence oracles. Weighted versions require additional machinery.

## Why these ideas belong together

Submodularity measures a diminishing-return structure. A matroid rank function is a specially constrained submodular function. Matroid intersection then explains what happens when two distinct independence systems must be satisfied simultaneously: the attractive one-pass greedy algorithm may fail, but a deeper min-max structure survives.

This is a recurring pattern in combinatorics. The algorithmic technique has to match the precise theorem being used. Greedy is exact for additive weights on one matroid, approximate for monotone submodular coverage under a cardinality limit, and generally insufficient for the intersection of two matroids. Recognizing the distinction is as important as recognizing the shared family resemblance.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(f:2^E\to\mathbb R\), submodularity means
\[f(A)+f(B)\ge f(A\cup B)+f(A\cap B).\]
For finite \(E\), equivalently, whenever \(A\subseteq B\subseteq E\), \(e\notin B\):
\[f(A\cup\{e\})-f(A)\ge f(B\cup\{e\})-f(B).\]
A coverage function \(f(S)=|\bigcup_{i\in S}C_i|\) is normalized, monotone, and submodular. A matroid rank function satisfies \(r(\varnothing)=0\), monotonicity, integrality, \(r(S)\le |S|\), and submodularity.

**Cardinality-constrained greedy bound:** for normalized nonnegative monotone submodular \(f\), and optimal \(O\) with \(|O|\le k\), the greedy iterates \(S_i\) satisfy
\[f(O)-f(S_{i+1})\le (1-1/k)(f(O)-f(S_i)),\]
so \(f(S_k)\ge[1-(1-1/k)^k]f(O)\ge(1-1/e)f(O)\). The guarantee is specific to monotone submodular maximization with a cardinality bound, not arbitrary matroid intersection.

**Matroid intersection (Edmonds):** for \(\mathcal M_j=(E,\mathcal I_j)\) with rank \(r_j\),
\[\max_{I\in\mathcal I_1\cap\mathcal I_2}|I|=\min_{A\subseteq E}\bigl(r_1(A)+r_2(E\setminus A)\bigr).\]
The \(\le\) direction follows by splitting \(I\) at \(A\); the nontrivial reverse direction uses augmentations / exchange graphs. Common independent sets of two matroids are not necessarily a matroid. A bipartite matching is the intersection of left-degree and right-degree partition matroids.

**Greedy counterexample:** left vertices \(a,b\), right \(1,2\), edges \(a1\) weight \(3\), \(a2\) weight \(2\), \(b1\) weight \(2\). Choosing \(a1\) first yields value \(3\), while matching \(\{a2,b1\}\) yields \(4\).

### Exercises with answers

1. Give a modular function on \(2^E\). **Answer:** \(f(S)=\sum_{e\in S}w_e\), with equality in the submodular inequality.
2. Is the rank of a set of linearly independent vectors necessarily its cardinality? **Yes** for an independent set; for a dependent set it is smaller.
3. Why does matroid intersection not inherit the one-matroid weighted greedy theorem? **Answer:** the common feasible sets may violate the augmentation axiom; the three-edge matching example proves failure.
4. State an easily computed upper bound on common independent-set cardinality. **Answer:** for any \(A\subseteq E\), \(r_1(A)+r_2(E\setminus A)\); minimizing makes the bound exact.

### Reading and source notes

- Matt Weinberg, [Princeton COS 521 lecture on Submodular Functions and the Lovász Extension](https://www.cs.princeton.edu/~hy2/teaching/fall22-cos521/notes/SFM.pdf).
- Jan Vondrák, [Stanford lecture 10: Matroid intersection](https://theory.stanford.edu/~jvondrak/CS369P/lec10.pdf), including Edmonds' min-max formula.
- James G. Oxley, [*Matroid Theory*, 2nd edition](https://repository.lsu.edu/facultybooks/466/), rank axioms and structural background.
