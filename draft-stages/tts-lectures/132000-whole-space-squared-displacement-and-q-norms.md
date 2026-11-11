# 132000 — Whole-space squared displacement and Q-norms

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `122000–123000`, `130000`, `131000`. **Next:** `133000`.

<!-- BEGIN SPOKEN LECTURE -->

# Whole-space squared displacement and Q-norms

Rotate a line in the plane through forty-five degrees. The rotation carries the original line to the target line, moving both coordinate directions by the same modest amount. Reflection across the halfway line also maps the original line to the target. It fixes one direction and reverses another. We can compare the two transformations by how far they move every vector in the ambient plane.

Imagine accounting for motion direction by direction. We could add the distances traveled. Or we could square each distance before adding, making a large movement more expensive relative to a small one. Both are reasonable ways to measure the same transformation. They can rank two transformations differently.

Our question is which part of the direct rotation's minimal-motion property survives when we measure **every direction in the whole space**, rather than just directions in the source. We will first prove a statement about squared movement. Only then will we ask which unsquared norms it controls.

## A positive operator records squared movement

Work first in a finite-dimensional real or complex inner-product space. Let the source and target subspaces be called U and V, with a direct rotation D carrying U to V. A competing orthogonal or unitary map W also carries U to V, but may act differently on vectors outside U.

Start with one unit vector x. Its displacement is the vector from W x back to x. We want its length squared. There is an operator that records exactly this quantity: take identity minus W, follow it by its adjoint, in Gram order. More precisely, apply identity minus W first, and then apply its adjoint. Call the resulting positive operator G.

When we take the inner product of G x with x, we get the squared distance between x and W x. The vector x can point anywhere in the ambient space. G is therefore a device for measuring the squared motion of a direction, even when W mixes principal planes.

Unitarity simplifies the formula. Expanding the product gives twice the identity minus W minus its adjoint. The eigenvalues of G are nonnegative. They are precisely the squared singular values of identity minus W. Those eigenvalues let us compare movement across all directions without relying on a particular basis.

For one principal plane of angle theta, the direct rotation turns both orthogonal directions through theta. The distance moved by either unit basis vector is a chord of length twice the sine of half theta. The associated G for D is therefore a scalar multiple of the identity on that plane, with scalar four times the sine squared of half theta. This is the numerical value we want to compare to other transporters.

## First control each half of the source space

Here is the first reason to separate directions. Every ambient vector has a part in U and a part perpendicular to U. We will examine the two starting parts separately, even though W can send them to different output spaces.

Start with vectors lying in U. Restrict identity minus W to those input vectors. The restricted-displacement theorem says that the ordered singular values for the direct rotation are no larger, one by one, than those for W. Geometrically, the canonical principal-vector match is optimal on the source itself, even when a competitor chooses a different orthonormal basis in the target.

The key point is that this statement only controls vectors in U. We need an independent estimate for vectors in the perpendicular complement. Fortunately, a unitary W carrying U onto V also carries U perpendicular onto V perpendicular. The direct rotation for the complementary pair is the same full-space operator D. Applying the restricted theorem a second time gives the analogous singular-value comparison on the complement.

Now square those restricted singular values. The squares are the eigenvalues of the two **diagonal compressions** of G. One compression describes displacements starting in U; the other describes displacements starting in U perpendicular.

There is a trap here. The full operator G for W need not be block diagonal. It can have cross terms between the two source blocks. We cannot simply concatenate the two restricted spectra and call the result the spectrum of G.

## Merge and then pinch

First imagine a positive operator with no cross terms. Its two diagonal blocks have separate eigenvalue lists. Joining the blocks means joining the lists and sorting them. For example, if the first list is four and one, and the second is three and two, the combined list is four, three, two, one. The largest two add to seven: we took one from each list. The largest three add to nine: we took the four from the first list and the three and two from the second. The calculation considers every possible split, then keeps the largest total.

More generally, a sum of the largest k eigenvalues can be computed by trying every split of those k places between the two blocks. Such sums are called Ky Fan prefix sums. Because the direct rotation has no larger eigenvalue at each position in either block, it has no larger prefix after the two lists are merged.

But we have only compared the **block-diagonal part** of W's squared displacement. The cross terms are still missing. That is the precise reason we need one more operation.

To relate those diagonal blocks to the full G, use **pinching**. Let J be the reflection that acts as plus one on U and minus one on U perpendicular. Average G with J G J. The off-diagonal blocks cancel, leaving exactly the two diagonal compressions. Unitary conjugation preserves every unitarily invariant norm, and taking an average cannot increase a norm. In particular, pinching cannot increase any Ky Fan prefix sum of this positive operator.

A two-by-two example makes the direction of the inequality visible. Start with the positive matrix having diagonal entries three and off-diagonal entries two. Its eigenvalues are five and one. Pinching to the coordinate axes gives the diagonal matrix with entries three and three. The largest eigenvalue drops from five to three; the sum of both eigenvalues remains six. The smaller eigenvalue has grown. So pinching controls the cumulative largest eigenvalues. It does not say that each individual eigenvalue goes down.

We can check this mechanism in the line-rotation example too. A reflection across the line halfway between source and target has the same source displacement energy as the direct rotation: twice one minus the cosine of theta. But on the source-perpendicular direction its displacement energy is twice one plus the cosine of theta. Those are the diagonal blocks of the reflection's squared displacement. Its full squared-displacement eigenvalues are four and zero, because a reflection fixes one direction and reverses the other. Pinching removes the cross terms, leaving just the two diagonal energies. The direct rotation has the smaller first diagonal energy on both source blocks, with equality on the source line, and the prefix comparison follows. This is the abstract proof made visible in a two-by-two matrix.

For D, something special happens. On a principal plane, D plus its adjoint is twice the cosine of the principal angle times the identity. The squared-displacement operator for D is therefore scalar on each such plane. It already respects the split into U and U perpendicular. Pinching D changes nothing.

The proof now has all its pieces. We can read them in order: compare the squared restricted singular values on U, compare them again on U perpendicular, merge those two lists, and pinch the competitor to bound the merged prefixes by those of its full squared displacement. Therefore every Ky Fan prefix of the direct G is at most the corresponding prefix of the competitor G. Ky Fan dominance extends this comparison to every unitarily invariant norm of the **positive squared-displacement operator**.

## What squaring allows, and what it does not

Can we turn that result into a theorem about the norm of identity minus W? Sometimes. The operator norm of the squared-displacement operator is the square of the operator norm of displacement. Its trace is the square of the Frobenius, or Hilbert–Schmidt, norm of displacement. Both inherit the direct rotation's optimality.

More generally, for a Schatten p norm with p at least two, the square of the Schatten p norm of a matrix X equals the Schatten p-over-two norm of X adjoint X. Since p over two is at least one, that second expression is a genuine unitarily invariant norm. Norms with such a representation are called Q-norms, and the squared theorem gives optimality for their unsquared displacements as well.

Why does this reasoning fail for the trace norm, the sum of singular values? Its square contains cross terms between different singular values. In fact, it cannot arise as a norm of X adjoint X in this way. To see the obstruction, look at a two-by-two diagonal matrix with entries one and zero. A hypothetical norm M representing the square of trace norm would assign its Gram matrix value one. The same holds with the one in the other diagonal position. But for the identity matrix, the squared trace norm is four. The triangle inequality for M would bound its value by one plus one, or two. That contradiction identifies the failed step: the purported M is not a norm.

## Return to two equal principal angles

Consider two perpendicular principal planes, each with angle forty-five degrees. The direct rotation moves four independent directions by the same amount, approximately point seven six five. The exact chord length is the square root of the quantity two minus square root of two. When squared, each of the four displacement singular values becomes two minus square root of two, about point five eight six.

A different admissible orthogonal transporter can fix one two-plane and turn its perpendicular two-plane through ninety degrees. Its displacement singular values are square root of two, square root of two, zero, and zero. The squared list is two, two, zero, zero.

The direct rotation's squared prefixes are approximately point five eight six, one point one seven two, one point seven five seven, and two point three four three. Those of the competitor are two, four, four, and four. Every squared prefix favors the direct rotation, exactly as the theorem predicts.

Yet the unsquared trace totals go in the other direction: the direct rotation costs about three point zero six one, while the competitor costs about two point eight two eight. The operator and Frobenius norms still favor the direct rotation. The same admissible pair thus separates the two optimization questions without contradicting either theorem.

## Conclusion

The whole-space squared-displacement theorem depends on a specific chain: restricted singular values on both complementary source spaces, merging Ky Fan sums, and pinching away cross terms. Its conclusion is robust for the positive Gram operator. To infer optimality for an unsquared displacement norm, that norm must also respect the squaring operation through the Q-norm identity. The trace norm does not, and the four-dimensional example shows the consequence.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Worked proof: compressions, pinching, and the Q-norm boundary

In finite dimension, write \(P=P_U\), \(J=2P-I\), and \(X_W=I-W\). Define
\[
G_W=X_W^*X_W=2I-W-W^*\succeq0,\qquad
\mathcal P_P(G_W)=PG_WP+(I-P)G_W(I-P)=\tfrac12(G_W+JG_WJ).
\]
The compressions of \(G_W\) to \(U\) and \(U^\perp\) equal the Gram operators
of \(X_W|_U\) and \(X_W|_{U^\perp}\). The restricted displacement theorem for
\((U,V)\) and \((U^\perp,V^\perp)\), followed by squaring nonnegative singular
values, gives componentwise domination of the corresponding compressed
eigenvalue lists for the direct rotation \(D\).

For positive block matrices \(A\oplus B\), each Ky Fan prefix is the maximum
over all splits \(i+j=k\) of the two block-prefix sums. Consequently
\[
\sum_{r=1}^k\lambda_r(G_D)
=\sum_{r=1}^k\lambda_r(\mathcal P_P(G_D))
\le\sum_{r=1}^k\lambda_r(\mathcal P_P(G_W))
\le\sum_{r=1}^k\lambda_r(G_W).
\]
The last step is Ky Fan convexity and unitary invariance applied to the average
\(\mathcal P_P\). The first equality uses \(\mathcal P_P(G_D)=G_D\).

For real lines \(U=\operatorname{span}(e_1)\) and
\(V=\operatorname{span}((c,s))\), the reflecting transporter
\(F=\begin{psmallmatrix}c&s\\s&-c\end{psmallmatrix}\) satisfies
\(F(U)=V\) and \(G_F=2(I-F)\). Relative to \(U\oplus U^\perp\),
\[
G_F=\begin{pmatrix}2(1-c)&-2s\\-2s&2(1+c)\end{pmatrix},\qquad
\mathcal P_P(G_F)=\operatorname{diag}(2(1-c),2(1+c)),
\]
while \(G_D=2(1-c)I_2\). The full eigenvalues of \(G_F\) are \((4,0)\),
so the last Ky Fan comparison is visible directly in the planar model.

A valid **positive** pinching example is
\[
\begin{pmatrix}3&2\\2&3\end{pmatrix}
\mapsto\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad
(5,1)\mapsto(3,3).
\]
The smaller eigenvalue *increases*; the claim is prefix (weak-majorization)
comparison, not pointwise eigenvalue comparison.

If \(N(X)^2=M(X^*X)\) with \(M\) a unitarily invariant norm, the theorem
applies to \(N\). For \(2\le p<\infty\),
\(\|X\|_p^2=\|X^*X\|_{p/2}\); the operator-norm case is the \(p=\infty\)
limit. Nuclear norm cannot have this Q-representation: if
\(N(X)=\|X\|_1\), then hypothetical \(M\) must give
\(M(E_{11})=M(E_{22})=1\) but \(M(I_2)=\|I_2\|_1^2=4\),
contradicting \(M(I_2)\le M(E_{11})+M(E_{22})=2\).

For \(\theta=\pi/4\) repeated twice, put
\(a=\sqrt{2-\sqrt2}\), \(b=\sqrt2\). There are transporters with
\(s(I-D)=(a,a,a,a)\) and \(s(I-W)=(b,b,0,0)\), so their Gram spectra are
\((a^2,a^2,a^2,a^2)\) and \((2,2,0,0)\). The squared prefixes satisfy
\(k(2-\sqrt2)\le2\min(k,2)\) for \(1\le k\le4\), whereas
\(4a>2b\) for unsquared trace norm.

Define \(G_W=(I-W)^*(I-W)=2I-W-W^*\). Proposition 4.3 gives
\[
 \sum_{j=1}^k s_j(G_D)\le \sum_{j=1}^k s_j(G_W)\quad(k\ge1),
\]
not pointwise domination of each \(s_j\). The proof uses restricted displacement on \(U\) and \(U^\perp\), squaring through \(s_j(X^*X)=s_j(X)^2\), block-sum Ky Fan comparison, and pinching.

A Q-norm \(N\) has \(N(X)^2=M(X^*X)\) for some unitarily invariant norm \(M\). Schatten \(p\) for \(2\le p\le\infty\) satisfy this with \(M=S_{p/2}\). The source also proves full-displacement operator- and Hilbert–Schmidt-norm consequences in infinite-dimensional matched-defect scope.

## Exact Lean declaration excerpts

**`proposition4_3_squaredDisplacement_kyFan`.** A `ℂ`-Hilbert-space result comparing **every Ky Fan prefix** of positive squared displacement, which is the valid root of the invariant-norm statement.

`DavisKahan/Geometry/Polar/DisplacementSquareExtremal.lean` — `proposition4_3_squaredDisplacement_kyFan` (exact declaration header; proof body omitted):

```lean
theorem proposition4_3_squaredDisplacement_kyFan (U V : Submodule ℂ H)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : IsUniformlyAcute U V) (W : H →L[ℂ] H)
    (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W) (k : ℕ) :
    (((1 - star (spectraDirectRotation U V hacute)) *
          (1 - spectraDirectRotation U V hacute)).kyFanGauge k : ℝ) ≤
      (((1 - star W) * (1 - W)).kyFanGauge k : ℝ) :=
```

**`IsQNorm`.** This predicate formalizes the additional norm property `N(A)^2 = M(A⋆A)` with `M` itself unitarily invariant.

`DavisKahan/FiniteDimensional/DirectRotation/QNorm.lean` — `IsQNorm` (exact declaration header; proof body omitted):

```lean
def IsQNorm (N : UnitarilyInvariantSeminorm 𝕜 E E) : Prop :=
```

**`directRotation_fullDisplacement_qnorm`.** `hN : IsQNorm N` is essential. The theorem allows any acute pair and any admissible isometric competitor; it does not impose the printed angle threshold.

`DavisKahan/FiniteDimensional/DirectRotation/QNorm.lean` — `directRotation_fullDisplacement_qnorm` (exact declaration header; proof body omitted):

```lean
theorem directRotation_fullDisplacement_qnorm
    (N : UnitarilyInvariantSeminorm 𝕜 E E) (hN : IsQNorm N)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V) (W : E ≃ₗᵢ[𝕜] E)
    (hmap : U.map W.toLinearMap = V) :
    N (LinearMap.id - (directRotation U V hacute).toLinearMap) ≤
      N (LinearMap.id - W.toLinearMap) :=
```

**`Proposition4_3_infiniteDimensional_nonacute_fullDisplacement_hilbertSchmidt`.** The infinite-dimensional Hilbert–Schmidt consequence is an extended-real comparison at matched-defect scope, not a claim of arbitrary unsquared invariant-norm optimality.

`DavisKahan/Sources/DavisKahan1970/Section4.lean` — `Proposition4_3_infiniteDimensional_nonacute_fullDisplacement_hilbertSchmidt` (exact declaration header; proof body omitted):

```lean
theorem Proposition4_3_infiniteDimensional_nonacute_fullDisplacement_hilbertSchmidt
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (J : DavisKahan.halmosSourceDefect U V ≃ₗᵢ[ℂ]
      DavisKahan.halmosTargetDefect U V)
    (W : H →L[ℂ] H) (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W) :
    ((OperatorIdealFamily.hilbertSchmidt ℂ).gauge (1 - DavisKahan.nonacuteDirectRotation U V J)) ≤
      ((OperatorIdealFamily.hilbertSchmidt ℂ).gauge (1 - W)) :=
```

