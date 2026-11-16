# 003000 — Partial and Directional Derivatives: The Information They Miss

**Track:** Multivariable Calculus from First Principles. **Background:** one-variable derivatives and multivariable limits. **Question:** when do slopes measured along lines describe a true local linear map?

<!-- BEGIN SPOKEN LECTURE -->

# Partial and Directional Derivatives: The Information They Miss

A function of two variables can change when we move east, when we move north, or when we move diagonally. We might begin by measuring the eastward slope and the northward slope separately. Those are partial derivatives. They are often easy to compute, but the important question is whether they tell the whole story.

For a function f of x and y, the partial derivative with respect to x fixes y and takes an ordinary one-variable derivative. The partial derivative with respect to y fixes x instead. On the surface whose height is x squared plus three times y squared, the x partial derivative is two x and the y partial derivative is six y. At one comma one, a small step to the right changes the height at a rate of two per unit distance; a step upward in the y direction changes it at rate six.

A directional derivative asks about a prescribed vector v, not just a coordinate axis. We look at f of a plus t times v, subtract f of a, and divide by t as t approaches zero. The vector v describes the displacement for one unit of t. If v is twice as long, the rate is twice as large when the derivative behaves linearly. Unit vectors are used when comparing rates per unit distance.

## What the familiar formula predicts

For a smooth surface, the directional derivative in direction v equals the x partial derivative times the x component of v, plus the y partial derivative times the y component. In the quadratic example, at one comma one the directional rate along the vector three comma four is two times three plus six times four, which is thirty. Along the unit direction three fifths comma four fifths, the rate per unit distance is six.

This formula is extremely useful. But its hypothesis matters. It follows from the existence of a full linear derivative; it does not follow merely from the separate existence of the two partial derivatives at a point.

## A function with every directional derivative but no linear derivative

Define a function away from the origin by x cubed divided by x squared plus y squared, and define its value at the origin as zero. It is continuous at zero: the absolute value is no greater than the distance to zero. Its partial derivative along the x axis at zero is one; along the y axis it is zero.

What about the diagonal direction one comma one? At the point t comma t the function equals t divided by two. Divide by t and the directional derivative is one half. Yet the formula predicted by the two partial derivatives would give one times one plus zero times one, or one. The measured rate is one half, not one.

In fact, every directional derivative exists at the origin for this function, but the dependence on direction is not linear. This is the obstruction. A total derivative must be a single linear map that simultaneously predicts the change for every small displacement. Direction-by-direction limits can fail to assemble into that map.

There is a second caution. Suppose a function has partial derivatives at the origin. It need not even be continuous there. Consider the fraction x squared times y divided by x to the fourth plus y squared, with value zero at the origin. Both coordinate-axis partial derivatives at the origin are zero. Yet along y equals x squared, the function is one half rather than something tending to zero. A measurement along each axis has missed a discontinuity between them.

## A sufficient condition that repairs the gap

Here is a theorem worth remembering. If all the first partial derivatives exist on an open neighborhood of the point and are continuous at the point, then the function is differentiable there. In particular, if the partial derivatives are continuous throughout a neighborhood, they produce a full linear approximation at each point of that neighborhood. The key is not simply the existence of slopes, but their controlled behavior as the base point moves.

Why is continuity of partial derivatives helpful? Move from x comma y to x plus h comma y plus k in two stages: first change x, then change y. Apply the one-variable mean value theorem to each stage. The coefficients are partial derivatives at nearby points. As h and k shrink, continuity makes those coefficients approach the partial derivatives at the original point. The error is small compared with the total displacement.

That proof strategy already explains why the theorem is stronger than the bare existence of partial derivatives at one isolated point. To control an error after moving, we need information at nearby points.

## A practical diagnostic

When given a formula that is smooth wherever its denominator is nonzero, ordinary differentiation rules are enough away from singularities. At a suspect point, however, distinguish four questions. Does the function have a limit? Is it continuous? Do the coordinate partial derivatives exist? Is it fully differentiable? These questions are related, but none of the weaker facts should be silently promoted into a stronger one.

Directional derivatives are valuable physical measurements, and partial derivatives are the coordinate entries of the true derivative when it exists. Their limitations lead us to the central object of multivariable calculus: a linear approximation controlled by the total size of the displacement, not just by selected directions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(v\in\mathbb R^n\), the two-sided directional derivative, when it exists, is
\[
D_vf(a)=\lim_{t\to0}\frac{f(a+tv)-f(a)}{t}.
\]
If \(f\) is differentiable at \(a\), then \(D_vf(a)=Df(a)v=\sum_i\partial_i f(a)v_i\). The converse fails. Define
\[
f(x,y)=\begin{cases}x^3/(x^2+y^2), &(x,y)\ne(0,0),\\0,&(x,y)=(0,0).
\end{cases}
\]
Then \(D_{(a,b)}f(0)=a^3/(a^2+b^2)\) for \((a,b)\ne0\), which is not linear in \((a,b)\). Along \((1,1)\) it equals \(1/2\), whereas the linear map predicted from partials \((1,0)\) would equal one. The function is continuous because \(|f(x,y)|\le |x|\le\sqrt{x^2+y^2}\).

**Sufficient criterion:** first-order partial derivatives existing in a neighborhood of \(a\) and continuous at \(a\) imply differentiability at \(a\). For vector-valued functions apply componentwise.

### Exercises with answers

1. Compute \(\partial_x,\partial_y\) of \(x^2+3y^2\) at \((1,1)\). **Answer:** \((2,6)\).
2. Find the directional rate along \((3/5,4/5)\). **Answer:** \(2(3/5)+6(4/5)=6\).
3. For the counterexample above, compute \(D_{(0,1)}f(0)\). **Answer:** zero.
4. Can a discontinuous function be differentiable? **Answer:** not at that point; differentiability implies continuity.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), partial and directional derivatives.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), differentiability.
- [Partial derivative](https://en.wikipedia.org/wiki/Partial_derivative); [Directional derivative](https://en.wikipedia.org/wiki/Directional_derivative).
