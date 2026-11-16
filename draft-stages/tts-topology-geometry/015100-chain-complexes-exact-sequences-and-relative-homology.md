# 015100 — Chain Complexes and Exact Sequences: How Topology Becomes Algebra

**Track:** Topology and Geometry. **Background:** integers, kernels and images, the idea of homology. **Central question:** how can a drawing of holes produce calculations that can be checked line by line?

<!-- BEGIN SPOKEN LECTURE -->

# Chain Complexes and Exact Sequences: How Topology Becomes Algebra

A circle has one independent loop. A filled disk does not. A sphere encloses a two-dimensional cycle, while a projective plane has a different kind of one-dimensional obstruction that disappears if counted twice. These statements sound geometric. To prove them systematically, we convert shapes into algebraic data.

The basic machine is a chain complex. Its ingredients are groups of formal pieces and maps that describe their boundaries. The same algebra will later appear in de Rham cohomology, elliptic complexes, Floer homology, and gauge-theoretic deformation theory. Learning to compute with it now pays off throughout advanced geometry.

## Build shapes from pieces

Imagine a triangle. Its vertices are zero-dimensional pieces, its edges are one-dimensional pieces, and its filled interior is a two-dimensional piece. Each edge has a signed boundary: the terminal vertex minus the initial vertex. The oriented triangular face has a signed sum of its three edges as boundary.

If we take the boundary of that boundary, the vertices cancel in pairs. This is not a coincidence peculiar to triangles. The boundary of an oriented boundary is always zero. In algebraic language, consecutive boundary maps compose to zero.

For a space made of many cells or simplices, form an integer combination of pieces of each dimension. The collection of such combinations is a chain group. The boundary operator tells us how those pieces meet. An expression with zero boundary is a cycle. A cycle that is itself the boundary of a higher-dimensional chain is called a boundary. Homology takes cycles and identifies those that differ by boundaries.

This quotient is the heart of the construction. It does not count every closed path separately. It counts the closed paths that cannot be filled using the pieces available in the space.

## Start with a circle

A circle can be built as a single vertex and a single edge whose two ends are attached to that vertex. The edge's boundary is the vertex minus itself, so the boundary map is zero. The edge is a cycle. No two-dimensional cell is present to make it a boundary.

Thus the first homology group is the integers. A loop can wrap once, twice, or negatively around the circle; those wrapping numbers do not disappear under continuous deformation. The zero-dimensional homology group is also the integers because the circle has one connected component.

Now fill the circle with a disk. A two-dimensional cell has appeared, with its boundary attached around the circle once. The original loop is now the boundary of the disk's face. Its class in first homology vanishes. Adding one cell has killed a hole.

The fact that these two spaces differ is now encoded in one boundary map, not in a visual judgment.

## A space with a cycle of finite order

The real projective plane is built by identifying opposite points of a disk's boundary. It has a cell structure with one vertex, one one-cell, and one two-cell. The crucial difference from the ordinary disk is that the attaching map of the two-cell travels twice around the one-cell, as seen in the cellular boundary map.

The resulting first homology is the integers modulo two. There is a nontrivial loop class, but taking it twice gives a boundary. This is a form of torsion. If we had used only ordinary real-valued differential forms and de Rham cohomology, this two-torsion information would disappear. Integer homology remembers something that real cohomology cannot.

That difference becomes important in bundle theory, spin structures, and characteristic classes. Not all topological data can be detected by integrating real differential forms.

## Exactness explains what one map cannot see

A sequence of groups and maps is called exact at a group when every element sent to zero by the next map comes from the previous group. The image of one map equals the kernel of the next.

It is useful to say this verbally. Exactness means that all failures of injectivity have already been explained by the preceding stage. A long exact sequence passes information between related topological spaces, keeping track of which cycles survive, which become boundaries, and which newly appear.

Suppose a subspace A lies inside X. Relative chains identify chains entirely inside A with zero. The relative homology of the pair measures what remains when A is treated as already filled in. The resulting long exact sequence connects the homology of A, the homology of X, and the relative homology of the pair.

Consider a disk and its boundary circle. The disk has no first-dimensional hole, but the pair consisting of the disk and its boundary has a relative two-dimensional class: the disk's interior, whose boundary lies in the designated subspace. The connecting map sends that relative class to the loop around the boundary circle. It is an isomorphism between two copies of the integers.

The map is not an abstract trick. It literally records the boundary of the relative two-dimensional object. Exactness then accounts for why this boundary loop is nontrivial on the circle but trivial when viewed inside the filled disk.

## Why the algebra generalizes

A chain complex need not be constructed from a triangulated picture. In de Rham theory, the objects are differential forms and the maps are exterior derivatives. In elliptic theory, a carefully chosen sequence of differential operators may form a complex. In Floer theory, the generators may be critical points or periodic trajectories, and the differential counts connecting solutions to differential equations.

In all these settings, the key proof obligation is the same: composing two consecutive differentials gives zero. Then cycles modulo boundaries make sense. Proving that a proposed differential really squares to zero can be one of the hardest parts of a new theory. But after that proof, familiar ideas such as exact sequences and maps induced by geometric constructions become available.

The geometry can be elaborate; the algebraic skeleton is stable. When an advanced lecture introduces a new cohomology group, ask four questions: what are its generators, what is its differential, why does that differential square to zero, and what maps between complexes preserve that structure? Those questions will keep the definitions connected to something calculable.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A chain complex \((C_*,\partial)\) has homomorphisms \(\partial_n:C_n\to C_{n-1}\) with \(\partial_{n-1}\partial_n=0\). Its homology is \(H_n(C)=\ker\partial_n/\operatorname{im}\partial_{n+1}\). Exactness of \(A\overset f\longrightarrow B\overset g\longrightarrow C\) at \(B\) means \(\operatorname{im}f=\ker g\).

**Cellular models.** For \(S^1\), \(C_1=C_0=\mathbf Z\), \(\partial_1=0\), and \(C_2=0\), hence \(H_1(S^1)=\mathbf Z\). For \(D^2\), a CW structure with one zero-, one one-, and one two-cell attached by degree one has \(\partial_2=1\), so \(H_1(D^2)=0\). The usual minimal CW structure of \(\mathbf{RP}^2\) has \(C_0=C_1=C_2=\mathbf Z\), \(\partial_1=0\), \(\partial_2=2\); hence \(H_1(\mathbf{RP}^2;\mathbf Z)=\mathbf Z/2\), \(H_2=0\).

For a pair \((X,A)\), relative chains \(C_*(X,A)=C_*(X)/C_*(A)\) fit into a short exact sequence of complexes. Its connecting homomorphism gives the long exact sequence \(\cdots\to H_n(A)\to H_n(X)\to H_n(X,A)\overset\delta\to H_{n-1}(A)\to\cdots\). For \((D^2,S^1)\), \(H_2(D^2,S^1)=\mathbf Z\), and \(\delta:H_2(D^2,S^1)\to H_1(S^1)\) is an isomorphism, up to orientation sign.

### Exercises with answers

1. **Homology condition.** Why is \(\operatorname{im}\partial_{n+1}\subseteq\ker\partial_n\)? **Answer:** \(\partial_n\partial_{n+1}=0\).
2. **One missing face.** What happens to the class of a circular edge after a two-cell is attached with degree one? **Answer:** The edge becomes a boundary, so its first-homology class vanishes.
3. **Torsion.** Compute \(\ker(0:\mathbf Z\to\mathbf Z)/\operatorname{im}(2:\mathbf Z\to\mathbf Z)\). **Answer:** \(\mathbf Z/2\).
4. **Exact sequence.** Interpret the connecting map for a disk relative to its boundary. **Answer:** It takes the relative disk class to its oriented boundary loop.

### Sources and further reading

- Allen Hatcher, [Algebraic Topology, Chapter 2: Homology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html).
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Background overviews: [Chain complex](https://en.wikipedia.org/wiki/Chain_complex), [Long exact sequence](https://en.wikipedia.org/wiki/Exact_sequence#Long_exact_sequence).
