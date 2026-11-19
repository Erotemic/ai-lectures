# Integrating over curves, surfaces, and boundaries

<!-- BEGIN SPOKEN LECTURE -->

# Integrating over curves, surfaces, and boundaries

## Curves and Line Integrals: Measuring Along a Path

A path through the plane may bend, loop, or retrace itself. Its length is not simply the change in its endpoints. If a particle moves in a circle and returns to its starting point, its net displacement is zero, but it has traveled a nonzero distance. Calculus distinguishes these quantities by studying a parametrized curve.

Let a smooth curve be given by a position vector r of t, with t ranging over an interval. Its derivative r prime is the velocity vector. Over a short time interval delta t, the path travels approximately the speed, which is the length of the velocity vector, multiplied by delta t. Add these small distances and let the time intervals shrink. We obtain the arc-length integral: integrate the speed over the parameter interval.

### Arc length around a circle

Take the quarter circle starting at one comma zero and ending at zero comma one. Parametrize it as cosine t comma sine t, with t from zero to pi over two. The velocity is minus sine t comma cosine t. Its length is one. Integrating the constant speed one over that time interval gives arc length pi over two. The result agrees with one quarter of the circumference of a unit circle.

If we make the particle travel the same curve twice as fast, its velocity doubles while its time interval halves. The computed length stays the same. Arc length does not depend on the choice of smooth regular parametrization, as long as the path's traversal and multiplicity are preserved.

### Integrating a scalar along the curve

Now imagine a thin wire lying along that quarter circle, with linear density equal to x plus y. The mass of a small segment is approximately its density times its small length. The total mass is the line integral of x plus y with respect to arc length.

On the quarter circle, the density becomes cosine t plus sine t, and the speed is one. Integrate from zero to pi over two. The integral of cosine is one; the integral of sine is also one. The mass is two in the chosen units.

For a scalar line integral, reversing the traversal direction does not change the result. The arc-length factor is nonnegative. Traversing the entire curve twice, however, doubles the result because we have counted the wire twice. If we mean the geometric set rather than the path with multiplicity, we must parametrize it accordingly.

### Integrating a vector field along the curve

A vector field assigns a vector, such as force, to each point. To calculate the work done along a moving path, take the dot product of force with the infinitesimal displacement. In a parametrization, that becomes the vector field evaluated along the curve dotted with velocity, integrated over time. Unlike scalar arc-length integration, this line integral depends on orientation.

Take a force field F of x comma y equal to y comma x. This field is the gradient of the scalar potential x times y. The work done along any smooth path from one comma zero to zero comma one is the final potential minus the initial potential. Both endpoint products are zero, so the total work is zero. The force may do positive work on one part of a path and negative work on another; only the net difference remains.

This is the fundamental theorem for line integrals. Whenever F is the gradient of a differentiable potential on the region containing the path, integration along the path becomes an endpoint calculation. In particular, the integral around every closed loop is zero.

### A field with nonzero circulation

Now choose F of x comma y equal to minus y comma x. Along the unit circle parametrized counterclockwise, the field equals the velocity vector. Their dot product is one, and integrating over a full turn gives two pi. The field continually pushes in the direction of motion, so its circulation is positive.

Reverse the direction of travel, and the work becomes negative two pi. The geometric circle has not changed, but the oriented path has. This reversal is central to the boundary integrals in Green's and Stokes' theorems.

A subtler example is a field that points around circles but decays like inverse radius. Away from the origin it can have zero local curl yet nonzero circulation around a loop enclosing the missing origin. That example explains why local derivative conditions alone may not guarantee a globally defined potential when the domain has holes.

### What a line integral is really measuring

Scalar integration with respect to arc length accumulates density along a geometric path. Vector-field work integration accumulates the component of the field along oriented motion. Their formulas look similar only because both use a curve parametrization. In one the speed appears as a nonnegative length; in the other the full velocity, including its direction, appears in a dot product.

These two integrals bridge elementary calculus and differential geometry. The work integral is naturally the integral of a differential one-form along a curve. The scalar line integral relies on a metric to measure arc length. Distinguishing them now will make the more abstract language later feel necessary rather than arbitrary.

## Green's Theorem: Circulation and Flux from Local Derivatives

Imagine walking around a small closed path in a moving fluid while measuring how strongly the fluid pushes along your direction of travel. The accumulated push around the loop is the circulation. If you divide this circulation by the loop's area and shrink the loop, you obtain a local measure of rotational tendency. Green's theorem says that summing this local rotation over a region gives the circulation around the region's outer boundary.

For a planar vector field with components P and Q, the local scalar curl is the x derivative of Q minus the y derivative of P. Green's theorem states that the counterclockwise boundary line integral of P d x plus Q d y equals the double integral of this scalar curl over the enclosed region, under the usual smoothness and boundary hypotheses.

The theorem is a two-dimensional example of a general pattern: a derivative integrated over the interior becomes the original quantity integrated over the oriented boundary.

### Calculate a spinning field around a circle

Take P equal to negative one half y and Q equal to one half x. The field points counterclockwise around circles, with strength proportional to distance from the origin. Its scalar curl is one: the x derivative of Q is one half, and the y derivative of P is negative one half; subtracting gives one.

For the unit disk, the double integral of the constant one is the disk's area, pi. Green's theorem therefore predicts that the counterclockwise circulation around the unit circle is pi.

Let's check directly. Parametrize the circle by x equals cosine t and y equals sine t, with t from zero to two pi. The differential of x is minus sine t times d t, and that of y is cosine t times d t. Substitute into P d x plus Q d y. The first term becomes one half sine squared t d t; the second becomes one half cosine squared t d t. Their sum is one half d t. A full turn gives pi. Boundary calculation and interior calculation agree.

This explicit calculation clarifies signs. If we traverse the circle clockwise, the boundary integral becomes negative pi. Green's theorem uses the positive orientation, counterclockwise with the interior on the left. Changing orientation changes a signed circulation, not the scalar area of the disk.

### Why interior edges cancel

Divide a rectangular region into many small rectangles. Each little rectangle has its own positively oriented boundary. Add the circulation integrals over all little boundaries. Every interior edge belongs to two adjacent rectangles and is traversed once in each direction. Its two contributions cancel. Only the external boundary remains.

Meanwhile, on one small rectangle, the difference between the circulation on its edges and zero is approximately the local scalar curl times its area. Summing the rectangles gives the interior integral of curl. The cancellation of shared boundaries is the geometric reason the theorem works.

One can make this rigorous by applying the one-variable fundamental theorem of calculus to the rectangular case, then extending to more general piecewise smooth regions. The cancellation mechanism also extends to the surfaces and solids of higher-dimensional Stokes-type theorems.

### Flux is another boundary measurement

Circulation measures the tangential component of a field along a boundary. Flux measures the normal component crossing a boundary. For an outward-pointing normal vector n, the flux is the boundary integral of F dot n with respect to arc length.

There is a companion planar identity: outward flux around the boundary equals the double integral of divergence in the interior. Divergence is the x derivative of the first field component plus the y derivative of the second. Positive divergence measures local net outflow. The formula is a rotated version of Green's theorem, not an unrelated coincidence.

For F equal to x comma y on the unit disk, divergence is two. Its interior integral is twice pi. On the unit circle, the outward unit normal equals the position vector, so F dot n equals one. The boundary length is two pi. Again the two sides agree.

### When does zero curl imply a potential?

If a smooth field is a gradient, its circulation around every closed loop is zero, because the integral is an endpoint difference. Conversely, a continuously differentiable field with zero scalar curl on a simply connected open planar region has a potential under the standard hypotheses. The condition on the region matters.

A field can have zero curl everywhere on a punctured plane and still circulate around the missing point. Its local derivative does not detect a singularity excluded from the domain. Green's theorem cannot be applied to a filled disk where the field is undefined at the center. If we remove a small disk around the hole, the region has two boundary components. The inner boundary must be taken clockwise in the positive boundary orientation of the annulus, and its contribution need not vanish.

This is our first concrete encounter with topology affecting a calculus conclusion. Closed loops can remember holes in a domain, even when the local curl is zero everywhere the field is defined.

Green's theorem makes a large-scale statement from a small-scale derivative. It unifies a local rotational rate with circulation on a whole boundary, and local divergence with outward flux. The corresponding theorems in three dimensions will use the same logic on surfaces and volumes.

## Surface Integrals: Area, Normal Vectors, and Flux

A curved roof occupies area even when viewed from above as a flat floor plan. If we want enough material to cover it, the projected area is not enough. If we want to calculate how much air crosses it, we also need its orientation. Surface integrals solve both problems by describing the surface through two parameters and measuring how a small patch changes under that parametrization.

A curve uses one parameter. A surface patch uses two. Think of a flexible sheet marked with grid coordinates u and v. Its location in three-dimensional space is a vector-valued map r of u comma v. Hold v fixed and vary u: this traces one family of curves on the surface. Hold u fixed and vary v: this traces another. Their velocity vectors r sub u and r sub v are tangent to the surface.

### From a coordinate patch to an area element

A tiny rectangle in the u-v grid, with side lengths delta u and delta v, becomes approximately a parallelogram in space. Its sides are r sub u times delta u and r sub v times delta v. The parallelogram's area is the length of the cross product of those sides. Thus the surface-area element is the length of r sub u cross r sub v times d u d v.

The cross product itself is perpendicular to the tangent plane. Its magnitude gives area scale, while its direction gives an orientation. Dividing by its magnitude gives a unit normal wherever the parametrization is regular. If we reverse the order of the parameters, the cross product changes sign, so orientation reverses even though area is unchanged.

This is the surface analogue of the Jacobian determinant for ordinary change of variables. A two-dimensional patch in a three-dimensional ambient space has two tangent directions, not a square three-by-three Jacobian. The cross-product magnitude is the correct area scale.

### A graph that curves upward

Consider the surface z equals x squared plus y squared above the unit disk in the x-y plane. Use x and y themselves as parameters. The position map is r of x comma y equals x comma y comma x squared plus y squared. Its x tangent vector is one comma zero comma two x. Its y tangent vector is zero comma one comma two y. Their cross product is minus two x comma minus two y comma one.

Its length is the square root of one plus four x squared plus four y squared. Therefore the curved surface area is the double integral of this square root over the unit disk. Polar coordinates reduce the calculation to a radial integral: two pi times the integral from zero to one of r times square root of one plus four r squared.

Substitute one plus four r squared as a new variable. The resulting area is pi divided by six times five to the three halves minus one. This is greater than pi, the area of the flat unit disk, as it should be: a sloping surface has more area than its horizontal projection.

It is worth checking units and limiting behavior. If the surface were flattened to z equals zero, the tangent cross-product length would be one everywhere, and the surface area would return to pi. The extra square-root factor is exactly the correction for slope.

### Scalar surface integrals

Suppose a thin coating on this curved surface has density sigma in kilograms per square meter of actual surface. Its mass is the integral of sigma times the surface area element. If sigma is constant, we multiply the computed area by that constant. If sigma varies with position, evaluate it at the points of the surface before integrating.

Like a scalar line integral, a scalar surface integral does not depend on the chosen orientation. Density is accumulated with a nonnegative area element. Care is still required to avoid counting overlapping parametrized patches twice.

### Flux needs a direction

Now imagine a constant upward flow F equal to the vector zero comma zero comma one. Its flux through the upward-oriented curved surface is the integral of F dotted with the oriented area vector r sub x cross r sub y. The dot product is one at every point. So the upward flux is simply the area of the unit disk, pi.

This does not contradict the fact that the curved surface has area greater than pi. On a steeper patch, the surface area increases, but the upward flow crosses that patch at a more oblique angle. The cosine factor from the dot product cancels the slope correction. Only the horizontal projected area remains for a uniform vertical field.

Reversing the surface normal reverses the flux. The physical flow has not changed, but we have reversed the direction we call positive. Flux measures signed crossing, not the total amount of fluid touching a surface.

### Closed surfaces and outward normals

For a closed surface such as a sphere, outward orientation is customary. At each regular point, the unit normal points away from the enclosed solid. A field may flow outward through one part and inward through another. The total flux adds these with opposite signs.

If a surface consists of several patches, their orientations must be consistent on overlaps. On an oriented closed surface, the outward normals can be chosen continuously. On a nonorientable surface, a global continuous normal may not exist. This is one reason orientation becomes a structural property rather than just an arrow drawn in a diagram.

### Where this leads

The same surface can carry two kinds of integrals. A scalar surface integral measures density weighted by actual area. A flux integral measures a vector field's normal component weighted by oriented area. Their difference mirrors the earlier distinction between scalar arc-length integrals and oriented work integrals along curves.

We now have enough machinery to see Stokes' theorem as a relation between circulation around a surface boundary and curl through the surface. And we can see the divergence theorem as a relation between outward flux through a closed surface and local net outflow inside the solid. Surface parametrization turns those statements into quantities we can calculate, not merely names to recognize.

## Stokes and Divergence: The Fundamental Theorem in Three Dimensions

One-variable calculus has a remarkable theorem. Add the rate of change of a function over an interval, and the answer depends only on the function values at the endpoints. The derivative's contributions throughout the interior combine into a boundary difference. In several dimensions, two major theorems have the same structure: Stokes' theorem relates curl through a surface to circulation along its edge, and the divergence theorem relates divergence inside a solid to flux through its closed boundary.

These statements are powerful, but they become clearer if we calculate both sides of a complete example.

### Curl and circulation through a disk

Take the three-dimensional vector field F whose components are negative one half y, one half x, and zero. This field rotates around the vertical axis. Its curl is the constant vector zero comma zero comma one. The vertical component can be computed from the x derivative of the second field component minus the y derivative of the first: one half minus negative one half equals one.

Consider the flat unit disk in the horizontal plane, oriented upward. The flux of curl through this disk is the integral of one over the disk, which is pi. Stokes' theorem predicts that the circulation of F around the boundary circle, taken counterclockwise when viewed from above, is also pi.

Parametrize the boundary with x equals cosine t and y equals sine t over a full turn. The field along it is negative one half sine t comma one half cosine t comma zero. The tangent velocity is negative sine t comma cosine t comma zero. Their dot product is one half. Integrate over two pi units of parameter and obtain pi. The two sides agree exactly.

Notice the geometric role of orientation. Upward surface normal corresponds, by the right-hand rule, to counterclockwise boundary orientation as seen from above. Reverse the normal while keeping the physical field fixed, and both sides change sign when the boundary orientation is reversed consistently.

### Why surface shape can change while boundary remains fixed

Imagine replacing the flat disk by a smooth curved cap with the same circular boundary, while keeping the upward-compatible orientation. Stokes' theorem says the integral of curl over the cap is still the boundary circulation, provided the field is smooth on the relevant neighborhood. The cap may have much more area than the flat disk, but the curl flux takes the angle between curl and the normal into account. For our constant vertical curl, the total upward projected area remains pi.

This is a useful check against the mistaken belief that an integral of a vector field over a surface is simply field strength times surface area. The oriented normal matters.

### Divergence and net outflow from a ball

Now take the radial vector field G of x comma y comma z equal to x comma y comma z. Its divergence is three, because the derivative of each component with respect to its corresponding coordinate is one. Inside the unit ball, the total integral of divergence is three times the ball's volume, or three times four pi over three. The result is four pi.

On the unit sphere, the outward unit normal equals the position vector. Our field G equals that same vector, so its dot product with the unit normal is one everywhere on the sphere. Integrating one over the sphere gives surface area four pi. Again the interior calculation and boundary calculation agree.

This is the divergence theorem: the total local rate of outflow inside a solid equals the net outward flux through its enclosing surface. It is an exact mathematical identity for sufficiently regular regions and fields, not an approximation based on physical intuition.

### The cancellation mechanism

Why should either theorem be true? Divide a surface into many smaller surface patches. Their boundary curves contain many shared internal edges. A shared edge appears twice, with opposite orientation, so its two line integrals cancel. Only the outer boundary survives. At the local level, curl measures circulation per oriented area. Summing over all the patches gives the flux of curl through the surface, while the boundary sum collapses to the circulation around the outside.

For the divergence theorem, divide a solid into many small volumes. Each internal face is outward-facing for one tiny volume and inward-facing for its neighbor, so its flux contributions cancel. Only faces on the external boundary remain. Locally, divergence measures net outward flux per volume. Sum those local rates, and the net flux through the outer boundary appears.

These cancellation arguments are the higher-dimensional relatives of the fundamental theorem of calculus on an interval. The interior pieces disappear in pairs because shared boundaries inherit opposite orientations.

### Conservation laws and what theorems do not claim

Suppose G represents fluid velocity and the fluid is incompressible, so divergence is zero in a region. The divergence theorem says the net outward flux through any suitable closed surface in that region is zero. It does not say the velocity is zero on the surface. Fluid may enter one side and leave the other in equal amounts.

Similarly, zero curl need not mean a vector field vanishes. It says the local circulation density vanishes. In a simply connected region this condition helps characterize gradient fields, but domains with holes need special care. Local derivative data and global topology are connected, not interchangeable.

In physical applications there may be sources, singularities, or discontinuities. The classical theorems require appropriate smoothness of the field and regularity of the domain. Distributional and weak versions extend them to rougher settings, and additional terms may appear when singularities are present. It is better to state the conditions than to apply a beautiful formula outside its domain of validity.

### The unifying formula

The later language of differential forms expresses these results in one compact pattern: integrate the exterior derivative of a form over an oriented region, and obtain the integral of the original form over its oriented boundary. In one dimension this is the fundamental theorem of calculus. On a planar region it becomes Green's theorem. On an oriented surface in three dimensions it becomes Stokes' theorem. On a solid it gives the divergence theorem after the appropriate identification of forms with vector fields and volume elements.

You do not need differential forms to verify the examples we just computed. But after seeing the same boundary-cancellation mechanism three times, the abstract formulation is no longer an arbitrary generalization. It is a way of preserving the common idea while removing dependence on the coordinates chosen for each special case.

The core lesson is simple but deep: derivatives describe local change, while integrals accumulate change. Under the right hypotheses, accumulation over an interior can be measured entirely at the boundary. That principle connects elementary calculus to geometry, topology, physics and partial differential equations.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Curves and Line Integrals: Measuring Along a Path

**Track:** Multivariable Calculus from First Principles. **Background:** derivatives of curves and one-variable integration. **Question:** how can a scalar field or vector field be integrated along a moving path?

#### Mathematical companion (not spoken)

For a piecewise \(C^1\) curve \(r:[a,b]\to\mathbb R^n\),
\[
L(r)=\int_a^b\|r'(t)\|\,dt,\qquad
\int_r f\,ds=\int_a^bf(r(t))\|r'(t)\|\,dt,
\]
while work or circulation is
\[
\int_r F\cdot dr=\int_a^bF(r(t))\cdot r'(t)\,dt.
\]
For \(r(t)=(\cos t,\sin t)\), \(0\le t\le\pi/2\), the length is \(\pi/2\) and \(\int_r(x+y)\,ds=2\). For \(F=\nabla(xy)=(y,x)\), \(\int_rF\cdot dr=xy\big|_{\mathrm{end}}-xy\big|_{\mathrm{start}}=0\). For \(F=(-y,x)\) and the full positively oriented unit circle, circulation is \(2\pi\).

##### Exercises with answers

1. Find the length of \(r(t)=(3t,4t)\), \(0\le t\le2\). **Answer:** \(\int_0^2 5\,dt=10\).
2. Integrate density \(f=2\) along a segment of length three. **Answer:** six.
3. Compute work for \(F=(2x,2y)\) along any curve from \((0,0)\) to \((1,1)\). **Answer:** two, the change in potential \(x^2+y^2\).
4. What happens to \(\int_rF\cdot dr\) when orientation reverses? **Answer:** it changes sign.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), parametrized curves and line integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), line integrals.
- [Line integral](https://en.wikipedia.org/wiki/Line_integral); [Conservative vector field](https://en.wikipedia.org/wiki/Conservative_vector_field).

### Green's Theorem: Circulation and Flux from Local Derivatives

**Track:** Multivariable Calculus from First Principles. **Background:** double integrals, line integrals, partial derivatives. **Question:** how does the behavior along the boundary reveal what happens throughout a region?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Find scalar curl of \(F=(-y,x)\). **Answer:** \(\partial_x x-\partial_y(-y)=2\).
2. Find circulation of \(F=(-y,x)\) around the counterclockwise unit circle. **Answer:** \(2\pi\).
3. Find outward flux of \(F=(x,y)\) across the circle of radius two. **Answer:** \(2\cdot\pi(2^2)=8\pi\).
4. Why does an annulus have a clockwise inner boundary in Green's theorem? **Answer:** positive boundary orientation keeps the region on the left during traversal.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Green's theorem and flux.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), circulation and flux.
- [Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem); [Divergence](https://en.wikipedia.org/wiki/Divergence).

### Surface Integrals: Area, Normal Vectors, and Flux

**Track:** Multivariable Calculus from First Principles. **Background:** cross products, double integrals, Jacobians. **Question:** how can we measure a curved surface and the field passing through it?

#### Mathematical companion (not spoken)

For a regular parametrization \(r:U\subset\mathbb R^2\to\mathbb R^3\),
\[
dS=\|r_u\times r_v\|\,du\,dv,\qquad
\int_S\sigma\,dS=\iint_U\sigma(r(u,v))\|r_u\times r_v\|\,du\,dv,
\]
and oriented flux is
\[
\int_SF\cdot n\,dS=\iint_UF(r(u,v))\cdot(r_u\times r_v)\,du\,dv.
\]
For the graph \(r(x,y)=(x,y,x^2+y^2)\),
\[
r_x\times r_y=(-2x,-2y,1),\quad
\operatorname{Area}(S)=2\pi\int_0^1 r\sqrt{1+4r^2}\,dr=\frac{\pi}{6}(5^{3/2}-1).
\]
The upward flux of \(F=(0,0,1)\) is \(\int_D1\,dx\,dy=\pi\).

##### Exercises with answers

1. Find the area factor for the plane \(r(u,v)=(u,v,2u)\). **Answer:** \(\|r_u\times r_v\|=\sqrt5\).
2. Find the upward flux of \(F=(0,0,3)\) through \(z=x^2+y^2\) over the unit disk. **Answer:** \(3\pi\).
3. Does reversing a surface orientation change \(\int_S\sigma\,dS\)? **Answer:** no; scalar area is nonnegative.
4. Does reversing orientation change vector-field flux? **Answer:** yes, it reverses the sign.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), surface integrals.
- OpenStax, [Calculus Volume 3](https://openstax.org/books/calculus-volume-3/pages/preface), surface area and flux.
- [Surface integral](https://en.wikipedia.org/wiki/Surface_integral); [Normal (geometry)](https://en.wikipedia.org/wiki/Normal_(geometry)).

### Stokes and Divergence: The Fundamental Theorem in Three Dimensions

**Track:** Multivariable Calculus from First Principles. **Background:** line integrals, surface flux, divergence and curl. **Question:** why do derivatives inside a region control integrals along its boundary?

#### Mathematical companion (not spoken)

For \(F\in C^1\) on a neighborhood of an oriented smooth surface \(S\) with piecewise smooth boundary, with compatible right-hand-rule boundary orientation,
\[
\oint_{\partial S}F\cdot dr=\iint_S(\nabla\times F)\cdot n\,dS.
\]
For \(F=(-y/2,x/2,0)\), \(\nabla\times F=(0,0,1)\); on the upward unit disk, both sides equal \(\pi\).

For \(G\in C^1\) on a neighborhood of a suitable bounded solid \(V\) with outward-oriented piecewise smooth boundary,
\[
\iiint_V\nabla\cdot G\,dV=\iint_{\partial V}G\cdot n\,dS.
\]
For \(G=(x,y,z)\) and the unit ball, \(\nabla\cdot G=3\), so \(3(4\pi/3)=4\pi\), while \(G\cdot n=1\) on the unit sphere with area \(4\pi\).

The generalized Stokes theorem, \(\int_M d\omega=\int_{\partial M}\omega\), requires consistent orientations and hypotheses ensuring both integrals are defined; the classical theorems are special coordinate incarnations.

##### Exercises with answers

1. Compute \(\nabla\times(-y,x,0)\). **Answer:** \((0,0,2)\).
2. Find flux of \(G=(x,y,z)\) through the outward sphere of radius \(R\). **Answer:** \(3(4\pi R^3/3)=4\pi R^3\).
3. Does \(\nabla\cdot G=0\) force \(G=0\)? **Answer:** no, e.g. a constant nonzero vector field has divergence zero.
4. What determines boundary orientation for Stokes? **Answer:** the chosen oriented surface normal via the right-hand rule.

##### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Stokes and divergence theorems.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), forms and generalized Stokes.
- [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem); [Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem).
