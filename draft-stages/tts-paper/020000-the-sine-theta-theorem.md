# 020000 — The sine-theta theorem

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sine-theta. **Audience:** the angle operator and its modulus identity; exact decompositions and trial residuals; the three gap shapes; Theorems 5.1 and 5.2; operator-ideal norms.

<!-- BEGIN SPOKEN LECTURE -->

The sine-theta theorem

This is the theorem the paper is built around. Everything in the course so far has been preparation for stating it with all of its hypotheses and proving it in a way a reader can reconstruct. The statement is short: delta times the size of the sine of the angle is at most the size of the residual. The content lies in what the angle is, what the residual is, what delta separates, and which sizes are allowed.

Here is the plan. First, the statement in full, every hypothesis spoken in the form one would check. Second, the proof, as three bridges: from the residual to a Sylvester equation, from the gap to a bound on its solution, and from that solution to the sine of the angle. Third, sharpness: a two-dimensional example in which the inequality is an equality at every angle. Fourth, the perturbation form, where the residual is H E zero, and a warning about the difference between the gap delta and an eigenvalue gap of the original operator. Fifth, how the theorem appears in the journal paper, and what it does not claim.

The statement

The setting is a separable Hilbert space over the real or the complex numbers. On it there is a self-adjoint operator A hat, the operator under study, which may be unbounded.

Trial data. There is a coordinate Hilbert space for the trial subspace, an isometry E zero from it into the ambient space, and a self-adjoint operator A zero on the trial coordinates, which may also be unbounded. E zero maps the domain of A zero into the domain of A hat. There is a bounded operator R from trial coordinates into the ambient space that agrees with A hat E zero minus E zero A zero on the domain of A zero. That is the residual.

Exact data. There are isometries F zero and F one from two coordinate spaces into the ambient space, whose ranges are perpendicular and together fill the space: F zero star F one is zero, and F zero F zero star plus F one F one star is the identity. There is a self-adjoint operator Lambda one on the coordinates of F one. F one maps the domain of Lambda one into the domain of A hat, and A hat F one equals F one Lambda one there. The range of F zero is the exact wanted subspace; P exact is its projection, F zero F zero star.

The angle. The sine of Theta zero is the positive square root of the identity minus E zero star, P exact, E zero, an operator on trial coordinates. Its eigenvalues, when it has them, are the sines of the angles from the trial subspace toward the exact wanted subspace.

The gap. There is a positive number delta, and one of four configurations holds. Either the spectrum of A zero lies in an interval from beta to alpha, and the spectrum of Lambda one does not meet the open interval from beta minus delta to alpha plus delta. Or the same with A zero and Lambda one exchanged. Or, for some number b, A zero is at least b plus delta and Lambda one is at most b, as quadratic forms on their domains. Or A zero is at most b and Lambda one is at least b plus delta.

The norm. N is a normalized symmetric operator-ideal norm with Ky Fan dominance where defined. The operator, Hilbert–Schmidt, trace, Schatten, and Ky Fan norms are examples.

The conclusion. If the sine of Theta zero and the residual R both belong to the ideal of N, then delta times N of the sine of Theta zero is at most N of R.

Notice what is not assumed. The trial operator need not be the Rayleigh–Ritz compression; any self-adjoint A zero works, provided the residual and the gap are formed with that same A zero. The wanted block Lambda zero is never mentioned. The trial and exact subspaces need not have the same dimension. And no assumption is made that the exact subspace is a spectral subspace; it only has to reduce A hat, with the gap condition on Lambda one doing the spectral work.

The proof, in three bridges

The first bridge turns the residual into a Sylvester equation. Let X be F one star E zero: it takes trial coordinates, forms the trial vector, and reads off its coordinates in the unwanted space. Apply F one star to the residual. On the domain of A zero, F one star R equals Lambda one X minus X A zero. For bounded operators this is algebra, using the adjoint of the intertwining identity. For unbounded operators, the duality test shows that X carries the domain of A zero into the domain of Lambda one: pair X x against Lambda one z for z in the domain of Lambda one, move Lambda one across using the intertwining identity and self-adjointness of A hat, and observe that the result is bounded in z.

The second bridge turns the gap into a bound on X. In the interval configurations, shift both operators by the center of the interval. The operator in the interval then has norm at most its half-width a, and the operator outside has a bounded inverse of norm at most one over a plus delta. Theorem 5.1 gives delta times N of X at most N of F one star R. In the ordered configurations, the solution of the Sylvester equation is an integral of e to the minus t times the upper operator, times the right-hand side, times e to the t times the lower operator, whose integrand decays like e to the minus t delta; equivalently, filled spectral cutoffs reduce the problem to bounded operators and Lemma 5.1 passes to the limit. Theorem 5.2 gives the same inequality, now with both A zero and Lambda one possibly unbounded. In every case the estimate is first obtained for each Ky Fan norm and then extended to N by Ky Fan dominance.

Then the contraction law: F one star has norm at most one, so N of F one star R is at most N of R.

The third bridge identifies the size of X with the size of the sine. X star X equals E zero star F one F one star E zero, which is E zero star times the identity minus P exact, times E zero, because F one F one star is the projection onto the complement. That equals the identity minus E zero star P exact E zero, which is the square of the sine of Theta zero. So the modulus of X is the sine of Theta zero, and since a symmetric ideal norm depends only on singular values, N of X equals N of the sine of Theta zero.

Chaining the three: delta times N of the sine of Theta zero equals delta times N of X, which is at most N of F one star R, which is at most N of R. That is the theorem.

The factor in front of N of R is exactly one. It comes from the window or cut geometry of the gap. Under a distance-only gap, the same chain works in the Hilbert–Schmidt norm with factor one, but in the operator norm the factor must be larger.

Sharpness

The constant cannot be improved. Take the plane, with A hat the diagonal matrix with entries zero and delta. Let the exact wanted subspace be the horizontal axis, so F zero is the first coordinate vector, F one the second, and Lambda one is the number delta. For an angle theta between zero and ninety degrees, let the trial vector be cosine theta, sine theta, and take the trial operator A zero to be zero. The interval configuration holds: zero lies in the interval from zero to zero, and delta lies outside the open interval from minus delta to delta.

The residual is A hat applied to the trial vector minus zero, which is the vector zero, delta times sine theta. Its length is delta sine theta. The sine of the angle from the trial line to the horizontal axis is sine theta. So delta times sine theta is at most delta times sine theta, with equality, at every angle. Davis and Kahan note that orthogonal direct sums of such planar examples give equality simultaneously in every unitarily invariant norm.

Notice that A zero equal to zero is not the Rayleigh–Ritz value of the trial vector unless theta is zero. The Rayleigh quotient would be delta sine squared theta, which gives a shorter residual and a smaller separation, delta cosine squared theta. In the paper's figure, with A hat the diagonal matrix with entries one point nine and zero point seven and the trial vector at forty degrees, the Rayleigh quotient is about one point four zero, the separation from zero point seven is about zero point seven zero, the residual has length about zero point five nine, and the bound on the sine is about zero point eight four, against a true value of about zero point six four. Each choice of trial operator gives a valid inequality with its own residual and its own separation.

What the theorem says in the operator norm

In the operator norm, N of the sine of Theta zero is the sine of the largest directed angle from the trial subspace toward the exact wanted subspace. So the theorem says: the sine of the largest such angle is at most the operator norm of the residual divided by delta. In particular, if the residual has norm less than delta, no trial vector is perpendicular to the exact wanted subspace.

That last statement is directed. It does not say the exact subspace is close to the trial subspace in the other direction. If the exact subspace has more dimensions than the trial subspace, some exact directions may be far from the trial subspace or perpendicular to it, and the theorem says nothing about them. A symmetric conclusion needs a second gap condition, as in Proposition 6.1 of the paper.

The perturbation form, and two different gaps

In applications, the theorem is often used with a perturbation. Let A be a self-adjoint operator whose spectral subspace we know, and A hat equal to A plus H, with H bounded. Take E zero to be a frame for the known spectral subspace of A, and A zero the block of A on it. Then the residual is H E zero, and N of R is at most N of H. If the gap condition holds between A zero and the unwanted block Lambda one of the perturbed operator, the theorem gives delta times N of the sine at most N of H.

Here is a two by two example. Let A be the diagonal matrix with entries three and zero, so the wanted eigenvector is the horizontal axis, with eigenvalue three, and the unwanted eigenvalue is zero. Let H have zeros on the diagonal and one half off the diagonal. Then A hat has eigenvalues about three point zero eight and minus zero point zero eight, and its top eigenvector is tilted about nine point two degrees from the horizontal, with sine about zero point one six zero. The residual, H applied to the horizontal unit vector, is the vector zero, one half, with length one half. The gap delta is between A zero, which is three, and Lambda one, the perturbed unwanted eigenvalue, about minus zero point zero eight. So delta is about three point zero eight, and the bound on the sine is one half divided by three point zero eight, about zero point one six two. The true value is zero point one six zero.

The point to notice is that delta involves the perturbed spectrum, which is usually unknown. The original operator has an eigenvalue gap, three, which we may write g. The theorem is not stated with g. To use the theorem without computing the perturbed spectrum, one certifies a separation: by Weyl's inequality, the unwanted eigenvalue of A hat lies within the norm of H, one half, of the unwanted eigenvalue of A. So the perturbed unwanted spectrum lies at or below one half, and the separation from three is at least two point five. That gives the certified bound one half over two point five, which is zero point two. Using g, three, in place of a certified delta would give one sixth, which happens to be a valid bound here but is not what the theorem proves. In general an original eigengap and a certified separation are different numbers, and only the second goes into the theorem.

How the theorem appears in the journal paper

The recent journal paper on this theory states the theorem with exactly these hypotheses, grouped into three bundles. The trial bundle contains the isometry of E zero, the domain inclusion, and the residual identity. The exact bundle contains the two isometries, perpendicularity, completeness, the domain inclusion for F one, and the intertwining identity. The gap condition has three cases: the interval case, which covers both orders of the two operators, and the two ordered cases stated as quadratic-form bounds. The norm is a normalized symmetric ideal norm, and the conclusion is stated under the two membership hypotheses, for the sine and for the residual.

Two details are worth knowing when reading it. The sine in the conclusion is defined by applying the sine function to the angle operator, and a separate result shows that it equals the modulus of the rectangular block, the identity minus P exact, times E zero. That identity is the third bridge of the proof. And the ordered cases of the gap are stated as quadratic-form bounds rather than spectral containments; for self-adjoint operators the two are equivalent, and the form-bound version is the one that is easiest to verify directly.

Where the theorem comes from

Chandler Davis studied the rotation of eigenvectors under perturbation in 1963 and 1965, and the sine-theta theorem appears, with the tangent and double-angle theorems, among the four headline results of Section 2 of the 1970 paper by Davis and William Kahan, after their 1969 announcement. Davis and Kahan assert that the constants in all four are best possible, attained by two-dimensional examples, and that when the perturbation depends linearly on a small parameter the four estimates agree to first order. They state the theorem for infinite as well as finite dimensional separable Hilbert spaces, for every unitarily invariant norm, and, with the domain conditions and a bounded residual, for unbounded self-adjoint operators with half-infinite spectral intervals.

To summarize. If a self-adjoint A hat has an exact reducing decomposition with unwanted block Lambda one, and a trial frame E zero with trial operator A zero has bounded residual R, and the spectra of A zero and Lambda one are separated by delta as a window or a cut, then delta times the size of the sine of Theta zero is at most the size of R, in every normalized symmetric ideal norm in which both are finite. The proof converts the residual into the Sylvester equation Lambda one X minus X A zero equals F one star R, bounds X by Theorem 5.1 or 5.2, and identifies the modulus of X with the sine. The constant one is sharp, attained in a plane at every angle.

The theorem is one-sided in two ways. It measures angles from the trial subspace toward the exact subspace, not back; and its gap compares the trial operator with the perturbed unwanted block, not the original operator's eigenvalues with each other. Each of these limitations has its own repair in the paper, and each repair needs an additional hypothesis.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Statement (journal paper, Theorem 1)

Separable \(\mathcal E\) over \(\mathbb R\) or \(\mathbb C\); \(\widehat A,A_0,\Lambda_1\) self-adjoint (possibly unbounded); isometries \(E_0,F_0,F_1\); \(E_0(\operatorname{dom}A_0)\subseteq\operatorname{dom}\widehat A\), \(R=\widehat AE_0-E_0A_0\) on \(\operatorname{dom}A_0\), bounded; \(F_0^*F_1=0\), \(F_0F_0^*+F_1F_1^*=I\), \(F_1(\operatorname{dom}\Lambda_1)\subseteq\operatorname{dom}\widehat A\), \(\widehat AF_1=F_1\Lambda_1\); \(\delta>0\) with \(\mathrm{SineGap}(A_0,\Lambda_1)\):
\[
\mathcal I_\delta(A_0,\Lambda_1)\ \vee\ \mathcal I_\delta(\Lambda_1,A_0)\ \vee\ \bigl(A_0\ge(b+\delta)I\wedge\Lambda_1\le bI\bigr)\ \vee\ \bigl(A_0\le bI\wedge\Lambda_1\ge(b+\delta)I\bigr).
\]
\(N\) a normalized symmetric operator-ideal norm with Ky Fan dominance. If \(\sin\Theta_0,R\in\mathfrak I_N\):
\[
\delta\,N(\sin\Theta_0)\le N(R),\qquad \sin\Theta_0=(I-E_0^*P_{\rm exact}E_0)^{1/2}.
\]

### Proof chain

\(X=F_1^*E_0\); \(\Lambda_1X-XA_0=F_1^*R\) on \(\operatorname{dom}A_0\); \(\delta N(X)\le N(F_1^*R)\) (Thm 5.1 after centering, or Thm 5.2); \(N(F_1^*R)\le N(R)\); \(X^*X=I-E_0^*P_{\rm exact}E_0\Rightarrow|X|=\sin\Theta_0\Rightarrow N(X)=N(\sin\Theta_0)\).

### Examples

- **Sharpness:** \(\widehat A=\operatorname{diag}(0,\delta)\), \(v_\theta=(\cos\theta,\sin\theta)\), \(A_0=0\), \(\Lambda_1=\delta\): \(R=(0,\delta\sin\theta)\), equality.
- **Figure 1:** \(\widehat A=\operatorname{diag}(1.9,0.7)\), \(\theta=40^\circ\), \(\rho\approx1.404\), \(\delta\approx0.704\), \(\|r\|\approx0.591\), bound \(\approx0.839\), true \(\sin\theta\approx0.643\).
- **Perturbation:** \(A=\operatorname{diag}(3,0)\), \(H=\begin{pmatrix}0&\tfrac12\\\tfrac12&0\end{pmatrix}\): \(\sigma(\widehat A)=\{\tfrac{3\pm\sqrt{10}}2\}\approx\{3.081,-0.081\}\), \(\theta\approx9.22^\circ\), \(\sin\theta\approx0.1602\); \(R=HE_0=(0,\tfrac12)\); \(\delta=3-\lambda_{\min}(\widehat A)\approx3.081\), bound \(\approx0.1623\). Certified: Weyl gives \(\lambda_{\min}(\widehat A)\le\tfrac12\), \(\delta\ge g-\|H\|=2.5\), bound \(0.2\). Original eigengap \(g=3\) is not \(\delta\).

### Lean correspondence

Journal paper, Listing 1; declared in `DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
theorem sinTheta_unbounded_formGap_whereDefinedUIN_rclike
    [TopologicalSpace.SeparableSpace E]
    (N : NormalizedSymmetricOperatorIdealFamily K)
    (A : LinearPMap K E E)
    (A0 : LinearPMap K F F)
    (Lambda1 : LinearPMap K G G)
    (E0 : ContinuousLinearMap K F E)
    (F0 : ContinuousLinearMap K H E)
    (F1 : ContinuousLinearMap K G E)
    (R : ContinuousLinearMap K F E)
    (hA : IsSelfAdjoint A)
    (hA0 : IsSelfAdjoint A0)
    (hLambda1 : IsSelfAdjoint Lambda1)
    (htrial : IsTrialResidual A A0 E0 R)
    (hexact : IsExactSpectralDecomposition A Lambda1 F0 F1)
    (delta : Real) (hdelta : 0 < delta)
    (hgap : FormBoundedSylvesterGap A0 Lambda1 delta) :
    N.Mem (sourceDirectedSinThetaOperator E0 F0) ->
    N.Mem R ->
      delta * N.gaugeReal (sourceDirectedSinThetaOperator E0 F0) <=
        N.gaugeReal R
```

**Reading the signature.** `K` is the scalar field (`RCLike`: ℝ or ℂ); Lean's `A` is \(\widehat A\); `E, F, G, H` are the ambient, trial, unwanted and exact coordinate spaces (so Lean's `H` is a space, not the perturbation). `LinearPMap` encodes possibly unbounded operators with domains. `IsTrialResidual`, `IsExactSpectralDecomposition` and `FormBoundedSylvesterGap` bundle the hypotheses listed above. `N.Mem` is finiteness of the gauge; `N.gaugeReal` its value. `sourceDirectedSinThetaOperator_eq_modulus` (`SineTheta/Presentation.lean`) is the third bridge.
