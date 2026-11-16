# 007000 — Eigenvalues and Eigenvectors: Finding Directions That Do Not Turn

**Track:** Linear Algebra from First Principles. **Background:** matrices, kernels and determinants. **Question:** can one coordinate system reveal a transformation's independent modes?

<!-- BEGIN SPOKEN LECTURE -->

# Eigenvalues and Eigenvectors: Finding Directions That Do Not Turn

Suppose a transformation stretches some vectors, rotates others, and mixes coordinates. If we apply it repeatedly, a generic vector may become difficult to track. But perhaps there are special directions that the transformation does not turn at all. They may grow, shrink, or reverse, yet remain on the same line. Those are eigenvectors, and their scaling factors are eigenvalues.

## An eigenvector is a direction, not just a number

A nonzero vector v is an eigenvector of a linear operator T if applying T gives a scalar multiple of v. The scalar is its eigenvalue. The zero vector is excluded because every scalar would satisfy the equation at zero and tell us nothing.

Take the map that doubles the x coordinate and triples the y coordinate. The horizontal direction is an eigenvector with eigenvalue two; the vertical direction is an eigenvector with eigenvalue three. Apply the map ten times: the horizontal component is multiplied by two ten times and the vertical component by three ten times. The decomposition makes long-term behavior transparent.

A vector such as one, one is not an eigenvector, because its image two, three points in a different direction. Yet one, one is the sum of the two coordinate eigenvectors. Knowing those modes tells us exactly how its image evolves.

## Finding the special directions

To find an eigenvalue of a matrix A, solve A v equals lambda times v. Rearrange this as A minus lambda times the identity, acting on v, equals zero. We seek a nonzero solution, so this new matrix must have a nontrivial kernel. In a finite-dimensional square matrix that happens precisely when its determinant is zero. The resulting polynomial equation in lambda is the characteristic equation.

Consider the matrix with first row two, one and second row zero, three. The characteristic polynomial is the product of two minus lambda and three minus lambda, because the matrix is triangular. Its eigenvalues are two and three. For eigenvalue two, the equation forces the second coordinate to be zero; the first coordinate can be anything. The vector one, zero works. For eigenvalue three, the equations force the two coordinates to be equal. The vector one, one works.

Those two eigenvectors are independent. Arrange them as the columns of a change-of-basis matrix. In their basis, our original upper-triangular matrix becomes diagonal, with entries two and three. That is diagonalization. It is not making the map simpler by approximation; it is describing the exact same map in directions adapted to its action.

## Why distinct eigenvalues help

Eigenvectors for distinct eigenvalues are linearly independent. To see the central idea, suppose one vector with eigenvalue two were a multiple of another with eigenvalue three. Applying the operator would have to multiply that same nonzero direction by both two and three, which is impossible. A slightly longer induction proves the result for any number of distinct eigenvalues.

Therefore, an n-dimensional operator with n distinct eigenvalues has an eigenbasis and is diagonalizable. But repeated eigenvalues do not guarantee enough eigenvectors. Consider a matrix with first row one, one and second row zero, one. Its only eigenvalue is one. The eigenvector equation forces the second coordinate to be zero. Only one independent eigenvector remains, so there is no basis of eigenvectors for the plane.

Repeated application of this matrix is revealing. It contains a shear. After n steps, the upper-right entry becomes n. The evolution includes polynomial growth even though every eigenvalue equals one. A theory based only on eigenvalues would miss this behavior. Generalized eigenvectors and Jordan blocks explain it; they are a later refinement, not a reason to dismiss eigenvalues.

## Real versus complex modes

Rotate the plane by ninety degrees. No nonzero real vector stays on its own line; every one is turned. So the real matrix has no real eigenvector. If we allow complex scalars, it has eigenvalues i and minus i. Complex vector spaces make many spectral statements cleaner, even when the original system is real.

A real symmetric matrix is better behaved than an arbitrary real matrix: it has real eigenvalues and an orthonormal eigenbasis. This is the spectral theorem, which will follow after we introduce inner products and adjoints. Thus diagonalization is not universal, but structure can guarantee it.

## Modes in differential equations and physical systems

Imagine a linear differential equation whose time derivative equals A times the current state. If the initial state is an eigenvector, the solution stays in that eigen-direction, multiplied by an exponential of the eigenvalue times time. A positive real eigenvalue grows, a negative one decays. Complex conjugate eigenvalues can produce oscillation. A general state decomposed into eigenmodes, when a basis exists, becomes a sum of such simpler solutions.

In vibration problems, normal modes are eigenvectors of suitable operators; the associated eigenvalues determine frequencies or frequency squares. In data analysis, eigenvectors of covariance matrices describe principal directions of variation. In quantum mechanics, eigenvectors of self-adjoint operators describe states with definite measured values. Each application adds hypotheses, but the shared core is the search for directions that do not mix.

An eigenvalue is not the same thing as a singular value. Eigenvalues describe invariant directions for a square operator and may be negative or complex. Singular values measure nonnegative stretch factors and exist for every real or complex matrix. We will build that distinction carefully rather than treating the two as synonyms.

The true power of eigenvectors is that they can turn a coupled problem into independent scalar problems. When they do not form a basis, the failure itself has a mathematical explanation. That is an essential part of learning the subject.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An eigenpair satisfies \(Av=\lambda v\), \(v\ne0\). Eigenvalues of \(A\in\mathbb F^{n\times n}\) satisfy \(\det(A-\lambda I)=0\) over a field containing the roots; the eigenspace is \(\ker(A-\lambda I)\). For \(A=\begin{psmallmatrix}2&1\\0&3\end{psmallmatrix}\), eigenvectors \((1,0)\) and \((1,1)\) form columns of \(P=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\); \(P^{-1}AP=\operatorname{diag}(2,3)\). The Jordan shear \(J=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) has \(J^n=\begin{psmallmatrix}1&n\\0&1\end{psmallmatrix}\) and only one independent eigenvector.

### Exercises with answers

1. Find the eigenvalues of \(\operatorname{diag}(4,-1)\). **Answer:** four and minus one.
2. Is \((1,1)\) an eigenvector of \(\operatorname{diag}(2,3)\)? **Answer:** no.
3. Is every triangular matrix diagonalizable? **Answer:** no; the Jordan shear is a counterexample.
4. Why does a ninety-degree rotation have no real eigenvector? **Answer:** it takes each nonzero vector to a perpendicular direction, not a real multiple.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), invariant subspaces, eigenvalues and upper-triangular operators.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), eigenvalue computations.
- [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).
