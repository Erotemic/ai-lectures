# 044000 — Matrix Functions: Turning Scalar Formulas into Operator Formulas

**Track:** Analysis from First Principles. **Background:** Eigenvectors, self-adjoint matrices, inverses, and elementary scalar functions. **Question:** What does it mean to take an exponential, square root, or reciprocal of a matrix?

<!-- BEGIN SPOKEN LECTURE -->

# Matrix Functions: Turning Scalar Formulas into Operator Formulas

You know how to square a matrix: multiply it by itself. You also know how to add a multiple of the identity. But what does it mean to take the exponential of a matrix? Or to take its square root? Or to evaluate a function that has no simple polynomial expression?

For a self-adjoint matrix, the answer starts with one geometric idea. Find a set of perpendicular eigenvector directions. In each of those directions, the matrix acts by multiplication by an ordinary real number. A scalar function can then act on that number. Finally, put the directions back together.

This is the finite-dimensional functional calculus. It is not merely a notation for manipulating matrix formulas. It turns a collection of scalar instructions into a linear transformation with well-defined action on every vector.

## Follow a vector through its spectral pieces

Consider a matrix that stretches one diagonal direction by a factor of three and the perpendicular diagonal direction by a factor of one. We encountered a concrete example: a two-by-two matrix with twos on the diagonal and ones off the diagonal.

Any vector in the plane decomposes uniquely into a piece along the first direction and a piece along the second. Applying the matrix multiplies the first piece by three and the second piece by one. Applying the matrix twice multiplies them by nine and one. The same decomposition works for every polynomial in the matrix.

Now replace the square function by the square-root function. We simply multiply the first component by the square root of three and leave the second component unchanged. This defines a positive square root of the matrix without ever guessing its entries.

For the exponential, multiply the two components by e cubed and e to the first power. For the reciprocal, multiply them by one third and one, provided no eigenvalue is zero. The rules are scalar once we have the perpendicular decomposition.

## Spectral projections as switches

We can make that construction coordinate free. Let P one be the orthogonal projection onto the eigenspace of eigenvalue three, and P two the projection onto the eigenspace of eigenvalue one. Then the original operator is three times P one plus one times P two.

A function f of the operator is f of three times P one plus f of one times P two. The projections behave like switches selecting independent frequency channels. They add up to the identity, and projecting onto one channel after another gives zero.

This formula explains why the same eigenvectors work for every function of the matrix. The function changes only the scalar multiplier assigned to each spectral channel. It does not change the spectral directions themselves.

A scalar function only needs to be defined at the eigenvalues. If two functions disagree everywhere except at one and three, but agree at those two points, they define the same function of this matrix. That is the finite version of saying that the spectrum is the correct domain for functional calculus.

## Compute an inverse without a symbolic trick

Let us compute a more interesting function. Take f of t to be one divided by t plus one. For our matrix with eigenvalues three and one, the spectral multipliers are one fourth and one half.

Reassemble the operator from the two projections. The resulting matrix has three eighths on the diagonal and negative one eighth off the diagonal. If you multiply it by the original matrix plus the identity, you obtain the identity exactly.

So f of A really is the inverse of A plus I. This may seem obvious from notation, but the spectral construction tells us why it is true and when it can fail. If the scalar denominator vanished at an eigenvalue, there would be no bounded inverse. The functional formula would not rescue an impossible division.

## Two kinds of exponential

An exponential of a self-adjoint matrix is positive and invertible, since its eigenvalue multipliers are positive. An exponential of i times a self-adjoint matrix behaves differently: each eigenvalue multiplier lies on the unit circle in the complex plane. Its magnitude is one, so the operator preserves lengths. In other words, it is unitary.

This contrast is central in applications. Exponentials with negative real spectral multipliers can damp signals. Exponentials with imaginary spectral multipliers can rotate their phases without losing energy. These two types of evolution will later reappear as the heat equation and the Schrödinger equation.

A different warning: the matrix exponential of A plus B does not generally equal the product of the matrix exponentials of A and B. For ordinary numbers it does. For matrices it requires commuting operators, or additional special structure. The obstacle is not the exponential function; it is noncommutativity between distinct operators.

## What if a matrix is not self-adjoint?

For a diagonalizable but non-self-adjoint matrix, we can still apply a scalar function on its eigenvalues by using an invertible eigenvector matrix and conjugating a diagonal matrix back. But those eigenvectors need not be perpendicular. The resulting numerical behavior may be sensitive to small perturbations.

For a matrix with a Jordan block, knowing values of f at the eigenvalues is no longer enough. Derivatives of f may be required. Consider a two-by-two matrix with a single eigenvalue zero and a one just above the diagonal. Its square is zero. The exponential is therefore exactly the identity plus the matrix. More generally an analytic function on this Jordan block depends on its value and first derivative at zero.

So functional calculus has different versions with different assumptions. The self-adjoint version treats very general continuous functions because perpendicular spectral geometry keeps everything controlled. For arbitrary matrices, analytic functions give a powerful alternative.

## The infinite-dimensional challenge

For a finite self-adjoint matrix, the spectral pieces are finitely many, and everything is built by addition. What changes in infinite dimensions? There may be infinitely many eigenvectors; an eigenvalue list may have limit points; and some self-adjoint operators have no eigenvectors at all.

But the matrix construction gives us a specification to preserve. Functions of an operator should respect sums and products of functions. Real functions should give self-adjoint outputs. Nonnegative functions should give positive outputs. The output should depend only on the function's values on the spectrum. And approximation of scalar functions should produce controlled approximation of operators.

These requirements will guide a construction that works even when the spectral pieces cannot be numbered one by one. The finite matrix formula is not discarded. It becomes the model for a much broader theorem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

If \(A=A^*\in M_n(\mathbb C)\), write \(A=\sum_{j=1}^m\lambda_jP_j\) with distinct real \(\lambda_j\) and mutually orthogonal spectral projections \(P_j\), \(\sum P_j=I\). Any function \(f:\sigma(A)\to\mathbb C\) defines
\[
f(A)=\sum_{j=1}^m f(\lambda_j)P_j.
\]
The calculus satisfies \((fg)(A)=f(A)g(A)\), \(\overline f(A)=f(A)^*\), \(\sigma(f(A))=f(\sigma(A))\), and \(\|f(A)\|=\max_{\lambda\in\sigma(A)}|f(\lambda)|\).

For \(A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), the explicit projections are \(P_+=\tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\) and \(P_-=\tfrac12\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\). Thus
\[
(A+I)^{-1}=\tfrac14P_++\tfrac12P_-=\tfrac18\begin{pmatrix}3&-1\\-1&3\end{pmatrix}.
\]
For a nilpotent Jordan block \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), \(N^2=0\) and \(f(N)=f(0)I+f'(0)N\) for analytic f near zero. This is **not** continuous functional calculus for arbitrary nonnormal matrices.

### Exercises with answers

1. **Polynomial.** For \(A=\operatorname{diag}(2,5)\), find \(A^2-3A+I\). **Answer:** \(\operatorname{diag}(-1,11)\).
2. **Heat.** If \(A\ge0\), what is the norm of \(e^{-tA}\) for \(t\ge0\)? **Answer:** \(\max_{\lambda\in\sigma(A)}e^{-t\lambda}=e^{-t\min\sigma(A)}\) in finite dimensions; it is at most one.
3. **Unitary.** Why is \(e^{itA}\) unitary for self-adjoint A and real t? **Answer:** In an orthonormal eigenbasis each diagonal multiplier has modulus one.
4. **Jordan.** Evaluate \(e^N\) for \(N^2=0\). **Answer:** \(I+N\).

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis, spectral theorem lectures](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [Michael Taylor, Lectures on Banach Algebras, holomorphic calculus](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf).
