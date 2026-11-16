# 047000 — Algebraic Groups, Group Schemes, and Lie Algebras

**Track:** Abstract Algebra. **Background:** affine schemes, functors of points, tangent spaces, representations. **Central question:** how can a group law be encoded algebraically so it works over fields, rings, and infinitesimal test objects?

<!-- BEGIN SPOKEN LECTURE -->

# A group whose coordinates obey polynomials

A group is a set with multiplication, inverses, and an identity. An algebraic variety is described by polynomial equations. An algebraic group combines these structures: the group operations must themselves be algebraic. This sounds like adding extra conditions to a familiar group. In fact it changes the questions we can ask.

Consider the invertible matrices of size n. Their multiplication uses polynomial expressions in their entries, but inversion introduces division by the determinant. That is still algebraic on the locus where the determinant is invertible. We obtain a group with a geometric structure, called the general linear group.

Another example is the multiplicative group of nonzero scalars. As a variety it can be described by adjoining an inverse to a coordinate. The additive group is the affine line with addition. These are elementary, but they reveal a key principle: the group law is not something pasted onto the points after the geometry is finished. It is part of the geometry.

## Why points over one field are not enough

Imagine a group described by equations over the real numbers. We might list its real points. We could also look at its complex points, or its solutions over a ring containing infinitesimal elements. All of these are different windows onto the same algebraic structure.

A group scheme assigns a group of solutions to each test ring in a way compatible with ring homomorphisms. For the multiplicative group, the solutions over a ring R are its units. For the general linear group, the solutions are invertible matrices with entries in R. Using all rings rather than one field is important because it lets us detect infinitesimal directions and families.

The coordinate ring of an affine group scheme carries a dual algebraic description. Multiplication of group points corresponds to a comultiplication of functions. Identity gives a counit; inversion gives an antipode. These are the defining pieces of a Hopf algebra. The reversal is worth emphasizing: a geometric multiplication map goes in one direction, while pullback of coordinate functions goes in the other.

## Tangent vectors at the identity

Now consider matrices that differ infinitesimally from the identity. Work over dual numbers, where epsilon squared is zero. A matrix of the form identity plus epsilon times A is invertible, and multiplying two such matrices adds their first-order parts. Thus the tangent vectors at the identity form the full space of n by n matrices.

Where does the Lie bracket come from? Compare products in opposite orders, carefully tracking terms to second order in independent infinitesimals. The commutator is AB minus BA. This bracket makes the tangent space a Lie algebra. For the general linear group, the Lie algebra is precisely the matrix algebra equipped with the commutator bracket.

The Lie algebra is a local, first-order shadow of the group near its identity. It tells us about infinitesimal symmetries and provides a bridge to differential equations and representation theory. But it does not remember the whole global group. The circle and the additive real line have isomorphic one-dimensional real Lie algebras, yet very different global topology.

## What goes wrong in positive characteristic

Group schemes also distinguish phenomena invisible from an ordinary list of points. Let the field have characteristic p. Consider the solutions of x to the pth power equal to zero, with the additive group law. Over a field there is only one solution, zero. But over a ring containing nilpotent elements, more solutions appear. This group scheme is called alpha p.

Its coordinate ring is not reduced. Despite having a single rational point over the field, it has a nonzero tangent space at that point. So counting geometric points does not reveal its infinitesimal structure. In positive characteristic the distinction between smooth algebraic groups and non-smooth group schemes becomes essential.

This is also why moving between algebraic groups and Lie algebras requires care. Over characteristic zero, smooth connected groups and their Lie algebras are closely connected, but even then global questions remain. In characteristic p, Frobenius maps and infinitesimal subgroup schemes introduce behavior that cannot be reconstructed from the ordinary Lie algebra alone.

## Representations and geometry together

A representation of a group scheme on a finite module is a compatible algebraic action, not merely a homomorphism from a chosen set of field-valued points. Its infinitesimal action gives a Lie algebra representation under appropriate smoothness assumptions. Conversely, a representation of a Lie algebra does not automatically integrate to the desired algebraic group representation.

Group schemes let arithmetic and geometry share a vocabulary. The same general linear group can act on lattices, vector spaces, families of curves, or modules over rings. Tangent Lie algebras expose the local structure, while the full functor of points retains global and infinitesimal information. The lesson is that symmetry can be a geometric object, not only a collection of transformations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The group schemes `G_a=Spec Z[t]`, `G_m=Spec Z[t,t^{-1}]`, and `GL_n=Spec Z[a_ij,1/det(a)]` represent the functors `R |-> (R,+)`, `R |-> R^x`, and `R |-> GL_n(R)`. For an affine group `G=Spec A`, the multiplication `m:GxG->G` induces the comultiplication `Delta=m^*:A->A tensor A`, with counit and antipode from identity and inversion.

For a field k and `R=k[epsilon]/(epsilon^2)`, the kernel of `GL_n(R)->GL_n(k)` comprises matrices `I+epsilon A`. As a vector space `Lie(GL_n)=M_n(k)`, with bracket `[A,B]=AB-BA`. For `E_12,E_21`, `[E_12,E_21]=E_11-E_22` (valid in all characteristics, with signs interpreted in k).

In characteristic `p>0`, `alpha_p=Spec k[t]/(t^p)` is an infinitesimal additive subgroup scheme; `alpha_p(k)={0}` when k is a field, but `Lie(alpha_p)` is one-dimensional. The group law is well-defined because `(a+b)^p=a^p+b^p` in characteristic p. The group scheme is not smooth over k. Group-point cardinality and tangent dimension are therefore distinct invariants.

### Exercises with answers

1. What are `G_m(Z)` and `G_m(Q)`? **Answer:** `{1,-1}` and all nonzero rational numbers.
2. For `GL_2`, compute `[E_12,E_21]`. **Answer:** `E_11-E_22`.
3. Why is `alpha_p(k)` insufficient to recover its tangent space? **Answer:** field-valued points miss nonreduced infinitesimal directions; dual-number points detect them.
4. Does a Lie algebra determine global topology? **Answer:** no; the real circle and the additive real line have isomorphic one-dimensional Lie algebras.

### Reading and source notes

- [Gabor Wiese, The Lie algebra of an algebraic group](https://math.uni.lu/wiese/talks/LieAlgebras.pdf), functor-of-points tangent constructions.
- [Milne, Algebraic Groups](https://www.jmilne.org/math/CourseNotes/iAG200.pdf), group schemes and representations.
- [Stacks Project, Group schemes](https://stacks.math.columbia.edu/tag/022R), definition and scheme-theoretic group operations.
