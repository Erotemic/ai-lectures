# 018500 — Chandler Davis II: Toronto, academic freedom, and the geometry of perturbation

**Track:** History · People and ideas. **Theme:** Toronto, teaching, collaboration, academic freedom and the Davis–Kahan mathematics. **Background:** elementary matrices and inner products; technical examples are taught in the lecture.

<!-- BEGIN SPOKEN LECTURE -->

In nineteen sixty-two Chandler Davis and Natalie Zemon Davis moved to Toronto after a decade in which American political investigations had disrupted their professional lives. Canada gave Chandler a regular mathematics position and gave both scholars a new institutional setting. The next decades did not erase what happened in Michigan. They changed the scale on which Davis could teach, publish, collaborate, edit, and advocate for other people. His most widely recognized mathematics emerged from a career that was never confined to mathematics alone.

In Toronto, Davis continued the study of the geometry of subspaces, collaborating with William Kahan, whose numerical-analysis perspective helped shape the third paper on the rotation of eigenvectors by perturbations, published in nineteen seventy. That paper was part of a sequence, not the invention of a subject without predecessors. Its methods grew from decades of work on spectral theory, principal angles, residual estimates and approximation. The theorem's two names compress a collaboration and a longer history of work by other mathematicians.

At Toronto, Davis found a university where he could teach, supervise students, and build a long research career. One former student, James Arthur, later recalled taking his real and complex analysis course as an undergraduate and finding it transformative. Peter Rosenthal, who came to know Davis as a mathematician and colleague, remembered the seriousness of his convictions alongside his generosity as a teacher and friend. He advised doctoral students, continued to work in operator theory, and made space for writing and editing as well as research. Eventually he served for more than twenty years as an editor of The Mathematical Intelligencer, where mathematical culture, argument, and personality all had a place.

The word 'principled' can make a biography sound too tidy. Davis's own account is more searching. In his interview with Mary Gray, he said that he remained proud of challenging the committee under the First Amendment but regretted tactical decisions in the legal case. He also described his disillusionment with the Soviet leadership, which he had defended for too long. His commitment to human rights persisted even as he reconsidered positions he had once held. He visited mathematicians in North Vietnam during the war, helped organize protests, and later worked for the rights of imprisoned scholars in several countries. Among the people he valued were mathematicians who disagreed with his politics but defended his right to conduct mathematics and speak publicly. This was a life of continuing argument, including argument with himself.

His friendship and activism also crossed into the profession's institutions. He supported organizations working on women's participation in mathematics and on opportunities for mathematicians excluded from established networks. He wrote poetry and continued to produce science fiction. When we look back at the perturbation questions that interested him, the relevant connection is a working habit: he cared about stating a problem in a way that others could examine, challenge, and extend. We can apply exactly that standard to the mathematical claims before us.

The University of Michigan eventually had to reckon publicly with what it had done in the nineteen fifties. In nineteen ninety, its faculty senate passed a resolution regretting the failure to protect intellectual freedom, and an annual Davis–Markert–Nickerson lecture was created. Institutional memory mattered: the punishment of three faculty members was no longer only a matter of personal testimony, but a subject on which the university had formally reflected. The later resolution did not undo the imprisonment, dismissal, or career exile that preceded it.

Davis died in September two thousand twenty-two, at the age of ninety-six. His lifetime spanned most of the twentieth century and reached deeply into the twenty-first. His wife Natalie, who became a major historian, survived him until twenty twenty-three. Their personal and scholarly partnership, along with their family, belongs to both intellectual histories. One can recognize his mathematics without allowing the theorem's familiar name to hide that life.

The mathematical work is now easier to place. Davis's question was not just whether two computations return the same ordered eigenvalues. It was how to compare the subspaces that carry physically or numerically meaningful information, especially when a cluster cannot be separated into individually reliable eigenvectors. We will keep the technical distinctions precise: an angle bound, a residual estimate, and a norm-minimizing ambient rotation are different statements. None should be quietly attributed to an early author merely because later textbooks attach a familiar name to it.

We can build the simplest perturbation calculation without advanced machinery. Consider a real symmetric two-by-two matrix. Before perturbation, its diagonal entries are zero and four and its off-diagonal entries are zero. The lower eigenvector points along the first coordinate axis, and the upper one along the second. Now insert the same small number, call it epsilon, in both off-diagonal positions. The matrix is still symmetric, so its eigenvectors can be chosen perpendicular. But the eigenvectors rotate. If epsilon is positive, the angle of the lower eigenvector relative to its old axis has magnitude one half of the arctangent of epsilon divided by two. For epsilon much smaller than four, that angle is approximately epsilon divided by four, in radians. The denominator is the separation between the two original eigenvalues. A large gap resists turning; a small gap allows substantial movement.

Take epsilon equal to one. The tangent of twice the rotation angle is one half. The angle is about thirteen point three degrees. The old lower coordinate direction has acquired a visible second-coordinate component, but it is still recognizable. Increase epsilon while holding the diagonal gap fixed, and the angle grows. Now repeat the experiment with original eigenvalues zero and one tenth. An off-diagonal perturbation of just one tenth creates a much larger angular response relative to the original axes. The absolute size of the perturbation tells only part of the story. The comparison with the surrounding spectrum tells the rest. This is the central reason a subspace perturbation theorem needs a spectral separation hypothesis.

A subtlety appears when the subspace is a cluster rather than a single eigenvector. Suppose a symmetric matrix has eigenvalues zero, one hundredth, and ten. If the first two eigenvalues move or cross after a perturbation, the corresponding individual eigenvectors need not stay attached to their original labels. But their common two-dimensional invariant subspace can still be well separated from the eigenvector associated with ten. The natural gap is the distance from the cluster to the unwanted part of the spectrum, rather than the tiny separation between eigenvalues within the cluster. That is the right unit of stability. The statement changes from 'this labelled eigenvector cannot rotate far' to 'this invariant subspace cannot leak far into the separated spectral complement.'

What does spectral separation actually do in a proof? Choose a trial frame, meaning a collection of perpendicular unit vectors spanning the approximate subspace. Apply the true operator to that frame. The part of the result that stays inside the trial subspace can be represented by a smaller matrix, obtained by taking inner products with the trial frame. The rest is the residual. An exact invariant subspace has residual zero. Project this relation into the unwanted spectral subspace of the true operator. The unknown projected trial frame is precisely the leakage we want to bound. It satisfies a linear operator equation of Sylvester type: the unwanted operator acts from one side, while the smaller trial matrix acts from the other. The residual is the forcing term.

The Sylvester equation is the bridge from a geometric error to spectral information. In the simplest diagonal case, each entry of its unknown is an entry of the projected residual divided by a difference of eigenvalues. A large denominator suppresses the response. If all relevant spectral differences are bounded away from zero, we can control the leakage. But the norm in which we control it matters. The Hilbert–Schmidt norm adds squared entries and behaves especially cleanly under orthonormal coordinate changes. The operator norm asks for the largest stretching direction, and an entrywise division argument does not automatically preserve the same constant. Davis–Kahan type theorems are precise because they specify the type of separation, the error being measured, and the norm in which the conclusion holds.

To keep the logical roles clear, separate three matrices in the residual picture. The full operator describes the physical or computational problem. The small matrix inside the trial space is the compression of that operator. The projected residual measures the part that escaped. An estimated eigenvalue is not the same as a true eigenvalue, and a residual gap measured relative to the wrong spectral set can be worthless. For example, a vector can have a tiny residual for some eigenvalue near a cluster without being close to a particular eigenvector in that cluster. The theorem's target is normally the entire separated invariant subspace. It uses the gap to decide which kind of closeness the residual certifies.

There is a second distinction that is central to Davis's geometric work. Given two subspaces, one may ask for an isometry taking the source into the target. An isometry acting just on the source subspace tells us how source vectors move. An orthogonal operator on the entire surrounding space must also say what happens to all perpendicular directions. Those are different optimization problems. Even if the source map is fixed, the behavior on its orthogonal complement may be changed by composing with an orthogonal transformation that preserves the source and its complement. It is therefore risky to assume a rotation that looks geometrically canonical must minimize every conceivable measure of whole-space displacement.

First examine two lines in a real plane, separated by an acute angle theta. The ordinary planar rotation through theta carries the source line to the target line. If we measure how far both coordinate directions move under this rotation, its displacement has two equal singular values, each equal to twice the sine of half theta. A reflection can also carry one line to the other; it fixes one direction and reverses its perpendicular direction. Its displacement singular values are zero and two. For a small angle the ordinary rotation is the natural low-displacement candidate. As the cost function changes, or as several principal planes can be coupled, the optimal choice can change. The word 'rotation' is not enough to settle the norm comparison.

Now consider the four-dimensional example with two equal principal angles. Let the source be a two-plane, and turn each of its two orthogonal principal directions through the same angle into a perpendicular complementary plane. The canonical transporter rotates the two independent coordinate planes by theta. Its displacement singular values are all equal to twice the sine of half theta. Their sum, the nuclear or trace norm of displacement, is eight times that half-angle sine. But one can couple the two principal planes using an additional quarter-turn within the source and within the target complement. The resulting orthogonal transporter still carries the source plane to the target. Its displacement spectrum is different: two singular values equal twice the sine of theta and two are zero. The sum is four times the sine of theta.

At theta equal to thirty degrees, the coupled transporter's trace displacement is exactly two. The canonical rotation's trace displacement is about two point zero seven one. So the canonical choice is worse under that particular whole-space trace cost. It is not enough to look at one vector's angle to see this. The coupled transporter has effectively concentrated movement into fewer ambient directions, and the trace norm rewards that concentration. This example exposes the boundary of a broad unsquared ambient optimality assertion in the third Rotation of Eigenvectors paper. The valid subspace-angle theorems, and appropriate restricted or squared-displacement statements, do not disappear because one stronger ambient claim fails.

It is worth understanding why squared displacement behaves differently. If an orthogonal map carries a fixed source orthonormal frame onto some target frame, then the sum of the squared travel distances of those source basis vectors can be expressed in terms of their pairwise inner products. For a fixed source and target pair, a canonical alignment optimizes certain such quantities. But a whole-space nuclear norm sums singular values without squaring. It can distinguish the cost of spreading movement across many directions from the cost of concentrating it. These functions of the singular-value list are not interchangeable. A theorem proved for a sum of squares cannot simply be transferred to a sum of absolute singular values.

Davis's contribution becomes clearer when we distinguish a conceptual achievement from any one theorem claim. Subspace angles and projections provide a coordinate-free account of the geometry. The perturbation theory converts spectral gaps and residuals into bounds on those angles. The transport question exposes the importance of the chosen norm and of whether we restrict a map to one subspace or optimize an orthogonal operator on the ambient space. Each of these questions can be asked independently; understanding one does not answer the others. Later analyses can correct the range of a claim while still relying on the basic geometric language that made the claim possible.

There is another way to see why projections are preferable to arbitrary bases. For two equal-dimensional subspaces K and L in a finite-dimensional Hilbert space, their difference of orthogonal projections is a self-adjoint operator. Its operator norm equals the sine of the largest principal angle. This gives a symmetric distance between the subspaces. But the directed leakage operator, restricted to K, still has a useful interpretation: it asks how far a particular source direction misses the target. When dimensions differ, the two quantities cease to tell exactly the same story. If a one-dimensional line lies inside a plane, leakage from line to plane is zero, while leakage from plane to line can be one. The choice between directed and symmetric measures must come from the question we actually want to answer.

This geometric precision is also helpful in scientific applications. Suppose we use a high-dimensional data set to estimate a low-dimensional signal subspace. The returned basis may differ from one computation to the next because of sign choices, permutations, or arbitrary rotations inside nearly repeated singular-value blocks. Comparing basis columns directly can exaggerate instability. Comparing the two orthogonal projections removes all of those artificial degrees of freedom. The projection difference cannot tell us everything about the science, but it does isolate the geometric discrepancy. A principal-angle theorem is useful because it supplies a way to estimate that discrepancy from an operator perturbation without first choosing a fragile matching of individual basis vectors.

Let us revisit the two-dimensional matrix and derive the rotation formula a little more carefully. A real symmetric two-by-two matrix can be written with diagonal entries a and d and the same off-diagonal entry b. An orthogonal rotation diagonalizes it. The off-diagonal entry after rotation is proportional to b times the cosine of twice the rotation angle, together with half the difference d minus a times the sine of twice the angle. Setting that off-diagonal entry to zero yields a tangent of twice the angle with magnitude two b divided by the original diagonal gap. For our matrix with a equal to zero, d equal to four, and b equal to epsilon, the magnitude becomes epsilon divided by two. This elementary calculation shows both the geometric sensitivity and the boundary of the approximation: the angle depends nonlinearly on the coupling, so a linear small-perturbation rule is accurate only while the coupling remains small relative to the gap.

The gap is not merely a convenient denominator. Remove it entirely by considering a scalar multiple of the identity on a two-dimensional space. Every line is an eigenspace, so an arbitrarily small perturbation can choose an entirely different preferred eigenbasis. There is no distinguished line to preserve. The operator can be close in norm while a chosen eigenvector changes by ninety degrees. If we insist on a theorem about a particular eigenvector without a separation condition, it cannot be true. But the whole two-dimensional space remains exactly the same subspace. This is a model case where the right mathematical object repairs an ill-posed comparison instead of trying to improve a false bound.

For higher-dimensional subspaces, the principal-angle construction can be derived as a sequence of constrained maximizations. Among all unit vectors in K and L, choose a pair with the largest possible inner product magnitude. Their angle is the smallest principal angle. Then repeat after requiring orthogonality to the directions already chosen. This generates a sequence of principal vectors. The same information appears in the singular values of the cross-Gram matrix because the singular-value decomposition solves the constrained maximizing problem simultaneously. The sines of the angles give the singular values of directed leakage, once dimensions and any zero or right angles are accounted for. Thus the geometric and matrix descriptions are two coordinates for one underlying relation.

What happens at a right angle? One principal direction in K may be orthogonal to L. Its leakage has norm one; its cosine overlap is zero. The source and target can still have equal dimensions, but there is no bounded graph map from one subspace to the other over that direction. This is important when a perturbation theorem is expressed through tangent bounds or through graph coordinates. A sine statement may remain meaningful at a right angle even when the tangent becomes infinite. The hypotheses that guarantee acute angles, such as a sufficiently small projection difference, are what make graph constructions safe. The choice between a sine bound, a tangent bound, and graph coordinates tells us which configurations a theorem can cover.

An especially clean operator identity explains why the projection difference measures the largest angle. Split a pair of equal-dimensional subspaces into their orthogonal principal-angle planes. On each two-dimensional plane the source and target projections are rank-one projections onto lines meeting at an angle theta. In an appropriate orthonormal basis, their difference has two opposite eigenvalues, each with magnitude sine theta. The operator norm over the full direct sum is the largest of those magnitudes. In the finite-dimensional setting this reduces the operator theorem to a two-by-two calculation, and also makes clear that the dimension count and the treatment of common or orthogonal parts cannot be skipped. The high-dimensional theorem is assembled from small geometric blocks.

The nineteen seventy Davis–Kahan paper develops more than this projection identity. It treats perturbations of self-adjoint operators and approximate spectral subspaces, and it uses different trigonometric functions of the angle operators for different hypotheses. A careful reading must distinguish the paper's estimates from its broader optimality language. A counterexample to a universal ambient norm-minimality claim does not contradict a sine-theta estimate derived through a Sylvester equation. Those statements make assertions about different operators, different feasible sets, and different costs. The point of a correction is to locate that boundary accurately so that valid consequences can continue to be used with confidence.

One can test the importance of the chosen norm with an elementary four-number comparison. Imagine two displacement singular-value lists. The first is one, one, zero, zero. The second is seven tenths repeated four times. The first list has trace sum two, while the second has trace sum two point eight. But their squared sums are two and one point nine six, respectively. The ordering has reversed. These lists are only a numerical illustration; a legitimate transport comparison also needs the maps to carry the same source subspace onto the same target. The explicit four-dimensional construction supplies exactly that feasibility condition. What the toy lists explain is why neither the trace norm nor the Frobenius norm is a cosmetic repackaging of the other. A proof that minimizes one must use properties of that objective, not merely a picture of 'small rotation.'

A final nuance concerns the phrase 'the subspace is stable.' Stable relative to what? If the perturbation size tends to zero while the desired spectral gap stays uniformly positive, a suitable angle bound tends to zero. If the gap collapses at the same rate as the perturbation, stability may disappear. If we change the target's dimension, even the object being compared has changed. If we switch from the largest angle to a sum over all angles, dimension can enter the estimate. And if we switch from self-adjoint to highly nonnormal operators, eigenvector conditioning can deteriorate in ways that spectral distance alone does not capture. Davis's geometric framework is valuable partly because it lets these qualifiers be stated as mathematical data rather than left as vague assurances.

The rotated coordinate plane made principal angles visible. The residual Sylvester equation explained why a spectral gap is relevant. The four-dimensional transporter comparison showed why an optimization claim must name its norm and feasible set. Davis's papers brought these questions into a common theory that other mathematicians continued to develop. The strength of that contribution is clearer when the boundaries of the individual results are kept precise.

The same discipline applies to historical credit. Camille Jordan's work on angles between subspaces, the spectral results of Weyl, and variational methods associated with Rayleigh, Ritz, Courant, and Fischer all supplied parts of the mathematical background. Davis did not create principal-angle geometry from nothing. He developed operator and perturbation questions in which that geometry became especially powerful. William Kahan's collaboration added a numerical-analysis perspective to the third paper. Reading a theorem name as shorthand for this accumulated development is more accurate, and more mathematically useful, than trying to attribute every idea to its last pair of authors.

Return to the pair of source and target subspaces in four-dimensional space. Their principal angles are properties of the pair, regardless of our basis. The sines measure directed leakage. A spectral gap turns residual information into a bound on that leakage under the appropriate hypotheses. An ambient transporter is a different object, with freedom on perpendicular directions; its optimality depends on the chosen displacement functional. These are now separate questions with separate mathematical answers. Chandler Davis's place in the story lies in developing the language and quantitative theory that allow us to ask them precisely. The lasting lesson is not a slogan about stability. It is a method: identify the geometric object, identify the spectral separation, and specify exactly what is being bounded before claiming that a computation is reliable.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### Subspace angles and leakage

For closed subspaces `K,L` with orthogonal projections `P,Q`, the directed
leakage operator is `(I-Q)P`. For equal-dimensional finite subspaces with
principal angles `\theta_j`, its nonzero singular values are the sines of
those angles, with zero values included as appropriate. In the equal-rank
finite case,

\[
\|P-Q\|_{\mathrm{op}}=\max_j\sin\theta_j
=\|(I-Q)P\|_{\mathrm{op}}.
\]

For a rank-two example with angles `\pi/6` and `\pi/18`, the leakage
singular values are `1/2` and `\sin(\pi/18)`.

### Two-by-two perturbation

For
\[
A_\varepsilon=\begin{pmatrix}0&\varepsilon\\\varepsilon&4\end{pmatrix},
\qquad |\tan 2\theta|=\frac{2|\varepsilon|}{4},
\]

the perturbed spectral line rotates by `|\theta|` relative to the first
coordinate axis. The small-perturbation law is `|\theta|\sim |\varepsilon|/4`.
An isolated **cluster** is the appropriate object when eigenvalues inside it
are too close to label stably.

### Distinguishing ambient transport costs

For two equal angles `\theta` in `\mathbb R^4`, the canonical direct rotation
has displacement singular values `(2\sin(\theta/2))` repeated four times. A
feasible coupled orthogonal transporter has singular values
`(2\sin\theta,2\sin\theta,0,0)`. Thus their trace-norm costs are

\[
8\sin(\theta/2) \quad\text{and}\quad 4\sin\theta.
\]

At `\theta=\pi/6`, these are approximately `2.07055` and `2.0`.
This comparison concerns unrestricted **ambient unsquared trace cost**; it
does not invalidate valid principal-angle bounds or restricted and
squared-displacement optimization results.

### Historical context

Davis published *Separation of Two Linear Subspaces* in 1958 and earlier
parts of *The Rotation of Eigenvectors by a Perturbation* before the 1970
third part jointly authored with William Kahan. His scientific career also
included science-fiction writing and advocacy of academic freedom; see the
University of Michigan record and University of Toronto account.

## Reading notes (non-spoken)
The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
### Historical reading for the second installment

- [AMS Notices, *Remembrances of Chandler Davis*](https://doi.org/10.1090/noti2740) — students, colleagues, mathematics and political life
- [University of Michigan, Davis–Markert–Nickerson history](https://facultysenate.umich.edu/davis-markert-and-nickerson-lecture-on-academic-and-intellectual-freedom/dmn-history/) — institutional reckoning and 1990 resolution
- [Mary Gray, *A Committed Life: An Interview with Chandler Davis*](https://www.ocf.berkeley.edu/~lekheng/interviews/ChandlerDavis.pdf) — first-person reflections
- [Natalie Zemon Davis, *Experiencing Exclusion*](https://doi.org/10.1017/S0018246X24000311) — family's own account
- [Wikipedia: Chandler Davis](https://en.wikipedia.org/wiki/Chandler_Davis) — orientation
