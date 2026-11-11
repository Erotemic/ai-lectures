# 142000 — Three subspaces and higher-order interactions

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `016000`, `042000–045000`, `108000`, `138000–141000`. **Next:** `143000`.

<!-- BEGIN SPOKEN LECTURE -->

# Three subspaces and higher-order interactions

Imagine three perpendicular coordinate axes rather than a division into just two subspaces. A symmetric matrix can couple the first axis to the second and the second to the third, even when it has no direct entry connecting the first and third. Information can travel from the first direction through the middle one to reach the third. Measuring each pair in isolation misses part of that interaction.

Davis and Kahan asked how their two-subspace estimates should change for decompositions into three or more mutually perpendicular pieces. To investigate, we will compare the coordinate systems using a three-by-three matrix of operator blocks, identify the relations imposed by orthogonality, and see why a single two-block Sylvester equation no longer tells the whole story.

## The geometric data

Take a finite-dimensional Hilbert space and divide it into three mutually orthogonal subspaces, called E zero, E one, and E two. Their projections sum to the identity. Take a second division into F zero, F one, and F two, whose projections also sum to the identity. The same construction works for finite orthogonal sums of closed Hilbert subspaces.

Choose an isometric coordinate map for each piece. The adjoint of the coordinate map extracts coordinates in that piece. If we place the three E maps side by side, we get a unitary coordinate map from the direct sum of three coordinate spaces onto the entire ambient space. Do the same for the F family.

Now compare the two coordinate systems. The comparison is another unitary operator. Write it as a three-by-three array of blocks. Block i, j takes coordinates from F j and reports their component in E i. It is the adjoint of E i followed by F j. This is exactly the block matrix described in Question ten point two.

For two blocks, the cosine–sine decomposition organizes this change of coordinates into independent planar rotations, plus elementary intersections and defects. With three blocks we retain a unitary matrix of operators, but there is no comparable universal reduction into independent, labelled two-dimensional principal planes.

## What unitarity already proves

Because the comparison operator is unitary, its blocks obey two families of equations. Fix an F column, say column j. The sum over i of block i,j adjoint times block i,j equals the identity on F j. Every unit vector in F j has its squared length divided among the three E spaces; those fractions sum to one.

Fix two distinct F columns, j and k. The sum over i of block i,j adjoint times block i,k equals zero. This says the columns remain orthogonal after all three contributions are added. No individual cross term has to vanish.

There is a matching pair of row equations. For any E row i, the sum of block i,j times its adjoint, over j, is identity on E i. Different E rows are orthogonal after their three contributions are added.

These four identities constrain the three-way overlaps. Arbitrary collections of pairwise sine angles do not automatically obey them.

A genuine obstruction already appears with three one-dimensional pieces. Suppose someone proposes a table of *squared overlap magnitudes* with these rows: one half, one half, zero; then one half, zero, one half; then zero, one half, one half. Every row adds to one. Every column also adds to one. So the table passes all length-distribution tests.

Now test whether that normalized overlap table could actually come from a unitary matrix. A unitary's columns must be orthogonal.

The first proposed column has a nonzero first coordinate and a nonzero second coordinate, each of magnitude one over square root of two. The second has a nonzero first coordinate and a nonzero third coordinate of the same size. Their nonzero positions overlap in exactly one row: the first.

In the inner product of the two columns, all other terms vanish. The remaining term has magnitude one half, regardless of which complex phases we assign. There is nothing available to cancel it. The two columns cannot be orthogonal, so no unitary realizes the table. Row and column sums alone did not enforce the needed cancellation.

## Why an intermediate block matters

Now imagine that the first coordinate direction is rotated toward the second by a small angle a, and then the second coordinate direction is rotated toward the third by a small angle b. Relative to the original basis, the resulting third direction acquires a first-coordinate component proportional to sine a times sine b. This is a second-order effect in small angles.

Neither elementary rotation directly mixed the first and third axes. Nevertheless their composition does. To verify this, start with the third basis vector. Rotate it into a combination of the second and third vectors, with second-coordinate coefficient sine b. Then rotate the first-second plane. The inherited second component develops a first-coordinate contribution whose magnitude is sine a times sine b.

For small a and b, those sines are approximately a and b. The indirect first-to-third coupling is therefore approximately a times b. Any perturbation analysis that treats only direct first-third blocks risks missing this mediated interaction.

The order of the two rotations also matters. Reverse their order and the first-third contribution changes. The difference is already visible in matrix multiplication: the elementary rotation generators need not commute. Their commutator records the first nonlinear interaction.

## The three-block perturbation equation

The spectral setting makes this geometry more structured. Let the first decomposition reduce a self-adjoint operator A. Let the second decomposition reduce a nearby self-adjoint operator B, which equals A plus H. Write A i for the compression of A to E i, and B j for the compression of B to F j.

Let X i,j be the overlap map from F j to E i. Use the reducing identities: A applied to E i equals E i applied to A i, while B applied to F j equals F j applied to B j. Calculate A i times X i,j minus X i,j times B j. Moving both maps back to the ambient space shows that this difference is minus E i adjoint times H times F j.

So every overlap block solves a Sylvester equation. When the spectra of A i and B j are separated, its norm can be estimated using the gap and the projected perturbation. For an ordered gap, we may obtain a constant-one operator-norm estimate. For merely pairwise distance, remember that the Hilbert–Schmidt and operator-norm constants differ.

This looks like nine independent problems, but it is not. All nine overlap maps share the same unitarity relations. Estimating them individually discards possible cancellations, and collecting independent upper bounds may even describe an impossible unitary comparison matrix.

Here is the research opportunity. Can we combine the Sylvester equations with the row and column identities to obtain joint sharp estimates? Can an estimate for the direct overlap between E zero and F two be improved when we also know the middle spectral cluster and the neighboring overlaps? Could a small coupling through the middle cluster produce a second-order improvement rather than a crude first-order bound?

## A controlled three-by-three example

Suppose A is diagonal with three distinct eigenvalues: minus g, zero, and g, where g is positive. Perturb it by a symmetric matrix having a small coupling s between the first two coordinates and another small coupling t between the last two. There is no direct first-to-third perturbation entry.

A first-order eigenvector correction to the lowest eigenvector points toward the middle coordinate with size proportional to s divided by g. The correction to the highest eigenvector points toward the middle with size proportional to t divided by g. The first-to-third mixing appears one order later, approximately s times t divided by g squared, with coefficients depending on the actual spectral denominators.

The exact coefficient can be computed from the eigenvector equation, rather than guessed from that approximation. The lowest eigenvector satisfies three coupled scalar equations. Eliminating its middle component produces an effective first-to-third term containing the product s times t and two spectral denominators. This is a Schur-complement mechanism: a middle coordinate mediates an interaction between endpoints that have no direct matrix coupling.

We can make the middle-coordinate mechanism exact. Let lambda be the lowest eigenvalue, and let x, y, z be the three coordinates of its eigenvector. The matrix has a coupling s from the first coordinate to the middle, and a coupling t from the middle to the last. There is no direct first-to-last coupling.

The last coordinate equation expresses z in terms of y: multiply y by minus t, then divide by g minus lambda. Substitute that into the middle equation. Now y can be expressed in terms of x.

After this elimination, the ratio of the last coordinate to the first contains the product s times t in its numerator. Two couplings were needed to get from one end to the other. The denominators record the two spectral obstacles. This is the concrete meaning of a Schur complement in the three-coordinate model.

When the couplings are small compared with g, the low eigenvalue is close to minus g. The denominator therefore approaches minus two g squared. The first-to-third coordinate ratio approaches s times t divided by two g squared, to leading order. That factor of two has a concrete origin: the low level is one gap below the middle level but two gaps below the high level. An estimate that remembers only the smallest gap misses that coefficient.

The example explains why a three-space theorem might strengthen a two-space theorem. It also shows what the theorem cannot ignore: the middle spectral location matters, because its denominators control the indirect coupling.

## What has and has not been established

We have proved the block-unitarity identities and the exact nine Sylvester equations. They are already powerful enough to generate bounds. But a theorem asserting the best simultaneous bounds, based only on prescribed three-block spectral information, requires an optimization over coupled overlap matrices. That is the unresolved problem described by Davis and Kahan in Question ten point two. In their beam calculation, they explicitly deferred an optimality assertion about a three-by-three comparison to this question.

The three-block identities constrain possible overlaps but do not determine the optimal bound. That extremal problem requires additional hypotheses and a construction attaining the proposed bound. A precise formulation must specify the three spectral clusters, the sizes of the perturbation blocks, the target overlap, and the norm in which it is measured. The corresponding extremal problem must also impose the common unitarity constraints and ask whether an actual triple of reducing subspaces attains the proposed bound.

You should now be able to derive the three-block equations yourself, calculate an indirect coupling of order s times t, and explain why independent pairwise angle estimates do not solve a coupled three-subspace optimization problem.

<!-- END SPOKEN LECTURE -->

---

## Display-only mathematical and Lean correspondence

The original-paper statement is `DK-10.2`, transcribed in `prose/distilled_literature/DavisKahan1970_part_III.tex`; it is posed as a question, not a theorem. For orthogonal isometric decompositions define `Wᵢⱼ = Eᵢ* Fⱼ`, yielding

\[\sum_i W_{ij}^*W_{ik}=\delta_{jk}I,\qquad \sum_j W_{ij}W_{kj}^*=\delta_{ik}I.\]

If `AEᵢ=Eᵢ Aᵢ`, `BFⱼ=Fⱼ Bⱼ`, and `B=A+H`, then

\[A_iW_{ij}-W_{ij}B_j=-E_i^*HF_j.\]

This is an elementary consequence of block algebra. The supporting Lean source declarations below formalize the component operator vocabulary; they do **not** prove a sharp three-way analogue of Davis–Kahan Question 10.2.

### A doubly stochastic table with no unitary realization

The nonnegative squared-modulus table
\[
 M=\frac12\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}
\]
has every row and column sum equal to \(1\). Were \(M_{ij}=|W_{ij}|^2\) for a unitary \(W\), the inner product of its first two columns would have a single nonzero term, \(\overline{W_{11}}W_{12}\), of modulus \(1/2\), contradicting orthogonality. Thus \(M\) is doubly stochastic but not unistochastic.

For \(A=\operatorname{diag}(-g,0,g)\) and \(H=\begin{psmallmatrix}0&s&0\\s&0&t\\0&t&0\end{psmallmatrix}\), let \((x,y,z)\) be an eigenvector of \(B=A+H\) with eigenvalue \(\lambda\) near \(-g\). From
\[
 (-g-\lambda)x+sy=0,\quad sx-\lambda y+tz=0,\quad ty+(g-\lambda)z=0
\]
one obtains (when the denominators are nonzero)
\[
 \frac zx=-\frac{st}{\lambda(g-\lambda)+t^2}
 =\frac{st}{2g^2}+\text{higher-order terms as }(s,t)\to(0,0).
\]
The leading coefficient follows from the **two distinct denominators** \(-g\) and \(-2g\). The mixed term illustrates mediated coupling, not a sharp general three-subspace theorem.

## Exact Lean declaration excerpts

**`adjoint_finiteAnalysis`** — Analysis and synthesis supply the isometric-coordinate vocabulary used to form overlap blocks. This statement alone does not establish Question 10.2.

Source: `ForTauCeti/Analysis/InnerProductSpace/FiniteFrame.lean`; exact declaration header (proof body omitted).

```lean
theorem adjoint_finiteAnalysis (v : ι → E) :
    (finiteAnalysis 𝕜 v).adjoint = finiteSynthesis 𝕜 v := by
```

**`IsOffDiagonal`** — The existing two-block off-diagonal predicate is a reference point; the three-way identities of the lecture are derived in prose and are not claimed as a new compiled theorem.

Source: `DavisKahan/FiniteDimensional/Core/OperatorBlocks.lean`; exact declaration header (proof body omitted).

```lean
def IsOffDiagonal (U : Submodule 𝕜 E) [U.HasOrthogonalProjection]
    (H : E →ₗ[𝕜] E) : Prop :=
```

