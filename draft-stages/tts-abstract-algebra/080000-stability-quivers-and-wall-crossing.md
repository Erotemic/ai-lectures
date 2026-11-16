# 080000 - Stability Conditions, Quiver Mutations, and Wall Crossing

**Track:** Abstract Algebra. **Background:** quiver representations, short exact sequences, derived categories, and Hall algebras. **Central question:** why can a representation become stable or unstable when only the notion of phase is varied?

<!-- BEGIN SPOKEN LECTURE -->

# A stable object depends on the question we ask

A representation of a quiver is a collection of vector spaces attached to vertices and linear maps attached to arrows. Whether that representation is indecomposable is an intrinsic algebraic question. Whether it is stable is different: stability depends on an additional choice of how to compare the phases of an object and its subobjects.

This distinction produces wall crossing. As the stability condition varies, a representation may stop being stable without changing its underlying vector spaces or arrow maps. The collection of stable objects can jump, and invariants that count stable objects may jump with it. The mathematics asks not merely where the jump occurs, but how to relate the counts on opposite sides of the wall.

A two-vertex quiver provides a complete example small enough to hold in mind. Put one arrow from vertex one to vertex two. Give each vertex a one-dimensional vector space and take the arrow map to be nonzero. Call the resulting representation E.

# The subobject that decides stability

There are two simple representations, one concentrated at the first vertex and one at the second. Because the arrow points from the first vertex to the second, E contains the simple object at the second vertex as a proper subrepresentation. It does not contain the simple at the first vertex as a proper subrepresentation: the nonzero arrow would leave its chosen target subspace.

Thus E sits in a short exact sequence with the second simple as subobject and the first simple as quotient. The sequence does not split. If the arrow were zero instead, the representation would be the direct sum of the two simples.

Now assign a complex number in the upper half-plane to the first simple and another to the second. This assignment is a central charge. Its argument defines a phase. For our fixed finite-length category, a stable object must have every proper nonzero subobject at strictly smaller phase than the object itself.

The only nontrivial proper subobject of E is the simple at vertex two. Therefore stability of E is decided by one inequality. All the apparent complexity of the definition collapses to a comparison of two angles.

# Walk across the wall explicitly

Give the first simple the central charge negative one plus i, and the second simple one plus i. The first phase is a hundred and thirty-five degrees; the second phase is forty-five degrees. The central charge of E is their sum, two i, whose phase is ninety degrees.

The only proper subobject has phase forty-five degrees, smaller than ninety. So E is stable.

Now reverse the two charges. The central charge of E remains two i, so its phase remains ninety degrees. But the phase of its subobject becomes a hundred and thirty-five degrees. That is larger than ninety, and E is unstable. The representation did not change. The ordering of the phases did.

At the wall, the two simple charges have the same argument. The extension object becomes semistable in the corresponding sense. The change is not a mysterious discontinuity in matrices. It is a change in which subobjects are allowed by the phase inequality.

# From one extension to a wall-crossing identity

For a two-vertex quiver there is only a small number of representations in a fixed small dimension, but Hall algebras can count how objects assemble by extensions across all dimensions. Their multiplication is organized around short exact sequences.

Changing the stability condition reorganizes which extension classes are stable. Wall-crossing identities express the same total category in different factorizations associated with the new order of phases. In refined settings, these factorizations involve quantum dilogarithms and noncommutative variables rather than ordinary sums of numerical counts.

It would be incorrect to infer a universal numerical jump from our two-vertex example alone. A Donaldson–Thomas invariant requires choices of category, stability, orientation or motivic refinement, and often finiteness and support conditions. The elementary phase comparison supplies the local mechanism, not the entire enumerative theory.

# Why quiver mutation enters

Cluster mutation changes the quiver seed by a combinatorial rule. In a two-vertex example with one arrow, mutation at one vertex reverses the arrow and replaces a cluster variable by a rational expression involving the two original variables.

In suitable derived or Calabi–Yau categorical settings, a mutation can be realized through changing the heart of a t-structure or through a related categorical operation. That is why wall crossing, cluster coordinates, and quiver mutation often occur together.

But the three are not synonyms. A wall of stability conditions concerns the phases of objects in a category. A cluster mutation is a rule on seed data. A categorical tilt changes the chosen abelian heart inside a derived category. Their compatibilities are theorems with hypotheses, not mere consequences of using the same quiver diagram.

# A geometry of choices

A space of stability conditions is divided by walls on which certain central charges align. Away from a wall, the list of stable objects of a fixed class can remain constant. Crossing the wall changes a filtration: what was stable may become an extension of stable factors in the opposite order.

The modest representation E showed all the essential pieces. There is a nontrivial extension, a specific subobject, a complex-valued charge, and a phase inequality that reverses under a parameter change. The deeper machinery of Hall algebras and cluster varieties keeps track of how that elementary event propagates through large categories.

Stability is therefore not a label permanently attached to an object. It is a relationship between the object and a chosen geometry of comparisons. Wall crossing is the study of how that relationship changes while the underlying algebraic world remains available for reinterpretation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the quiver `1 -> 2`, take `E=(k --id--> k)`. Its only proper nonzero subrepresentation is `S_2=(0 -> k)`, and
\[
0\longrightarrow S_2\longrightarrow E\longrightarrow S_1\longrightarrow0
\]
is nonsplit. With central charges in the strict upper half-plane and `Z(E)=Z(S_1)+Z(S_2)`, the finite-length phase stability criterion is `arg Z(S_2)<arg Z(E)` (strict) for this `E`. If `Z(S_1)=-1+i` and `Z(S_2)=1+i`, the inequality reads `pi/4<pi/2`, so `E` is stable. If the charges swap, it reads `3pi/4<pi/2`, so `E` is unstable. At aligned phases the object is strictly semistable under the corresponding conditions.

For the coefficient-free cluster seed with one arrow `1 -> 2`, mutation at vertex 1 gives `x_1'=(1+x_2)/x_1` and reverses the arrow. A Bridgeland stability condition, a Hall-algebra wall-crossing identity, and a cluster seed mutation are distinct objects; relating them requires categorical/Calabi–Yau assumptions and conventions.

### Exercises with answers

1. Why is `S_1` not a subrepresentation of `E` when the arrow is nonzero? **Answer:** the arrow sends the full source into the target, so target subspace zero is not preserved.
2. Compute `Z(E)` for `Z(S_1)=-1+i`, `Z(S_2)=1+i`. **Answer:** `2i`.
3. What is the phase of `E` in this example? **Answer:** `pi/2`.
4. Does a cluster mutation automatically mean that a representation changed stability? **Answer:** No; the connection depends on an explicit categorical model and stability parameters.

### Reading and source notes

- [Bridgeland, Stability Conditions on Triangulated Categories](https://arxiv.org/abs/math/0212237), foundational stability framework.
- [Fomin and Zelevinsky, Cluster Algebras I: Foundations](https://arxiv.org/abs/math/0104151), seed mutation.
- [Kontsevich and Soibelman, Stability Structures and Motivic Donaldson–Thomas Invariants](https://arxiv.org/abs/0811.2435), wall-crossing identities.
