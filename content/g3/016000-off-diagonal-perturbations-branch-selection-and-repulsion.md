# 016000 — Off-diagonal perturbations, branch selection, and repulsion

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** tangent-double-angle. **Audience:** reducing decompositions and block operators; the angle operator and the direct rotation; the ordered gap shape; quadratic forms.

<!-- BEGIN SPOKEN LECTURE -->

Off-diagonal perturbations, branch selection, and repulsion

The double-angle theorems bound the sine or tangent of twice the angle. Twice the angle has an ambiguity built in: the sine of two theta is small both when theta is near zero and when theta is near ninety degrees. A bound on it alone cannot tell whether an approximate subspace is close to the target or nearly perpendicular to it. Section 8 of the Davis–Kahan paper resolves this for an important class of perturbations, those that only couple a subspace to its complement. This lecture studies that class, and Theorem 8.1, which selects the correct branch and turns the selection into a quantitative statement about eigenvalues moving apart.

Here is what we will establish. First, a perturbation H is off-diagonal relative to a subspace when its two diagonal blocks vanish; then the reflection through the subspace reverses H, and A plus H and A minus H have the same spectrum, so eigenvalues depend on the coupling only to second order while eigenvectors move to first order. Second, if the reference operator has an ordered gap, with block A zero at most alpha and block A one at least alpha plus delta, then an off-diagonal perturbation, of any size, leaves the open interval from alpha to alpha plus delta free of spectrum. Third, Theorem 8.1: among reducing subspaces of the perturbed operator, the angle operator from the reference subspace is at most forty-five degrees exactly when the perturbed blocks keep the same ordering, lower block at most alpha and upper block at least alpha plus delta; such a subspace exists and is unique, namely the spectral subspace of the perturbed operator below alpha. Fourth, for that subspace, a quadratic-form inequality expresses spectral repulsion: the upper reference block minus alpha is at most the cosine of the complementary angle, times the perturbed upper block minus alpha, times the same cosine. In finite dimensions this says each eigenvalue is pushed away from the gap by at least the factor one over cosine squared of its angle.

The ambiguity of doubled angles

Take the plane with A the diagonal matrix with entries minus one and one, and H equal to zero. The reducing subspaces of A plus H, which is just A, include the horizontal axis and the vertical axis. If the reference subspace is the horizontal axis and we happen to pick the vertical axis as the exact subspace, the angle between them is ninety degrees, and the sine of twice ninety degrees is zero. A double-angle bound of the form delta times the sine of two Theta at most twice the norm of H is satisfied trivially, with both sides zero, even though the chosen exact subspace is as far as possible from the reference.

The double-angle theorems compare the reference subspace with a reducing subspace of the perturbed operator, but they do not say which reducing subspace. When there is a choice, a wrong choice can make the angle near ninety degrees. Section 8 identifies the spectrally correct choice and proves that it gives angles at most forty-five degrees, where the sine of two theta and theta are small together.

Off-diagonal perturbations

Let P be the projection onto a reference subspace that reduces A, with blocks A zero on the subspace and A one on its complement. Write H in the same blocks: H zero, the off-diagonal block B and its adjoint, and H one. The perturbation is off-diagonal when H zero and H one are both zero: H only couples the subspace to its complement.

Let J be the reflection two P minus the identity, which fixes the subspace and negates its complement. Conjugating a block operator by J keeps the diagonal blocks and negates the off-diagonal ones. So J A J equals A, and for an off-diagonal H, J H J equals minus H. Therefore J times A plus H, times J, equals A minus H. Since J is unitary, A plus H and A minus H have the same spectrum.

That has a striking consequence. If the perturbation is H equal to a small number h times a fixed off-diagonal operator, the eigenvalues of A plus h times that operator are the same as for minus h. So they are even functions of h, and change only to second order. The eigenvectors, by contrast, typically move to first order in h.

The two by two example shows both. Let A be diagonal with entries minus two and two, and let H have zeros on the diagonal and h off the diagonal. The eigenvalues of A plus H are plus and minus the square root of four plus h squared, which are even in h and differ from plus and minus two by about h squared over four for small h. The eigenvector for the lower eigenvalue makes an angle theta with the horizontal axis whose doubled tangent, tangent two theta, is exactly h over two, so theta is about h over four, first order. With h equal to one, theta is about thirteen point three degrees, while the eigenvalues have moved from two to about two point two four.

The gap survives

The example also shows the eigenvalues moving apart. Before the perturbation they were minus two and two; afterward they are further from zero. This is general for off-diagonal perturbations of an ordered gap.

Suppose A zero is at most alpha and A one is at least alpha plus delta, in the sense of quadratic forms, and H is off-diagonal. Take any number c strictly between alpha and alpha plus delta. In blocks, A plus H minus c has top-left block A zero minus c, which is negative definite, since A zero is at most alpha, below c. Its bottom-right block A one minus c is positive definite. And its off-diagonal blocks are B and B star, the coupling.

A block operator with a negative definite top-left block, a positive definite bottom-right block, and any coupling, is invertible. One way to see this is through the Schur complement: eliminate the top block, and the remaining block is A one minus c, plus B times the inverse of c minus A zero, times B star, which is a positive definite operator plus a positive one, hence invertible. So c is not in the spectrum. The interval from alpha to alpha plus delta, which separated the reference blocks, still separates the perturbed spectrum, no matter how large the coupling is. Off-diagonal perturbations push eigenvalues away from the gap, never into it.

Theorem 8.1: selecting the branch

Since the perturbed operator has no spectrum in the gap, its spectrum splits naturally into a lower part, at most alpha, and an upper part, at least alpha plus delta. The spectral subspace for the lower part is a reducing subspace of A plus H with blocks Lambda zero at most alpha and Lambda one at least alpha plus delta. That is the spectrally corresponding choice.

Theorem 8.1 says, under the paper's standing assumption that the two defect spaces have equal dimension: for a reducing subspace of A plus H, the full angle operator from the reference subspace is at most forty-five degrees exactly when its blocks satisfy Lambda zero at most alpha and Lambda one at least alpha plus delta. The spectral subspace below alpha is therefore on the acute branch, and it is the only reducing subspace satisfying the angle bound.

The proof reduces to a single principal plane and compares two ways of computing a Rayleigh quotient. Take a principal plane, with x zero a unit vector in the reference subspace, y one a unit vector in its complement, and the exact vector making angle theta with x zero. Expressing the Rayleigh quotient of the perturbed operator at the exact vector once from the reference side and once from the complementary side gives two formulas, and equating them yields: the coupling between y one and x zero, times tangent theta minus cotangent theta, equals the Rayleigh quotient of A one at y one minus the Rayleigh quotient of A zero at x zero. By the ordered gap, the right side is at least delta, which is positive. On the left, tangent theta minus cotangent theta is zero at forty-five degrees, so theta can never equal forty-five degrees. Its sign changes there, so the spectral placement of the blocks decides on which side of forty-five degrees theta lies, and the correct placement gives theta below forty-five.

Repulsion, quantitatively

For the spectral subspace on the acute branch, Theorem 8.1 also relates the blocks before and after perturbation. Choose isometric frames for the reference subspace and its complement, and transport them by the direct rotation to frames for the exact subspace and its complement. In these matched coordinates, the inequality is: A one minus alpha is at most cosine Theta one, times Lambda one minus alpha, times cosine Theta one, as quadratic forms. A mirror-image inequality holds for the lower blocks.

Read it as a statement about pushing. Both sides are measured relative to alpha, the edge of the gap. The left side is how far above the gap the reference upper block sits. The right side is how far above the gap the perturbed upper block sits, damped by the squared cosine of the angle through which its eigenvectors have turned. So the perturbed upper eigenvalues must lie above the gap by at least the reference amount divided by cosine squared. The more an off-diagonal coupling rotates the eigenvectors, the further it must push the eigenvalues.

In finite dimensions, with the eigenvalues of A one and of Lambda one in increasing order, the k-th reference eigenvalue minus alpha is at most the squared operator norm of cosine Theta one times the k-th perturbed eigenvalue minus alpha. And for every symmetric gauge function, the list of reference distances from alpha is dominated by the list of perturbed distances, each multiplied by the cosine squared of the corresponding angle. Davis and Kahan call this spectral repulsion.

Check it in the plane with A equal to diagonal minus two and two, alpha equal to minus two, so the reference upper block minus alpha is four. With coupling h equal to two, the perturbed upper eigenvalue is two root two, about two point eight three, the angle is twenty-two and a half degrees, and its cosine squared is about zero point eight five four. The right side is two point eight three plus two, times zero point eight five four, which is about four point one two. Four is at most four point one two, as the theorem requires. As h tends to zero, the two sides approach each other: the inequality is tight to first order.

What Theorem 8.1 does for the double-angle theorems

The doubled-tangent theorem uses exactly these hypotheses: an ordered gap between the reference blocks, and an off-diagonal perturbation. Its conclusion bounds the tangent of twice the angle. Theorem 8.1 adds that, for the spectral subspace below alpha, the angle is at most forty-five degrees, so twice the angle is at most ninety, and the doubled tangent is finite and increasing on that branch. A small doubled tangent then genuinely means a small angle.

The doubled-sine theorem has different hypotheses, an interval gap between the two perturbed blocks, and needs a different branch-selection result, Theorem 8.2, based on smallness of the perturbation rather than its off-diagonal structure.

To summarize. An off-diagonal perturbation anticommutes with the reflection through the reference subspace, so A plus H and A minus H have the same spectrum, and eigenvalues move only to second order while eigenvectors move to first order. With an ordered reference gap, the open gap interval stays free of spectrum for every off-diagonal coupling, by the Schur complement argument. Theorem 8.1 then identifies the spectrally correct reducing subspace, the spectral subspace below alpha, as the unique one whose angle from the reference is at most forty-five degrees, and proves the repulsion inequality A one minus alpha at most cosine Theta one times Lambda one minus alpha times cosine Theta one, which in finite dimensions bounds how far each eigenvalue must be pushed in terms of how far its eigenvector turned.

Without the off-diagonal structure, a perturbation can move eigenvalues into the gap, and none of this applies. Branch selection for general perturbations requires smallness instead.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Off-diagonal structure

\(H\sim\begin{pmatrix}0&B^*\\B&0\end{pmatrix}\), \(J=2P-I\): \(JAJ=A\), \(JHJ=-H\), so \(J(A+H)J=A-H\) and \(\sigma(A+H)=\sigma(A-H)\).
2×2: \(A=\operatorname{diag}(-2,2)\), \(H=h\begin{pmatrix}0&1\\1&0\end{pmatrix}\): \(\sigma=\{\pm\sqrt{4+h^2}\}\), \(\tan2\theta=h/2\). \(h=1\): \(\theta\approx13.28^\circ\), \(\sqrt5\approx2.236\).

### Gap survival

\(A_0\le\alpha\), \(A_1\ge\alpha+\delta\), \(c\in(\alpha,\alpha+\delta)\): \(A+H-c=\begin{pmatrix}A_0-c&B^*\\B&A_1-c\end{pmatrix}\), \(A_0-c<0\), \(A_1-c>0\); Schur complement \(A_1-c+B(c-A_0)^{-1}B^*>0\) ⇒ invertible.

### Theorem 8.1

Hypotheses: \(\mathcal O_\delta\) on reference blocks (\(A_0\le\alpha\), \(A_1\ge\alpha+\delta\)), \(H\) bounded, \(H_0=H_1=0\); for the equivalence, \(\dim D_0=\dim D_1\).

- \(\Theta\le\pi/4\iff\Lambda_0\le\alpha,\ \Lambda_1\ge\alpha+\delta\); existence: \(Q=E_{A+H}((-\infty,\alpha])\); uniqueness (formal).
- (8.1)–(8.2): \(x_0^*B^*y_1(\tan\theta-\cot\theta)=y_1^*A_1y_1-x_0^*A_0x_0\ge\delta>0\).
- (i) \(A_1-\alpha\le C_1(\Lambda_1-\alpha)C_1\), \(C_1=\cos\Theta_1\) (frames transported by the direct rotation), and the lower analogue.
- (ii) finite dimensions: \(\alpha_k-\alpha\le\|C_1\|^2(\lambda_k-\alpha)\).
- (iii) \(\Phi(\alpha_1-\alpha,\dots)\le\Phi((\lambda_1-\alpha)\cos^2\theta_1,\dots)\) for symmetric gauges \(\Phi\).

Check (\(h=2\)): \(\Lambda_1=2\sqrt2\), \(\theta=22.5^\circ\), \((2\sqrt2+2)\cos^2\theta\approx4.121\ge4\).

### Lean correspondence

Inventory entry `DK-8.1-thm` (`dev/davis-kahan-1970-formalization-result-inventory.json`), declarations in `namespace TauCeti.DavisKahan1970`; finite-dimensional eigenvalue repulsion in `DavisKahan/Sources/DavisKahan1970/Section8/Theorem81EigenvalueSource.lean`, which uses `Submodule.principalCosines` of the canonical low branch. The journal paper (§4.1) states the existence and uniqueness of the reducing subspace with \(\Theta\le\pi/4\).
