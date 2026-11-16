# 042000 — Self-Adjoint and Positive Operators: The Geometry of Energy

**Track:** Analysis from First Principles. **Background:** Inner products, adjoints, matrices, bounded operators. **Question:** Why do real measurements and nonnegative energy lead naturally to self-adjoint operators?

<!-- BEGIN SPOKEN LECTURE -->

# Self-Adjoint and Positive Operators: The Geometry of Energy

Take a spring attached to a moving object. Its stored energy is proportional to the square of its displacement. If the spring acts in several directions, the energy can be a quadratic expression involving interactions between coordinates. The matrix in that expression should be symmetric: swapping the two input directions does not change the energy. In complex Hilbert spaces, the corresponding symmetry is self-adjointness.

An operator A is self-adjoint when A equals its adjoint. This means the inner product of A x with y equals the inner product of x with A y for all x and y. One immediate consequence is that the scalar inner product of A x with x is real. We can interpret it as a measurable quantity, even though it need not be positive.

An operator is positive when that quantity is nonnegative for every x. Positive operators are self-adjoint by definition in the standard complex Hilbert-space formulation. The phrase positive here does not mean that the entries of a matrix are positive. It means that every vector produces a nonnegative quadratic measurement.

## Rotate to the revealing coordinates

Consider the two-by-two real matrix with two on the diagonal and one off the diagonal. Apply it to the vector whose entries are both one. The output is three times the input. Apply it to the vector whose entries are one and negative one. The output is the input itself. These two perpendicular directions are eigenvectors, with eigenvalues three and one.

In the coordinates formed by those directions, the matrix is diagonal. Its energy on a vector with coordinates a and b is three a squared plus b squared. It cannot be negative, even though the original off-diagonal entries couple the two coordinates.

This is the simplest form of the finite-dimensional spectral theorem: every self-adjoint matrix admits an orthonormal basis of eigenvectors, and all its eigenvalues are real. The positivity of such a matrix is equivalent to nonnegativity of those eigenvalues.

Why are eigenvalues real? If A x equals lambda x for a nonzero vector, then the inner product of A x with x equals lambda times the squared norm of x. Self-adjointness makes the left side real, so lambda must be real. Why are different eigenspaces perpendicular? Evaluate the same mixed inner product in two ways, moving A from one slot to the other. Distinct real eigenvalues force the inner product to vanish.

Those short arguments explain why diagonalization is especially clean for self-adjoint matrices. General matrices may have complex eigenvalues, nonorthogonal eigenvectors, or too few eigenvectors to form a basis.

## A positive operator need not look positive

Let T be any bounded linear operator on a Hilbert space. Form T adjoint T. For any x, the quadratic measurement associated with this product is exactly the squared length of T x. It is never negative. Thus T adjoint T is positive.

This construction appears whenever a measurement procedure has an associated least-squares error. If T maps an unknown signal to predicted observations, the quantity measuring squared prediction length is governed by T adjoint T. Its positivity is built into the geometry, not into the numerical signs of a chosen matrix.

Orthogonal projections give another example. Project onto a closed subspace and then compare the result with the original vector. The quadratic measurement of the projection is the squared length of the projected component. Every orthogonal projection is positive and self-adjoint. Its only possible eigenvalues in finite dimensions are zero and one.

But a self-adjoint operator need not be positive. A reflection across a line has one eigenvalue equal to one and another equal to negative one. It preserves lengths and is self-adjoint, yet its quadratic measurement can be negative. Self-adjointness expresses symmetry; positivity adds an ordering condition.

## Positive square roots

For a positive matrix, computing a square root becomes natural after diagonalization. Take its nonnegative eigenvalues, replace each by its ordinary nonnegative square root, and retain the same eigenvectors. The resulting matrix B is positive and satisfies B composed with B equals A.

For our example with eigenvalues three and one, the positive square root has eigenvalues square root of three and one. There is no need to guess entries and solve a nonlinear system of matrix equations. The spectral coordinates turn the construction into scalar arithmetic.

Among positive square roots the answer is unique. There may be other square roots that are not positive, because signs can be changed on eigenspaces. The positivity condition selects the natural one.

In infinite dimensions, a positive bounded self-adjoint operator also has a unique positive bounded square root. Proving this in general will require a more flexible way to apply scalar functions to operators. The familiar matrix construction tells us what that larger theory must recover.

## Ordering operators by their energy

If A and B are self-adjoint, we say A is no greater than B when B minus A is positive. This means that the quadratic measurement of A never exceeds that of B on any vector.

For positive operators, the order is about all vectors at once. Looking at matrix entries does not tell the whole story. Even multiplying positive operators together need not produce a positive operator if they fail to commute. To see the issue, remember that a positive operator must be self-adjoint. The product AB has adjoint BA, and those may differ.

This noncommutativity is one reason functional calculus is subtle. A function of a single self-adjoint operator behaves like ordinary scalar algebra, because all polynomial expressions in that operator commute with one another. Functions of two different operators are a different problem.

## A multiplication operator with no eigenvectors

Return to the Hilbert space of square-integrable functions on the unit interval. Define A to multiply a function by its position t. The quadratic measurement is the integral of t times the squared magnitude of the function. Since t lies between zero and one, A is positive. It is also self-adjoint.

Yet it has no nonzero eigenvectors. If multiplying by t always gave a fixed scalar lambda times the original function, then the function could be nonzero only where t equals lambda. A single point has zero measure, so the resulting square-integrable vector would be zero.

The operator is positive, bounded, and self-adjoint, but it has no eigenbasis. Nevertheless we know what its positive square root should do: multiply by the ordinary square root of t. This example tells us that applying functions to operators must eventually work without diagonalizing into eigenvectors.

That is the transition from matrix spectral theory to functional calculus. The goal is not to abandon the familiar diagonal picture; it is to preserve exactly what made the picture useful when no list of eigenvectors exists.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A bounded \(A:H\to H\) is self-adjoint if \(A=A^*\). It is positive, written \(A\ge0\), if \(A=A^*\) and \(\langle Ax,x\rangle\ge0\) for every \(x\). Over a complex Hilbert space the reality of all quadratic forms \(\langle Ax,x\rangle\) itself implies self-adjointness by polarization.

For \(A=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), normalized eigenvectors \(u_+=(1,1)/\sqrt2\), \(u_-=(1,-1)/\sqrt2\) have eigenvalues \(3\) and \(1\). Thus
\[
A=3u_+u_+^*+u_-u_-^*,\qquad A^{1/2}=\sqrt3\,u_+u_+^*+u_-u_-^*.
\]
For an orthogonal projection \(P=P^*=P^2\), \(\langle Px,x\rangle=\|Px\|^2\). For \(T\in\mathcal B(H)\), \(T^*T\ge0\).

For \(A=M_t\) on \(L^2([0,1])\), \(\langle Af,f\rangle=\int_0^1 t|f(t)|^2dt\), \(0\le A\le I\), and \(A^{1/2}=M_{\sqrt t}\). The latter statement is an explicit multiplication-operator calculation, not an appeal to a complete eigenbasis.

### Exercises with answers

1. **Negative energy.** Find a unit vector on which the reflection \(\operatorname{diag}(1,-1)\) has negative quadratic measurement. **Answer:** \((0,1)\), giving \(-1\).
2. **Square root.** Determine the positive square root of \(\operatorname{diag}(4,9)\). **Answer:** \(\operatorname{diag}(2,3)\).
3. **Not entrywise.** Is \(\begin{pmatrix}1&2\\2&1\end{pmatrix}\) positive? **Answer:** No; eigenvalues are \(3,-1\).
4. **Products.** Explain why positivity of A and B does not alone ensure positivity of AB. **Answer:** AB may fail to be self-adjoint if AB differs from BA.

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis, compact and self-adjoint operator lectures](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
