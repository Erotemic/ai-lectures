# 028000 — Quantizing the Sphere: Holomorphic Sections and Spin

**Track:** Topology and Geometry. **Background:** prequantum line bundles, complex projective space, holomorphic sections, and representation theory. **Central question:** how does a classical sphere lead to a finite-dimensional state space with precisely n plus one basis states?

<!-- BEGIN SPOKEN LECTURE -->

# A sphere has too many ordinary functions

A symplectic sphere admits a prequantum line bundle when its total area, divided by two pi times Planck's constant, is an integer n. That integer is the line bundle's first Chern number. But sections of a line bundle can vary in infinitely many ways. Prequantization by itself has not explained why a quantum spin system should have a finite number of states.

To reduce the state space, geometric quantization introduces a polarization. The basic idea is to use only half of the classical phase-space variables, in a sense made precise by integrable Lagrangian distributions. On a Kähler manifold, a holomorphic polarization gives a particularly concrete answer: choose holomorphic sections of the prequantum line bundle.

The two-sphere is also the complex projective line. Its points can be represented by nonzero pairs of complex coordinates, with pairs identified when one is a nonzero complex multiple of the other. The line bundle O of n over this space is our central example.

# Counting holomorphic sections

For nonnegative n, holomorphic sections of O of n correspond to homogeneous polynomials of degree n in two complex variables. This is a theorem about projective space, but the counting is elementary once the correspondence is known.

How many monomials have total degree n? They are x to the n, x to the n minus one times y, and so on, ending with y to the n. There are n plus one of them. Each is linearly independent, and every homogeneous polynomial of degree n is their linear combination. Therefore the space of holomorphic sections has complex dimension n plus one.

If n equals zero, the space is one-dimensional: constants. If n equals one, the sections are linear polynomials in two variables, so the space is two-dimensional. If n equals two, the sections are quadratic polynomials and form a three-dimensional space.

The pattern now has a geometric explanation. Total symplectic area controls the line bundle's Chern number. The line bundle's degree controls the number of holomorphic sections. The quantum Hilbert space dimension is therefore tied to the integral geometry of the classical sphere.

# Where spin enters

Rotations of the sphere are described by the group SO three. A closely related group, SU two, is its double cover. SU two acts naturally on pairs of complex coordinates, and therefore on homogeneous polynomials in those coordinates. The degree-n polynomial space is the nth symmetric power of the fundamental two-dimensional complex representation.

That representation is irreducible and has dimension n plus one. In the standard physics convention, it is the spin-j representation with j equal to n over two. Thus n equals one gives spin one-half with two states, n equals two gives spin one with three states, and n equals three gives spin three-halves with four states.

We must be careful with the interpretation. The classical sphere here is not literally the configuration space of a tiny rigid ball. It is a coadjoint orbit carrying a symplectic form. Its group action and moment map encode classical angular momentum. Quantizing that orbit yields an irreducible representation of SU two.

This is a special case of a broad bridge between symplectic geometry and representation theory. Many finite-dimensional representations of compact Lie groups can be obtained from geometric data on appropriate orbits. The point is not only that we recover the right dimensions, but that the group action on the states comes from the action on the underlying geometry.

# Why a polarization changes the answer

Without a polarization, we might try to use all square-integrable prequantum sections. That space is much larger than the n-plus-one-dimensional space of holomorphic sections. The holomorphic condition is a differential restriction. It selects sections compatible with the complex structure and eliminates most of the freely varying functions.

On the projective line this restriction is especially transparent because all holomorphic sections can be described by finite-degree polynomials. On a general compact Kähler manifold, a similar construction uses the space of global holomorphic sections of a positive line bundle. Its dimension may be computed using Riemann–Roch and vanishing theorems, subjects already developed in the Algebra track.

So there are two independent ingredients. The integral symplectic form permits a line bundle in the first place. The polarization selects a subspace of sections. Neither step should be silently replaced by the other.

# The half-form qualification

Some geometric quantization constructions include a metaplectic correction, often called a half-form correction. This can shift which classical symplectic form corresponds to a given representation, and it changes some counting formulas. For the uncorrected holomorphic quantization of O of n on the projective line, the dimension is exactly n plus one. That is the convention we are using here.

A different correction convention may refer to a sphere with a shifted symplectic area when describing the same spin representation. These are not contradictory calculations when the geometric input and the correction are stated correctly. Trouble arises when formulas from different conventions are mixed without notice.

# A useful test of the construction

Try replacing n by a noninteger. There is no honest holomorphic line bundle O of that nonintegral degree on the projective line. So the polynomial construction cannot even begin. This is the global integrality condition reappearing in a simple algebraic form.

Next try n negative. In the same holomorphic polarization, O of a negative integer has no nonzero holomorphic sections. That is another sign that the orientation of the symplectic structure and choice of holomorphic line bundle matter. A negative degree with an incompatible polarization does not produce a state space by simply taking a negative number of monomials.

Finally, consider n large. The state-space dimension grows linearly with the normalized area of the sphere. More sophisticated semiclassical results say that dimensions of quantization spaces for higher-dimensional compact Kähler manifolds have leading terms controlled by symplectic volume. Our sphere calculation is the simplest example of that geometry-to-dimension relationship.

We have now built a complete example of quantization: integral symplectic area, a prequantum bundle, a holomorphic polarization, a finite-dimensional section space, and a symmetry representation. The same ingredients link topology, algebraic geometry, and quantum mechanics. They also show why geometric quantization is richer than simply replacing classical coordinates with noncommuting symbols.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `CP^1` carry its standard complex structure, and choose a symplectic form with prequantum degree `n>=0`. The uncorrected Kähler-polarized state space is
\[
\mathcal H_n=H^0(\mathbb{CP}^1,\mathcal O(n))
\cong\operatorname{Sym}^n((\mathbb C^2)^*),
\qquad\dim_{\mathbb C}\mathcal H_n=n+1.
\]
A basis is `z_0^n, z_0^{n-1}z_1, ..., z_1^n`; these are degree-n homogeneous polynomials in homogeneous coordinates. For `n<0`, `H^0(CP^1,O(n))=0` in the chosen holomorphic polarization.

The group SU(2) acts on `C^2`; its symmetric-power representation on degree-n homogeneous polynomials is irreducible of highest weight n and corresponds to spin `j=n/2`, with dimension `2j+1=n+1`. SO(3) acts projectively on half-integer-spin representations, whereas SU(2) acts linearly; distinguish the groups.

The Hirzebruch–Riemann–Roch expression on a curve is `chi(L)=deg L+1-g`. On `CP^1`, `g=0` and for `n>=0`, `H^1(O(n))=0`, so `h^0(O(n))=n+1`. A half-form/metaplectic correction may shift the relation between the symplectic area, the chosen bundle, and a representation. All formulas above use **uncorrected** holomorphic quantization.

### Exercises with answers

1. How many holomorphic sections does `O(4)` have on `CP^1`? **Answer:** five, represented by the five degree-four monomials in two variables.
2. Which spin corresponds to `O(3)` under the chosen convention? **Answer:** spin three-halves, with four states.
3. Does `O(-1)` have any nonzero holomorphic sections on `CP^1`? **Answer:** no.
4. Why do rotations naturally act on the section space? **Answer:** SU(2) acts on the homogeneous coordinates, preserving the degree-n polynomial subspace.

### Reading and source notes

- [Woodhouse, Geometric Quantization](https://doi.org/10.1093/oso/9780198536734.001.0001), holomorphic polarizations, Kähler quantization and the sphere.
- [Guillemin and Sternberg, Symplectic Techniques in Physics](https://mitpressbookstore.mit.edu/book/9780521389907), coadjoint orbits, moment maps and representation theory.
- [Fulton and Harris, Representation Theory: A First Course](https://doi.org/10.1007/978-1-4612-0979-9), symmetric powers of SU(2) and highest-weight representations.
