# 130000 — Restricted direct-rotation optimality

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `037000–051000`, `052000–057000`, `095000–100000`. **Next:** `131000`.

<!-- BEGIN SPOKEN LECTURE -->

# Restricted direct-rotation optimality

Turn a unit line through sixty degrees inside a plane. Its unit vector moves by a straight-line distance of one. A rotation through the shorter arc achieves that distance. Any longer turn that reaches the same target line moves the vector at least as far, once we choose the target direction with positive overlap.

Now replace the line by a two-dimensional subspace. An orthogonal or unitary map carrying it onto a target subspace may mix the two principal directions, so the one-line argument no longer settles the problem. Can that mixing reduce the largest displacement, or the sum of displacements measured by a different norm?

The restricted direct-rotation theorem answers this for every unitarily invariant norm: among all admissible transports, the canonical direct rotation minimizes the displacement **of vectors starting in the source subspace**. Its proof rests on a singular-value min–max argument, and we will see exactly why a tempting pointwise Gram-matrix comparison is too strong. The displacement of vectors outside the source is a separate question.

## Set up the competitors

Take two finite-dimensional subspaces U and V of the same Hilbert space. For the first proof, suppose there is a canonical direct rotation D taking U to V. In particular, we can choose orthonormal principal vectors u-one through u-r in U and matching vectors v-one through v-r in V. Their inner products are the cosines of the principal angles, each between zero and a right angle. On each principal plane D turns u-j into v-j through the shorter angle and acts canonically on the perpendicular direction. Common directions stay fixed.

Let W be any competing unitary taking U onto V. It may rotate inside V after arriving there; it may mix different principal planes; and it may act in any permissible way on the complementary space. We measure its **restricted displacement** by applying identity minus W only to vectors in U. In matrix notation that is the rectangular map from U to the ambient space sending x to x minus W x.

For the direct rotation, call that restricted map T. For the competitor, call it S. We want more than an operator-norm inequality. We will compare their entire decreasing lists of singular values, one coordinate at a time.

## A geometric inequality for one vector

Choose any unit vector x in U. Since W takes U onto V, the vector W x is a unit vector in V. The squared distance from x to W x is two minus twice the real part of their inner product. Because W x lies in V, that real inner product is no greater than the length of the orthogonal projection of x onto V.

We therefore get an elementary lower bound: the squared displacement of x under W is at least two minus twice the norm of the V-projection of x. Notice that this estimate only used the destination subspace. It did not assume W respects principal directions.

The bound involves the length of the V projection rather than its inner product with x. That distinction is important. We cannot replace the projection length by the quadratic form of the positive cosine operator and claim a pointwise ordering of the two displacement Gram operators. Such a quadratic-form ordering is generally false when a competitor mixes principal directions.

Instead, keep the norm bound and use a subspace on which it becomes sharp enough. Define the positive cosine operator C on U as the modulus of the projection from U onto V. Its eigenvalues are the principal cosines. Arrange the principal angles in descending order, so the corresponding cosines are ascending.

For a chosen index k, take M to be the span of the first k principal vectors, those with the largest angles and smallest cosines. For every unit vector x in M, the norm of its projection onto V equals the norm of C x, and is at most cosine theta-k. This follows by expanding x in those principal vectors: each coefficient is multiplied by a cosine no larger than cosine theta-k.

Return to the earlier one-vector inequality. For every unit x in M, the squared displacement under W is at least two minus twice cosine theta-k. Therefore the displacement norm is at least two sine of theta-k over two, uniformly on the entire k-dimensional subspace M.

That is precisely the kind of lower bound required by the singular-value min–max principle. We do not need the competing displacement to be larger on every individual vector than the direct displacement.

## From quadratic forms to singular values

The singular-value min–max theorem says that the k-th largest singular value of a rectangular map is the maximum, over k-dimensional source subspaces, of the minimum output length on their unit spheres. We just exhibited such a subspace on which every unit vector has output length at least two sine of theta-k over two. That lower bound therefore holds for the competitor’s k-th singular value.

Consequently the k-th singular value of the competitor's restricted displacement is at least that principal chord. For the direct rotation the same chord is exactly its k-th singular value. This proves the pointwise singular-value ordering for every k, without asserting a false Gram-operator ordering.

To see the direct list explicitly, consider a principal vector u with principal angle theta. Its image under D is the matching vector v. Their inner product is cosine theta, so the distance between them is the square root of the difference between two and twice the cosine of theta. The half-angle identity turns this into twice the sine of half theta. Different principal planes are orthogonal; consequently the singular-value list of the restricted displacement of D consists of these principal chords, sorted from largest to smallest, with zeros where appropriate.

Here is a numerical example. Take two source directions with principal angles thirty and sixty degrees. The direct restricted displacement has singular values approximately one point zero and zero point five one eight. Any unitary carrying the source plane onto the target must have its first singular value at least one and its second at least zero point five one eight. This conclusion allows the competitor to mix the two directions.

Here is an actual competitor that mixes them. Place the two source directions in four-dimensional space, with independent principal planes. The first makes a sixty-degree angle with its target vector, and the second a thirty-degree angle. Instead of mapping each source vector to its corresponding target vector, let the competitor send the first source vector to a target combination obtained by a ten-degree rotation within V. Send the second source vector to the perpendicular target combination. These two images remain orthonormal, so this is an isometry on U that extends to an orthogonal map of the ambient space.

What happens to its displacement Gram matrix? In the principal source coordinates, the direct rotation has a diagonal cosine-overlap matrix: one half in the first entry, and square root of three divided by two in the second. The mixed competitor multiplies this matrix by a ten-degree planar rotation. The restricted displacement Gram matrix is twice identity minus that overlap matrix and its transpose. Subtract the direct Gram matrix. The resulting two-by-two symmetric matrix has positive diagonal entries but a negative determinant, hence one negative eigenvalue.

So it would be false to claim that the direct displacement Gram operator is below the competitor's Gram operator in positive-semidefinite order. Nevertheless the min–max argument just proved that the competitor's singular values cannot be smaller than the two principal chords. Its conclusion survives precisely because it uses a carefully chosen subspace for each index rather than a pointwise comparison for all source vectors.

## Passing to every invariant norm

A unitarily invariant norm depends only on the singular values through a symmetric gauge. Every such gauge is monotone under coordinatewise domination of nonnegative sorted singular values. Since we proved the stronger pointwise comparison, the direct rotation minimizes every unitarily invariant norm of the restricted displacement.

For the operator norm, the conclusion concerns the largest chord. For the Frobenius norm, square and sum the chords. For the trace norm, add the chords themselves. We do not have to prove separate optimization theorems for those three choices.

In infinite-dimensional Hilbert space we replace finite singular-value lists with approximation numbers, and we must account for ideal membership. If the competitor's restricted displacement belongs to a normalized invariant ideal satisfying the appropriate Ky Fan dominance property, the approximation-number comparison places the direct displacement in the ideal and bounds its gauge. The original theorem retains compact-angle and crossed-defect hypotheses in its infinite-dimensional setting. The construction of the chosen defect matching is part of the direct rotation, rather than a new freedom in the objective.

## Where the proof can be misapplied

There are two different rectangular maps in play. The map x goes to x minus W x with x restricted to U measures the distance the source vectors themselves travel. The full operator identity minus W allows an input vector entirely outside U. Our comparison says nothing pointwise about that additional part.

The restricted theorem also does not say the competitor must be the canonical rotation to attain equality. If singular values coincide or some directions are fixed, there may be several optimizers. For a strictly convex objective and nondegenerate angles one can sometimes prove more, but that needs separate hypotheses.

Finally, be careful with the meaning of an angle. The principal angle between U and V is determined by projections, not by the angle between an arbitrary vector x and its image W x. For the direct rotation these quantities coincide along principal vectors. A competing W can move some vectors farther while still arriving at the correct target subspace.

## Closing proof map

The argument has four parts. First, the direct rotation chooses the positive cosine geometry of the source-to-target projection. Second, a subspace of the k largest principal-angle directions gives a uniform lower bound on the competitor's output length. Third, singular-value min–max converts that subspace bound into every singular-value inequality. Fourth, symmetric-gauge monotonicity converts that list comparison into universal restricted-norm optimality.

This establishes restricted-norm optimality. It does not assert that the same transporter minimizes every unsquared norm of displacement across the entire ambient space.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

The relevant restricted maps are \(T_D=(I-D)|_U\) and \(T_W=(I-W)|_U\). The finite conclusion is \(s_k(T_D)\le s_k(T_W)\) for all \(k\), and consequently \(N(T_D)\le N(T_W)\) for any unitarily invariant norm \(N\). The direct singular values are \(2\sin(\theta_j/2)\).

### A competitor that defeats Gram ordering but not singular-value ordering

Let \(c_1=\cos(\pi/3)=1/2\), \(c_2=\cos(\pi/6)=\sqrt3/2\), \(C=\operatorname{diag}(c_1,c_2)\), and \(R_\varphi=\begin{psmallmatrix}\cos\varphi&-\sin\varphi\\\sin\varphi&\cos\varphi\end{psmallmatrix}\). Choose orthonormal principal vectors \((u_1,u_2)\) and \((v_1,v_2)\) with \(\langle u_i,v_j\rangle=c_i\delta_{ij}\). The restricted isometry \(W|_U\) sending the source basis to \((v_1,v_2)R_\varphi\) extends to an ambient orthogonal map. Let \(S=(I-W)|_U\) and \(T=(I-D)|_U\). Then
\[
 S^*S=2I-CR_\varphi-R_\varphi^TC,\qquad
 T^*T=2I-2C,
\]
\[
 S^*S-T^*T=\begin{pmatrix}
 2c_1(1-\cos\varphi)&-(c_2-c_1)\sin\varphi\\
 -(c_2-c_1)\sin\varphi&2c_2(1-\cos\varphi)
 \end{pmatrix}.
\]
Its determinant is
\[
 4c_1c_2(1-\cos\varphi)^2-(c_2-c_1)^2\sin^2\varphi.
\]
This is negative for all sufficiently small nonzero \(\varphi\), and in particular for \(\varphi=\pi/18\). Thus the Gram difference is not positive semidefinite. Still \(s_k(T)\le s_k(S)\) by the principal-vector subspace min–max proof, so all unitarily invariant restricted-displacement norm conclusions remain valid.

**Proof-scope note.** The proof uses the pointwise projection-length bound **plus** a k-dimensional principal-vector subspace and the min–max characterization of singular values. It deliberately does not assert quadratic-form ordering of the two displacement Gram operators. In the nonacute case the source uses matched crossed defects and the nonacute direct-rotation construction. The compact Hilbert-space result is stated for approximation numbers and has additional existence/ideal hypotheses.

## Exact Lean declaration excerpts

**`finite_proposition4_1_singularValues`.** Finite-dimensional `𝕜` is an `RCLike` scalar field; `U,V` are submodules with orthogonal projections, and `W` is an isometric equivalence mapping one to the other. Its conclusion is indexed singular-value domination for **restricted** displacements.

`DavisKahan/Sources/DavisKahan1970/Section4FiniteSurface.lean` — `finite_proposition4_1_singularValues` (exact declaration header; proof body omitted):

```lean
theorem finite_proposition4_1_singularValues
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V)
    (W : E ≃ₗᵢ[𝕜] E) (hmap : U.map W.toLinearMap = V) (n : ℕ) :
    ((LinearMap.id - (DavisKahan.FiniteDimensional.directRotation U V hacute).toLinearMap) ∘ₗ
        U.starProjection.toLinearMap).singularValues n ≤
      ((LinearMap.id - W.toLinearMap) ∘ₗ U.starProjection.toLinearMap).singularValues n :=
```

**`proposition4_1_directRotation_sourceExact_complex`.** Here `D` is the paper’s source-defined direct rotation, not merely any intertwining unitary. The conclusion includes the principal-chord list and a pointwise approximation-number bound at the compact Hilbert-space scope.

`DavisKahan/Sources/DavisKahan1970/Section4DirectRotationSource.lean` — `proposition4_1_directRotation_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem proposition4_1_directRotation_sourceExact_complex
    [TopologicalSpace.SeparableSpace H]
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hcompact : IsCompactOperator (TauCeti.principalSineOperator U V))
    (D : H →L[ℂ] H) (hD : DavisKahan.IsSourceDirectRotation U V D)
    (W : H →L[ℂ] H) (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W) :
    (∃ v : {n : ℕ // 0 < TauCeti.principalSineSequence U V n} → U,
        Orthonormal ℂ v ∧
          ∀ n : {n : ℕ // 0 < TauCeti.principalSineSequence U V n},
            TauCeti.principalAngleSequence U V (n : ℕ) ≤
              TauCeti.vectorAngle ℂ (v n : H) (W (v n : H))) ∧
      (∀ n : ℕ,
        ((((1 - D) ∘L U.starProjection).singularValue n : ℝ) : Real) =
          2 * Real.sin (TauCeti.principalAngleSequence U V n / 2)) ∧
      ∀ n : ℕ,
        (((1 - D) ∘L U.starProjection).singularValue n : ℝ) ≤
          (((1 - W) ∘L U.starProjection).singularValue n : ℝ) :=
```

**`corollary4_1_directRotation_sourceExact_complex`.** `N` is a normalized unitary-invariant norm with an `N.Mem` hypothesis on the competitor’s restricted displacement; the conclusion supplies membership for the direct displacement and a gauge bound.

`DavisKahan/Sources/DavisKahan1970/Section4DirectRotationSource.lean` — `corollary4_1_directRotation_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem corollary4_1_directRotation_sourceExact_complex
    [TopologicalSpace.SeparableSpace H]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hcompact : IsCompactOperator (TauCeti.principalSineOperator U V))
    (D : H →L[ℂ] H) (hD : DavisKahan.IsSourceDirectRotation U V D)
    (W : H →L[ℂ] H) (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W)
    (hWmem : N.Mem ((1 - W) ∘L U.starProjection)) :
    N.Mem ((1 - D) ∘L U.starProjection) ∧
      N.gauge ((1 - D) ∘L U.starProjection) ≤
        N.gauge ((1 - W) ∘L U.starProjection) :=
```

