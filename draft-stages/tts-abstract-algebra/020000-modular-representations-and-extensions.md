# 020000 — Modular Representations: When Symmetry No Longer Splits

**Track:** Abstract Algebra. **Background:** group representations, Maschke's theorem, modules, short exact sequences, and resolutions. **Central question:** what replaces a decomposition into irreducibles when the characteristic of the field divides the group order?

<!-- BEGIN SPOKEN LECTURE -->

# Modular Representations: When Symmetry No Longer Splits

A finite group acting on a vector space can often be understood by decomposing the space into smaller invariant pieces. Over the complex numbers, Maschke's theorem guarantees this for every finite group representation. We can take a representation apart into irreducibles and study those parts one at a time.

But that guarantee relies on division by the order of the group. What if the coefficient field does not permit that division? Then a subrepresentation may exist without any invariant complement. Two irreducible pieces can be attached in a way that is invisible if we only count the pieces. This is the beginning of modular representation theory.

## A group with two elements in characteristic two

Consider the group consisting of the identity and an element g with g squared equal to the identity. Over the field with two elements, examine the two-dimensional vector space with basis e one and e two. Let g fix e one, but send e two to e two plus e one.

Apply g twice. The first application adds e one. The second adds e one again. In characteristic two, adding e one twice adds zero. So g squared acts as the identity, exactly as required. We have a valid representation of the two-element group.

The line spanned by e one is invariant, and g acts trivially there. The quotient by that line is also a one-dimensional trivial representation, because the extra e one disappears in the quotient. Thus, viewed only through its two successive one-dimensional pieces, the representation looks like two copies of the trivial representation.

Yet it is not the direct sum of two trivial representations. In a direct sum of trivial representations, g would act as the identity everywhere. Here g changes e two. Could there be a different invariant line complementary to the first? Every vector outside the first line has the form e two plus a times e one. Applying g adds e one, so this vector cannot be fixed. Over the field with two elements every one-dimensional representation of our two-element group is trivial. Therefore no invariant complementary line exists.

We have found a nonsplit short exact sequence: a trivial one-dimensional representation sits inside a two-dimensional representation whose quotient is trivial, but the middle representation is not a direct sum of the ends.

## What happened to averaging?

Maschke's theorem proves the existence of invariant complements by starting with any linear projection onto an invariant subspace and averaging its conjugates over the group. Dividing the sum by the group order makes the average a projection commuting with the group action.

For a group of order two over a field of characteristic two, division by two is impossible because two equals zero. The argument does not merely break as a matter of technique; our explicit representation proves its conclusion is false. More generally, when the characteristic divides the finite group order, representations need not be semisimple.

Semisimple does not mean every representation has no interesting internal structure. It means that all representations can be expressed as direct sums of simple ones. In the modular example, the two-dimensional representation is not simple because it has an invariant line, and it is not a direct sum of smaller subrepresentations either. It is indecomposable but reducible. Those terms name two different properties.

## The group algebra reveals the attachment

A representation of a finite group over a field k is the same thing as a module over the group algebra k G. For our two-element group in characteristic two, write epsilon for g minus the identity. Then epsilon squared equals g squared minus two g plus one, which simplifies to zero. The group algebra is isomorphic to a truncated polynomial ring: polynomials in epsilon with epsilon squared set equal to zero.

In the two-dimensional example, epsilon sends e two to e one and sends e one to zero. Thus epsilon is a nonzero nilpotent linear operator whose square is zero. The invariant line is the image and kernel of epsilon, both spanned by e one. The representation is a module over a ring with a nonzero nilpotent element, and the failure of splitting is encoded by that nilpotent action.

Compare two modules over this ring. In one module, epsilon acts as zero on a two-dimensional vector space. That is the direct sum of two trivial modules. In the other, epsilon acts by a single two-by-two nilpotent Jordan block. Both modules have the same composition factors: two copies of the trivial simple module. But the modules are not isomorphic. Composition factors do not determine a module when extensions can be nontrivial.

## Extensions become data

A short exact sequence from A into E onto B is called an extension of B by A. Sometimes it splits, so E is a direct sum. Sometimes, as in our example, it does not. Extensions are not merely annoying exceptions; they are information that an irreducible decomposition loses.

Homological algebra provides a way to organize this information. The first Ext group, Ext one of B with A, classifies equivalence classes of module extensions of B by A, with the split extension representing zero. Higher Ext groups study more complicated obstructions and derived behavior.

For our group algebra k of epsilon with epsilon squared zero, the simple module k has epsilon acting by zero. A free resolution of this simple module is periodic: repeatedly multiply the ring by epsilon, and finally map the ring onto k by taking the quotient. Each multiplication by epsilon has image equal to kernel, because the elements annihilated by epsilon are exactly its multiples.

Apply the module homomorphism functor into k. Multiplication by epsilon induces the zero map because epsilon acts as zero on k. Consequently Ext one of k with k is a one-dimensional vector space over k. Over the two-element field, that leaves two extension classes: the split one and the nonsplit one represented by our two-dimensional module.

This calculation does not require us to classify every modular representation of every finite group. It shows why projective resolutions were worth learning. They detect precisely the data that a list of irreducible constituents misses.

## The change of viewpoint

Characteristic zero and characteristic dividing the group order lead to different questions. In the semisimple setting, character tables and decomposition multiplicities often suffice to distinguish representations up to isomorphism. In the modular setting, extension classes, projective indecomposables, block structure, and interactions between modules become central.

The two-dimensional example is small enough to inspect by hand, but it carries the conceptual transition. Having the same simple constituents does not imply being the same module. Symmetry can glue pieces together, and the glue is mathematically meaningful. Once we stop insisting that everything splits, homological algebra becomes a natural language for representation theory rather than an optional abstraction.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(k=\mathbb F_2\), \(G=C_2=\langle g\mid g^2=1\rangle\). Define the representation \(V=k^2\) by
\[
\rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}=I+N,\quad N^2=0.
\]
Since \(2=0\) in \(k\), \(\rho(g)^2=I+2N+N^2=I\). The line \(ke_1\subset V\) and the quotient \(V/ke_1\) are trivial representations, but \(V\) has no invariant complementary line. Thus \(0\to k\to V\to k\to0\) is nonsplit.

The group algebra satisfies
\[
k[G]\cong k[\varepsilon]/(\varepsilon^2),\quad \varepsilon=g-1.
\]
Its trivial module is \(k=k[G]/(\varepsilon)\), and a free resolution is
\[
\cdots\xrightarrow{\varepsilon}k[G]\xrightarrow{\varepsilon}k[G]\xrightarrow{\varepsilon}k[G]\twoheadrightarrow k\to0.
\]
Exactness holds because \(\ker(\varepsilon\cdot)=\varepsilon k[G]=\operatorname{im}(\varepsilon\cdot)\). Applying \(\operatorname{Hom}_{k[G]}(-,k)\) yields zero coboundary maps. Therefore \(\operatorname{Ext}^1_{k[G]}(k,k)\cong k\). The Yoneda interpretation identifies zero with split extensions. This computation assumes the usual equivalence of short exact sequences fixing the end terms.

**Maschke's hypothesis.** If \(G\) is finite and \(\operatorname{char}k\nmid|G|\), every finite-dimensional \(k[G]\)-module is semisimple. The counterexample above shows why dropping that hypothesis can change the conclusion.

### Exercises with answers

1. Find the fixed subspace of \(V\). **Answer:** \(\ker N=ke_1\).
2. Why cannot \(e_2\) span an invariant complement? **Answer:** \(g e_2=e_2+e_1\notin ke_2\).
3. Do the split and nonsplit modules have the same simple composition factors? **Yes:** two copies of \(k\); the extension class distinguishes the modules.
4. Over \(\mathbb F_3\), does this exact matrix define a \(C_2\) representation? **No:** \((I+N)^2=I+2N\ne I\). Maschke's theorem applies to \(C_2\) in characteristic three.

### Reading and source notes

- Pavel Etingof et al., MIT OCW [Introduction to Representation Theory](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), group algebras and semisimplicity.
- Charles A. Weibel, [An Introduction to Homological Algebra](https://doi.org/10.1017/CBO9781139644136), projective resolutions and Ext.
