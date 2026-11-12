# 000000 — The problem and the paper

**Track:** G3 audio paper track. **Draft:** careful second pass, 12 November 2026. **Section:** orientation. **Audience:** linear algebra, eigenvalues and eigenvectors of symmetric matrices, singular values, inner-product notation.

<!-- BEGIN SPOKEN LECTURE -->

The problem and the paper

When a symmetric matrix or a self-adjoint operator changes a little, its eigenvalues change a little. Its eigenvectors may not. This course is about the theory that says exactly when and how far an eigenvector, or more precisely an eigenspace, can move: the Davis–Kahan theory, from the 1970 paper by Chandler Davis and William Kahan titled The Rotation of Eigenvectors by a Perturbation, Part Three. It is also about a recent journal paper that formalizes that paper, proving its results in a computer proof assistant one at a time. In doing so it finds that one of the 1970 propositions is false, gives a counterexample, proves the correct replacement, and solves the optimization problem that the counterexample exposes. The goal of the course is that a careful listener can read both papers, follow their proofs, and know exactly what each theorem assumes.

This first lecture states the problem, works one small example that already contains the main theorem, describes the results of both papers in plain terms, and explains why the course takes the order it does.

Eigenvalues are stable, eigenvectors need a gap

Start with what is true about eigenvalues. List the eigenvalues of a symmetric matrix in increasing order, do the same for a second symmetric matrix, and compare them position by position. Weyl's inequality says that no eigenvalue moves by more than the size of the difference between the two matrices, where size means the largest stretching factor, the operator norm. Eigenvalues are stable.

The journal paper shows in two dimensions why nothing like this holds for eigenvectors. Fix a small positive number epsilon. Let A be the diagonal matrix with entries zero and epsilon, and let A hat be the diagonal matrix with entries epsilon and zero. The two matrices have the same eigenvalues, zero and epsilon, and their difference has size epsilon. But the eigenvector of A for the eigenvalue zero is the horizontal axis, and the eigenvector of A hat for zero is the vertical axis. A perturbation of size epsilon has turned the eigenvector for zero through ninety degrees.

A listener might object that nothing really moved here: the two axes are eigenvectors of both matrices, and only the eigenvalues traded places. The objection is fair, and a family of examples answers it. Keep A as before, with eigenvalue zero on the horizontal axis and eigenvalue epsilon on the vertical axis. Now pick an angle phi and turn the whole picture through phi. That gives a matrix A hat with the same eigenvalues, zero and epsilon, whose eigenvector for zero is the line at angle phi above the horizontal axis, and whose eigenvector for epsilon is the line perpendicular to it. Here the eigenvector genuinely turns, through any angle we choose.

How large is the perturbation H, equal to A hat minus A? Each of the two matrices is epsilon times the orthogonal projection onto one line: the vertical axis for A, and the vertical axis turned through phi for A hat. The difference of the projections onto two lines that meet at angle phi has operator norm the sine of phi. So the norm of H is epsilon times the sine of phi.

Read that relation in reverse. A perturbation of size eta, no larger than epsilon, can turn the eigenvector through the angle whose sine is eta over epsilon. If eta is much smaller than the gap epsilon between the two eigenvalues, that angle is small, about eta over epsilon in radians. As eta grows toward epsilon, the angle grows toward ninety degrees, and at phi equal to ninety degrees the turned matrix is exactly the swapped one from before. So the movement of an eigenvector is governed by the size of the perturbation relative to the gap between eigenvalues, and when the two are comparable, nothing prevents the eigenvector from turning all the way.

One more feature of the problem changes what we should measure. When eigenvalues repeat or cluster tightly, individual eigenvectors are not even determined; any orthonormal basis of the repeated eigenspace will do. What is determined is the subspace spanned by all the eigenvectors for the cluster. So the right question concerns subspaces: given a gap separating a wanted part of the spectrum from the rest, how far can the corresponding spectral subspace move?

Two ways to ask the question

The question comes in two forms, and the 1970 paper treats both.

In the perturbation form, we know an operator A and its spectral subspaces, and the operator we care about is A hat, equal to A plus a perturbation H. How far is the spectral subspace of A hat from the corresponding one of A?

In the residual form, we have an approximate subspace, called a trial subspace, from a numerical method or a model, together with a trial operator describing how A hat acts on it. The residual measures how far the trial subspace is from being invariant: apply A hat to the trial vectors, subtract what the trial operator predicts, and measure what is left. How far can the trial subspace be from the exact spectral subspace of A hat?

The two forms meet. If the trial subspace is a spectral subspace of A and the trial operator is A's action there, then A already maps the trial subspace into itself as predicted, and the residual is just the perturbation H applied to the trial subspace. Its size is at most the size of H.

The journal paper opens with the way this is used in practice, which runs in the other direction. Often we observe the perturbed operator and the reference operator is unknown: a sample covariance matrix is observed, and the population covariance it estimates is not. Take an eigenspace computed from the observed matrix as the trial subspace for the unknown one. The residual is then the difference of the two matrices applied to that eigenspace, so its size is at most the size of the difference. That bound can be available, for instance from probability estimates, even though neither the unknown matrix nor the residual itself can be computed. The gap still has to be checked against the unknown matrix's spectrum, and Weyl's inequality helps here, because it places the unknown eigenvalues within the size of the difference of the observed ones.

The answer, in one line

Davis and Kahan's sine-theta theorem says: delta times the size of the sine of the angle between the trial subspace and the exact subspace is at most the size of the residual. Here delta is a gap between the spectrum of the trial operator and the unwanted part of the spectrum of the exact operator. The angle is an operator, whose eigenvalues, when it has them, are the principal angles between the two subspaces.

The turned family shows the theorem at work, and shows that it cannot be improved. Take the horizontal axis as the trial subspace, with trial operator zero, which is how A acts there. Apply A hat to the horizontal unit vector. A hat is epsilon times the projection onto the turned vertical line, and the horizontal unit vector has a component of length sine phi along that line, so the residual has length epsilon times sine phi. The trial eigenvalue is zero, and the unwanted eigenvalue of A hat is epsilon, so the gap delta is epsilon. The angle between the trial subspace and the exact one is phi. So delta times the sine of the angle is epsilon times sine phi, and the residual is also epsilon times sine phi. The two sides are equal, for every phi. The 1970 paper remarks that the constants in all four of its main theorems are best possible for exactly this reason: two-dimensional examples attain them.

Every word in the theorem's sentence carries a condition, and much of the course is about those conditions. The angle is an operator because subspaces of dimension more than one meet at a list of angles, and in infinite dimensions possibly at a continuum of them. The size can be any unitarily invariant norm: the largest sine, the square root of the sum of squared sines, the sum of the sines, or any of infinitely many others, and the theorem holds for all of them at once. The gap must have the right shape. Either the trial spectrum lies in an interval and the unwanted spectrum lies outside that interval enlarged by delta on each side, or the reverse, or one spectrum lies entirely below a cut point and the other entirely above it. If the two spectra only stay a distance delta apart while interleaving, part of the theorem survives: the bound with constant one still holds when size means the square root of the sum of squared sines, but a bound on the largest sine then needs a constant larger than one. Finally, the operators may be unbounded, like differential operators, provided their domains and the residual are handled correctly.

The 1970 paper has four headline theorems, bounding the sine of the angle, the tangent of the angle, the sine of twice the angle, and the tangent of twice the angle. They differ in their hypotheses and in which operators the gap compares. The sine theorem compares the trial operator with the unwanted part of the exact operator. The tangent theorem compares the same two operators, but needs the unwanted spectrum entirely on one side of the trial spectrum, and needs the perturbation to have no part acting within the trial subspace; in return it bounds the tangent, which is larger than the sine. The doubled-sine theorem compares the wanted and unwanted parts of the perturbed operator with each other, and the doubled-tangent theorem compares the two parts of the reference operator, with the perturbation acting only between them. Neither doubled-angle theorem involves the trial operator in its gap, and both pay a price for it: a small sine of twice an angle could mean an angle near zero or an angle near ninety degrees.

The transport question

The 1970 paper also asks a second kind of question. Given two subspaces, which unitary map of the whole space carries one onto the other while moving everything as little as possible? The natural candidate is the direct rotation. In the basic case, where every principal angle between the two subspaces is less than ninety degrees, it turns each principal plane through its own angle and leaves everything perpendicular to those planes alone. Davis and Kahan prove that, among all unitary maps carrying the first subspace onto the second, it minimizes the displacement of vectors in the first subspace, in every unitarily invariant norm. They also prove that it minimizes the square of the displacement of all vectors, again in every such norm. Then, in Proposition 4.4, they claim that for real spaces with all principal angles at most sixty degrees, it also minimizes the unsquared displacement of all vectors in every such norm.

That claim is false. In real four-dimensional space, take two planes whose two principal angles are both equal to theta. The direct rotation turns each of the two principal planes through theta. Its displacement, the identity minus the rotation, has four singular values, each equal to twice the sine of half theta, so its trace norm, the sum of the singular values, is eight times the sine of half theta. There is another orthogonal map carrying the first plane onto the second, which couples the two principal planes: it fixes one plane and rotates the complementary plane through twice theta. Its displacement has two singular values equal to twice the sine of theta and two equal to zero, so its trace norm is four times the sine of theta. By the double-angle formula, four sine theta equals eight sine of half theta times cosine of half theta, and the cosine is less than one. So the coupled map moves the space less, in trace norm, at every acute angle theta, including every angle in the proposition's sixty-degree range. This construction is a real form of a complex example that Davis and Kahan themselves gave.

The journal paper locates the step that fails in the printed proof, a comparison of sums of largest singular values that does not hold. It then proves the correct replacement. The squared result implies the unsquared one for every norm N with the following property: the square of N at an operator T equals some unitarily invariant norm of T star T. These are called Q-norms. That class includes the operator norm and the Frobenius norm, but not the trace norm. And it answers the question the counterexample raises: what is the cheapest real transport in the trace norm? Each principal angle can be moved on its own, by a rotation or by a reflection, or coupled with one other angle as in the counterexample. The minimum is found by a matching problem: choose which angles to pair so that the total saving is largest.

What the journal paper checks

The journal paper takes as its targets the four headline theorems and every named theorem, proposition, lemma, and corollary that the 1970 paper establishes, twenty-nine results in all. It proves twenty-eight of them under their stated hypotheses, in real and complex Hilbert spaces, for unbounded self-adjoint operators, for spectral separations that may run off to infinity on one side, and in unitarily invariant norms on operator ideals, where a norm can be infinite and finiteness must be assumed. The twenty-ninth is Proposition 4.4, which it refutes. A course that prepares a reader for that paper therefore has to cover the same ground: the geometry, the spectral theory, the norms, and the operator equations, at the generality the theorems are stated in.

Why the course comes in this order

The order of the course follows the proof of the sine-theta theorem. To state and prove it, four things are needed.

First, a way to measure how far apart two subspaces are. That is the geometry of two subspaces: principal angles, the angle operator, the classification of pairs of subspaces, and the direct rotation that carries one subspace to the other.

Second, the exact subspace itself. For a matrix it is spanned by eigenvectors, but for an unbounded operator there may be no eigenvectors at all, and the exact subspace comes from the spectral theorem. This part also defines the trial subspace and residual precisely, and examines the shapes a spectral gap can take.

Third, a way to measure the size of an operator. These are the unitarily invariant norms, the Ky Fan comparison principle that lets one proof cover all of them at once, and the operator ideals that carry them into infinite dimensions.

Fourth, a bridge from the residual to the angle. Project the residual onto the unwanted part of the space. The result satisfies an operator equation, the Sylvester equation, whose unknown records exactly how the trial subspace leans into the unwanted part, and whose coefficients are the trial operator and the unwanted exact operator. The gap controls the size of its solution, and the shape of the gap decides which estimate applies.

With these in place, the sine-theta theorem and its generalizations follow, including the passage between real and complex scalars. The tangent and doubled-angle theorems need one more piece of geometry, the description of a subspace as the graph of an operator, and the doubled-angle theorems need results that decide which subspace a bound refers to. The course ends with transport: the extremal properties of the direct rotation, the counterexample to Proposition 4.4 and the repair, and the matching theorem with its proof. A separate lecture traces where each of these constructions comes from historically.

Throughout, examples carry their own data. The turned family from this lecture returns, along with a few others, and each time its matrices and angles are stated again.

To summarize. Eigenvalues are stable under perturbation, but an eigenvector can turn through the angle whose sine is the size of the perturbation divided by the gap, and through ninety degrees once the perturbation is as large as the gap. The question is therefore about spectral subspaces and gaps, and it comes in a perturbation form and a residual form. Davis and Kahan bound the sine of the angle by the residual divided by the gap, in every unitarily invariant norm, under a gap of the right shape, and the two-dimensional turned family shows that the bound is attained. The 1970 paper also studies the cheapest unitary transport between two subspaces. Its Proposition 4.4 is false, as a coupled rotation in four dimensions shows, while the squared version and its Q-norm consequence are true, and the cheapest real transport in trace norm is given by a matching on the principal angles.

<!-- END SPOKEN LECTURE -->

---

## Companion (display only)

### Statements previewed

- Weyl: \(\max_j|\lambda_j(A)-\lambda_j(A+H)|\le\|H\|\).
- Swap example (journal paper, Section 2): \(A_\varepsilon=\operatorname{diag}(0,\varepsilon)\), \(\widehat A_\varepsilon=\operatorname{diag}(\varepsilon,0)\); same eigenvalues, \(\|A_\varepsilon-\widehat A_\varepsilon\|=\varepsilon\); the 0-eigenvector moves from \(e_1\) to \(e_2\).
- Turned family: \(A=\varepsilon\,e_2e_2^{\mathsf T}\), \(G_\varphi\) the rotation by \(\varphi\), \(\widehat A=G_\varphi A G_\varphi^{\mathsf T}=\varepsilon\,uu^{\mathsf T}\) with \(u=(-\sin\varphi,\cos\varphi)\). Then \(\|H\|=\|\widehat A-A\|=\varepsilon\sin\varphi\); \(\varphi=\pi/2\) gives the swap.
- Sharpness: \(E_0=e_1\), \(A_0=0\), \(R=\widehat Ae_1=-\varepsilon\sin\varphi\,u\), \(\|R\|=\varepsilon\sin\varphi\); \(\delta=\varepsilon\); \(\theta_0=\varphi\); \(\delta\sin\theta_0=\|R\|=\|H\|\).
- Residual \(R=\widehat AE_0-E_0A_0\); perturbation form \(R=HE_0\), \(N(R)\le N(H)\).
- Sine-theta: \(\delta N(\sin\Theta_0)\le N(R)\) under an interval/exterior or cut separation of \(\sigma(A_0)\) and \(\sigma(\Lambda_1)\) (G3 020000). Distance gap only: Hilbert–Schmidt with constant 1 (Theorem 6.2); operator norm needs constant \(\pi/2\) (G3 010000).
- Transport: direct rotation minimizes \(N((I-W)P)\) (Prop. 4.1) and \(N((I-W)^*(I-W))\) (Prop. 4.3); Proposition 4.4 refuted (024000); Q-norm repair (018500); matching theorem (025000–025700).
- Counterexample: two principal angles \(\theta\) in \(\mathbb R^4\); \(\|I-D\|_1=8\sin(\theta/2)\), coupled competitor \(\|I-W\|_1=4\sin\theta=8\sin(\theta/2)\cos(\theta/2)\).

### Course map

| Part | Lectures |
|---|---|
| Orientation | 000000, 000500 |
| Geometry | 003900, 004000, 004500, 005000, 005500 |
| Spectral side | 001000, 011000, 003000, 002000 |
| Norms | 006000, 013000 |
| Sylvester | 008000, 009000, 010000, 012000 |
| Sine-theta | 020000, 020500, 020700 |
| Tangent and double angle | 014000, 021000, 016000, 022000, 023000 |
| Transport | 017000, 018000, 018500, 024000, 025000, 025500, 025700 |

Primary sources: Davis and Kahan (1970); the journal paper `papers/dk_formalization_journal/paper.tex` in the formalization repository (introduction; Section 2 swap example). Coverage plan: `PAPER_COVERAGE_PLAN.md`.
