# 031000 — Property Testing: Deciding Without Reading Everything

**Track:** Discrete Mathematics. **Background:** probability, graphs, finite fields, randomized algorithms. **Central question:** when can a few queries distinguish a property from objects far away from having it?

<!-- BEGIN SPOKEN LECTURE -->

# What could a hundred questions reveal about a billion entries?

Suppose someone hands you a truth table with more entries than you could inspect in a lifetime. They claim the table represents a linear function. You can check a few random values, but how could a hundred checks say anything about billions of unseen entries?

There is an essential change of goal. Property testing does not usually promise to decide whether the data differs from the desired property in even one place. It promises to accept objects that have the property and reject objects that are far from it. There may be a middle region where either answer is permitted. Once we allow that gap, local tests can detect global structure with surprisingly few queries.

This difference between exact decision and approximate property testing is central. An adversary can hide a single incorrect entry anywhere in a huge table. No tester using a fixed number of queries can guarantee finding it. But if one quarter of the entries must be changed to make the table linear, random local consistency checks have a chance to expose that widespread defect.

# A three-query test for linearity

Consider functions from n-bit vectors to one bit, where addition is performed modulo two. A linear function must satisfy the rule that the value at x plus y equals the sum of the values at x and y, again modulo two.

The Blum–Luby–Rubinfeld test samples two independent uniform inputs x and y, queries the function at x, y, and their sum, and checks that equation. Every truly linear function passes every time. More remarkably, if the function is far from every linear function, a nontrivial fraction of random pairs expose a violation.

To hear a complete miniature example, take the parity function and flip every output bit. The result is an affine function, parity plus one, but it is not linear because its value at zero is one. Evaluate the test equation: the two flipped terms on the left cancel their extra ones, but the single flipped term on the right retains one. Every test rejects. This is why a linearity tester is testing homomorphisms, not arbitrary affine maps.

Now imagine that the function equals parity except on a small random set of inputs. Most checks still pass, and the rejection rate reflects the amount of corruption. We repeat the experiment and estimate its rejection probability. The BLR soundness theorem connects that probability to distance from the closest linear function.

# Why the theorem is deeper than random inspection

A failed equation proves only that one local triple is inconsistent. The difficult direction is showing that if almost every triple is consistent, there exists one global linear function close to the original table. The proof builds that global candidate from the overwhelmingly consistent local behavior, often using majority correction or Fourier analysis on the Boolean cube.

This is a local-to-global principle. We are not accumulating enough samples to recover an entire truth table. We are exploiting an algebraic constraint that couples different entries. The structure of linearity is what makes the tester powerful.

The query count depends on the tolerated distance and the target error probability, not on the number of entries in the truth table. The work needed to generate a random n-bit query still depends on n, so it would be misleading to say that every aspect of running time is independent of input size. The important sublinear guarantee concerns oracle probes.

# Distance depends on how data is presented

For a Boolean function, distance is the fraction of inputs on which two functions disagree. For a dense graph stored as an adjacency matrix, distance commonly means a fraction of the possible edges that would have to be added or removed. For a bounded-degree graph accessed through adjacency lists, distance is scaled by the maximum degree times the number of vertices. These are different models, with different queries and different notions of being far.

A graph could look easy to test in one model and hard in another. Consider testing whether a dense graph is triangle-free. If the graph is far from triangle-free, the triangle-removal lemma implies that there are many triangles, in a quantitative sense depending on the distance parameter. Sample random triples of vertices, check their three adjacency relations, and a tester can eventually find one with probability bounded away from zero.

The quantitative bound obtained from the triangle-removal lemma can be enormous. Constant query complexity as a function of graph size does not mean a small or practical constant as a function of the required accuracy. That subtlety matters when turning a theorem into an algorithm.

# A graph oracle changes the questions we can ask

In the bounded-degree model, we can query a vertex and an index to retrieve a neighboring vertex. We cannot instantly ask whether an arbitrary pair is connected unless the oracle supports such a question. A local algorithm may explore a neighborhood by breadth-first search and decide whether it finds a forbidden configuration.

For some graph properties, testers can use a number of neighbor queries depending mainly on the degree bound and the distance parameter. Others provably require dependence on the number of vertices. We should not transfer a query-complexity claim from dense adjacency matrices to bounded-degree access without checking its assumptions.

Property testing also differs from local computation. A tester returns a yes-or-no answer about approximate membership. A local computation algorithm answers a query about one part of a hypothetical global solution, while ensuring consistency between answers to different queries. For example, one might want to know the color of a queried vertex in a proper coloring without constructing and storing the whole coloring. This consistency requirement can be much more demanding than merely detecting an error.

# The tradeoff between promises and conclusions

There are two more distinctions worth making. A tolerant tester must distinguish objects very close to the property from objects substantially farther away, rather than accepting only exact members. A distribution-free tester must be accurate when input points are drawn from an unknown distribution, not necessarily the uniform distribution built into the BLR model. Both strengthen the problem and can increase its complexity.

We should also separate one-sided error from two-sided error. The BLR test never rejects a genuinely linear function, so it has one-sided error. A more general tester might have some probability of rejecting a correct object, but it must meet a specified acceptance guarantee.

The real achievement of property testing is not magic access to unseen data. It is the discovery that some global structures have local consistency witnesses, and that widespread violations force many such witnesses. Three queries can be enough to expose a distant failure of linearity because addition binds the entire truth table together. When that kind of coupling is absent, no comparable guarantee should be expected.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `f:F_2^n -> F_2`, define relative Hamming distance to linearity by
\[
\operatorname{dist}(f,\mathrm{Lin})=\min_{\ell\text{ linear}}\Pr_{x\sim U}[f(x)\ne\ell(x)].
\]
The BLR tester draws independent uniform x,y and accepts iff `f(x)+f(y)=f(x+y)` in F2. It has perfect completeness. Its soundness theorem shows rejection probability bounded below by a positive function of `dist(f,Lin)` (indeed a linear lower bound in standard formulations); sampling `O(1/epsilon)` independent pairs suffices for constant rejection probability if f is epsilon-far, up to the particular soundness constant. All oracle query statements use the uniform-table access model.

For `f(x)=<a,x>+1`, `f(x)+f(y)=<a,x+y>` while `f(x+y)=<a,x+y>+1`: rejection probability is one. A graph in the dense model is epsilon-far from triangle-free if at least `epsilon n^2` adjacency changes (up to normalization conventions) are needed; the triangle removal lemma ensures `delta(epsilon)n^3` triangles and therefore a tester based on O(`1/delta(epsilon)`) sampled vertex triples. This theorem's quantitative dependence on epsilon can be huge, and a bounded-degree adjacency-list oracle is a different model.

### Exercises with answers

1. Why can a constant-query tester not always detect a single wrong table entry? **Answer:** an adversary can place that entry outside the queried positions; property testing has a far-from-property rejection promise, not exact error detection.
2. Does an affine function with constant term one satisfy the BLR equality? **Answer:** no; it violates every pair check.
3. Must triangle-testing guarantees transfer unchanged from dense to sparse graph models? **Answer:** no; the query oracles and distance normalization differ.
4. Does a property tester reconstruct the whole nearest linear function? **Answer:** no; testing and correction/reconstruction are distinct tasks.

### Reading and source notes

- [Oded Goldreich, Introduction to Property Testing](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html), models, algorithms and limitations.
- [Goldreich, property-testing lecture notes](https://www.wisdom.weizmann.ac.il/~oded/pt-ln.html), BLR and graph testing examples.
- [Blum, Luby and Rubinfeld, Self-Testing/Correcting with Applications to Numerical Problems](https://doi.org/10.1145/100216.100225), original local linearity testing work.
