# 005000 — The direct rotation

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** geometry. **Audience:** angle operators, Halmos's two-subspace form, polar decomposition.

<!-- BEGIN SPOKEN LECTURE -->

The direct rotation

Given two subspaces U and V of the same dimension, many unitary maps carry U onto V. Even in the plane, if U is the horizontal line and V is the line at thirty degrees above it, three different orthogonal maps do the job: the rotation through thirty degrees, the rotation through two hundred and ten degrees, and the reflection across the line at fifteen degrees. Each sends the horizontal line onto the tilted one. Only the first is the obvious answer: turn the shortest way, and do nothing else.

This lecture makes that answer precise in any Hilbert space. The results are these. First, Davis and Kahan's definition: a unitary carrying U onto V is a direct rotation when, in block form relative to U and its complement, its two diagonal blocks are positive and its two off-diagonal blocks are negatives of each other's adjoints, exactly like a planar rotation matrix through an acute angle. Second, the construction of Sz.-Nagy and Kato: the operator T equal to Q P plus the identity minus Q, times the identity minus P, carries U into V, and its unitary polar factor is the direct rotation. Third, Davis and Kahan's Proposition 3.1: when both defect spaces are zero, the direct rotation exists, is unique, and is already singled out by positivity of the two diagonal blocks. Fourth, the direct rotation is a square root of the product of two reflections, and it turns each vector in the theta spectral subspace of the angle operator through exactly the angle theta. Interchanging U and V replaces the direct rotation by its inverse.

P and Q are the projections onto U and V, and Theta is the full angle operator of the pair.

Three ways to carry a line onto a line

Write each of the three planar maps as a two by two matrix in the standard basis, with the horizontal axis as U, and look at the four entries. The top left entry is the action of the map within U, the bottom right entry is the action within the complement of U, and the off-diagonal entries are the crossing parts.

The rotation through thirty degrees has cosine thirty on both diagonal entries, sine thirty below the diagonal, and minus sine thirty above it. Both diagonal entries are positive, and the off-diagonal entries are negatives of each other.

The rotation through two hundred and ten degrees has minus cosine thirty on both diagonal entries. It turns the horizontal unit vector around past the vertical, to the opposite end of the tilted line. Both diagonal entries are negative.

The reflection across the line at fifteen degrees has cosine thirty in the top left, minus cosine thirty in the bottom right, and sine thirty in both off-diagonal positions. Its action within U is positive, but within the complement of U it reverses direction.

The diagonal entries measure how much each map twists the subspace and its complement within themselves. The short rotation does not twist either: a vector of U goes to a vector whose component along U points the same way, and likewise for the complement. That is the property Davis and Kahan take as the definition.

The definition

Let W be a unitary map of the whole space that carries U onto V. This means W P equals Q W: projecting onto U and then applying W is the same as applying W and then projecting onto V. Relative to the decomposition of the space into U and its complement, W has four blocks. Following the paper, write C zero for the block from U to U, S zero for the block from U to the complement, minus S one for the block from the complement to U, and C one for the block from the complement to itself.

W is a direct rotation from U to V when three conditions hold. The diagonal block C zero is a positive operator on U. The diagonal block C one is a positive operator on the complement of U. And S one equals S zero star, so that the two crossing blocks are S zero and minus S zero star. In the plane, these are the conditions that the matrix has the form cosine, minus sine, sine, cosine with nonnegative cosine: a rotation through an angle between zero and ninety degrees.

The rotation through thirty degrees satisfies all three. The rotation through two hundred and ten degrees fails the positivity of both diagonal blocks. The reflection fails the positivity of C one, and its off-diagonal entries are equal rather than opposite.

The Sz.-Nagy–Kato construction

To build a direct rotation, start from a simpler operator that carries U into V but is not unitary. Define T to be Q P plus the identity minus Q, times the identity minus P. In words: take the component of a vector in U and project it onto V; take the component in the complement of U and project it onto the complement of V; add the results.

T sends U into V and the complement of U into the complement of V. Indeed T P equals Q P, and Q T also equals Q P, because Q annihilates the second term. So T P equals Q T. The only defect of T is that it shrinks lengths: projecting a vector of U onto V shortens it by the cosine of its angle.

How much does T shrink? Compute T star T. The cross terms vanish, because the first term of T lands in V and the second lands in the complement of V. What remains is P Q P plus the identity minus P, times the identity minus Q, times the identity minus P. On U this is P Q P, the squared cosine compression, cosine squared of Theta zero. On the complement of U it is the corresponding compression for the complements, cosine squared of Theta one. So T star T equals cosine squared of Theta. Equivalently, T star T equals the identity minus the square of P minus Q, since we know the square of P minus Q is sine squared of Theta. The modulus of T is cosine Theta.

Now remove the shrinking. The polar decomposition writes T as a unitary-type factor times its modulus, and when the modulus is invertible the factor is T times the inverse of cosine Theta. Cosine Theta is invertible exactly when every angle stays away from ninety degrees, which is the condition that the norm of P minus Q is less than one. Under that condition, define the direct rotation as T times the inverse of cosine Theta.

This was the construction of Béla Sz.-Nagy, in work published in 1947, given a streamlined algebraic form by Tosio Kato: T times the inverse square root of the identity minus the square of P minus Q, which is unitary.

Why is this factor the right one? First, it still carries U onto V. The square of P minus Q commutes with P, so cosine Theta does too, and so does its inverse. Therefore the direct rotation times P equals T times P times the inverse cosine, which equals Q T times the inverse cosine, which is Q times the direct rotation.

Second, it is a direct rotation in Davis and Kahan's sense. Its block from U to U is P Q P times the inverse of cosine Theta zero, which is cosine squared over cosine, namely cosine Theta zero. That is a positive operator. The same calculation on the complement gives cosine Theta one, also positive. The crossing blocks come out as negatives of each other's adjoints.

The cleanest way to see the whole operator is Halmos's form. On the generic part, written as K plus K with cosine C and sine S, the projection P has the identity in the top left, and Q has blocks C squared, C S, C S, S squared. Multiplying out, T has blocks C squared, minus C S, C S, C squared. Factor out C: T equals C times the block matrix with entries C, minus S, S, C. That block matrix is the planar rotation matrix with the angle replaced by the operator Theta. So T is the cosine times a rotation, and dividing by the cosine leaves the rotation. On the common part and the exterior part, both projections agree, T is the identity, and so is the direct rotation.

In the four-dimensional example with angles thirty and sixty degrees, U spanned by e one and e two, and V spanned by e one tilted thirty degrees toward e three and e two tilted sixty degrees toward e four, the direct rotation turns the plane of e one and e three through thirty degrees and the plane of e two and e four through sixty degrees. It is the map that rotates each principal plane through its own angle.

Uniqueness

Proposition 3.1 of the paper says more than existence. Suppose both defects are zero: no source vector is perpendicular to the whole target, and no target vector is perpendicular to the whole source. This is what Davis and Kahan call the acute case. Then the direct rotation exists and is unique, and in fact positivity of the two diagonal blocks alone determines it.

The proof shows how little room there is. Every unitary carrying U onto V can be written as the direct rotation times a unitary Z that maps U onto itself. Indeed, if W carries U onto V, then the inverse of the direct rotation, applied after W, carries U back onto U. Such a Z is block diagonal: a unitary Z zero on U and a unitary Z one on the complement. The diagonal block of W on U is then cosine Theta zero times Z zero.

Now impose positivity. Suppose cosine Theta zero times Z zero is a positive operator; call it G. A positive operator is self-adjoint, so G squared equals G times G star. That product is cosine Theta zero, times Z zero times Z zero star, times cosine Theta zero, which is cosine squared of Theta zero, because Z zero is unitary. So G is a positive square root of cosine squared Theta zero, and by uniqueness of positive square roots, G equals cosine Theta zero itself. Thus cosine Theta zero times Z zero equals cosine Theta zero, so Z zero is the identity on the range of cosine Theta zero. That range is dense in U exactly when cosine Theta zero has no kernel, that is, when no source vector is perpendicular to the target: the source defect is zero. In that case Z zero is the identity. The same argument on the complement uses the target defect. So in the acute case, W equals the direct rotation.

When the norm of P minus Q is less than one, cosine Theta is invertible, and the Sz.-Nagy–Kato formula applies. Davis and Kahan's acute case allows more. With both defects zero, cosine Theta has no kernel even if its spectrum reaches zero, and T is still one-to-one with dense range. Its polar decomposition then still produces a unitary factor, which is the direct rotation. So the hypothesis of Proposition 3.1 is the defect condition, not a bound on the norm of P minus Q.

A square root of two reflections

There is a second description of the direct rotation, which explains the name. Let J be the reflection through U, the operator two P minus the identity: it fixes U and negates its complement. In block form J is diagonal, with the identity and minus the identity.

Conjugating a block matrix by J negates its off-diagonal blocks and leaves its diagonal blocks alone. For the direct rotation, with blocks C zero, minus S zero star, S zero, C one, the conjugate has blocks C zero, S zero star, minus S zero, C one. That is its adjoint, since the diagonal blocks are self-adjoint. So J times the direct rotation times J equals the inverse of the direct rotation: reflecting the picture through U reverses the direction of turning.

From this, a short calculation gives the square. The reflection through V is two Q minus the identity, and since the direct rotation carries U onto V, this reflection equals the direct rotation times J times the inverse of the direct rotation. Multiply the two reflections: the reflection through V times the reflection through U equals the direct rotation, times J, times the inverse of the direct rotation, times J. The last three factors are J times the inverse rotation times J, which is the rotation again. So the product of the two reflections is the square of the direct rotation.

In the plane this is the familiar fact that reflecting across one line and then across another line at angle theta to it produces a rotation through two theta. The direct rotation is the half-way rotation. Davis and Kahan's Proposition 3.3 states this in general: every direct rotation is the principal unitary square root of the product of the reflections through V and through U, the square root whose spectrum lies in the closed right half of the complex plane. Conversely, such a square root is a direct rotation provided it carries the source defect onto the target defect. That proviso only matters when the defects are nonzero, where several square roots compete.

How the direct rotation moves vectors

The angle operator Theta commutes with both projections, with the direct rotation, and with the reflection J. The direct rotation can be written as the exponential of a skew operator times Theta: cosine Theta plus a partial isometry times sine Theta, the operator version of the planar formula for rotation through an angle. These are the commutation statements of Proposition 3.5.

They have a concrete meaning. If x lies in the spectral subspace where Theta equals theta, then the angle between x and its image under the direct rotation is exactly theta. In the four-dimensional example, e one moves through thirty degrees and e two through sixty. A vector halfway between them, e one plus e two over root two, is not an eigenvector of Theta; its image is the combination of the two rotated vectors, and the angle it moves through is the angle whose cosine is the average of cosine thirty and cosine sixty, about forty-seven degrees. The angle of motion is controlled by the angle operator, one spectral subspace at a time.

In the acute case Davis and Kahan add a uniqueness statement: the theta spectral subspace of Theta is the largest subspace that reduces both projections and on which every source vector meets its projection onto V at angle theta, and every complementary vector meets its projection onto the complement of V at angle theta.

Reversing the direction

Finally, what is the direct rotation from V back to U? The angle operator of the pair does not depend on the order, since the square of P minus Q is symmetric in P and Q. The skew factor changes sign. So the direct rotation from V to U is the adjoint of the direct rotation from U to V, which is its inverse. This is Corollary 3.2 of the paper. In the plane, turning the tilted line back to the horizontal is the rotation through minus thirty degrees.

The construction is invariant in another sense too. Because it is built from P and Q alone, it does not depend on any choice of bases, and when the norm of P minus Q is less than one it varies continuously with the two projections. That is the property that made it useful in perturbation theory: as an operator changes, the direct rotation identifies its moving spectral subspace with the original one without any arbitrary choice of eigenvectors.

Where the idea comes from

The intertwiner T and its unitary polar factor go back to Sz.-Nagy's 1947 work on perturbations of spectral projections; Kato gave the algebraic formula in a 1955 report and in his book Perturbation Theory for Linear Operators. Simon's survey of Kato's work recounts this history. Davis and Kahan named the direct rotation, characterized it by positive diagonal blocks, proved uniqueness in the acute case, and identified it as the principal square root of the product of two reflections.

To summarize. A direct rotation from U to V is a unitary carrying U onto V whose diagonal blocks are positive and whose crossing blocks are opposite adjoints. The intertwiner T equals Q P plus the complementary product has modulus cosine Theta, and its unitary polar factor is the direct rotation; in Halmos's coordinates T is the cosine times the operator rotation matrix. When both defects are zero, the direct rotation is unique, and positivity of the diagonal blocks alone characterizes it. It is the principal square root of the reflection through V times the reflection through U, it commutes with Theta, it turns each theta spectral subspace through exactly theta, and reversing the pair inverts it.

What the acute case excludes are right angles that are actually attained. When a source vector is perpendicular to the whole target, the intertwiner kills it, and the polar decomposition no longer determines a unitary there. Whether a direct rotation exists in that case depends on comparing the two defect spaces.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Definition 3.1

A unitary \(W\) with \(WP=QW\), in blocks relative to \(U\oplus U^\perp\),
\[
W\sim\begin{pmatrix}C_0&-S_1\\S_0&C_1\end{pmatrix},
\]
is a **direct rotation** when \(C_0\ge0\), \(C_1\ge0\), \(S_1=S_0^*\).

Planar check (\(U\) = horizontal axis, \(V\) at \(30^\circ\)): rotation by \(30^\circ\) is direct; rotation by \(210^\circ\) has \(C_0=C_1=-\cos30^\circ\); the reflection across \(15^\circ\), \(\begin{pmatrix}\cos30^\circ&\sin30^\circ\\\sin30^\circ&-\cos30^\circ\end{pmatrix}\), has \(C_1<0\) and \(S_1=-S_0\).

### Sz.-Nagy–Kato construction

\[
T=QP+(I-Q)(I-P),\qquad TP=QP=QT,\qquad T^*T=PQP+(I-P)(I-Q)(I-P)=I-(P-Q)^2=\cos^2\Theta.
\]
If \(\|P-Q\|<1\):
\[
U_{\rm dr}=T\,(I-(P-Q)^2)^{-1/2}=T(\cos\Theta)^{-1},\qquad U_{\rm dr}PU_{\rm dr}^*=Q,
\]
\(PU_{\rm dr}P=\cos\Theta_0\), \((I-P)U_{\rm dr}(I-P)=\cos\Theta_1\). In Halmos coordinates on \(K\oplus K\):
\[
T=\begin{pmatrix}C^2&-CS\\CS&C^2\end{pmatrix}=C\begin{pmatrix}C&-S\\S&C\end{pmatrix},\qquad U_{\rm dr}=\begin{pmatrix}C&-S\\S&C\end{pmatrix}.
\]
\(\ker T=D_0\oplus D_1\); \(T\) is injective with dense range iff \(D_0=D_1=\{0\}\), in which case its polar factor is unitary even if \(\|P-Q\|=1\).

### Propositions 3.1, 3.3, 3.5 and Corollary 3.2

- **3.1** (\(D_0=D_1=\{0\}\)): a direct rotation exists, is unique, and \(C_0,C_1\ge0\) alone characterize it among unitaries with \(WP=QW\). Proof: \(W=U_{\rm dr}(Z_0\oplus Z_1)\); \(C_0=\cos\Theta_0Z_0\ge0\Rightarrow C_0^2=\cos^2\Theta_0\Rightarrow C_0=\cos\Theta_0\Rightarrow Z_0=I\) on \(\overline{\operatorname{ran}}\cos\Theta_0=U\).
- **3.3**: with \(J=2P-I\), \(JU_{\rm dr}J=U_{\rm dr}^{-1}\) and \(2Q-I=U_{\rm dr}JU_{\rm dr}^{-1}\), so
\[
U_{\rm dr}^2=(2Q-I)(2P-I),
\]
\(\sigma(U_{\rm dr})\subseteq\{\operatorname{Re}z\ge0\}\). Conversely a unitary square root of \((2Q-I)(2P-I)\) with spectrum in the closed right half-plane, mapping \(D_0\) onto \(D_1\), is a direct rotation.
- **3.5**: \(\Theta\) commutes with \(P,Q,J_{\rm skew},U_{\rm dr}\); \(U_{\rm dr}=e^{J_{\rm skew}\Theta}=\cos\Theta+J_{\rm skew}\sin\Theta\); \(\cos^2\Theta=PQP+P^\perp Q^\perp P^\perp\); \(\Theta x=\theta x\Rightarrow\angle(x,U_{\rm dr}x)=\theta\); in the acute case the \(\theta\)-eigenspace is the unique maximal reducing subspace with the stated angle property.
- **Cor 3.2**: interchanging \(P,Q\) leaves \(\Theta\) unchanged, \(J_{\rm skew}\mapsto-J_{\rm skew}\), and the direct rotation becomes \(U_{\rm dr}^*\).

**Example.** Four-dimensional pair (angles \(30^\circ,60^\circ\)): \(U_{\rm dr}\) rotates \(\operatorname{span}\{e_1,e_3\}\) by \(30^\circ\) and \(\operatorname{span}\{e_2,e_4\}\) by \(60^\circ\). For \(x=(e_1+e_2)/\sqrt2\): \(\langle x,U_{\rm dr}x\rangle=\tfrac12(\cos30^\circ+\cos60^\circ)\approx0.683\), angle \(\approx46.9^\circ\).

### Lean correspondence

`DavisKahan/Geometry/Halmos/GenericRotationPredicates.lean`:

```lean
structure IsDirectRotation
    (U V : Submodule 𝕜 H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection] (T : H →L[𝕜] H) : Prop where
  unitary_mem : T ∈ unitary (H →L[𝕜] H)
  intertwines : T * U.starProjection = V.starProjection * T
  source_compression_nonnegative :
    ∀ x : H, 0 ≤ RCLike.re
      ⟪x, (U.starProjection * T * U.starProjection) x⟫_𝕜
  complement_compression_nonnegative :
    ∀ x : H, 0 ≤ RCLike.re
      ⟪x, ((Uᗮ).starProjection * T * (Uᗮ).starProjection) x⟫_𝕜
  crossed_blocks :
    (Uᗮ).starProjection * T * U.starProjection =
      -star (U.starProjection * T * (Uᗮ).starProjection)
```

`DavisKahan/FiniteDimensional/DirectRotation/Basic.lean`:

```lean
noncomputable def canonicalIntertwiner (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] : E →ₗ[𝕜] E :=
  V.starProjection.toLinearMap ∘ₗ U.starProjection.toLinearMap +
    Vᗮ.starProjection.toLinearMap ∘ₗ Uᗮ.starProjection.toLinearMap

noncomputable def directRotation (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V) : E ≃ₗᵢ[𝕜] E   -- polar isometry of canonicalIntertwiner
```

`DavisKahan/Sources/DavisKahan1970/Section3AcuteDirectRotation.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
theorem proposition3_1 (hacute : Submodule.IsAcute U V) :
    acute_directRotation U V ∈ unitary (H →L[𝕜] H) ∧
      acute_directRotation U V * U.starProjection =
        V.starProjection * acute_directRotation U V ∧
      (U.starProjection * acute_directRotation U V * U.starProjection).IsPositive ∧
      (Uᗮ.starProjection * acute_directRotation U V * Uᗮ.starProjection).IsPositive ∧
      Uᗮ.starProjection * acute_directRotation U V * U.starProjection =
        -star (U.starProjection * acute_directRotation U V * Uᗮ.starProjection) ∧
      ∀ W : H →L[𝕜] H,
        W ∈ unitary (H →L[𝕜] H) →
        W * U.starProjection = V.starProjection * W →
        (U.starProjection * W * U.starProjection).IsPositive →
        (Uᗮ.starProjection * W * Uᗮ.starProjection).IsPositive →
        W = acute_directRotation U V
```

**Mapping notes.**

- `Submodule.IsAcute U V` is the defect condition; `TauCeti.isAcute_iff_inf_orthogonal_eq_bot` identifies it with \(U\cap V^\perp=\{0\}\wedge U^\perp\cap V=\{0\}\). Proposition 3.1 carries no bound on \(\|P-Q\|\), no dimension assumption (1.5), and no finite-dimensionality, matching the lecture's remark that the hypothesis is the defect condition.
- `IsDirectRotation` states positivity of the diagonal compressions through real parts of quadratic forms; `proposition3_1` uses genuine operator positivity `IsPositive`.
- Proposition 3.3: `proposition3_3_complex_forward`, `proposition3_3_complex_converse` (and real variants). Proposition 3.5: `proposition3_5_commutations`, `proposition3_5_eigenvector_angle`, `proposition3_5_angleEigenspace_uniqueMaximal`. Corollary 3.2: `corollary3_2`, `complex_directRotation_reversal`, `real_directRotation_reversal`. All in `TauCeti.DavisKahan1970`; see `dev/davis-kahan-1970-formalization-result-inventory.json`.
