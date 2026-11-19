# 023000 — The doubled-tangent theorem

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** tangent-double-angle. **Audience:** off-diagonal perturbations and Theorem 8.1; graph subspaces and tangents; the tangent and doubled-sine theorems.

<!-- BEGIN SPOKEN LECTURE -->

The doubled-tangent theorem

The fourth headline theorem of the Davis–Kahan paper bounds the tangent of twice the angle. It has the strongest conclusion of the four and the most specific hypotheses: the gap is an ordered gap between the two blocks of the reference operator, and the perturbation must be off-diagonal. In return its gap is the one we usually know, since it concerns the unperturbed operator, and in the plane it reduces to an exact formula familiar from numerical linear algebra.

Here is what we will establish. First, the statement: if the reference blocks satisfy A zero at most alpha and A one at least alpha plus delta, and the perturbation H has both diagonal blocks zero, then delta times the size of the tangent of two Theta zero is at most twice the size of the residual, and delta times the size of the tangent of two Theta is at most twice the size of H. Second, the planar case: a symmetric two by two matrix is diagonalized by a rotation through theta exactly when the tangent of two theta equals twice the off-diagonal entry divided by the difference of the diagonal entries, so the theorem is an equality there. Third, the proof in general reads the invariance condition at principal vectors, and, as in the tangent theorem, it shows that the cosine of twice the angle cannot vanish rather than assuming it. Fourth, in practice the off-diagonal hypothesis can always be arranged by taking the reference operator to be the block-diagonal part of the operator under study, which is how the paper applies the theorem to the free beam.

The statement

Let A be self-adjoint with a reducing reference subspace, blocks A zero and A one. Assume the ordered gap: the spectrum of A zero lies in an interval from beta to alpha, and the spectrum of A one lies at or above alpha plus delta. Let H be bounded and self-adjoint with both diagonal blocks zero, H zero and H one, so that H only couples the reference subspace to its complement through an off-diagonal block B. Let Q be a reducing subspace of A plus H, with Theta the angle between the reference subspace and Q.

Then, for every unitarily invariant norm: delta times the norm of the tangent of two Theta zero is at most twice the norm of R, which here equals the norm of B, and delta times the norm of the tangent of two Theta is at most twice the norm of H.

As Davis and Kahan emphasize, no separate hypothesis excludes the angles where the tangent of two theta is infinite, at forty-five degrees, and no spectral hypothesis is placed on the perturbed blocks. Both are consequences. Combined with Theorem 8.1, which identifies the spectral subspace of A plus H below alpha as the unique reducing subspace with all angles at most forty-five degrees, the theorem says that for that subspace twice the angle is below ninety degrees, and its tangent is controlled.

The planar formula

Take a real symmetric two by two matrix with diagonal entries a zero and a one, a zero smaller, and off-diagonal entry b. Rotate the horizontal axis through an angle theta, giving the unit vector q with coordinates cosine theta and sine theta, and its perpendicular partner, with coordinates minus sine theta and cosine theta. The rotated line is invariant, that is, an eigenvector line, exactly when the matrix sends q to a vector with no component along the partner.

Compute that component. The matrix applied to q has first coordinate a zero cosine theta plus b sine theta, and second coordinate b cosine theta plus a one sine theta. Its inner product with the partner is minus sine theta times the first coordinate plus cosine theta times the second. Collecting terms: sine theta cosine theta, times a one minus a zero, plus b times cosine squared theta minus sine squared theta. Using the double-angle identities, that is one half sine two theta times a one minus a zero, plus b cosine two theta. Setting it to zero gives the tangent of two theta equal to minus two b divided by a one minus a zero.

So in the plane the angle of the eigenvectors is given exactly: the tangent of twice the angle is twice the coupling divided by the gap between the diagonal entries. This is the rotation used in Jacobi's classical method for symmetric eigenvalue problems, which annihilates one off-diagonal entry at a time.

Read it as the theorem. The reference operator is the diagonal part, with blocks a zero and a one and gap a one minus a zero, which we may take as delta. The perturbation is the off-diagonal part, with norm the absolute value of b. The formula says delta times the absolute value of the tangent of two theta equals twice the absolute value of b. The doubled-tangent theorem is an equality in the plane, for every coupling strength.

For example, with diagonal entries minus two and two and coupling one, the tangent of two theta is one half. With diagonal entries zero and three and coupling zero point seven, it is about zero point four six seven. With diagonal entries one and one point five and coupling two, it is eight: the coupling is large compared with the gap, and twice the angle is close to ninety degrees, but still below it, as the theorem guarantees.

The general argument

In general, Davis and Kahan read the same invariance condition in block form. The exact subspace and its complement reduce A plus H, so the block of A plus H from the exact complement to the exact subspace vanishes. Writing that block through the direct rotation, with blocks cosine Theta, the partial isometry J zero, and sine Theta, gives an identity they number 7.6. It involves the coupling B, the reference blocks A zero and A one, and the cosines and sines of the angle.

Now evaluate the identity at a pair of principal vectors with angle theta, x in the reference subspace and y in its complement. The ordered gap enters as before: the Rayleigh quotient of A one at y is at least alpha plus delta, and that of A zero at x is at most alpha, so their difference is at least delta. The result is the scalar inequality: plus or minus two times the cosine of two theta, times the real part of the coupling between y and x, is at least delta times the sine of two theta. This is the planar formula turned into an inequality.

Two conclusions follow. If the sine of two theta is positive, the left side is positive, so the cosine of two theta is not zero: the angle is not forty-five degrees. That is how the pole of the doubled tangent is excluded by the argument. Then dividing, twice the coupling is at least delta times the absolute value of the tangent of two theta. Summing over the k largest angles with Ky Fan's variational principle gives delta times the Ky Fan k-norm of the tangent of two Theta zero at most twice the Ky Fan k-norm of B, for every k, and dominance gives every unitarily invariant norm. Since H zero is zero, the residual is E one B, with the same norms as B. Lemma 6.1, comparing direct sums, extends the bound to the full angle and the full perturbation.

Arranging the off-diagonal hypothesis

At first sight, requiring both diagonal blocks of H to vanish is restrictive. In practice it is a choice of how to split the operator under study.

Suppose we are given a self-adjoint operator, call it the operator under study, and a trial subspace. Define the reference operator A to be its block-diagonal part relative to the trial subspace: on the trial subspace, its compression, the Rayleigh–Ritz operator; on the complement, its compression to the complement. Define H to be the rest, the off-diagonal part. Then H zero and H one are zero by construction, and the operator under study is A plus H. The hypotheses of the doubled-tangent theorem reduce to a spectral statement about two compressions: the Ritz values on the trial subspace lie at or below alpha, and the compression to the complement lies at or above alpha plus delta.

That is how the paper uses the theorem for the free beam. The trial subspace is the span of the two rigid motions, the Rayleigh–Ritz operator on it has eigenvalues about zero point two one epsilon and zero point seven nine epsilon, and the compression of the perturbed beam operator to the complement exceeds five hundred. So delta can be taken as five hundred minus about zero point seven nine epsilon. The residual of the Rayleigh–Ritz trial data has norm epsilon over root fifteen. The theorem gives the tangent of twice the largest angle less than about zero point zero zero one zero three three epsilon, divided by one minus zero point zero zero one five eight epsilon, exactly twice the bound the tangent theorem gave for the tangent of the angle itself. Because this residual has rank one, the same bound holds for the sum of the doubled tangents of both angles.

Comparing the four headline theorems

With all four theorems in hand, it is worth placing them side by side, because their hypotheses are easy to blur.

The sine theorem compares the trial operator A zero with the unwanted perturbed block Lambda one, in a window or a cut, and allows any self-adjoint trial operator. The tangent theorem compares the same two operators but requires a cut with the unwanted block above, and the Rayleigh–Ritz condition H zero equal to zero. The doubled-sine theorem compares the two perturbed blocks Lambda zero and Lambda one in a window, and needs nothing about the trial operator. The doubled-tangent theorem compares the two reference blocks A zero and A one in a cut, and needs both diagonal blocks of H to vanish.

Each conclusion has a factor matched to its quantity: one for the sine and tangent, two for the doubled sine and doubled tangent. Davis and Kahan state that all four constants are best possible, attained in two dimensions, and that for a perturbation depending linearly on a small parameter the four estimates agree to first order. In the plane with diagonal entries minus two and two and coupling h, for instance, every one of the four predicts an angle of h over four to first order.

To summarize. Under an ordered gap between the reference blocks and an off-diagonal perturbation, delta times the size of the tangent of two Theta zero is at most twice the size of the residual, and delta times the size of the tangent of two Theta is at most twice the size of H. In the plane this is the exact Jacobi formula, tangent of two theta equals twice the coupling over the diagonal gap. In general the block invariance identity, read at principal vectors, gives two cosine two theta times the coupling at least delta sine two theta, which both excludes forty-five degrees and bounds the doubled tangent. Any operator can be put in the theorem's form by taking its block-diagonal part as the reference, which turns the hypotheses into conditions on two compressions.

Davis and Kahan record that, unlike the doubled-sine theorem, no extension of the doubled-tangent theorem to a trial subspace of smaller dimension than the exact one was known to them. The off-diagonal structure that the proof relies on pairs each trial direction with a complementary direction, and unequal dimensions break that pairing.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Statement (S2-tan-two-theta)

\(\sigma(A_0)\subseteq[\beta,\alpha]\), \(\sigma(A_1)\subseteq[\alpha+\delta,\infty)\), \(H\) bounded, \(H_0=H_1=0\):
\[
\delta N(\tan2\Theta_0)\le2N(R),\qquad\delta N(\tan2\Theta)\le2N(H).
\]
No hypothesis excludes \(\cos2\theta_j=0\); it is derived.

### Planar formula

\(M=\begin{pmatrix}a_0&b\\b&a_1\end{pmatrix}\), \(q=(\cos\theta,\sin\theta)\), \(q^\perp=(-\sin\theta,\cos\theta)\):
\[
\langle q^\perp,Mq\rangle=\tfrac12\sin2\theta\,(a_1-a_0)+b\cos2\theta=0\iff\tan2\theta=-\frac{2b}{a_1-a_0}.
\]
Examples: \((-2,2,1)\): \(\tfrac12\); \((0,3,0.7)\): \(0.467\); \((1,1.5,2)\): \(8\).

### Proof (Section 7, (7.6))

\(F_0^*(A+H)F_1=0\Rightarrow -C_0B^*C_1+S_0^*BS_0^*=S_0^*A_1C_1-C_0A_0S_0^*\); at principal vectors \(\pm2\cos2\theta_j\operatorname{Re}(y_j^*Bx_j)\ge\delta\sin2\theta_j\), hence \(\cos2\theta_j\ne0\) and \(2\operatorname{Re}(y_j^*Bx_j)\ge\delta|\tan2\theta_j|\); Ky Fan sums, dominance, Lemma 6.1.

### Beam (9.7)

Reference = block-diagonal part of \(A+H\) relative to \(E_0\); \(\widehat A_0=\tfrac\varepsilon2\operatorname{diag}(1\mp\tfrac1{\sqrt3})\), \(\widehat A_1=E_1^*(A+H)E_1>500\), \(\|\widehat R\|=\varepsilon/\sqrt{15}\):
\[
\tan2\theta_1<\frac{0.0010328\,\varepsilon}{1-0.0015774\,\varepsilon}.
\]

### The four headline theorems

| Theorem | Gap between | Shape | Extra | Constant |
|---|---|---|---|---|
| \(\sin\theta\) | \(A_0,\Lambda_1\) | window or cut | — | 1 |
| \(\tan\theta\) | \(A_0,\Lambda_1\) | cut | \(H_0=0\) | 1 |
| \(\sin2\theta\) | \(\Lambda_0,\Lambda_1\) | window | — | 2 |
| \(\tan2\theta\) | \(A_0,A_1\) | cut | \(H_0=H_1=0\) | 2 |

### Lean correspondence

Inventory entry `S2-tan-two-theta` (`dev/davis-kahan-1970-formalization-result-inventory.json`), declarations in `namespace TauCeti.DavisKahan1970`; the Section 9 numerical consequences are not among the 29 counted results.
