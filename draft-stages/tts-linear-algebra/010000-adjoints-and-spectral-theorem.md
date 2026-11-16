# 010000 — Adjoints and the Spectral Theorem: Symmetry Makes Operators Solvable

**Track:** Linear Algebra from First Principles. **Background:** inner products, eigenvectors and matrices. **Question:** why are symmetric transformations so much easier to understand than arbitrary ones?

<!-- BEGIN SPOKEN LECTURE -->

# Adjoints and the Spectral Theorem: Symmetry Makes Operators Solvable

Imagine stretching a sheet more in one direction than another. If the stretch is purely symmetric, we can find perpendicular axes along which the sheet expands or contracts without shearing between them. A symmetric matrix has an orthonormal eigenbasis. That remarkable conclusion is the finite-dimensional spectral theorem. It explains why many physical and mathematical operators can be studied by independent modes.

## Move an operator across an inner product

Let T be a linear map on an inner-product space. Its adjoint is the operator T star characterized by the following rule: taking the inner product of T applied to u with v is the same as taking the inner product of u with T star applied to v. For real coordinates with the standard dot product, the adjoint matrix is the transpose. For complex coordinates, it is the conjugate transpose.

This is an exact identity for every pair of vectors, not a statement that T and T star have equal entries. It describes the same bilinear measurement from the other side. In a real example, if T sends x, y to two x plus y, three y, then the matrix transpose sends the test vector in the opposite direction of the pairing.

An operator is self-adjoint if T equals T star. For real matrices, that means symmetry across the diagonal. For complex matrices it means Hermitian symmetry: entries below the diagonal are complex conjugates of those above. Complex self-adjoint operators have real eigenvalues, despite acting on complex vector spaces.

## Why the eigenvalues are real

Suppose T is self-adjoint and T v equals lambda v with v nonzero. Pair T v with v. By the eigenvector equation the result is lambda times the squared length of v, under our convention. By self-adjointness this number equals its own complex conjugate. Since squared length is a positive real number, lambda must be real. This is a structural consequence, not a happy accident of a particular matrix.

Two eigenvectors for distinct eigenvalues must be perpendicular. Take the inner product of T u with v. We can evaluate it as lambda times the pairing of u with v. Or move T across the inner product and evaluate it as mu times that pairing. If lambda and mu differ, the pairing must be zero. Thus the independent modes of a self-adjoint operator are automatically orthogonal.

## A symmetric example with actual numbers

Take the matrix with rows two, one and one, two. Apply it to the vector one, one: the output is three, three, so that direction has eigenvalue three. Apply it to one, minus one: the output is one, minus one, so that direction has eigenvalue one. These two directions are perpendicular. Normalize each by dividing by the square root of two and we obtain an orthonormal eigenbasis.

In this basis, the operator is diagonal with entries three and one. Any input decomposes uniquely into those two modes. The first is stretched threefold and the second is unchanged. Matrix powers, exponentials, and many other functions of the operator can now be computed by applying the scalar function to each eigenvalue.

For example, applying the matrix ten times multiplies the first mode by three to the tenth power and leaves the second mode unchanged. Applying an exponential of the matrix multiplies the modes by the corresponding scalar exponentials. This is the finite-dimensional origin of functional calculus.

## Why an orthonormal eigenbasis exists

The difficult part of the spectral theorem is not that different eigenvalues give perpendicular eigenvectors; it is that a self-adjoint operator actually has enough eigenvectors to span the whole space. Here is the finite-dimensional argument in outline.

On the unit sphere, consider the real-valued function sending v to the inner product of T v with v. The unit sphere is compact and this function is continuous, so it attains a maximum. At a maximizing vector, varying v slightly in any perpendicular direction shows that T v has no component in that perpendicular direction. Hence T v is a multiple of v: we found an eigenvector.

Now consider its orthogonal complement. Self-adjointness shows that this complement is preserved by T. Restrict T to that smaller space and repeat. Induction gives an orthonormal basis of eigenvectors. This proof makes clear why finite dimensionality and self-adjointness are doing work. It does not automatically establish the spectral theorem for every unbounded or infinite-dimensional operator; there one needs domain, measure and convergence hypotheses.

## Positive operators and quadratic energy

A self-adjoint operator is positive semidefinite if the inner product of T v with v is never negative. In its eigenbasis this energy is a sum of eigenvalues times squared coordinate magnitudes. Consequently, positivity is equivalent to all eigenvalues being nonnegative. Strict positive definiteness means every eigenvalue is positive in the finite-dimensional self-adjoint setting.

The same structure appears in the Hessian matrix of a smooth real function. Near a critical point, a positive-definite Hessian means the quadratic approximation bends upward in every direction. In mechanical systems, symmetric stiffness matrices have eigenvectors representing normal modes. In statistics, covariance matrices are positive semidefinite because they measure average squared fluctuations.

A symmetric matrix is easy to analyze because its different modes do not interfere under an orthonormal change of coordinates. The spectral theorem turns symmetry in a bilinear pairing into a complete set of independent directions. That is why it reappears in operator theory, geometry, differential equations, and quantum mechanics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Use the convention that \(\langle\cdot,\cdot\rangle\) is linear in its first input. The adjoint satisfies \(\langle Tu,v\rangle=\langle u,T^*v\rangle\). In standard real coordinates \([T^*]=[T]^T\); over complex coordinates \([T^*]=\overline{[T]}^T\). If \(T=T^*\), every eigenvalue is real and eigenvectors for different eigenvalues are orthogonal. Finite-dimensional spectral theorem: \(A=Q\Lambda Q^*\) with \(Q\) unitary (orthogonal over \(\mathbb R\)), \(\Lambda\) real diagonal. For \(A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), normalized eigenvectors are \(u_+=(1,1)/\sqrt2\), \(u_-=(1,-1)/\sqrt2\), with eigenvalues \(3,1\).

### Exercises with answers

1. Is \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) self-adjoint? **Answer:** yes; it equals its transpose.
2. Find the eigenvalues of \(\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\). **Answer:** three and one.
3. Does positive semidefinite mean invertible? **Answer:** no; zero eigenvalues are allowed.
4. Why do distinct eigenvectors of a self-adjoint operator become orthogonal? **Answer:** compare \(\langle Tu,v\rangle\) and \(\langle u,Tv\rangle\).

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), operators on inner-product spaces and the spectral theorem.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), symmetric matrices.
- [Spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem).
