# 020600 — Localization on the Projective Line: An Integral from Two Fractions

**Track:** Topology and Geometry. **Background:** equivariant Euler classes, Chern classes, projective coordinates, moment maps. **Central question:** can we recover ordinary intersection numbers by an explicit fixed-point calculation?

<!-- BEGIN SPOKEN LECTURE -->

# Localization on the Projective Line: An Integral from Two Fractions

We now have enough structure to calculate the entire simplest localization example, including an equivariant line bundle rather than only the tangent Euler class. The manifold is the complex projective line, the space of lines through the origin in the complex plane of dimension two. Topologically it is a two-sphere.

Let the circle leave the first coordinate unchanged and multiply the second coordinate by a complex number of unit length. It sends the homogeneous point with coordinates Z zero and Z one to the point with the same first coordinate and rotated second coordinate. The only fixed projective points are the coordinate axes.

## Work in two local charts

Near the point where Z one is zero, use the affine coordinate z equal to Z one divided by Z zero. The circle sends z to e to the i theta times z. Thus the tangent complex line has weight plus one.

Near the opposite fixed point, use w equal to Z zero divided by Z one. The circle sends w to e to the minus i theta times w. Its tangent complex line has weight minus one.

Call the first fixed point north and the other south. We have recovered the opposite tangent weights geometrically from coordinate changes. There is no need to memorize a sign table.

## Add the hyperplane line bundle

Take the tautological line bundle O of minus one. At a projective point, its fiber is exactly the line in the ambient two-dimensional complex space represented by that point. At north, the fiber is the first coordinate axis, which carries weight zero. At south, it is the second axis, which carries weight plus one.

The dual line bundle O of plus one therefore has fiber weights zero at north and minus one at south. Let x be its equivariant first Chern class. Restriction to a fixed point converts this class into the weight times u. So x restricts to zero at north and to minus u at south.

We have everything needed for localization: two tangent denominators, plus u and minus u; and two numerator restrictions, zero and minus u.

## Integrate x

At north, the contribution is zero divided by u, which is zero. At south, it is minus u divided by minus u, which is one. The sum is one.

Forget the circle action for a moment. The ordinary first Chern class of O of one integrates to one over the projective line. The localization sum agrees exactly. This is a genuine calculation of a global topological invariant from fixed-point fiber representations.

If we instead integrate the equivariant unit class, we obtain one over u plus one over minus u, hence zero. If we integrate x squared, the north contribution is zero and the south contribution is u squared divided by minus u, giving minus u. This is not an ordinary degree-four integral over a two-dimensional sphere. It is an equivariant result in degree two, and it can be nonzero because the target ring contains u.

## Find the ring relation

At north, x is zero. At south, x plus u is zero, because x restricts to minus u. Thus the product x times x plus u restricts to zero at both fixed points. In this example, the equivariant cohomology ring has the relation x times x plus u equals zero. More precisely, it is the polynomial ring in u and x, modulo that one quadratic relation.

The relation captures the calculation we just made. Replacing x squared by minus u times x and integrating gives minus u, because integrating x equals one. This provides an independent internal check on the localization result.

At u equals zero, the relation becomes x squared equals zero, which is the ordinary cohomology ring of the two-sphere. The equivariant relation remembers how the circle rotates the coordinate charts; the ordinary relation does not.

## Check the moment-map picture

There is also a differential-form version. Normalize the sphere's area to total one and parameterize the circle by t modulo one. Let the generating vector field be two pi times the derivative with respect to the azimuthal angle. Then the corresponding normalized moment map takes values plus one-half at north and minus one-half at south.

The Cartan extension of area is omega plus u times mu. It restricts to plus u over two at north and minus u over two at south. Divide by the tangent Euler classes plus u and minus u: each pole contributes one-half. The sum is one, agreeing with the total area.

Notice that these two computations use different equivariant degree-two classes. The class x of O of one restricts to zero and minus u. The equivariant symplectic class restricts to plus u over two and minus u over two. They differ by adding one-half u. Both integrate to one because the pushforward of the constant u over a two-manifold is zero.

This distinction is the source of many apparent sign errors in localization examples. The line-bundle linearization determines one representative, while the arbitrary additive constant in a moment map determines another. Once each choice is stated, both calculations agree.

## What the example teaches

We have not merely checked the formula for a quantity whose answer was known. We have computed tangent weights from local coordinates, line weights from actual fibers, cohomology restrictions from those weights, and a global integral from two elementary fractions. We also recovered a ring relation and checked it against a normalized moment map.

That collection of checks is what makes localization dependable. In more complicated problems, the fixed sets can be entire manifolds and the denominators are polynomials in several weights. But the same four pieces remain: identify fixed sets, determine normal weights, restrict the cohomology class, and add the corrected contributions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On `CP¹` let `S¹` act by `[Z_0:Z_1]↦[Z_0:e^{2πit}Z_1]`. Fixed points are `N=[1:0]` and `S=[0:1]`, with tangent weights `+1` and `-1`. Give `O(-1)` its natural equivariant lift from the ambient C² with weights `(0,1)`. For `x=c_1^{S¹}(O(1))`, restrictions are `(0,-u)`. Thus

\[
\int_{\mathbb{CP}^1}1=\frac1u-\frac1u=0,\quad
\int_{\mathbb{CP}^1}x=\frac0u+\frac{-u}{-u}=1,\quad
\int_{\mathbb{CP}^1}x^2=-u.
\]

The ring `H_{S¹}^*(CP¹;R)=R[u,x]/(x(x+u))` agrees with these pushforwards. For normalized area `ω=(1/(4π))sinθ dθ∧dφ`, `X=2π∂_φ`, `μ=(1/2)cosθ`, `ι_Xω=dμ`, and `Ω=ω+uμ` is equivariantly closed. With our choices, `Ω=x+u/2` as equivariant classes. Then `∫Ω=1`.

### Exercises with answers

1. Why is the weight at infinity negative one? **Answer:** the coordinate `w=1/z` transforms by inverse rotation.
2. Compute the fixed-point integral of x. **Answer:** `0/u+(-u)/(-u)=1`.
3. What is the relation between x² and x? **Answer:** `x²=-ux` in equivariant cohomology.
4. What happens to that relation after setting u to zero? **Answer:** it reduces to the ordinary relation `x²=0` on CP¹.

### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1), fixed-point restriction and localization.
- [Equivariant cohomology](https://en.wikipedia.org/wiki/Equivariant_cohomology); [Complex projective line](https://en.wikipedia.org/wiki/Complex_projective_line).
