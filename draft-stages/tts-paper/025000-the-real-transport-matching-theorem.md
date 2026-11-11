# 025000 — The real transport matching theorem

**Track:** G3 audio paper track. **Draft:** adapted from G2 lecture 145000. **Section:** section4-transport. **Audience:** prior linear algebra and basic analysis.

<!-- BEGIN SPOKEN LECTURE -->

# From rotation counterexample to real transport matching

The canonical direct rotation need not minimize an unsquared Schatten norm of whole-space displacement among all real orthogonal maps transporting one subspace onto another. A four-dimensional example with two equal principal angles refutes the broad claim. A useful positive problem remains: characterize the global minimum when the exponent p is strictly between one and two.

## What are we optimizing?

Take two subspaces K and L of equal finite dimension inside a real Euclidean space. Consider every orthogonal operator U that maps K onto L. Measure its displacement from the identity using a Schatten p norm. Concretely, take every singular value of the difference between U and the identity, raise it to power p, add, and then take the pth root.

For p equal two, this is the Frobenius norm. For p equal one, it is the nuclear or trace norm. When p lies strictly between one and two, the contribution of a set of singular values differs from its squared-energy contribution. That is precisely where the direct rotation can lose optimality.

Why do we require equal dimensions? An invertible orthogonal map preserves dimension. If K and L have different dimensions, no such U maps one onto the other, regardless of how close their projections might be. We would first need a different admissible notion of transport.

## The single principal-angle block

Begin with a single principal angle theta between two lines. In their common real two-dimensional principal plane, an orthogonal rotation through theta maps the first line to the second. Its displacement operator has two equal singular values, each equal to twice sine of theta over two. Therefore its pth power Schatten cost is two times the quantity twice sine theta over two, raised to power p.

There is a choice of the sign of the rotation, but its singular values are the same. Reflections can also map one line to the other. Their displacement costs may differ, so the full optimization must allow all orthogonal transports, not just orientation-preserving rotations.

With two or more principal angles, a naive strategy would minimize the cost in each principal plane independently and sum. That works for some objectives, but our four-dimensional counterexample demonstrated a failure of unrestricted independent-plane optimality.

The missing degree of freedom is a coupling between two principal-angle blocks. A four-dimensional orthogonal operator can mix their coordinates while still mapping the entire source subspace onto the target. It might produce a more favorable distribution of displacement singular values under the chosen exponent.

## Why a matching appears

The real transport optimization turns that freedom into a finite combinatorial problem. Label the positive principal angles. Each label can remain a singleton, carrying the best permitted one-angle cost, or it can be paired with another label, carrying the best two-angle cost from a four-dimensional block.

A matching consists of disjoint pairs together with unmatched singletons. Represent it by a permutation that equals its own inverse: a fixed point denotes a singleton, and a two-cycle a paired block. No angle label can belong to two different pairs.

The cost of a matching is the sum of singleton weights and complete pair weights. If we sum over all labels rather than over edges, each pair contributes half its full weight at each endpoint, so it is counted exactly once. The minimum over all matchings exists because the set of involutive permutations of finitely many labels is finite.

This is a substantial simplification. Instead of optimizing over a continuum of orthogonal matrices all at once, we can evaluate finitely many candidate matchings, where the difficult continuous optimization has been absorbed into the one-angle and two-angle weights.

## An exact two-angle test

Suppose the positive principal angles are theta and psi. There are two combinatorial candidates. One leaves both labels unmatched. Its cost is the sum of the two singleton costs. The other pairs them, and its cost is a single optimized four-dimensional value.

The global minimum is the smaller of those two numbers. For p equal two, the squared Frobenius objective is tied directly to the sum of squared displacements, and the canonical direct rotation satisfies the established squared-objective theorem. For exponents strictly between one and two, the paired option can be better.

The optimized cost of a paired block need not equal the cost of the direct rotation acting independently on its two principal planes. The correct pair cost minimizes over both relevant four-dimensional determinant classes. Replacing it with the direct rotation's candidate cost would assert an optimality property that fails for the unsquared objective.

For three positive angles, the finite choices are: three singletons, or one pair and one singleton. For four, we also have two disjoint pairs. In general, the number of matchings grows, but the mathematical structure stays finite and explicit.

## A paired candidate that genuinely wins inside the theorem's range

We can test the matching idea without knowing the optimized pair weight. In real four-space let U be the plane of the first two coordinate axes. Form two perpendicular unit vectors by adding the first and third coordinate vectors, and by adding the second and fourth, normalizing each sum. Rotate their span by ninety degrees and leave its orthogonal complement fixed. Call this orthogonal map W and set V equal to W of U. The two principal angles between U and V are both forty-five degrees, as the cross-Gram calculation confirms. The canonical direct rotation has four displacement singular values, each about point seven six five. The map W has two displacement singular values equal to the square root of two and two zeros.

Choose the exponent p equal to one point one. Raise each singular value to that power and add. For the direct rotation, the p-th power total is approximately two point nine eight one. For the coupled transporter, it is approximately two point nine two eight. The coupled transporter is better, and p lies strictly between one and two.

Now choose p equal to one point five. The corresponding totals are approximately two point six seven eight for the direct rotation and three point three six four for this coupled candidate. Their order has reversed.

A subtle point is that the coupled transporter we wrote down is a feasible four-dimensional block, but we have not shown it minimizes the pair weight. The optimized pair weight can only be smaller than or equal to its cost. At p equal to one point one, the example therefore proves that an admissible pair configuration can beat the independent direct rotations. At p equal to one point five, it proves only that this specific coupled candidate loses; another allowed transporter could still be better. The matching theorem is what resolves the global comparison.

## The two directions of an optimality proof

A formula for the minimum needs two distinct inequalities. First, every admissible real orthogonal transporter must have a displacement cost at least the matching minimum. Second, every candidate matching, or at least an optimal matching, must be realizable by a genuine orthogonal transporter with exactly the assigned cost.

The first direction is an extraction theorem. It analyzes an ambient optimizer and shows that its cost is represented by suitable singleton and paired blocks, preserving the original principal-angle labels. The second direction is a realization theorem. It assembles orthogonal blocks into an ambient transporter with the required action on the source subspace.

Neither direction can be replaced merely by noting that the minimum of finitely many numbers exists. A combinatorial optimizer might describe no actual geometric operator unless realization is proved. Conversely, a construction of candidate transports does not rule out a more exotic, lower-cost orthogonal matrix.

The result combines two arguments in finite-dimensional real spaces with equal-dimensional subspaces and Schatten exponent p strictly between one and two: a lower bound extracting matching data from every ambient optimizer, and an upper bound constructing an orthogonal transporter from an optimizing matching. Repeated and zero principal angles remain legitimate labeled inputs.

## Why the exponent matters

The nuclear norm is the sum of singular values, and the Frobenius norm comes from their squared sum. A cost that is additive in squared singular values rewards a different distribution than a cost that is additive in singular values themselves. Between powers one and two, changing the singular-value distribution by mixing principal planes can be advantageous.

This is why one must name the exponent in an optimality theorem. The best operator for one Schatten norm need not minimize another. The direct rotation's optimality for a squared objective does not imply its optimality for an unsquared objective, even though the underlying pair of subspaces is identical.

There are also delicate endpoint questions. A theorem proved for exponents strictly between one and two should not be quoted as automatically covering p equal one or p equal two. Continuity of an optimized value can help study endpoint costs, but a complete endpoint statement may need its own realization and attainment arguments.

## Scope of the matching theorem

For real finite-dimensional spaces and source and target subspaces of equal dimension, with Schatten exponent p strictly between one and two, the minimum pth-power displacement cost is the minimum of the matching costs. There is a real orthogonal transporter realizing it, and every admissible transporter has at least that cost.

A small calculation makes the competing possibilities concrete. Take two principal angles, thirty and sixty degrees, and let p equal three halves. If we choose the canonical direct rotation independently in the two principal planes, their chord lengths are approximately zero point five one eight and one. Each occurs twice among the displacement singular values. The resulting pth-power cost is about two point seven four five. That is an explicit feasible cost, not an assertion that it is the minimum.

The matching problem compares the optimized singleton configuration with the optimized coupled four-dimensional block. Whichever has the smaller *optimized* cost yields a realizable transporter. The difficult direction of the theorem is proving that no more complicated orthogonal mixing does better than every matching. Without that global lower bound, a matching construction would supply only candidate transports.

The theorem concerns real finite-dimensional spaces, equal subspace dimensions, and exponents strictly between one and two. The endpoints and arbitrary symmetric gauges require their own arguments. The geometry of principal-angle blocks explains the candidate costs; the matching theorem establishes that these blocks are sufficient for the stated global optimization.

<!-- END SPOKEN LECTURE -->

---

## Display-only mathematical and Lean correspondence

The matching program lives in `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`, `.../SchattenRealMatchingWeights.lean`, and `.../RealMatchingAttainment.lean`. For a planar rotation by `θ`, the two displacement singular values equal `2 sin(θ/2)`; the direct-rotation **candidate** p-cost is therefore `2(2 sin(θ/2))^p`. The singleton and paired weights in the matching theorem refer to their own optimized class-specific definitions, not to this candidate formula by default.

The source theorem `exists_minimizing_real_schatten_transport_matching` proves the unrestricted ambient minimum for real finite-dimensional equally ranked subspaces and `1<p<2`. Do not extend the result to other exponents merely from this declaration.

**A feasible cost is not the matching minimum.** For \(\theta_1=\pi/6\), \(\theta_2=\pi/3\) and \(p=3/2\), the two-plane canonical direct rotation has
\[
 \|I-D\|_{S_p}^{p}=2\bigl(2\sin(\pi/12)\bigr)^p+2\bigl(2\sin(\pi/6)\bigr)^p\approx2.74485.
\]
The matching optimum compares *optimized* singleton and pair weights. This expression is only an admissible candidate upper bound for that minimum.

**Explicit interior-exponent witness, separate from the optimized pair weight.** Let \(U=\operatorname{span}(e_1,e_2)\) and
\[
W=\frac12\begin{pmatrix}
1&-1&-1&-1\\1&1&1&-1\\-1&-1&1&-1\\1&-1&1&1
\end{pmatrix},\qquad V=WU.
\]
The top-left \(2\times2\) cross-Gram block is \(\frac12\begin{psmallmatrix}1&-1\\1&1\end{psmallmatrix}\), with both singular values \(1/\sqrt2\), so both principal angles are \(\pi/4\). The map \(W\) fixes a two-plane and rotates its perpendicular plane by ninety degrees. Set \(a=\sqrt{2-\sqrt2}\) and \(b=\sqrt2\). Then
\[
 s(I-D)=(a,a,a,a),\quad s(I-W)=(b,b,0,0),\quad
 F_D(p)=4a^p,\quad F_W(p)=2b^p.
\]
At \(p=11/10\), \(F_D\approx2.980689>2.928171\approx F_W\). At \(p=3/2\), \(F_D\approx2.678332<3.363586\approx F_W\). Since a paired block cost is defined by optimizing its admissible four-dimensional class, its value is **at most** the displayed candidate \(F_W(p)\); the candidate is not asserted to realize that optimized weight. In particular the first strict inequality exhibits a genuinely beneficial coupled choice in the theorem's interior exponent range.

## Exact Lean declaration excerpts

**`realSchattenMatchingCost`** — The combinatorial cost sums fixed-point singleton weights and half a paired weight at each endpoint of a two-cycle. The paired weight comes from the optimized four-dimensional model.

Source: `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`; exact declaration header (proof body omitted).

```lean
def realSchattenMatchingCost {ι : Type*} [Fintype ι]
    (p : ℝ) (theta : ι → ℝ) (s : Equiv.Perm ι) : ℝ := by
```

**`exists_attains_realSchattenMatchingMinimum`** — This theorem only attains the FINITE COMBINATORIAL minimum. It does not by itself construct an ambient orthogonal transporter.

Source: `DavisKahan/FiniteDimensional/DirectRotation/SchattenRealMatching.lean`; exact declaration header (proof body omitted).

```lean
theorem exists_attains_realSchattenMatchingMinimum {ι : Type*} [Fintype ι]
    (p : ℝ) (theta : ι → ℝ) :
    ∃ s : Equiv.Perm ι, Function.Involutive s ∧
      realSchattenMatchingCost p theta s = realSchattenMatchingMinimum p theta := by
```

**`exists_minimizing_real_schatten_transport_matching`** — This theorem supplies the missing geometric attainment and global comparison for equal-dimensional REAL subspaces with Schatten exponent strictly between one and two.

Source: `DavisKahan/FiniteDimensional/DirectRotation/RealMatchingAttainment.lean`; exact declaration header (proof body omitted).

```lean
theorem exists_minimizing_real_schatten_transport_matching
    (p : ℝ≥0∞) [Fact (1 ≤ p)] (hp : p ≠ ∞)
    (hp1 : 1 < p.toReal) (hp2 : p.toReal < 2)
    (K L : Submodule ℝ E) (hKL : Module.finrank ℝ K = Module.finrank ℝ L) :
    ∃ U : E ≃ₗᵢ[ℝ] E, K.map U.toLinearMap = L ∧
      UnitarilyInvariantSeminorm.schatten ℝ E E p
          (LinearMap.id - U.toLinearMap) ^ p.toReal =
        realPositiveSchattenMatchingMinimum p.toReal
          (fun j : {j : Fin (Module.finrank ℝ K) // 0 < K.principalAngles L j} =>
            K.principalAngles L j.val) ∧
      ∀ T : E ≃ₗᵢ[ℝ] E, K.map T.toLinearMap = L →
        UnitarilyInvariantSeminorm.schatten ℝ E E p
            (LinearMap.id - U.toLinearMap) ^ p.toReal ≤
          UnitarilyInvariantSeminorm.schatten ℝ E E p
            (LinearMap.id - T.toLinearMap) ^ p.toReal := by
```

