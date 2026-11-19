# Modular representations and group-cohomology obstructions

<!-- BEGIN SPOKEN LECTURE -->

# Modular representations and group-cohomology obstructions

## Modular Representations: When Symmetry No Longer Splits

A finite group acting on a vector space can often be understood by decomposing the space into smaller invariant pieces. Over the complex numbers, Maschke's theorem guarantees this for every finite group representation. We can take a representation apart into irreducibles and study those parts one at a time.

But that guarantee relies on division by the order of the group. What if the coefficient field does not permit that division? Then a subrepresentation may exist without any invariant complement. Two irreducible pieces can be attached in a way that is invisible if we only count the pieces. This is the beginning of modular representation theory.

### A group with two elements in characteristic two

Consider the group consisting of the identity and an element g with g squared equal to the identity. Over the field with two elements, examine the two-dimensional vector space with basis e one and e two. Let g fix e one, but send e two to e two plus e one.

Apply g twice. The first application adds e one. The second adds e one again. In characteristic two, adding e one twice adds zero. So g squared acts as the identity, exactly as required. We have a valid representation of the two-element group.

The line spanned by e one is invariant, and g acts trivially there. The quotient by that line is also a one-dimensional trivial representation, because the extra e one disappears in the quotient. Thus, viewed only through its two successive one-dimensional pieces, the representation looks like two copies of the trivial representation.

Yet it is not the direct sum of two trivial representations. In a direct sum of trivial representations, g would act as the identity everywhere. Here g changes e two. Could there be a different invariant line complementary to the first? Every vector outside the first line has the form e two plus a times e one. Applying g adds e one, so this vector cannot be fixed. Over the field with two elements every one-dimensional representation of our two-element group is trivial. Therefore no invariant complementary line exists.

We have found a nonsplit short exact sequence: a trivial one-dimensional representation sits inside a two-dimensional representation whose quotient is trivial, but the middle representation is not a direct sum of the ends.

### What happened to averaging?

Maschke's theorem proves the existence of invariant complements by starting with any linear projection onto an invariant subspace and averaging its conjugates over the group. Dividing the sum by the group order makes the average a projection commuting with the group action.

For a group of order two over a field of characteristic two, division by two is impossible because two equals zero. The argument does not merely break as a matter of technique; our explicit representation proves its conclusion is false. More generally, when the characteristic divides the finite group order, representations need not be semisimple.

Semisimple does not mean every representation has no interesting internal structure. It means that all representations can be expressed as direct sums of simple ones. In the modular example, the two-dimensional representation is not simple because it has an invariant line, and it is not a direct sum of smaller subrepresentations either. It is indecomposable but reducible. Those terms name two different properties.

### The group algebra reveals the attachment

A representation of a finite group over a field k is the same thing as a module over the group algebra k G. For our two-element group in characteristic two, write epsilon for g minus the identity. Then epsilon squared equals g squared minus two g plus one, which simplifies to zero. The group algebra is isomorphic to a truncated polynomial ring: polynomials in epsilon with epsilon squared set equal to zero.

In the two-dimensional example, epsilon sends e two to e one and sends e one to zero. Thus epsilon is a nonzero nilpotent linear operator whose square is zero. The invariant line is the image and kernel of epsilon, both spanned by e one. The representation is a module over a ring with a nonzero nilpotent element, and the failure of splitting is encoded by that nilpotent action.

Compare two modules over this ring. In one module, epsilon acts as zero on a two-dimensional vector space. That is the direct sum of two trivial modules. In the other, epsilon acts by a single two-by-two nilpotent Jordan block. Both modules have the same composition factors: two copies of the trivial simple module. But the modules are not isomorphic. Composition factors do not determine a module when extensions can be nontrivial.

### Extensions become data

A short exact sequence from A into E onto B is called an extension of B by A. Sometimes it splits, so E is a direct sum. Sometimes, as in our example, it does not. Extensions are not merely annoying exceptions; they are information that an irreducible decomposition loses.

Homological algebra provides a way to organize this information. The first Ext group, Ext one of B with A, classifies equivalence classes of module extensions of B by A, with the split extension representing zero. Higher Ext groups study more complicated obstructions and derived behavior.

For our group algebra k of epsilon with epsilon squared zero, the simple module k has epsilon acting by zero. A free resolution of this simple module is periodic: repeatedly multiply the ring by epsilon, and finally map the ring onto k by taking the quotient. Each multiplication by epsilon has image equal to kernel, because the elements annihilated by epsilon are exactly its multiples.

Apply the module homomorphism functor into k. Multiplication by epsilon induces the zero map because epsilon acts as zero on k. Consequently Ext one of k with k is a one-dimensional vector space over k. Over the two-element field, that leaves two extension classes: the split one and the nonsplit one represented by our two-dimensional module.

This calculation does not require us to classify every modular representation of every finite group. It shows why projective resolutions were worth learning. They detect precisely the data that a list of irreducible constituents misses.

### The change of viewpoint

Characteristic zero and characteristic dividing the group order lead to different questions. In the semisimple setting, character tables and decomposition multiplicities often suffice to distinguish representations up to isomorphism. In the modular setting, extension classes, projective indecomposables, block structure, and interactions between modules become central.

The two-dimensional example is small enough to inspect by hand, but it carries the conceptual transition. Having the same simple constituents does not imply being the same module. Symmetry can glue pieces together, and the glue is mathematically meaningful. Once we stop insisting that everything splits, homological algebra becomes a natural language for representation theory rather than an optional abstraction.

The failure of averaging in modular characteristic leaves room for extensions that do not split. Group cohomology turns certain such failures into computable classes.

## Group Cohomology: When a Group Extension Refuses to Split

A short exact sequence of groups tells us that one group sits inside another as a normal subgroup, and that the quotient is a third group. It is tempting to think that knowing the kernel and the quotient determines the middle group. Often it does not. The missing information is an extension class, and group cohomology gives a disciplined way to calculate it.

Take the cyclic group of order four. It contains a subgroup of order two, and its quotient by that subgroup also has order two. The direct product of two cyclic groups of order two has exactly the same kernel and quotient data. Yet the groups differ: the cyclic group of order four has an element of order four, whereas the product does not. The exact sequence alone has left something unsaid.

### Choosing representatives creates an error term

Let G be the quotient group, and let A be an abelian normal subgroup of the middle group E. Conjugation by an element of E acts on A. Because A is abelian, this action depends only on the corresponding element of G. Thus A becomes a G-module: every element of G acts on the additive group A by an automorphism.

Now choose one representative in E for each element of G. There is no promise that this choice respects multiplication. Multiply the representative of g by the representative of h. The result and the chosen representative of the product g h lie in the same coset of A. Their difference is an element of A. Call that difference f of g and h.

This difference is not random. Associativity in E forces a relation among four terms involving g, h, and k. One way to hear it is this: first multiply g and h, then k, or first multiply h and k, then g. The two answers must match. Comparing the correction terms yields the two-cocycle condition.

The condition contains the action of G on A because moving an element of the normal subgroup past a chosen representative conjugates it. For a trivial action, it reduces to a familiar-looking equation: the corrections along the two ways of multiplying three elements add to the same amount.

### Changing choices changes the formula, not the extension

A different selection of representatives changes the correction function. Suppose the new representative of g differs from the old one by some element b of g, drawn from A. Substitution shows that the new correction differs by an expression made from b of g, b of h, and b of g h. This special kind of change is called a coboundary.

Two cocycles that differ by a coboundary describe equivalent extensions with the given action. The collection of cocycles modulo coboundaries forms the second cohomology group, H two of G with coefficients in A. The zero class corresponds to an extension admitting a homomorphic section, hence to a semidirect product for that action. A nonzero class measures why there is no such splitting.

Return to the groups of order four. Let both G and A be cyclic of order two, with trivial action. For the direct product, choose the obvious representatives; multiplication introduces no correction and the cocycle is zero. For the cyclic group of order four, choose the representative of the nontrivial coset to be an element of order four. Squaring it lands in the nontrivial element of the kernel. That correction cannot be removed by changing representatives. It is the nonzero class in a cohomology group of order two.

This is an obstruction one can calculate, rather than an observation that the groups happen to look different.

### Why the other degrees appear

The second cohomology group is not isolated. Degree zero records elements of A fixed by every element of G. Degree one records crossed homomorphisms, functions that obey a modified homomorphism rule in which the action intervenes. Quotienting these functions by changes of origin gives H one. Such classes can parametrize ways of choosing complements or describing torsors, depending on the problem.

Higher cohomology appears when compatibility must be checked at yet another layer. If a candidate action of G on a nonabelian kernel is specified only up to inner automorphisms, the obstruction to constructing the desired extension can live in degree three, with appropriately chosen coefficients. This requires more hypotheses and structure than our simple abelian-kernel example. The important idea is that cohomological degree records how many layers of coherence are involved.

### An algebraic complex behind the calculation

The cocycle equation can be organized into a chain of maps between abelian groups of functions on tuples of group elements. At degree zero we have functions on a singleton, or simply elements of A. At degree one, functions on G. At degree two, functions on pairs of group elements. The differential sends a function to its failure to satisfy the next compatibility rule.

The key identity says that applying the differential twice yields zero. That is why coboundaries are automatically cocycles, and why the quotient of cocycles by coboundaries is meaningful. This is the same structural reason that homology and Ext constructions work: a complex measures the difference between being locally compatible and being globally explained by a lower-level choice.

For computations, one can construct a projective resolution of the trivial module over the group ring, apply a Hom functor, and calculate its cohomology. This relates group cohomology directly to the homological algebra already used to study modules and extensions. In standard conventions, group cohomology is Ext over the group ring.

### What the obstruction actually tells us

The point is not to classify every finite group from one formula. Cohomology depends on a specified group action and on the kind of extension being considered. But within those hypotheses it separates an arbitrary choice of representatives from the intrinsic obstruction left behind.

We began with two groups whose kernel and quotient were identical. One extension split; the other did not. The cocycle made the difference visible, and quotienting out changes of representatives made the answer independent of our bookkeeping. Group cohomology is what remains when the arbitrary choices are removed and the underlying failure to split is measured directly.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Modular Representations: When Symmetry No Longer Splits

**Track:** Abstract Algebra. **Background:** group representations, Maschke's theorem, modules, short exact sequences, and resolutions. **Central question:** what replaces a decomposition into irreducibles when the characteristic of the field divides the group order?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Find the fixed subspace of \(V\). **Answer:** \(\ker N=ke_1\).
2. Why cannot \(e_2\) span an invariant complement? **Answer:** \(g e_2=e_2+e_1\notin ke_2\).
3. Do the split and nonsplit modules have the same simple composition factors? **Yes:** two copies of \(k\); the extension class distinguishes the modules.
4. Over \(\mathbb F_3\), does this exact matrix define a \(C_2\) representation? **No:** \((I+N)^2=I+2N\ne I\). Maschke's theorem applies to \(C_2\) in characteristic three.

##### Reading and source notes

- Pavel Etingof et al., MIT OCW [Introduction to Representation Theory](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), group algebras and semisimplicity.
- Charles A. Weibel, [An Introduction to Homological Algebra](https://doi.org/10.1017/CBO9781139644136), projective resolutions and Ext.

### Group Cohomology: When a Group Extension Refuses to Split

**Track:** Abstract Algebra. **Background:** group actions, exact sequences, modules, cocycles and quotient groups. **Central question:** how can one measure the obstruction to rebuilding a group from its kernel and quotient?

#### Mathematical companion (not spoken)

Let G act on an abelian group A. An extension inducing this action is \(1\to A\to E\to G\to1\). Choose a set-theoretic section \(s:G\to E\), with \(s(1)=1\). In additive notation for A define
\[s(g)s(h)=f(g,h)s(gh),\qquad f(g,h)\in A.\]
Associativity gives the **2-cocycle condition**
\[f(g,h)+f(gh,k)=g\cdot f(h,k)+f(g,hk).\]
For another section \(s'(g)=b(g)s(g)\),
\[f'(g,h)=f(g,h)+b(g)+g\cdot b(h)-b(gh).\]
Hence equivalence classes of extensions inducing the fixed G-action correspond to \(H^2(G,A)=Z^2(G,A)/B^2(G,A)\). The zero class gives a split extension (semidirect product). For trivial action and \(G=A=C_2\), \(H^2(C_2,C_2)\cong C_2\). The nontrivial class realizes \(C_4\), whereas the zero class realizes \(C_2\times C_2\).

More generally \(H^n(G,A)\cong\operatorname{Ext}^n_{\mathbb Z[G]}(\mathbb Z,A)\), with the trivial action on \(\mathbb Z\). This identity uses left-module conventions consistently.

##### Exercises with answers

1. Why is A automatically a G-module when A is an abelian normal subgroup of E? **Answer:** conjugation by representatives of a coset differs by an inner automorphism of A, which is trivial because A is abelian.
2. What does a zero class in \(H^2(G,A)\) say? **Answer:** the extension admits a homomorphic splitting and is isomorphic to the semidirect product determined by the action.
3. Why does \(C_4\) not split as an extension of \(C_2\) by \(C_2\)? **Answer:** any section sending the nonidentity quotient element to a group element would need an element of order two outside the kernel; no such element exists.
4. What is \(H^0(G,A)\)? **Answer:** \(A^G=\{a:g\cdot a=a\ \forall g\}\).

##### Reading and source notes

- Kenneth S. Brown, [*Cohomology of Groups*](https://link.springer.com/book/10.1007/978-1-4684-9327-6), low-dimensional group cohomology and extensions.
- [MIT OpenCourseWare, Algebra II](https://ocw.mit.edu/courses/18-702-algebra-ii-spring-2011/), background on groups and extensions.
- Charles Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), derived-functor interpretation.
