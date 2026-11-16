# 009000 — Maxima, Minima, and Saddle Points in Several Variables

**Track:** Multivariable Calculus from First Principles. **Background:** gradients, Hessians, compactness. **Question:** where can a multivariable function attain its largest or smallest value?

<!-- BEGIN SPOKEN LECTURE -->

# Maxima, Minima, and Saddle Points in Several Variables

A function of one variable may have a local maximum at a point where its derivative is zero. In several variables, we might begin with the same idea: at an interior local maximum or minimum of a differentiable function, the gradient must vanish. But solving the gradient equations is only the beginning. A critical point could be a minimum, a maximum, a saddle, or something more complicated. And the largest value on a restricted region may occur on its boundary, where the unconstrained gradient need not vanish.

Let's see how to organize these possibilities without losing candidates.

## An interior minimum by completing the square

Consider f of x and y equal to x squared plus twice y squared minus twice x minus four y. Its x partial derivative is two x minus two, and its y partial derivative is four y minus four. Both vanish at one comma one. The Hessian is diagonal with entries two and four, so it is positive definite. The second-derivative test therefore identifies a strict local minimum.

But we can say more. Complete the squares. The function equals x minus one squared, plus twice y minus one squared, minus three. Every squared term is nonnegative, so the function is at least negative three everywhere, with equality only at one comma one. This proves a global minimum, not just a local one. It also shows the value of having more than one proof method: the Hessian classifies local shape, while the algebraic identity gives a global bound.

The absence of a global maximum is equally clear. Let x grow without bound while y stays one. The function goes to infinity.

## Why zero gradient is not enough

At the origin, the function x squared minus y squared has gradient zero. Along the x axis it is positive away from the origin; along the y axis it is negative. No neighborhood of the origin consists entirely of values above or entirely below the value at the origin. This is a saddle point.

The Hessian has a positive and a negative eigenvalue. The second-derivative test detects the saddle. A positive definite Hessian at a critical point implies a strict local minimum; a negative definite Hessian implies a strict local maximum; an indefinite Hessian implies a saddle. If the Hessian has zero eigenvalues, the test may be inconclusive.

Consider x to the fourth plus y to the fourth. The Hessian at zero is the zero matrix, but the function has a strict global minimum there. The geometry first becomes visible at fourth order. Derivative tests are tools, not substitutes for examining the function.

## Boundary candidates are different

Now maximize x plus y on the closed unit disk. The gradient is the nonzero constant vector one comma one. It never vanishes anywhere, so there are no interior critical points. Does this mean the function has no maximum? No. The disk is closed and bounded, hence compact, and the function is continuous, so a maximum and minimum must exist.

We need to check the boundary circle. Write x equals cosine t, y equals sine t. Along the circle the function is cosine t plus sine t. This reaches its maximum square root of two at the point one over square root of two comma one over square root of two, and its minimum negative square root of two at the opposite point. The extrema occur on the boundary, although the full gradient is not zero there.

The Cauchy–Schwarz inequality provides another solution. The dot product of one comma one with a point in the unit disk is at most square root of two times the length of that point, hence at most square root of two. Equality requires the point to be the outward unit vector in the gradient direction. Both proofs emphasize that the domain matters.

## A systematic procedure for closed regions

Suppose we seek absolute extrema of a continuous function on a compact region in the plane. First find interior critical points, where all partial derivatives vanish or, for a less regular function, where differentiability fails. Then analyze the boundary separately. If the boundary is a smooth curve, parametrize it and optimize the resulting one-variable function. If the boundary has corners or several pieces, examine each piece and its endpoints. Finally compare actual function values at all the candidates.

This method handles a rectangle, triangle, disk, or other manageable region. It is tempting to solve only the gradient equations and announce an answer, but that can miss the true extrema entirely.

For noncompact regions, continuity alone does not guarantee that absolute extrema exist. Even a bounded function can approach a supremum without attaining it. On the whole real line, arctangent x approaches one half pi but never reaches it. In several variables the same escape to infinity is possible.

## Beyond calculus exercises

The calculus of extrema leads directly to optimization, equilibrium mechanics, and variational problems. A system at an interior stable equilibrium often has vanishing first variation and positive second variation, at least after relevant constraints are accounted for. A saddle can be an equilibrium without being stable. On a boundary or a constraint surface, the gradient need only vanish along allowed directions.

That final observation leads to constrained optimization. First learn to identify all the places where extrema may occur. Then ask which directions are actually permitted by the problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Fermat necessary condition.** If \(f\) is differentiable at an interior local extremum \(a\), then \(Df(a)=0\), equivalently \(\nabla f(a)=0\). If \(H_f(a)\) is positive definite, \(a\) is a strict local minimum; negative definite gives strict local maximum; indefinite gives a saddle. Semidefinite Hessians require further analysis.

For \(f(x,y)=x^2+2y^2-2x-4y\),
\[
f=(x-1)^2+2(y-1)^2-3,\quad \nabla f=(2x-2,4y-4),\quad H=\begin{pmatrix}2&0\\0&4\end{pmatrix}.
\]
On \(D=\{x^2+y^2\le1\}\), \(g=x+y\) attains \(\max_D g=\sqrt2\) and \(\min_D g=-\sqrt2\), both on the boundary. Compactness is used to guarantee existence of global extrema, not to identify them.

### Exercises with answers

1. Classify \((0,0)\) for \(f=x^2+y^2\). **Answer:** strict global minimum.
2. Find the minimum of \((x-2)^2+3(y+1)^2+4\). **Answer:** value four at \((2,-1)\).
3. Maximize \(x\) on the unit disk. **Answer:** maximum one at \((1,0)\).
4. Why is the origin for \(x^4+y^4\) a minimum despite the inconclusive Hessian? **Answer:** both fourth powers are nonnegative and vanish simultaneously only at the origin.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), maxima and minima.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), extrema of several-variable functions.
- [Critical point (mathematics)](https://en.wikipedia.org/wiki/Critical_point_(mathematics)); [Extreme value theorem](https://en.wikipedia.org/wiki/Extreme_value_theorem).
