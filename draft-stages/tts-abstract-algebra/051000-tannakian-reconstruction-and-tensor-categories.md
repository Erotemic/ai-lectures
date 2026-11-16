# 051000 — Tannakian Reconstruction: Recovering Symmetry from Representations

**Track:** Abstract Algebra. **Background:** representations, tensor products, symmetric monoidal categories, algebraic groups. **Central question:** if we know every representation and how representations combine, can we recover the group itself?

<!-- BEGIN SPOKEN LECTURE -->

# The group behind the actions

A group acts on a vector space through matrices. Usually we begin with the group and study its representations. But suppose someone erases the name and definition of the group, leaving us its entire collection of finite-dimensional representations. We can still see the linear maps between them. We know how to take direct sums, duals, and tensor products. We know which representation is the trivial one. Is the original symmetry recoverable from this information?

For a suitable class of algebraic groups, the answer is yes. Tannakian reconstruction makes that statement precise. It also explains why a category, together with its tensor operations, can carry enough information to describe an object that seems external to the category.

It is tempting to say that a group is just the collection of dimensions of its irreducible representations. That is false. Dimensions discard most of the relationships between representations. The tensor product carries more information: it tells us which representations appear when two symmetries act jointly. Morphisms, duals, and the symmetry of the tensor operation carry still more.

## An example we can reconstruct

Consider the multiplicative algebraic group: nonzero scalars acting by multiplication. Its finite-dimensional representations in characteristic zero decompose into weight spaces. On a weight-n line, a scalar t acts as t to the n. The weight-zero line is trivial. The dual of weight n has weight negative n. The tensor product of weight m and weight n has weight m plus n.

Imagine forgetting the scalars but remembering the weight lines and their tensor multiplication. A symmetry of the forgetful functor to vector spaces must act on each weight line by a scalar. If it acts by lambda on weight one, compatibility with tensor products forces it to act by lambda squared on weight two, by lambda cubed on weight three, and by the inverse of lambda on weight negative one. The entire action is determined by a single invertible scalar.

We have recovered the multiplicative group from the requirement that a family of linear transformations respect every tensor operation. This is the simplest tangible example of the reconstruction principle.

## The fiber functor is essential

Here is the formal setup, expressed carefully. We have a suitable rigid, abelian, symmetric tensor category over a field. Rigid means that objects have duals. A fiber functor sends its objects to finite-dimensional vector spaces, preserving the tensor product and the unit object. We require it to be faithful and exact: it must not identify distinct morphisms or destroy the short exact sequence structure.

Now consider all tensor-compatible natural automorphisms of that functor. To every commutative algebra over the base field, we can assign a group of such automorphisms after extending scalars. This assignment is represented, under the Tannakian hypotheses, by an affine group scheme. In other words, an algebraic symmetry object emerges from the category and the fiber functor.

The phrase group scheme matters. The recovered object need not be understood completely by listing its points over one field. It may carry infinitesimal structure, or possess fewer rational points than its geometry over larger fields suggests. The reconstruction is algebraic, not merely set-theoretic.

Without a specified fiber functor, the category can still contain substantial symmetry information, but reconstruction may produce a group over an extension or a more general gerbe. The chosen way of realizing abstract objects as vector spaces is part of the neutral reconstruction data. This is why the theorem is not simply that any tensor category secretly *is* a group.

## Why naturality constrains the answer

A natural transformation of the fiber functor provides a linear transformation on every representation. But those choices cannot be arbitrary. If a map between two representations commutes with the group action, our family of transformations must commute with that map as well. It must respect tensor products and the identity representation.

These constraints are strong enough to prevent fake symmetries. In the weight example, assigning independent scalars to weight one and weight two violates the tensor product law unless the second is the square of the first. The category's internal operations enforce the same relations that multiplication enforces in the original group.

This perspective is useful when the representations come first. In arithmetic geometry, we may study a category of vector bundles with connection, local systems, or motives and ask what symmetry object governs them. A Tannakian group can encode monodromy or other hidden symmetries of those objects.

The reconstruction does not make every such category easy to calculate. It tells us which data are sufficient to pose the question correctly and why tensor structure is indispensable. If the category is not abelian, if duals are missing, or if the proposed functor is not exact, the standard theorem may not apply.

## What counts as recovering the group?

A powerful feature of the theorem is that it is reversible. Starting with an affine group scheme, we form its finite-dimensional representation category with the ordinary forgetful functor. Reconstructing from that pair gives back the group scheme. Conversely, a neutral Tannakian category can be described as the representation category of its recovered affine group scheme.

The lesson is that symmetry is not only a set of transformations of one object. It is also the pattern of coherent transformations across *all* objects of a representation theory. Tensor products tell us how separate actions coexist; duals tell us how to reverse them; naturality tells us which choices are compatible. Recovering the group means recovering those constraints as a single algebraic object.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A neutral Tannakian category over a field `k` (classically `char(k)=0` for the simplest formulation) is a rigid abelian `k`-linear symmetric monoidal category `C` with `End(1)=k` and an exact faithful `k`-linear tensor functor `omega:C -> Vec_k^fd`. Its Tannaka group is the affine group scheme
\[
G=\operatorname{Aut}^{\otimes}(\omega), \qquad
G(R)=\operatorname{Aut}^{\otimes}(R\otimes_k\omega),
\]
with scalar-extension and naturality conditions understood. The reconstruction theorem identifies `(C,omega)` with `(Rep_k^fd(G), forget)` as tensor categories with fiber functor.

For `G_m`, weight representations `k(n)` satisfy `k(m) \otimes k(n) \cong k(m+n)`, `k(n)^\vee \cong k(-n)`. A monoidal automorphism is determined by its scalar `lambda in R^x` on `k(1)`; the action on `k(n)` is `lambda^n`. Hence `Aut^tensor(omega) = G_m` as a functor of algebras, not just by a pointwise count.

The theorem needs structural hypotheses. An arbitrary monoidal category with a functor to sets is not automatically Tannakian. The recovered group scheme can be nonreduced in positive characteristic, and the Tannakian formalism there requires attention to the precise formulation.

### Exercises with answers

1. If a tensor automorphism acts by `lambda` on `k(1)`, how does it act on `k(-3)`? **Answer:** by `lambda^{-3}`.
2. Why can't we choose independent actions on `k(1)` and `k(2)`? **Answer:** their tensor relationship forces the second action to be the square of the first.
3. What does the fiber functor supply? **Answer:** a faithful exact tensor realization of abstract objects as finite-dimensional vector spaces.
4. Why reconstruct a group *scheme* rather than only its k-valued points? **Answer:** points over varying k-algebras can detect algebraic and infinitesimal structure invisible over k alone.

### Reading and source notes

- [Deligne and Milne, Tannakian Categories](https://www.jmilne.org/math/xnotes/tc2022.pdf), reconstruction, fiber functors and affine group schemes.
- [Milne, Algebraic Groups](https://www.jmilne.org/math/CourseNotes/iAG200.pdf), algebraic group representations and group schemes.
- [The Stacks Project, Groupoid Schemes](https://stacks.math.columbia.edu/download/groupoids.pdf), group schemes and quotient structures.
