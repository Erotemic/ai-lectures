# 021000 — The tangent-theta theorem

**Track:** G3 audio paper track. **Draft:** adapted from G2 lecture 112000. **Section:** angle-theorems. **Audience:** prior linear algebra and basic analysis.

<!-- BEGIN SPOKEN LECTURE -->

# The single-angle tangent theorem

Imagine approximating a horizontal eigenvector by a tilted line. At thirty degrees, the line has a modest slope. At eighty-nine degrees, its vertical component is still at most one, but its slope is enormous. Measuring only the sine of the angle cannot express that growth very well.

The tangent theorem asks whether an operator residual and a spectral gap control the slope itself. To define that slope, projecting the trial line back onto the horizontal axis must never erase a nonzero trial vector. For subspaces, this is the transversality requirement: the trial space must not contain a direction entirely in the exact orthogonal complement.

We will see that a suitable ordered gap between Ritz values and the unwanted exact spectrum both guarantees transversality and gives a sharp tangent estimate. The proof needs one additional geometric step beyond the sine theorem: Galerkin orthogonality supplies the cosine factor that turns a sine estimate into a tangent estimate.

## Fix the setting

Let A be a self-adjoint operator on a finite-dimensional real or complex inner-product space H. Let U be an A-invariant subspace. Because A is self-adjoint, its orthogonal complement is also invariant.

Let E be an isometry from a trial-coordinate space F into H. Write V for its range. Compress A to F to form the Ritz operator M, equal to E adjoint A E. Define the Ritz residual R by A E minus E M. Galerkin orthogonality says E adjoint R is zero.

We assume the spectrum of M and the spectrum of A restricted to the unwanted complement are separated in an ordered way. To fix an orientation, suppose every Ritz eigenvalue is at most alpha, while every complementary eigenvalue is at least alpha plus delta, for some positive delta. Reversing the order gives the analogous result.

These are concrete hypotheses: they compare the computed Ritz spectrum with the exact unwanted spectrum, not merely the two blocks of A with one another.

The theorem says that delta times a unitarily invariant norm of the directed tangent is at most the same norm of the residual. It also proves the transversality needed for that tangent to represent actual principal angles.

## Why the ordered gap matters

Recall the complementary coordinate maps. C extracts the component of a trial vector inside U, and S extracts its component in U perpendicular. Since E is an isometry, the squared moduli satisfy cosine squared plus sine squared equals the identity on F.

The source's coordinate tangent is S followed by the inverse of the positive cosine magnitude. In finite dimensions one can define a Moore–Penrose inverse even when the cosine is singular. But totalizing a formula does not make a ninety-degree angle finite. We need to establish that the cosine magnitude has no kernel.

Suppose a nonzero trial vector E y lies entirely in U perpendicular. Since A leaves U perpendicular invariant, its Rayleigh quotient is at least alpha plus delta. On the other hand, the same Rayleigh quotient equals the Rayleigh quotient of M at y, which is at most alpha, because M is the Ritz compression.

Those two statements contradict one another. Therefore V has zero intersection with U perpendicular. This is the elementary transversality proof. In equal finite dimensions it also makes the horizontal projection invertible, so V is a graph over U. Without equal dimensions, the source uses a directed coordinate tangent rather than claiming an everywhere-defined graph over all of U.

## The residual equation is still present

Let F one be an isometric coordinate map onto U perpendicular, and let Lambda one represent A on that space. Define X equal to F one adjoint E. Exactly as in the sine theorem, the complementary residual equation is Lambda one X minus X M equals F one adjoint R.

An ordered spectral gap allows a constant-one Sylvester estimate on X. That immediately bounds the sine, since X has the same positive modulus as S. But the tangent is larger than the sine. Dividing by cosine without another argument would create an uncontrolled factor.

Choose a principal trial direction y with maximal unwanted overlap. Call its sine s and its cosine c. The sine measures how much lies outside the exact space; the cosine measures how much remains inside.

Call the outside component v. It has length s, and its trial-space projection is s squared times y. This principal-vector identity supports the residual estimate.

The corrected test vector has length c. Dividing by that positive cosine turns the sine into the tangent. The argument requires c greater than zero.

Pair the residual R y with v. The unwanted block of A contributes at least alpha plus delta times s squared. The Ritz term contributes at most alpha times s squared. Therefore the real part of this pairing is at least delta times s squared.

To locate that square, write the complementary component as s times a unit unwanted vector w. The inner product with v has two factors of s: one from each copy of the complementary component. The spectral gap bounds their coefficient difference. This is why the gap estimate begins with s squared, even though the final conclusion concerns the ratio s over c.

Now use Galerkin orthogonality: R y is perpendicular to the entire trial space. We may replace v in the inner product by its projection perpendicular to the trial space. The squared length of that projected vector is s squared minus s to the fourth power, so its length is s times c.

If rho bounds the operator norm of R, Cauchy–Schwarz gives delta times s squared at most rho times s times c. For s positive, divide by s. We obtain delta times s at most rho times c. Since c is positive by transversality, divide again to obtain delta times tangent theta at most rho.

Choosing a largest singular value proves the operator-norm tangent estimate. Notice how the factor c appears from Galerkin orthogonality. Merely applying the earlier sine theorem would not have produced it.

For the full unitarily invariant norm statement, the proof must control every leading singular-value sum. The finite-dimensional source supplies this through its ordered Ritz-gap theorem and its Ky Fan machinery. An operator-norm argument for only the largest singular value would not by itself prove the nuclear-norm or every other symmetric-gauge statement.

## Watch the theorem become equality in the plane

Take A diagonal with entries zero and five. Let U be the horizontal axis, and take a trial unit vector with coordinates cosine theta and sine theta, where theta is strictly between zero and ninety degrees.

The Ritz value M is five sine squared theta. The unwanted complementary eigenvalue is five. Therefore the actual ordered gap is five cosine squared theta.

Apply A to the trial vector. Subtract the Ritz value times the same vector. The resulting Ritz residual is five sine theta cosine theta times a unit vector perpendicular to the trial line. Its length is five sine theta cosine theta.

In coordinates, that perpendicular unit vector has horizontal entry negative sine theta and vertical entry cosine theta. The residual has exactly this direction. The unwanted vertical unit vector, after its trial-space projection is subtracted, equals cosine theta times the same perpendicular unit vector. Thus the Cauchy–Schwarz step in the proof is equality for this example: the residual and the corrected test vector point in the same direction.

The directed tangent is tangent theta. Multiply it by the gap: five cosine squared theta times tangent theta equals five sine theta cosine theta. That is exactly the residual length.

So the inequality is equality for every acute theta. This is a sharpness example, with the correct Ritz gap and the correct Ritz residual used consistently.

Notice the difference from the sine theorem's earlier example. There we fixed the trial operator at zero, and the residual had norm five sine theta. Here the Ritz operator follows the trial line, so both the residual and the relevant gap change with theta.

## The behavior near a right angle

As theta approaches ninety degrees, the tangent tends to infinity. Does that contradict a bounded residual? No. In our example the Ritz eigenvalue approaches five, the unwanted eigenvalue. Thus the ordered gap tends to zero at the same time.

The theorem's product remains equal to the residual. We cannot hold the old gap of five fixed while allowing the Ritz value to move toward five.

This also explains why a uniform positive ordered gap implies transversality. If the cosine vanished in any direction, the corresponding Ritz quotient would enter the unwanted spectral region. The gap excludes that possibility.

The tangent theorem therefore provides a stronger geometric conclusion than a sine bound, but only under a more structured comparison involving the Ritz spectrum.

## Operator norms, Frobenius norms, and arbitrary gauges

In operator norm, the result controls the worst principal slope. If the largest tangent is at most rho divided by delta, every principal angle is at most the arctangent of rho over delta. This angle bound remains strictly below ninety degrees for every finite rho.

In Frobenius norm, the squares of all directed tangents add. The theorem limits the aggregate squared slope by the squared residual length after scaling by delta.

For a Ky Fan norm, the estimate bounds the sum of the largest several tangent singular values. The all-prefix inequalities matter because a largest-singular-value estimate alone does not control their sum. For example, two singular values equal to one each have the same maximum as the pair one and zero, but a different sum. General unitarily invariant norms follow after the prefix comparisons have been proved.

The source's exact theorem assumes an isometric trial frame and the Ritz identity. More general trial frames can be normalized, but the normalization and their lower bounds must be stated, rather than simply reusing the isometric formula.

## What this theorem does not say

It does not state that arbitrary pairwise-separated spectra supply the same constant-one estimate in every norm. It does not identify the graph of V over all of U when the dimensions do not match. And it does not allow a zero cosine to be treated as an ordinary finite tangent just because a Moore–Penrose inverse exists.

Doubled-angle bounds instead arise from reflection identities and different spectral-gap configurations. Their conclusions cannot be substituted for the directed tangent estimate without checking the corresponding branch and norm hypotheses.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

Let `E : F →ₗᵢ[𝕜] H`, `M = E* A E`, `R = A E - E M`, and let `U` reduce self-adjoint `A`. If the Ritz spectrum lies on one side of `A|Uᗮ` with ordered gap `δ > 0`, the source concludes both `Disjoint (range E) Uᗮ` and, for every rectangular unitarily invariant seminorm `N`,

\[\delta\,N(\mathrm{tanThetaEmbedding}(U,E))\leq N(R).\]

The source's totalized tangent uses a Moore–Penrose inverse, but its singular-value interpretation as principal tangents is justified by the separate transversality theorem. In the planar Ritz example `A=diag(0,5)`, `M=5sin²θ`, `δ=5cos²θ`, and `‖R‖=5sinθcosθ=δtanθ`.

**The planar cosine gain as a vector identity.** Write \(s=\sin\theta\), \(c=\cos\theta\), \(u=(c,s)^\top\), and \(w=(-s,c)^\top\). For \(A=\operatorname{diag}(0,5)\),
\[
 M=5s^2,\qquad r=Au-uM=5sc\,w,\qquad \delta=5c^2.
\]
If \(e_2=(0,1)^\top\), then \(P_{\operatorname{span}(u)}e_2=su\) and \(e_2-su=cw\). Consequently
\[
 \langle r,e_2\rangle=5sc^2=\delta s
 \quad\text{and}\quad
 \|r\|\,\|e_2-su\|=(5sc)c=\delta s.
\]
The Galerkin projection removes a vector of length \(s\) from the test direction, leaving length \(c\). Division by \(c^2\) in the gap and by \(c\) in this pairing yields \(\delta\tan\theta=\|r\|\).

### Source declaration excerpts

`DavisKahan/FiniteDimensional/Residual/AngleEmbeddings.lean` — `isTransverse_of_orderedRitzGap` (exact declaration header; body omitted):

```lean
theorem isTransverse_of_orderedRitzGap
    {A : E →ₗ[𝕜] E} (hA : A.IsSymmetric) {U : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A))
    (X : F →ₗᵢ[𝕜] E) {M : F →ₗ[𝕜] F} (hM : M.IsSymmetric)
    (hGalerkin : M = compression A X)
    {δ : ℝ} (hδ : 0 < δ) (hgap : OrderedGap M ⊤ A Uᗮ δ) :
    Disjoint (approximateSubspace X) Uᗮ := by
```

`DavisKahan/FiniteDimensional/Residual/AngleEmbeddings.lean` — `tanThetaEmbedding_residual_le_of_orderedGap` (exact declaration header; body omitted):

```lean
theorem tanThetaEmbedding_residual_le_of_orderedGap
    (N : UnitarilyInvariantSeminorm 𝕜 F E)
    {A : E →ₗ[𝕜] E} (hA : A.IsSymmetric) {U : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] (hU : (U ∈ Module.End.invtSubmodule A))
    (X : F →ₗᵢ[𝕜] E) {M : F →ₗ[𝕜] F} (hM : M.IsSymmetric)
    (hGalerkin : M = compression A X)
    {δ : ℝ} (hδ : 0 < δ) (hgap : OrderedGap M ⊤ A Uᗮ δ) :
    δ * N (tanThetaEmbedding U X) ≤ N (residual A X M) := by
```

`DavisKahan/FiniteDimensional/Residual/AngleEmbeddings.lean` — `singularValues_graphOperator` (exact declaration header; body omitted):

```lean
theorem singularValues_graphOperator (U : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] (X : F →ₗᵢ[𝕜] E)
    (htrans : Disjoint (approximateSubspace X) Uᗮ) :
    (graphOperator U X).singularValues =
      (approximateSubspace X).principalTangents U := by
```

**Mapping.** `hGalerkin` fixes `M` as the Ritz compression; `OrderedGap M ⊤ A Uᗮ δ` compares its spectrum with the unwanted exact complement. `tanThetaEmbedding` is a map from trial coordinates to the ambient space, not an arbitrarily chosen graph map on all of `U`. The transversality theorem gives the angle interpretation; the norm theorem supplies the constant-one bound in each registered rectangular unitarily invariant seminorm.
