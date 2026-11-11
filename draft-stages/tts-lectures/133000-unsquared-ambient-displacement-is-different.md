# 133000 — Unsquared ambient displacement is different

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `130000–132000`. **Next:** `134000`.

<!-- BEGIN SPOKEN LECTURE -->

# Unsquared ambient displacement is different

Suppose we must carry one line to another by an orthogonal motion. If the angle is forty-five degrees, rotating the whole plane by forty-five degrees seems economical: both directions move a little. A reflection also succeeds, but it reverses one direction completely. In the plane, the rotation wins for every unitarily invariant norm of displacement. In four dimensions, with two such line-pairs, a transporter can do better in trace norm by linking the planes.

The difference is freedom in the **whole-space transport constraint**. Understanding that freedom also explains why a bound for restricted movement cannot simply be promoted to a bound for the entire ambient space.

## What is allowed to move?

Let U and V be equally dimensional subspaces of a finite-dimensional real inner-product space. An admissible transporter W is an orthogonal map with W of U equal to V. Its full displacement is identity minus W. A unitarily invariant norm measures that displacement through its singular values, without choosing a favored coordinate basis.

To describe that freedom, first choose the direct rotation D as a reference motion. Think of a competitor as having two stages. Before the direct rotation acts, it may rearrange directions *inside* the source. It may independently rearrange directions inside the perpendicular complement. As long as it leaves those two spaces intact, the final direct rotation still sends the source onto V.

Call this preliminary rearrangement S. Algebraically, S is D inverse followed by W, because undoing D after W brings the target V back to U. Thus S maps U onto itself. Since S is orthogonal, it also maps U perpendicular onto itself. Conversely, every orthogonal S with these two properties produces an admissible W by composing D with S.

Relative to the split into U and its complement, S has two diagonal blocks. That sounds restrictive, but each block may mix the principal-vector directions inside its own space. When D acts afterward, the resulting W need not preserve the separate principal planes. The distinction is between preserving the **source subspace** and preserving **each canonical principal plane**. The transport constraint requires the first, not the second.

That is the extra variable missing from a plane-by-plane comparison. The principal angles are fixed by U and V, but the displacement singular values of W are not.

## Why the planar sixty-degree rule is correct

Take one real source line and one target line making angle theta, between zero and ninety degrees, inside a two-dimensional ambient plane. Up to signs, the best orientation-preserving transporter is the rotation through theta. Its two displacement singular values are equal to a, where a is twice the sine of half theta.

The orientation-reversing option is a reflection that maps the source line onto the target line. Its displacement singular values are two and zero. We can compare these lists without choosing a particular unitarily invariant norm. For two nonnegative entries, weak majorization has just two tests. Compare the largest entry, and compare the sum of both entries.

For the rotation, the list is a and a. For the reflection, it is two and zero. The largest-entry test always succeeds: a is at most two. The total-sum test asks whether twice a is at most two, or simply whether a is at most one. Since a is twice the sine of half theta, this holds exactly when theta is at most sixty degrees.

So the sixty-degree threshold is a theorem about the **two-dimensional choice** between a rotation and a reflection. It has not examined internal rearrangements across several principal planes.

This proves the familiar threshold for the planar choice. It does not tell us that a higher-dimensional W is a direct sum of these same planar choices. An arbitrary source-preserving S can rearrange directions *within* U and *within* its complement, so the global list of displacement singular values can change shape.

## What two equal angles permit

Now let U be a two-dimensional coordinate plane in real four-space. Write a vector as two two-component pieces. For an angle theta, define a canonical map D that sends a source vector, with second component zero, to the vector whose first component is cosine theta times the source and whose second component is sine theta times the source. Its action on the whole space is a direct sum of two equal planar rotations.

Let A be an ordinary rotation by theta inside the two-dimensional source coordinates. Apply A to each of the two component spaces before applying D. This produces another orthogonal W, equal to D composed with the block-diagonal map having A in each block. It still carries U onto the same V, because A merely changes coordinates within the source plane.

What changes is W's action on the ambient four-space. Two orthogonal planes, built by pairing a vector with its quarter-turned copy, reveal the answer. On one such plane W is the identity. On the other it is a rotation through twice theta. The direct map D instead rotates two planes through theta each.

Therefore the displacement singular values of D are four copies of twice the sine of half theta. Those of W are twice the sine of theta, repeated twice, followed by two zeros. The extra internal motion has redistributed displacement among the ambient directions. Two directions now do not move at all; the other two move farther. Keep that picture in mind before taking a norm: fewer moving directions can lower a sum of lengths, even when it raises the largest displacement.

For trace norm the direct cost is eight times the sine of half theta. The coupled map costs four times the sine of theta. The double-angle formula says this second cost equals the first times the cosine of half theta. For every strictly positive theta, that cosine is less than one. Thus W has strictly smaller trace cost, even if theta is far below sixty degrees.

The planar threshold remains true. It simply addresses a smaller feasible family.

## Why squared displacement can still be minimal

At forty-five degrees, the four singular values of the direct displacement are all approximately point seven six five. The coupled competitor has approximately one point four one four, one point four one four, zero, zero.

Square the lists. The direct values become four copies of point five eight six. The competitor becomes two, two, zero, zero. Every Ky Fan prefix of the squared direct list is no larger than the corresponding prefix of the competitor list. Yet the sum of the *unsquared* values is larger for D.

Taking square roots entry by entry does not preserve weak-majorization comparisons. The square-root function rewards distributing a fixed amount of squared energy across more entries. This is why the positive squared-displacement theorem and the failed universal trace-norm claim can coexist.

## A lower bound that never depended on the direct rotation

There is still a universal comparison for unsquared full displacement. Denote the source and target orthogonal projections by P and Q. The transport constraint gives Q equal to W P W adjoint.

The geometric obstacle is visible in the projections. Let P project onto the source and Q onto the target. Their difference measures how much the two subspaces disagree. Any map W carrying one subspace onto the other must pay at least that much displacement, in every unitarily invariant norm.

Here is the reason. Form the source reflection J by making it plus one on U and minus one on U perpendicular. Form the target reflection the same way using V. Since W sends both source pieces to their corresponding target pieces, transporting first and reflecting second agrees with reflecting first and transporting second.

Each reflection equals twice its projection minus the identity. The difference of the two reflections is therefore twice Q minus twice P. Multiply that difference by W. Using their intertwining property, the result can be written as W times J minus J times W: a commutator.

Now replace each occurrence of W in this commutator by identity plus W minus identity. The identity terms cancel. What remains is the difference of two products, each containing W minus identity and one orthogonal reflection. Multiplication by a reflection leaves an invariant norm unchanged. The triangle inequality therefore bounds the commutator by **twice** the norm of identity minus W.

But the commutator also represents **twice** the difference of the two projections, up to the orthogonal factor W. The factors of two cancel. We obtain the promised lower bound: the norm of P minus Q is no greater than the norm of identity minus W, for every admissible W. This bound applies whether or not the direct rotation minimizes the chosen norm.

The bound does not say that D achieves equality. In the four-dimensional equal-angle trace example, the coupled transporter does achieve equality, while D has larger cost. We can therefore certify that the competing map is globally trace-optimal without searching through every orthogonal matrix.

## Conclusion

A two-dimensional angle restriction can settle the choice between planar rotation and reflection. The unrestricted ambient problem includes internal source and complement motions, and those motions can couple principal planes. Restricted singular-value optimality survives; squared full-displacement optimality survives. A universal unsquared statement requires its own argument, and for trace norm in the real four-dimensional case the direct rotation is not the minimizer.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Exact transport fiber and why its stabilizer can mix principal planes

Fix one admissible orthogonal transport \(D(U)=V\). Every other admissible
orthogonal \(W\) factors uniquely as
\[
W=DS,\qquad S=D^*W,\qquad S(U)=U,\quad S(U^\perp)=U^\perp.
\]
Relative to \(U\oplus U^\perp\), \(S=A\oplus B\) with independent orthogonal
blocks. There is no requirement that these blocks preserve the principal vectors.
For repeated principal angles, selecting nontrivial \(A,B\) redistributes
full-space displacement without changing \(U,V\) or their principal angles.

For one real principal plane the direct and reflecting candidates have
\(s(I-D)=(a,a)\), \(s(I-F)=(2,0)\),
\(a=2\sin(\theta/2)\). Weak majorization of \((a,a)\) by \((2,0)\)
is equivalent to \(2a\le2\), hence \(\theta\le\pi/3\). This implication is
specific to that one-plane comparison.

For the global lower bound, put \(P=P_U\), \(Q=P_V\),
\(J_P=2P-I\), \(J_Q=2Q-I\). Since \(J_QW=WJ_P\),
\[
2(Q-P)W=(J_Q-J_P)W=WJ_P-J_PW
=(W-I)J_P-J_P(W-I).
\]
Every unitarily invariant norm \(N\) therefore satisfies
\[
2N(Q-P)\le 2N(W-I),\quad\text{so}\quad N(P-Q)\le N(I-W).
\]
The proof uses no angle restriction and does not assume optimality of \(D\).

The printed real claim is a universal inequality for \(N(I-D)\) over every unitarily invariant norm and every orthogonal \(W\) mapping \(U\) to \(V\) when \(\theta_{\max}\le\pi/3\). The repository represents it as a proposition-valued definition and proves its negation. The planar candidates have singular values \((2\sin(\theta/2),2\sin(\theta/2))\) and \((2,0)\). Their all-gauge weak-majorization threshold is \(\theta\le\pi/3\), but this planar classification does not extend to arbitrary four-dimensional transporters.

For all admissible \(W\), \(N(P_U-P_V)\le N(I-W)\). This is a general lower bound, not an optimality assertion for \(D\).

## Exact Lean declaration excerpts

**`example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three`.** This is the **two-dimensional Example 4.1 model**, with a Boolean choice between direct and reflecting transporter. It does not assert arbitrary-dimensional minimality.

`DavisKahan/Sources/DavisKahan1970/Section4LowDimensional.lean` — `example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three` (exact declaration header; proof body omitted):

```lean
theorem example4_1_directRotation_uiNorm_minimal_of_le_pi_div_three
    {theta : ℝ} (h0 : 0 ≤ theta) (hpi : theta ≤ Real.pi / 2)
    (hθ : theta ≤ Real.pi / 3)
    (flip : Bool)
    (N : UnitarilyInvariantSeminorm ℝ RealPlane RealPlane) :
    N (LinearMap.id - example41DirectRotation theta) ≤
      N (LinearMap.id - example4_1_competitor theta flip) :=
```

**`DavisKahanProposition4_4_Finite`.** This is the proposition-valued **false** printed assertion. It universally quantifies over real finite-dimensional spaces, acute pairs below `π/3`, transporters, and unitarily invariant seminorms.

`DavisKahan/FiniteDimensional/DirectRotation/ShortRotationCounterexample.lean` — `DavisKahanProposition4_4_Finite` (exact declaration header; proof body omitted):

```lean
def DavisKahanProposition4_4_Finite : Prop :=
```

**`projectionDifference_uiNorm_le_displacement`.** For every admissible transporter and invariant seminorm, projection difference is a lower bound for **full** displacement with no small-angle assumption.

`DavisKahan/FiniteDimensional/DirectRotation/ProjectionDisplacement.lean` — `projectionDifference_uiNorm_le_displacement` (exact declaration header; proof body omitted):

```lean
theorem projectionDifference_uiNorm_le_displacement
    (N : UnitarilyInvariantSeminorm 𝕜 E E)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (W : E ≃ₗᵢ[𝕜] E) (hmap : U.map W.toLinearMap = V) :
    N (U.starProjection.toLinearMap - V.starProjection.toLinearMap) ≤ N (LinearMap.id -
        W.toLinearMap) :=
```

