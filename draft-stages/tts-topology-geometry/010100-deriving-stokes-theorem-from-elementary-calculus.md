# 010100 - Deriving Stokes' Theorem from Elementary Calculus

**Track:** Topology and Geometry. **Background:** line integrals, partial derivatives, oriented forms, partitions of unity. **Question:** how does the fundamental theorem of calculus become a theorem on manifolds?

<!-- BEGIN SPOKEN LECTURE -->

# Deriving Stokes' Theorem from Elementary Calculus

The fundamental theorem of calculus says that the integral of a derivative along an interval is the difference between the function's values at its endpoints. Green's theorem says that the circulation of a vector field around a planar region is the integral of its curl across the region. The divergence theorem says that the flux through the boundary of a solid is the integral of divergence inside it. These do not look like the same formula at first glance. But generalized Stokes' theorem puts all of them into one sentence: integrate the exterior derivative over a region, and you obtain the integral of the original form over its oriented boundary.

We will not simply quote that sentence. We will see how the elementary one-dimensional result supplies the entire mechanism, and where orientation and local coordinates enter.

## Begin with an interval

Let f be a smooth real function on the interval from a to b. Its differential is f prime times d x. Integrate this one-form from a to b. The fundamental theorem says the answer is f of b minus f of a. The boundary of an oriented interval consists of the right endpoint with positive sign and the left endpoint with negative sign. If we regard f as a zero-form and integrate it over that signed boundary, we obtain the same answer.

This is already Stokes' theorem in dimension one. The mysterious boundary orientation is simply a precise way to record the subtraction that was present in elementary calculus all along.

## A rectangle and Green's theorem

Take a rectangle with x between a and b and y between c and d. Let alpha be the one-form P d x plus Q d y. Walk around the rectangle counterclockwise. Along the bottom edge we integrate P from left to right. Along the top we integrate P from right to left. Subtract the two, and use the fundamental theorem in the y direction: their combined contribution is the negative of the double integral of the y derivative of P.

Now inspect the right and left edges. The right edge travels upward and contributes Q integrated from c to d. The left travels downward and contributes the negative of the corresponding integral. Their difference, by the fundamental theorem in the x direction, is the double integral of the x derivative of Q.

Add all four edges. We obtain the double integral of the x derivative of Q minus the y derivative of P. But that expression is exactly the coefficient of d alpha, since d of P d x plus Q d y is that coefficient times d x wedge d y.

We have proved Green's theorem for a rectangle by using the fundamental theorem twice and keeping the orientation of each edge. For regions built from rectangles, the shared interior edges are traversed in opposite directions and cancel. For more general smooth regions, approximation, parametrization, or local chart arguments carry the result further. Notice the pattern: the contributions inside adjacent pieces cancel; only the outer boundary remains.

## What changes in higher dimensions

On a three-dimensional box, a two-form has three kinds of coefficient terms, corresponding to the three coordinate-plane directions. Differentiate it. Each coefficient contributes a partial derivative in the one direction not already present. Integrate over the box. By the one-dimensional fundamental theorem, that contribution becomes the difference between the values on the two faces perpendicular to that direction.

The orientation of the two opposite faces is opposite. Again the signs are not optional: one face has outward normal pointing toward increasing coordinate, the opposite face toward decreasing coordinate. After gathering all faces we have the integral of the original two-form over the oriented boundary. In familiar vector language this is the divergence theorem.

The same proof works in n dimensions. A form of degree n minus one has one coefficient term for each omitted coordinate. Its exterior derivative differentiates that coefficient in the omitted coordinate, with the sign determined by where that coordinate would appear in the ordered wedge product. Integrating over a rectangular box reduces each term to boundary faces. The algebra of wedge products remembers the signs that in vector calculus might be inserted by a separate normal-vector convention.

## Why the statement is about manifolds

A manifold is locally modeled on Euclidean space or a Euclidean half-space if it has a boundary. In an interior chart, a compactly supported form contributes no boundary integral; applying the Euclidean theorem to its compact support gives zero on both sides. In a boundary chart, its support can meet the flat boundary of the half-space. Applying the one-dimensional fundamental theorem perpendicular to that flat boundary produces the boundary contribution, with the induced orientation.

Now choose a smooth partition of unity subordinate to such charts. Multiply the form by each weight and apply the local theorem to each piece. Because the weights add to one, the sum of their exterior derivatives is the exterior derivative of the original form: the extra terms produced by differentiating the weights cancel since the derivative of their sum is zero. The boundary pieces add to the integral over the global boundary. This is how local calculus becomes global Stokes, not by pretending we found a chart covering the whole manifold.

One should state the scope. The usual clean theorem concerns a compact oriented smooth manifold with smooth boundary and a smooth form of degree one less than the dimension. A version for noncompact manifolds holds for compactly supported forms under suitable hypotheses. Corners can be handled with compatible conventions, but they are an extension of the simplest formulation.

## The punctured disk and the missing boundary

Here is a calculation that reveals why boundary bookkeeping matters. On the punctured plane, take the one-form negative y d x plus x d y divided by x squared plus y squared. Its exterior derivative is zero away from the origin. Nevertheless the integral around a counterclockwise unit circle is two pi.

Does this contradict Stokes' theorem? No. The one-form is not smooth on the full unit disk because it is undefined at the origin. If we remove a smaller disk around the origin, the remaining annulus has two boundary components. The outer circle receives counterclockwise orientation; the inner circle receives clockwise orientation. The integral around the outer circle is two pi and around the inner circle is negative two pi. Their sum is zero, exactly equal to the integral of the zero exterior derivative over the annulus.

The missing boundary is a geometric way of seeing the obstruction to a global potential. This example also prepares us for cohomology: closed forms integrate to zero over boundaries of regions on which they are defined, but they may have nonzero integrals over cycles that do not bound such a region in the domain.

## What Stokes tells us, and what it does not

Stokes' theorem does not assert that every curve bounds a surface within the domain. It says that when a suitable oriented region and boundary are present, and the form is smooth where required, the two integrals agree. Nor does it eliminate the need to specify orientation. Reverse orientation of the region and both sides change sign. Changing only the boundary orientation breaks the equality.

From the interval to the rectangle, from the box to the smooth manifold, the proof is the same idea repeated under better organization. Integration of a derivative is a boundary calculation. The exterior derivative is engineered to make the cancellations work in every dimension, while partitions of unity make the local result independent of chart choices. Stokes is not a collection of lucky analogies. It is the fundamental theorem of calculus written in a language that survives geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a compact oriented \(n\)-manifold \(M\) with smooth boundary and \(\omega\in\Omega^{n-1}(M)\),
\[\boxed{\int_Md\omega=\int_{\partial M}\omega}.\]
Boundary orientation is determined by the rule: an outward-pointing normal followed by a positively oriented basis of \(T\partial M\) gives a positive basis of \(TM\).

For \(R=[a,b]\times[c,d]\), \(\alpha=P\,dx+Q\,dy\), Green's theorem is
\[\oint_{\partial R}\alpha=\int_c^d\int_a^b(\partial_xQ-\partial_yP)\,dx\,dy.\]
For a partition \(\sum_i\rho_i=1\), \(\sum_i d(\rho_i\omega)=d\omega\), since \(\sum_i d\rho_i=d1=0\).

**Annulus calculation.** For \(\eta=(-y\,dx+x\,dy)/(x^2+y^2)\), \(d\eta=0\) on \(r_0\le r\le r_1\), and \(\int_{\partial A}\eta=2\pi-2\pi=0\).

### Check your understanding

1. What is \(\partial[a,b]\) as an oriented zero-chain? **Answer:** \([b]-[a]\).
2. Why do the interior edges cancel when neighboring rectangles are combined? **Answer:** they inherit opposite orientations.
3. May Stokes be applied to the singular one-form \(\eta\) on the disk including the origin? **No:** it is not defined there.

### Reading and sources

- Dominic Joyce, [Stokes Theorem: Orientations and Integration](https://people.maths.ox.ac.uk/~joyce/Nairobi2019/IDG5%2B6handout.pdf).
- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Generalized Stokes theorem](https://en.wikipedia.org/wiki/Generalized_Stokes_theorem).
