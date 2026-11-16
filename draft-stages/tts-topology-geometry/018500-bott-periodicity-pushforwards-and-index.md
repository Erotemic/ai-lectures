# 018500 — Bott Periodicity and Index Pushforwards: Turning Symbols into Integers

**Track:** Topology and Geometry. **Background:** reduced K-theory of spheres, elliptic symbols, Chern character. **Central question:** why is the topological index of an elliptic operator a K-theoretic pushforward rather than a count of zeros?

<!-- BEGIN SPOKEN LECTURE -->

# Bott Periodicity and Index Pushforwards: Turning Symbols into Integers

We have built virtual bundles and computed one generator of reduced K-theory on the two-sphere. How does this help us understand a differential operator? The missing link has two parts. Bott periodicity tells us how K-theory behaves when two new spatial directions are introduced. A pushforward tells us how to turn a class defined over a geometric space into a class over a point or parameter space.

This lecture is about their meaning and one completely calculable example, rather than a proof of the full Atiyah–Singer theorem.

## The symbol knows which directions matter

Take a differential operator D acting on sections of a bundle over a compact manifold. Its principal symbol is a bundle map depending on a point x and a cotangent vector xi. For an elliptic operator, that map is invertible whenever xi is nonzero. This is a local, high-frequency condition. It says the only possible failure of invertibility is concentrated at the zero section of the cotangent bundle.

Because the symbol is invertible away from that section, it defines a class in K-theory with compact support on the cotangent bundle. It is not, in general, simply a class in K zero of the original manifold. The variable xi, representing the direction and frequency of oscillation, is essential to the construction.

The analytic index counts kernel minus cokernel. The topological index starts with this symbol class, transports it through K-theoretic constructions, and ends in the integers. The index theorem says the two integers agree.

## Why the plane acts like the two-sphere

The real plane becomes a sphere after adding one point at infinity. Compactly supported K-theory on the plane is therefore reduced K-theory of the two-sphere. Our class beta, built from the Hopf line minus a trivial line, generates this group.

There is a canonical Bott class on the plane; it is the K-theoretic orientation of a complex one-dimensional vector space. Multiplying a class by this Bott element and using the two additional real directions yields an isomorphism in compactly supported K-theory. This is Bott periodicity in a geometric form.

Its deeper implication is that complex K-theory repeats every two degrees. The periodicity is not obvious from the definition by bundles. Establishing it is one of the major theorems behind topological index theory.

## Push a class toward a point

Imagine integrating a differential form over a compact oriented fiber. The result is a form of lower degree on the base. A K-theoretic pushforward plays an analogous role. But ordinary orientation is not enough. Complex K-theory needs a K-orientation, supplied, for example, by a spin-C structure or by an almost-complex structure in appropriate geometric settings.

For an elliptic symbol over a compact manifold, embedding into a Euclidean space, using Thom classes and excision, and then Bott periodicity gives a topological index in the integers. This paragraph compresses a substantial construction. Its important warning is that different orientations yield different pushforwards; a pushforward is not defined automatically for any continuous map.

With families, the target is not necessarily a point. For a smooth proper family of spin-C manifolds over a base B, one pushes fiberwise and obtains a class in K zero of B. This is the topological counterpart of the index bundle of a family of Dirac operators.

## A worked complex curve

Take the complex projective line. Twist the Dolbeault operator by the holomorphic line bundle O of k, where k is an integer. Its analytic index equals the dimension of holomorphic sections minus the dimension of first sheaf cohomology.

For nonnegative k, global holomorphic sections correspond to homogeneous polynomials of degree k in two coordinates. There are k plus one independent monomials, and the first cohomology vanishes. So the index is k plus one. For negative k, the same formula still holds, although the kernel may be zero and the cokernel nonzero.

Now compute the topological expression. Let h be the positive degree-two generator of cohomology, normalized to integrate to one. The Chern character of O of k is one plus k h. The holomorphic tangent bundle of the projective line has first Chern class two h. In complex dimension one its Todd class is one plus h. Multiplying gives one plus k plus one times h, after discarding the degree-four term. Integrating the degree-two term gives k plus one.

This is a small Riemann–Roch theorem we can actually check. The fractional terms of Todd theory did not spoil integrality. They corrected the index to the right integer.

## What this example does not prove

The calculation verifies an index formula for one family of examples. It does not prove that all elliptic symbols have matching analytic and topological indices. Nor does it establish the families theorem, which may produce nonzero classes in higher-degree cohomology on the parameter base.

But it provides a map of the ideas. The principal symbol supplies a compactly supported K class. Bott periodicity makes Euclidean stabilization possible. A K-oriented pushforward turns the class into an index. The Chern character translates that pushforward into an integral with characteristic-class corrections.

The heavy index theorem is no longer a string of unfamiliar names. Each step has a distinct mathematical job, and we have verified the output in a case where both analysis and cohomology can be counted by hand.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For compact M, an elliptic symbol determines `[\sigma(D)]∈K_c^0(T^*M)`. The analytic index is `dim ker D - dim coker D`. The topological index uses an embedding, the K-theory Thom isomorphism and Bott periodicity to map that class to `K_c^0(R^{2N})≈Z`. For a spin-C family `π:X→B`, the K pushforward is `π_!:K^0(X)→K^0(B)` (with the required K-orientation and degree conventions). Its Chern character satisfies the relevant families Riemann–Roch relation.

For `X=CP¹`, write `h=c_1(O(1))`, `∫h=1`. Then

\[
\operatorname{ch}(O(k))=1+kh,\quad
\operatorname{Td}(TX)=1+\tfrac12 c_1(TX)=1+h,\quad
\chi(O(k))=\int_X (1+kh)(1+h)=k+1.
\]

The formula for `chi` holds for every integer k. For `k=-2`, `h^0=0`, `h^1=1`, and the index equals minus one. The explicit sheaf-cohomology count is developed later.

### Exercises with answers

1. Where does an elliptic principal symbol define a K class? **Answer:** in compactly supported K-theory of the cotangent bundle, because it is invertible off the zero section.
2. Why is `K_c^0(R²)` isomorphic to `\widetilde K^0(S²)`? **Answer:** the one-point compactification of R² is S².
3. Find `chi(O(2))` on CP¹. **Answer:** three.
4. Find `chi(O(-2))` and interpret its sign. **Answer:** minus one; the first cohomology has dimension one while holomorphic sections vanish.

### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), Bott periodicity and Thom constructions.
- [Atiyah–Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem); [Hirzebruch–Riemann–Roch theorem](https://en.wikipedia.org/wiki/Hirzebruch%E2%80%93Riemann%E2%80%93Roch_theorem).
