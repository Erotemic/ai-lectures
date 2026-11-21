# 003000 — A Sphere as a Space of Symmetries

**Track:** Lie Groups, Lie Algebras, and Representations. **Preparation:** group actions, tangent spaces, and the matrix rotation group. **Theme:** an orbit is a quotient of a group by the symmetries that leave one point fixed.

<!-- BEGIN SPOKEN LECTURE -->

# A Sphere as a Space of Symmetries

Imagine pointing a telescope in an arbitrary direction. You can describe the direction with a point on the unit sphere. You can also describe how to get there by starting from the north pole and rotating a rigid frame. The first description uses two coordinates locally: latitude and longitude, for instance. The second uses a full three-dimensional rotation, with three independent infinitesimal directions. Why does the second description contain one extra degree of freedom?

Because several different rotations point the telescope in exactly the same direction. Once it points north, turning the entire frame around the north–south axis does not change the direction. More generally, after you choose any target point, there is a whole circle of rotations that leave it where it is. The sphere is therefore not the whole rotation group, but the rotation group with a certain family of transformations identified.

This is a homogeneous space, and it gives a geometrically concrete way to connect Lie groups, group actions, quotient spaces, and tangent directions.

## An action and its stabilizer

A group action is a rule telling us how each element of a group transforms points of a space, compatibly with multiplication. For the group SO three acting on the unit sphere, the rule is ordinary matrix multiplication: take a rotation matrix and apply it to a unit vector. Rotations preserve vector length, so the result remains on the sphere.

Choose the north pole, the vector with coordinates zero, zero, one. The orbit of the north pole is the set of all positions reachable by group elements. Every unit vector is reachable from the north pole by some rotation, so its orbit is the entire sphere. We call the action transitive: any point can be reached from any other.

Now collect the rotations that leave the north pole fixed. This collection is a subgroup, called its stabilizer. It consists exactly of rotations about the vertical axis, and is itself a copy of SO two. A rotation that tilts north to east is not in the stabilizer. But composing such a tilt on the right with a rotation around the original north axis produces a different group element with the same final pointing direction.

Thus two rotations carry the north pole to the same point precisely when they differ by multiplication on the right by an element of the stabilizer. The sphere can be identified with the space of left cosets of that subgroup, written SO three divided by SO two. We obtain those cosets by identifying rotations that differ by right multiplication with an element of the stabilizer. This is a quotient *space*. It is not, in general, a quotient *group*, because the stabilizer need not be a normal subgroup. Confusing those two notions is a common trap when translating geometry into algebra.

## Recovering two dimensions by differentiation

The rotation group has three independent infinitesimal directions. What happens to those directions when we look only at the position of the north pole?

Take an infinitesimal rotation X, a skew-symmetric three-by-three matrix. The infinitesimal change of the pole is X times the pole vector. Such a change is perpendicular to the pole: differentiating a vector of fixed unit length gives a tangent vector orthogonal to the starting direction.

The map sending X to X times the pole has a kernel. Any infinitesimal rotation *about* the vertical axis fixes the pole to first order, and in fact fixes it for all time. That kernel is the one-dimensional Lie algebra of SO two. The other two independent generators move the pole along two independent tangent directions on the sphere.

The rank is therefore three minus one, which is two. This is the differential version of orbit–stabilizer. More generally, for a smooth Lie group action, the orbit through a point is an immersed submanifold, and its dimension is the dimension of the group minus the dimension of the stabilizer. Under familiar proper-action hypotheses, the orbit is also an embedded submanifold.

At the tangent-space level, we obtain a vector-space identification: the tangent space of the orbit at the selected point is the Lie algebra of the group modulo the vector subspace belonging to the stabilizer. Again, this vector-space quotient does not automatically have a Lie algebra bracket, because the stabilizer algebra need not be an ideal.

That distinction is geometrically meaningful. A sphere has a tangent plane, but tangent vectors at a point on the sphere do not naturally form a Lie algebra just because the sphere came from rotations.

## The stabilizer changes when the point changes

Suppose we now point the telescope east rather than north. The rotations that keep that direction fixed are rotations about the new pointing axis. They form a subgroup conjugate to the original stabilizer.

Algebraically, if g carries north to east, the new stabilizer is g times the old stabilizer times g inverse. Conjugation moves the location of the symmetry axes, while preserving the abstract group structure. This gives a natural reason to study conjugation and its derivative, rather than treating it merely as a group-theoretic formula.

Let g be a fixed group element. For a matrix Lie group, the conjugation map sends h to g h g inverse. Differentiate with respect to h at the identity. A Lie-algebra element X is sent to g X g inverse. This linear transformation on the Lie algebra is called Ad of g, the adjoint action.

The group acts on its own infinitesimal directions. In SO three, those directions correspond to ordinary three-dimensional vectors. Conjugating a rotation generator by g simply rotates the axis vector. So the adjoint representation of SO three is the familiar three-dimensional rotation representation, presented from a new perspective.

Differentiate the adjoint action in g as well. The infinitesimal adjoint operator associated to X sends Y to the bracket of X and Y. This is usually written lower-case ad of X. The group-level process of conjugating finite movements and the algebra-level process of taking commutators are two faces of the same operation.

## A space can carry an invariant geometry

The unit sphere is not just a set of directions. It has lengths, angles, and geodesics. Rotations preserve these structures. This means the metric on the sphere is invariant under the SO three action: rotate two tangent vectors together, and their inner product is unchanged.

To understand an invariant metric on a homogeneous space, we can often work at a single point. Choose an inner product on the two-dimensional tangent plane at the north pole. If it is preserved by the north-pole stabilizer, which rotates that tangent plane, the group action transports the metric consistently to every point of the sphere. For the standard sphere this forces the metric at the pole to be a positive scalar multiple of the ordinary Euclidean inner product. That is because a quadratic form invariant under every planar rotation has the same value in every unit direction.

This illustrates a recurring method in geometry: reduce a global problem to linear algebra at one point, then use symmetry to reconstruct the global object. It is closely related to what representations do. The stabilizer acts linearly on the tangent space, and invariant tensors are exactly the objects left fixed by that representation.

## The same sphere from another group

There is a second group related to the same three-dimensional rotations: SU two, the special unitary two-by-two matrices. It has dimension three as a real Lie group, and its Lie algebra is isomorphic to that of SO three. Yet the groups are not isomorphic. There is a surjective homomorphism from SU two onto SO three with a two-element kernel. In particular, the matrices I and negative I in SU two give the same rotation in SO three.

What does this mean for the sphere? SU two can act on the sphere through the map to SO three. The resulting action still reaches every point and still has the same infinitesimal orbit directions. But some global transformations in SU two are invisible in the action. This is an early example of why a representation, or an action, can forget part of a group: it may have a nontrivial kernel.

If our only observation is the orientation of a classical rigid body, the distinction may not be visible. If our objects transform according to other representations, the central element negative I can act nontrivially. That will lead to the difference between integer and half-integer spin representations.

## Why quotient spaces recur in mathematics

The construction has many variants. A projective space can be described by taking nonzero vectors and identifying vectors that differ by a nonzero scalar, or by a suitable homogeneous-space quotient. A Grassmannian, the space of all k-dimensional subspaces of a fixed vector space, can be described as a quotient of a general linear group by the subgroup preserving a reference k-dimensional plane. Spaces of matrices of fixed rank, flags of nested subspaces, and families of geometric configurations all admit similar descriptions.

The benefit is that a space with complicated-looking coordinates may have a concise description in terms of symmetries and stabilizers. Differentiating that description gives a tangent-space model. Studying how the stabilizer acts on the tangent space constrains possible invariant metrics, differential forms, and other geometric structures.

The circle action on the plane, the full rotation action on the sphere, and the general linear action on subspaces are thus not isolated examples. They belong to one idea: points can be understood as group transformations, with all transformations that leave a reference point unchanged identified.

We began with a missing degree of freedom in the telescope description. The stabilizer accounts for it exactly. Three directions of rotation minus one direction that does not move the pointer leaves two directions on the sphere. At the global level the orbit is a coset space; at the infinitesimal level its tangent space is a quotient of vector spaces; and at the geometric level invariant structures are controlled by a linear stabilizer representation. This is the passage from group theory to geometry that makes Lie groups so broadly useful.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth action \(G\curvearrowright M\), define orbit \(G\cdot p=\{g\cdot p:g\in G\}\) and stabilizer \(G_p=\{g:g\cdot p=p\}\). The orbit map \(g\mapsto g\cdot p\) induces \(G/G_p\cong G\cdot p\) as a homogeneous space (with the standard smooth structure). Its differential at the identity yields
\[
\mathfrak g/\mathfrak g_p\;\cong\;T_p(G\cdot p)
\]
as **vector spaces**; \(\mathfrak g_p\) need not be an ideal.

For \(p=e_3\in S^2\), \(G=SO(3)\), \(G_p\cong SO(2)\), \(\dim SO(3)=3\), \(\dim SO(2)=1\), \(\dim S^2=2\). Infinitesimal orbit map: \(X\mapsto Xe_3\). Conjugate stabilizers: \(G_{g\cdot p}=gG_pg^{-1}\).

\[
\operatorname{Ad}_g(X)=gXg^{-1},\quad \operatorname{ad}_X(Y)=[X,Y].
\]

**Exercises and solutions.** (1) What stabilizes the north pole in \(SO(3)\)? *Precisely vertical-axis rotations.* (2) Is \(SO(3)/SO(2)\) a quotient group? *Not by the ordinary coset construction; \(SO(2)\) is not a normal subgroup.* (3) Why does a rotation-invariant inner product on the north-pole tangent plane have only one free scale? *Its symmetric matrix commutes with all planar rotations and hence is scalar.* (4) Are the two groups \(SU(2)\) and \(SO(3)\) locally similar? *Yes, their Lie algebras are isomorphic, but globally the former double-covers the latter.*

### Sources and further reading

- MIT OCW 18.745 (2020), lecture 4 on homogeneous spaces and Lie group actions, and lecture 8 on Lie algebras: https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed.: https://doi.org/10.1007/978-3-319-13467-3
- Existing preparation: `topology-geometry:008000` and `abstract-algebra:001000`.
