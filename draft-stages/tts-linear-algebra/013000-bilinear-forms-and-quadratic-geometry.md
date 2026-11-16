# 013000 — Bilinear and Quadratic Forms: Curvature, Energy, and Signature

**Track:** Linear Algebra from First Principles. **Background:** matrices, duals, inner products and eigenvalues. **Question:** what does a measurement involving two directions tell us about geometric shape?

<!-- BEGIN SPOKEN LECTURE -->

# Bilinear and Quadratic Forms: Curvature, Energy, and Signature

A linear functional takes one vector and returns a number. A bilinear form takes two vectors and returns a number, linearly in each argument. It can measure lengths and angles, as an inner product does, but it can also measure signed area, energy interactions, or mixed second derivatives. The resulting quadratic forms are the language of local optimization, Riemannian metrics, and much of mathematical physics.

## Start with two inputs

Consider the rule that takes two plane vectors, multiplies their first coordinates and adds their second coordinates multiplied together. That is the dot product, an example of a symmetric bilinear form. Another rule takes the first coordinate of the first vector times the second coordinate of the second, then subtracts the second coordinate of the first times the first coordinate of the second. That is the determinant of the two vectors, an alternating bilinear form. Swapping its inputs reverses the sign.

Both rules are linear in either input when the other is held fixed, yet they describe different geometry. The dot product of a nonzero vector with itself is positive. The determinant of any vector with itself is zero. Symmetry and alternation are different structural properties; one cannot infer them from the word bilinear alone.

Choose a basis. Any bilinear form B has a matrix M whose entry in row i and column j is B of basis vector i with basis vector j. On coordinate columns x and y, the form is x transpose times M times y. Symmetry of the form corresponds to a symmetric matrix. If we change coordinates using a matrix P, the new matrix is P transpose times M times P. This is congruence, not the similarity change used for linear operators. The distinction matters because a bilinear form eats two vectors whereas an operator sends one vector to another.

## A quadratic form measures a vector against itself

Define Q of v to be B of v with itself. If B is symmetric, Q records its diagonal behavior. For example, take Q of x, y equal to the square of x minus y. This is always nonnegative, but it vanishes for every vector along the line x equals y. The corresponding symmetric matrix has rows one, minus one and minus one, one. It has rank one. This quadratic form is positive semidefinite, not positive definite.

Now consider Q of x, y equal to x squared minus y squared. Along the horizontal axis it is positive except at the origin; along the vertical axis it is negative. The matrix has one positive and one negative eigenvalue. This form is indefinite. The origin is not a local minimum or maximum of Q; arbitrarily close points have both positive and negative values.

The signature records how many positive, negative, and zero directions remain after diagonalizing a real symmetric form by a suitable change of coordinates. Sylvester's law of inertia says these counts do not depend on which basis we used. Individual matrix entries may change dramatically, but the numbers of intrinsically positive and negative directions do not.

## From quadratic forms to a second derivative test

At a critical point of a smooth function of several variables, the first derivative vanishes. The leading correction to the function's value is often a quadratic expression involving its Hessian: the matrix of second partial derivatives. When the Hessian is positive definite, every sufficiently small nonzero displacement raises the function value, yielding a strict local minimum. A negative-definite Hessian gives a strict local maximum. An indefinite Hessian produces a saddle point.

But a zero eigenvalue makes the second derivative test inconclusive. Consider the function x to the fourth power at zero. Its second derivative vanishes there, yet zero is a strict local minimum. Consider minus x to the fourth power: the same second derivative, but a strict local maximum. The quadratic approximation does not contain enough information. We must examine higher-order terms.

This example is a valuable warning: a sufficient condition is not a necessary one. Positive definite Hessian proves a strict local minimum, but failure of positive definiteness does not disprove one.

## How a metric differs from a general form

A Riemannian metric assigns a positive-definite symmetric bilinear form to the tangent space at every point, smoothly varying with the point. It measures squared lengths of tangent vectors and angles between them. At one point, an appropriate basis can make its matrix the identity. Across a curved manifold, however, no single coordinate system need make the metric constant everywhere. Curvature measures part of the obstruction to such a global simplification.

Indefinite nondegenerate forms also play an important role. In spacetime geometry, a Lorentzian metric has one time-like direction and space-like directions with opposite sign, under a chosen convention. It does not give a positive squared length to every nonzero tangent vector. Nevertheless it is a symmetric nondegenerate bilinear form, so much of the same algebra applies with different geometric consequences.

## Polarization reconstructs cross terms

If B is symmetric over the real numbers, we can recover B of u and v from Q. Evaluate Q on u plus v and subtract Q on u and Q on v. The difference is twice B of u and v. So knowledge of the quadratic form on every vector determines the symmetric bilinear form. We call this polarization.

Alternating forms cannot be recovered by evaluating a vector twice, because B of v with v always vanishes. Their information lives in how distinct directions interact. This is the distinction between the metric geometry of inner products and the area geometry of symplectic forms.

Bilinear forms are a common language for phenomena that can look unrelated: a Hessian in optimization, the dot product in Euclidean space, a Lorentzian spacetime interval, or an alternating two-form on a symplectic manifold. Learning their transformations and positivity conditions gives us a reliable way to move between these subjects without confusing the different kinds of structure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A bilinear form \(B:V\times V\to\mathbb R\) has coordinate form \(B(u,v)=u^TMv\); under \([u]_{\rm old}=P[u]_{\rm new}\), its matrix becomes \(M_{\rm new}=P^TM_{\rm old}P\). A symmetric form has quadratic form \(Q(v)=B(v,v)\) and polarization \(B(u,v)=\tfrac12(Q(u+v)-Q(u)-Q(v))\). Sylvester inertia theorem asserts invariance of the counts of positive, negative and zero entries under real congruence diagonalization. For \(Q(x,y)=(x-y)^2\), \(M=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), with eigenvalues two and zero. For \(Q(x,y)=x^2-y^2\), the inertia is \((1,1,0)\).

For \(f\in C^2\), \(f(x_0+h)=f(x_0)+Df(x_0)h+\tfrac12h^T\nabla^2f(x_0)h+o(\|h\|^2)\). Positive-definite Hessian at a critical point is sufficient for a strict local minimum, not necessary.

### Exercises with answers

1. Is \(Q(x,y)=(x-y)^2\) positive definite? **Answer:** no, it vanishes on the nonzero line \(x=y\).
2. Determine the signature of \(x^2-y^2\). **Answer:** one positive and one negative direction.
3. Why does an alternating form satisfy \(B(v,v)=0\)? **Answer:** exchanging identical arguments reverses sign, hence the value is its negative over a field of characteristic not two.
4. Does a zero Hessian force a critical point to be a saddle? **Answer:** no, \(x^4\) has a strict minimum with zero Hessian at zero.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), multilinear algebra and bilinear forms.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), symmetric and positive-definite matrices.
- [Sylvester's law of inertia](https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia).
