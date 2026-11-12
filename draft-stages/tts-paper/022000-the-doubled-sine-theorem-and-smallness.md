# 022000 — The doubled-sine theorem and smallness

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** tangent-double-angle. **Audience:** the sine-theta theorem and Proposition 6.1; the squared direct rotation and mirrored subspaces; off-diagonal perturbations and reflections.

<!-- BEGIN SPOKEN LECTURE -->

The doubled-sine theorem and smallness

The third headline theorem of the Davis–Kahan paper bounds the sine of twice the angle. It differs from the sine-theta theorem not only in its conclusion but in where its gap sits: it needs no hypothesis on the trial operator at all, only that the two blocks of the perturbed operator itself are separated. Its proof is a reflection argument, and its weakness is the branch ambiguity of doubled angles. Theorem 8.2 removes that weakness when the perturbation is small.

Here is what we will establish. First, the statement: if the perturbed operator A plus H has a reducing decomposition whose blocks satisfy an interval and exterior gap, with the spectrum of Lambda zero in an interval and the spectrum of Lambda one outside it enlarged by delta, then delta times the size of the sine of two Theta is at most twice the size of H, and delta times the size of the sine of two Theta zero is at most twice the size of the residual. Second, the proof: reflect the perturbation through the reference subspace; the reflected operator has the mirrored exact subspace with the same blocks, the two exact subspaces meet at twice the original angle, and the symmetric sine theorem applied to the pair gives the bound. Third, the constant is sharp: for a two by two off-diagonal perturbation, both sides are equal. Fourth, Theorem 8.2: if in addition the norm of H, or of the residual, is less than half of delta, and the reference block lies within half of delta of the exact block's interval, then every angle is strictly less than forty-five degrees, so a small doubled sine means a small angle.

The statement

Let A be self-adjoint with a reducing subspace, the reference or trial subspace, with projection P and blocks A zero and A one. Let A plus H be self-adjoint, on the same domain as A, with a reducing subspace, the exact subspace, with projection Q and blocks Lambda zero and Lambda one. Assume, for an interval from beta to alpha and a positive delta, that the spectrum of Lambda zero lies in the interval, and the spectrum of Lambda one does not meet the open interval from beta minus delta to alpha plus delta.

Then, for every unitarily invariant norm: delta times the norm of the sine of two Theta is at most twice the norm of H, where Theta is the full angle between the reference and exact subspaces. And with the residual R equal to A plus H, times E zero, minus E zero A zero, which is H E zero, delta times the norm of the sine of two Theta zero is at most twice the norm of R.

Two features are worth noticing immediately. The gap compares the two blocks of the perturbed operator, the wanted block against the unwanted one, and says nothing about the trial operator A zero. And the conclusion concerns twice the angle, whose sine is small both near zero and near ninety degrees.

The reflection argument

Let J be the reflection through the reference subspace, two P minus the identity. As in the study of off-diagonal perturbations, J commutes with A, since A is block diagonal relative to P, and conjugating H by J keeps its diagonal blocks and negates its off-diagonal block B. So J times A plus H, times J, equals A plus J H J, an operator in which the coupling between the reference subspace and its complement has the opposite sign.

Because J is unitary, A plus J H J is just A plus H seen in a mirror. Its exact subspace is the mirror image of Q, the reflection of the exact subspace through the reference subspace, call it Q minus. And its blocks on Q minus and its complement are unitarily equivalent to Lambda zero and Lambda one. So A plus J H J satisfies the same gap condition, with the same delta.

Now compare the two operators A plus H and A plus J H J directly. Their difference is H minus J H J, which consists of the off-diagonal part of H, doubled. By the pinching lemma, the off-diagonal part of H has every norm at most that of H, so the difference has every norm at most twice the norm of H.

Each operator has an exact subspace: Q for the first, Q minus for the second. The symmetric sine theorem, Proposition 6.1, applies to this pair of operators and subspaces. Its two gap conditions ask that the wanted block of one operator be separated from the unwanted block of the other, in both directions. Here both are the gap between Lambda zero and Lambda one, which holds by hypothesis. So delta times the sine of the angle between Q and Q minus is at most the norm of the difference, H minus J H J.

The last step is geometry. What is the angle between the exact subspace and its mirror image? In the plane, if Q is the line at angle theta above the reference axis, its mirror image is the line at angle theta below. The angle between them is two theta, if two theta is at most ninety degrees, and one hundred eighty minus two theta otherwise. Either way, the sine of that angle is the sine of two theta. In general, the square of the direct rotation from P to Q carries Q minus onto Q, and by the half-angle calculation in its block form, the sine of the angle operator between Q minus and Q is the sine of two Theta. Combining, delta times the norm of the sine of two Theta is at most the norm of H minus J H J, which is at most twice the norm of H.

The residual version comes from the same argument restricted to the trial side: the directed sine of twice the angle on the trial coordinates is controlled by the off-diagonal block of H minus J H J, which is twice B, and B is the complementary part of the residual. So delta times the norm of the sine of two Theta zero is at most twice the norm of R.

Sharpness

Take the plane, with A diagonal with entries zero and two, and H with zeros on the diagonal and one half off the diagonal. The perturbed operator has eigenvalues one minus the square root of five fourths and one plus the square root of five fourths, about minus zero point one two and two point one two. Its lower eigenvector makes an angle theta with the horizontal axis whose doubled tangent is one half, so theta is about thirteen point three degrees and the sine of two theta is about zero point four four seven.

The gap between the two perturbed eigenvalues is about two point two four. Delta times the sine of two theta is two point two four times zero point four four seven, which is one. And twice the norm of H is one. The bound is an equality. The residual, H applied to the horizontal unit vector, is the vector zero, one half, so twice its norm is also one, and the residual form is an equality too. For two by two off-diagonal perturbations this happens at every coupling strength: the doubled-sine bound with the factor two is exact.

Why the factor two matters

The factor two cannot be removed from the residual form, and the paper's own example shows it. Let A be diagonal with entries zero and d, for any positive d, and let H have first row zero, one and second row one, minus d. Then A plus H has zeros on the diagonal and ones off the diagonal, with eigenvalues one and minus one and eigenvectors along the diagonals. The angle between the horizontal reference axis and either diagonal is forty-five degrees, so the sine of twice it is one. The gap between the perturbed blocks, one and minus one, is two. The residual H E zero is the vector zero, one, of length one. So delta times the sine of two Theta zero is two, which equals twice the residual, with no room to spare.

The same example shows why the gap must sit on the perturbed blocks. The reference operator's own gap is d, which can be as large as we like. If one mistakenly used d in place of delta, the left side, d times the sine of two theta, would grow without bound while twice the residual stays two. The doubled-sine theorem's gap is the separation of the exact blocks of the perturbed operator, and no other.

Smallness selects the branch

The branch ambiguity is real. With H equal to zero, A equal to the diagonal matrix with entries minus one and one, and the reference subspace the horizontal axis, the vertical axis is also a reducing subspace of A plus H. If it is chosen as the exact subspace, the angle is ninety degrees, the sine of twice it is zero, and the doubled-sine bound holds trivially.

Theorem 8.2 adds two hypotheses to exclude this. First, the perturbation or the residual is small: its operator norm is less than half of delta. Second, the reference block A zero has spectrum within half of delta of the exact block's interval, that is, in the interval from beta minus delta over two to alpha plus delta over two. Under these hypotheses the conclusion of the doubled-sine theorem holds, and in addition every angle is strictly less than forty-five degrees.

In the example with the vertical axis chosen, the exact block Lambda zero is one, so its interval is the single point one, and delta is at most two, the distance to the other eigenvalue. The reference block A zero is minus one, at distance two from that interval, which is more than half of delta. The second hypothesis fails, and the wrong branch is excluded. With the horizontal axis chosen instead, everything is consistent and the angle is zero.

The proof follows a path of operators. For sigma between zero and one, let A of sigma be A plus H, minus sigma times H. At sigma equal to zero this is A plus H, and at sigma equal to one it is A. Because the norm of H is less than half of delta, the spectral band near the interval from beta to alpha stays separated from the rest of the spectrum along the whole path, so the spectral projection Q of sigma for that band varies continuously. Measure the angles between the fixed exact subspace Q, at sigma equal to zero, and Q of sigma. At sigma equal to zero they are all zero. The difference between A plus H and A of sigma is sigma times H, so the doubled-sine theorem, with the gap delta of A plus H, gives the sine of twice each angle at most two sigma times the norm of H over delta, which is less than one. So each angle is either at most one half the arc sine of that quantity, below forty-five degrees, or at least ninety degrees minus that amount. The angles start at zero and move continuously with sigma, and they cannot cross the forbidden band around forty-five degrees. At sigma equal to one, Q of one is the spectral subspace of A for the band, which by the placement hypothesis on A zero is the reference subspace, and its angles from Q are therefore all below forty-five degrees.

The residual version reduces to the perturbation version. Given only a bounded residual on the reference subspace with norm less than half of delta, one can construct a bounded self-adjoint perturbation of norm at most that of the residual which produces the same residual and the same exact blocks, and then apply the argument above.

In the two by two example with coupling one half, the norm of H is one half, which is less than half of delta, about one point one two, and the reference block zero lies within delta over two of the exact block, about minus zero point one two. So Theorem 8.2 applies, and indeed the angle, thirteen point three degrees, is on the acute branch.

Davis and Kahan close Section 8 by noting that the doubled-sine theorem extends to a trial subspace of smaller dimension than the exact subspace, in the manner of Theorem 6.1, while no corresponding extension of the doubled-tangent theorem was known.

To summarize. If the two blocks of the perturbed operator are separated by delta in the interval and exterior shape, then delta times the size of the sine of two Theta is at most twice the size of H, and delta times the size of the sine of two Theta zero is at most twice the size of the residual. The proof reflects H through the reference subspace, observes that the reflected operator has the mirrored exact subspace with the same gap, and applies the symmetric sine theorem to the two operators, whose difference is twice the off-diagonal part of H, and whose exact subspaces meet at twice the original angle. The factor two is attained, both for two by two off-diagonal perturbations and for the paper's example with gap two and angle forty-five degrees. Theorem 8.2 adds smallness, the norm of H or R below delta over two, and a placement condition on A zero, and concludes that all angles are below forty-five degrees, by continuity along a path from A to A plus H.

The doubled-sine theorem needs no information about the trial operator's spectrum, which makes it useful when only the perturbed operator's separation is known. Without smallness, though, its conclusion cannot distinguish a nearly correct subspace from a nearly perpendicular one.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Statement (S2-sin-two-theta)

\(A,\widehat A=A+H\) self-adjoint on a common domain; \(\sigma(\Lambda_0)\subseteq[\beta,\alpha]\), \(\sigma(\Lambda_1)\cap(\beta-\delta,\alpha+\delta)=\varnothing\):
\[
\delta N(\sin2\Theta)\le2N(H),\qquad\delta N(\sin2\Theta_0)\le2N(R),\quad R=\widehat AE_0-E_0A_0=HE_0 .
\]

### Proof (Section 7)

\(J=P-P^\perp\): \(A+JHJ\sim\begin{pmatrix}A_0+H_0&-B^*\\-B&A_1+H_1\end{pmatrix}\) (7.1); \((A+H)U^2=U^2(A+JHJ)\) (7.3); \(U^2\sim\begin{pmatrix}\cos2\Theta_0&-J_0^*\sin2\Theta_1\\J_0\sin2\Theta_0&\cos2\Theta_1\end{pmatrix}\) (7.4); \(\delta N(\sin2\Theta)\le N(H-JHJ)\le2N(H)\) (7.5), with \(H-JHJ=2\begin{pmatrix}0&B^*\\B&0\end{pmatrix}\).

### Examples

- **Sharp 2×2:** \(A=\operatorname{diag}(0,2)\), \(H=\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix}\): \(\sigma(\widehat A)=1\pm\sqrt{5/4}\), \(\theta\approx13.28^\circ\), \(\sin2\theta=1/\sqrt5\), \(\delta=\sqrt5\), \(\delta\sin2\theta=1=2\|H\|=2\|R\|\). Generally, \(A=\operatorname{diag}(0,2c)\), \(H=h\sigma_x\): \(\delta\sin2\theta=2h\).
- **Source example (Section 7):** \(A=\operatorname{diag}(0,d)\), \(H=\begin{pmatrix}0&1\\1&-d\end{pmatrix}\), \(A+H=\sigma_x\): \(\delta=2\) (perturbed blocks \(\pm1\)), \(\theta=\pi/4\), \(\|R\|=\|B\|=1\), \(\delta\sin2\theta_0=2=2\|R\|\); using the reference gap \(d\) would give \(d\sin2\theta_0=d\) unbounded.

**Note on the 1970 proof.** The residual line of the Section 7 proof concludes \(\delta\|\sin2\Theta_0\|\le\|B\|\le\|R\|\), dropping the factor 2 that \(H-JHJ=2\,\mathrm{offdiag}(B)\) carries; the source example above attains \(2=2\|R\|\). The stated theorem (Section 2) has the factor 2 and is correct; the formal theorem `sinTwoTheta_commonDomain_whereDefinedUIN_rclike` proves it.

### Theorem 8.2

Add \(\|H\|_{\rm op}<\delta/2\) or \(\|R\|_{\rm op}<\delta/2\), \(\sigma(A_0)\subseteq[\beta-\delta/2,\alpha+\delta/2]\), \(\dim D_0=\dim D_1\): the double-angle bound holds and \(\Theta<\pi/4\). Homotopy \(A(\sigma)=A+H-\sigma H\), \(\gamma=\|H\|\): close parameters satisfy \(\theta(\sigma)\le\tfrac12\arcsin(2\sigma\gamma/\delta)\le\tfrac\pi2\sigma\gamma/\delta<\pi/4\). Residual case: bounded self-adjoint completion \(K\) with \(\|K\|\le\|R\|\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/SinTwoThetaCommonDomain.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
theorem sinTwoTheta_commonDomain_whereDefinedUIN_rclike
    [TopologicalSpace.SeparableSpace E]
    (N : NormalizedSymmetricOperatorIdealFamily.{u, v} K)
    {A T : E →ₗ.[K] E} (hA : IsSelfAdjoint A) (hT : IsSelfAdjoint T)
    (hdom : T.domain = A.domain)
    {P Q : Submodule K E} [P.HasOrthogonalProjection] [Q.HasOrthogonalProjection]
    (hP : _root_.LinearPMap.IsReducing A P)
    (hQ : _root_.LinearPMap.IsReducing T Q)
    {gap : Real} (hgapPos : 0 < gap)
    (hgap : FormBoundedSylvesterGap
      (TauCeti.LinearPMap.reducingRestriction T Q hQ)
      (TauCeti.LinearPMap.reducingRestriction T Q.orthogonal hQ.orthogonal) gap) :
    (∀ R : P →L[K] E,
      (∀ p : P, ∀ hp : (p : E) ∈ T.domain,
        T (⟨(p : E), hp⟩) = A (⟨(p : E), by rw [← hdom]; exact hp⟩) + R p) ->
      N.Mem (Angle.directedSinTwoAngleOperator P Q) → N.Mem R ->
        gap * N.gaugeReal (Angle.directedSinTwoAngleOperator P Q) ≤ 2 * N.gaugeReal R) ∧
    (∀ Hop : E →L[K] E, Hop.IsSymmetric ->
      T = TauCeti.LinearPMap.addBounded A Hop ->
      N.Mem (Angle.sinTwoAngleOperator P Q) → N.Mem Hop ->
        gap * N.gaugeReal (Angle.sinTwoAngleOperator P Q) ≤ 2 * N.gaugeReal Hop)
```

Lean's `T` is \(A+H\). The gap predicate is on the two reducing restrictions of `T` (the perturbed blocks \(\Lambda_0,\Lambda_1\)); note that the formal gap predicate also admits the ordered configurations. Theorem 8.2: `Section8.theorem8_2_sinTwoTheta_perturbation_symmetricNorming`, `Section8.theorem8_2_sinTwoTheta_residual_symmetricNorming`, `Section8.theorem8_2_branch_directed_complex` (and real variants).
