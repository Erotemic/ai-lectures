# Equivariant cohomology and fixed-point localization

<!-- BEGIN SPOKEN LECTURE -->

# Equivariant cohomology and fixed-point localization

## Equivariant Cohomology: The Space That Remembers Its Symmetry

Imagine two ways for a circle to act on a sphere. In one, the circle does nothing: every point is fixed. In the other, it rotates the sphere around an axis: only the poles are fixed. The underlying sphere is the same in both cases, so its ordinary cohomology cannot distinguish these actions. An ordinary quotient remembers some of the difference, but it has another weakness: at a fixed point, an entire group collapses to the same location.

Equivariant cohomology is designed to retain the topology of the space together with how the symmetry acts on it. To build it, we first need a simple but powerful construction called a homotopy quotient.

### Why the ordinary quotient loses information

For a group G acting on a space M, the orbit space M divided by G identifies points that can be moved into each other. If the action is free and well behaved, this quotient is often a useful geometric space. But if there are fixed points, the quotient can hide stabilizers: a point fixed by the whole group and a point with no nontrivial stabilizer both become points of the orbit space.

The most extreme example is the action of a circle on a single point. Its ordinary quotient is still one point. If we take ordinary cohomology of that quotient, we see only the constants. Yet the group action has retained an entire circle's worth of symmetry at that point. A theory intended to remember stabilizers should not simply discard it.

### Replace orbits with homotopy orbits

Introduce a contractible space called E G on which G acts freely. Form the product E G times M, with G acting diagonally, and divide by G. The result is the Borel construction, also called the homotopy quotient of M by G.

It looks elaborate, but it solves exactly the problem we encountered. By inserting E G, we replace the original action with a free diagonal action before taking the quotient. The ordinary cohomology of this new space is, by definition, Borel equivariant cohomology of M.

The resulting space fibers over B G, the quotient E G divided by G. Its fiber is M. The base B G records the symmetry group, while the fiber records the original space. The manner in which they fit together records how the group acts.

### Calculate the action on a point

For the circle group, its classifying space B S one can be modeled by infinite complex projective space. Its cohomology with real coefficients is a polynomial algebra in one variable u of degree two.

Therefore equivariant cohomology of a point under the circle group is not just the real numbers. It is the full polynomial ring in u. The variable is not an arbitrary trick. It is the first Chern class of the universal complex line bundle over the classifying space, and it records the circle's geometry in cohomological degree two.

The polynomial degrees continue indefinitely even though the original space consists of one point. There is no paradox: we are taking cohomology of the homotopy quotient, which contains the topology of B S one, not the original point by itself.

### A free action gives a simpler result

Let the circle act on itself by multiplication. Every orbit is the entire circle, and the action is free. Its ordinary orbit space is one point. The homotopy quotient is homotopy equivalent to the same point, so its equivariant cohomology is simply the real numbers.

Compare that with the trivial action on a point, which gave a polynomial ring. In one example, no point has any nontrivial stabilizer; in the other, every point is fixed by the whole group. The difference is now visible algebraically.

More generally, when G acts freely and sufficiently nicely on M, the Borel construction is homotopy equivalent to M divided by G. Equivariant cohomology then agrees with ordinary cohomology of the quotient. This explains why the construction is an extension of quotient topology, not a replacement for it in every situation.

### What if the group acts trivially on a larger space?

When a circle acts trivially on M, the Borel construction becomes the product of M with B S one. With real coefficients and the usual finite-type assumptions, its cohomology is the ordinary cohomology of M tensored with the polynomial ring in u.

For a two-sphere with trivial action, we obtain two families of classes: constants and the sphere's degree-two generator, each multiplied by arbitrary powers of u. For rotation of the same sphere, the additive structure may look similar, but the way the classes multiply and restrict to the fixed points carries the action data.

The degree-two variable u is the bookkeeping device that eventually appears in localization denominators. Before dividing by anything, we need to understand why it is present and why its degree is two.

### Why fixed points will matter

Suppose a circle rotates a compact manifold and fixes isolated points. Near one fixed point, the group acts linearly on the tangent space, with integer rotation weights. Those weights are invisible to ordinary cohomology of the underlying manifold but visible in equivariant characteristic classes. When we later restrict an equivariant class to the fixed point, the answer is a polynomial in u whose coefficients remember those weights.

The localization theorem will allow us to recover a global integral from these weighted fixed-point restrictions after inverting u. That remarkable conclusion rests on a modest starting idea: when taking a quotient, do not throw away the symmetry group's topology. Build a space that remembers the group even at the points it leaves fixed.

## The Cartan Model: An Exterior Derivative that Knows the Action

The homotopy quotient explains what equivariant cohomology is, but it is rarely where we want to do calculations. The auxiliary contractible space E G is infinite-dimensional in the standard models. We would rather work with differential forms on the original finite-dimensional manifold and a manageable symbol recording the group action.

For a smooth circle action, the Cartan model does exactly that. It modifies the exterior derivative by one operation from vector calculus: inserting the infinitesimal generator of the symmetry into a differential form.

### What contraction does

A vector field X tells us the direction in which a one-parameter group moves each point. A differential one-form assigns a number to a tangent vector. Contracting that one-form with X simply evaluates the form on X. For a two-form, contraction produces a one-form by placing X into the first slot. In general, contraction lowers form degree by one.

The usual exterior derivative raises form degree by one. If we want to subtract contraction from the exterior derivative while keeping a consistent total grading, we multiply contraction by a formal variable u of degree two. Then both terms raise total degree by one.

Define the equivariant differential by the ordinary exterior derivative minus u times contraction with X. This formula is often written d sub T. Different books use an overall sign change or another normalization of X; we will keep this convention fixed.

### Why the square is zero only for invariant forms

The square of the ordinary exterior derivative is zero. Contracting twice with the same vector field is also zero because alternating forms vanish when two slots receive the same vector. The remaining cross terms combine into the Lie derivative along X, by Cartan's identity.

Consequently the square of d sub T is minus u times the Lie derivative. This is not zero on an arbitrary differential form. It becomes zero on forms invariant under the circle action, because those have zero Lie derivative along X.

Thus the Cartan complex consists of circle-invariant differential forms with coefficients in the polynomial ring in u, equipped with d sub T. Its cohomology computes circle-equivariant cohomology with real coefficients, for a compact circle action. We have traded the abstract homotopy quotient for differential forms and a formal variable.

### Work out the freely rotating circle

Take M to be a circle with coordinate t modulo one. Let the circle act on itself by translation, so the generating vector field X is the derivative with respect to t. The invariant differential forms are combinations of constants and the one-form dt, with polynomial coefficients in u.

The ordinary exterior derivative of dt is zero. Its contraction with X is one. Therefore the equivariant differential of dt is minus u. That single calculation has a large consequence: u is an equivariant boundary. So are all its positive powers, since u to the k is the equivariant differential of minus u to the k minus one times dt.

What remains in equivariant cohomology is just the constant class. This matches the Borel calculation: a circle acting freely on itself has contractible homotopy quotient. We have reproduced that fact using an explicit two-term algebra of differential forms.

The result also explains why the polynomial variable is not automatically a nonzero class in every equivariant space. It exists in the complex, but a differential can kill it when the geometry of the action supplies an invariant one-form evaluating to one on X.

### A Hamiltonian action has a special closed form

Now let the circle act on a symplectic manifold with symplectic form omega. Suppose the generator X is Hamiltonian: contraction of omega with X equals the differential of a function mu, called a moment map component.

Consider the combination omega plus u times mu. Apply the equivariant differential. The derivative of omega vanishes because omega is symplectic. The remaining terms are u times the differential of mu minus u times the contraction of omega. They cancel exactly.

So omega plus u mu is equivariantly closed. This is a crucial bridge between symplectic geometry and localization. Ordinary omega carries area. The moment-map term records the action. Their sum is a single cohomology class in the Cartan complex.

It is essential that mu be a genuine global function. On a flat torus, translation in one coordinate preserves the area form but its contracted one-form may have a nonzero period; then no global mu exists. The Cartan combination cannot be constructed in that simple way for that action.

### A check at a fixed point

At a fixed point p, every positive-degree differential form on a point vanishes. The equivariant class omega plus u mu restricts to u times the number mu of p. A global symplectic form has become a polynomial, and its coefficient is the moment-map value at the fixed point.

Later the fixed-point tangent weights will appear in a denominator. The Cartan model has already given us the numerator. It makes the localization theorem less mysterious: the fixed-point formula evaluates a globally closed equivariant object where the symmetry stops moving the manifold.

The two calculations worth retaining are small. On a freely rotating circle, d sub T of dt equals minus u. For a Hamiltonian action, d sub T of omega plus u mu equals zero. These two identities explain much of the difference between free actions and actions with fixed points.

## Fixed-Point Localization: Weights, Euler Classes, and Denominators

A localization formula can look suspicious at first. How could an integral over an entire compact manifold equal a finite sum over isolated points? To understand why, focus not on the sum but on the denominator. It measures the directions lost when we restrict from the manifold to its fixed set.

Near a fixed point of a circle action, the group acts linearly on the tangent space. Because the group is compact, we can choose a compatible metric and split the representation into two-dimensional rotation planes and directions on which the action is trivial. For an isolated fixed point, no nonzero tangent direction is fixed, so the tangent space splits into genuine rotation planes.

### Rotation weights are integers

On an oriented real two-plane carrying a complex structure, the circle can act by rotating a vector through n times the group angle. The integer n is the weight. Positive and negative weights give opposite oriented rotations. Weight zero means the circle acts trivially on that plane, so it would be tangent to a fixed component rather than normal to one.

For one such complex line, the equivariant Euler class is its weight multiplied by the polynomial generator u, with the orientations chosen consistently. For a direct sum of rotation planes, multiply the individual Euler classes. Thus an isolated fixed point in a four-dimensional manifold with two weights a and b has tangent equivariant Euler class a times b times u squared.

This is why the weights cannot be omitted. Two fixed points with the same value of an integrand may contribute differently if their normal representations have different weights.

### The localization statement

For a compact oriented manifold with a torus action, the Atiyah–Bott–Berline–Vergne formula expresses the equivariant integral of a closed equivariant class as a sum over fixed components. On each component, restrict the class, divide by the equivariant Euler class of its normal bundle, and integrate over that component.

Division requires care. Before localization, the coefficient ring consists of polynomials in equivariant parameters. After localization, we invert nonzero weights and the necessary polynomial factors. The individual fixed-point contributions may be rational functions, even though their sum is a polynomial. This cancellation is one of the most instructive features of the theorem.

If the fixed points are isolated, integration over a point does nothing. The formula reduces to a sum of the values of the equivariant class divided by tangent Euler classes. If a fixed component has positive dimension, we must integrate over that component and use the Euler class of its *normal* bundle. Tangent directions within the fixed component are not divided out.

### Two poles and two opposite weights

Rotate a two-sphere around its vertical axis. Only the north and south poles are fixed. With the complex orientation induced by the sphere's area form, the linearized rotation has weight plus one at the north pole and minus one at the south pole, when the circle generator and orientations are normalized consistently.

Integrate the equivariant unit class one. The north contribution is one divided by u. The south contribution is one divided by minus u. They cancel. That is exactly what the cohomological degree rule predicts: integrating a degree-zero class over an oriented two-dimensional manifold produces an element in degree minus two, which must vanish in the unlocalized polynomial ring.

Now integrate the equivariant Euler class of the tangent bundle. At a fixed point its restriction equals the tangent Euler class itself, so each quotient is one. The result is two, equal to the Euler characteristic of the sphere. In ordinary Gauss–Bonnet language, curvature integrated over the sphere also yields two after the conventional normalization. The localization formula has converted a global curvature invariant into two local representation calculations.

### Why the formula is geometrically plausible

On the part of the manifold where the circle acts without fixed points, the generating vector field does not vanish. One can use an invariant one-form that evaluates to one on the generator and construct a homotopy showing, after inverting u, why equivariant cohomology there is severely constrained. Near the fixed set that construction breaks down because the generating vector field becomes zero.

So after localization, the fixed set is precisely where the surviving equivariant information concentrates. A rigorous proof uses equivariant Thom classes, pushforwards and the self-intersection formula, or an equivalent differential-form argument. The Euler-class denominator is the correction factor for inserting a fixed component into the ambient manifold.

### Boundaries of the theorem

The compactness and orientation assumptions are not optional decoration. For a noncompact manifold, an integral may diverge or receive boundary-at-infinity terms. For a fixed component with a nontrivial normal bundle, its equivariant Euler class contains ordinary characteristic classes in addition to the weights. If the normal representation has zero weights, the supposed fixed component was not the full fixed locus or the chosen torus parameter requires refinement.

There is no general permission to replace integration by counting fixed points. What localization permits is a precisely weighted pushforward after a specified algebraic localization. Once the tangent weights and degree conventions are visible, the formula becomes a tool for actual computations rather than a magic trick.

## Localization on the Projective Line: An Integral from Two Fractions

We now have enough structure to calculate the entire simplest localization example, including an equivariant line bundle rather than only the tangent Euler class. The manifold is the complex projective line, the space of lines through the origin in the complex plane of dimension two. Topologically it is a two-sphere.

Let the circle leave the first coordinate unchanged and multiply the second coordinate by a complex number of unit length. It sends the homogeneous point with coordinates Z zero and Z one to the point with the same first coordinate and rotated second coordinate. The only fixed projective points are the coordinate axes.

### Work in two local charts

Near the point where Z one is zero, use the affine coordinate z equal to Z one divided by Z zero. The circle sends z to e to the i theta times z. Thus the tangent complex line has weight plus one.

Near the opposite fixed point, use w equal to Z zero divided by Z one. The circle sends w to e to the minus i theta times w. Its tangent complex line has weight minus one.

Call the first fixed point north and the other south. We have recovered the opposite tangent weights geometrically from coordinate changes. There is no need to memorize a sign table.

### Add the hyperplane line bundle

Take the tautological line bundle O of minus one. At a projective point, its fiber is exactly the line in the ambient two-dimensional complex space represented by that point. At north, the fiber is the first coordinate axis, which carries weight zero. At south, it is the second axis, which carries weight plus one.

The dual line bundle O of plus one therefore has fiber weights zero at north and minus one at south. Let x be its equivariant first Chern class. Restriction to a fixed point converts this class into the weight times u. So x restricts to zero at north and to minus u at south.

We have everything needed for localization: two tangent denominators, plus u and minus u; and two numerator restrictions, zero and minus u.

### Integrate x

At north, the contribution is zero divided by u, which is zero. At south, it is minus u divided by minus u, which is one. The sum is one.

Forget the circle action for a moment. The ordinary first Chern class of O of one integrates to one over the projective line. The localization sum agrees exactly. This is a genuine calculation of a global topological invariant from fixed-point fiber representations.

If we instead integrate the equivariant unit class, we obtain one over u plus one over minus u, hence zero. If we integrate x squared, the north contribution is zero and the south contribution is u squared divided by minus u, giving minus u. This is not an ordinary degree-four integral over a two-dimensional sphere. It is an equivariant result in degree two, and it can be nonzero because the target ring contains u.

### Find the ring relation

At north, x is zero. At south, x plus u is zero, because x restricts to minus u. Thus the product x times x plus u restricts to zero at both fixed points. In this example, the equivariant cohomology ring has the relation x times x plus u equals zero. More precisely, it is the polynomial ring in u and x, modulo that one quadratic relation.

The relation captures the calculation we just made. Replacing x squared by minus u times x and integrating gives minus u, because integrating x equals one. This provides an independent internal check on the localization result.

At u equals zero, the relation becomes x squared equals zero, which is the ordinary cohomology ring of the two-sphere. The equivariant relation remembers how the circle rotates the coordinate charts; the ordinary relation does not.

### Check the moment-map picture

There is also a differential-form version. Normalize the sphere's area to total one and parameterize the circle by t modulo one. Let the generating vector field be two pi times the derivative with respect to the azimuthal angle. Then the corresponding normalized moment map takes values plus one-half at north and minus one-half at south.

The Cartan extension of area is omega plus u times mu. It restricts to plus u over two at north and minus u over two at south. Divide by the tangent Euler classes plus u and minus u: each pole contributes one-half. The sum is one, agreeing with the total area.

Notice that these two computations use different equivariant degree-two classes. The class x of O of one restricts to zero and minus u. The equivariant symplectic class restricts to plus u over two and minus u over two. They differ by adding one-half u. Both integrate to one because the pushforward of the constant u over a two-manifold is zero.

This distinction is the source of many apparent sign errors in localization examples. The line-bundle linearization determines one representative, while the arbitrary additive constant in a moment map determines another. Once each choice is stated, both calculations agree.

### What the example teaches

We have not merely checked the formula for a quantity whose answer was known. We have computed tangent weights from local coordinates, line weights from actual fibers, cohomology restrictions from those weights, and a global integral from two elementary fractions. We also recovered a ring relation and checked it against a normalized moment map.

That collection of checks is what makes localization dependable. In more complicated problems, the fixed sets can be entire manifolds and the denominators are polynomials in several weights. But the same four pieces remain: identify fixed sets, determine normal weights, restrict the cohomology class, and add the corrected contributions.

## Moment-Map Measures: From Symplectic Area to Duistermaat–Heckman

Suppose we place points uniformly at random on the surface of a round sphere. What is the distribution of their heights? Most people first imagine that the sphere has more surface near the equator, because those latitude circles are longer. So perhaps heights near the equator should be more likely.

That conclusion misses the width of a thin band. Near the equator, a change in height corresponds to a shorter meridional distance. Near a pole, the same change in height sweeps a longer meridional distance. These effects cancel exactly. Uniform area on a sphere gives a uniform distribution of height.

This elementary fact is an instance of the geometry behind the Duistermaat–Heckman theorem. We will prove it directly, then recover it again from equivariant localization.

### Normalize the sphere

Give the sphere total symplectic area one. Use polar angle theta measured from the north pole and azimuthal angle phi, with phi running once around from zero to two pi. The area form is sine theta divided by four pi, times d theta wedge d phi.

Let the circle parameter t run from zero to one and rotate phi by two pi t. The generating vector field is two pi times the derivative with respect to phi. Under the Hamiltonian convention used in this track, contracting the symplectic form with the generator equals the derivative of the moment map. One convenient moment map is one-half cosine theta.

Its value at north is plus one-half and at south minus one-half. Call that value m. When theta increases, m decreases. Differentiating gives minus one-half sine theta times d theta. Substitute this into the area form. The measure becomes d t times d m, with the correct orientation accounting for the reversed limits.

Integrating over the circular coordinate t contributes one. What remains is ordinary Lebesgue measure in m, on the interval from minus one-half to plus one-half. Thus the moment map pushes normalized area to uniform measure on that interval.

### A physical check with bands

Consider a thin band between heights m and m plus a small change delta m. Its area is approximately delta m, independent of m, as long as the band stays away from the endpoints. Its probability under uniform surface area is the same number. The direct coordinate derivation has now become an immediately testable geometric statement.

The endpoints are special: the latitude circle collapses to a fixed point at the north or south pole. At interior values, the circle action is free on each moment level. Symplectic reduction of the two-sphere at a regular moment value produces a zero-dimensional manifold, a single point. Its symplectic volume is one under the standard zero-dimensional convention. That is another reason the pushforward density is constant.

In higher dimensions, the reduced spaces can have positive dimension and their symplectic volumes vary with the moment value. The Duistermaat–Heckman theorem says that, under its Hamiltonian torus-action hypotheses, the resulting density is piecewise polynomial. The sphere is the degree-zero case.

### Derive the exponential integral

A useful way to package the entire height distribution is its moment-generating integral. Multiply the area form by the exponential of a parameter times the height and integrate over the sphere. With the normalized uniform distribution, this is simply the integral of the exponential from minus one-half to plus one-half. Elementary calculus gives the hyperbolic sine expression: two times sinh of half the parameter, divided by the parameter.

Now let the parameter be t times the equivariant variable u, but use a different spoken name for the circle coordinate to avoid confusion. The equivariantly closed form omega plus u mu can be exponentiated formally. Integrating its exponential after multiplying by an auxiliary parameter a produces two times sinh of a u over two, divided by u. For u approaching zero, the expression approaches a, the integral of a omega, exactly as expected from the first-degree term of the exponential.

### Recover the same expression at fixed points

At the north pole, the equivariant symplectic form restricts to plus u over two. At the south pole it restricts to minus u over two. Their tangent Euler classes are plus u and minus u.

Localization says the integral of the exponential of a times the equivariant symplectic form is the north exponential divided by u, minus the south exponential divided by u. This is the hyperbolic sine expression we obtained by ordinary integration.

The equality is stronger than the single identity that area equals one. As a formal power series in a and u, it equates all the moments of the height distribution with fixed-point information. Expanding the hyperbolic sine, we see that the mean height is zero, the second moment is one-twelfth, and higher even moments follow similarly. Odd moments vanish by symmetry.

The calculation is exact because the sphere is compact, the circle action is Hamiltonian, and our normalization was specified. Change the total area or the period of the generating circle, and the numerical coefficients change accordingly. The conceptual theorem does not change, but a careless mixture of conventions would make the fixed-point and coordinate calculations disagree.

### Why this matters beyond spheres

In symplectic reduction, the moment map assigns conserved quantities to points of a symplectic manifold. The pushforward of Liouville measure describes how much phase-space volume lies near each value. Duistermaat and Heckman's result connects this measure with reduced spaces and, through equivariant localization, with fixed-point geometry.

This is the foundational bridge between moment maps, equivariant cohomology, and localization. We began with an intuitive probability question, derived the answer using coordinates, reinterpreted it using reduced spaces, and finally recovered the full generating function using two fixed points. The abstract theory earns its place because all four descriptions agree.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Equivariant Cohomology: The Space That Remembers Its Symmetry

**Track:** Topology and Geometry. **Background:** ordinary cohomology, quotient spaces, classifying spaces in outline. **Central question:** why is cohomology of the ordinary quotient insufficient when fixed points exist?

#### Mathematical companion (not spoken)

For a suitable G-space M, choose contractible free EG. Then

\[
M_G=EG\times_G M,\qquad H_G^*(M;R)=H^*(M_G;R),
\]

with a fibration `M→M_G→BG`. For `G=S¹`, `BG≈CP^∞`, and `H^*(BG;R)=R[u]`, `|u|=2`. When G acts trivially, `M_G≈M×BG` and over a field the Künneth formula gives `H_G^*(M)≈H^*(M)⊗R[u]` under standard hypotheses. When G acts freely and the action yields a well-behaved quotient, `M_G≈M/G` up to homotopy.

##### Exercises with answers

1. What is `H_{S¹}^*(pt;R)`? **Answer:** `R[u]`, with u in degree two.
2. What is the equivariant cohomology of S¹ acting on itself freely by translation? **Answer:** R in degree zero and zero in positive degrees.
3. Why does ordinary cohomology of a sphere not distinguish trivial from rotational circle action? **Answer:** the underlying topological sphere is identical; the action is extra structure.
4. What information can restriction to a fixed point reveal? **Answer:** the circle weights on equivariant bundles and tangent representations.

##### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf), foundational exposition.
- [Equivariant cohomology](https://en.wikipedia.org/wiki/Equivariant_cohomology); [Classifying space](https://en.wikipedia.org/wiki/Classifying_space).

### The Cartan Model: An Exterior Derivative that Knows the Action

**Track:** Topology and Geometry. **Background:** differential forms, Lie derivative, contraction with vector fields. **Central question:** how can equivariant cohomology be calculated using differential forms on the original manifold?

#### Mathematical companion (not spoken)

Let `X` be the infinitesimal generator of a period-one circle action. Work over R and set

\[
\Omega_{S^1}(M)=\big(\Omega^*(M)\otimes\mathbb R[u]\big)^{S^1},\quad
|u|=2,\quad d_T=d-u\iota_X.
\]

Cartan's identity `dι_X+ι_X d=L_X` gives `d_T²=-uL_X=0` on invariant forms. On `M=R/Z` with `X=∂_t`, `d_T(dt)=-u`; hence `H^*(\Omega_{S^1}(M),d_T)=R` in degree zero. For Hamiltonian `ι_X ω=dμ`, `d_T(ω+uμ)=0`. The moment map is defined only up to a constant; shifting μ adds a multiple of the equivariant class u.

##### Exercises with answers

1. What degree must u have for `uι_X` to raise total degree by one? **Answer:** two.
2. Why is the Cartan differential square-zero only on invariant forms? **Answer:** `d_T²=-uL_X`; invariance gives `L_X=0`.
3. Calculate `d_T(u² dt)` for the free translation circle. **Answer:** `-u³`.
4. If `ι_Xω=dμ`, what is the simplest equivariantly closed extension of omega under this sign convention? **Answer:** `ω+uμ`.

##### Sources and further reading

- L. Jeffrey, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), Cartan model and localization.
- [Cartan model](https://en.wikipedia.org/wiki/Equivariant_cohomology#The_Cartan_model); [Cartan's magic formula](https://en.wikipedia.org/wiki/Cartan%27s_magic_formula).

### Fixed-Point Localization: Weights, Euler Classes, and Denominators

**Track:** Topology and Geometry. **Background:** equivariant cohomology, characteristic classes, oriented integration. **Central question:** why does a fixed point contribute the reciprocal of a rotation weight?

#### Mathematical companion (not spoken)

For a torus T acting on compact oriented M, and `α∈H_T^*(M)` over Q or R, the ABBV formula in localized equivariant cohomology reads

\[
\int_M\alpha=\sum_{F\subset M^T}\int_F\frac{i_F^*\alpha}{e_T(N_F)}.
\]

At an isolated fixed point with oriented complex tangent weights `w_1,...,w_n`, `e_T(T_pM)=(∏_j w_j)u^n` for S¹. For standard oriented `S²`, north and south weights are `+1,-1`. Thus `∫_{S²}1=1/u-1/u=0`; `∫_{S²}e_T(TS²)=1+1=2`.

The phrase “integral of 1” denotes the degree-lowering cohomological pushforward, not the area of the sphere. Area is the integral of a degree-two form. The distinction prevents a frequent false comparison.

##### Exercises with answers

1. What is the equivariant Euler class of a weight-three complex line? **Answer:** `3u`.
2. What is it for two complex lines of weights two and minus three? **Answer:** `-6u²`.
3. Why do the two fixed-point contributions for `∫1` cancel on S²? **Answer:** their tangent weights have opposite signs.
4. What bundle supplies the denominator for a positive-dimensional fixed component F? **Answer:** the equivariant normal bundle `N_F`, not `TF`.

##### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1) (1984).
- L. Jeffrey, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf), the abelian localization theorem.
- [Atiyah–Bott localization theorem](https://en.wikipedia.org/wiki/Equivariant_cohomology).

### Localization on the Projective Line: An Integral from Two Fractions

**Track:** Topology and Geometry. **Background:** equivariant Euler classes, Chern classes, projective coordinates, moment maps. **Central question:** can we recover ordinary intersection numbers by an explicit fixed-point calculation?

#### Mathematical companion (not spoken)

On `CP¹` let `S¹` act by `[Z_0:Z_1]↦[Z_0:e^{2πit}Z_1]`. Fixed points are `N=[1:0]` and `S=[0:1]`, with tangent weights `+1` and `-1`. Give `O(-1)` its natural equivariant lift from the ambient C² with weights `(0,1)`. For `x=c_1^{S¹}(O(1))`, restrictions are `(0,-u)`. Thus

\[
\int_{\mathbb{CP}^1}1=\frac1u-\frac1u=0,\quad
\int_{\mathbb{CP}^1}x=\frac0u+\frac{-u}{-u}=1,\quad
\int_{\mathbb{CP}^1}x^2=-u.
\]

The ring `H_{S¹}^*(CP¹;R)=R[u,x]/(x(x+u))` agrees with these pushforwards. For normalized area `ω=(1/(4π))sinθ dθ∧dφ`, `X=2π∂_φ`, `μ=(1/2)cosθ`, `ι_Xω=dμ`, and `Ω=ω+uμ` is equivariantly closed. With our choices, `Ω=x+u/2` as equivariant classes. Then `∫Ω=1`.

##### Exercises with answers

1. Why is the weight at infinity negative one? **Answer:** the coordinate `w=1/z` transforms by inverse rotation.
2. Compute the fixed-point integral of x. **Answer:** `0/u+(-u)/(-u)=1`.
3. What is the relation between x² and x? **Answer:** `x²=-ux` in equivariant cohomology.
4. What happens to that relation after setting u to zero? **Answer:** it reduces to the ordinary relation `x²=0` on CP¹.

##### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1), fixed-point restriction and localization.
- [Equivariant cohomology](https://en.wikipedia.org/wiki/Equivariant_cohomology); [Complex projective line](https://en.wikipedia.org/wiki/Complex_projective_line).

### Moment-Map Measures: From Symplectic Area to Duistermaat–Heckman

**Track:** Topology and Geometry. **Background:** Hamiltonian circle actions, equivariant forms, elementary probability densities. **Central question:** how can the distribution of a conserved quantity be computed by geometry and fixed points?

#### Mathematical companion (not spoken)

Use `φ∈[0,2π)`, `t=φ/(2π)`, `ω=(1/(4π))sinθ dθ∧dφ`, `X=2π∂_φ`, `μ=cosθ/2`; then `∫_{S²}ω=1`, `ι_Xω=dμ` and `μ_*(ω)` is Lebesgue measure on `[-1/2,1/2]`. For formal parameter a,

\[
\int_{S^2}e^{a(\omega+u\mu)}
=\frac{e^{au/2}-e^{-au/2}}{u}
=\frac{2\sinh(au/2)}{u}.
\]

On the left, the cohomological integral extracts only form degree 2. The same result comes from integrating `a e^{auμ} ω` over S², or from ABBV at the two fixed points. Expanding about `u=0` gives `a+a³u²/24+...`, so for the uniform variable μ, `E[μ]=0`, `E[μ²]=1/12`. Duistermaat–Heckman generalizes this to piecewise-polynomial densities under appropriate compactness/properness and torus-action assumptions.

##### Exercises with answers

1. What is the total area of a moment-map band with m between 0 and 1/4? **Answer:** 1/4.
2. What is the expectation of μ under normalized area? **Answer:** zero.
3. What is the second moment of μ? **Answer:** `∫_{-1/2}^{1/2}m² dm=1/12`.
4. What is the symplectic quotient at a regular moment value for this sphere action? **Answer:** a point (zero-dimensional reduced space).

##### Sources and further reading

- J. J. Duistermaat and G. J. Heckman, [On the Variation in the Cohomology of the Symplectic Form of the Reduced Phase Space](https://doi.org/10.1007/BF01399506), Inventiones Mathematicae 69 (1982), 259–268.
- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1) (1984).
- [Duistermaat–Heckman formula](https://en.wikipedia.org/wiki/Duistermaat%E2%80%93Heckman_formula); [Moment map](https://en.wikipedia.org/wiki/Moment_map).
