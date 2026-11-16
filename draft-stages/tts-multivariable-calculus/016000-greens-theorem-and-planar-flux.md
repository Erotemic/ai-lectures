# 016000 — Green's Theorem: Circulation and Flux from Local Derivatives

**Track:** Multivariable Calculus from First Principles. **Background:** double integrals, line integrals, partial derivatives. **Question:** how does the behavior along the boundary reveal what happens throughout a region?

<!-- BEGIN SPOKEN LECTURE -->

# Green's Theorem: Circulation and Flux from Local Derivatives

Imagine walking around a small closed path in a moving fluid while measuring how strongly the fluid pushes along your direction of travel. The accumulated push around the loop is the circulation. If you divide this circulation by the loop's area and shrink the loop, you obtain a local measure of rotational tendency. Green's theorem says that summing this local rotation over a region gives the circulation around the region's outer boundary.

For a planar vector field with components P and Q, the local scalar curl is the x derivative of Q minus the y derivative of P. Green's theorem states that the counterclockwise boundary line integral of P d x plus Q d y equals the double integral of this scalar curl over the enclosed region, under the usual smoothness and boundary hypotheses.

The theorem is a two-dimensional example of a general pattern: a derivative integrated over the interior becomes the original quantity integrated over the oriented boundary.

## Calculate a spinning field around a circle

Take P equal to negative one half y and Q equal to one half x. The field points counterclockwise around circles, with strength proportional to distance from the origin. Its scalar curl is one: the x derivative of Q is one half, and the y derivative of P is negative one half; subtracting gives one.

For the unit disk, the double integral of the constant one is the disk's area, pi. Green's theorem therefore predicts that the counterclockwise circulation around the unit circle is pi.

Let's check directly. Parametrize the circle by x equals cosine t and y equals sine t, with t from zero to two pi. The differential of x is minus sine t times d t, and that of y is cosine t times d t. Substitute into P d x plus Q d y. The first term becomes one half sine squared t d t; the second becomes one half cosine squared t d t. Their sum is one half d t. A full turn gives pi. Boundary calculation and interior calculation agree.

This explicit calculation clarifies signs. If we traverse the circle clockwise, the boundary integral becomes negative pi. Green's theorem uses the positive orientation, counterclockwise with the interior on the left. Changing orientation changes a signed circulation, not the scalar area of the disk.

## Why interior edges cancel

Divide a rectangular region into many small rectangles. Each little rectangle has its own positively oriented boundary. Add the circulation integrals over all little boundaries. Every interior edge belongs to two adjacent rectangles and is traversed once in each direction. Its two contributions cancel. Only the external boundary remains.

Meanwhile, on one small rectangle, the difference between the circulation on its edges and zero is approximately the local scalar curl times its area. Summing the rectangles gives the interior integral of curl. The cancellation of shared boundaries is the geometric reason the theorem works.

One can make this rigorous by applying the one-variable fundamental theorem of calculus to the rectangular case, then extending to more general piecewise smooth regions. The cancellation mechanism also extends to the surfaces and solids of higher-dimensional Stokes-type theorems.

## Flux is another boundary measurement

Circulation measures the tangential component of a field along a boundary. Flux measures the normal component crossing a boundary. For an outward-pointing normal vector n, the flux is the boundary integral of F dot n with respect to arc length.

There is a companion planar identity: outward flux around the boundary equals the double integral of divergence in the interior. Divergence is the x derivative of the first field component plus the y derivative of the second. Positive divergence measures local net outflow. The formula is a rotated version of Green's theorem, not an unrelated coincidence.

For F equal to x comma y on the unit disk, divergence is two. Its interior integral is twice pi. On the unit circle, the outward unit normal equals the position vector, so F dot n equals one. The boundary length is two pi. Again the two sides agree.

## When does zero curl imply a potential?

If a smooth field is a gradient, its circulation around every closed loop is zero, because the integral is an endpoint difference. Conversely, a continuously differentiable field with zero scalar curl on a simply connected open planar region has a potential under the standard hypotheses. The condition on the region matters.

A field can have zero curl everywhere on a punctured plane and still circulate around the missing point. Its local derivative does not detect a singularity excluded from the domain. Green's theorem cannot be applied to a filled disk where the field is undefined at the center. If we remove a small disk around the hole, the region has two boundary components. The inner boundary must be taken clockwise in the positive boundary orientation of the annulus, and its contribution need not vanish.

This is our first concrete encounter with topology affecting a calculus conclusion. Closed loops can remember holes in a domain, even when the local curl is zero everywhere the field is defined.

Green's theorem makes a large-scale statement from a small-scale derivative. It unifies a local rotational rate with circulation on a whole boundary, and local divergence with outward flux. The corresponding theorems in three dimensions will use the same logic on surfaces and volumes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a positively oriented, piecewise \(C^1\) simple closed curve \(\partial D\) enclosing a suitable planar region \(D\), and \(P,Q\in C^1\) on a neighborhood of \(\overline D\),
\[
\oint_{\partial D}P\,dx+Q\,dy
=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA.
\]
For \((P,Q)=(-y/2,x/2)\), scalar curl is one. On \(D\) the unit disk, both sides equal \(\pi\). The planar divergence formula is
\[
\oint_{\partial D}F\cdot n\,ds=\iint_D(\partial_xF_1+\partial_yF_2)\,dA.
\]
For \(F=(x,y)\) on the unit disk both sides equal \(2\pi\).

**Hole caution:** \(F=(-y/(x^2+y^2),x/(x^2+y^2))\) on \(\mathbb R^2\setminus\{0\}\) has scalar curl zero on its domain, but \(\oint_{|r|=1}F\cdot dr=2\pi\). Green's theorem over the filled disk is inapplicable because the field is undefined at the origin.

### Exercises with answers

1. Find scalar curl of \(F=(-y,x)\). **Answer:** \(\partial_x x-\partial_y(-y)=2\).
2. Find circulation of \(F=(-y,x)\) around the counterclockwise unit circle. **Answer:** \(2\pi\).
3. Find outward flux of \(F=(x,y)\) across the circle of radius two. **Answer:** \(2\cdot\pi(2^2)=8\pi\).
4. Why does an annulus have a clockwise inner boundary in Green's theorem? **Answer:** positive boundary orientation keeps the region on the left during traversal.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Green's theorem and flux.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), circulation and flux.
- [Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem); [Divergence](https://en.wikipedia.org/wiki/Divergence).
