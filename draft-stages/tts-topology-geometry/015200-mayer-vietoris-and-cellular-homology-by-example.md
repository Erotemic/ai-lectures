# 015200 — Calculating Homology of Circles, Spheres, and Tori

**Track:** Topology and Geometry. **Background:** chain complexes, cycles and boundaries, exact sequences. **Central question:** when a theorem says we can calculate by gluing, what does a complete calculation look like?

<!-- BEGIN SPOKEN LECTURE -->

# Calculating Homology of Circles, Spheres, and Tori

Saying that homology detects holes is helpful for intuition, but not yet a method. How do we find the homology of a space that has no convenient global coordinates? We can cover it with simpler regions, or build it by attaching cells. Both techniques turn a complicated global question into a few maps between familiar groups.

We will calculate the first homology of a circle, the top-dimensional homology of a sphere, and the homology of a torus. The purpose is not to memorize three answers. It is to understand why those answers follow from exactness and boundary maps.

## Cutting a circle into two easy regions

Cover a circle with two open arcs, each slightly longer than half the circumference. Each individual arc can be continuously shrunk to a point. Their intersection, however, consists of two disconnected short arcs. This is the subtlety. The pieces are individually simple, but the overlap has two connected components.

The Mayer–Vietoris sequence relates the homology of the overlap, the two pieces, and their union. In the part dealing with first homology, the connecting map goes from loops in the whole circle to reduced zero-dimensional homology of the overlap. Reduced zero-dimensional homology records one independent difference between the overlap's two components.

A loop going all the way around the circle crosses from one overlapping component to the other in a way that cannot be resolved inside a single arc. The connecting homomorphism records that difference. Since both arcs have no first homology, the relevant exact sequence identifies the circle's first homology with one copy of the integers.

Notice how the global loop was detected by an overlap consisting of disconnected pieces. Local triviality does not force global triviality; the gluing carries information.

## Build a sphere out of two disks

Now take a two-dimensional sphere and cover it by a slightly enlarged northern disk and southern disk. Their intersection is a thick band around the equator, which retracts onto a circle. Each disk is contractible. Just as before, Mayer–Vietoris transfers a homology class from the overlap to the union, but now in one higher dimension.

The equatorial circle is the boundary between north and south. Think of the upper and lower hemispheres with opposite induced boundary orientations. Their common equator cancels when the hemispheres are added to form a closed sphere. That gives a two-cycle with no boundary.

Exactness tells us that its class generates the second homology group of the sphere. In integers, the answer is one independent two-dimensional class. This is the algebraic expression of the sphere's fundamental oriented surface.

There is a pattern here. The n-dimensional sphere can be cut into two contractible pieces whose overlap retracts onto the sphere of one dimension less. The same exact-sequence argument shifts the nontrivial reduced homology up by one degree. Inductively, the n-sphere has reduced homology equal to the integers in degree n and zero in other degrees.

## A torus by attaching a square

For the torus, a cell structure is the shorter calculation. Draw a square and identify opposite edges with matching directions. The four corners become a single vertex. There are two distinct one-cells: one horizontal loop and one vertical loop. The square's interior is a single two-cell.

The two one-cells have zero boundary, because each begins and ends at the same vertex. What is the boundary of the two-cell? Read around the square. The attaching word is: horizontal, vertical, reverse horizontal, reverse vertical. It is a commutator.

In a fundamental group, a commutator carries information. But the cellular boundary map counts signed occurrences of each one-cell in an abelian group. Horizontal appears once positively and once negatively. The same happens for vertical. Thus the cellular boundary of the two-cell is zero.

The first homology therefore has two integer generators: the horizontal and vertical loops. The second homology has one integer generator, coming from the oriented square whose edges cancel. Zero-dimensional homology is also one copy of the integers because the torus is connected.

The Betti numbers of a torus are consequently one, two, one, and its Euler characteristic is one minus two plus one, which is zero. That is consistent with Gauss–Bonnet for a flat torus, whose Gaussian curvature can vanish everywhere.

## When coefficients change the answer

The same cell structure may be analyzed with integer, rational, or finite-field coefficients. For the torus just considered, the free ranks behave predictably. For the projective plane, the coefficient choice is more dramatic. The two-cell attaches with degree two, so its boundary map is multiplication by two. Over the integers, the first homology is integers modulo two. Over the real numbers, multiplication by two is invertible and that first homology vanishes.

This explains why de Rham cohomology, which uses real-valued forms, cannot detect every integral torsion class. The smoothness of a space does not remove the distinction between integer and real invariants.

## The role of exactness and functoriality

Mayer–Vietoris is more than a collection of shortcuts. It describes how cycles in the overlap become cycles or boundaries in the union. The maps matter as much as the groups. Two gluing problems can use pieces with identical homology groups but attach them by different maps, producing different global spaces.

Likewise, a cellular calculation requires the degree of each attaching map. Counting how many cells exist is not enough. The relative signs and winding numbers determine the boundary maps, and the boundary maps determine homology.

Later we will pair these cycles with differential forms. A closed one-form integrated around either torus generator measures its cohomology class. A top-degree form integrated over the oriented surface measures the two-dimensional class. Those pairings connect the combinatorial calculation here to the analytic language of de Rham and Hodge theory.

The practical method is now clear: choose simple pieces, write the actual maps, compute kernels and images, and only then name the resulting groups. This is the difference between recognizing a hole in a drawing and proving what the topology contains.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(S^1=U\cup V\) with \(U,V\) contractible and \(U\cap V\) consisting of two contractible components, reduced Mayer–Vietoris yields \(\tilde H_1(S^1)\cong\tilde H_0(U\cap V)\cong\mathbf Z\). For \(S^n\), \(n\ge2\), hemispherical covers with \(U\cap V\simeq S^{n-1}\) yield \(\tilde H_k(S^n)\cong\tilde H_{k-1}(S^{n-1})\), so \(\tilde H_k(S^n;\mathbf Z)=\mathbf Z\) if \(k=n\) and zero otherwise.

For \(T^2\), a CW structure has \(C_2=\mathbf Z\), \(C_1=\mathbf Z a\oplus\mathbf Z b\), \(C_0=\mathbf Z\), \(\partial_1=0\), and \(\partial_2=0\), since the attaching word \(aba^{-1}b^{-1}\) has exponent sum zero in each generator. Consequently \(H_0=\mathbf Z\), \(H_1=\mathbf Z^2\), \(H_2=\mathbf Z\); \(\chi(T^2)=1-2+1=0\).

For \(\mathbf{RP}^2\), \(\partial_2:\mathbf Z\to\mathbf Z\) is multiplication by two, yielding \(H_1(\mathbf{RP}^2;\mathbf Z)=\mathbf Z/2\) but \(H_1(\mathbf{RP}^2;\mathbf R)=0\). These computations concern ordinary singular/cellular homology; de Rham cohomology is over \(\mathbf R\).

### Exercises with answers

1. **Overlap.** Why is \(\tilde H_0(U\cap V)\) a single copy of \(\mathbf Z\) for the two-arc cover of \(S^1\)? **Answer:** Two components give ordinary \(H_0\cong\mathbf Z^2\), and reduced \(H_0\) removes one diagonal copy.
2. **Sphere.** Compute \(\tilde H_2(S^2)\) from the overlap of two disks. **Answer:** It is \(\tilde H_1(S^1)\cong\mathbf Z\).
3. **Torus.** What happens to the boundary of the square after edge identification? **Answer:** Each one-cell occurs with opposite signs, so the cellular boundary is zero.
4. **Coefficient test.** Compute \(\mathbf Z/2\otimes\mathbf R\). **Answer:** Zero, consistent with disappearance of first homology torsion over real coefficients.

### Sources and further reading

- Allen Hatcher, [Algebraic Topology, Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), cellular homology and Mayer–Vietoris.
- Allen Hatcher, [Algebraic Topology, complete volume](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
- Overviews: [Mayer–Vietoris sequence](https://en.wikipedia.org/wiki/Mayer%E2%80%93Vietoris_sequence), [Cellular homology](https://en.wikipedia.org/wiki/Cellular_homology).
