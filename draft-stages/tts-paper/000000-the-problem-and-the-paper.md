# 000000 — The problem and the paper

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** orientation. **Audience:** linear algebra, eigenvalues and eigenvectors of symmetric matrices, singular values, inner-product notation.

<!-- BEGIN SPOKEN LECTURE -->

The problem and the paper

When a symmetric matrix or a self-adjoint operator changes a little, its eigenvalues change a little. Its eigenvectors may not. This course is about the theory that says exactly when and how much an eigenvector, or more precisely an eigenspace, can move: the Davis–Kahan theory, from the 1970 paper by Chandler Davis and William Kahan titled The Rotation of Eigenvectors by a Perturbation, Part Three. It is also about a recent journal paper that re-examines that paper result by result, finds that one of its propositions is false, repairs it, and solves the optimization problem the error exposes. The goal of the course is that a careful listener can read both papers, follow their proofs, and know exactly what each theorem assumes.

This first lecture states the problem, gives the main results in plain terms, and describes the route the course takes.

Eigenvalues are stable, eigenvectors need a gap

Start with two matrices. Let A be the two by two diagonal matrix with entries zero and epsilon, for some small positive epsilon, and let A hat be the diagonal matrix with entries epsilon and zero. They have the same eigenvalues, zero and epsilon. Their difference has size epsilon. So in every reasonable sense A hat is a small perturbation of A. But the eigenvector of A for the eigenvalue zero is the vertical axis, and the eigenvector of A hat for zero is the horizontal axis. They are perpendicular.

Eigenvalues behaved: Weyl's inequality says that, listed in order, the eigenvalues of two symmetric matrices differ by at most the size of their difference. Eigenvectors did not. The reason is visible in the numbers: the gap between the two eigenvalues, epsilon, is as small as the perturbation. With a perturbation small compared with the gap, eigenvectors are stable; with a perturbation as large as the gap, they can turn arbitrarily.

When eigenvalues repeat or cluster, individual eigenvectors are not even determined; only the subspace they span is. So the right question concerns subspaces: given a gap separating a wanted part of the spectrum from the rest, how far can the corresponding spectral subspace move?

Two ways to ask the question

The question comes in two forms, and the paper treats both.

In the perturbation form, we know an operator A and its spectral subspaces, and the operator we care about is A hat, equal to A plus a perturbation H. How far is the spectral subspace of A hat from the corresponding one of A?

In the residual form, we have an approximate subspace, called a trial subspace, from a numerical method or a model, together with a trial operator describing how A hat acts on it. The residual measures how far the trial subspace is from being invariant: apply A hat to trial vectors, subtract what the trial operator predicts, and measure what is left. How far can the trial subspace be from the exact spectral subspace of A hat?

The two forms meet: if the trial subspace is a spectral subspace of A and the trial operator is A's action there, the residual is the perturbation H applied to that subspace, and its size is at most the size of H.

The answer, in one line

Davis and Kahan's sine-theta theorem says: delta times the size of the sine of the angle between the trial subspace and the exact subspace is at most the size of the residual. Here delta is a spectral gap between the trial operator and the unwanted part of the exact operator, and the angle is not a single number but an operator, whose eigenvalues, when it has them, are the principal angles between the subspaces.

Every word in that sentence needs care, and much of the course is about that care. The angle is an operator because subspaces of dimension more than one meet at a list of angles, and in infinite dimensions a continuum of them. The size can be any unitarily invariant norm: the largest sine, the root sum of squared sines, the sum of sines, or any of infinitely many others, and the theorem holds for all of them at once. The gap must have the right shape: one spectrum inside an interval and the other outside it enlarged by delta, or one spectrum entirely below a cut and the other entirely above. A gap of delta between interlaced spectra is not enough for the constant one in the operator norm. And the operators may be unbounded, like differential operators, provided the domains and residuals are handled correctly.

The 1970 paper has four headline theorems: bounds on the sine of the angle, the tangent of the angle, the sine of twice the angle, and the tangent of twice the angle. They differ in their hypotheses, in which operators the gap compares, and in what extra structure they need, and the course treats them one at a time.

The transport question

The paper asks a second kind of question. Given two subspaces, which unitary map of the whole space carries one onto the other while moving everything as little as possible? The natural candidate is the direct rotation, which turns each principal plane through its own angle and does nothing else. Davis and Kahan prove that it minimizes the motion of vectors in the first subspace, and the squared motion of all vectors, in every unitarily invariant norm. Then, in Proposition 4.4, they claim that for real spaces with all angles at most sixty degrees, it also minimizes the unsquared motion in every such norm.

That claim is false. In real four-dimensional space, for every positive angle, there is a map that moves the space less, in the trace norm, than the direct rotation does, by coupling two principal planes instead of rotating each separately. The construction is a real form of a complex example Davis and Kahan themselves gave. The journal paper identifies the step in the printed proof that fails, proves the correct replacement, which holds for a class of norms that includes the operator and Frobenius norms but not the trace norm, and then answers the question the counterexample raises. The cheapest real transport in trace norm is computed by a matching problem: pair up principal angles whose planes should move together, leave the rest alone, and choose the pairing that saves the most.

The journal paper also checks every other selected result of the 1970 paper, twenty-eight in all, under their stated hypotheses, with the proofs verified by a computer proof assistant. Those details belong to the paper's companion materials; in this course, what matters is the mathematics they confirm.

How the course is organized

The course builds the theory in dependency order, in seven parts.

First, the geometry of two subspaces: principal angles, the angle operator, the classification of pairs of subspaces, and the direct rotation, including what happens when some vectors of one subspace are perpendicular to the whole of the other.

Second, the spectral side: spectral subspaces and exact decompositions, unbounded self-adjoint operators and their domains, trial subspaces and residuals, and the geometry of spectral gaps.

Third, norms: unitarily invariant norms, Ky Fan dominance, and operator ideals in infinite dimensions, where a norm can be infinite and membership has to be assumed.

Fourth, the Sylvester equation, which turns a residual into an equation for the angle, and the estimates that solve it under each shape of gap, including for unbounded operators.

Fifth, the sine-theta theorem itself, its generalizations, and the passage between real and complex scalars.

Sixth, the tangent and double-angle theorems, with the geometry of graphs and the branch-selection results that tell a double-angle bound which subspace it is talking about.

Seventh, transport: the extremal properties of the direct rotation, the counterexample to Proposition 4.4, and the matching theorem with its proof.

A separate lecture traces where each construction comes from historically.

A few examples recur throughout, and each lecture restates the data it uses: a plane with a diagonal matrix and a trial line at forty degrees, from the journal paper's first figure; the swapped diagonal matrices above; a pair of planes in four-dimensional space with principal angles of thirty and sixty degrees, and a related pair with two equal angles that becomes the counterexample; the vibrating free beam, which is the 1970 paper's own numerical example; and three principal angles of thirty, forty-five, and seventy-five degrees, the journal paper's matching example.

The course assumes linear algebra, singular values, and inner products, and some comfort with limits and integrals. Functional-analytic ideas, such as Hilbert spaces, spectral measures, domains, and operator ideals, are introduced where they are needed, at the level required to read the papers.

To summarize. Eigenvalues are stable under perturbation, but eigenvectors and eigenspaces are stable only relative to a spectral gap, as two swapped diagonal matrices show. Davis and Kahan bound the angle between an approximate and an exact spectral subspace by a residual or perturbation divided by a gap, in every unitarily invariant norm, with hypotheses that depend on the shape of the gap and on which operators it compares. The 1970 paper also studies the cheapest unitary transport between two subspaces; its Proposition 4.4 is false, the squared version and its Q-norm consequence are true, and the real trace-norm minimum is a matching problem on the principal angles.

Each of those statements has precise hypotheses, and the rest of the course is devoted to stating them exactly and proving the results that depend on them.

<!-- END SPOKEN LECTURE -->

---

## Companion (display only)

### Statements previewed

- Swap example: \(A_\varepsilon=\operatorname{diag}(0,\varepsilon)\), \(\widehat A_\varepsilon=\operatorname{diag}(\varepsilon,0)\); Weyl: \(\max_j|\lambda_j(A)-\lambda_j(A+H)|\le\|H\|\).
- Residual \(R=\widehat AE_0-E_0A_0\); perturbation form \(R=HE_0\), \(N(R)\le N(H)\).
- Sine-theta: \(\delta N(\sin\Theta_0)\le N(R)\) under \(\mathrm{SineGap}(A_0,\Lambda_1)\) (G3 020000).
- Transport: direct rotation minimizes \(N((I-W)P)\) and \(N((I-W)^*(I-W))\); Proposition 4.4 refuted (024000); Q-norm repair (018500); matching theorem (025000–025700).

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

Primary sources: Davis and Kahan (1970); the journal paper `papers/dk_formalization_journal/paper.tex` in the formalization repository. Coverage plan: `PAPER_COVERAGE_PLAN.md`.
