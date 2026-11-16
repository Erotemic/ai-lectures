# 037000 — Divisors, Line Bundles, and Picard Groups

**Track:** Abstract Algebra. **Background:** affine schemes, localization, invertible modules, projective spaces. **Central question:** how can locally defined equations determine a global geometric object?

<!-- BEGIN SPOKEN LECTURE -->

# Divisors, Line Bundles, and Picard Groups

A line on a surface may be given by one equation near one point and a different equation somewhere else. That sounds like an inconvenience of coordinates. But the failure to find one global equation is often the geometric feature we want to measure. Divisors and line bundles turn the difference between local and global equations into algebra.

Begin with the projective line. It has two standard coordinate charts. On one chart we use the coordinate t, and on the other we use its reciprocal. Neither coordinate is defined at every point. Nevertheless, the point at infinity is a perfectly legitimate geometric object. It is cut out by a local equation in the chart that contains it, though not by a single ordinary polynomial function on the entire projective line.

A divisor on a smooth algebraic curve can be pictured as a finite collection of points, each carrying an integer weight. A positive weight records a prescribed zero; a negative weight permits a pole. We can add divisors by adding weights. If a rational function has a zero of order three at a point and a pole of order three elsewhere, those orders form its principal divisor. A crucial distinction is that not every divisor comes from one rational function.

## Equations that agree up to units

To understand the geometry in more than one dimension, consider an effective Cartier divisor. Near each point it is defined by a single equation, and that equation is required to be a non-zero-divisor in the local ring. Two local equations for the same divisor differ on overlaps by multiplication by an invertible regular function, a unit. That unit is not arbitrary error: it is precisely the transition function needed to glue a line bundle.

A line bundle is a family of one-dimensional vector spaces over the points of our space, locally trivial but not necessarily globally trivial. A section chooses one vector from each fiber compatibly. On overlapping trivializations the coordinates of that vector are multiplied by an invertible function. Around a loop or across several charts, these multipliers may obstruct any single globally consistent nonzero section.

An effective Cartier divisor determines an invertible sheaf, conventionally called O of D. Its canonical section vanishes along the divisor. Conversely, a line bundle with a suitable regular section determines an effective Cartier divisor. These constructions explain why local equations and line bundles are two ways to encode related information, although a completely arbitrary line bundle need not come equipped with a section whose zero set is a divisor.

## How an integer emerges from a bundle

Return to the projective line. On the overlap of its two affine charts, the coordinate t is invertible. We may glue trivial line bundles using a power of t as transition function. Different powers produce the standard twisting bundles, usually written O of n. Tensoring two of them adds the exponents.

Over a field, every algebraic line bundle on the projective line is isomorphic to exactly one of these twists. The Picard group, which classifies line bundles up to isomorphism under tensor product, is therefore the integers. The integer is the degree of the bundle. The bundle O of one point has degree one; its inverse has degree minus one.

Here is a way to see the difference without computing the full classification. A line bundle with a nowhere-vanishing global section is trivial: that section gives a basis in every fiber. Yet a bundle of positive degree cannot have a nowhere-vanishing section on the projective line. Any nonzero section has zeros counted with total multiplicity equal to the degree. The obstruction is measurable, not merely a missing choice of coordinates.

## Cartier divisors are not always Weil divisors

There is another, closely related use of the word divisor. A Weil divisor is a formal integer combination of codimension-one integral closed subspaces. On a smooth variety, the local rings in codimension one are particularly well behaved, and Cartier and Weil divisors agree up to the usual equivalence. On a singular variety they need not. A codimension-one subspace may fail to be given locally by one non-zero-divisor equation, and a Weil divisor may not define a line bundle.

This distinction stops several tempting but false generalizations. Knowing which codimension-one pieces exist is not always enough to know which bundles glue. Nor does the existence of many local equations imply the existence of a single global equation.

The Picard group remembers the obstruction to globally trivializing locally free rank-one data. Divisor classes give concrete ways to calculate it. On curves, this bridge will let us translate a geometric question—how many functions can have specified poles?—into a theorem relating degrees, genus, and the dimension of spaces of functions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Assume schemes are over a field unless otherwise noted. An **effective Cartier divisor** on a scheme X is a closed subscheme locally defined by a non-zero-divisor f in O_X(U). Its ideal sheaf I_D is invertible and O_X(D) = Hom_O_X(I_D,O_X). The inclusion I_D -> O_X gives a canonical section of O_X(D). For effective D,E, one has O_X(D+E) isomorphic to O_X(D) tensor O_X(E).

A **line bundle** is a locally free O_X-module of rank one. Its isomorphism classes form Pic(X), with group operation tensor product and identity O_X. A chosen trivialization on U_i has transition functions g_ij in O_X^*(U_i intersect U_j), satisfying g_ij g_jk = g_ik on triple overlaps. Up to coboundaries, this gives Pic(X) = H^1(X,O_X^*) in the sheaf-cohomology sense.

On an integral smooth projective curve, a Weil divisor is D = sum_P n_P[P], supported at finitely many closed points. The divisor of f in k(X)^* is div(f) = sum_P ord_P(f)[P]. The degree is sum_P n_P [k(P):k], with degree zero for principal divisors on a proper curve. Over an algebraically closed field the residue degrees equal one. For smooth curves, divisor classes modulo principal divisors correspond to Pic(X).

**Projective line:** Pic(P^1_k) is isomorphic to Z by [O(n)] -> n. A section of O(n) for n >= 0 corresponds to a homogeneous degree-n polynomial in two variables, with dimension n+1. Do not assert that Weil divisors coincide with Cartier divisors on arbitrary singular schemes; regular or locally factorial hypotheses matter.

### Exercises with answers

1. Why can local defining equations differ by a unit? **Answer:** if two non-zero-divisor equations define the same effective Cartier ideal on an overlap, each is an invertible multiple of the other; the multipliers provide the gluing functions.
2. Compute O(P+Q) on P^1 up to isomorphism for two rational points. **Answer:** O(2), of degree two, whether or not P and Q coincide.
3. Does every line bundle admit a global nowhere-vanishing section? **Answer:** no; such a section would trivialize the bundle, while O(1) on P^1 is nontrivial.
4. Why does the local equation y=0 define an effective Cartier divisor on A^2_k? **Answer:** y is a non-zero-divisor in k[x,y]; its principal ideal is locally free of rank one.

### Reading and source notes

- [Stacks Project, Effective Cartier divisors and invertible sheaves](https://stacks.math.columbia.edu/tag/0C4S), including the construction of O(D).
- [Stacks Project, Picard group of projective space](https://stacks.math.columbia.edu/tag/0BXJ), including Pic(P^n_k) = Z.
