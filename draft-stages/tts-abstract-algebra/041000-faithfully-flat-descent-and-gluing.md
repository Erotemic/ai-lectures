# 041000 — Faithfully Flat Descent: Recovering Objects from a Larger Ring

**Track:** Abstract Algebra. **Background:** modules, tensor products, flatness, sheaves and line bundles. **Central question:** when can information computed after a change of rings be recovered without loss?

<!-- BEGIN SPOKEN LECTURE -->

# Faithfully Flat Descent and the Logic of Gluing

Suppose an equation, a vector bundle, or a module is much easier to study after extending the scalars. We might solve a real equation over the complex numbers, or describe a geometric object on a collection of coordinate charts. But a solution over a larger ring is not automatically a solution over the original one. We must know both which data came from the smaller ring and whether two descriptions agree whenever they refer to the same point.

That is the purpose of descent. It turns the intuitive instruction, “solve locally and glue,” into a precise mathematical theorem. The first surprise is that gluing requires more than matching objects on their own. We must supply a comparison on overlaps, and those comparisons must satisfy a compatibility condition on triple overlaps.

Begin with a familiar example. A complex vector space may be obtained from a real vector space by allowing complex coefficients. But knowing only its complex dimension does not tell us which real vectors were present. One can recover the real vector space when the complex space is equipped with a compatible conjugation operation. A vector is real precisely when conjugation fixes it. An arbitrary complex-linear basis need not be a real basis, but a basis of the fixed vectors produces the original complex space by extending coefficients.

The conjugation is not cosmetic. It is descent data: information that identifies the two ways of regarding an object over the double overlap of the extension. With no such data, an object over the larger field might have several possible origins, and in more complicated settings it might have none.

## What flatness buys us

For a ring map from A to B, extending a module M means forming the tensor product of B with M over A. An especially valuable feature is flatness: short exact sequences of A-modules remain exact after tensoring with B. Kernels and relations therefore behave predictably under this change of scalars.

But flatness alone is not enough. Consider the projection from the product ring k times k onto its first factor. It is flat, but it entirely forgets a module supported on the second factor. Nothing in the image can tell us that the missing component ever existed.

Faithful flatness adds the ability to detect whether a module or a map was zero, injective, or surjective by checking after extension. It is flatness with a guarantee that we have not accidentally discarded part of the problem. Ordinary localization is flat, but generally not faithful, because it can kill modules supported where the inverted element vanishes.

A faithfully flat extension is thus an appropriate analogue of a covering family in geometry. Every part of the original object remains visible somewhere after pullback.

## Why overlap data are necessary

Let us imagine that a B-module N is proposed as the extension of some unknown A-module. There are two natural ways to pull N back to the ring formed by tensoring B with itself over A. If N really comes from M, these two pullbacks agree by a canonical isomorphism: they are both ways of describing M after two successive changes of scalars.

For an arbitrary N we must choose such an isomorphism. Then, after extending to three copies of B, there are two routes for comparing the first copy with the third. A valid descent datum demands that the two routes agree. This is the cocycle condition.

Think of three overlapping coordinate charts. Going from chart one to chart three directly must give the same identification as going from chart one to chart two, then chart two to chart three. Without that rule, local choices cannot define a coherent global object.

The faithfully flat descent theorem says that a B-module equipped with compatible descent data comes from an A-module, uniquely up to the appropriate isomorphism. More strongly, morphisms between descended objects can also be recovered. It is an equivalence of categories, not merely an existence theorem for some individual examples.

## A concrete reconstruction over the real numbers

Return to the extension from real scalars to complex scalars. Let the complex vector space be just one complex dimension, with ordinary conjugation as its real structure. The fixed elements are the real numbers. If we extend those fixed elements back to complex coefficients, we recover the original complex line. Conjugation tells us which scalar multiples were already real and which arose only after extension.

With two complex coordinates, ordinary coordinatewise conjugation similarly recovers the real plane. More general compatible conjugate-linear involutions can recover different real subspaces, but after choosing an appropriate basis each is a real form whose scalar extension is the complex space. The involution must square to the identity; an arbitrary conjugate-linear map is not sufficient.

This example also shows the role of a covering group in descent. For a finite Galois extension of fields, compatible actions of the Galois group express the overlap conditions. The familiar language of Galois symmetry becomes a mechanism for reconstructing linear algebra.

## From modules to geometry

For schemes, coordinate rings on charts are replaced by quasi-coherent sheaves. A faithfully flat, quasi-compact covering permits us to specify sheaves upstairs together with isomorphisms on fiber-product overlaps, and then descend them. Vector bundles are locally free sheaves, so their transition functions are examples of the same idea.

The theorem does not say that every kind of geometric object descends under every cover. Different categories require their own descent statements and hypotheses. Nor does it say that a module over a faithfully flat extension has a unique origin without a chosen descent datum. The origin is recovered from the object plus its coherent comparisons.

The value of descent is that it tells us when local computation is logically complete. A calculation in convenient coordinates, or after enlarging the coefficient field, can produce a genuine global theorem if we carry the compatibility information along with it. The larger world makes the problem tractable; descent tells us exactly what belongs to the smaller one.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a ring map \(A\to B\), faithful flatness means \(-\otimes_A B\) is exact and faithful. Equivalently it is flat and \(M\otimes_A B=0\Rightarrow M=0\). The projection \(k\times k\to k\) is flat but not faithful: \((0,k)\otimes_{k\times k}k=0\).

A descent datum on a B-module N is a \(B\otimes_A B\)-linear isomorphism
\[\varphi:p_1^*N\xrightarrow{\sim}p_2^*N\]
satisfying \(p_{23}^*\varphi\circ p_{12}^*\varphi=p_{13}^*\varphi\) over \(B\otimes_A B\otimes_A B\). If A→B is faithfully flat, descent data on B-modules form a category equivalent to A-modules. In one standard convention the descended module is the equalizer
\[M=\{n\in N:1\otimes n=\varphi(n\otimes1)\},\qquad B\otimes_A M\simeq N.\]
For a finite Galois field extension L/K with group G, the corresponding data on an L-vector space are a semilinear G-action; the descent module is \(V^G\), and \(L\otimes_K V^G\cong V\).

**Counterexample to a tempting simplification:** the existence of a B-module N is not sufficient descent data. Even for faithfully flat extensions the compatible gluing maps must be supplied. Faithfully flat descent for quasi-coherent sheaves applies to fpqc covers; it does not imply effective descent of all morphism or scheme classes without additional hypotheses.

### Exercises with answers

1. Show that \(\mathbf C\otimes_{\mathbf R}\mathbf R^2\cong\mathbf C^2\). **Answer:** send \(z\otimes(a,b)\) to \((za,zb)\); conjugation fixes exactly \(\mathbf R^2\).
2. Why is localization \(\mathbf Z\to\mathbf Z[1/2]\) not faithfully flat? **Answer:** it kills the nonzero module \(\mathbf Z/2\mathbf Z\).
3. Describe the cocycle equation for transition matrices \(g_{ij}\). **Answer:** with a consistent convention, \(g_{ij}g_{jk}=g_{ik}\) on triple overlaps.
4. Does a B-module without a chosen gluing datum determine an A-module? **Answer:** not in general; descent is an equivalence between A-modules and *B-modules with descent data*.

### Reading and source notes

- [Stacks Project, Faithfully flat descent](https://stacks.math.columbia.edu/tag/03O6), the fpqc descent theorem for quasi-coherent sheaves.
- [Stacks Project, Descent for modules](https://stacks.math.columbia.edu/tag/023N), the equivalence of categories and equalizer construction.
