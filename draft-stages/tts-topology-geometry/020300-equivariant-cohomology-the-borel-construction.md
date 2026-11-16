# 020300 — Equivariant Cohomology: The Space That Remembers Its Symmetry

**Track:** Topology and Geometry. **Background:** ordinary cohomology, quotient spaces, classifying spaces in outline. **Central question:** why is cohomology of the ordinary quotient insufficient when fixed points exist?

<!-- BEGIN SPOKEN LECTURE -->

# Equivariant Cohomology: The Space That Remembers Its Symmetry

Imagine two ways for a circle to act on a sphere. In one, the circle does nothing: every point is fixed. In the other, it rotates the sphere around an axis: only the poles are fixed. The underlying sphere is the same in both cases, so its ordinary cohomology cannot distinguish these actions. An ordinary quotient remembers some of the difference, but it has another weakness: at a fixed point, an entire group collapses to the same location.

Equivariant cohomology is designed to retain the topology of the space together with how the symmetry acts on it. To build it, we first need a simple but powerful construction called a homotopy quotient.

## Why the ordinary quotient loses information

For a group G acting on a space M, the orbit space M divided by G identifies points that can be moved into each other. If the action is free and well behaved, this quotient is often a useful geometric space. But if there are fixed points, the quotient can hide stabilizers: a point fixed by the whole group and a point with no nontrivial stabilizer both become points of the orbit space.

The most extreme example is the action of a circle on a single point. Its ordinary quotient is still one point. If we take ordinary cohomology of that quotient, we see only the constants. Yet the group action has retained an entire circle's worth of symmetry at that point. A theory intended to remember stabilizers should not simply discard it.

## Replace orbits with homotopy orbits

Introduce a contractible space called E G on which G acts freely. Form the product E G times M, with G acting diagonally, and divide by G. The result is the Borel construction, also called the homotopy quotient of M by G.

It looks elaborate, but it solves exactly the problem we encountered. By inserting E G, we replace the original action with a free diagonal action before taking the quotient. The ordinary cohomology of this new space is, by definition, Borel equivariant cohomology of M.

The resulting space fibers over B G, the quotient E G divided by G. Its fiber is M. The base B G records the symmetry group, while the fiber records the original space. The manner in which they fit together records how the group acts.

## Calculate the action on a point

For the circle group, its classifying space B S one can be modeled by infinite complex projective space. Its cohomology with real coefficients is a polynomial algebra in one variable u of degree two.

Therefore equivariant cohomology of a point under the circle group is not just the real numbers. It is the full polynomial ring in u. The variable is not an arbitrary trick. It is the first Chern class of the universal complex line bundle over the classifying space, and it records the circle's geometry in cohomological degree two.

The polynomial degrees continue indefinitely even though the original space consists of one point. There is no paradox: we are taking cohomology of the homotopy quotient, which contains the topology of B S one, not the original point by itself.

## A free action gives a simpler result

Let the circle act on itself by multiplication. Every orbit is the entire circle, and the action is free. Its ordinary orbit space is one point. The homotopy quotient is homotopy equivalent to the same point, so its equivariant cohomology is simply the real numbers.

Compare that with the trivial action on a point, which gave a polynomial ring. In one example, no point has any nontrivial stabilizer; in the other, every point is fixed by the whole group. The difference is now visible algebraically.

More generally, when G acts freely and sufficiently nicely on M, the Borel construction is homotopy equivalent to M divided by G. Equivariant cohomology then agrees with ordinary cohomology of the quotient. This explains why the construction is an extension of quotient topology, not a replacement for it in every situation.

## What if the group acts trivially on a larger space?

When a circle acts trivially on M, the Borel construction becomes the product of M with B S one. With real coefficients and the usual finite-type assumptions, its cohomology is the ordinary cohomology of M tensored with the polynomial ring in u.

For a two-sphere with trivial action, we obtain two families of classes: constants and the sphere's degree-two generator, each multiplied by arbitrary powers of u. For rotation of the same sphere, the additive structure may look similar, but the way the classes multiply and restrict to the fixed points carries the action data.

The degree-two variable u is the bookkeeping device that eventually appears in localization denominators. Before dividing by anything, we need to understand why it is present and why its degree is two.

## Why fixed points will matter

Suppose a circle rotates a compact manifold and fixes isolated points. Near one fixed point, the group acts linearly on the tangent space, with integer rotation weights. Those weights are invisible to ordinary cohomology of the underlying manifold but visible in equivariant characteristic classes. When we later restrict an equivariant class to the fixed point, the answer is a polynomial in u whose coefficients remember those weights.

The localization theorem will allow us to recover a global integral from these weighted fixed-point restrictions after inverting u. That remarkable conclusion rests on a modest starting idea: when taking a quotient, do not throw away the symmetry group's topology. Build a space that remembers the group even at the points it leaves fixed.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a suitable G-space M, choose contractible free EG. Then

\[
M_G=EG\times_G M,\qquad H_G^*(M;R)=H^*(M_G;R),
\]

with a fibration `M→M_G→BG`. For `G=S¹`, `BG≈CP^∞`, and `H^*(BG;R)=R[u]`, `|u|=2`. When G acts trivially, `M_G≈M×BG` and over a field the Künneth formula gives `H_G^*(M)≈H^*(M)⊗R[u]` under standard hypotheses. When G acts freely and the action yields a well-behaved quotient, `M_G≈M/G` up to homotopy.

### Exercises with answers

1. What is `H_{S¹}^*(pt;R)`? **Answer:** `R[u]`, with u in degree two.
2. What is the equivariant cohomology of S¹ acting on itself freely by translation? **Answer:** R in degree zero and zero in positive degrees.
3. Why does ordinary cohomology of a sphere not distinguish trivial from rotational circle action? **Answer:** the underlying topological sphere is identical; the action is extra structure.
4. What information can restriction to a fixed point reveal? **Answer:** the circle weights on equivariant bundles and tangent representations.

### Sources and further reading

- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf), foundational exposition.
- [Equivariant cohomology](https://en.wikipedia.org/wiki/Equivariant_cohomology); [Classifying space](https://en.wikipedia.org/wiki/Classifying_space).
