# Orthogonalize Without Losing the Geometry: QR, Householder Reflections, and Least Squares

**Track:** Linear Algebra from First Principles. **Background:** dot products, Euclidean length, projections, matrix multiplication and triangular systems. **Purpose:** construct QR from vectors and reflections, prove the least-squares reduction, and explain why numerical orthogonality matters.

<!-- BEGIN SPOKEN LECTURE -->

# Orthogonalize Without Losing the Geometry

Suppose three measurements are supposed to come from a model with only two adjustable parameters. There are three equations and two unknowns. Usually no parameter choice satisfies all the equations exactly. We need to choose the model whose predictions come as close as possible to the data.

A familiar algebraic trick is to multiply the system by the transpose of its coefficient matrix, producing the normal equations. That is mathematically valid for least squares, but as a numerical recipe it can make an already delicate problem worse. We can find the best fit more directly by changing to coordinates in which lengths and angles remain under control.

That is the purpose of QR factorization. Its first factor has orthonormal columns: each column has length one and is perpendicular to the others. Its second factor is triangular, so the resulting equations are easy to solve. The theorem is simple to state. The construction is where the ideas of projection, stable algorithms, and approximation meet.

## The first orthogonal direction

Take two column vectors in ordinary three-dimensional space. Let the first be one, one, zero, and the second one, zero, one. They are independent, but not perpendicular: their dot product is one. Put them side by side as the two columns of a matrix A.

We begin by turning the first column into a unit vector. Its length is the square root of two. So our first orthonormal direction, q one, has components one over the square root of two, one over the square root of two, and zero.

Now ask how much of the second column points along q one. Its dot product with q one is one over the square root of two. Remove that component. The remainder has entries one-half, negative one-half, one. Its length is the square root of three-halves. After dividing by that length, we obtain q two, whose components are one, negative one, two, each divided by the square root of six.

Check the claims: q one and q two both have unit length, and their dot product is zero. We have not changed the plane spanned by the original columns. We have replaced a tilted, non-orthogonal coordinate system for that plane by two perpendicular axes.

This procedure is Gram–Schmidt orthogonalization. Each subtraction removes a projection onto a previously constructed direction. The numbers we used to scale and subtract become entries of an upper triangular matrix R. The two new unit columns form a three-by-two matrix Q. The original matrix equals Q times R.

For our example, R has first row square root of two, one over the square root of two, and second row zero, square root of six divided by two. Multiplying Q by R reconstructs the original vectors exactly. The first column of A is a multiple of q one. The second is a component along q one plus a component along q two. That is the entire factorization in two sentences.

## Least squares by Pythagoras, not by a formula to memorize

Let the measurements be one, two, two. We want a vector x of two parameters that makes the Euclidean length of A times x minus b as small as possible.

The column space of A is the plane spanned by q one and q two. Any prediction A times x lies in that plane. Split b into its orthogonal projection onto the plane and the part perpendicular to the plane. The perpendicular part cannot be changed by adjusting x. Any additional error within the plane merely adds a nonnegative squared length. By the Pythagorean theorem, the best prediction is exactly the projection of b onto the column space.

Because Q has orthonormal columns, its transpose extracts the coefficients of that projection. So the least-squares problem reduces to the triangular system R times x equals Q transpose times b. This is not a heuristic. It follows from orthogonality and the Pythagorean theorem.

Our exact example is particularly friendly. Q transpose times b has entries three over the square root of two and three over the square root of six. Solve the second triangular equation first: the second parameter is one. Substitute into the first equation: the first parameter is also one.

That pair predicts two, one, one. The observed vector was one, two, two. The residual, observed minus predicted, is negative one, one, one. Its dot product with each column of A is zero, which certifies that it is perpendicular to the model plane. Its length is the square root of three. No other pair of parameters can make the residual shorter.

There are qualifications. The unique triangular solve described here assumes A has linearly independent columns. If the columns are dependent, R has a zero diagonal entry in exact arithmetic, and there are infinitely many parameter vectors that produce the same best prediction. The projection remains well defined, but finding one particular parameter vector requires an additional rule, such as selecting the one of smallest Euclidean norm.

## How orthogonal transformations preserve information

Why should orthogonal methods be more numerically trustworthy? The mathematical reason is that an orthogonal matrix preserves Euclidean length. Rotate or reflect a vector as much as you like; its length does not change. For a full orthogonal matrix H, H transpose times H is the identity. Therefore the square of the length of H times v is the same as the square of the length of v.

A change of variables by H cannot make one measurement error enormously larger than another simply because we chose bad coordinate axes. Orthogonal transformations are condition-number one in the Euclidean norm. That does not make every ensuing computation perfect, but it removes one source of artificial amplification.

Compare this with the normal equations. They are formed by multiplying A transpose by A. The eigenvalues of that product are the squares of the singular values of A. So, for a full-column-rank matrix, its two-norm condition number is the square of the two-norm condition number of A. If A has a condition number of a million, the normal-equations matrix has a condition number of a trillion. Solving the normal equations in ordinary precision can lose information that the original least-squares problem did not require us to lose.

Using QR does not cure an intrinsically ill-conditioned model. Nearly dependent measurement columns are still nearly dependent. It does, however, avoid deliberately squaring their condition number before we solve the system.

## Why Gram–Schmidt is not the end of the numerical story

The Gram–Schmidt derivation is conceptually clean. In floating-point arithmetic, a straightforward version can lose orthogonality when one input column is nearly parallel to another. The subtraction of their large common component leaves a small difference, and rounding in the earlier projection may contaminate that difference.

Modified Gram–Schmidt rearranges the operations: it orthogonalizes each remaining column against one newly computed direction at a time. That usually behaves better than the simplest classical implementation. Reorthogonalization can improve it further. But the standard robust approach for general dense QR factorization uses a different elementary operation: a Householder reflection.

A Householder reflection across a plane perpendicular to a unit vector w is the identity matrix minus twice w times w transpose. Acting on a vector, it subtracts twice the component along w. The result is a reflection, not an arbitrary stretch, so it preserves length exactly in real arithmetic.

Take the two-dimensional vector three, four, whose length is five. We want to turn it into a vector with its entire magnitude in the first coordinate. Choose w to have components two over the square root of five and one over the square root of five. The corresponding reflection sends three, four to negative five, zero. We have annihilated the lower component without dividing by a small pivot or trying to subtract almost parallel unit vectors.

For a taller matrix, apply such a reflection to its first column, zeroing every entry below the first diagonal position. Then restrict attention to the rows and columns that remain and apply a second reflection to zero entries below the next diagonal position. Continue. The product of these reflections is orthogonal, and the transformed matrix is upper triangular or, for a rectangular matrix, upper trapezoidal. Reverse the product to reconstruct Q. Implementations generally store the reflection vectors rather than forming an enormous full Q matrix.

The choice of sign in constructing a reflection vector is important: choosing the sign that avoids subtracting two nearly equal numbers helps avoid cancellation. The mathematical reflection formula alone does not encode that floating-point decision.

## Knowing which columns carry independent information

In exact arithmetic, full column rank can be read from the nonzero diagonal entries of R. With noisy measurements and finite precision, that simple test becomes a question of scale. A small diagonal entry may signal near-dependence, or it may simply reflect units.

Column-pivoted QR chooses which input column to orthogonalize next, often based on the remaining column norms. The resulting factorization is A times a column-permutation matrix equals Q times R. It helps expose independent directions, though the diagonal entries by themselves are not universal certificates of singular values. Strong rank-revealing variants and singular-value analysis can provide more reliable information when the numerical rank matters greatly.

There is also a structural reason to distinguish row and column permutations. Row pivoting in LU keeps the system equivalent while protecting elimination. Column pivoting in QR rearranges model parameters, and the solution coordinates must be put back in the original order. The two procedures solve different bookkeeping problems.

## The factorization is also a geometric proof

QR is not merely a way to avoid forming A transpose times A. It explains what a least-squares answer means: find the orthogonal projection of the data onto the predictions the model can produce, then recover its coefficients by a triangular solve. The residual is perpendicular to every allowed prediction direction.

It also opens the way to solving eigenvalue problems by orthogonal iteration, building Krylov subspaces without losing independence, and estimating the sensitivity of models with many correlated measurements. The next question is unavoidable: how should we quantify the sensitivity of the mathematical problem itself, and how can we separate it from errors introduced by our chosen algorithm?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Thin QR worked example

\[
A=\begin{bmatrix}1&1\\1&0\\0&1\end{bmatrix},\qquad
Q=\begin{bmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{bmatrix},
\qquad R=\begin{bmatrix}\sqrt2&1/\sqrt2\\0&\sqrt6/2\end{bmatrix}.
\]

Verify \(Q^TQ=I_2\), \(QR=A\). For \(b=(1,2,2)^T\),
\[
Q^Tb=\begin{bmatrix}3/\sqrt2\\3/\sqrt6\end{bmatrix},\quad
Rx=Q^Tb\implies x=(1,1)^T,\quad
r=b-Ax=(-1,1,1)^T.
\]
Then \(A^Tr=0\) and \(\|r\|_2=\sqrt3\). For any other \(z\),
\[
\|Az-b\|_2^2=\|A(z-x)\|_2^2+\|r\|_2^2\ge\|r\|_2^2.
\]
This follows from \(r\perp\operatorname{col}(A)\). It proves optimality; full column rank proves uniqueness.

### Reflection construction

For a unit vector \(w\in\mathbb R^m\), let \(H=I-2ww^T\). Then \(H^T=H\), \(H^2=I\), and \(\|Hz\|_2=\|z\|_2\). With \(w=(2,1)^T/\sqrt5\),
\[
H=\begin{bmatrix}-3/5&-4/5\\-4/5&3/5\end{bmatrix},\qquad H(3,4)^T=(-5,0)^T.
\]
In general, for nonzero \(x\in\mathbb R^m\), choose \(v=x+\operatorname{sign}(x_1)\|x\|_2e_1\), using \(\operatorname{sign}(0)=1\); set \(w=v/\|v\|_2\). Then \(Hx=-\operatorname{sign}(x_1)\|x\|_2e_1\). The sign choice avoids cancellation in forming \(v\). Stable norm computation is also needed in a floating-point implementation.

### Least squares, normal equations, conditioning

For full-column-rank \(A\in\mathbb R^{m\times n}\), thin QR yields \(A=QR\), \(Q^TQ=I_n\), and \(R\in\mathbb R^{n\times n}\) nonsingular. The least-squares solution is \(x=R^{-1}Q^Tb\), without explicitly computing \(R^{-1}\). Normal equations are \(A^TAx=A^Tb\), with \(\kappa_2(A^TA)=\kappa_2(A)^2\). QR does not remove the sensitivity of \(x\) to noisy inputs.

For **complex** matrices, replace transposes by conjugate transposes; orthogonal becomes unitary. For a **rank-deficient** matrix, use a rank-aware method and specify which least-squares solution is intended.

### Exercises with answers

1. **QR reconstruction:** Verify the first column of \(QR\). **Answer:** \(\sqrt2 q_1=(1,1,0)^T\).
2. **Projection:** Why is \(r=(-1,1,1)^T\) a least-squares certificate for the example? **Answer:** \(A^Tr=0\), so the residual is orthogonal to the column space.
3. **Reflection:** Evaluate \(H(3,4)^T\) for the displayed H. **Answer:** \((-5,0)^T\).
4. **Normal equations:** If \(\kappa_2(A)=10^4\), what is \(\kappa_2(A^TA)\) under full column rank? **Answer:** \(10^8\).
5. **Dependent columns:** If the second column equals twice the first, is the best fitted prediction unique? Is its parameter representation unique? **Answer:** the orthogonal projection is unique; the parameter representation need not be.

### Further reading and source connections

- Gilbert Strang, MIT OpenCourseWare 18.06SC, linear algebra course units on Gram–Schmidt, QR, projections and least squares, https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/ .
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, SIAM, 1997, https://people.maths.ox.ac.uk/trefethen/text.html , for Householder triangularization and least-squares stability.
- Jim Hefferon, *Linear Algebra*, https://hefferon.net/linearalgebra/ , for inner products and orthogonal projections.
- Wikipedia topic pointers: [QR decomposition](https://en.wikipedia.org/wiki/QR_decomposition), [Householder transformation](https://en.wikipedia.org/wiki/Householder_transformation), [Linear least squares](https://en.wikipedia.org/wiki/Linear_least_squares).

The numerical-analysis overview `numerical-analysis:006000` discusses why QR is preferred to unqualified normal equations; this lecture derives the QR construction and least-squares reduction explicitly.
