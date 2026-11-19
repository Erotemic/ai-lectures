# 025500 — The matching proof, I: optimal transporters split into blocks

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** the matching theorem statement; real orthogonal matrices as rotations and reflections; matrix exponentials of skew-symmetric matrices; complexification.

<!-- BEGIN SPOKEN LECTURE -->

The matching proof, part one: optimal transporters split into blocks

The matching theorem says that the cheapest real orthogonal transport of one subspace onto another, in trace norm, is assembled from blocks of dimension two and four, each carrying one or two principal angles. Building such transporters from a matching is easy. The hard direction is to show that an optimal transporter can always be found among them: that no cleverer coupling of three or more principal planes ever does better. This lecture proves the structural half of that claim. Starting from a global minimizer of a smoothed cost, we use its first-order optimality conditions to split the space into perpendicular blocks, each preserved by the source projection, the target projection, and the transporter, and each of dimension two or four. The next lecture computes the cheapest transporter on each kind of block and passes to the trace norm.

Here is the plan, following the six steps of the journal paper's proof. Step one: replace the trace norm, which is not differentiable, by the sum of p-th powers of the displacement singular values, for an exponent p between one and two, and take a global minimizer, which exists by compactness. Step two: differentiate the cost along curves of transporters obtained by composing with rotations that preserve the source subspace; the derivative is a trace pairing with a skew-symmetric spectral gradient, and stationarity forces that gradient to couple the source subspace only to its complement. Step three: on each positive level of the gradient, the gradient defines a complex structure, the transporter becomes a complex unitary with at most two eigenphases, and the reflection through the source acts as complex conjugation; common invariant subspaces of these objects give real blocks of dimension two or four. The space where the gradient vanishes contributes only fixed directions and planes with one angle.

Step one: a smooth cost and a minimizer

The trace norm of the identity minus W is the sum of the singular values of the displacement. As a function of a singular value s, the summand is s itself, which behaves like an absolute value near zero and is not differentiable there. Displacements typically do have zero singular values, as the counterexample's competitor did, so the trace norm has corners exactly where optimal transporters tend to live.

The remedy is to raise the singular values to a power p slightly above one. Define the cost Phi p of W to be the sum over all singular values of the identity minus W of that singular value to the power p. For p greater than one, s to the p has derivative zero at s equal to zero, and the cost is differentiable even where singular values vanish. We take p between one and two; at the end, we let p decrease to one.

The feasible set is the set of real orthogonal matrices W with W carrying K onto L, equivalently W P K W transpose equals P L, where P K and P L are the projections. It is nonempty: send an orthonormal basis of K to one of L, and extend to the complements. It is closed, since the constraint is an equation, and bounded, since orthogonal matrices have norm one. So it is compact, the cost is continuous, and a global minimizer exists. Fix one and call it W.

Two additivity facts make blocks useful. Suppose the space splits into perpendicular subspaces, each preserved by P K, P L, and W. In a basis adapted to the split, all three are block diagonal, so the displacement is block diagonal, its singular values are the union of the blocks' singular values, and the cost Phi p is the sum of the blocks' costs. And the compression of P L to K is block diagonal too, so the list of principal angles of K and L is the union of the blocks' lists. If we can split the space into such blocks, each carrying one or two angles, the angle labels are partitioned into singletons and pairs, which is a matching.

Step two: derivatives along feasible curves

To extract information from minimality, we need curves of feasible transporters through W. Here is a supply. Let Omega be a skew-symmetric matrix, so Omega transpose equals minus Omega. Then e to the t Omega is orthogonal for every real t, because its transpose is e to the minus t Omega, its inverse. If Omega also commutes with P K, then so does e to the t Omega, which therefore maps K onto itself. So W times e to the t Omega first rotates K within itself and then applies W: it is still a feasible transporter. Since W is a minimizer, the derivative of the cost along every such curve, at t equal to zero, must vanish.

To compute the derivative, recall that every real orthogonal matrix decomposes into perpendicular pieces: lines where it acts as one, lines where it acts as minus one, and planes where it acts as a rotation through some angle between zero and one hundred eighty degrees. On a rotation plane with angle t, the displacement has two singular values, each two sine of t over two. So that plane contributes twice phi of t to the cost, where phi of t is two sine of t over two, raised to the power p.

Define the spectral gradient G: on each rotation plane of W with angle t, G is phi prime of t times the quarter-turn on that plane, and on the lines where W acts as plus or minus one, G is zero. G is skew-symmetric and commutes with W, because on each plane both are combinations of the identity and the same quarter-turn.

The first-variation formula is: the derivative of Phi p of W e to the t Omega, at t equal to zero, equals minus the trace of G times Omega, for every skew-symmetric Omega. Why? To first order, only the part of Omega that turns each rotation plane within itself changes the cost. If Omega turns a plane with angle t at rate b, the plane's angle becomes t plus b times the time, and its cost changes at rate twice b times phi prime of t. The trace pairing gives the same: minus the trace of phi prime of t times the quarter turn, times b times the quarter turn, is twice b phi prime of t, because the quarter turn squares to minus the identity. The parts of Omega that mix different planes contribute nothing to first order: changing the sign of one whole plane is a symmetry of W, and averaging over such symmetries cancels the mixing parts without changing the derivative.

Now impose stationarity, the vanishing of this derivative for every feasible Omega. Choose the particular direction Omega equal to P K times G times P K. It is skew-symmetric, and it commutes with P K. Stationarity gives zero equals minus the trace of G times P K G P K, which by cyclicity of trace is minus the trace of the square of P K G P K. For a skew-symmetric matrix A, minus the trace of A squared is the sum of the squares of its entries. So the block of G inside K, P K G P K, is zero. The same argument with the identity minus P K in place of P K shows that the block of G inside the complement of K is zero.

So, at a minimizer, the spectral gradient has no component that turns K within itself or turns the complement within itself. It only couples K to its complement. Equivalently, let J K be the reflection through K, two P K minus the identity. Then J K times G times J K equals minus G: the source reflection anticommutes with the gradient. This single identity is the source of the block structure.

Step three: blocks with one or two source directions

The rotation planes of W used to define G need not respect K. The task now is to build blocks that respect both W and K.

Start with the positive levels of the gradient. The matrix minus G squared is symmetric and nonnegative, since its quadratic form at x is the squared length of G x. Decompose the space into its eigenspaces. On an eigenspace with positive eigenvalue g squared, the operator G divided by g squares to minus the identity and preserves lengths. Such an operator is a complex structure: declare multiplication by i to be G over g, and the eigenspace becomes a complex vector space, with a real plane spanned by x and G x over g becoming a single complex line.

Three things happen on this complex space. First, W commutes with G, so it is complex-linear, and since it preserves lengths it is a complex unitary. Second, the source reflection J K anticommutes with G, so it reverses the complex structure: J K applied to a times x, for a complex number a, is the conjugate of a times J K x. Together with J K squared equal to the identity, this says J K acts as complex conjugation. Third, W has few eigenphases here. On this level, every rotation angle t of W satisfies phi prime of t equals g. The function phi prime first increases and then decreases on the interval from zero to one hundred eighty degrees, because its derivative changes sign exactly once, where the tangent squared of t over two equals p minus one. A horizontal line at height g therefore meets it at most twice. So W acts on the level as e to the i phi one on one subspace and e to the i phi two on its complement, with at most two phases.

We want subspaces preserved by both W and J K. W is preserved by any subspace that the projection Pi onto the first phase space preserves. So we want common invariant subspaces of Pi and of conjugation. Write Pi in coordinates in which J K is ordinary conjugation, as a real part plus i times an imaginary part, both real matrices. Because Pi is a self-adjoint projection, the real part is symmetric and the imaginary part is skew-symmetric, and they satisfy two algebraic relations coming from Pi squared equals Pi.

Those relations make small common blocks appear. Take an eigenvector u of the real part, with eigenvalue lambda strictly between zero and one. Then the imaginary part maps u to a vector perpendicular to u, of length the square root of lambda times one minus lambda; normalize it to get v. The real part sends v to one minus lambda times v, and the imaginary part sends v back to a multiple of u. So the real span of u and v is preserved by both parts. When lambda is zero or one, the imaginary part kills u, and the line through u is preserved by itself. Peeling off such lines and planes one at a time, which is possible because the real part is symmetric and the imaginary part skew, exhausts the space.

Now return to the original real space. The complex span of the pair u, v is the real span of four vectors: u, v, and their images under G over g. The first two are fixed by conjugation, so they lie in K; the last two are negated by conjugation, so they lie in the complement of K. That is a four-dimensional real block, preserved by W and by P K, with two source directions. Since P L equals W P K W transpose, it is preserved by P L as well, and so its principal-angle list has two entries. A complex line through a single u gives a two-dimensional real block with one source direction and one angle.

The space where the gradient vanishes

What remains is the kernel of G. There, every rotation angle t of W satisfies phi prime of t equals zero. Phi prime vanishes only at zero and at one hundred eighty degrees, so W has eigenvalues plus one and minus one on the kernel: it is a reflection there, possibly with trivial parts.

Two projections now act on the kernel: P K, and the projection onto the minus-one eigenspace of W. Halmos's two-subspace decomposition splits the kernel into lines and planes preserved by both, and so by W. On a line, the source and target are each either the whole line or zero, and they agree. If W acts as minus one on such a line, replacing minus one by plus one keeps the source and target and lowers the cost by two to the p, the cost of a displacement singular value two. That cannot happen at a global minimizer. So the remaining blocks in the kernel are fixed directions, where W is the identity, and planes containing one source direction, where W reflects.

The structure of a minimizer

Putting the pieces together: at a global minimizer W of the smoothed cost, the whole space splits into perpendicular blocks, each preserved by P K, P L, and W, of three kinds. Fixed directions, with no angle and no cost. Two-dimensional blocks, each containing one source direction and so carrying one principal angle. And four-dimensional blocks, each containing two source directions and so carrying two principal angles. Because the cost and the angle list both add over blocks, every principal angle belongs to exactly one block, and the blocks with two angles pair up their labels. A minimizer therefore determines a matching.

Two things remain, and they are the subject of the next lecture. First, on each block, W must be the cheapest transporter of that block, since otherwise replacing it there would lower the global cost; so we must compute the minimal cost of a one-angle plane and of a two-angle four-dimensional block. Second, everything here used an exponent p greater than one, and we must let p decrease to one to recover the trace norm.

To summarize. Replacing the trace norm by the sum of p-th powers of displacement singular values, with p between one and two, makes the cost differentiable, and compactness gives a global minimizer W. Composing W with rotations that preserve K gives feasible curves, and the derivative of the cost along them is minus the trace of the spectral gradient G times the rotation generator. Stationarity forces the blocks of G inside K and inside its complement to vanish, so the source reflection anticommutes with G. On each positive level of G, G defines a complex structure, W becomes a unitary with at most two phases, and the source reflection becomes conjugation; their common invariant subspaces are real blocks of dimension two or four, carrying one or two source directions. On the kernel of G, W is a reflection, and minimality removes useless sign flips. So a minimizer splits into fixed directions, one-angle planes, and two-angle four-dimensional blocks.

Nothing in the argument allows a block with three or more angles. That is the structural content of the matching theorem: optimal real transports only ever couple principal planes in pairs.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Step 1

\(\mathcal F=\{W\in O(n):W P_KW^T=P_L\}\) compact, nonempty; \(\Phi_p(W)=\sum_js_j(I-W)^p\), \(1<p<2\), differentiable. Block additivity: if \(\mathbb R^n=\bigoplus_aM_a\) with each \(M_a\) invariant under \(P_K,P_L,W\), then \(\Phi_p(W)=\sum_a\Phi_p(W|_{M_a})\) and the principal-angle lists merge.

### Step 2

\(\Omega^T=-\Omega\), \([\Omega,P_K]=0\Rightarrow We^{t\Omega}\in\mathcal F\). \(\varphi(t)=(2\sin\tfrac t2)^p\); on a rotation plane of angle \(\vartheta\): \(W=\cos\vartheta I_2+\sin\vartheta J\), \(G=\varphi'(\vartheta)J\); \(G=0\) on \(\pm1\) eigenspaces; \([G,W]=0\).
\[
\frac{d}{dt}\Phi_p(We^{t\Omega})\Big|_{t=0}=-\operatorname{tr}(G\Omega).
\]
\(\Omega=P_KGP_K\): \(0=-\operatorname{tr}((P_KGP_K)^2)=\|P_KGP_K\|_F^2\); likewise for \(P_K^\perp\). Hence \(G=\begin{pmatrix}0&G_{01}\\-G_{01}^T&0\end{pmatrix}\), \(J_KGJ_K=-G\), \(J_K=2P_K-I\).

### Step 3

\(-G^2\ge0\); on the \(g^2\)-eigenspace \(N\): \(\mathcal J=G/g\), \(\mathcal J^2=-I\); \(W|_N\) complex unitary; \(J_K\mathcal J=-\mathcal JJ_K\) (conjugation).
\(\varphi'(t)=p(2\sin\tfrac t2)^{p-1}\cos\tfrac t2\), \(\varphi''(t)=p(2\sin\tfrac t2)^{p-2}((p-1)\cos^2\tfrac t2-\sin^2\tfrac t2)\): one sign change at \(\tan^2\tfrac t2=p-1\), so \(\varphi'(t)=g\) has at most two roots; \(W|_N=e^{i\varphi_1}\Pi+e^{i\varphi_2}(I-\Pi)\).
\(\Pi=\mathcal R+i\mathcal I\): \(\mathcal R^T=\mathcal R\), \(\mathcal I^T=-\mathcal I\), \(\mathcal R^2-\mathcal I^2=\mathcal R\), \(\mathcal R\mathcal I+\mathcal I\mathcal R=\mathcal I\). For \(\mathcal Ru=\lambda u\), \(0<\lambda<1\): \(\kappa=\sqrt{\lambda(1-\lambda)}\), \(v=\mathcal Iu/\kappa\); \(\mathcal Rv=(1-\lambda)v\), \(\mathcal Iu=\kappa v\), \(\mathcal Iv=-\kappa u\). Real block \(\operatorname{span}\{u,v,\mathcal Ju,\mathcal Jv\}\) (two source directions); \(\lambda\in\{0,1\}\): \(\operatorname{span}\{u,\mathcal Ju\}\) (one).
Kernel of \(G\): \(W\) has eigenvalues \(\pm1\); a one-dimensional \(-1\) block can be flipped to \(+1\), lowering \(\Phi_p\) by \(2^p\).

### Lean correspondence

All under `DavisKahan/FiniteDimensional/DirectRotation/` (journal paper, comment after the proof): `SchattenRealDecomposition.lean`, `SchattenRealRestrictions.lean` (block reduction); gradient and stationarity files such as `SchattenGradientSpectrum.lean`, `SchattenGradientKernel.lean`, `SchattenGradientNoMixing.lean`, `SchattenNoMixing.lean`; smoothed variants `SmoothedPower*.lean`.
