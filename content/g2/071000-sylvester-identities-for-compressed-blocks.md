# 071000 — Sylvester identities for compressed blocks

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `021000` Rayleigh–Ritz compression; `030000` spectral projections; `043000` directed sines; `062000–070000` Sylvester equations. **Next:** `072000` infinite-dimensional Hilbert examples.

<!-- BEGIN SPOKEN LECTURE -->

# Where the Sylvester unknown comes from in subspace geometry

Imagine trying to estimate the error in a spectral subspace. You know an operator, a perturbed operator, and some spectral information, but the quantity you want is an angle between two subspaces. It is not obvious why an equation of the form A X minus X B should appear.

The key is to find a map X that literally measures how much a vector in one subspace leaks outside the other. Once we project the operator equation onto the right spaces, that leakage map satisfies a Sylvester equation. We can then divide the projected residual by a spectral gap.

We will derive the identity before estimating it, and check every piece in a two-dimensional example.

## Choose the two spectral subspaces

Let T be a bounded self-adjoint operator on a Hilbert space. Let P be an orthogonal projection onto one of its reducing subspaces. Reducing means T preserves the selected subspace and also its orthogonal complement, or equivalently T commutes with P.

Now let S be another bounded self-adjoint operator, with S equal to T plus a perturbation E. Let Q project onto a reducing subspace of S.

Call the range of P the old selected space and the range of Q the new selected space. We want to know how far a unit vector from the old space can fall outside the new one.

Take such a vector p. Project it onto the orthogonal complement of Q. This is the part of p that misses the new space. The map performing that operation, restricted to the old space, is our unknown X.

Its operator norm is the largest length of this missed component over unit vectors in the old selected space. For finite-dimensional equal-rank subspaces, it is the sine of the largest principal angle. More generally, it is the directed sine from the old space to the new one.

## Compress the operators to the right sides

X sends an old selected vector into the complement of the new selected space. So the left coefficient of our Sylvester equation must act on that complement, and the right coefficient must act on the old selected space.

Let A be S restricted to the orthogonal complement of Q. This is legitimate because Q reduces S. Let B be T restricted to the range of P, which is legitimate because P reduces T.

The residual should be a map from the old selected space to the new complement, just like X. We will see that it is the perturbation E, first restricted to the old space and then projected outside Q.

Notice the roles. X measures leakage; A and B describe the spectral pieces we need to separate; E is the known change in the original operator.

## Derive one projected identity

Take a vector p in the range of P. Apply X: the result is p projected outside Q. Apply A: because S commutes with Q, this is the same as applying S to p and then projecting outside Q.

Now apply B to p first. B is just T acting within the old selected subspace. Applying X afterward projects T p outside Q.

Subtract those two results. The projected S p and projected T p differ by the projection of S minus T, applied to p. Since S minus T is E, we get the projection of E p outside Q.

That is the whole algebraic argument. In operator language, A X minus X B equals the restriction of I minus Q, followed by E, to the range of P. The identity has the correct input and output spaces on both sides.

We did not use a small perturbation or a spectral gap. Those hypotheses enter only when we decide how to estimate X from this exact equation.

## Compute a complete two-dimensional example

Let T be diagonal with values zero and two. The old selected subspace is the horizontal coordinate axis, so P projects onto that axis.

Let S be the matrix whose four entries are all one. It has eigenvalue zero on the diagonal line pointing down and right, represented by the vector one, negative one. It has eigenvalue two on the other diagonal, represented by one, one. Choose Q as the projection onto the zero eigenspace of S.

Start with the unit vector e-one along the old horizontal axis. Its component outside Q lies on the up-right diagonal. That component is the vector one half, one half, whose length is one over the square root of two.

Thus X has norm one over the square root of two. It is exactly the directed sine of a forty-five-degree angle between the old horizontal line and the new down-right diagonal line.

Next identify the compressed coefficients. On the new complement, S acts as multiplication by two. On the old selected line, T acts as multiplication by zero. So A X minus X B is simply twice X.

Compute E as S minus T. Applied to e-one, E produces the vector one, one. That is already in the new complement. Its length is the square root of two. Twice the length of X is also the square root of two.

Every part of the compressed Sylvester identity agrees. The restricted spectral gap is two, the residual has norm the square root of two, and the exact sine of the angle is one over the square root of two. The constant-one inequality holds with equality here.

## What gap must actually be checked?

The two compressed spectra in the example are zero, from the old selected piece of T, and two, from the complementary piece of S. The gap is between those two particular pieces.

It would make little sense to demand that the *entire* spectra of T and S be disjoint. In this example they both have zero and two as eigenvalues. Yet the useful compressed spectral blocks are separated.

If the compressed spectra are ordered, the semigroup estimate gives delta times the operator norm of X at most the projected residual norm. If they are merely pairwise separated, the Hilbert-Schmidt argument controls the corresponding square norm, and the operator-norm estimate may have a different constant.

This is why a sine-theta theorem must state exactly which selected cluster is separated from which complementary cluster, and in which norm.

## The opposite directed leakage

We can reverse the question. Start with a vector in the new selected space and ask how much of it lies outside the old selected space. The corresponding map projects a vector from the range of Q onto the complement of P.

Applying the same derivation with the roles of S and T exchanged produces a second Sylvester equation, with the corresponding projected negative perturbation.

For two one-dimensional lines, the directed sine is the same in both directions. In higher dimensions, unequal ranks and right-angle defects can make the two directed errors different. A bound on one direction does not automatically control the other unless a separate geometric argument applies.

The two crossed maps are therefore separate pieces of information in an ambient projection estimate.

## The trial-subspace version

A closely related identity works even when our trial subspace is not invariant. Suppose V embeds a finite-dimensional coordinate space isometrically into the Hilbert space. Its columns form an orthonormal trial frame.

Let M be the compression V adjoint T V. This is the matrix of the trial operator in the chosen coordinates. Define the residual R to be T V minus V M. The residual measures the part of the action of T that the trial compression does not reproduce.

Let Q now be an exact reducing spectral projection of T. Our leakage map X is V followed by projection outside Q. The left coefficient is T restricted to that exact complement, and the right coefficient is the finite matrix M.

Apply the same projected subtraction. We obtain A X minus X M equal to the projection of R outside Q.

Here is a quick numerical check. Let T again be diagonal with values zero and two. Take a unit trial vector making thirty degrees with the horizontal zero-eigenvector. Its compression M is one half. Its leakage into the vertical complementary eigenspace has length one half.

The difference between the exact exterior eigenvalue two and the trial compression one half is one and a half. The exterior component of the residual has length three quarters. Multiplying the gap one and a half by the leakage one half gives precisely three quarters.

The full residual is larger because it also has a component along the exact zero eigenspace. It is the projected exterior residual that appears in the identity. A bound using the full residual is valid but may lose sharpness.

## Domain boundaries in infinite dimensions

If T or S is unbounded, a spectral projection may preserve the operator's domain in the proper spectral-theoretic sense, but that must be established. We cannot apply T to an arbitrary vector merely because the vector lies in its ambient Hilbert space.

A domain-aware proof begins on vectors for which every composition is defined. It may use bounded spectral windows to control the operators and extend a bounded identity after proving continuity. The compressed left and right operators must have stated domains, and the range of X must meet those domains wherever the Sylvester expression is evaluated.

For bounded self-adjoint operators the derivation is elementary projection algebra. Its value is that it shows which object an angle theorem must estimate: a cross-projection map satisfying an exact Sylvester equation, whose right-hand side is a projected perturbation or Ritz residual. Spectral separation supplies the inequality only after that geometry is in place.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

With bounded self-adjoint \(T,S=T+E\), reducing orthogonal projections \(P\) for \(T\) and \(Q\) for \(S\), let \(H_P=\operatorname{ran}P\) and \(H_{Q^\perp}=\operatorname{ran}(I-Q)\). Define
\[
X=(I-Q)|_{H_P}:H_P\to H_{Q^\perp},\quad
A=S|_{H_{Q^\perp}},\quad B=T|_{H_P}.
\]
Then
\[
AX-XB=(I-Q)E|_{H_P},\qquad
\|X\|=\|(I-Q)P\|.
\]
This also has a Rayleigh–Ritz variant: if \(V^*V=I\), \(M=V^*TV\), \(R=TV-VM\), and \(Q\) reduces \(T\), then
\[
(T|_{Q^\perp})[(I-Q)V]-[(I-Q)V]M=(I-Q)R.
\]
The infinite-dimensional Lean source uses domain-aware spectral cuts, and its block identity is more general than the bounded-algebra proof narrated here.

**Projected perturbation worked example.** With
\[
T=\begin{bmatrix}0&0\\0&2\end{bmatrix},\qquad
S=\begin{bmatrix}1&1\\1&1\end{bmatrix},\qquad
E=S-T=\begin{bmatrix}1&1\\1&-1\end{bmatrix},
\]
let \(P=e_1e_1^*\) and \(Q=qq^*\) for
\(q=(1,-1)^\mathsf T/\sqrt2\). Then
\[
Xe_1=(I-Q)e_1=(1/2,1/2)^\mathsf T,\quad
A=\left.S\right|_{Q^\perp}=2,\quad B=\left.T\right|_P=0,
\]
and \(AXe_1-XBe_1=(1,1)^\mathsf T=(I-Q)Ee_1\). Consequently
\(2\|X\|=\sqrt2=\|(I-Q)E|_P\|\) with \(\|X\|=1/\sqrt2\).

**Ritz-residual worked example.** For the same
\(T=\operatorname{diag}(0,2)\), choose
\(v=(\sqrt3/2,1/2)^\mathsf T\), \(V:\mathbb C\to\mathbb C^2\),
\(V(1)=v\), and \(Q=e_1e_1^*\). Then
\[
M=V^*TV=1/2,\quad
R=Tv-vM=(-\sqrt3/4,3/4)^\mathsf T,\quad
X=(I-Q)v=(0,1/2)^\mathsf T.
\]
The restricted exterior operator is \(A=2\), and
\[
AX-XM=(2-1/2)(0,1/2)^\mathsf T=(0,3/4)^\mathsf T
=(I-Q)R,\quad
\|R\|=\sqrt3/2,\quad \|(I-Q)R\|=3/4.
\]
The exact sine of the trial-vector angle is \(1/2\), and the projected
residual gives \((3/2)(1/2)=3/4\) without excess.

**Lean bridge (verified source excerpts).**

`DavisKahan/InfiniteDimensional/SinTheta/Restriction.lean` — `directedPerturbation_sylvesterEquation` (exact source declaration header):

```lean
theorem directedPerturbation_sylvesterEquation
    {A B : E →L[𝕜] E}
    (_hA : A.IsSymmetric) (hB : B.IsSymmetric)
    {U V : Submodule 𝕜 E}
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hU : Submodule.IsReducing U A) (hV : Submodule.IsReducing V B) :
    ContinuousLinearMap.sylvester (B.restrict ((Module.End.mem_invtSubmodule_iff_forall_mem_of_mem
      _).mp hV.orthogonal_mem_invtSubmodule))
      (A.restrict hU.mem_invtSubmodule)
      (((Vᗮ.starProjection ∘L U.subtypeL)).codRestrict Vᗮ
        (fun _x => Vᗮ.starProjection_apply_mem _)) =
      ((Vᗮ.starProjection ∘L (B - A) ∘L U.subtypeL)).codRestrict Vᗮ
        (fun _x => Vᗮ.starProjection_apply_mem _) := by
```

The formal conclusion is the exact compressed perturbation equation; `U` reduces the old `A`, `V` reduces the new `B`, and the projected difference `B - A` is the Sylvester defect.

`DavisKahan/InfiniteDimensional/SinTheta/Restriction.lean` — `directedResidual_sylvesterEquation` (exact source declaration header):

```lean
theorem directedResidual_sylvesterEquation
    {A : E →L[𝕜] E} (hA : A.IsSymmetric)
    {U : Submodule 𝕜 E} [U.HasOrthogonalProjection]
    (hU : Submodule.IsReducing U A)
    {X : F →L[𝕜] E} {M : F →L[𝕜] F} :
    ContinuousLinearMap.sylvester (A.restrict ((Module.End.mem_invtSubmodule_iff_forall_mem_of_mem
      _).mp hU.orthogonal_mem_invtSubmodule)) M
      (((Uᗮ.starProjection ∘L X)).codRestrict Uᗮ (fun _x => Uᗮ.starProjection_apply_mem _)) =
      ((Uᗮ.starProjection ∘L DavisKahan.residual A X M)).codRestrict Uᗮ
        (fun _x => Uᗮ.starProjection_apply_mem _) := by
```

This version uses a trial map `X` and its `DavisKahan.residual` with a trial compression `M`; the exact spectral complement supplies the left restricted operator.
