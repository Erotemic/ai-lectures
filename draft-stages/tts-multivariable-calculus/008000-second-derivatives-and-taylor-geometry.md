# 008000 — Hessians and Taylor's Formula: The Shape Beyond the Tangent Plane

**Track:** Multivariable Calculus from First Principles. **Background:** total derivatives and one-variable Taylor expansions. **Question:** what does the first-order approximation miss, and how does second-order geometry appear?

<!-- BEGIN SPOKEN LECTURE -->

# Hessians and Taylor's Formula: The Shape Beyond the Tangent Plane

A tangent plane captures the leading change in a smooth surface. But two surfaces can have the same tangent plane at a point and bend in entirely different ways. The second derivatives describe that bending. Collected into a matrix, they form the Hessian.

Consider the functions x squared plus y squared and x squared minus y squared. Both have value zero and gradient zero at the origin. Their tangent planes are the same horizontal plane. Yet the first is a bowl, rising in every nonzero direction, while the second is a saddle, rising along the x axis and falling along the y axis. First derivatives cannot distinguish them at the origin. Their second-order terms do.

## Differentiate a derivative

For a twice-differentiable scalar function of x and y, we can differentiate first with respect to x and then with respect to y, or vice versa. The resulting mixed partial derivatives measure how the x slope changes as y changes and how the y slope changes as x changes. Under the usual hypothesis of continuous second partial derivatives near the point, these mixed derivatives agree. The Hessian is then a symmetric matrix.

Why should symmetry matter? A symmetric matrix has real eigenvalues and an orthogonal set of eigenvectors. Along those eigenvector directions, the quadratic bending separates into independent curvatures. The Hessian is a linear-algebraic picture of local shape.

But do not drop the continuity qualification on the mixed-derivative theorem. At less regular points, both mixed second derivatives can exist and still differ. The elementary rule is powerful because it comes with hypotheses.

## The second-order Taylor approximation

For a smooth f, near a base point a, the value of f at a plus h can be approximated by f at a, plus the derivative of f applied to h, plus one half of h transposed times the Hessian at a times h. The remaining error is small compared with the square of the displacement length, provided the second derivatives are continuous near the point.

We can see where this comes from without memorizing a many-variable formula. Fix the displacement h and follow the line a plus t h as t runs from zero to one. Along this line, f becomes an ordinary one-variable function of t. Its first derivative is Df times h. Its second derivative is h transposed times the Hessian times h. Apply one-variable Taylor's theorem, and the multivariable formula follows.

The method of restricting to a line is valid here because a full smoothness hypothesis already gives uniform control of the derivatives. Contrast this with the failed path tests for continuity: there we tried to infer a global limit merely by checking selected curves. Here we derive an identity for each displacement from a theorem that already applies everywhere nearby.

## A computed saddle

Take the function exponential x times cosine y. At the origin its value is one. Its gradient there is one comma zero. The Hessian there has entries one and minus one along the diagonal, with zero off-diagonal entries. Therefore its quadratic Taylor approximation is one plus x plus one half times x squared minus one half times y squared. The first-order term tilts the surface in the x direction, and the opposite signs of the second-order terms describe different bending along x and y.

For a still simpler example, f equals x squared minus y squared has no remainder beyond second order. Its Hessian is the constant diagonal matrix with entries two and minus two. A displacement along the x axis raises the value by a square, while one along the y axis lowers it by a square. There is no local minimum or maximum at the origin despite the gradient being zero.

## The Hessian as a bilinear form

The expression h transposed H h is a quadratic form. A positive definite Hessian means this expression is positive for every nonzero h. A negative definite Hessian makes it negative. An indefinite Hessian has both signs. At a critical point these distinctions often classify a strict local minimum, a strict local maximum, or a saddle.

If the Hessian has a zero eigenvalue, the second-order test is inconclusive. The function x to the fourth at the origin has zero second derivative but a strict minimum. The function minus x to the fourth has the same zero second derivative but a strict maximum. The function x cubed has neither. Higher-order terms decide.

This is not a failure of Taylor's theorem. The theorem accurately reports that the quadratic contribution is absent. It is our attempt to classify the point using only that contribution that runs out of information.

## Why quadratic approximations matter

Optimization algorithms use Hessians to predict curvature and propose steps. Mechanics uses quadratic energy approximations to analyze the stability of an equilibrium. Statistics uses local quadratic approximations of log-likelihoods. Riemannian geometry later uses second derivatives of coordinate data to describe acceleration and curvature, with additional geometric care about what is coordinate invariant.

The Hessian completes a progression. Continuity controls values. The derivative predicts first-order change. The Hessian predicts second-order bending. Each layer requires stronger information, and each gives a more refined local model.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(f\in C^2(U)\), the Hessian is \(H_f(a)=(\partial_i\partial_j f(a))\), which is symmetric by Schwarz–Clairaut. Taylor's second-order formula is
\[
f(a+h)=f(a)+Df(a)h+\tfrac12 h^TH_f(a)h+o(\|h\|^2).
\]
The remainder \(o(\|h\|^2)\) follows from continuity of second derivatives. If \(\varphi(t)=f(a+th)\), then \(\varphi''(t)=h^TH_f(a+th)h\).

For \(f(x,y)=e^x\cos y\),
\[
f(0,0)=1,\quad\nabla f(0,0)=(1,0),\quad
H_f(0,0)=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
so \(f(x,y)=1+x+\frac12(x^2-y^2)+o(x^2+y^2)\). For the strict second-derivative test, evaluate the Hessian **at a critical point**; definiteness gives the corresponding strict local extremum and indefiniteness gives a saddle.

### Exercises with answers

1. Find the Hessian of \(x^2+3xy+2y^2\). **Answer:** \(\begin{pmatrix}2&3\\3&4\end{pmatrix}\).
2. Classify the origin for \(x^2-2y^2\). **Answer:** saddle, because the Hessian has one positive and one negative eigenvalue.
3. Can a zero Hessian classify a critical point? **Answer:** no; compare \(x^4\), \(-x^4\), and \(x^3\) at zero.
4. Why are the cross terms in \(h^THh\) doubled when \(H\) is symmetric? **Answer:** \(H_{ij}h_ih_j\) and \(H_{ji}h_jh_i\) contribute equally for each distinct pair.

### Sources and further reading

- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), second derivatives and Taylor polynomials.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), local extrema.
- [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix); [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem).
