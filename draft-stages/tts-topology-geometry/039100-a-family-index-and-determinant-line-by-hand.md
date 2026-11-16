# 039100 — A Family Index and Determinant Line by Hand: One Zero, One Twist

**Track:** Topology and Geometry. **Background:** K-theory, line bundles, kernels and cokernels, sheaf cohomology. **Central question:** how can every operator in a family have index zero while the determinant line of the family remains nontrivial?

<!-- BEGIN SPOKEN LECTURE -->

# A Family Index and Determinant Line by Hand: One Zero, One Twist

The numerical index of an operator is the dimension of its kernel minus the dimension of its cokernel. That number is stable under suitable deformations. But a family can contain topology invisible in this number. We will construct a finite-dimensional model in which every map has numerical index zero, yet the associated virtual bundle and determinant line are nontrivial.

This model is not yet an infinite-dimensional elliptic family. Its advantage is that we can see exactly what a families index and a determinant line are recording before analytic complications enter.

## The parameter space is a sphere

Let the parameter space B be the complex projective line, topologically a two-sphere. Over B, take two complex line bundles. The domain bundle E is trivial. The target bundle F is O of one, the degree-positive line bundle whose first Chern number is one.

At each parameter point b, we want a complex-linear map from the one-dimensional space E at b to the one-dimensional space F at b. Such a family of maps is the same thing as a section of the Hom bundle from E to F. Because E is trivial, that Hom bundle is simply O of one.

Choose a holomorphic section s of O of one with exactly one simple zero. In homogeneous coordinates, a coordinate linear form gives such a section. At a point where s does not vanish, our fiberwise map is multiplication by a nonzero element of a complex line and is therefore an isomorphism. At the one zero, the map is the zero linear map between one-dimensional vector spaces.

## Kernels and cokernels jump together

Away from the zero, the map is invertible. Its kernel and cokernel both have dimension zero. At the zero, both have dimension one. Thus the numerical index is zero for every b, including the singular parameter.

If we tried to form a kernel bundle by collecting the kernels, we would fail: the dimension jumps from zero to one. The same happens to cokernels. This is exactly the difficulty that appears for families of elliptic differential operators when an eigenvalue passes through zero.

Yet the formal difference between the domain bundle and target bundle is meaningful for the entire family. Its K zero class is the trivial line minus O of one. That is the negative of the sphere's reduced K-theory generator. It has rank zero and nonzero first Chern class.

Numerically, the family has zero index everywhere. Topologically, its index class has a nonzero twist. Both statements are true.

## Construct the determinant line

For a single Fredholm map, its determinant line is the top exterior power of the kernel tensor the dual of the top exterior power of the cokernel. For a finite-dimensional map from E to F, this line can be identified canonically with the determinant of E tensor the dual of the determinant of F. Because our E and F are lines, the resulting determinant line over B is E tensor F dual, namely O of minus one.

The first Chern number of this determinant line is minus one. That is already a witness that it is not trivial. Notice that this sign follows from our convention: the determinant line belongs to the virtual bundle E minus F, not F minus E.

There is also a naturally associated determinant *section*, but it lives in the dual determinant line. The determinant of the fiberwise linear map is an element of the line Hom of E to F. Here that dual determinant line is O of one, and its section is precisely s.

This is a point at which conventions matter. If we call the determinant line det kernel tensor det cokernel dual, the map's scalar determinant is naturally a section of the *dual* line. Confusing the line and its dual reverses the first Chern class.

## Count the zero as a Chern number

Our section s of O of one vanishes once, with positive multiplicity, because it is holomorphic and has one simple zero. The zero count represents the first Chern number of O of one, which is plus one. The determinant line defined using kernel minus cokernel is its dual and has Chern number minus one.

Here the algebraic topology of the family has become a count we can draw. The family is invertible except at one parameter, where kernel and cokernel appear together. A local trivialization of the dual determinant line identifies s near that parameter with a complex coordinate. Its argument winds once around the origin on a small loop.

This local winding is the obstruction to extending a nowhere-vanishing determinant section across the sphere. It is exactly the obstruction recorded by the first Chern class.

## What changes for elliptic operators

An elliptic family consists of maps between infinite-dimensional spaces of sections. Its individual kernels and cokernels are finite-dimensional but may jump in dimension. Analytic Fredholm theory allows a finite-dimensional stabilization, and the stable formal difference of the resulting bundles defines an index class in K zero of the parameter space.

The determinant line of this class continues to make sense even as kernel dimensions jump. Under additional analytic structure, such as a family of Dirac operators, one can define metrics and connections on the determinant line. The curvature of suitable natural connections is related to fiber integrals of characteristic forms, as developed by Bismut and Freed following work of Quillen and others.

Our finite-dimensional model does not prove those curvature formulas. It demonstrates the topology that the formulas must respect: an index bundle may have zero rank at every parameter but nonzero first Chern class, and its determinant line remembers that nonzero class.

## The conceptual takeaway

Three pieces of information must not be conflated. A numerical index belongs to one operator. An index *bundle class* belongs to a family and can twist over parameter space. Its determinant line is a one-dimensional shadow of that twisting. A scalar determinant may vanish at singular parameters, while the determinant line remains well defined and nontrivial.

One zero of a section over the sphere gave us all three features in a calculation we can verify. That is the foundation needed before studying determinant bundles of elliptic families, Berry connections, and gauge-theoretic orientation lines.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `B=CP¹`, `E=1_B`, `F=O(1)`. Choose `s∈Γ(B,Hom(E,F))=Γ(B,O(1))` with one simple zero, and define `D_b:E_b→F_b` by `D_b(v)=v·s(b)`. All fiber maps have numerical index zero, since both source and target are one-dimensional. At the zero `b_0`, `dim ker D=dim coker D=1`; elsewhere both dimensions vanish.

The index K-class is `Ind(D)=[E]-[F]=-[O(1)]+[1]=-β∈\widetilde K^0(S²)`. Its determinant line under the convention `det(Ind)=det(ker D)⊗det(coker D)^*` is the canonically extended line

\[
\det(\operatorname{Ind}D)=\det E\otimes(\det F)^*
=O(-1),\qquad c_1=-h.
\]

The fiberwise ordinary determinant of `D` gives a section of its **dual** `O(1)` with one zero and positive local winding. This finite-dimensional model illustrates but is not a proof of the families Atiyah–Singer theorem or of Quillen/Bismut–Freed analytic metrics and connections.

### Exercises with answers

1. What is the numerical index away from the zero? **Answer:** zero.
2. What is the numerical index at the zero? **Answer:** one minus one, still zero.
3. What is the Chern number of the index determinant line? **Answer:** minus one, under the convention det kernel tensor det cokernel dual.
4. Where does the ordinary determinant section live? **Answer:** in the *dual* determinant line `O(1)`.

### Sources and further reading

- M. Atiyah and I. Singer, [The Index of Elliptic Operators: IV](https://doi.org/10.2307/1970756), families index theorem.
- J.-M. Bismut and D. Freed, [The Analysis of Elliptic Families I](https://doi.org/10.1007/BF01210930), determinant metrics and connections (1986).
- [Determinant line bundle](https://en.wikipedia.org/wiki/Determinant_line_bundle); [Index theory](https://en.wikipedia.org/wiki/Index_theory).
