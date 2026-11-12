# 025000 — The matching theorem

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** principal angles and principal planes; transporters and displacement; the Proposition 4.4 counterexample; real versus complex transports.

<!-- BEGIN SPOKEN LECTURE -->

The matching theorem

The counterexample to Proposition 4.4 shows that the direct rotation is not always the cheapest orthogonal map carrying one real subspace onto another, when cost is measured by the trace norm of the displacement. It does not say what the cheapest map is. The final theorem of the journal paper answers that question exactly, for every pair of equal-dimensional subspaces of a finite-dimensional real space. The answer is a formula, a minimum over matchings of the principal angles, and this lecture states it, explains each ingredient, and works through the paper's example. The proof occupies the next two lectures.

Here is what we will establish. Each positive principal angle theta i labels a principal plane, and there are two ways to transport a single plane on its own: rotate it through theta i, at trace-norm cost four sine of theta i over two, or reflect it across the bisector, at cost two. The cheaper of the two is the singleton cost s i. Two planes can also be transported together, in the four-dimensional space they span, by a map that fixes two directions and rotates the other two through theta i plus theta j, at cost e i j equal to four sine of half of theta i plus theta j. The matching theorem says: the minimum trace-norm displacement over all real orthogonal maps carrying K onto L equals the minimum, over all ways of pairing up some of the angle labels, of the sum of the pair costs for the chosen pairs plus the singleton costs of the unpaired labels. Both minima are attained. Finding the best pairing is a maximum-weight matching problem on a graph whose vertices are the angles.

The question

Let K and L be subspaces of real n-dimensional space with the same dimension. Consider all orthogonal n by n matrices W with W carrying K onto L. There is no requirement that W preserve principal planes, have determinant one, or act in any particular way off K. Among all such W, minimize the trace norm of the identity minus W, the sum of its singular values.

Since the set of orthogonal matrices is compact and the constraint is closed, a minimizer exists. The question is its value, in terms of the geometry of K and L. That geometry is entirely captured by the principal angles, so the answer must be a function of them.

Write theta one through theta m for the positive principal angles, counted with multiplicity, each between zero and ninety degrees inclusive. Zero angles correspond to common directions, which every good transporter can leave fixed at no cost, so they drop out.

Moving one principal plane

Each positive angle theta i comes with a principal plane, containing a unit source vector x i and a unit target vector y i at angle theta i. Treat the plane alone. Any orthogonal map of the plane carrying the line of x i onto the line of y i is either a rotation or a reflection.

The shortest rotation turns through theta i. Its displacement has two singular values, each two sine of theta i over two, for a trace norm of four sine of theta i over two. A rotation the long way costs more.

The reflection across the line bisecting x i and y i carries the source line onto the target line. It fixes the bisector and reverses the perpendicular direction, so its displacement has singular values zero and two, for a trace norm of two.

Which is cheaper? Four sine of theta over two is less than two exactly when sine of theta over two is less than one half, that is, when theta is less than sixty degrees. So for small angles the rotation is cheaper, and beyond sixty degrees the reflection is. The singleton cost s i is the minimum of four sine of theta i over two and two. At thirty degrees it is about one point zero four, at forty-five degrees about one point five three, and at seventy-five degrees it is two, from the reflection.

Moving two planes together

The counterexample showed that coupling two principal planes can be cheaper than moving them separately. For two labels i and j, the two principal planes span a four-dimensional space. In it, there is an orthogonal map that carries the two source directions onto the two target directions, fixes a two-dimensional subspace, and rotates the complementary plane through theta i plus theta j. Its displacement has singular values two sine of half of theta i plus theta j, twice, and zeros, for a trace norm of four sine of half of theta i plus theta j. That is the pair cost e i j.

When the two angles are equal, the pair cost is four sine theta, which is exactly the counterexample's competitor, and it equals the cost of the complex phase construction: twice the sum of the two sines. When the angles differ, the pair cost exceeds twice the sum of the sines, by the factor one over the cosine of half their difference. Pairing is most effective for nearly equal angles.

The theorem

A matching of the labels one through m is a set of disjoint pairs. Each label is used in at most one pair, and the labels not in any pair are unmatched. The empty matching, with every label unmatched, is allowed. The cost of a matching is the sum of the pair costs e i j over its pairs, plus the singleton costs s i over its unmatched labels.

The matching theorem: the minimum, over real orthogonal maps W carrying K onto L, of the trace norm of the identity minus W, equals the minimum over matchings of the matching cost. Both minima are attained. The statement includes repeated angles, right angles, and common directions, and places no determinant or principal-plane restriction on W.

One direction is easy. Given a matching, build a transporter block by block: for each matched pair, the four-dimensional pair map on the sum of the two principal planes; for each unmatched label, the cheaper of the rotation and the reflection on its principal plane; and the identity on common directions and on everything perpendicular to both subspaces. These blocks act on mutually perpendicular subspaces, so the trace norm of the total displacement is the sum of the blocks' trace norms, which is the matching cost. Every matching cost is therefore achieved by some transporter, and the minimum trace norm is at most the minimum matching cost.

The other direction is the hard part. It says that an optimal transporter can always be taken to have this block form, with blocks of dimension two and four only, so that no cleverer coupling of three or more planes ever helps. That is what the next two lectures prove.

Matching as maximum weight

The minimization over matchings is a classical combinatorial problem. Start from the all-singleton cost, the sum of all the s i. Pairing i with j changes the cost by e i j minus s i minus s j. So assign each pair the weight s i plus s j minus e i j, the saving from pairing. A matching's cost is the all-singleton cost minus the total weight of its pairs. Minimizing cost is maximizing total weight. Pairs with negative weight are never worth choosing.

This is the maximum-weight matching problem on the complete graph whose vertices are the angle labels. It is solvable in polynomial time, by the blossom methods that descend from Jack Edmonds's 1965 work on matchings in general graphs. The graph is not bipartite, since any label may pair with any other, which is why general matching rather than assignment is needed.

The paper's example

Take two three-dimensional subspaces of six-dimensional real space with trivial intersection and principal angles thirty, forty-five, and seventy-five degrees.

Singleton costs: four sine of fifteen degrees, about one point zero three five, for thirty degrees; four sine of twenty-two and a half degrees, about one point five three one, for forty-five; and two, by reflection, for seventy-five.

Pair costs: thirty with forty-five, four sine of thirty-seven and a half degrees, about two point four three five; thirty with seventy-five, four sine of fifty-two and a half degrees, about three point one seven three; forty-five with seventy-five, four sine of sixty degrees, about three point four six four.

There are four matchings. All singletons: one point zero three five plus one point five three one plus two, about four point five six six. Pair thirty and forty-five, leave seventy-five alone: two point four three five plus two, about four point four three five. Pair thirty and seventy-five: three point one seven three plus one point five three one, about four point seven zero four. Pair forty-five and seventy-five: three point four six four plus one point zero three five, about four point four nine nine.

The minimum is four point four three five: couple the thirty and forty-five degree planes in a four-dimensional block, and reflect the seventy-five degree plane. In weight form, the three edges have savings about zero point one three one, minus zero point one three eight, and zero point zero six seven, and the best matching takes the single edge with the largest saving.

Two comparisons put the answer in context. The direct rotation, rotating each plane separately, would cost the sum of four sine of half of each angle, about one point zero three five plus one point five three one plus two point four three five, which is about five point zero. And the complex lower bound, twice the sum of the sines, is about four point three four six, which the real optimum, four point four three five, does not reach, because the coupled angles are not equal.

For two equal angles of thirty degrees, by contrast, pairing costs four sine of thirty degrees, which is two, exactly the complex bound, while the direct rotation costs eight sine of fifteen degrees, about two point zero seven.

Where this sits

Davis and Kahan's complex phase example showed that a phase change can lower the full trace displacement. Bolotnikov, Li, and Rodman formulated the ambient minimal-distortion problem for unitary maps and proved Q-norm and Frobenius optimality results. The matching formula specifies the unrestricted real trace-norm minimum through singleton and paired angle costs; the authors of the journal paper did not locate this exact formula in the sources they compared. The real field permits pairing between distinct principal planes, and the complex field permits a phase within one plane, which is why the real answer is an optimization over matchings while the complex answer is simply twice the sum of the sines.

To summarize. For real subspaces K and L of equal dimension, with positive principal angles theta one through theta m, the minimum trace-norm displacement of a real orthogonal map carrying K onto L equals the minimum over matchings of the labels of the sum of pair costs four sine of half of theta i plus theta j, over matched pairs, and singleton costs, the minimum of four sine of theta i over two and two, over unmatched labels. Every matching is realized by a block transporter, which gives the inequality in one direction. Choosing the matching is a maximum-weight matching problem with weights equal to the savings from pairing. In the paper's example with angles thirty, forty-five, and seventy-five degrees, the optimum pairs the first two and reflects the third, for a cost of about four point four three five.

The difficult claim is that nothing better than blocks of two and four dimensions exists. Proving it requires analyzing an optimal transporter directly, which is the work of the remaining two lectures.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Theorem (journal paper, §6)

\(K,L\subseteq\mathbb R^n\), \(\dim K=\dim L\), positive principal angles \(\theta_1,\dots,\theta_m\in(0,\pi/2]\):
\[
\min_{\substack{W\in O(n)\\W(K)=L}}\|I-W\|_1=\min_{M}\Bigl(\sum_{\{i,j\}\in M}e_{ij}+\sum_{i\ \text{unmatched}}s_i\Bigr),\quad
e_{ij}=4\sin\tfrac{\theta_i+\theta_j}2,\quad s_i=\min\{4\sin\tfrac{\theta_i}2,2\}.
\]
Both minima attained. Weight form: \(w_{ij}=s_i+s_j-e_{ij}\), cost \(=\sum_is_i-\sum_{\{i,j\}\in M}w_{ij}\).
\(e_{ij}=2(\sin\theta_i+\sin\theta_j)/\cos\tfrac{\theta_i-\theta_j}2\ge2(\sin\theta_i+\sin\theta_j)\).

### Example (journal paper, Figure 3)

| | cost |
|---|---|
| \(s\): \(30^\circ,45^\circ,75^\circ\) | \(1.0353,\ 1.5307,\ 2\) |
| \(e_{12},e_{13},e_{23}\) | \(2.4350,\ 3.1734,\ 3.4641\) |
| \(w_{12},w_{13},w_{23}\) | \(0.1310,\ -0.1381,\ 0.0666\) |
| \(\varnothing,\{12\},\{13\},\{23\}\) | \(4.5660,\ \mathbf{4.4350},\ 4.7041,\ 4.4994\) |

Direct rotation \(\approx5.001\); complex bound \(2\sum\sin\theta_i\approx4.346\). Equal \(30^\circ\) pair: \(4\sin30^\circ=2\) vs \(8\sin15^\circ\approx2.071\).

### Lean correspondence

`DavisKahan/FiniteDimensional/DirectRotation/RealNuclearMatching.lean`:

```lean
theorem exists_minimizing_real_nuclear_transport_matching
    (K L : Submodule ℝ E) (hKL : Module.finrank ℝ K = Module.finrank ℝ L) :
    ∃ T : E ≃ₗᵢ[ℝ] E, K.map T.toLinearMap = L ∧
      UnitarilyInvariantSeminorm.schatten ℝ E E 1 (LinearMap.id - T.toLinearMap) =
        realNuclearMatchingMinimum
          (fun j : {j : Fin (Module.finrank ℝ K) // 0 < K.principalAngles L j} =>
            K.principalAngles L j.val) ∧
      ∀ V : E ≃ₗᵢ[ℝ] E, K.map V.toLinearMap = L →
        UnitarilyInvariantSeminorm.schatten ℝ E E 1 (LinearMap.id - T.toLinearMap) ≤
          UnitarilyInvariantSeminorm.schatten ℝ E E 1 (LinearMap.id - V.toLinearMap)
```

`RealMatchingExponent.lean`:

```lean
def realNuclearPairWeight (theta psi : ℝ) : ℝ :=
  4 * Real.sin ((theta+psi)/2)

def realNuclearMatchingCost (theta : ι → ℝ) (s : Equiv.Perm ι) : ℝ := by
  classical
  exact ∑ i, if s i = i then min (4*Real.sin (theta i/2)) 2
    else realNuclearPairWeight (theta i) (theta (s i))/2
```

**Mapping notes.** A matching is encoded as an involution `s` of the label set (fixed points are unmatched labels; each pair contributes half its weight at each endpoint). The proof first establishes the matching formula for a differentiable Schatten exponent between 1 and 2 (it instantiates \(p=3/2\)) and passes to the trace-norm endpoint. The matching-value theorem does not certify a blossom algorithm.
