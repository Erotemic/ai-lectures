# From Eigenvectors to Schur Form: Orthogonal Similarity and the QR Algorithm

**Track:** Linear Algebra from First Principles. **Background:** eigenvalues, eigenvectors, orthonormal bases, QR factorization, invariant subspaces. **Purpose:** explain why Schur form is the stable finite-dimensional replacement for computing Jordan form, prove the complex Schur theorem, and derive the basic QR iteration using a complete exact example.

<!-- BEGIN SPOKEN LECTURE -->

# From Eigenvectors to Schur Form: Orthogonal Similarity and the QR Algorithm

Every square complex matrix has a Jordan form. Yet numerical linear algebra does not usually try to calculate that form. The reason is not that Jordan form is mathematically unimportant. It is that small changes in the entries of a matrix can change its exact Jordan blocks, while floating-point computation is built out of small errors. A calculated Jordan block can be a fragile statement about data that are known only approximately.

There is another representation that keeps the eigenvalues visible without demanding a numerically unstable classification into Jordan chains. It is called Schur form. It uses changes of basis that preserve lengths and angles. Those orthogonal or unitary changes of basis are the central design principle behind reliable dense eigenvalue algorithms.

## Similarity, but with a restriction

A change of basis transforms A into S inverse times A times S. Any invertible S is allowed in pure linear algebra. In numerical computation, however, S might be very poorly conditioned: it can enormously magnify errors when we transform vectors to and from its coordinates.

If we require S to be unitary, meaning its inverse equals its conjugate transpose, this problem disappears at the level of the change of basis itself. Multiplying by a unitary matrix preserves Euclidean lengths. In the real case the corresponding matrices are orthogonal. Their condition number in the Euclidean norm is one.

Of course, a unitary change of basis cannot turn every matrix into a diagonal matrix. That would mean every complex matrix is unitarily diagonalizable, which is false. But it can turn every complex square matrix into an upper triangular matrix. The result is Schur's triangularization theorem.

Concretely, there exists a unitary Q such that Q conjugate transpose times A times Q equals an upper triangular matrix T. The entries on T's diagonal are the eigenvalues of A, counted with algebraic multiplicity. The entries above the diagonal record how the modes interact. They may be essential. We have not claimed that the matrix is diagonalizable or that its eigenvectors are orthogonal.

## Why the triangularization theorem is true

The proof is short enough to hold in mind. Over the complex numbers, the characteristic polynomial has a root, so A has some eigenvalue lambda and a nonzero eigenvector. Normalize that eigenvector to length one and call it q one. Complete it to an orthonormal basis of the whole space. Such a completion is always possible by elementary inner-product geometry.

Express A in that new orthonormal basis. Because the first basis vector is an eigenvector, the first column of the transformed matrix has lambda at the top and zeros below it. The remaining lower-right block is an arbitrary square matrix of one smaller dimension. Apply the same reasoning inductively to that block, using a unitary transformation that fixes the first basis vector. Continue until all entries below the diagonal are zero.

Notice what this proof did not need. It did not require enough linearly independent eigenvectors to form a basis. It did not require distinct eigenvalues. It did not classify Jordan chains. The proof succeeds for every complex matrix, including defective ones. The triangular off-diagonal entries remember precisely the coupling that diagonalization cannot always remove.

For a real matrix, requiring real orthogonal changes of basis gives a slightly different statement. A real matrix can have nonreal eigenvalues, which come in conjugate pairs. Real Schur form is therefore quasi-upper-triangular, with one-by-one real blocks and two-by-two blocks carrying conjugate pairs. For example, a plane rotation combined with a uniform scaling can have a complex eigenvalue pair without any real eigenvector. The real two-by-two block is the honest representation of that fact.

## Why the diagonal entries are enough for eigenvalues

The determinant of a triangular matrix is the product of its diagonal entries. Its characteristic polynomial is therefore the product of the terms lambda minus each diagonal entry, accounting for multiplicity. A unitary similarity transformation does not change that polynomial. Thus, once Schur form is available, eigenvalues can simply be read from its diagonal in the complex case, or from the eigenvalues of its one-by-one and two-by-two blocks in the real case.

But do not confuse the diagonal with the full action. Take the matrix with rows two, five and zero, three. It is already upper triangular, with eigenvalues two and three. Applied to the second coordinate direction, however, it produces the vector five, three. The matrix can stretch much more strongly than either diagonal entry suggests. The upper-right five is not a small correction to the story; it is part of the operator.

This example also distinguishes a Schur basis from an eigenvector basis. The first coordinate axis is invariant: applying A to a vector along it stays on that axis. The second coordinate axis is not invariant, because A mixes it with the first. The columns of Q leading up to some position span invariant subspaces, but an individual Schur vector need not be an eigenvector.

## Invariant subspaces and two different projections

Suppose a Schur form is divided into a leading block and a trailing block. The upper triangular structure has a zero block below the leading block. Consequently the span of the corresponding leading columns of Q is invariant under A. This gives a stable way to represent a spectral subspace by an orthonormal basis, even when choosing individual eigenvectors would be numerically delicate.

The orthogonal projector onto such a subspace is Q one times Q one conjugate transpose, where Q one contains the selected orthonormal columns. It is a particularly well-behaved projector: its Euclidean operator norm is one whenever the subspace is nontrivial. But an invariant subspace need not have an invariant orthogonal complement. Therefore this projector need not commute with A.

Return to the triangular matrix with rows two, five and zero, three. The projector onto its first coordinate axis simply zeros the second coordinate. Apply the projector before A and after A, and you get different answers, because the upper-right five transfers the second coordinate into the first. The projector is orthogonal and its range is invariant, yet it is not a spectral projector commuting with A.

By contrast, the exact spectral projector onto eigenvalue two along the eigenspace for eigenvalue three is an oblique projector. It commutes with A but is not orthogonal in the ordinary inner product. We met such projectors in the finite-dimensional polynomial functional calculus. Schur subspaces let us use orthonormal coordinates without claiming that all the algebraically natural projectors are orthogonal.

## From QR factorization to an eigenvalue algorithm

How do we actually find Schur form? A foundational idea is QR iteration. Begin with A zero. Compute its QR factorization, A zero equals Q zero times R zero, where Q zero is orthogonal or unitary and R zero is upper triangular. Then reverse the factors: define A one equal to R zero times Q zero.

There is a crucial identity hiding in this reversal. Since R zero equals Q zero conjugate transpose times A zero, the new matrix A one equals Q zero conjugate transpose times A zero times Q zero. So the step is a unitary similarity. It preserves all eigenvalues exactly in exact arithmetic, and it transforms the matrix without using a poorly conditioned eigenvector basis.

Repeat: factor A one as Q one R one, reverse the factors to form A two, and continue. Under suitable conditions, the matrices approach triangular or quasi-triangular form. The accumulated product of the Q factors tracks the overall change of basis.

Let's do one complete step. Take the symmetric matrix with rows two, one and one, two. Its eigenvalues are three and one, but suppose we do not know that yet. The first column has length the square root of five. Normalize it to get the first Q column, two over root five, one over root five. An orthogonal second column is negative one over root five, two over root five.

The resulting R has first row five over root five, four over root five, and second row zero, three over root five. Reverse the factors. Multiplication gives A one with rows fourteen fifths, three fifths and three fifths, six fifths. This is still symmetric. Its trace is four and determinant three, as before, so the eigenvalues have not moved. But the off-diagonal entry has shrunk from one to three fifths. The matrix is beginning to expose its invariant directions.

This example explains the mechanism, but it does not prove that the naive unshifted algorithm converges quickly or even usefully for every matrix. Practical implementations add shifts, work with upper-Hessenberg form to avoid expensive dense operations at every step, and use deflation when small couplings can be separated at the chosen accuracy. Real implementations commonly use implicitly shifted QR variants and related methods. Their details matter for reliable software.

## Why shifts and Hessenberg form matter

For a dense matrix of substantial size, performing a full QR factorization from scratch at each iteration would waste work. A preliminary orthogonal similarity can reduce a general matrix to upper-Hessenberg form: entries below the first subdiagonal become zero. Householder reflections accomplish this without sacrificing the eigenvalues. QR iteration then exploits that shape, making each step much cheaper than a fresh dense factorization.

A shift temporarily replaces A by A minus mu times the identity when computing Q and R, then adds the shift back after reversing the factors. The result is still a unitary similarity of the original A. A good shift can accelerate the reduction of a subdiagonal entry toward zero, making it possible to split off a converged eigenvalue or block. The exact selection and deflation rules are important implementation details, not consequences of the basic similarity identity alone.

The words 'small subdiagonal entry' also require care. A scale-dependent threshold is a numerical decision, not a proof that the exact entry is zero. When values are clustered or matrices are nonnormal, the relationship between a tiny coupling and accurate individual eigenvectors is more subtle than a simple threshold might suggest.

## Symmetric matrices are the favorable case

If A is real symmetric, its Schur triangular form must actually be diagonal, because an upper triangular matrix that remains symmetric can have no nonzero entries above the diagonal. The Schur basis is then an orthonormal eigenvector basis. Hermitian matrices behave analogously with unitary transformations. This is the spectral theorem in algorithmic form.

For nonsymmetric matrices, upper triangular is generally the right endpoint. Repeated eigenvalues, nonnormal coupling, and eigenvector sensitivity can all remain visible above the diagonal. Asking a QR eigenvalue routine to deliver a numerically trustworthy Jordan classification would demand a conclusion its stable operations do not support.

A computed Schur decomposition is still subject to rounding error. One should inspect the residual of the factorization and its orthogonality: how closely does A Q equal Q T, and how closely does Q conjugate transpose Q equal the identity? These provide evidence about the computed decomposition. They do not by themselves prove that individual eigenvalues are insensitive to small changes in A.

## What Schur form gives us

Schur form sits between elementary eigenvectors and the full numerical spectral theory. It provides eigenvalues through a structured triangular matrix, invariant subspaces through orthonormal columns, and a framework for QR-based numerical algorithms. Most importantly, it preserves a distinction that exact Jordan form can obscure in numerical work: a matrix can be well represented by a stable orthogonal basis even when its individual eigenvectors are a poor object to compute.

The remaining question is how sensitive the spectrum itself can be. For a normal matrix, eigenvalues behave in a controlled way under small perturbations. For a nonnormal matrix, the same small change can move them farther than one might expect. We need a tool that describes that sensitivity rather than assuming the matrix is well behaved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Complex and real Schur forms

For every \(A\in\mathbb C^{n\times n}\), there exists unitary \(Q\) and upper triangular \(T\) with
\[
Q^*AQ=T,\qquad A=QTQ^*,\qquad T_{ii}\in\sigma(A).
\]
Induction: normalize an eigenvector \(q_1\), complete to an ON basis, and obtain \(Q_1^*AQ_1=\begin{bmatrix}\lambda&w^*\\0&B\end{bmatrix}\). Apply the induction hypothesis to \(B\) and lift its unitary factor by \(\operatorname{diag}(1,U)\).

Over \(\mathbb R\), orthogonal similarity gives **real Schur form** with real \(1\times1\) and \(2\times2\) diagonal blocks. For example,
\[
\begin{bmatrix}1&-2\\2&1\end{bmatrix}
\]
is already an admissible real \(2\times2\) block; its eigenvalues are \(1\pm2i\). A normal upper triangular complex matrix is diagonal, so Hermitian/normal problems are especially favorable.

### Leading invariant Schur spaces and projections

Partition \(Q=[Q_1\ Q_2]\), \(T=\begin{bmatrix}T_{11}&T_{12}\\0&T_{22}\end{bmatrix}\). Then
\[
AQ_1=Q_1T_{11},\qquad P_{\rm orth}=Q_1Q_1^*,\qquad P_{\rm orth}^2=P_{\rm orth}=P_{\rm orth}^*.
\]
An invariant range does **not** imply \(AP_{\rm orth}=P_{\rm orth}A\). For
\[
A=\begin{bmatrix}2&5\\0&3\end{bmatrix},\quad
P_{\rm orth}=\begin{bmatrix}1&0\\0&0\end{bmatrix},\quad
P_{\rm spectral}=\begin{bmatrix}1&-5\\0&0\end{bmatrix},
\]
we have \(AP_{\rm orth}\ne P_{\rm orth}A\), while \(AP_{\rm spectral}=P_{\rm spectral}A\). The spectral projector is idempotent but not self-adjoint.

### One exact QR step

\[
A_0=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad
Q_0=\frac1{\sqrt5}\begin{bmatrix}2&-1\\1&2\end{bmatrix},\quad
R_0=\frac1{\sqrt5}\begin{bmatrix}5&4\\0&3\end{bmatrix}.
\]
Check \(A_0=Q_0R_0\) and \(Q_0^TQ_0=I\). Then
\[
A_1=R_0Q_0=\frac15\begin{bmatrix}14&3\\3&6\end{bmatrix}=Q_0^TA_0Q_0,
\qquad \sigma(A_0)=\sigma(A_1)=\{3,1\}.
\]
The off-diagonal magnitude is reduced from \(1\) to \(3/5\). This illustrative step does **not** establish general convergence of unshifted QR.

Shifted iteration uses \(A_k-\mu_k I=Q_kR_k\) then \(A_{k+1}=R_kQ_k+\mu_k I=Q_k^*A_kQ_k\). Hessenberg reduction supplies a sparse-in-structure starting matrix via unitary similarities, and deflation separates numerically small subdiagonal couplings with an explicit scale policy.

### Exercises with answers

1. **Schur theorem:** Why can a defective complex matrix still have a Schur form? **Answer:** the proof only requires one eigenvector at each induction step on a smaller block, not a basis of eigenvectors for A.
2. **Projection:** Compute \(AP_{\rm orth}\) and \(P_{\rm orth}A\) in the triangular example. **Answer:** \(\begin{bmatrix}2&0\\0&0\end{bmatrix}\) and \(\begin{bmatrix}2&5\\0&0\end{bmatrix}\), respectively.
3. **QR:** Verify that \(\operatorname{tr}A_1=4\) and \(\det A_1=3\). **Answer:** \((14+6)/5=4\); \((84-9)/25=3\).
4. **Real Schur:** Why need a real matrix not have a real upper triangular Schur form? **Answer:** a real upper triangular matrix has only real diagonal eigenvalues, while some real matrices have nonreal conjugate pairs.
5. **Symmetry:** Why is Schur form diagonal for a real symmetric matrix? **Answer:** orthogonal similarity preserves symmetry, and a symmetric upper triangular matrix must have zero off-diagonal entries.

### Sources and reading

- Lloyd N. Trefethen and David Bau III, [*Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), for Schur form, Hessenberg reduction, and QR iteration.
- James W. Demmel, [*Applied Numerical Linear Algebra*](https://doi.org/10.1137/1.9781611971446), for dense eigenvalue computation and numerical sensitivity.
- Sheldon Axler, [*Linear Algebra Done Right*, fourth edition](https://linear.axler.net/), for invariant subspaces, normal operators, and inner-product methods.
- Wikipedia topic pointers: [Schur decomposition](https://en.wikipedia.org/wiki/Schur_decomposition), [QR algorithm](https://en.wikipedia.org/wiki/QR_algorithm), [Hessenberg matrix](https://en.wikipedia.org/wiki/Hessenberg_matrix), [Invariant subspace](https://en.wikipedia.org/wiki/Invariant_subspace).

For exact algebraic spectral projectors, read `linear-algebra:018000`. For numerical QR construction, read `linear-algebra:021000`. This lecture explains the distinct problem of **orthogonal similarity for eigenvalue computation**.
