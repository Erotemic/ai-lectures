# 021000 — The tangent theorem

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** tangent-double-angle. **Audience:** graph subspaces and tangents; the direct rotation in block form; the sine-theta theorem; Ky Fan norms; Lemmas 6.1 and 6.2.

<!-- BEGIN SPOKEN LECTURE -->

The tangent theorem

The sine-theta theorem bounds the sine of the angle between a trial subspace and an exact spectral subspace. The tangent-theta theorem, the second of the paper's four headline results, bounds the tangent by the same quantity, residual over gap. Since the tangent is larger than the sine and never vacuous, this is a strictly stronger conclusion, and it costs two strengthened hypotheses: the gap must be ordered, with the unwanted spectrum entirely on one side, and the trial operator must be the Rayleigh–Ritz compression.

Here is what we will establish. First, the statement: if the spectrum of A zero lies in an interval with top alpha, the spectrum of Lambda one lies at or above alpha plus delta, and A zero is the Rayleigh–Ritz compression E zero star A hat E zero, then delta times the size of the tangent of Theta zero is at most the size of the residual, and delta times the size of the full tangent of Theta is at most the size of H. Second, the proof: a block identity for the direct rotation gives, for each principal angle, cosine theta times a coupling at least delta times sine theta; this forces every cosine to be positive and bounds each tangent, and Ky Fan sums finish the argument. Third, in the plane, with the Rayleigh–Ritz choice, the tangent bound is an equality. Fourth, the one-sided placement is essential: with unwanted spectrum on both sides of the trial value, the tangent bound fails while the sine bound still holds. Fifth, a subtlety in reading the printed theorem, concerning its full-angle conclusion in infinite dimensions.

The statement

The data are as in the sine-theta theorem. A self-adjoint operator A hat, the perturbation of a reference operator A by H, has an exact reducing decomposition with frames F zero and F one, and blocks Lambda zero and Lambda one. The trial subspace has isometric frame E zero, its complement has frame E one, and the reference operator A is block diagonal with respect to them, with blocks A zero and A one.

There are two hypotheses. First, the ordered gap: the spectrum of A zero lies in an interval from beta to alpha, and the spectrum of Lambda one lies in the half-line from alpha plus delta upward. Second, the Rayleigh–Ritz condition: the diagonal block of H on the trial subspace, H zero, is zero. Equivalently, A zero equals E zero star A hat E zero, the compression of the perturbed operator to the trial subspace.

The conclusions, for every unitarily invariant norm, are: delta times the norm of the tangent of Theta zero is at most the norm of R, and delta times the norm of the tangent of Theta is at most the norm of H. The first is directed and stated with the residual; the second concerns the full angle and the whole perturbation.

The generalized form, Theorem 6.3 of the paper, keeps the Rayleigh–Ritz trial data and the ordered gap, and allows the trial subspace to have smaller dimension than the exact subspace.

What the residual is under the Rayleigh–Ritz condition

With the Rayleigh–Ritz condition, the residual has a simple form. Write H in blocks relative to the trial subspace and its complement: H zero on the trial subspace, H one on the complement, and the off-diagonal block B, which takes trial coordinates to complementary coordinates. Since A E zero equals E zero A zero, the residual A hat E zero minus E zero times A zero plus H zero equals H E zero minus E zero H zero, and when H zero is zero, that is E one B. So R is the off-diagonal block B, embedded into the ambient space, and R and B have the same norm in every unitarily invariant norm.

The key identity

The proof uses the direct rotation U from the trial subspace to the exact subspace. In blocks, its diagonal entries are cosine Theta zero and cosine Theta one, its crossing block from the trial subspace to the complement is S zero, equal to J zero times sine Theta zero, and the block back is minus S zero star.

The direct rotation diagonalizes the perturbed operator: A hat times U equals U times the block-diagonal operator with blocks Lambda zero and Lambda one, because U carries the trial subspace onto the exact one and its complement onto the exact complement. Write this out in blocks and read off the block in the second row and first column. After taking adjoints, it gives the identity: cosine Theta one times B equals S zero A zero minus Lambda one S zero. Davis and Kahan label this equation 6.5. It is a Sylvester-type identity, with the coupling B on the left, and the crossing block of the direct rotation, which encodes the sines, on the right.

Now pass to principal vectors. Take x, a unit eigenvector of Theta zero in trial coordinates with angle theta, and y, the corresponding unit vector in complementary coordinates, so that S zero x equals sine theta times y, S zero star y equals sine theta times x, and cosine Theta one times y equals cosine theta times y. Take the inner product of both sides of the identity with y on the left and x on the right.

The left side gives cosine theta times the inner product of y with B x. The right side gives sine theta times the Rayleigh quotient of A zero at x, minus sine theta times the Rayleigh quotient of Lambda one at y. By the ordered gap, the first Rayleigh quotient is at most alpha and the second is at least alpha plus delta. So the right side is at most minus delta times sine theta. Taking absolute values: cosine theta times the absolute value of the inner product of y with B x is at least delta times sine theta.

Two consequences follow. If sine theta is positive, the left side is positive, so cosine theta is not zero: the angle is strictly less than ninety degrees. Right angles are excluded by the inequality itself, not assumed. And dividing by cosine theta, the tangent of theta is at most the absolute value of the inner product of y with B x, divided by delta.

Summing over the k largest angles, with the x's orthonormal and the y's orthonormal, the sum of the k largest tangents is at most the sum of the corresponding inner products, divided by delta. By Ky Fan's characterization, the sum over orthonormal pairs of inner products of y with B x is at most the Ky Fan k-norm of B. So delta times the Ky Fan k-norm of the tangent of Theta zero is at most the Ky Fan k-norm of B, for every k, and Ky Fan dominance gives every unitarily invariant norm. Since B and R have the same norms, the directed conclusion follows.

In this argument Davis and Kahan first assume that all operators are bounded and that the crossing block is compact, so that principal vectors exist. The appendix to Section 6 removes both assumptions. Without compactness there may be no principal vectors; instead one chooses finite-rank projections that nearly capture the largest singular values. Lemma 6.3 controls what such a choice leaves out: if a rank nu compression of an operator captures all but eta squared of the sum of its nu largest squared singular values, then the part it misses, the leakage, has norm less than eta. The near-optimal vectors then satisfy the scalar inequality approximately, and the error tends to zero.

The full-angle conclusion

The full tangent of Theta has two off-diagonal corners, J zero times tangent Theta zero and minus J zero star times tangent Theta one, which have the same norms, equal to the norm of the directed tangent. Each corner is bounded by B divided by delta: the directed one by the argument above, and the other through the intertwining partial isometry J zero. So by Lemma 6.1, delta times the full tangent is dominated by the off-diagonal block operator with corners B and B star. By the pinching Lemma 6.2, that block operator is dominated by the full perturbation H, written in blocks with zero in the top-left corner, B and B star off the diagonal, and H one in the bottom-right corner. So delta times the norm of the tangent of Theta is at most the norm of H.

Equality in the plane

In two dimensions the tangent bound is exact for every Rayleigh–Ritz trial vector. Let A hat be diagonal with entries lambda one, the wanted eigenvalue, and lambda two, the unwanted one, with lambda one larger, and let the trial vector make angle theta with the wanted axis. The Rayleigh quotient is lambda one cosine squared theta plus lambda two sine squared theta. The residual has length lambda one minus lambda two, times sine theta, times cosine theta. The separation between the Rayleigh quotient and lambda two is lambda one minus lambda two, times cosine squared theta. Their ratio is sine over cosine, the tangent of theta.

In the paper's figure, with entries one point nine and zero point seven and the trial vector at forty degrees, the ratio of residual to separation is about zero point eight three nine, which is tangent forty degrees exactly. The sine theorem, from the same numbers, bounded the sine by zero point eight three nine against a true sine of zero point six four three. The tangent theorem turns the same ratio into an exact statement about the tangent.

This orientation is the mirror image of the printed statement, with the trial value above the unwanted eigenvalue. The theorem holds in both orientations: replacing A hat by minus A hat reverses every spectrum and turns one into the other.

One-sided placement is essential

Why must the unwanted spectrum lie entirely on one side? Davis and Kahan give an example with gap one, tangent one, and residual one over root two, in which unwanted spectrum lies on both sides. Here is a three by three instance with those numbers. Let A hat be diagonal with entries zero, one, and minus one, and let the wanted exact subspace be the first axis, with eigenvalue zero. The unwanted spectrum is one and minus one, at distance one on either side. Take the trial vector with coordinates one over root two, one half, one half. Its Rayleigh quotient is zero, so the Rayleigh–Ritz trial value is zero, exactly the wanted eigenvalue. The angle between the trial vector and the first axis is forty-five degrees, so its tangent is one. The residual is A hat applied to the trial vector, with coordinates zero, one half, minus one half, and length one over root two.

The interval and exterior gap holds with delta equal to one, so the sine theorem applies: one times the sine of forty-five degrees is one over root two, which equals the residual. But the tangent theorem would claim one times tangent forty-five degrees, which is one, is at most one over root two. It is not. The two unwanted components of the residual, pulling in opposite directions from the two sides, partly cancel in the Rayleigh quotient, and the trial vector can lean a long way toward the unwanted space without the residual noticing as much as the tangent would require.

In the proof, the cancellation shows up at the step that used the ordered gap: the Rayleigh quotient of Lambda one at y could be anywhere between minus one and one, including zero, and the right-hand side would not be bounded away from zero.

The beam, refined

The paper's numerical example uses exactly this improvement. For the free beam with perturbation epsilon t, the trial subspace is the span of the rigid motions. With the trial operator zero, the sine theorem bounds the largest sine by about zero point eight one epsilon divided by five hundred. With the Rayleigh–Ritz trial operator, the trial eigenvalues are epsilon over two times one minus or plus one over root three, about zero point two one epsilon and zero point seven nine epsilon. The residual becomes much smaller, with operator norm epsilon over root fifteen, about zero point two six epsilon, and rank one. The gap to the unwanted spectrum, which lies above five hundred, is five hundred minus about zero point seven nine epsilon. The tangent theorem then gives the tangent of the largest angle less than about zero point zero zero zero five one six epsilon, divided by one minus zero point zero zero one five eight epsilon. Because the residual has rank one, the same bound holds for the sum of the two tangents.

A subtlety in the printed statement

There is a point of interpretation worth knowing when reading the paper. The tangent theorem is printed in Section 2, before Davis and Kahan introduce, in Section 3, the standing assumption that the two defect spaces have the same dimension. It is proved in Section 6, where that assumption is in force.

The directed conclusion needs no such assumption: the scalar inequality itself excludes right angles on the trial side whenever the residual is finite. The full-angle conclusion is different. In infinite dimensions there is a configuration, built from the nested half-spaces of the shift example, in which the trial side has no right angles but the complementary side has one. Then the full tangent of Theta is not a bounded operator, and its norm is not a finite number, while H can have finite norm. The printed full-angle conclusion is meaningful there only under the paper's announced convention that a result is vacuous when a displayed norm does not exist, together with the standing defect assumption. A careful statement of the full-angle tangent theorem therefore includes the equal-defect hypothesis and concludes, rather than assumes, that the tangent belongs to the ideal of the norm. Read that way, it is faithful to the paper's own global conventions. This is a different situation from Proposition 4.4, where every quantity is finite and the printed conclusion is false.

To summarize. Under an ordered gap, spectrum of A zero below alpha and of Lambda one above alpha plus delta, and the Rayleigh–Ritz condition H zero equal to zero, delta times the size of the tangent of Theta zero is at most the size of the residual, and delta times the size of the full tangent is at most the size of H. The proof reads the block identity cosine Theta one times B equals S zero A zero minus Lambda one S zero at principal vectors, obtaining cosine theta times a coupling at least delta sine theta, which excludes right angles and bounds each tangent; Ky Fan sums and dominance give every norm, and Lemmas 6.1 and 6.2 give the full angle. The bound is exact in the plane for every Rayleigh–Ritz trial vector, and it fails when unwanted spectrum lies on both sides, even though the sine bound survives.

The tangent theorem asks more of the trial data than the sine theorem does: a Rayleigh–Ritz trial operator, and a one-sided gap. When those hold, it gives a bound that remains meaningful for arbitrarily large residuals.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Statement (S2-tan-theta; generalized: Theorem 6.3)

\(\sigma(A_0)\subseteq[\beta,\alpha]\), \(\sigma(\Lambda_1)\subseteq[\alpha+\delta,\infty)\), \(H_0=0\) (\(A_0=E_0^*\widehat AE_0\)):
\[
\delta N(\tan\Theta_0)\le N(R),\qquad \delta N(\tan\Theta)\le N(H).
\]
Theorem 6.3 allows \(\dim\operatorname{ran}E_0<\dim\operatorname{ran}F_0\).

### Proof

\(H\sim\begin{pmatrix}H_0&B^*\\B&H_1\end{pmatrix}\); \(H_0=0\Rightarrow R=E_1B\).
From \(\widehat AU=U\operatorname{diag}(\Lambda_0,\Lambda_1)\) ((6.3)–(6.4)): \(C_1B=S_0A_0-\Lambda_1S_0\) (6.5).
With \(S_0x=\sin\theta\,y\), \(S_0^*y=\sin\theta\,x\), \(C_1y=\cos\theta\,y\):
\[
\cos\theta\,\langle y,Bx\rangle=\sin\theta\bigl(\langle x,A_0x\rangle-\langle y,\Lambda_1y\rangle\bigr)\le-\delta\sin\theta,
\]
so \(\cos\theta\,|\langle y,Bx\rangle|\ge\delta\sin\theta\) (6.6), \(\cos\theta>0\) whenever \(\sin\theta>0\), and \(\delta\sum_{j\le k}\tan\theta_j\le\|B\|_{(k)}\).
Ambient: \(\delta\|\tan\Theta\|\le\left\|\begin{pmatrix}0&B^*\\B&0\end{pmatrix}\right\|\le\left\|\begin{pmatrix}0&B^*\\B&H_1\end{pmatrix}\right\|=\|H\|\) (Lemmas 6.1, 6.2).

**Lemma 6.3:** rank-\(\nu\) \(\Gamma,\Psi\), \(K\Psi=\Gamma K\Psi\), \(\sum_{k\le\nu}\mu_k^2>\sum_{k\le\nu}\kappa_k^2-\eta^2\Rightarrow\|\Gamma K\Psi^\perp\|_{\rm op}<\eta\).

### Examples

- **Plane, Rayleigh–Ritz:** \(\|r\|=(\lambda_1-\lambda_2)\sin\theta\cos\theta\), \(\delta=(\lambda_1-\lambda_2)\cos^2\theta\), \(\|r\|/\delta=\tan\theta\). Figure 1: \(0.5909/0.7042=0.8391=\tan40^\circ\).
- **Two-sided failure** (numbers of Example 6.1): \(\widehat A=\operatorname{diag}(0,1,-1)\), \(v=(\tfrac1{\sqrt2},\tfrac12,\tfrac12)\), \(\rho=0\), \(r=(0,\tfrac12,-\tfrac12)\), \(\|r\|=\tfrac1{\sqrt2}\), \(\delta=1\), \(\tan\theta=1\): \(\delta\tan\theta>\|r\|\), \(\delta\sin\theta=\|r\|\).
- **Beam (9.5)–(9.6):** \(\widehat A_0=\tfrac\varepsilon2\operatorname{diag}(1-\tfrac1{\sqrt3},1+\tfrac1{\sqrt3})\), \(\widehat R^*\widehat R=\tfrac{\varepsilon^2}{30}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), \(\|\widehat R\|=\varepsilon/\sqrt{15}\), gap \(500-0.7887\varepsilon\), \(\tan\theta_1<0.0005164\varepsilon/(1-0.0015774\varepsilon)\).

### Nonlocal reading of the ambient conclusion

The source reconstruction's editorial note (`prose/distilled_literature/DavisKahan1970_part_III.tex`, “nonlocal source semantics”) records: the printed Section 2 statement omits (3.5); under the literal reading with \(\|\tan\Theta\|=+\infty\) allowed, a nested infinite-dimensional pair satisfies the printed hypotheses with finite \(\|H\|\) and an unbounded \(\tan\Theta\). The repository formalizes the ambient conclusion with a crossed-defect hypothesis and a membership conclusion, and records the interpretation in `dev/davis-kahan-1970-formalization-result-inventory.json`, entry `S2-tan-theta`, field `nonlocal_source_interpretation`.

### Lean correspondence

Inventory entries `S2-tan-theta`, `DK-6.3-thm` and `DK-6.3-lem` in `dev/davis-kahan-1970-formalization-result-inventory.json` list the declarations, all in `namespace TauCeti.DavisKahan1970`.
