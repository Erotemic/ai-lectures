# Vector Fields and Oriented Boundaries: From Tangents to Conservation

<!-- BEGIN SPOKEN LECTURE -->

# Vector Fields and Oriented Boundaries: From Tangents to Conservation

Imagine a small boat moving through a river. The river's velocity field assigns a direction and speed to each point. If the boat travels along a prescribed path, the current may push with the boat in some places and against it in others. If instead you stretch a floating net across the river, the quantity of water passing through the net depends on the component of velocity pointing across it.

Both are integrals of a vector field, but they measure different things. One uses the direction tangent to a path; the other uses a normal direction. Much of vector calculus becomes clearer once that distinction is secure.

## Three kinds of integrals that look similar

First, suppose a curve is traced by a moving point. To integrate a scalar quantity along it, such as mass per unit length, we multiply the scalar by a short arc length and add. Reversing the direction of travel does not change the total scalar mass of the curve.

Second, suppose a force field acts on a particle traveling along that curve. The small amount of work is the force dotted with the tiny displacement. Summing these pieces gives the line integral of the vector field dotted with the directed displacement. Reverse the path and the work changes sign, because each directed displacement is reversed.

Third, suppose we want flow across a line in a two-dimensional fluid, or across a surface in three-dimensional space. At each point we use the field's component normal to the barrier, not its component tangent to the barrier. Reverse the chosen normal and the flux changes sign. The geometric surface is the same; the orientation of the measurement changed.

These distinctions already tell us how to sanity-check a formula. A scalar integral cannot become negative solely because we reverse the path. A circulation integral usually does change sign under reversal. And an outward flux is not the same as inward flux.

## Compute circulation on all four sides

Take the vector field whose horizontal component is minus y and whose vertical component is x. It looks like a rotational flow around the origin. Let our curve be the boundary of the unit square, traced counterclockwise, starting at the bottom-left corner.

On the bottom edge, y is zero and we move horizontally. The field points vertically there, so it does no work along that edge. The contribution is zero.

On the right edge, x is one and we move upward. The vertical component of the field is one, so the line integral along this edge is one.

On the top edge, y is one and we move left. The horizontal component of the field is minus one. The field and our movement are both leftward, so the contribution is another one. Notice how easy it would be to miss that sign if we described the edge as x from zero to one rather than x from one to zero.

On the left edge, x is zero and we move down. The field there is horizontal, perpendicular to our movement, so that edge contributes zero.

Add the four sides: two. This is the counterclockwise circulation of our field around the unit square.

Now inspect the field locally. The derivative of its vertical component with respect to x is one. The derivative of its horizontal component with respect to y is minus one. Subtracting gives two. Green's theorem says that the circulation around the counterclockwise boundary is the integral of this difference across the interior. Since the square has area one, the area integral is also two.

One computation added contributions on the edge. The other added a local measure of rotation throughout the interior. Green's theorem tells us those measurements agree under its smoothness and domain assumptions.

## Why internal boundaries disappear

Why should a boundary integral know anything about an entire region? Think of dividing the square into many tiny squares. Apply the little circulation formula to each one. Every interior grid edge is traced once in each direction by neighboring squares. Those two contributions cancel. The only edges left uncancelled are the ones on the outside of the large square.

The curl term measures the infinitesimal tendency to circulate. Adding local circulation over all cells recovers the circulation around the exterior because internal contributions are counted with opposite orientations. This is the geometric mechanism behind Green's theorem and its three-dimensional relatives.

It also explains why holes require attention. Suppose we remove a small disk from the middle of a larger disk. The inner circular boundary is part of the boundary of the remaining region, and its positive orientation is clockwise: as you walk the boundary in that direction, the remaining region stays on your left. Ignoring that inner circle discards a term needed for cancellation.

For example, away from the origin consider the rotational field with components minus y divided by squared distance from the origin, and x divided by squared distance. Its curl is zero wherever it is defined. Yet a counterclockwise circle around the origin has circulation two pi. There is no contradiction: the field is not defined at the origin, so Green's theorem does not apply to the filled-in disk. On an annulus, the outer circle contributes two pi and the inner, clockwise circle contributes minus two pi. Their sum is zero, matching the curl integral over the annulus.

## Flux measures crossing, not spinning

Now take the field with components x and y on the same unit square. This field points away from the origin, and its divergence is two: one from the rate at which its horizontal component changes with x, and one from its vertical component changing with y.

Compute outward flux through the square. At the right edge the outward normal points right; the field's horizontal component is one, so the flux across that edge is one. At the top edge the normal points up and the vertical component is one, so that contribution is one. On the left and bottom edges the corresponding normal component of the field is zero. Total outward flux is two.

The area integral of divergence is also two, since divergence equals two throughout a square of area one. This is the planar flux form of Green's theorem. It has the same cancellation story: what leaves one small cell enters its neighbor, so internal face fluxes cancel and only exterior flux survives.

Circulation and flux are not interchangeable. The rotating field we used first has zero divergence but nonzero curl. The expanding field we used second has positive divergence but zero curl. A flow can swirl without being a local source, or expand without swirling.

## Surface orientation in three dimensions

In three dimensions, a surface may be parameterized by two coordinates. If a patch is described by a vector position depending on parameters u and v, its two parameter derivatives are tangent vectors. Their cross product is perpendicular to the surface. Its length gives local area scaling, and its direction records an orientation.

Switch the order of the parameters, and the cross product reverses direction. The physical patch does not change, but the chosen orientation does. This is why the order of the cross product matters for flux.

Consider a unit sphere centered at the origin and the field whose vector at each point is the position vector itself. The outward unit normal is the radial direction. On the sphere the field also points radially outward with magnitude one. Their dot product is one everywhere. Thus the outward flux equals the surface area, four pi.

The divergence of this field is three, because each coordinate component has derivative one in its own direction. The enclosed ball has volume four pi over three. Multiply volume by divergence: again four pi. That is the divergence theorem verified directly for this sphere.

For a sphere of radius R, the same reasoning gives outward flux four pi times R cubed. The field has magnitude R on the surface and the surface has area four pi R squared. The volume calculation gives three times four pi R cubed over three. Both routes agree.

## Stokes' theorem: tangential motion around a surface

The divergence theorem relates outward flux through a closed surface to divergence inside a volume. Stokes' theorem instead relates circulation around the boundary of an oriented surface to the component of curl passing through the surface.

Take the vector field whose horizontal component is minus one half of y and vertical component is one half of x, with zero vertical component. Its curl points upward with magnitude one. Choose the upper hemisphere of the unit sphere and orient it with the upward-pointing normal. Its boundary is the equator, traced counterclockwise when viewed from above.

Around that equator, the field moves tangent to the circle with constant magnitude one half. The circumference is two pi, so circulation is pi. Through the hemisphere, the upward curl contributes the area of the hemisphere's projection onto the horizontal disk, which is pi. The two values agree.

It is essential that we orient the boundary consistently with the normal. Reverse the surface normal, and the induced boundary direction reverses too. Neither side is intrinsically positive without a choice of orientation.

## Gradients and path independence

There is another simple way to compute some line integrals. If a vector field is the gradient of a scalar potential, its work along a path is just the potential at the endpoint minus its value at the starting point. This is the fundamental theorem for line integrals.

Take the scalar potential x squared plus y squared. Its gradient has components two x and two y. Travel along any smooth path from the origin to the point one, one. The work is the final potential, two, minus the initial potential, zero. It is two regardless of the route.

By contrast, the rotating field from our square example is not the gradient of a single-valued potential throughout the plane: its circulation around a closed loop was two, whereas a genuine gradient would have zero circulation on every closed loop in its domain. On regions with holes, even a zero-curl field need not be a global gradient, as the annulus example showed.

## A usable sign-checking routine

When solving a vector-calculus problem, begin by naming the measurement: scalar accumulation, tangential work, or normal flux. Then specify how the curve or surface is oriented. For a parameterization, calculate the tangent or cross product in the correct order. Only after that choose whether direct integration or a theorem is simpler.

If you use Green, Stokes, or divergence, check the hypotheses: the field must have the needed smoothness on the relevant region, the domain must include any inner boundary, and the curve or surface must be oriented consistently. Those requirements are not decorative. They are what make the cancellation of internal boundaries legitimate.

The common idea is remarkably simple. A derivative describes a local change. A boundary integral records what accumulates around or through an edge. Adding the local changes across a region makes internal contributions cancel, leaving the net effect at the outside. That is why the fundamental theorem of calculus keeps reappearing in new dimensions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Scalar, tangential and normal integrals

For \(\gamma:[a,b]\to\mathbb R^n\) piecewise \(C^1\),
\[
\int_C f\,ds=\int_a^b f(\gamma(t))\|\gamma'(t)\|dt,
\qquad
\int_C F\cdot d\mathbf r=\int_a^bF(\gamma(t))\cdot\gamma'(t)dt.
\]
The first is independent of direction, the second changes sign under reversal. For a positively oriented planar curve \(\gamma=(x(t),y(t))\), the right-hand normal displacement is \((y',-x')dt\); this is outward for a counterclockwise boundary.

### Green's theorem checked edge by edge

For \(F=(P,Q)=(-y,x)\) on \([0,1]^2\) with counterclockwise boundary,
\[
\oint_{\partial D}P\,dx+Q\,dy=0+1+1+0=2,
\quad
\iint_D(Q_x-P_y)dA=\iint_D(1-(-1))dA=2.
\]
For \(G=(x,y)\), \(\nabla\cdot G=2\), and outward flux through the right/top edges is \(1+1=2\).

### Annular warning: smoothness and inner boundaries

For \(F=(-y/(x^2+y^2),x/(x^2+y^2))\), \(\operatorname{curl}F=0\) on \(\mathbb R^2\setminus\{0\}\). On a counterclockwise circle of radius \(r\),
\[
\oint F\cdot d\mathbf r=\int_0^{2\pi}1\,d\theta=2\pi.
\]
An annulus has a clockwise inner boundary, whose contribution is \(-2\pi\); the total is zero. Applying Green's theorem to a full disk containing the singular origin is invalid.

### Divergence on a ball and Stokes on a hemisphere

For \(F=(x,y,z)\) and \(B_R=\{\|x\|\le R\}\),
\[
\nabla\cdot F=3,\quad \iiint_{B_R}3\,dV=4\pi R^3
=\iint_{\partial B_R}F\cdot n\,dS.
\]
For \(A=(-y/2,x/2,0)\), \(\nabla\times A=(0,0,1)\). Let \(S\) be the upper unit hemisphere, oriented upward/outward. Its induced boundary orientation is counterclockwise viewed from above. Then
\[
\oint_{\partial S}A\cdot d\mathbf r=\pi
=\iint_S (\nabla\times A)\cdot n\,dS.
\]

### Exercises with answers

1. **Reorient the square.** Traverse the square clockwise with \(F=(-y,x)\). **Answer:** the circulation is \(-2\), because tangent displacement changes sign.
2. **Scalar line integral.** Integrate \(x^2+y^2\) with respect to arc length around the circle of radius two. **Answer:** the scalar is four and the circumference is four pi, so the integral is \(16\pi\), independent of traversal direction.
3. **A conservative field.** Integrate \((2x,2y)\) along any path from \((0,0)\) to \((1,1)\). **Answer:** \((x^2+y^2)|_{(1,1)}-(x^2+y^2)|_{(0,0)}=2\).
4. **Sphere orientation.** Reverse the normal for the sphere with \(F=(x,y,z)\). **Answer:** flux becomes \(-4\pi R^3\); the usual divergence theorem uses outward normals.
5. **A hole matters.** Why does the rotational singular field have a nonzero loop integral despite zero curl off the origin? **Answer:** the loop surrounds a point outside the field's domain; on an annulus its clockwise inner-boundary term cancels the outer one.

### Sources and further reading

- [OpenStax, *Calculus Volume 3*, §6.2, Line Integrals](https://openstax.org/books/calculus-volume-3/pages/6-2-line-integrals), tangential and normal line integrals.
- [OpenStax, *Calculus Volume 3*, §6.6, Surface Integrals](https://openstax.org/books/calculus-volume-3/pages/6-6-surface-integrals), orientation and parameterized flux.
- [OpenStax, *Calculus Volume 3*, §6.8, The Divergence Theorem](https://openstax.org/books/calculus-volume-3/pages/6-8-the-divergence-theorem), flux conservation and boundary integration.
- [Wikipedia: Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem), oriented boundary and region hypotheses.
- [Wikipedia: Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem), boundary orientation and surface curl.
- Existing survey: `multivariable-calculus:015000` gives the larger conceptual overview; this lecture expands the edge calculations and sign checks.
