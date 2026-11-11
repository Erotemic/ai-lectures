# 134000 — The four-dimensional real counterexample

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `042000–045000`, `132000–133000`. **Next:** `135000`.

<!-- BEGIN SPOKEN LECTURE -->

# The four-dimensional real counterexample

Consider two two-dimensional subspaces in real four-space whose principal angles are both forty-five degrees. The canonical direct rotation is obvious once the principal planes are known: rotate each plane by forty-five degrees. We will build a second, equally admissible orthogonal motion that fixes two ambient directions completely and turns the other two through ninety degrees. Its trace-norm displacement is strictly smaller.

We will verify three things independently: that the competing map really carries the source onto the target, that the subspaces have the claimed principal angles, and that the competing map has the claimed singular values. Only after those checks can the cost comparison refute a universal optimality statement.

## Construct the subspaces first

Write real four-space as two copies of the ordinary coordinate plane. We can specify any ambient vector by giving two planar vectors, x and y. The source U consists of all pairs where y is zero. So x can move freely in two directions, while the other two coordinates begin at zero. This is a two-dimensional source inside a four-dimensional ambient space.

Fix an angle theta strictly between zero and ninety degrees, and abbreviate its cosine and sine by c and s. Define the direct rotation D of this four-space by the following rule. Its first output component is c times x minus s times y. Its second output component is s times x plus c times y.

This is an orthogonal map because the usual cosine-sine rotation identity works componentwise. It sends U onto V, where V consists of the pairs c x and s x as x ranges over the coordinate plane. The source and target both have dimension two.

To find their principal angles, choose an orthonormal basis of U and use its images under D as an orthonormal basis of V. The matrix of overlaps between these two bases is simply c times the two-by-two identity. Its two singular values are c. Therefore both principal angles equal theta. In particular, theta equal forty-five degrees satisfies the printed sixty-degree restriction with room to spare.

## Introduce an internal rotation

Inside the two-dimensional coordinate plane, let A be the ordinary counterclockwise rotation by theta. Construct a new ambient orthogonal operator W by first applying A to x and A to y, and then applying D.

The first stage is orthogonal because each A is. The second stage is orthogonal because D is. Therefore their composition W is orthogonal. On a vector in U, whose second component is zero, the result is the pair c times A x and s times A x. As x ranges over the plane, so does A x. Thus W of U equals V exactly.

This is a proof of admissibility, not an assertion based on the appearance of a matrix. We are now free to compare W against D for a norm that measures full ambient displacement.

## Find the two planes on which W acts simply

We want to understand W without expanding a four-by-four characteristic polynomial. The trick is to describe two planes by how their two coordinate pieces relate.

Let J be the quarter-turn in the ordinary coordinate plane. It rotates a vector by ninety degrees, and applying J twice sends a vector to its negative. The internal rotation A is cosine theta times identity plus sine theta times J.

Consider first the pairs x and J x. If x points to the right, J x points upward. So one example of such a four-dimensional vector is the pair of planar arrows right and up. These pairs fill a two-dimensional plane inside the ambient four-space.

Apply W to such a pair. The internal A turns both pieces forward by theta. The subsequent D turns this linked pair back by theta. The two effects cancel. Every vector of this form is fixed by W.

For a second family, use the pairs x and minus J x: right paired with down in the example. These pairs form the orthogonal complement of the fixed plane. This time the internal turn and the direct rotation reinforce one another. W sends x to A applied twice to x, a rotation through twice theta, and preserves the negative-quarter-turn relation between the two components.

We have accounted for all four ambient dimensions. Two form a fixed plane; the other two form a plane rotated through twice theta. That is the mental picture behind the singular values.

The eigenvalue picture follows without diagonalizing a four-by-four characteristic polynomial. W fixes two orthogonal directions and rotates their perpendicular plane through twice theta. Its displacement has two zero singular values and two equal nonzero singular values, each twice the sine of theta.

The canonical D has a different distribution. It rotates two perpendicular principal planes through theta, so all four singular values of identity minus D are twice the sine of half theta.

## Compare the costs at forty-five degrees

Set theta equal to forty-five degrees. The two nonzero singular values of identity minus W become square root of two, while the other two are zero. Its trace norm, the sum of all four singular values, is two square roots of two, approximately two point eight two eight.

For D, all four singular values are equal. Each is approximately point seven six five. Exactly, it is the square root of the quantity two minus square root of two. Adding four copies gives a trace cost of approximately three point zero six one.

The decimal comparison is clear, but there is also a short exact check. Both costs are positive, so we may square them without changing which is larger. The direct cost squared is sixteen times the quantity two minus square root of two. The competing cost squared is eight. The first exceeds the second precisely when square root of two is less than three halves. That last inequality holds because two is less than nine quarters.

This supplies two acute real subspaces, an admissible orthogonal transporter, and a specific invariant norm for which the direct rotation loses. That is enough to disprove a statement asserting that D minimizes *every* such norm under a sixty-degree threshold.

## Check the positive squared displacement too

The example is stronger when we calculate the quantity that remains optimal. For D, the eigenvalues of its positive squared displacement are four copies of two minus square root of two, about point five eight six. For W, they are two, two, zero, zero.

At prefixes of length one through four, the direct sums are approximately point five eight six, one point one seven two, one point seven five seven, and two point three four three. The competitor prefixes are two, four, four, and four. Every prefix of the direct squared list is smaller.

Consequently the direct rotation satisfies the squared-displacement theorem here. It also has smaller Frobenius displacement, whose square is the sum of the squared singular values. It loses only the unsquared trace-norm comparison in this calculation. The two conclusions concern different spectral operations.

## Certify global trace optimality

We have proved that W beats D. To know whether W is actually best among *all* orthogonal transports, we need a lower bound that applies to every competitor.

The source and target each have an orthogonal projection. Their difference measures the unavoidable geometric change between the subspaces. For any orthogonal transporter Z carrying U to V, the trace norm of its full displacement is at least the trace norm of that projection difference. A reflection-commutator argument proves the bound without assuming Z preserves principal planes.

Our two principal angles are both theta. Each contributes two projection-difference singular values, each equal to the sine of theta. So the projection-difference trace norm is four times the sine of theta.

Now look back at W. It has exactly two moving singular directions, each with displacement twice the sine of theta. Their sum is also four times the sine of theta. W reaches the lower bound shared by all admissible transports. That is why it is a global trace-norm minimizer, not just an improvement over D.

The same calculation works for every positive theta at most a right angle. D costs eight times the sine of half theta, while W costs four times the sine of theta. The double-angle formula makes the second cost the first multiplied by the cosine of half theta, strictly less than one for positive theta. Thus no positive angle threshold, however small, can make the printed unsquared all-norm assertion valid for arbitrary real ambient dimensions.

## Conclusion

The transport constraint allows a coordinated internal rotation of the source and its complement. In four real dimensions that freedom changes two small ambient rotations into one larger rotation and one fixed plane. The full trace norm favors the latter, while the squared displacement favors the canonical direct rotation. The distinction comes from the actual singular-value lists, and it persists for arbitrarily small positive principal angles.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### A parameterized, verified four-dimensional family

Write \(\mathbb R^4=\mathbb R^2\oplus\mathbb R^2\),
\(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\),
\(c=\cos\theta\), \(s=\sin\theta\), and
\[
A_\theta=cI+sJ,\qquad
D_\theta=\begin{pmatrix}cI&-sI\\sI&cI\end{pmatrix},\qquad
W_\theta=D_\theta\begin{pmatrix}A_\theta&0\\0&A_\theta\end{pmatrix}.
\]
Both factors in \(W_\theta\) are orthogonal. Let
\(U=\{(x,0):x\in\mathbb R^2\}\),
\(V=\{(cx,sx):x\in\mathbb R^2\}\). Since
\(W_\theta(x,0)=(cA_\theta x,sA_\theta x)\), one has \(W_\theta U=V\).
The cross-Gram matrix for the natural orthonormal frames of \(U,V\) is
\(cI_2\), giving exactly two principal angles equal to \(\theta\).

Set \(M_+=\{(x,Jx)\}\) and \(M_-=\{(x,-Jx)\}\). These are orthogonal,
span \(\mathbb R^4\), and satisfy
\[
W_\theta|_{M_+}=I,\qquad
W_\theta(x,-Jx)=(A_\theta^2x,-JA_\theta^2x).
\]
Thus the latter restriction rotates through \(2\theta\). Exact singular values:
\[
\begin{aligned}
s(I-D_\theta)&=(2\sin(\theta/2))^{[4]},\\
s(I-W_\theta)&=(2\sin\theta,2\sin\theta,0,0),\\
s(P_U-P_V)&=(\sin\theta)^{[4]}.
\end{aligned}
\]
Therefore \(\|I-W_\theta\|_1=4\sin\theta=\|P_U-P_V\|_1\) is
the **global** trace minimum; for \(0<\theta\le\pi/2\),
\(\|I-D_\theta\|_1=8\sin(\theta/2)>4\sin\theta\).

At \(\theta=\pi/4\), a separate coordinate realization already certified
by `ShortRotationCounterexample.lean` is the sign matrix \(W\) displayed
below. Its eigenvalues and trace costs agree with the family above; no
identity between these two coordinate matrices is asserted.

With \(U=\operatorname{span}(e_1,e_2)\) and
\[
W=\tfrac12\begin{pmatrix}
1&-1&-1&-1\\1&1&1&-1\\-1&-1&1&-1\\1&-1&1&1
\end{pmatrix},\quad V=WU,
\]
the cross-Gram matrix has \(C^*C=\tfrac12I_2\), so \(\theta_1=\theta_2=\pi/4\). The singular values are
\[
s(I-W)=(\sqrt2,\sqrt2,0,0),\qquad
s(I-D)=(\sqrt{2-\sqrt2},\sqrt{2-\sqrt2},\sqrt{2-\sqrt2},\sqrt{2-\sqrt2}).
\]
Hence \(\|I-W\|_1=2\sqrt2<4\sqrt{2-\sqrt2}=\|I-D\|_1\). Yet \(s((I-D)^*(I-D))\prec_w s((I-W)^*(I-W))\). The exact matrix and refutation are in `ShortRotationCounterexample.lean`; a continuum of equal-angle examples is documented in `papers/dk_formalization_journal/counterexample.tex`.

## Exact Lean declaration excerpts

**`Wmat`.** The explicit real `4×4` witness matrix is `½` times a sign matrix. Its orthogonality and transport properties are established elsewhere in the same source module.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `Wmat` (exact declaration header; proof body omitted):

```lean
@[expose] def Wmat : Matrix (Fin 4) (Fin 4) ℝ :=
```

**`principalAngle_le`.** The source proves the maximal principal angle is at most `π/3` for the exact witness (and the module establishes that both angles equal `π/4`).

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `principalAngle_le` (exact declaration header; proof body omitted):

```lean
theorem principalAngle_le : Submodule.principalAngles U4 V4 0 ≤ Real.pi / 3 :=
```

**`kyFanSum_lt`.** This proves the strict reversed trace-norm comparison at full Ky Fan rank four.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `kyFanSum_lt` (exact declaration header; proof body omitted):

```lean
theorem kyFanSum_lt :
    (LinearMap.id - Wequiv.toLinearMap).kyFanSum 4 <
      (LinearMap.id -
        (directRotation U4 V4 acute).toLinearMap).kyFanSum 4 :=
```

**`shortRotation_fullDisplacement_refuted`.** The witness includes real subspaces, acuteness, an admissible unitary, a short largest principal angle, and a strict trace-norm improvement.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `shortRotation_fullDisplacement_refuted` (exact declaration header; proof body omitted):

```lean
theorem shortRotation_fullDisplacement_refuted :
    ∃ (U V : Submodule ℝ (EuclideanSpace ℝ (Fin 4)))
      (hacute : Submodule.IsAcute U V)
      (W : EuclideanSpace ℝ (Fin 4) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin 4)),
      U.map W.toLinearMap = V ∧
      Submodule.principalAngles U V 0 ≤ Real.pi / 3 ∧
      (LinearMap.id - W.toLinearMap).kyFanSum 4 <
        (LinearMap.id - (directRotation U V hacute).toLinearMap).kyFanSum 4 :=
```

**`not_davisKahanProposition4_4_Finite`.** This discharges the formal negation of the universal proposition by instantiating it with trace norm.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `not_davisKahanProposition4_4_Finite` (exact declaration header; proof body omitted):

```lean
theorem not_davisKahanProposition4_4_Finite :
    ¬ DavisKahanProposition4_4_Finite.{0} :=
```

