# 061000 — Quadratic-form inequalities and singular values

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `027000` Rayleigh quotients; `028000` Courant–Fischer; `033000` Loewner order; `035000` modulus; `058000` invariant norms. **Next:** the Sylvester inverse problem.

<!-- BEGIN SPOKEN LECTURE -->

# From inequalities on vectors to inequalities on singular values

For two self-adjoint matrices, saying that A is at least B can mean that every vector x has quadratic measurement under A at least as large as under B. This is a quadratic-form order. It is defined by testing all vectors, not by comparing matrix entries.

Take A diagonal with entries two and three, and B diagonal with entries one and one. The difference is positive, so A is above B in quadratic-form order. Their ordered eigenvalues obey the same inequality by the min–max theorem. Because these particular matrices are positive, their singular values agree with their eigenvalues.

But singular values discard signs. A matrix and its negative have the same singular values, even though they are oppositely ordered in quadratic-form terms when the matrix is positive. We therefore need positivity and self-adjointness hypotheses before converting a form inequality into a singular-value statement.

We will derive the valid comparison using the variational principles, then explain how componentwise singular-value bounds differ from stronger statements about sums and unitarily invariant norms.

## Recall the positive-operator order

A self-adjoint operator H is positive semidefinite when its quadratic form is nonnegative on every vector. That means the inner product of H x with x is at least zero for every x.

For two self-adjoint operators H and K, we write H less than or equal to K in the Loewner order when K minus H is positive semidefinite. Equivalently, H's quadratic form is at most K's quadratic form on every vector.

In the finite-dimensional self-adjoint setting, the min–max principle says that the ordered eigenvalues of H are at most the corresponding ordered eigenvalues of K whenever H is below K in this form order.

Why? Choose any fixed trial subspace. Every vector in it has a Rayleigh quotient for H no larger than the corresponding quotient for K. Taking a maximum over that subspace preserves the inequality, and then taking the appropriate minimum over all trial subspaces preserves it again.

This is a direct consequence of the nested minimization and maximization in Courant–Fischer. We compare the two quadratic measurements on the very same trial vector before taking any extremum, so the subspaces used in the two optimizations can also be the same. No assumption that H and K commute is needed.

There is a useful caution here. Loewner order is a statement about every vector in the ambient space. Comparing a couple of diagonal entries in one basis would not suffice. A matrix can have smaller diagonal entries and still have a larger quadratic form on a tilted vector because the off-diagonal terms contribute.

## Positive operators give singular-value comparisons

Now suppose H and K are not just self-adjoint but both positive, with H less than or equal to K.

A positive operator's singular values equal its nonnegative eigenvalues, counted with multiplicity and arranged in decreasing order. The previous min–max argument therefore gives each singular value of H no larger than the corresponding singular value of K.

Consequently all Ky Fan sums of H are no larger than those of K. Every symmetric gauge, and hence every unitarily invariant norm, gives H no larger a value than K.

Notice the two positive hypotheses in the statement. They allow us to identify singular values with ordinary eigenvalues rather than absolute values of potentially negative eigenvalues.

To see why positivity matters, take H equal to negative identity and K equal to zero. The inequality H less than or equal to K holds, because zero minus negative identity is positive. But every singular value of H is one, while every singular value of K is zero.

Thus Loewner order between arbitrary self-adjoint operators does not imply singular-value order. Our proof requires positive H and K.

## Apply the idea to rectangular maps

Let A and B have the same finite-dimensional input space, but perhaps different output spaces. We cannot compare A and B directly in a Loewner order because they may not even be square or self-adjoint.

We can, however, compare their source Gram operators, A adjoint A and B adjoint B. Those are both positive endomorphisms of the same input space.

Suppose that for every input vector x, the squared length of A x is at most the squared length of B x.

By the adjoint identity, these squared lengths are the quadratic forms of A adjoint A and B adjoint B. Therefore the Gram operator of A is below the Gram operator of B in Loewner order.

Apply the min–max theorem to the two positive Gram operators. Their eigenvalues, sorted from largest to smallest, satisfy a coordinatewise inequality.

But those eigenvalues are precisely the squares of the singular values of A and B. Since square root is increasing on nonnegative numbers, taking square roots gives the same inequality for the singular values themselves.

Thus a uniform comparison of squared output lengths implies that A's j-th largest singular value is at most B's j-th largest singular value, for every index j.

And by our symmetric-gauge theorem, every standard unitarily invariant norm of A is at most the corresponding norm of B, provided the same cross-space norm rule is being used.

## A rectangular numerical example

Take A from two-dimensional space to three-dimensional space with first output column of length three along the first coordinate axis, and second column of length one along the second output axis.

Take B to be a map with output lengths four and two on those same orthogonal input directions.

Their source Gram matrices are diagonal: nine and one for A, sixteen and four for B. The difference is diagonal with entries seven and three, so it is positive.

Therefore A adjoint A is below B adjoint B. The singular values of A are three and one. Those of B are four and two.

The inequalities hold individually, and hence also for the operator, Frobenius, nuclear, and Ky Fan norms. For example, the Frobenius norm of A is the square root of ten, while that of B is the square root of twenty.

The example is simple because the Gram operators commute. The theorem does not rely on that feature. What makes it work is the shared input: we can compare the squared lengths of A x and B x for every x in that one space. Their output spaces may differ.

To picture the noncommuting case, tilt one output measurement so that its strongest direction is not a coordinate axis. If the quadratic comparison still holds on every input vector, the min–max theorem still compares the ordered Gram eigenvalues. We never need to match their individual eigenvectors.

## Why squaring a form inequality can fail

There is another plausible but incorrect maneuver. Suppose positive operators H and K satisfy H less than or equal to K. Can we square both sides and conclude H squared is below K squared?

In general, no. Matrix multiplication is sensitive to noncommutativity, and the scalar observation that smaller nonnegative numbers have smaller squares does not automatically extend to noncommuting operators.

We can make this failure completely explicit.

Let H be the two-by-two diagonal matrix with entries one and zero. Let K have first row two, one, and second row one, one.

First check positivity. H is positive. K is symmetric, has positive trace three and determinant one, so both of its eigenvalues are positive.

The difference K minus H has all four entries equal to one. Its quadratic form on a vector with coordinates x and y is the square of x plus y. So K minus H is positive. Hence H is below K.

But K squared has first row five, three, and second row three, two. Subtract H squared, which equals H, and the resulting matrix has rows four, three and three, two.

Its determinant is eight minus nine, which is negative. A symmetric matrix with negative determinant has eigenvalues of opposite signs, so this difference is not positive.

Therefore H squared is not below K squared, even though both original operators are positive and H is below K.

This example is worth retaining because it prevents a common proof error. If we want to compare squared singular values, we should compare the Gram operators directly. We cannot indiscriminately square a Loewner inequality involving noncommuting operators.

## Trace inequalities versus singular-value inequalities

If H and K are positive and H is below K, their difference is positive. The trace of a positive matrix is nonnegative, so trace H is at most trace K.

This scalar trace inequality follows immediately from positivity and linearity. It is weaker than the complete eigenvalue comparison we obtained by min–max.

For positive operators, the trace is the nuclear norm. Thus the trace comparison is one instance of an invariant-norm comparison.

But trace control by itself does not imply operator-norm control. A matrix can have small total trace concentrated in one direction, while another has larger total trace spread across many directions. We need stronger hypotheses, such as the full form-order relation, to infer all the coordinatewise eigenvalue bounds.

A trace bound, an inequality of quadratic forms on every vector, and a sequence of ordered eigenvalue inequalities are different assertions. Each requires its own justification.

## Where the comparison is useful

Consider recovering an unknown map from a difference of two compositions. This kind of equation often comes with a spectral gap, and the goal is to control an unknown correction by a known residual.

The estimates will involve norms, including Frobenius and general unitarily invariant norms. To manipulate them safely, we must recognize when a hypothesis controls a quadratic form, when it controls singular values, and when a separate argument is required for an operator-norm bound.

The Gram and min–max argument is a standard bridge between these languages. Its strength comes from the exact hypotheses and the explicit intermediate comparison.

## What the argument establishes

The key route has three steps. A comparison of output lengths for every input vector becomes a Loewner comparison of the two source Gram operators. Min–max compares their ordered eigenvalues. Finally, square roots turn those eigenvalues into singular values, which symmetric gauges can measure.

Each step has a hypothesis that cannot be discarded. Self-adjoint form order does not compare singular values if signs are unrestricted. Even positive Loewner order does not allow us to square noncommuting operators. The proof succeeds by comparing the Gram operators directly.
<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### The comparison uses one common input space

For \(A:E\to F\) and \(B:E\to G\), the same vector \(x\in E\) appears in both measurements:
\[
\|Ax\|^2=\langle A^*Ax,x\rangle,
\quad \|Bx\|^2=\langle B^*Bx,x\rangle.
\]
This is why the Loewner comparison is well-typed even when \(F\ne G\). The min–max principle gives
\(\lambda_j(A^*A)\le\lambda_j(B^*B)\) and hence \(\sigma_j(A)\le\sigma_j(B)\), with source-indexed zeros included.

A matrix-entry comparison is not enough: \(\operatorname{diag}(1,1)\) and \(\begin{pmatrix}1&1\\1&1\end{pmatrix}\) have equal diagonal entries, but their forms differ on \((1,1)\) and \((1,-1)\). One must compare quadratic forms on every vector.


For \(0\preceq H\preceq K\), Courant–Fischer yields \(\lambda_j(H)\le\lambda_j(K)\), so \(\sigma_j(H)\le\sigma_j(K)\). For rectangular \(A:E\to F\), \(B:E\to G\),
\[
\forall x\in E,\quad\|Ax\|^2\le\|Bx\|^2
\quad\Longleftrightarrow\quad A^*A\preceq B^*B
\quad\Longrightarrow\quad\sigma_j(A)\le\sigma_j(B).
\]
Loewner comparison of arbitrary self-adjoint operators need not compare their singular values, and \(0\preceq H\preceq K\) does not generally imply \(H^2\preceq K^2\).

**Lean bridge (verbatim excerpts).**

`ForTauCeti/Analysis/InnerProductSpace/RectangularSingularValues.lean`:

```lean
theorem le_eigenvalues_adjointCompSelf_of_norm_sq_floor
    (A : E →ₗ[𝕜] F) {α : ℝ} (hfloor : ∀ x, α * ‖x‖ ^ 2 ≤ ‖A x‖ ^ 2)
    {d : ℕ} (hd : finrank 𝕜 E = d) (i : Fin d) :
    α ≤ A.isSymmetric_adjoint_comp_self.eigenvalues hd i := by
```

The theorem turns a pointwise lower bound on squared output norms into a Gram-eigenvalue lower bound. The lecture derives the general two-map comparison from Courant–Fischer; this specific excerpt is one source-side ingredient, not the full conclusion in one declaration.

`ForTauCeti/Analysis/InnerProductSpace/RectangularSingularValues.lean`:

```lean
theorem singularValues_eq_of_gram_eq {F' : Type*} [NormedAddCommGroup F']
    [InnerProductSpace 𝕜 F'] [FiniteDimensional 𝕜 F'] {A : E →ₗ[𝕜] F} {B : E →ₗ[𝕜] F'}
    (h : A.adjoint ∘ₗ A = B.adjoint ∘ₗ B) : A.singularValues = B.singularValues := by
```

This shows why singular-value information can be recovered entirely from source Gram operators; the positivity and min–max arguments supply the monotonicity step.

**Reconstruction exercise:** Reprove the principal displayed identity from the spoken lecture, then identify the exact source/target types and extra assumptions in each displayed Lean declaration.
