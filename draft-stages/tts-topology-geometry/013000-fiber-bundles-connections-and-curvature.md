# 013000 — Fiber Bundles, Connections, and Curvature

**Track:** Topology and Geometry. **Background:** quotient spaces, smooth manifolds, tangent spaces, differential forms. **Central question:** how can a family of vector spaces twist globally, and what extra structure lets us compare vectors at different points?

<!-- BEGIN SPOKEN LECTURE -->

# Fiber Bundles, Connections, and Curvature

In elementary geometry, a vector can be drawn as an arrow in a fixed plane. We can move it from one point to another without changing its components, because every tangent space of that plane has been identified with the same vector space. On a curved surface, that identification is no longer automatic. Vectors based at different points live in different tangent spaces. Even on a topologically simple space, a family of vector spaces can be arranged with a twist.

Fiber bundles provide a language for the family itself. Connections tell us how to compare neighboring fibers. Curvature measures the failure of that comparison to be independent of the route taken.

## A bundle looks like a product nearby

A fiber bundle is a space E equipped with a projection onto a base space B. Above a point b in the base sits the fiber: all points of E that project to b. The key local property is that around each point of the base, the bundle looks like a product of a neighborhood with a fixed typical fiber.

For a vector bundle, the fibers are vector spaces of a fixed dimension, and the local product maps are linear on each fiber. The tangent bundle of a smooth manifold is the central example. At each point, its fiber is the tangent space. When we collect all tangent vectors at all points, we obtain a new geometric space, with a projection that remembers which point each vector belongs to.

A local trivialization supplies coordinates for this construction. We choose a basis of vectors over a small open set and represent each vector by its coefficients in that basis. But bases chosen on overlapping neighborhoods need not agree. Their change-of-basis functions, called transition functions, encode how the bundle fits together globally.

## The Möbius strip: local simplicity, global twist

Take a rectangle and identify its two ends after giving one end a half-turn. The resulting Möbius strip is a real line bundle over a circle if we regard each short cross-section as a one-dimensional vector space. Locally there is no twist: over a short arc it is just an arc times a line. But if you follow the local choice of positive direction around the whole circle, it returns reversed.

Compare the cylinder. It is also a line bundle over a circle, but it is globally a product. The cylinder has a continuous nowhere-zero section: choose the same positive vector in every fiber. The Möbius line bundle does not. If we represent such a section by a nonzero real function along one traversal, the twist would require its final value to be the negative of its starting value. By continuity, a real function cannot do that without passing through zero.

This is a concrete obstruction to global triviality. Every local piece has a basis, yet no single continuous nonzero basis vector exists everywhere. It is why an object can be locally ordinary and globally different.

## Sections and the need for comparison

A section of a vector bundle assigns one vector in the fiber over each base point. A vector field on a smooth manifold is a section of its tangent bundle. Suppose such a section varies from point to point. We want to differentiate it.

Ordinary differentiation subtracts vector values at nearby points. But those vectors lie in different fibers, so subtraction is not defined until we choose a way to identify them. A connection supplies the missing rule.

For a smooth vector bundle, a covariant derivative maps a vector field X and a section s to another section, written nabla in the direction X of s. It is linear in X over smooth functions, linear in s over constants, and obeys a Leibniz rule: differentiating f times s gives the directional derivative of f times s, plus f times the covariant derivative of s. That extra term makes the construction compatible with ordinary calculus.

In a local frame, the rule looks like differentiation plus a matrix-valued one-form A. The ordinary derivative differentiates the coordinate components; A corrects for the changing local frame. Choosing a different frame changes the matrix A, even though the connection itself is geometric.

## Parallel transport

Once a connection is specified, we can transport a vector along a smooth path by requiring its covariant derivative along that path to vanish. This is parallel transport. Given a starting vector and suitable regularity, a linear differential equation determines its transported value.

Parallel transport along two different paths with the same endpoints may produce different results. That phenomenon is called holonomy. If you transport a tangent vector around a loop on a curved surface, the final vector can be rotated relative to the initial one. The comparison is not the familiar rotation of an arrow against some external coordinate axes; it is a property of the connection used to identify tangent spaces.

Parallel transport is additional structure. A bare topological vector bundle does not choose a preferred connection, and even a trivial bundle can carry connections with nonzero curvature.

## Curvature is the obstruction to commuting derivatives

A connection lets us differentiate a section along two vector fields X and Y. We can take the derivative along X and then Y, or reverse the order. The difference is not generally zero. After correcting for the Lie bracket of the vector fields, the resulting operator is the curvature of the connection.

In a local matrix frame, if the connection is written as d plus A, its curvature form is dA plus A wedge A. For a line bundle, the matrix multiplication issue disappears, and the formula reduces to dA. The curvature is geometric even though A changes with the choice of frame.

Consider a trivial complex line bundle over the plane. Give it the connection d plus i times x dy, where i is the imaginary unit. Its curvature is i times dx wedge dy. Parallel transport once around a counterclockwise rectangle changes a unit complex vector by the phase obtained from the negative exponential of i times the enclosed area. Two routes can differ even though the underlying bundle is just a product.

This illustrates an important distinction: twisting of the bundle is topological; curvature belongs to a chosen connection. They interact, but they are not the same data.

## Flat does not always mean globally trivial transport

A connection with zero curvature is called flat. On a sufficiently small simply connected neighborhood, flatness allows path-independent parallel transport. But global topology still matters. On a circle, a flat connection can have nontrivial holonomy around a full loop. Local curvature may vanish, while the global return map is nontrivial.

This mirrors the themes of topology we have already studied. Local exactness of a differential form need not imply global exactness. A local trivialization need not produce a global trivialization. In both cases, understanding how local choices fit together reveals the global obstruction.

Fiber bundles, connections, and curvature are therefore different layers of a single story. The bundle says what vector space lives at each point. The connection says how vectors are compared as we move. The curvature says what that comparison does around small loops. The same ideas appear in differential geometry, gauge theory, and modern topology, but their mathematical content begins with these precise distinctions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A rank-\(r\) smooth vector bundle \(\pi:E\to M\) is locally isomorphic, fiberwise linearly, to \(U\times\mathbb F^r\). On overlapping trivializations, frames differ by smooth transition maps \(g_{\alpha\beta}:U_\alpha\cap U_\beta\to\operatorname{GL}(r,\mathbb F)\) satisfying cocycle relations.

A connection \(\nabla\) acts on smooth sections and obeys \(\nabla_X(fs)=X(f)s+f\nabla_X s\). In a local frame, \(\nabla=d+A\). With frame transformation \(e'=eg\),
\[A'=g^{-1}Ag+g^{-1}dg,\qquad F_\nabla=dA+A\wedge A,\qquad F'=g^{-1}Fg.\]
In invariant form,
\[F_\nabla(X,Y)s=(\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]})s.\]
For a complex line bundle over \(\mathbb R^2\) with \(A=i x\,dy\), \(F=i\,dx\wedge dy\). On a counterclockwise rectangle \(\gamma\) enclosing area \(ab\), parallel transport has scalar holonomy \(e^{-\oint_\gamma A}=e^{-iab}\) (with the stated sign convention).

**Möbius example:** the real line bundle \(([0,2\pi]\times\mathbb R)/((0,t)\sim(2\pi,-t))\to S^1\) is locally trivial but admits no everywhere-nonzero continuous section. Such a section would correspond to a continuous \(f\) on the interval with \(f(2\pi)=-f(0)\) and no zeros, contradicting the intermediate value theorem.

### Exercises with answers

1. Can a trivial line bundle have a connection with nonzero curvature? **Yes:** \(A=i x\,dy\) above is an explicit example.
2. Is \(A\) invariant under change of frame? **No:** it changes by \(g^{-1}Ag+g^{-1}dg\), while curvature transforms by conjugation.
3. Does curvature zero imply trivial holonomy around every global loop? **No:** a flat connection on a nonsimply-connected base can have nontrivial global holonomy.
4. What is a section of the tangent bundle? **Answer:** a vector field, assigning a tangent vector to each point.

### Reading and source notes

- Allen Hatcher, [*Vector Bundles & K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), bundles, transition functions and global nontriviality.
- John Baez and Javier P. Muniain, [*Gauge Fields, Knots and Gravity*](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), vector-bundle connections and curvature.
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), smooth bundle and connection prerequisites.
