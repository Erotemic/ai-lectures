# Positive-Definite Matrices: Why Cholesky Works and When It Fails

**Track:** Linear Algebra from First Principles. **Background:** symmetric matrices, inner products, elimination, triangular systems, quadratic forms. **Purpose:** construct Cholesky rather than merely name it, understand the positive-definite hypothesis, and explain the advantages and costs of preserving matrix structure.

<!-- BEGIN SPOKEN LECTURE -->

# Positive-Definite Matrices: Why Cholesky Works and When It Fails

Imagine that you are solving a system with thousands of unknowns. You have already learned to factor a general matrix using elimination, and to protect the calculation with pivoting. But now someone tells you that the matrix is symmetric and positive definite. Those are not merely descriptive labels. They change the geometry of the equation and let us solve it with a simpler, more economical factorization. They also connect the equation to minimizing an energy, which will become the basis of an iterative method.

We will build the factorization from its first step, use it to solve a complete numerical example, and then ask where it can break. The distinction between a mathematical positive-definiteness assumption and a test made in floating-point arithmetic will matter throughout.

## What positive definite actually asserts

For a real square matrix A, symmetry means that exchanging a row and a column index leaves every entry unchanged. Positive definiteness is a statement about all nonzero vectors: x transpose times A times x must be strictly positive. For a complex matrix, we replace symmetry by Hermitian symmetry and the transpose by conjugate transpose. This expression is then a real number.

Why use the quadratic expression? If A represents stiffness in a mechanical model, it often describes an energy stored by a displacement x. If A is the Hessian of a quadratic optimization problem, positivity says that every nonzero displacement from the minimizer increases the energy. The algebra makes the idea precise: the function one half x transpose A x minus b transpose x has a unique minimizer, and its first-order condition is A x equals b.

For a symmetric matrix, positive definiteness is equivalent to every eigenvalue being strictly positive. To see one direction, expand x in an orthonormal eigenvector basis. The quadratic expression becomes a sum of positive eigenvalues multiplied by squared coordinates. Conversely, choosing an eigenvector corresponding to a nonpositive eigenvalue contradicts strict positivity.

Two weaker-looking statements are not enough. Having positive diagonal entries does not make a symmetric matrix positive definite. The matrix with rows one, two and two, one has positive diagonal entries, but along the direction one, negative one, its quadratic form is negative. Likewise, a positive determinant by itself does not establish positive definiteness. We need to inspect the whole form, not one convenient entry.

## The first square root

Take a two-by-two symmetric matrix with first row a, c and second row c, d. We seek a lower triangular matrix L such that A equals L times L transpose. Let the entries of L be ell eleven and zero in the first row, and ell twenty-one and ell twenty-two in the second, with positive diagonal entries. Multiplying L by its transpose gives three equations.

First, ell eleven squared equals a. Therefore ell eleven is the positive square root of a. Second, ell twenty-one times ell eleven equals c, so ell twenty-one equals c divided by the square root of a. Third, ell twenty-one squared plus ell twenty-two squared equals d. Consequently ell twenty-two is the positive square root of d minus c squared divided by a.

The computation has exposed its own requirement. We need a positive a and a positive remainder after eliminating the first variable. That remainder is the Schur complement of a. Positive definiteness guarantees both. Indeed, choosing a vector supported in the first coordinate proves a is positive. Choosing the first coordinate to cancel its cross term with the second proves the remainder is positive.

This is Cholesky factorization. More generally, at each column we take a positive square root of the remaining diagonal contribution, then use that number to compute entries underneath it. No separate upper triangular factor is needed because symmetry gives the other half for free.

For a positive-definite matrix, the lower triangular factor with positive diagonal entries is unique. It is a structured version of elimination: instead of writing a general L times U, we preserve the relation U equals L transpose. In dense arithmetic this needs about half the leading cubic work of general LU. The storage savings can matter as well, though sparse problems introduce additional complications.

## A three-variable solve from beginning to end

Consider a matrix whose first row is four, two, zero; second row two, five, two; and third row zero, two, five. It is symmetric. We can construct a lower triangular factor with first column two, one, zero. After removing that column's contribution, the remaining leading diagonal value is four, whose positive square root is two. The next lower entry is one. The last remaining diagonal value is four again, whose square root is two.

So L has rows two, zero, zero; one, two, zero; and zero, one, two. Multiply it by L transpose to check that it reproduces A exactly. Notice what each successive positive pivot tells us: the energy remains positive after earlier variables have been eliminated.

Now solve A x equals b, with b equal to six, nine, seven. Write L y equals b, then L transpose x equals y. Forward substitution gives y one equals three; y two equals three; and y three equals two. Back substitution gives x three equals one, x two equals one, and x one equals one. We have solved the system with two triangular passes and no matrix inverse.

This is also a compact proof of positive definiteness for our example. For any nonzero x, x transpose A x equals the squared Euclidean length of L transpose x. Because L is invertible, that length cannot vanish for nonzero x. Thus the factorization is not just a computational convenience; it certifies a geometric property of the matrix.

## Why a principal minor test works

The first Cholesky pivot checks the leading one-by-one part of the matrix. The second checks what remains after the first part, and so on. The determinant of each leading principal block is the product of squares of the Cholesky diagonal entries up to that point. For a real symmetric matrix, all those leading principal determinants are positive if and only if the matrix is positive definite. This equivalence is called Sylvester's criterion.

For our three-by-three example the successive leading determinants are four, sixteen, and sixty-four. They are all positive. One could use this to verify the hypothesis before solving, though computing many determinants separately would be a poor numerical implementation. The criterion is a theorem about the matrix; the factorization is the more useful constructive test when we actually have the entries.

The block version of the same idea is worth remembering. Partition A into a positive scalar a, a cross-term vector c, and a trailing matrix B. Then A is positive definite exactly when a is positive and the trailing Schur complement, B minus c c transpose divided by a, is positive definite. The proof follows by completing the square in the quadratic form. Cholesky repeats this argument one variable at a time.

## Positive semidefinite is a different promise

Now change the two-by-two example to the matrix whose every entry is one. Its quadratic form is the square of the sum of the two coordinates, which is never negative. But along the nonzero vector one, negative one the form is zero. The matrix is positive semidefinite, not positive definite, and singular.

Ordinary Cholesky reaches a first pivot of one and then a second pivot of zero. The strict positive-diagonal factorization no longer exists. A zero or negative pivot in exact arithmetic indicates that the positive-definite hypothesis has failed somewhere. It does not by itself tell us whether we have a genuine singularity, an indefinite matrix, or corrupted input.

For an indefinite symmetric matrix, a different factorization is appropriate, often a pivoted L D L transpose factorization in which D can have positive and negative entries or small blocks. For a positive-semidefinite matrix, specialized pivoted Cholesky or rank-revealing methods may be suitable. Blindly taking the square root of a nonpositive pivot is not a repair.

There is a particularly instructive nearly singular example. Let the two-by-two matrix have rows one, one and one, one plus a small positive delta. Its exact second Schur complement is delta. Thus it is positive definite for every positive delta, however tiny. But if delta is too small to be represented distinctly from one at the available precision, the stored matrix may be indistinguishable from the singular all-ones matrix. A numerical failure here does not refute the exact theorem; it tells us something about the represented data and arithmetic.

Some software adds a positive multiple of the identity to make a factorization possible. This is sometimes called a diagonal shift or jitter. It can be entirely appropriate in an inference or optimization model, but it changes the system. We must state the shift and assess its effect instead of pretending that the original equation was solved unchanged.

## Sparse structure and the cost of eliminating variables

In scientific computing, A may be enormous but mostly zero. Positive definiteness does not mean that its Cholesky factor will be equally sparse. Eliminating one variable creates interactions among variables that were both connected to it. Those new nonzero entries are called fill.

Picture four variables arranged around a square. Each interacts with its two neighbors but not with the variable across the square. Eliminate the first variable and its two neighbors become coupled in the remaining Schur complement. A zero that was present in the original matrix becomes nonzero in the factorization. Elimination order can therefore change memory requirements dramatically even though it leaves the mathematical solution unchanged.

Sparse Cholesky implementations use ordering strategies to reduce fill, symbolic analysis to plan storage, and numerical factorization to compute values. Positive definiteness helps avoid the usual search for numerical pivots, but one still needs to consider scaling, rounding, near-singularity, and memory. A large sparse direct solve can be dominated by factor storage even when multiplying A by a vector remains cheap.

This contrast motivates iterative alternatives. If you can compute A times a vector cheaply, perhaps you can solve the positive-definite system without storing a potentially dense factor. But to do so reliably, we need the energy geometry that positive definiteness supplies.

## What the factorization has taught us

We started with one inequality: x transpose A x is positive away from zero. From it we obtained positive Schur complements, a unique positive-diagonal triangular square root, a method to solve linear systems, a characterization by principal minors, and a strictly convex energy landscape. We also learned what the guarantee excludes: semidefinite rank loss, indefinite quadratic forms, numerical uncertainty near zero, and sparse fill caused by variable elimination.

Cholesky is the natural direct method when its hypotheses fit. It is not automatically the cheapest method for every structured system. The same energy will now let us construct a sequence of improving approximations using only matrix-vector products and a small number of stored vectors.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Definitions, factor and exact solve

For real symmetric \(A\in\mathbb R^{n\times n}\),
\[
A\succ0\quad\Longleftrightarrow\quad x^TAx>0\text{ for all }x\ne0
\quad\Longleftrightarrow\quad \lambda_{\min}(A)>0.
\]
For complex Hermitian \(A\), replace \(T\) by \(*\). If \(A\succ0\), there is a unique lower triangular \(L\) with strictly positive real diagonal and \(A=LL^T\).

\[
A=\begin{bmatrix}4&2&0\\2&5&2\\0&2&5\end{bmatrix},
\qquad L=\begin{bmatrix}2&0&0\\1&2&0\\0&1&2\end{bmatrix},
\qquad LL^T=A.
\]
With \(b=(6,9,7)^T\), \(Ly=b\) gives \(y=(3,3,2)^T\) and \(L^Tx=y\) gives \(x=(1,1,1)^T\). Leading principal determinants are \(4,16,64\).

### Schur complement and construction

For \(A=\begin{bmatrix}a&c^T\\c&B\end{bmatrix}\) with \(a>0\),
\[
\begin{bmatrix}t\\z\end{bmatrix}^TA\begin{bmatrix}t\\z\end{bmatrix}
=a\left(t+\frac{c^Tz}{a}\right)^2+z^T\left(B-\frac{cc^T}{a}\right)z.
\]
Thus \(A\succ0\) iff \(a>0\) and \(S=B-cc^T/a\succ0\). Factoring the one-dimensional part then recursively factoring \(S\) constructs \(L\). Entrywise,
\[
\ell_{jj}=\sqrt{a_{jj}-\sum_{k<j}\ell_{jk}^{2}},\quad
\ell_{ij}=\frac{a_{ij}-\sum_{k<j}\ell_{ik}\ell_{jk}}{\ell_{jj}}\ (i>j).
\]
The radicands are positive in exact arithmetic for an SPD matrix. If \(A=LL^T\), then \(\det A=\prod_i \ell_{ii}^{2}\) and \(x^TAx=\|L^Tx\|_2^2\). Existence and uniqueness follow inductively with positive square roots.

### Cases where the hypothesis changes

\[
\begin{array}{c|c|c}
A & \text{second Schur complement} & \text{classification}\\\hline
\begin{bmatrix}1&1\\1&1\end{bmatrix} & 0 & \text{positive semidefinite, rank one}\\
\begin{bmatrix}1&2\\2&1\end{bmatrix} & -3 & \text{indefinite}\\
\begin{bmatrix}1&1\\1&1+\delta\end{bmatrix},\delta>0 & \delta & \text{positive definite}\end{array}
\]
For the last family, \(\delta\) below representation precision near one may be rounded away. A diagonal shift \(A+\lambda I\) changes the solved equation, even when used as a practical regularizer.

### Sparse fill: a four-cycle

Let \(A=4I-C\), where \(C\) is the adjacency matrix of a four-cycle, with edges \(1\!\! -\!\! 2\), \(2\!\! -\!\! 3\), \(3\!\! -\!\! 4\), \(4\!\! -\!\! 1\). It is strictly diagonally dominant and SPD. Eliminate variable 1. In the Schur complement on variables \(2,3,4\), the \((2,4)\) entry becomes \(0-(-1)(-1)/4=-1/4\): a new nonzero entry. This illustrates fill, not instability.

### Exercises with answers

1. **Test a candidate:** Is \(\begin{bmatrix}2&3\\3&2\end{bmatrix}\) SPD? **Answer:** no; \((1,-1)A(1,-1)^T=-2\) using the coordinates as a column vector, or observe the eigenvalue \(-1\).
2. **Construct:** Find \(L\) for \(\begin{bmatrix}9&3\\3&2\end{bmatrix}\). **Answer:** \(L=\begin{bmatrix}3&0\\1&1\end{bmatrix}\).
3. **Certify:** Why does a nonsingular \(L\) imply \(LL^T\) is SPD? **Answer:** \(x^TLL^Tx=\|L^Tx\|_2^2>0\) for every nonzero \(x\).
4. **Failure mode:** A second computed pivot is slightly negative for a theoretically SPD input. What can be concluded? **Answer:** the *computed factorization* cannot proceed as ordinary positive-pivot Cholesky; investigate representation, floating-point effects, symmetry and the strength of the SPD guarantee before making a claim about the exact input.
5. **Solve:** Verify \(x=(1,1,1)^T\) for the displayed three-variable system by direct multiplication. **Answer:** \(Ax=(6,9,7)^T\).

### Sources and reading

- Nicholas J. Higham, [*What Is a Cholesky Factorization?*](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/) (2020), for the construction, SPD hypotheses, and computational uses.
- Nicholas J. Higham, [*Cholesky Factorization*](https://eprints.maths.manchester.ac.uk/1199/) (2008 preprint / 2009 article), for stability, semidefinite and pivoted variants.
- Lloyd N. Trefethen and David Bau III, [*Numerical Linear Algebra*](https://people.maths.ox.ac.uk/trefethen/text.html), for factorization, conditioning and sparse-system context.
- Wikipedia topic pointers: [Positive-definite matrix](https://en.wikipedia.org/wiki/Definite_matrix), [Cholesky decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition), [Schur complement](https://en.wikipedia.org/wiki/Schur_complement), [Sylvester's criterion](https://en.wikipedia.org/wiki/Sylvester%27s_criterion).

Read `linear-algebra:020000` for elimination and triangular solves; `linear-algebra:022000` for conditioning and finite-precision interpretation. The present lecture proves the SPD-specific factorization and exposes sparse fill.
