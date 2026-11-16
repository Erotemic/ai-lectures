# 014000 — Tensor Products and Exterior Algebra: How Measurements Combine

**Track:** Linear Algebra from First Principles. **Background:** dual spaces, linear maps and bilinear forms. **Question:** how can we encode measurements that depend on several vectors, and why does alternating them describe area?

<!-- BEGIN SPOKEN LECTURE -->

# Tensor Products and Exterior Algebra: How Measurements Combine

A length measurement depends on one vector. An inner product depends on two. A determinant in three dimensions depends on three. Advanced geometry studies fields that assign such multilinear measurements at each point of a manifold. The algebraic machinery is called tensors, and its alternating part is exterior algebra. We can build the ideas from familiar operations rather than starting with index notation.

## A measurement of two vectors

A bilinear map takes a vector u from one space and a vector v from another and returns an output that depends linearly on each input separately. For example, from two coordinate vectors with components u one, u two and v one, v two, we can make four products: u one times v one, u one times v two, u two times v one, and u two times v two. Every bilinear scalar expression is a linear combination of those four products.

This suggests a construction. Instead of treating a bilinear map as something requiring two separate inputs, encode the pair of vectors in a single object u tensor v, with rules forcing linearity in each slot. A bilinear map can then be handled as an ordinary linear map out of the tensor product space. This is the universal property of the tensor product.

The symbol u tensor v represents a pure tensor. Sums of pure tensors make the general elements. Not every tensor can be expressed as one pure tensor: a general two-by-two matrix need not have rank one. This is important in applications because tensor decomposition can be a nontrivial mathematical or numerical problem.

If the spaces have dimensions m and n, their tensor product has dimension m times n. A basis is formed from every pair of basis elements, one from each space. For two-dimensional spaces, four such basis tensors appear. This explains the number of entries in a matrix of a bilinear form and the coordinate array for a rank-two tensor.

## Contravariant and covariant slots

A vector lives in a space V. A covector lives in its dual V star and evaluates vectors. A tensor can have slots that transform as vectors, as covectors, or both. A bilinear form on V is naturally an element of V star tensor V star in finite dimensions. A linear operator from V to V can be identified with an element of V tensor V star. These identifications explain why changing coordinates produces different index rules in different positions.

An abstract tensor does not depend on a chosen basis. Its coordinate array does, and the transformation law ensures that a complete contraction gives the same scalar in every chart. For example, a covector evaluating a vector is a contraction. The row and column components transform oppositely so their pairing remains unchanged.

## Antisymmetry means oriented area

Now consider two covectors alpha and beta. Form the alternating bilinear expression alpha of u times beta of v minus alpha of v times beta of u. This is alpha wedge beta evaluated on u and v. It changes sign when we exchange u and v, and vanishes when they point along the same line.

For the standard coordinate covectors d x and d y, the wedge d x wedge d y on vectors u and v is precisely the determinant of the matrix with columns u and v. It measures their signed parallelogram area. The wedge product is not just a symbol inserted between differential letters; it is an antisymmetrized tensor product that produces geometric quantities independent of coordinates.

For higher-degree alternating tensors, wedge products combine oriented measurements. If alpha is a one-form and beta a two-form, alpha wedge beta is a three-form. Swapping a p-form and a q-form introduces a sign of minus one to the power p times q. This graded sign rule makes differentials and Stokes' theorem work consistently.

At a point of an n-dimensional vector space, alternating k-forms are zero when k exceeds n, because we cannot supply more than n independent directions. The dimension of the space of k-forms is the number of ways to choose k basis directions from n, written n choose k. In particular, the top-degree alternating forms form a one-dimensional space. A nonzero top-degree form gives an orientation and a way to measure signed volume after a normalization is chosen.

## Why differential forms are tensors that can be integrated

On a smooth manifold, tangent spaces vary from point to point. A differential k-form assigns an alternating k-linear functional to each tangent space in a smooth way. A one-form can be integrated along a path because it evaluates each tangent velocity. A two-form can be integrated over a parameterized surface because it evaluates the two tangent directions induced by the surface coordinates. The wedge product combines forms to build higher-dimensional volume elements.

The exterior derivative is a further operation, depending on how a form varies from point to point. It raises degree by one and satisfies a graded product rule. A form is not the same as its exterior derivative; the latter captures how the original measurement changes across space. The generalized Stokes theorem relates integrating an exterior derivative over a region to integrating the original form over the boundary.

## One concrete pullback calculation

Let a coordinate transformation take parameters s, t to the plane by x equals two s and y equals s plus three t. The pullbacks of the coordinate one-forms are d x equals two d s and d y equals d s plus three d t. Wedge them. The d s wedge d s term vanishes, leaving six times d s wedge d t. The factor six is the determinant of the coordinate transformation. Exterior algebra has recovered the Jacobian formula from the transformation of one-forms.

This example is the bridge between linear algebra, multivariable calculus, and geometry. A change of variables in an integral is not a separate trick: it follows from how alternating multilinear measurements behave under linear maps.

Tensor products organize several-input linearity. Exterior products organize oriented measurements. Once these constructions are comfortable, coordinates in differential geometry stop looking like a maze of superscripts and subscripts, and start looking like a systematic way to keep track of which kinds of objects are being measured.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The tensor product \(V\otimes W\) represents bilinear maps: \(\mathrm{Bilin}(V\times W,Z)\cong\mathrm{Lin}(V\otimes W,Z)\). In finite dimensions, \(\dim(V\otimes W)=\dim(V)\dim(W)\) and \(\mathrm{Bil}(V\times V,\mathbb F)\cong V^*\otimes V^*\). Alternating k-tensors form \(\Lambda^kV^*\), of dimension \(\binom nk\) if \(n=\dim V\). For one-forms,
\[
(\alpha\wedge\beta)(u,v)=\alpha(u)\beta(v)-\alpha(v)\beta(u).
\]
In general \(\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha\) when degrees are \(p,q\). For \(F(s,t)=(2s,s+3t)\), \(F^*(dx\wedge dy)=d(2s)\wedge d(s+3t)=6\,ds\wedge dt\).

### Exercises with answers

1. What is the dimension of \(\mathbb R^2\otimes\mathbb R^3\)? **Answer:** six.
2. Evaluate \((dx\wedge dy)((1,2),(3,4))\). **Answer:** \(1\cdot4-3\cdot2=-2\).
3. Why does \(dx\wedge dx=0\)? **Answer:** a one-form wedged with itself is alternating and vanishes (over characteristic not two).
4. How many independent two-forms are there on a four-dimensional vector space? **Answer:** six.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), multilinear algebra and tensor products.
- Raoul Bott and Loring Tu, [Differential Forms in Algebraic Topology](https://doi.org/10.1007/978-1-4757-3951-0), exterior products and de Rham cohomology.
- [Exterior algebra](https://en.wikipedia.org/wiki/Exterior_algebra).
