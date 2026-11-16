# 009100 - Differential Forms: Circulation, Flux, and Curl

**Track:** Topology and Geometry. **Background:** multivariable calculus, oriented curves and surfaces, elementary differential forms. **Question:** how are line integrals, flux integrals, curl and divergence related?

<!-- BEGIN SPOKEN LECTURE -->

# Differential Forms: Circulation, Flux, and Curl

Imagine a small paddle wheel in a flowing stream. Whether it turns depends on how the water moves around it. Now imagine a closed curve in the stream and ask how strongly the current pushes along the curve as you travel around it. These are two views of the same circulation phenomenon, one local and one integrated. Differential forms make the relationship precise and reveal that several familiar vector-calculus theorems have the same underlying shape.

We will work first in the plane, with coordinates x and y and the usual counterclockwise orientation. Suppose the flow has horizontal component P and vertical component Q. The associated one-form is P d x plus Q d y. When a particle traces a parametrized path, we evaluate this form on its velocity. The result is P times the horizontal velocity plus Q times the vertical velocity: the rate at which the field works along the path.

## Computing a circulation integral

Take the field whose horizontal component is negative y and whose vertical component is x. Its arrows circulate around the origin. On the unit circle parametrized counterclockwise by cosine t and sine t, the velocity is negative sine t in the x direction and cosine t in the y direction. The field evaluated at that point is exactly the same vector. Their dot product is one. Integrating from zero to two pi gives circulation two pi.

We can also measure local circulation. Differentiate the one-form negative y d x plus x d y. The exterior derivative is two times d x wedge d y. Thus the exterior derivative says that every unit of oriented area carries local circulation density two. The unit disk has area pi, so integrating the two-form over the disk gives two pi. The boundary integral and the area integral agree.

This is Green's theorem in differential-form language. In conventional coordinates it says the counterclockwise line integral of P d x plus Q d y equals the double integral of the x derivative of Q minus the y derivative of P. The expression in the integrand is the scalar curl in two dimensions. The derivative of the one-form automatically produces it with the correct orientation.

## Why orientation changes the sign

Walking the same curve in the opposite direction changes every tangent velocity to its negative, so the line integral changes sign. Reversing orientation on the region changes its area form sign as well. Boundary and interior must be oriented compatibly for Green's theorem. The usual convention on a planar region is that a counterclockwise boundary walk keeps the region on your left.

The sign is not bookkeeping to be repaired after the calculation. An oriented integral measures something with a direction. If you want an unsigned total amount, that is a different operation. This becomes especially important when we move from curves to surfaces.

## Flux uses a different form

In the plane, circulation measures the component tangent to a boundary. Flux measures the component passing across it. For a vector field with components P and Q, the outward-flux one-form along a positively oriented boundary is P d y minus Q d x. You can see this on the right side of a rectangle. As you walk upward, d y is positive and the outward normal points right, so the contribution is positive P times height. On the top edge, walking left makes d x negative, and the outward normal points upward, so the contribution is positive Q times width.

Differentiate the flux form: it becomes the sum of the x derivative of P and the y derivative of Q, times d x wedge d y. That sum is the divergence. Integrating it over a region measures total outward flux. The same Stokes principle that gave circulation and curl now gives flux and divergence, simply because we chose the form appropriate to the measurement.

Consider the outward-pointing radial field P equals x, Q equals y on the unit disk. Its divergence is two, so total outward flux is two pi. On the unit circle, the field has unit normal component and the boundary has circumference two pi. Both calculations return two pi. This example is not merely a mnemonic: it tells us why an integral over a boundary can be replaced with an integral of a local source density.

## Moving up to three dimensions

In three dimensions, the differential-form degree is crucial. A one-form integrates along a curve, and its exterior derivative is a two-form that integrates over a surface. With a Euclidean metric and chosen orientation, the coefficients of that two-form correspond to the curl vector. The theorem says circulation along the boundary curve equals the flux of curl through the spanning oriented surface.

For a three-dimensional vector field with components P, Q and R, the outward-flux two-form is P d y wedge d z plus Q d z wedge d x plus R d x wedge d y. Its exterior derivative is divergence times d x wedge d y wedge d z. Integrating over a solid region gives the divergence theorem. There is no distinct exterior derivative invented for flux; the same operator d is used on forms of different degrees.

Why do conventional vector-calculus courses seem to use several different operators? Because the Euclidean metric and orientation allow us to identify vectors with covectors and with particular forms. The gradient comes from the derivative of a function; curl from the derivative of a one-form; divergence from the derivative of a two-form. When we change the dimension or metric, these identifications change, but the exterior derivative remains.

## The zero-after-zero principle

There is a structural reason that curl of gradient is zero, and divergence of curl is zero in their usual three-dimensional interpretation. Applying the exterior derivative twice gives zero. A potential function produces an exact one-form. Differentiating it again gives zero. A one-form produces a two-form; differentiating that again also gives zero. The familiar vector identities are just instances of the same algebraic rule.

But the reverse statements are not automatic. A curl-free field in a domain with a hole need not be the gradient of a globally defined potential. The circulating field proportional to negative y over radius squared and x over radius squared is curl-free away from the origin and still circulates around the missing point. Likewise, the global existence of a potential in higher dimensions depends on topology as well as local differential identities.

The lesson is that line and surface integrals are not unrelated recipes. Differential forms distinguish what type of oriented object we integrate over. The exterior derivative translates local change into a boundary integral. The metric may translate these forms into familiar vector fields, but the Stokes identity underneath them is the same.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On a region \(D\subset\mathbb R^2\), for \(\alpha=P\,dx+Q\,dy\),
\[d\alpha=(\partial_x Q-\partial_y P)\,dx\wedge dy,\qquad \int_{\partial D}\alpha=\int_Dd\alpha.\]
For the outward-flux one-form \(\beta=P\,dy-Q\,dx\),
\[d\beta=(\partial_xP+\partial_yQ)\,dx\wedge dy,\qquad \int_{\partial D}\beta=\int_D\operatorname{div}(P,Q)\,dx\,dy.\]
In \(\mathbb R^3\), the flux form of \(V=(P,Q,R)\) is \(\iota_V(dx\wedge dy\wedge dz)=P\,dy\wedge dz+Q\,dz\wedge dx+R\,dx\wedge dy\). Then \(d(\iota_V\mathrm{vol})=(\operatorname{div}V)\mathrm{vol}\).

### Worked examples and checks

1. For \(V=(-y,x)\), \(\oint_{\partial D} V\cdot d\mathbf r=\int_D2\,dA=2\pi\) for the unit disk.
2. For \(V=(x,y)\), outward flux across the unit circle is \(\int_D2\,dA=2\pi\).
3. Does reversing the orientation of the boundary keep a circulation integral fixed? **No:** it negates the integral.
4. Does curl-free imply a global gradient on the punctured plane? **No:** nontrivial periods obstruct it.

### Reading and sources

- Denis Auroux and Kartik Venkatram, MIT OCW [Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), differential forms and integration.
- Dominic Joyce, [Stokes Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- Overview: [Green's theorem](https://en.wikipedia.org/wiki/Green%27s_theorem), [Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem), [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem).
