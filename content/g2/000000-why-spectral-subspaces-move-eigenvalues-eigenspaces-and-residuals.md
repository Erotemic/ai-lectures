# Why spectral subspaces move: eigenvalues, eigenspaces, and residuals

<!-- BEGIN SPOKEN LECTURE -->

# Why spectral subspaces move: eigenvalues, eigenspaces, and residuals

## Course introduction: Why spectral subspaces move

Suppose a symmetric matrix describes a system with two distinct modes. One mode has an eigenvalue of zero, the other an eigenvalue of four, and the two eigenvectors point along perpendicular coordinate axes. What happens if we change the matrix slightly? Will the eigenvalues remain close? Will the eigendirections remain close? And how much separation between the two modes is needed to make either prediction reliable?

Those questions lead to the Davis–Kahan theory of spectral subspaces. They also open a path through geometry, linear algebra, and functional analysis. This course develops that path far enough to explain the central perturbation estimates from their hypotheses, rather than treating them as formulas to be remembered.

### A small change in a matrix

Begin with a two-by-two diagonal matrix whose diagonal entries are zero and four. Its lower eigenspace is the horizontal axis, and its upper eigenspace is the vertical axis. Now put a one in each of the two off-diagonal positions. The new matrix is still symmetric, but it mixes the two coordinate directions.

Its eigenvalues are two minus the square root of five and two plus the square root of five. Each has moved by approximately zero point two three six from its original value. Meanwhile, the lower eigenline has rotated by about thirteen point three degrees. To calculate that angle, diagonalize the new matrix: the magnitude of the tangent of twice the rotation angle is one half.

Two different things have happened. The eigenvalues have moved along the number line, and the eigenvectors have changed direction. We can estimate the first movement without knowing much about the eigendirections. The second depends critically on the gap separating the spectral values. If the two original eigenvalues were almost equal, the same off-diagonal coupling could produce a much larger rotation.

Now imagine two eigenvalues that are exactly equal. There is no distinguished pair of eigenvectors inside their joint eigenspace. We can rotate an orthonormal basis within that space while leaving the underlying operator and the space itself unchanged. This is why the theory asks about subspaces rather than attempting to track every eigenvector individually. A subspace is an intrinsic geometric object; a basis is one way to describe it.

Davis and Kahan developed methods for controlling how spectral subspaces move when the underlying operator is perturbed. Their work asks for quantitative estimates that depend on the size of a perturbation, a residual, and the relevant separation of spectra. Our task is to understand where those estimates come from and when their hypotheses hold.

### How to measure a moving subspace

For two lines through the origin, an angle is easy to picture. For two planes in a much larger space, a single angle may not describe the comparison. One direction may agree almost perfectly while another is far apart. Principal angles describe these different degrees of alignment.

Orthogonal projections provide a way to study subspaces without choosing particular coordinates inside them. A projection keeps the component in a chosen subspace and removes the perpendicular component. From a pair of projections, we can recover the sines and cosines of the principal angles, understand when two subspaces meet at a right angle, and build a canonical rotation that carries one subspace toward the other.

This geometry will have several forms. An orthonormal frame gives coordinates for a subspace; a Gram operator records how its vectors overlap; a graph represents a tilted subspace as a map from one component to its perpendicular complement. Those representations are useful for different proofs. They describe the same underlying geometry, but the choice of representation can make a difficult estimate almost immediate.

The course develops these ideas from linear maps, inner products, adjoints, and orthogonal projections. We begin with familiar finite-dimensional calculations and prove the identities that later let us work without relying on a particular matrix basis.

### Why the foundations go beyond matrices

The starting background is ordinary linear algebra and calculus: matrix multiplication, elementary eigenvalue calculations, derivatives, and integrals. Prior knowledge of Banach spaces, spectral measures, or unbounded operators is not required.

A norm tells us how large a vector or an operator is. Completeness tells us when Cauchy approximations actually converge inside the space under study. Banach spaces package these analytic ideas; Hilbert spaces add inner products and orthogonality. Together they provide a setting in which projections, adjoints, limits, and operator equations can be handled rigorously.

Spectral theory begins with eigenvalues but cannot end there. An operator acting on functions may have spectral values without any corresponding eigenvector. A multiplication operator, for example, can have a continuous range of spectral values even when individual points are not eigenvalues. Spectral projections and spectral measures replace the idea that every operator can be diagonalized using a list of eigenvectors.

Functional calculus then lets us apply functions to self-adjoint operators. It explains positive square roots, operator absolute values, and spectral restrictions. From these constructions come singular values and polar decomposition, which separate how an operator stretches from how it moves directions. Matrix exponentials and skew-adjoint generators provide another description of rotations and continuous motions.

The infinite-dimensional case brings a further complication: some important self-adjoint operators are defined only on a dense domain, rather than on every vector. Differential operators are common examples. Multiplying such operators, restricting them to subspaces, or passing to limits requires domain conditions. The course establishes the spectral cutoffs, resolvent arguments, and closed-operator facts needed to carry the finite-dimensional reasoning into this setting.

### The mechanism behind an angle estimate

Here is the central proof idea. Suppose a self-adjoint operator has an exact invariant subspace, and we have an approximate subspace obtained from a computation or an experiment. The approximate subspace is represented by an orthonormal frame. Apply the operator to that frame, then subtract the part predicted by the operator compressed to the trial subspace. What remains is called the residual.

If the residual vanishes, the trial subspace is invariant. If it is small, the trial subspace is approximately invariant. But a small residual alone does not tell us which exact spectral subspace it approximates. We also need spectral separation from the unwanted part of the operator.

Projecting the residual into the orthogonal complement of the target subspace produces an operator equation. The unknown in that equation measures how far the trial frame leaks into the complementary space. The equation has the form of a Sylvester equation: one operator multiplied by the unknown, minus the unknown multiplied by a second operator, equals a known residual.

In a diagonal matrix, solving the equation amounts to dividing by differences of eigenvalues. The general theory makes that division precise. Under the right spectral-gap hypotheses, a bound for the inverse Sylvester operator becomes a bound for the sine of a subspace angle.

Different spectral gaps support different estimates. If one spectral set lies entirely above another, we have an ordered separation. If the sets are merely a positive distance apart, without an ordering, some of the same arguments require a different norm or a different constant. Knowing exactly which gap is being used is part of constructing a correct proof.

There is also more than one way to measure an operator. The operator norm measures its largest stretching factor; the Frobenius or Hilbert–Schmidt norm combines the squares of all singular values. Ky Fan sums and majorization compare entire singular-value lists. Davis and Kahan also studied unitarily invariant norms, whose value is unchanged by unitary changes of coordinates. In infinite dimensions, an estimate in an ideal norm must also account for which operators actually belong to that ideal.

### Four angle families, with different hypotheses

The principal perturbation results control the sine of an angle, the tangent of an angle, the sine of twice an angle, and the tangent of twice an angle. They are related, but they are not interchangeable.

Sine bounds measure how much a trial subspace enters the unwanted orthogonal complement. Tangent bounds become natural when a nearby subspace can be written as a graph over the exact one. A reflection across a subspace can turn an ordinary angle into a doubled-angle problem, especially for off-diagonal perturbations. For a tangent-of-twice-the-angle estimate, the choice of angular branch is essential: a small value of the sine of twice an angle, by itself, does not tell us whether the original angle is close to zero or close to ninety degrees.

The proofs therefore develop both the estimates and the geometric conditions that allow us to use them. We will distinguish results for a single largest angle from results controlling a whole singular-value list, and finite-dimensional arguments from those that require spectral measures or operator ideals. Real and complex Hilbert spaces also deserve explicit attention, because complex spectral methods sometimes need to be transferred back to the real setting.

### What happens after the angle estimates

Subspace geometry leads to a second question: when many rotations or unitary maps carry one subspace to another, which one moves the ambient space the least? A canonical direct rotation arises naturally from the geometry of two projections. Its existence and its optimality depend on the setting and on what displacement is being measured.

The original 1970 paper contains a broad claim about unsquared whole-space displacement that is false. A concrete four-dimensional real counterexample separates that claim from valid optimality results for restricted displacement and squared whole-space displacement. Studying the counterexample is part of understanding the geometry, not an aside about historical wording.

The theory also meets concrete calculations. A free-beam problem uses a fourth-order differential operator, trial functions, a Rayleigh–Ritz matrix, and residual estimates to study approximate modes. Other applications connect the same subspace ideas to singular-vector perturbations, spectral statistics, and the alignment of numerical embeddings. These settings show which aspects of a proof remain the same when the objects and norms change.

Section ten of the 1970 paper raises questions that reach beyond the estimates established there. We will examine the proved results, the counterexamples, and the questions left open by the arguments themselves.

### What understanding the theory should mean

By the end, you should be able to take a proposed angle estimate and identify the exact and trial subspaces, the residual, the relevant spectral gap, and the norm in which the estimate is supposed to hold. You should be able to derive the operator equation behind the bound, explain how its inverse is controlled, and recognize when domains, norm-class membership, or angular branch selection require an additional argument.

Proofs, worked examples, and counterexamples will make these decisions intelligible. The two-by-two matrix at the beginning is a small instance of the larger problem: spectral information can move under perturbation, and geometry plus spectral separation tells us how much. The two-dimensional calculation gives us a starting point; reconstructing the general proof will be the task of the advanced capstone.

## What changes and what stays invariant

Return to the symmetric two-by-two matrix that multiplies the horizontal coordinate by zero and the vertical coordinate by four. We can now compare its eigenvalue motion and eigenspace motion quantitatively.

Its lower eigenvalue is zero, and its lower eigenvector points horizontally. Its upper eigenvalue is four, with a vertical eigenvector. There's a spectral gap of four.

Now change only the off-diagonal entries. Put a one in the upper-right corner and a one in the lower-left corner. We haven't changed either diagonal entry, but the eigenvectors are no longer horizontal and vertical.

The eigenvalues have changed too. Yet the numerical shifts are much smaller than the rotation of the eigenvectors might lead you to expect.

This is the central tension in spectral perturbation theory. We can control how far eigenvalues move using one kind of argument. Controlling which eigenspaces they belong to, and how those spaces rotate, requires additional information about spectral separation.

### Work through the two-level example

Call the original diagonal matrix A and the perturbed matrix B. Their difference H has zeros on the diagonal and ones off the diagonal.

The operator norm of H is one: it has eigenvalues one and negative one.

To find the eigenvalues of B, solve its characteristic equation. The answer is two minus the square root of five, and two plus the square root of five.

Numerically, those are about negative zero point two three six and four point two three six. Each eigenvalue has moved by about zero point two three six from its original value.

Now look at the lower eigenvector. Write it as a unit vector making an angle theta with the horizontal axis.

Its Rayleigh quotient under B is four times sine squared theta plus two times sine theta times cosine theta.

At an eigenvector, this expression is stationary. Differentiating gives an equation involving twice the angle: four times sine of twice theta plus two times cosine of twice theta equals zero.

The lower eigenvector therefore rotates downward by about thirteen point three degrees. More precisely, its angle is negative one half of the arctangent of one half.

The perturbation had operator norm one. The eigenvalues moved by about a quarter of a unit. The lower eigendirection turned by over thirteen degrees.

These measurements describe different aspects of the perturbation. A statement about eigenvalue displacement does not directly give an angle estimate.

### Why eigenvalues have a simple stability bound

For any unit vector x, the Rayleigh quotient of B differs from the Rayleigh quotient of A by the inner product of x with H x.

Cauchy–Schwarz bounds that difference in absolute value by the operator norm of H. So every unit vector's Rayleigh quotient changes by at most one in our example.

The min–max principle identifies each ordered eigenvalue of a Hermitian matrix by optimizing these Rayleigh quotients over subspaces of the appropriate dimension.

Since every candidate Rayleigh quotient changes by at most the same amount, the minima and maxima used by the min–max principle also change by at most that amount.

Therefore the k-th ordered eigenvalue of B differs from the k-th ordered eigenvalue of A by no more than the norm of H.

This is Weyl's perturbation bound for Hermitian matrices.

The argument remains true when eigenvalues coincide. That's useful for eigenvalue estimates, but coincident eigenvalues are precisely where an individual eigenvector may cease to be uniquely determined.

### Watch a subspace selection fail at a crossing

Take the original diagonal matrix with entries zero and four again.

Now introduce a parameter t between zero and one. Increase the first diagonal entry by five t, and decrease the second by five t.

The two eigenvalues are now five t and four minus five t.

At t equals zero, the lower eigenspace is horizontal. At t equals one, it is vertical.

Where does the switch happen? Set five t equal to four minus five t. The equality occurs at t equals two fifths. At that instant, both eigenvalues equal two, and the matrix is two times the identity.

Every direction is then an eigenvector. There is no distinguished one-dimensional lower eigenspace at the crossing.

Immediately before the crossing, choosing the lower eigenvalue selects the horizontal line. Immediately after, it selects the vertical line. Those lines are perpendicular.

Yet the two eigenvalue curves themselves are continuous functions of t.

This is an exact example of why tracking the lowest eigenvector can fail when a spectral gap closes. To follow an isolated subspace continuously, we need an isolation condition that remains valid along the perturbation.

### Sometimes the right object is a whole cluster

Consider a three-dimensional diagonal matrix with entries zero, zero, and ten.

The first two coordinate directions span a two-dimensional eigenspace. But there is no preferred pair of basis vectors inside it. Any rotation within that plane gives another legitimate orthonormal basis of the same eigenspace.

Now perturb only the upper-left two-by-two block. The individual eigenvectors in that block can rotate considerably, and the repeated zero eigenvalue can split.

As long as the perturbation doesn't couple that plane to the third coordinate, the plane itself stays exactly the same invariant subspace. Its orthogonal projection is unchanged.

That gives us a more stable object to track: the whole selected spectral subspace, represented by an orthogonal projection. Principal angles compare these subspaces without requiring us to match arbitrary eigenvector bases.

### Which gap do we actually need?

A spectral gap must be attached to two specified spectral sets.

In the plane example, if our target is the lower eigenspace, the important competing spectrum is the upper eigenvalue. The distance to that unwanted part influences how easily a vector can leak into the wrong eigenspace.

In more general problems, the chosen cluster might be an interval with unwanted spectrum on either side. In another problem, the two spectral sets might be ordered, with one entirely above the other.

Those arrangements support different operator estimates. Knowing only that two spectra don't intersect is weaker than knowing the ordered separation used by a particular Sylvester theorem.

Weyl's eigenvalue bound helps us determine whether an initially isolated cluster stays isolated under a sufficiently small perturbation. Once we know which cluster is selected, subspace perturbation theory asks how its projection changes.

### The residual measures one vector's failure to be invariant

There's a second way to approach the angle question, especially when we're given an approximate eigenvector rather than two complete matrices.

Let u be a unit trial vector and mu a proposed eigenvalue. Apply the operator to u and subtract mu times u. The result is the residual.

If the residual is zero, u is an exact eigenvector with eigenvalue mu. If the residual is small, u nearly satisfies that particular eigenvalue equation.

For the perturbed matrix B in our first example, take the original horizontal vector as a trial vector and choose mu equal to its Rayleigh quotient, which is zero. Applying B gives the vertical unit vector. The residual is therefore vertical with norm one.

That vertical error is the component trying to move us out of the original target direction.

But a zero residual does not by itself say that the vector is near the *selected* eigenspace. Return to the original diagonal matrix. The vertical unit vector has zero residual when paired with its own eigenvalue four. It is nevertheless perpendicular to the lower eigenspace.

We must specify the trial spectral value and separate it from the unwanted spectrum. The residual can then be converted into a complementary-coordinate equation, and a spectral-gap bound turns that equation into an angle estimate.

The conclusion is a precise distinction. Eigenvalues of self-adjoint matrices are stable in operator norm, by the min–max principle. Eigenspaces are stable under additional conditions that keep the selected spectral component isolated. A residual measures failure of an eigenvalue equation, while a suitable gap tells us which subspace that residual can control.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Course introduction: Why spectral subspaces move

### Course introduction: Why spectral subspaces move

### What changes and what stays invariant

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `026000` finite spectral theorem; `027000` Rayleigh quotients; `031000` spectral gaps; `042000` principal angles; `105000` proof-readiness assembly. **Next:** `107000` trial spaces, exact subspaces and residuals.

---

#### Companion: mathematics and Lean correspondence (display only)

Let `B=A+H` with self-adjoint matrices. Courant–Fischer gives `|λ_k(B)-λ_k(A)| ≤ ‖H‖`, but no analogous subspace estimate follows without separating the selected spectral sets. For `A=diag(0,4)` and `H=[[0,1],[1,0]]`, the lower eigendirection rotates through `θ=-(1/2) arctan(1/2)` and eigenvalues become `2±√5`. For `A(t)=diag(5t,4-5t)`, the lower spectral subspace changes at the collision `t=2/5`.

The exact source-backed sharpness model below supplies a distinct planar perturbation model used by the sine theorem. It is an analogy, not a formalization of both examples in this lecture.

##### Worked example: eigenvalue motion and subspace crossing

Let
\[
A=\begin{pmatrix}0&0\\0&4\end{pmatrix},\qquad
H=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad B=A+H.
\]
Then \(\|H\|=1\) and \(\sigma(B)=\{2-\sqrt5,2+\sqrt5\}\), so each ordered eigenvalue moves by \(\sqrt5-2\approx0.236\). The lower eigenvector makes angle \(\theta=-\tfrac12\arctan(1/2)\) with \(e_1\), approximately \(-13.28^\circ\).

For \(A(t)=\operatorname{diag}(5t,4-5t)\), the eigenvalues collide at \(t=2/5\) and the selected lower one-dimensional eigenspace changes from \(\operatorname{span}(e_1)\) to \(\operatorname{span}(e_2)\). Individual eigenvectors are not trackable through that collision without an additional selection rule.

##### Source declaration excerpts

`DavisKahan/Sources/DavisKahan1970/SineTheta/Sharpness.lean` — `planarTrialMap` (exact declaration header; body omitted):

```lean
noncomputable def planarTrialMap (theta : ℝ) :
    𝕜 →L[𝕜] PlanarModelSpace 𝕜 :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Sharpness.lean` — `planarAmbient` (exact declaration header; body omitted):

```lean
noncomputable def planarAmbient (delta : ℝ) :
    PlanarModelSpace 𝕜 →L[𝕜] PlanarModelSpace 𝕜 :=
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Sharpness.lean` — `planarResidual` (exact declaration header; body omitted):

```lean
noncomputable def planarResidual (delta theta : ℝ) :
    𝕜 →L[𝕜] PlanarModelSpace 𝕜 :=
```

**Mapping.** `planarAmbient`, `planarTrialMap` and `planarResidual` model exact and trial geometry in two coordinates. The next lectures use the source's general `residual` function for a trial map and a trial operator. The examples here are elementary matrix calculations, and no claim is made that they are literally the input values of the cited Lean declarations.

## Advanced continuation (not spoken)

The [proof reconstruction capstone](105000-proof-reconstruction-residual-estimates-and-the-davis-kahan-theorem-families.md) develops the residual-to-angle argument and reconstructs the theorem families after the technical topic routes. Review the matching and beam routes before its final stages.
