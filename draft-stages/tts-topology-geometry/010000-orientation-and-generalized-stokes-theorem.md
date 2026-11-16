# 010000 — Generalized Stokes' Theorem: The Interior Speaks Through Its Boundary

**Track:** Topology and Geometry. **Background:** oriented smooth manifolds, differential forms, exterior derivatives, and classical calculus. **Central question:** why do the fundamental theorem of calculus, Green's theorem, and the classical Stokes and divergence theorems share one formula?

<!-- BEGIN SPOKEN LECTURE -->

# Generalized Stokes' Theorem: The Interior Speaks Through Its Boundary

The fundamental theorem of calculus relates a derivative integrated over an interval to the values of a function at the two endpoints. In the plane, Green's theorem relates a derivative-like quantity spread across a region to a line integral around its boundary. In three-dimensional space, the divergence theorem relates sources inside a volume to flux through its enclosing surface.

These are often taught as separate results with separate formulas. Differential forms show that they are versions of one assertion: the integral of the exterior derivative of a form over an oriented region equals the integral of the original form over its oriented boundary.

Before this assertion can be precise, we must decide what orientation means, what boundary means, and which degree of form we are integrating.

## The role of orientation

An orientation is a coherent choice of what counts as positive ordering of tangent directions. In the plane, it decides whether the pair of directions right then up is positive or negative. On a curve, it decides which way we traverse. On a surface, it chooses a consistent normal direction whenever such a global choice is possible.

If we reverse the orientation of an oriented manifold, the integral of a top-degree form changes sign. This is not a nuisance to be removed; it carries directional information. A line integral around a circle in the clockwise direction is the negative of the same integral counterclockwise.

The orientation on a boundary is not chosen independently. There is a convention called outward normal first. At a point on the boundary, put an outward-pointing normal vector first, then an oriented basis of tangent directions to the boundary. Together they should give a positive orientation of the ambient manifold.

In the standard oriented plane, that convention makes the boundary of a disk travel counterclockwise. On the interval from a to b, the right endpoint contributes positively and the left endpoint negatively. These choices are what make the signs in the theorem work.

## State the general theorem

Let M be an oriented smooth n-dimensional manifold with boundary, and let omega be a smooth differential form of degree n minus one. If M is compact, we can integrate omega over its boundary and the exterior derivative of omega over M. Generalized Stokes says those integrals are equal. On a noncompact manifold, a standard version requires omega to have compact support so that the integrals are well defined.

The smooth manifold and compact-support assumptions are not decorative. They rule out ways of losing contributions at infinity and give meaning to integration and the boundary orientation. The theorem also requires the form to have precisely the correct degree: a one-form integrates over a curve, while its two-form derivative integrates over a surface.

## Return to the interval

Take M to be the closed interval from a to b. Here n equals one, so the form omega has degree zero: it is an ordinary smooth function f. The exterior derivative is f prime times d x. Integrating it from a to b gives f of b minus f of a. The boundary consists of two oriented points. Its integral of f is f at b with a plus sign and f at a with a minus sign. The generalized formula is exactly the fundamental theorem of calculus.

Nothing mysterious has been added. The familiar theorem is already a statement that the interior derivative controls the contribution from the boundary.

## A disk and its circular boundary

Consider the unit disk in the plane, with its usual orientation. Let omega be negative y d x plus x d y. Its exterior derivative is two times d x wedge d y. The integral of that derivative over the unit disk is twice the area of the disk, so it equals two pi.

Now look at the boundary circle. Parametrize it counterclockwise by x equals cosine t and y equals sine t, with t moving from zero to two pi. Along that curve, d x contributes negative sine t times d t, and d y contributes cosine t times d t. Substitute these into omega. The result is sine squared t plus cosine squared t, all multiplied by d t. That is simply d t. Integrate once around, and the result is two pi.

The two calculations agree. One integrates rotation-like information throughout the disk; the other measures its circulation along the circle. This is Green's theorem for this particular one-form, and the same structure works for general smooth planar fields and sufficiently regular regions.

## Recover familiar vector calculus

On an oriented surface in three-dimensional space, a one-form corresponding to a vector field has an exterior derivative corresponding to the normal component of curl. Stokes' theorem says the circulation of the field around the boundary equals the flux of curl through the surface.

For a three-dimensional region, associate a two-form to the flux of a vector field across an oriented surface. Its exterior derivative corresponds to divergence times the oriented volume form. Generalized Stokes becomes the divergence theorem: total outward flux equals total divergence in the interior.

To make these identifications, we use the Euclidean metric and orientation to translate vector fields into differential forms. The exterior derivative itself does not require a metric; curl and divergence in their usual vector forms involve those additional identifications. This is one reason differential forms are useful on manifolds where no single flat coordinate grid covers the entire space.

## Why interior contributions cancel

Imagine cutting a surface into many small oriented patches. Apply a local boundary formula to every patch. Along an edge shared by two adjacent patches, the induced orientations are opposite. The integral along that edge appears twice with opposite signs and cancels. Only edges on the external boundary survive.

This cancellation is the geometric heart of Stokes' theorem. A rigorous proof uses coordinate charts and partitions of unity to reduce the statement to the fundamental theorem of calculus on Euclidean half-spaces. In that local calculation, contributions from interior directions cancel and only the true boundary remains. The partition of unity then reassembles the result without double-counting overlapping charts.

This reasoning also suggests why the boundary of a boundary vanishes. Algebraically, the exterior derivative squared is zero. Geometrically, oriented boundaries of adjacent boundary pieces cancel. These two statements are dual expressions of the same underlying structure, one in differentiation and the other in chains.

## A limitation with topological consequences

Stokes does not say that every closed form is exact. On the punctured plane, there is a closed one-form whose integral around a circle enclosing the missing point is nonzero. The circle is not the boundary of a disk lying entirely inside the punctured plane. We cannot invoke Stokes over a disk that includes a point absent from our manifold. The missing point is exactly the obstruction.

This is where calculus meets topology. A local derivative equation does not automatically supply a global potential, and whether a cycle bounds a region can depend on the topology of the space. Generalized Stokes connects the two sides without pretending that topology disappears.

The theorem teaches a principle broader than any one integral formula. The interior is not independent of its boundary: differentiation measures what must appear along that boundary, and orientation tells us how the contributions combine. Once the degrees and signs are handled coherently, several classical theorems become one geometric statement.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(M\) be a compact, oriented smooth \(n\)-manifold with boundary, and \(\omega\in\Omega^{n-1}(M)\). The induced orientation on \(\partial M\) uses **outward normal first**. Generalized Stokes' theorem is
\[
\boxed{\int_M d\omega=\int_{\partial M}\iota^*\omega},\qquad \iota:\partial M\hookrightarrow M.
\]
For noncompact \(M\), the common formulation assumes \(\omega\) compactly supported. Corners require an appropriate manifolds-with-corners formulation; the piecewise-smooth disk boundary example is covered by the usual extensions.

**One dimension.** \(M=[a,b]\), \(\omega=f\), \(\partial[a,b]=\{b\}-\{a\}\): \(\int_a^b f'(x)\,dx=f(b)-f(a)\).

**Unit disk.** \(D=\{x^2+y^2\le1\}\), \(\omega=-y\,dx+x\,dy\), \(d\omega=2\,dx\wedge dy\),
\[
\int_Dd\omega=2\pi=\int_{\partial D}\omega,
\]
with \(x=\cos t,y=\sin t\), \(0\le t\le2\pi\), and the counterclockwise boundary orientation.

**Vector-calculus identifications in Euclidean \(\mathbb R^3\).** For \(F=(P,Q,R)\), set \(\alpha=Pdx+Qdy+Rdz\). Then \(d\alpha\) corresponds to \(\nabla\times F\) via the metric and volume form. Set \(\beta=P\,dy\wedge dz+Q\,dz\wedge dx+R\,dx\wedge dy\). Then \(d\beta=(\nabla\cdot F)\,dx\wedge dy\wedge dz\). These give classical curl and divergence theorems.

### Exercises with answers

1. What is the induced boundary orientation of the standard interval? **Answer:** \(\{b\}-\{a\}\).
2. If the disk's orientation is reversed, what happens to both sides of Stokes? **Answer:** both integrals reverse sign.
3. Can the punctured-plane closed one-form with nonzero circular integral be exact? **No:** exact forms integrate to zero around every closed curve.
4. Why cannot a two-form be integrated over a curve in the ordinary differential-forms integration theory? **Answer:** integration of differential forms pairs a degree-\(k\) form with an oriented \(k\)-dimensional domain; the degrees must match.

### Reading and source notes

- Dominic Joyce, Oxford University, [Stokes' Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- MIT OCW [Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/), differential forms and generalized Stokes.
