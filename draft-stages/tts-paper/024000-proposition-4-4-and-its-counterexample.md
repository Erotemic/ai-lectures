# 024000 — Proposition 4.4 and its counterexample

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** the direct rotation; restricted and squared displacement; Ky Fan norms; Q-norms; real and complex transports.

<!-- BEGIN SPOKEN LECTURE -->

Proposition 4.4 and its counterexample

Of the twenty-nine results of the 1970 Davis–Kahan paper that the journal paper examines, twenty-eight are true as stated. The twenty-ninth, Proposition 4.4, is false. It claims that for real subspaces whose principal angles are all at most sixty degrees, the direct rotation minimizes every unitarily invariant norm of the full displacement. This lecture constructs a counterexample at every positive acute angle, computes everything in it, identifies the step in the printed proof that fails, and places the result in its history.

Here is what we will establish. First, in real four-dimensional space, for every angle theta strictly between zero and ninety degrees, there are two planes U and V with both principal angles equal to theta, and an orthogonal map W carrying U onto V, such that the trace norm of the identity minus W is four sine theta, while for the direct rotation it is eight sine of theta over two, which is larger. Taking theta small gives a counterexample to the printed claim with angles as small as we like, far below sixty degrees. Second, the competitor is a global minimizer: no orthogonal map carrying U onto V has smaller trace-norm displacement, because the trace norm of P minus Q, which is four sine theta, is a lower bound for every transporter. Third, the operator norm ranks the two maps the other way, as it must, since it is a Q-norm. Fourth, the printed proof uses a comparison that adds Ky Fan norms of the displacement restricted to separate principal planes; at forty-five degrees the restrictions of the competitor's displacement to the two principal planes both land in the same two-dimensional plane, so their contributions cannot be added, and the comparison fails. Fifth, the competitor is the realification of a complex phase example that Davis and Kahan themselves gave, and four is the smallest dimension in which the trace-norm claim fails.

The claim

Recall the setting. A transporter is an orthogonal or unitary map W of the whole space with W carrying U onto V. The full displacement is the identity minus W. Proposition 4.3 shows the direct rotation minimizes every unitarily invariant norm of the squared displacement, and hence every Q-norm of the displacement, such as the operator and Frobenius norms. Davis and Kahan also give two examples showing that the unsquared statement fails in general. In a real plane, when the angle exceeds sixty degrees, the reflection across the bisector beats the direct rotation in the trace norm. And in a complex plane, multiplying the direct rotation by a phase lowers the trace norm at any angle.

Proposition 4.4 then claims that in a real space, if every principal angle is at most sixty degrees, neither obstruction applies, and the direct rotation minimizes every unitarily invariant norm of the full displacement. The sixty-degree threshold is exactly where the planar reflection starts to win, and the restriction to real spaces excludes the complex phase.

Building the counterexample

Work in real four-dimensional space with coordinates one through four, and fix an angle theta between zero and ninety degrees. Let c be cosine theta and s be sine theta.

The source plane U is spanned by e one and e two. The target plane V is spanned by two orthonormal vectors: y one, with coordinates c, zero, zero, s, and y two, with coordinates zero, c, minus s, zero. So y one tilts e one toward the fourth axis by theta, and y two tilts e two toward the third axis, in the negative direction, by theta. The overlap matrix of the two bases is c times the two by two identity, so both principal angles equal theta. The principal planes are the plane of e one and e four, and the plane of e two and e three.

The direct rotation D turns each principal plane through theta. Its displacement, the identity minus D, has four singular values, each two sine of theta over two, one pair from each principal plane. So the trace norm of the identity minus D is eight sine of theta over two.

The competitor W is built differently. Consider two other planes: the plane M spanned by e one plus e three and e two plus e four, and the perpendicular plane Z spanned by e one minus e three and e two minus e four. Let W rotate M through twice theta and leave Z fixed. Then W is orthogonal. A direct computation shows that W sends e one to c times y one plus s times y two, and e two to a similar combination, so W carries U onto V. It is a transporter.

Its displacement is zero on Z, because W fixes Z, and on M it is the displacement of a rotation through two theta, with two singular values, each two sine theta. So the identity minus W has singular values two sine theta, two sine theta, zero, zero, and its trace norm is four sine theta.

Compare. Four sine theta equals eight sine of theta over two times cosine of theta over two, by the double-angle formula. Since cosine of theta over two is less than one, four sine theta is strictly less than eight sine of theta over two, at every angle between zero and ninety degrees. At forty-five degrees the numbers are about two point eight three for the competitor and three point zero six for the direct rotation. At twenty degrees they are about one point three seven and one point three nine. The gap shrinks as the angle shrinks, but it never closes.

Given any positive bound, choose theta below both that bound and sixty degrees. Then every principal angle is at most sixty degrees, the space is real, and the direct rotation does not minimize the trace norm of the full displacement. Proposition 4.4 is false, with no positive threshold below which it holds.

Why the competitor is optimal

The competitor is not just better than the direct rotation. It is the best possible transporter in trace norm.

Here is a lower bound valid for every transporter W and every unitarily invariant norm. Since W carries U onto V, W P W star equals Q, so P minus Q equals P minus W P W star. Multiply on the right by W: P minus Q, times W, equals P W minus W P, the commutator of P with W. The commutator of P with W equals the commutator of P with W minus the identity, because the identity commutes with everything. And the commutator of a projection with any operator K picks out only the off-diagonal blocks of K, relative to the projection, with a sign flip on one of them. By the pinching lemma, the off-diagonal part of K is no larger than K in any unitarily invariant norm. Putting it together, every unitarily invariant norm of P minus Q is at most the same norm of the identity minus W.

In the four-dimensional example, the trace norm of P minus Q is twice the sum of the sines of the two principal angles, which is four sine theta. The competitor's displacement has trace norm exactly four sine theta, so it attains the lower bound. It is a global minimizer of the trace-norm displacement among all orthogonal transporters, real or complex.

The operator norm disagrees

In the operator norm the order reverses. The direct rotation's displacement has operator norm two sine of theta over two, while the competitor's has operator norm two sine theta, which is larger. That must happen, because the operator norm is a Q-norm, and Proposition 4.3 guarantees the direct rotation wins in every Q-norm. The Frobenius norm agrees with the operator norm here. The two displacement singular-value lists, four copies of two sine of theta over two against two copies of two sine theta and two zeros, are not comparable by weak majorization: one has the smaller maximum, the other the smaller sum. No single transporter can be best in every unitarily invariant norm.

Where the printed proof fails

The paper's argument for the unsquared displacement compares Ky Fan norms through restrictions to the principal planes. For an even index nu, it uses the inequality: the Ky Fan nu norm of the full displacement K is at least the sum, over the first nu over two principal planes, of the Ky Fan two-norm of K restricted to that plane. This is equation 4.3 of the paper.

Test it at forty-five degrees with the competitor. Let K be the identity minus W, and take nu equal to four, with the two principal planes, that of e one and e four and that of e two and e three. The Ky Fan four-norm of K is its trace norm, two root two, about two point eight three. The restriction of K to the first principal plane has singular values one and one, so its Ky Fan two-norm is two. The same holds for the second principal plane. The inequality would require two root two to be at least two plus two, which is four. It is not.

Why does the inequality fail? Look at where the restricted maps send their inputs. K kills the fixed plane Z and maps everything into the moving plane M. So K restricted to the first principal plane maps onto M, and K restricted to the second principal plane also maps onto M. Both restrictions land in the same two-dimensional output space. Adding their Ky Fan norms treats them as if they had perpendicular images, as they would in a block-diagonal operator. Here they share an image, and the total singular-value budget of K is only what fits in that one plane. A direct-sum comparison needs perpendicular inputs and perpendicular outputs; the competitor provides the first but not the second.

The direct rotation, by contrast, maps each principal plane into itself, so its restrictions do have perpendicular images, and for it the comparison is an equality. The error in the printed proof is to assume that every transporter decomposes over the principal planes in that way.

The squared displacement does not have this problem. Its pinching argument only needs the Gram operators of the restricted displacements, which live on the input side, where the principal planes are perpendicular. That is why Proposition 4.3 survives and Proposition 4.4 does not.

A complex example made real

The construction was not pulled from nowhere. Davis and Kahan's own Example 4.2 works in a complex plane: multiplying the direct rotation by the phase e to the i theta keeps the source line on the target line and lowers the trace norm of the displacement from four sine of theta over two to two sine theta. Identify complex two-dimensional space with real four-dimensional space, letting multiplication by i act as a quarter turn on suitable pairs of real coordinates. Under that identification the complex direct rotation becomes the real direct rotation D above, and the phased map becomes the competitor W. Realification doubles every singular-value multiplicity, which is why the competitor's list has two copies of two sine theta. The restriction to real spaces in Proposition 4.4 was meant to exclude the phase, but in four real dimensions a coupled pair of planes can imitate it.

Smaller dimensions do not suffice. In real spaces of dimension at most three, under the printed hypotheses, the direct rotation does minimize the trace norm of the full displacement; four is the smallest dimension in which the trace-norm claim fails.

History

Bolotnikov, Li, and Rodman, in 2001, studied minimal distortion problems for unitary maps carrying one subspace onto another, proved Q-norm optimality, and gave counterexamples for Schatten norms with exponent between one and two. Qiu, Zhang, and Li later repeated the sixty-degree assertion, and Zhang and Qiu noted in 2010 that trace-norm minimality fails in general, without addressing the particular real, small-angle restriction. As far as the journal paper's authors could determine, the contradiction of the printed real claim at every positive angle had not previously been made explicit.

To summarize. In real four-dimensional space, for each angle theta between zero and ninety degrees, the planes spanned by e one, e two and by c e one plus s e four, c e two minus s e three have both principal angles theta. The direct rotation has trace-norm displacement eight sine of theta over two, while the map rotating the plane of e one plus e three and e two plus e four through two theta, and fixing its complement, has trace-norm displacement four sine theta, which is smaller and equals the universal lower bound, the trace norm of P minus Q. So Proposition 4.4 fails at arbitrarily small angles. The failed step is the inequality 4.3, which adds Ky Fan norms of restrictions to separate principal planes; for the competitor those restrictions share an output plane. The valid replacement is the Q-norm statement, which follows from the squared-displacement result, Proposition 4.3.

The counterexample also raises a new question. If the direct rotation is not the trace-norm minimizer, what is the minimum, for an arbitrary pair of real subspaces with arbitrary principal angles? The answer is a matching problem on the principal angles.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Construction (journal paper, Theorem in §5)

\(c=\cos\theta\), \(s=\sin\theta\), \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), \(C=\cos2\theta\,I_2+\sin2\theta\,J\), \(H=\tfrac1{\sqrt2}\begin{pmatrix}I_2&I_2\\I_2&-I_2\end{pmatrix}\):
\[
W_\theta=H\begin{pmatrix}C&0\\0&I_2\end{pmatrix}H^T=\begin{pmatrix}c^2I+scJ&-s^2I+scJ\\-s^2I+scJ&c^2I+scJ\end{pmatrix},\qquad Y=\begin{pmatrix}cI_2\\sJ\end{pmatrix},\quad X^TY=cI_2,
\]
\[
D_\theta=\begin{pmatrix}cI_2&sJ\\sJ&cI_2\end{pmatrix},\quad T=QP+(I-Q)(I-P)=c\,D_\theta,\quad (I-D_\theta)^T(I-D_\theta)=(2-2c)I_4 .
\]
\(s(I-W_\theta)=(2s,2s,0,0)\), \(\|I-W_\theta\|_1=4\sin\theta\); \(s(I-D_\theta)=(2\sin\tfrac\theta2)^{\times4}\), \(\|I-D_\theta\|_1=8\sin\tfrac\theta2\). Operator norms: \(2\sin\tfrac\theta2<2\sin\theta\).
Numbers: \(45^\circ\): \(2.828\) vs \(3.061\); \(20^\circ\): \(1.368\) vs \(1.389\).
\(W_{\pi/4}=\tfrac12\begin{pmatrix}1&-1&-1&-1\\1&1&1&-1\\-1&-1&1&-1\\1&-1&1&1\end{pmatrix}\).

### Lower bound

\((P-Q)W=PW-WP=[P,W-I]=P(W-I)P^\perp-P^\perp(W-I)P\), so \(N(P-Q)\le N(\text{off-diagonal part of }I-W)\le N(I-W)\) (Lemma 6.2). \(\|P-Q\|_1=2\sum\sin\theta_i=4\sin\theta\).

### Failure of (4.3) at \(\theta=\pi/4\)

\(K=I-W_{\pi/4}\), \(\Omega_1=\operatorname{span}\{e_1,e_4\}\), \(\Omega_2=\operatorname{span}\{e_2,e_3\}\): \(\|K\|_{(4)}=2\sqrt2\), \(\|K\Omega_1\|_{(2)}=\|K\Omega_2\|_{(2)}=2\); \(\operatorname{ran}K\Omega_1=\operatorname{ran}K\Omega_2=\operatorname{span}\{e_1+e_3,e_2+e_4\}\).

### Realification

\(D^{\mathbb C}=\begin{pmatrix}c&is\\is&c\end{pmatrix}\), \(W^{\mathbb C}=e^{i\theta}D^{\mathbb C}\) (Example 4.2) become \(D_\theta,W_\theta\) under \(\mathbb C^2\cong\mathbb R^4\), \(i\mapsto J\).

### Lean correspondence

`namespace TauCeti.DavisKahan1970`: `proposition4_4_printedStatement`, `proposition4_4_refuted`, `proposition4_4_refutingPair` (inventory `DK-4.4-prop`).
`DavisKahan/FiniteDimensional/DirectRotation/SmallAngleCounterexample.lean`: `principalAngles_eq` (both angles \(\theta\)); `TraceOptimality.lean`: `traceDisplacement_lower_bound`, `Wequiv_traceMinimizer`.
`DavisKahan/FiniteDimensional/DirectRotation/DimensionMinimality.lean`: `nuclear_directRotation_le_of_finrank_le_three` (trace-norm minimality in real dimension at most three under the printed hypotheses) and `isLeast_real_shortAngle_nuclear_counterexample_dimension` (four is least).
In these sources the coordinates are 0-indexed (\(e_0,\dots,e_3\)).
