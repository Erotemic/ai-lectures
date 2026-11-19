# 018500 — Squared displacement and Q-norms

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** restricted displacement and Proposition 4.1; Ky Fan norms, dominance, and Q-norms; Lemmas 6.1 and 6.2.

<!-- BEGIN SPOKEN LECTURE -->

Squared displacement and Q-norms

The restricted displacement only tests source vectors. To compare transporters on the whole space, Davis and Kahan look at the full displacement, the identity minus W, and at its square, the identity minus W, star, times the identity minus W. For the square they prove a complete result: the direct rotation minimizes it in every unitarily invariant norm. That is Proposition 4.3, and it is correct. For the unsquared full displacement the corresponding claim, Proposition 4.4, is false. This lecture proves Proposition 4.3, derives the Q-norm consequence that repairs Proposition 4.4, and explains exactly why the squared statement does not imply the unsquared one.

Here is what we will establish. First, the squared full displacement of a transporter W is a positive operator whose quadratic form at x is the squared length of x minus W x, and whose eigenvalues are the squared singular values of the full displacement. Second, Proposition 4.3: for every transporter W and every unitarily invariant norm, the norm of the squared displacement of the direct rotation is at most the norm of the squared displacement of W. The proof pinches the squared displacement into its blocks on U and its complement, applies Proposition 4.1 to each block, and merges with Lemma 6.1. Third, the Q-norm consequence: for every norm N whose square is a unitarily invariant norm of Z star Z, the direct rotation minimizes N of the identity minus W. This includes the operator norm and the Frobenius norm, needs no restriction on the angles, and is valid in finite dimensions for every acute pair. Fourth, the gap: weak majorization of squared singular values does not imply weak majorization of the singular values themselves, because the square root is concave. The trace norm is not a Q-norm, and it is where the direct rotation can lose.

The squared displacement

For a transporter W, let G of W be the identity minus W, star, times the identity minus W. Expanding, and using that W is unitary, G of W equals two times the identity minus W minus W star. Its quadratic form at a vector x is the squared length of x minus W x, the squared displacement of x. Its eigenvalues are the squared singular values of the identity minus W.

For the direct rotation D, the sum D plus D star is twice the cosine of the angle operator Theta, which commutes with the projection P. So G of D, equal to two times the identity minus twice cosine Theta, is block diagonal with respect to U and its complement. Its block on U is the squared restricted displacement of D, with eigenvalues four sine squared of half the principal angles. Its block on the complement of U is the corresponding operator for the complementary subspaces.

Proposition 4.3

The claim is that for every transporter W, the eigenvalues of G of D are weakly majorized by those of G of W; then every unitarily invariant norm of G of D is at most that of G of W.

Step one: pinch. Write G of W in blocks relative to U and its complement. Its two diagonal blocks are P G of W P and the corresponding block on the complement. By the pinching lemma, Lemma 6.2, keeping only the diagonal blocks cannot increase any Ky Fan norm. So it suffices to show that the block-diagonal part of G of W dominates G of D.

Step two: identify the diagonal blocks. The block P G of W P is the Gram operator of the restricted displacement, the identity minus W, times P: its quadratic form at a source vector x is the squared length of x minus W x. So its eigenvalues are the squared singular values of the restricted displacement of W. Likewise the block on the complement has as eigenvalues the squared singular values of the identity minus W, times the identity minus P.

Step three: compare each block. By Proposition 4.1, every singular value of the restricted displacement of W is at least the corresponding singular value for D. The direct rotation from U to V is also the direct rotation from the complement of U to the complement of V, because complementing both subspaces does not change the angle operator or the defining block conditions. W also carries the complement of U onto the complement of V. So Proposition 4.1 applies to the complements as well. Squaring nonnegative numbers preserves order, so each diagonal block of G of W has eigenvalues at least those of the corresponding block of G of D.

Step four: merge. Lemma 6.1 says that if each diagonal block of one operator dominates the corresponding block of another in every Ky Fan norm, the block-diagonal sums do too. The block-diagonal part of G of W therefore dominates G of D, which is already block diagonal.

Chaining, every Ky Fan norm of G of D is at most the corresponding Ky Fan norm of the block-diagonal part of G of W, which is at most that of G of W. By Ky Fan dominance, every unitarily invariant norm of the squared displacement is minimized by the direct rotation.

Notice what the argument never needed: any comparison between the unsquared displacement and the restricted displacements. The pinching inequality was applied to a positive operator whose diagonal blocks are exactly the Gram operators of the restricted displacements. That is what makes the squared problem tractable.

The Q-norm consequence

A unitarily invariant norm N is a Q-norm if there is a unitarily invariant norm M with N of Z, squared, equal to M of Z star Z, for every Z. Then N of the identity minus W, squared, is M of G of W. By Proposition 4.3, M of G of D is at most M of G of W. Taking square roots, N of the identity minus D is at most N of the identity minus W.

So in every Q-norm, the direct rotation minimizes the full displacement. The operator norm is a Q-norm, with M the operator norm. The Frobenius norm is a Q-norm, with M the trace norm. The Schatten p-norms with p at least two are Q-norms. Davis and Kahan already note that Proposition 4.3 implies minimality in the operator norm and the Hilbert–Schmidt norm. The general Q-norm statement, for every acute pair in finite dimensions, real or complex, is the repair that the journal paper derives for Proposition 4.4. It requires no restriction on the angles.

Bolotnikov, Li, and Rodman had earlier studied minimal distortion problems for this class of subspace-transport constraints, including Q-norm minimization and counterexamples for Schatten norms with exponent between one and two.

Why the square root breaks majorization

Proposition 4.3 says the squared singular values of the direct rotation's displacement are weakly majorized by those of any competitor. Does it follow that the singular values themselves are weakly majorized? If so, the direct rotation would minimize every unitarily invariant norm of the unsquared displacement, which is what Proposition 4.4 claims.

It does not follow. Weak majorization is preserved by applying an increasing convex function to every entry, but the square root is concave. Here is the smallest example. The list three, three is weakly majorized by the list five, one: three is at most five, and three plus three is at most five plus one. Take square roots. The first list becomes root three, root three, with sum about three point four six. The second becomes root five and one, with sum about three point two four. Now the first sum is larger. Majorization of squares does not give majorization of square roots, and in particular it does not give the trace-norm comparison.

The paper's planar example shows the same thing with transporters. In a real plane, let U be the horizontal axis and V the line at angle theta. The direct rotation's displacement has two singular values, each two sine of theta over two. The reflection across the bisector has displacement singular values two and zero: it fixes the bisector and reverses the perpendicular direction. The squared lists are four sine squared of theta over two, twice, against four and zero. The squares of the rotation are weakly majorized by those of the reflection for every acute angle, as Proposition 4.3 requires. But the trace norms are four sine of theta over two against two. These are equal at sixty degrees, and beyond sixty degrees the reflection has the smaller trace norm. At seventy-five degrees, for example, the rotation's trace norm is about two point four four and the reflection's is two.

This is the source of the sixty-degree threshold in the printed Proposition 4.4, which asserts that for real spaces with all angles at most sixty degrees the direct rotation minimizes every unitarily invariant norm of the full displacement. In the plane the threshold is right. In four dimensions it is not, because two principal planes can be coupled, as the counterexample shows at every positive angle.

To summarize. The squared full displacement two minus W minus W star has the squared displacement singular values as eigenvalues. Pinching it relative to U and its complement leaves the Gram operators of the two restricted displacements; Proposition 4.1, applied to U and to its complement, makes each block dominate the direct rotation's block, and Lemma 6.1 merges them; so the direct rotation minimizes every unitarily invariant norm of the squared displacement. Taking square roots gives minimality in every Q-norm, including the operator and Frobenius norms, with no angle restriction. The step to the unsquared full displacement in every norm fails, because weak majorization of squares does not survive the concave square root: three, three against five, one is the smallest instance, and the planar reflection beats the direct rotation in trace norm beyond sixty degrees.

The trace norm is not a Q-norm, and it is exactly where the printed Proposition 4.4 breaks down.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Proposition 4.3

\(G(W)=(I-W)^*(I-W)=2I-W-W^*\); \(G(D)=2I-2\cos\Theta\) is block diagonal relative to \(U\oplus U^\perp\).
\[
PG(W)P=((I-W)P)^*((I-W)P),\qquad P^\perp G(W)P^\perp=((I-W)P^\perp)^*((I-W)P^\perp).
\]
Proposition 4.1 on \((U,V)\) and \((U^\perp,V^\perp)\) (the direct rotation is common to both) gives \(\lambda_k(PG(W)P)\ge\lambda_k(PG(D)P)\) and likewise on \(U^\perp\). Lemma 6.1 and Lemma 6.2:
\[
\|G(D)\|_{(k)}\le\|PG(W)P+P^\perp G(W)P^\perp\|_{(k)}\le\|G(W)\|_{(k)}\quad\forall k\ \Rightarrow\ N(G(D))\le N(G(W)).
\]

### Q-norm consequence (journal paper, Proposition in §5)

\(N(Z)^2=M(Z^*Z)\Rightarrow N(I-D)^2=M(G(D))\le M(G(W))=N(I-W)^2\). Finite-dimensional, acute, real or complex; no \(\pi/3\) restriction. Examples: operator norm, Frobenius (\(M=\|\cdot\|_1\)), Schatten \(p\ge2\).

### Square roots and majorization

\((3,3)\prec_w(5,1)\) but \(\sqrt3+\sqrt3\approx3.464>\sqrt5+1\approx3.236\).
Plane (Example 4.1): rotation \(\{2\sin\tfrac\theta2,2\sin\tfrac\theta2\}\), reflection \(\{2,0\}\); squares \(8\sin^2\tfrac\theta2\le4\); traces \(4\sin\tfrac\theta2\) vs \(2\), equal at \(60^\circ\); at \(75^\circ\): \(2.435>2\).

### Lean correspondence

`namespace TauCeti.DavisKahan1970`: `proposition4_3_compact_nonacute_idealGauge`, `proposition4_3_compact_nonacute_real_idealGauge`, `proposition4_3_compact_nonacute_symmetricNorming_complex` (inventory `DK-4.3-prop`). The Q-norm consequence and the counterexample are in `DavisKahan/FiniteDimensional/DirectRotation/` (see `TraceOptimality.lean`, `SmallAngleCounterexample.lean`).

**Note on the source proof.** The source reconstruction presents the Ky Fan comparisons (4.3)–(4.4) over principal planes in the passage that establishes Proposition 4.3; the journal paper (§5) shows that the even-index comparison (4.3) is false for a general transporter. The pinching proof above does not use (4.3).
