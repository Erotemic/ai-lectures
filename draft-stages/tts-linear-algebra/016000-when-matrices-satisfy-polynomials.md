# When a Matrix Satisfies Its Own Polynomial: Cayley–Hamilton and the Minimal Polynomial

**Track:** Linear Algebra from First Principles. **Background:** linear maps, matrix multiplication, determinants, characteristic polynomials, and eigenvectors. **Purpose:** bridge elementary eigenvalue calculations to algebraic control of arbitrary finite-dimensional operators.

<!-- BEGIN SPOKEN LECTURE -->

# When a Matrix Satisfies Its Own Polynomial

Suppose we are studying the same transformation applied repeatedly. We know the matrix that describes one step. We want the result after a thousand steps, or we want to understand a differential equation whose coefficients are that matrix. Multiplying matrices a thousand times is possible, but it hides the structure. Can we replace enormous powers of a matrix with a few simpler ones, exactly rather than approximately?

For a matrix of size two, the surprising answer is that every power can be expressed using only the identity matrix and the original matrix. For a matrix of size three, we need at most the first three powers. Something much more general is going on: a square matrix satisfies a polynomial equation of its own.

To see what that means, we must be careful about two different kinds of inputs to a polynomial. One is an ordinary number. The other is a linear transformation.

## Evaluate a polynomial at a matrix

Start with a polynomial in an ordinary variable, such as the square of x minus four x plus four. When we put the number three into it, we obtain one. Now replace the variable with a square matrix A. We define the corresponding matrix expression by taking A squared, subtracting four times A, and adding four times the identity matrix. The identity is essential. An ordinary constant in a polynomial becomes that constant times the identity, so that all the terms are matrices of the same size.

This substitution behaves well with addition and multiplication of polynomials. If the polynomial factors into x minus two times x minus two, its matrix evaluation is A minus twice the identity, multiplied by itself. These factors commute because each is built from powers of the same matrix. That detail will matter later. Two completely arbitrary matrices need not commute.

An equation saying that a polynomial evaluated at A gives the zero matrix is called an annihilating polynomial identity. It says more than a collection of facts about the eigenvalues. It holds when we apply the matrix expression to every vector, not just to the vectors we already know how to diagonalize.

Take the matrix with rows two, one and zero, two. Applying it to the horizontal unit vector doubles that vector. Applying it to the vertical unit vector sends some of it horizontally, as well as doubling its vertical part. Write this matrix as twice the identity plus a matrix N that has one in the upper-right corner and zeros elsewhere. Applying N twice gives zero: the first application can move the second coordinate into the first, but the second application has nowhere left to send it. Therefore the square of A minus twice the identity is zero. In other words, A squared minus four A plus four times the identity is the zero matrix.

Yet this matrix is not diagonalizable. It has only one independent eigenvector. The polynomial identity continues to work precisely where the easiest eigenvector method has stopped working.

## The characteristic polynomial is not merely a root-finding trick

In elementary linear algebra we find eigenvalues by taking the determinant of x times the identity minus A and setting it equal to zero. The result is the characteristic polynomial. Its roots are the eigenvalues, at least when we allow complex roots. But the characteristic polynomial has another property, called the Cayley–Hamilton theorem: substitute the matrix itself for x and the result is the zero matrix.

For a two-by-two matrix, the characteristic polynomial is x squared minus the trace times x plus the determinant. The trace is the sum of the diagonal entries. The theorem says that A squared, minus the trace of A times A, plus the determinant of A times the identity, is zero.

Consider the matrix whose rows are one, two and three, four. Its trace is five and its determinant is minus two. The identity says A squared minus five A minus two times the identity is zero. We can verify that by multiplying: A squared has rows seven, ten and fifteen, twenty-two. Five A has rows five, ten and fifteen, twenty. Subtraction leaves two on the diagonal and zero elsewhere, which is exactly canceled by subtracting two times the identity.

That computation may look like a coincidence. It is not. For a general square matrix there is a polynomial identity obtained from the determinant of x times the identity minus A. One exact proof starts with the adjugate identity: the matrix times its adjugate equals its determinant times the identity. Treat x as an ordinary variable, expand both sides in powers of x, and compare the matrix coefficients. Those equations link each coefficient to the next. Multiplying the equations by successive powers of A causes them to telescope, until the characteristic polynomial evaluated at A is left over. The result is zero. The full coefficient calculation belongs in the written companion, but the logical idea is important: we establish a polynomial identity with an ordinary variable first, then obtain the identity for A by comparing its coefficients. We do not make an unjustified substitution into an expression with arbitrary matrix coefficients.

Cayley–Hamilton is valid over the real or complex numbers, and in fact over any commutative coefficient ring. It does not require the matrix to be diagonalizable.

## Reduce all large powers to a small collection

Return to the two-by-two example with trace five and determinant minus two. Its identity gives A squared equals five A plus two times the identity. Multiply both sides by A. Then A cubed equals five A squared plus two A. Replace A squared using the same identity again, and A cubed becomes twenty-seven A plus ten times the identity. We have computed a third power without three separate matrix multiplications.

More generally, divide any polynomial by the characteristic polynomial, as in ordinary polynomial long division. The remainder has degree smaller than the matrix size. Because the characteristic polynomial vanishes when evaluated at A, the original polynomial and its remainder produce exactly the same matrix. This gives a finite collection of powers from which every polynomial function of A can be assembled.

It also gives a useful formula for inverse matrices. If A is invertible, the constant term of its characteristic polynomial is nonzero. The Cayley–Hamilton equation can then be rearranged to express A inverse as a polynomial in A. This is not necessarily the best numerical way to invert a matrix. It is an algebraic demonstration that the inverse lives in the same family of transformations generated by A.

## The shortest equation is often more informative

Cayley–Hamilton provides an annihilating polynomial, but it may contain unnecessary factors. Consider the identity matrix of size two. Its characteristic polynomial is the square of x minus one. But we do not need to square anything to annihilate it: the identity matrix minus itself is already zero. The polynomial x minus one is enough.

Now compare our shearing matrix, twice the identity plus N. Here A minus twice the identity is N, and N is not zero. We must square the expression before it vanishes. Its shortest monic annihilating polynomial is the square of x minus two.

This shortest monic polynomial is called the minimal polynomial. For every square matrix there is a unique one. To understand uniqueness, suppose two different monic polynomials of the least possible degree both annihilated A. Their difference would have smaller degree and would still annihilate A, which is impossible unless their difference is zero. To understand why the minimal polynomial divides every annihilating polynomial, divide the latter by the minimal polynomial. Evaluate that division at A. Both the original polynomial and the multiple of the minimal polynomial vanish, so the remainder also vanishes. Its degree is too small unless it is zero.

This is more than a neat definition. The minimal polynomial measures precisely how much of the characteristic polynomial is needed to control the transformation. Its degree tells us how many initial powers may be needed for the polynomial calculations of that matrix.

## What repeated roots do and do not tell us

A characteristic polynomial can have repeated roots for different reasons. The identity matrix has a repeated eigenvalue because the same eigenvalue acts independently on two directions. The shearing example also has a repeated eigenvalue, but the two directions are coupled. The characteristic polynomial alone does not distinguish these situations. The minimal polynomial does.

Over the complex numbers, a matrix is diagonalizable exactly when its minimal polynomial factors into distinct linear factors, without a repeated factor. This is a powerful test, but it comes with an essential condition on the field. A real rotation through ninety degrees has no real eigenvectors, though it is diagonalizable over the complex numbers. Over the real numbers, the corresponding criterion is that the minimal polynomial split into distinct real linear factors. The phrase 'distinct roots' must be interpreted in the field over which diagonalization is intended.

Why does a repeated factor matter? A factor of the form x minus lambda, raised to the second or third power, may reveal a direction that is eventually killed by repeated application of A minus lambda times the identity, even if it is not killed after one application. Such a direction is called a generalized eigenvector. These generalized eigenvectors allow us to describe matrices like the shear without pretending that a missing eigenvector can be supplied by wishful thinking.

The distinction will also matter when we move from polynomials to functions such as the exponential. An ordinary eigenvector contributes a familiar scalar expression. A generalized eigenvector can contribute an additional factor of time. A repeated eigenvalue is not merely a duplicated entry in a list; it can carry extra dynamical information.

## The boundary between algebraic truth and numerical practice

The identities developed here are exact. In floating-point arithmetic, however, computing a characteristic polynomial and substituting a rounded matrix may accumulate considerable error. Near a repeated eigenvalue, tiny changes to the matrix can change the structure of its eigenspaces. The minimal polynomial is therefore a valuable mathematical descriptor, not an automatic recipe for a stable numerical algorithm.

When a numerical problem asks for a solution of a linear system, a matrix exponential, or selected eigenvalues, we usually choose factorizations or other algorithms designed for that task. Cayley–Hamilton explains what is possible algebraically. Conditioning and backward-error analysis explain which computations can be trusted.

We began by asking how to control repeated applications of one transformation. The answer is that finite-dimensional linear maps satisfy finite polynomial identities. The characteristic polynomial guarantees such an identity, and the minimal polynomial removes the unnecessary parts. Once we know that, we can study transformations without assuming every matrix has enough ordinary eigenvectors. That is the opening to generalized eigenspaces, algebraic spectral projections, and linear dynamics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an endomorphism \(A\in M_n(F)\), evaluate \(q(x)=\sum_{k=0}^d a_kx^k\) as \(q(A)=\sum_{k=0}^d a_kA^k\), where \(A^0=I\). This is a ring homomorphism \(F[x]\to M_n(F)\). Its kernel is a nonzero ideal, generated by the unique monic **minimal polynomial** \(m_A\). The Cayley–Hamilton theorem gives \(p_A(A)=0\) for \(p_A(x)=\det(xI-A)\), so \(m_A\mid p_A\).

### Cayley–Hamilton by coefficients, without illegal matrix substitution

Let \(\operatorname{adj}(tI-A)=\sum_{j=0}^{n-1}t^jB_j\), and \(p_A(t)=t^n+\sum_{j=0}^{n-1}c_jt^j\). The polynomial-matrix identity

\[
(tI-A)\operatorname{adj}(tI-A)=p_A(t)I
\]

implies, on comparing coefficients,

\[
B_{n-1}=I,\quad B_{k-1}-AB_k=c_kI\ (1\le k<n),\quad -AB_0=c_0I.
\]

Starting from \(A^n=A^nB_{n-1}\), substitute these recurrences successively to obtain

\[
A^n=-c_{n-1}A^{n-1}-\cdots-c_1A-c_0I.
\]

This proof is valid for matrices with coefficients in a commutative ring. Importantly, it **does not** evaluate a polynomial identity with possibly noncommuting matrix coefficients at \(t=A\).

For \(A=\begin{pmatrix}1&2\\3&4\end{pmatrix}\),
\[
p_A(t)=t^2-5t-2,\quad A^2=\begin{pmatrix}7&10\\15&22\end{pmatrix}=5A+2I,\quad A^3=27A+10I.
\]

For the shear \(S=\begin{pmatrix}2&1\\0&2\end{pmatrix}\), write \(S=2I+N\) with \(N^2=0\), \(N\ne0\). Both its characteristic and minimal polynomial are \((t-2)^2\). For \(2I\), the characteristic polynomial is \((t-2)^2\) but the minimal polynomial is \(t-2\).

**Diagonalization criterion.** For \(A\in M_n(\mathbb C)\), \(A\) is diagonalizable iff \(m_A\) is square-free. Over \(\mathbb R\), it is diagonalizable *over \(\mathbb R\)* iff \(m_A\) is a product of distinct monic linear polynomials in \(\mathbb R[t]\). The real rotation \(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) has \(m_A=t^2+1\) and no real eigenvectors.

### Problems with answers

1. For \(A=\operatorname{diag}(2,3)\), determine \(m_A\). **Answer:** \((t-2)(t-3)\).
2. For \(A=2I_3\), determine \(p_A\) and \(m_A\). **Answer:** \((t-2)^3\) and \(t-2\).
3. If \(A^2-3A+2I=0\), show that \(A\) is invertible and find \(A^{-1}\). **Answer:** multiply \(A(3I-A)=2I\), so \(A^{-1}=(3I-A)/2\).
4. If \(p(A)=0\), why does \(p(A)A^5=0\)? **Answer:** multiplying the zero matrix by any matrix gives zero; all polynomial factors in \(A\) commute.

### Source anchors and routes onward

- Sheldon Axler, [*Linear Algebra Done Right*, fourth edition](https://linear.axler.net/), chapters on generalized eigenvectors and characteristic/minimal polynomials.
- Jim Hefferon, [*Linear Algebra*](https://hefferon.net/linearalgebra/), eigenvalues, similarity, and polynomial calculations.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), elementary eigenvalues and matrix powers.
- [Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem) and [minimal polynomial (linear algebra)](https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)).

This lecture bridges `linear-algebra:006000` to generalized eigenvectors, `differential-equations:004000` and the finite-dimensional part of `analysis:046000`; it does **not** establish an infinite-dimensional spectral theorem.
