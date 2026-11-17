# Multivariable Taylor Remainders: From a Line to a Reliable Bound

**Track:** Multivariable Calculus from First Principles. **Focus:** turn the second-order Taylor picture into a quantitative statement, with assumptions strong enough to justify an error bound and examples that distinguish them.

<!-- BEGIN SPOKEN LECTURE -->

# Multivariable Taylor Remainders: From a Line to a Reliable Bound

A quadratic model can look persuasive even when it is a poor guide. We replace a curved surface by its tangent plane, then add the bending described by its Hessian. But how far can we move before that replacement stops being trustworthy? The answer cannot be read from the Hessian at one point alone. We need information about how the Hessian changes between our starting point and the point we want to predict.

This question links multivariable calculus to optimization, numerical differential equations, and error estimation. A numerical algorithm proposes a step using a local model. A proof must decide how much of the actual function that model captures. We will derive the exact identity behind the familiar approximation, then turn it into a bound that can be checked.

## Begin with a path, not a memorized formula

Let f be a real-valued function of several real variables, defined on an open region. Pick a base point a and a displacement h such that the entire straight segment from a to a plus h remains inside the region. Suppose f has continuous second derivatives around this segment.

Define a one-variable function g of t by evaluating f at a plus t times h, where t runs from zero to one. At t equals zero we are at a; at t equals one we have arrived at a plus h. The chain rule gives g prime of t as the gradient of f at the moving point, dotted with h. Differentiating again gives g double prime of t as h transpose times the Hessian of f at that point times h.

Now use the fundamental theorem of calculus twice. First, the total change in g is the integral of its first derivative. Second, the first derivative at time t is its value at zero plus the integral of its second derivative from zero to t. Interchanging the resulting integrals produces a very useful exact statement. The value at a plus h equals the value at a, plus the gradient at a dotted with h, plus the integral from zero to one of one minus t, multiplied by h transpose, the Hessian at a plus t h, and h.

There is no neglected remainder in this identity. It is an equality. Only when we replace the changing Hessian along the path by the fixed Hessian at a do we introduce an approximation.

Because the integral of one minus t from zero to one is one half, that replacement yields the familiar quadratic expression: the function value, plus the linear term, plus one half of h transpose H at a times h. The remainder is another integral, but now its integrand contains the difference between the Hessian at a plus t h and the Hessian at a.

This form of the remainder is more informative than writing three dots after a polynomial. It tells us exactly what quantity controls the error.

## Continuous curvature and a small-oh remainder

Suppose we only know the Hessian is continuous at a. As the displacement h approaches zero, every Hessian along the segment approaches the Hessian at a. In a fixed matrix norm the maximum difference goes to zero. Meanwhile, each quadratic expression involving h is bounded by the matrix norm times the squared length of h.

Consequently the remainder divided by the squared length of h approaches zero. We say it is little-oh of the squared length. For sufficiently short displacements, the error is small compared with the quadratic scale. This is the correct general second-order Taylor statement under continuity of the Hessian.

Notice what it does not say. It does not promise a single numerical constant times the cube of the distance. Continuity can be much weaker than a Lipschitz estimate. Even a function with a continuous second derivative may have a Taylor remainder that decreases more slowly than the cube of the displacement length.

For example, in one variable, the function absolute x to the power two and a half has a continuous second derivative at zero, with value zero there. Its quadratic approximation at zero vanishes. But its actual value is the distance to the power two and a half, which is not bounded by a fixed constant times the distance cubed near zero. A small-oh quadratic remainder and a cubic bound are different claims.

## A hypothesis that yields a cubic error bound

Now impose an additional, quantitative condition. Suppose the Hessian is Lipschitz continuous on the segment with some constant L. This means that the matrix norm of the difference between Hessians at any two points is at most L times the distance between those points.

At the intermediate point a plus t h, that difference from the Hessian at a is at most L times t times the length of h. Insert this estimate into the integral remainder. The two appearances of h contribute two powers of its length. The Lipschitz difference contributes a third. What remains is the integral of t times one minus t, which equals one sixth.

We obtain a clean result: the absolute second-order Taylor error is at most L over six times the cube of the displacement length. The coefficient one sixth comes from the same one-dimensional integration that produced the quadratic term's coefficient one half. Nothing special has happened to the number of variables.

A common shortcut is to assert this bound because f has a third derivative. That can work if the third derivative is suitably bounded along the segment. But the bounded-Hessian-change condition is more general, and it states exactly what the calculation uses. Neither version is automatic from the existence of a Hessian at the starting point.

There is a related first-order estimate worth separating from this one. If the gradient is Lipschitz with constant M, then the error in the tangent-plane approximation is at most M over two times the squared distance. Here we have used a bound on the change of the first derivative to control the error after the linear term. At second order, we use a bound on the change of the second derivative to control the error after the quadratic term. The pattern is the same, but the hypotheses are one derivative apart.

## A calculation where the quadratic model misses a cubic term

Consider a function of x and y obtained by adding x squared, three times x y, two y squared, and x cubed. At the origin its value and gradient vanish. Its Hessian there has first row two and three, second row three and four.

The quadratic Taylor model at the origin is therefore x squared plus three x y plus two y squared. The actual function differs from this model by exactly x cubed. We do not need a numerical approximation to see the error.

Move from the origin to the point with x equal to one fifth and y equal to minus one tenth. The quadratic expression at that point is zero: four hundredths minus six hundredths plus two hundredths. Yet the actual function is one hundred and twenty-fifth. If we predicted zero, our absolute error would be eight thousandths.

Does the bound detect the possibility? The only entry of the Hessian that changes with position is the top-left entry, which changes by six times the change in x. In the Euclidean operator norm, a valid Lipschitz constant is six. The distance of our step is the square root of five hundredths, a little under a quarter. The cubic remainder bound says the error is no more than the cube of that distance. Numerically that is about eleven thousandths. The actual eight thousandths lies within the bound.

The striking part of this example is not that the estimate is conservative. It is that the quadratic prediction happens to cancel completely along the selected direction. A small predicted change does not imply a small absolute error. We must compare the model's margin to a bound on its remainder.

Suppose we wanted to certify that a proposed step decreases f. A negative quadratic prediction of one hundredth would not be enough if our maximum possible remainder were two hundredths. The true change could have either sign. If the quadratic prediction were negative three hundredths while the remainder was at most one hundredth, then descent would be certified. This simple bookkeeping becomes a central idea in globalization of optimization methods.

## Curvature in all directions, not just along coordinate axes

The Hessian is a matrix, but the second-order term is a scalar. It asks how much curvature is seen in the particular displacement h. Mixed second derivatives matter because most directions are not coordinate directions.

Rotate the coordinate axes and the matrix entries change. The value of h transpose H h does not change if we transform both the Hessian and h consistently under an orthogonal change of coordinates. It describes geometry, not a favorite set of axes.

When the Hessian is symmetric, its eigenvectors give orthogonal principal directions. Positive eigenvalues describe upward second-order bending, negative eigenvalues downward bending, and zero eigenvalues directions where the quadratic approximation alone is silent. This geometric reading is useful, but one must distinguish the eigenvalues of H at one point from bounds valid along a whole segment.

A quadratic model at a stationary point with positive-definite Hessian proves a strict local minimum, because for sufficiently small h the positive quadratic term dominates its little-oh quadratic remainder. If the Hessian is indefinite, suitable directions produce both positive and negative changes near the point, giving a saddle. If the Hessian is only positive semidefinite, the conclusion is inconclusive: higher-order terms decide what happens in its flat directions.

For instance, x squared plus y to the fourth has a strict minimum at the origin, although the Hessian there has a zero eigenvalue. Replace the positive y-to-the-fourth term by its negative, and the origin is no longer a minimum. Both functions have the same Hessian at that point.

## Error estimates are hypotheses translated into numbers

A Taylor polynomial is not just a computational trick. It is an assertion about a local relationship between a function and its derivatives. Different regularity assumptions produce different kinds of control. Existence of derivatives at one point gives less than continuity nearby; continuity gives less than a specified Lipschitz constant; and a local bound says nothing about a step that exits the region where it holds.

When reading an optimization proof or the specification of an approximation algorithm, ask three questions. What object is being approximated? Which derivative is controlled in the region of interest? And is the conclusion an asymptotic statement, a numerical bound, or a guarantee of the sign of a change?

With those distinctions in place, the Hessian stops being merely a matrix of second partial derivatives. It becomes the input to a model whose reliability we can quantify. That is the foundation on which Newton's method will stand.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Exact integral remainder

Let \(f\in C^2(U;\mathbb R)\), with the segment \([a,a+h]\subset U\). Define \(g(t)=f(a+th)\). Then

\[
 g''(t)=h^T\nabla^2 f(a+th)h,
 \qquad
 f(a+h)=f(a)+\nabla f(a)^Th+\int_0^1(1-t)g''(t)\,dt.
\]

Separating the constant Hessian gives

\[
 f(a+h)=f(a)+\nabla f(a)^Th+\tfrac12 h^T\nabla^2 f(a)h+R_2(a,h),
\]
\[
 R_2(a,h)=\int_0^1(1-t)h^T\big(\nabla^2 f(a+th)-\nabla^2 f(a)\big)h\,dt.
\]

If \(\nabla^2 f\) is continuous at \(a\), then \(R_2(a,h)=o(\|h\|^2)\). If \(\|\nabla^2 f(x)-\nabla^2 f(y)\|_2\le L\|x-y\|_2\) on the segment, then

\[
 |R_2(a,h)|\le L\|h\|_2^3\int_0^1 t(1-t)\,dt
 =\frac L6\|h\|_2^3.
\]

For \(\nabla f\) merely \(M\)-Lipschitz, the first-order remainder instead satisfies \(|f(a+h)-f(a)-\nabla f(a)^Th|\le M\|h\|_2^2/2\).

### Worked computation and an exact Hessian Lipschitz constant

For \(f(x,y)=x^2+3xy+2y^2+x^3\),

\[
 \nabla f=(2x+3y+3x^2,\,3x+4y)^T,
 \quad H(x,y)=\begin{pmatrix}2+6x&3\\3&4\end{pmatrix}.
\]

The spectral norm of \(H(x,y)-H(u,v)\) is \(6|x-u|\le6\|(x,y)-(u,v)\|_2\). Thus \(L=6\) is valid globally. For \(h=(1/5,-1/10)\), \(h^TH(0)h/2=0\), the true remainder is \(1/125=0.008\), and the bound is \(\|h\|^3=(\sqrt5/10)^3\approx0.01118\).

### Exercises with solutions

1. **One-derivative analog.** Derive the tangent-plane error from \(f(a+h)-f(a)=\int_0^1 \nabla f(a+th)^Th\,dt\). **Answer:** subtract \(\nabla f(a)^Th\), apply the gradient Lipschitz bound \(Mt\|h\|^2\), and integrate \(t\) to obtain \(M\|h\|^2/2\).
2. **Second-order but not cubic.** Why is \(f(x)=|x|^{5/2}\) a counterexample to a universal cubic bound from mere \(C^2\) regularity? **Answer:** \(f''(x)=(15/4)|x|^{1/2}\) for \(x\ne0\), continuously extending as zero; yet \(|f(x)|/|x|^3=|x|^{-1/2}\to\infty\).
3. **Flat directions.** Classify the origin for \(x^2+y^4\) and \(x^2-y^4\). **Answer:** strict minimum for the first; saddle for the second. Both have \(H(0)=\mathrm{diag}(2,0)\).
4. **Certified sign.** A step has quadratic predicted change \(-0.03\) with \(L\|h\|^3/6=0.01\). What is certified? **Answer:** the true change lies between \(-0.04\) and \(-0.02\), so strict descent is guaranteed.
5. **Different hypothesis.** Does a locally bounded Hessian suffice to make the *first-order* remainder \(O(\|h\|^2)\)? **Answer:** yes, by integrating a bounded Hessian along the segment, even if no Hessian Lipschitz bound is available.

### Sources and reading

- [OpenStax Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), multivariable derivatives and Taylor geometry.
- [MIT 18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), quantitative multivariable calculus context.
- [Wikipedia: Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem), terminology, multivariable and integral remainder formulations.
- [Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), the use of local models in unconstrained minimization.

This is a quantitative extension of the Hessian-and-Taylor segment in `multivariable-calculus:008000`, not a replacement for that introductory calculation.
