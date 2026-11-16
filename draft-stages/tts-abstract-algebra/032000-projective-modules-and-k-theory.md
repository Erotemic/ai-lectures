# 032000 — Projective Modules, Vector Bundles, and the First Idea of K-Theory

**Track:** Abstract Algebra. **Background:** modules and direct sums, tensor products, affine and topological vector bundles. **Central question:** can a module behave locally like a free module without admitting a global basis?

<!-- BEGIN SPOKEN LECTURE -->

# Projective Modules, Vector Bundles, and the First Idea of K-Theory

In elementary linear algebra, a finite-dimensional vector space has a basis. Over a general ring, a module need not have any basis at all. Yet some modules behave enough like vector spaces that one can perform almost all the same constructions locally. These are projective modules.

To understand why they matter, think about a Möbius band. Near any single point of its central circle, the band looks like a product of a little interval with a line. But if you travel once around the circle, the line reverses its orientation. No single continuous choice of a nonzero vector along every fiber can be made consistent after the circuit.

The module of continuous sections of this line bundle will give us an example of a module that is locally free but not globally free. Algebra alone can record the twist.

## Splitting a free module

A module P over a ring R is projective when it is a direct summand of some free module. That means there is another module Q for which P direct sum Q is free. A finitely generated projective module is a direct summand of a finite-rank free module.

Why use this definition? A free module comes with independent coordinate directions. A direct summand can inherit many of its good properties without possessing global coordinates of its own. A familiar equivalent definition says that maps from P into quotients can be lifted across surjections. This is the categorical lifting property, and it explains why projectives support the resolutions used in homological algebra.

One way to build projective modules is through idempotent matrices. An idempotent is a matrix E whose square equals itself. Its image and kernel form complementary submodules of a free module. The image is projective, even if no global basis exists for that image. Conversely, every finitely generated projective module arises as the image of some finite idempotent matrix.

This turns an abstract algebraic property into a computational object. Rather than guessing a basis, we can specify a projection and ask what its image does at different points of the underlying space.

## A rotating line that never quite returns

Let R be the ring of continuous real-valued functions on the circle. A rank-one bundle over the circle can be described by a line in the plane that rotates through half a turn as we go once around the circle. The line returns to itself because a line has no preferred arrow, although any attempted choice of a unit vector returns with the opposite sign.

At angle theta, take the orthogonal projection onto the line making angle theta divided by two with the horizontal axis. Its matrix entries can be written using only sine and cosine of theta. Consequently they are continuous, periodic functions on the circle, even though a chosen unit vector with angle theta divided by two is not periodic.

The resulting matrix is idempotent at every point. Its image gives a finitely generated projective module of continuous sections of the Möbius line bundle. It cannot be free of rank one. If it were, one global basis section would give a nonvanishing continuous choice of vector around the circle, contradicting the twist.

Yet the module is a direct summand of a free module of rank two. The complementary image is another line bundle, and together they recover the trivial plane bundle. The apparent paradox is exactly the distinction between being free and being projective.

## Why topology and algebra meet

The Serre–Swan theorem makes this connection systematic. For a compact Hausdorff space X, finite-rank real or complex vector bundles correspond to finitely generated projective modules over the ring of continuous real or complex functions on X. Passing from a bundle to its module of sections is not just a source of examples; it establishes an equivalence of categories with appropriate conventions.

Thus the algebra of a ring of functions remembers how vectors twist over the space. Matrix idempotents encode vector bundles. Module operations become geometric operations: direct sum combines bundles fiberwise, and tensor product combines their fibers multiplicatively.

Notice the role of the coefficient field. The real Möbius line bundle is nontrivial. Complex line bundles on a circle are all trivial, so the same example would not witness nonfree rank-one complex projective modules over continuous complex-valued functions on the circle. The ring matters.

## Turning modules into an invariant

There are many projective modules, and adding them by direct sum does not immediately give a group: one cannot generally subtract an actual vector bundle from another. Grothendieck's idea is to formally add differences.

Start with isomorphism classes of finitely generated projective modules, with direct sum as addition. Construct its universal abelian group completion. This group is called K zero of the ring. A formal difference of projective modules represents an element of K zero, subject to relations expressing how direct sums behave.

For a field, every finite-dimensional vector space is determined by its dimension. K zero is therefore the integers. For rings of functions on spaces with nontrivial vector bundles, K zero can contain more information than rank.

The Möbius example gives a glimpse of that extra information. Its line bundle L is not trivial, yet L direct sum L is a trivial real plane bundle over the circle. In reduced real K-theory, the difference between L and the trivial line has order two. The torsion is a trace of the half-turn that no rank count can detect.

We should distinguish the two statements carefully. The equation in K-theory tells us about stable equivalence, where adding trivial bundles can make two objects comparable. It does not mean the original Möbius line has suddenly acquired a global frame.

## Why this is the right abstraction

Projective modules are the right replacement for finite-dimensional vector spaces when geometry can twist. They explain why resolutions have good lifting properties, why locally free objects can fail to be globally free, and why new invariants are needed beyond dimension.

K-theory begins with a surprisingly modest move: take objects we can add but not subtract, and construct a group that records their stable differences. What emerges is a bridge among matrix algebra, vector bundles, topology, and arithmetic. The same philosophy will recur whenever we want to compare complicated objects by how they fit into sums, extensions, and exact sequences.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A module \(P\) over \(R\) is projective iff it is a direct summand of a free module, equivalently iff \(\operatorname{Hom}_R(P,-)\) is exact. Finite projectives correspond to images of idempotent matrices \(E\in M_n(R)\), \(E^2=E\): \(R^n=\operatorname{im}E\oplus\ker E\).

**Möbius projector:** take \(R=C(S^1,\mathbb R)\), with \(\theta\) an angular coordinate modulo \(2\pi\), and
\[E(\theta)=\frac12\begin{pmatrix}1+\cos\theta&\sin\theta\\\sin\theta&1-\cos\theta\end{pmatrix}.\]
It is continuous and periodic with \(E(\theta)^2=E(\theta)\), and projects onto the line spanned by \((\cos(\theta/2),\sin(\theta/2))\). This line is well-defined modulo sign and gives the Möbius real line bundle \(L\). \(L\) has no nowhere-vanishing global section, hence its module of sections is not free of rank one. The orthogonal complement line bundle is isomorphic to \(L\), and \(L\oplus L\cong\underline{\mathbb R}^2\).

The Grothendieck group \(K_0(R)\) is the group completion of isomorphism classes of finitely generated projectives under direct sum. For a field \(k\), \(K_0(k)\cong\mathbb Z\) via dimension. For \(C(S^1,\mathbb R)\), the reduced group \(\widetilde K_0\cong\mathbb Z/2\) detects the Möbius class. More generally the Serre–Swan equivalence identifies finite-rank bundles on compact Hausdorff \(X\) with finitely generated projective modules over \(C(X,\mathbb F)\), \(\mathbb F=\mathbb R\) or \(\mathbb C\).

### Exercises with answers

1. If \(E^2=E\), why is \(R^n=\mathrm{im}E\oplus\ker E\)? **Answer:** write \(v=Ev+(v-Ev)\); the summands intersect trivially.
2. Why is a nontrivial line bundle over \(S^1\) not free as a rank-one section module? **Answer:** a free rank-one section would be a nowhere-vanishing global frame.
3. Why does \(L\oplus L\) being trivial not imply \(L\) trivial? **Answer:** direct-sum cancellation does not hold for arbitrary vector bundles; stable and actual triviality differ.
4. What does \(K_0(k)\) measure for a field \(k\)? **Answer:** the dimension, extended to virtual differences, giving \(\mathbb Z\).

### Reading and source notes

- Richard G. Swan, [*Vector Bundles and Projective Modules*](https://www.math.unl.edu/~jkettinger2/swan.pdf), original proof of the compact Hausdorff correspondence.
- Allen Hatcher, [*Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), bundle examples, stable classes, and K-theoretic constructions.
- [Stacks Project, projective modules and direct summands](https://stacks.math.columbia.edu/tag/0ELQ), commutative algebra background.
