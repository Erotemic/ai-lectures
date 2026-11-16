# 018200 — Vector Bundle K-Theory: Why Subtraction Needs New Objects

**Track:** Topology and Geometry. **Background:** vector bundles, direct sums, homotopy. **Central question:** what information survives when we permit adding trivial bundles and formally subtracting bundles?

<!-- BEGIN SPOKEN LECTURE -->

# Vector Bundle K-Theory: Why Subtraction Needs New Objects

There are two ways to compare a pair of vector bundles. We can ask whether they are isomorphic as they stand, or we can ask whether they become isomorphic after adding an auxiliary bundle. The second question is less rigid. It is also the one that occurs naturally when we study elliptic differential operators, because the dimensions of a kernel and cokernel can change in a family even when their formal difference remains meaningful.

The simplest analogy comes from counting apples. Natural numbers let us add collections. If one collection contains three apples and another contains five, then a difference of the collections would have value negative two. The natural numbers do not contain that answer, so we pass to the integers. K-theory performs a related construction on vector bundles. We must take care: a bundle is much more than its rank. Two bundles of the same rank may twist differently over the same base.

## The addition we already possess

Fix a compact space such as a finite CW complex. A complex vector bundle assigns a complex vector space to each point, varying locally like a product. If we have bundles E and F, their direct sum has fiber E at x direct-summed with F at x. Its rank is the sum of their ranks. Direct sum is associative and commutative up to canonical isomorphism, and the rank-zero bundle is an identity.

But there is no ordinary inverse bundle. If E has positive rank, there is no bundle F with E direct-summed with F equal to the rank-zero bundle. The rank would have to be negative. This is exactly the obstruction that prevents the natural numbers from supporting subtraction.

To create a difference, write a formal pair: E minus F. Two such pairs represent the same virtual bundle if adding suitable auxiliary bundles makes their positive and negative parts isomorphic. In the group of virtual bundles, the difference of E and F plus the difference of F and E is zero. The resulting group is K zero of the space.

This does not say there is an actual vector bundle of negative rank sitting over each point. A virtual bundle is an algebraic class represented by a difference, not a mysterious physical bundle with negative-dimensional fibers.

## Stable equivalence and an embedding trick

Suppose E is a complex vector bundle over a compact Hausdorff base. We can find another bundle F such that E plus F is a trivial bundle of some finite rank. The idea is to use finitely many local generating sections, combine them with a partition of unity, and embed E into a sufficiently large trivial bundle. A Hermitian metric lets us take an orthogonal complement.

This is an important surprise. A bundle need not be trivial, but it can be a direct summand of a trivial bundle. Consequently, stabilization by trivial summands is not an arbitrary game: it has the geometry of embeddings and complements behind it.

If two bundles become isomorphic after adding trivial summands of possibly different ranks, they define the same appropriate stable difference. Conversely, equality in K zero can be expressed in terms of stable isomorphisms. One must still track rank, because the trivial line and the rank-zero bundle represent different classes even though neither has any twisting.

## Calculate K zero of a point

Over a point, every complex bundle is merely a vector space. Its isomorphism class is determined by a nonnegative integer, its dimension. Direct sum adds dimensions. Completing that monoid to a group gives the integers. Thus K zero of a point is the ordinary integer group.

There is a rank map from K zero of a connected space to the integers. It sends E minus F to rank E minus rank F. The reduced K group is the kernel of the restriction to a chosen basepoint. Reduced classes remember twisting after the rank information has been discarded.

The distinction matters. A class of rank zero can still be nonzero in reduced K-theory. We will encounter one on the sphere, where a complex line bundle differs from the trivial line without changing the rank.

## Multiplication comes from tensor products

We also know how to multiply bundles: take a tensor product. A fiber of E tensor F has dimension rank E times rank F. Tensor product distributes over direct sum, so it extends to products of virtual classes. K zero is therefore not only an additive group but a ring. The trivial complex line is the multiplicative identity.

For the Möbius real line over a circle, tensoring the line with itself gives a trivial real line. This hints at torsion-like multiplicative behavior in real K-theory. We focus on complex K-theory first; its periodicity is simpler. The underlying theme remains the same: addition records direct sum, while multiplication records tensor product.

## Why an index wants this language

An elliptic operator between spaces of sections has a finite-dimensional kernel and cokernel, despite acting between infinite-dimensional function spaces. For one operator, the analytic index is dimension kernel minus dimension cokernel. In a family of operators, neither kernel nor cokernel need form a vector bundle because their dimensions can jump. After finite-dimensional stabilization, however, their formal difference defines a class in K zero of the parameter space.

When the parameter space is a point, we recover the familiar integer index. When it has loops or surfaces, the K class may contain information not captured by any list of integers. This is why virtual bundles are not just a convenient abstraction: they preserve geometry that dimensions alone forget.

The key moves are now visible. Begin with actual bundles and direct sums. Allow formal differences, while respecting stable equivalence. Remember rank separately from twisting. Add tensor products to obtain a ring. These steps turn vector-bundle geometry into an algebra suited to families and index problems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For compact Hausdorff X, let `Vect_C(X)` be the commutative monoid of isomorphism classes of finite-rank complex bundles under direct sum. Its Grothendieck group `K^0(X)` is generated by `[E]` with relations `[E⊕F]=[E]+[F]`. An equality `[E]-[F]=[E']-[F']` holds precisely when some auxiliary bundle `G` makes `E⊕F'⊕G ≅ E'⊕F⊕G`. Because bundles are summands of trivial bundles on compact Hausdorff X, this can be expressed using sufficiently large trivial stabilizations.

The rank homomorphism `K^0(X)→H^0(X;Z)` is locally constant. On connected based X, `\widetilde K^0(X)=ker(K^0(X)→K^0(pt))`, and `K^0(X)≈Z⊕\widetilde K^0(X)` by restriction and pullback. Tensor products supply the ring product.

### Exercises with answers

1. For E of rank 4 and F of rank 6, what is the rank of `[E]-[F]`? **Answer:** minus two, although this is not an actual negative-dimensional bundle.
2. Why is `K^0(pt)=Z`? **Answer:** bundles over a point are classified by nonnegative integer dimension; group completion adds formal additive inverses.
3. If E is nontrivial but `E⊕F` is trivial, must E be trivial? **Answer:** no; being a summand of a trivial bundle is weaker than being trivial.
4. What does multiplication of `[E]` and `[F]` represent? **Answer:** the tensor product class `[E⊗F]`.

### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Chapters 1–2.
- [Topological K-theory](https://en.wikipedia.org/wiki/Topological_K-theory); [Grothendieck group](https://en.wikipedia.org/wiki/Grothendieck_group).
