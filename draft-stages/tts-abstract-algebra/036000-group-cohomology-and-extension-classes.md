# 036000 — Group Cohomology: When a Group Extension Refuses to Split

**Track:** Abstract Algebra. **Background:** group actions, exact sequences, modules, cocycles and quotient groups. **Central question:** how can one measure the obstruction to rebuilding a group from its kernel and quotient?

<!-- BEGIN SPOKEN LECTURE -->

# Group Cohomology: When a Group Extension Refuses to Split

A short exact sequence of groups tells us that one group sits inside another as a normal subgroup, and that the quotient is a third group. It is tempting to think that knowing the kernel and the quotient determines the middle group. Often it does not. The missing information is an extension class, and group cohomology gives a disciplined way to calculate it.

Take the cyclic group of order four. It contains a subgroup of order two, and its quotient by that subgroup also has order two. The direct product of two cyclic groups of order two has exactly the same kernel and quotient data. Yet the groups differ: the cyclic group of order four has an element of order four, whereas the product does not. The exact sequence alone has left something unsaid.

## Choosing representatives creates an error term

Let G be the quotient group, and let A be an abelian normal subgroup of the middle group E. Conjugation by an element of E acts on A. Because A is abelian, this action depends only on the corresponding element of G. Thus A becomes a G-module: every element of G acts on the additive group A by an automorphism.

Now choose one representative in E for each element of G. There is no promise that this choice respects multiplication. Multiply the representative of g by the representative of h. The result and the chosen representative of the product g h lie in the same coset of A. Their difference is an element of A. Call that difference f of g and h.

This difference is not random. Associativity in E forces a relation among four terms involving g, h, and k. One way to hear it is this: first multiply g and h, then k, or first multiply h and k, then g. The two answers must match. Comparing the correction terms yields the two-cocycle condition.

The condition contains the action of G on A because moving an element of the normal subgroup past a chosen representative conjugates it. For a trivial action, it reduces to a familiar-looking equation: the corrections along the two ways of multiplying three elements add to the same amount.

## Changing choices changes the formula, not the extension

A different selection of representatives changes the correction function. Suppose the new representative of g differs from the old one by some element b of g, drawn from A. Substitution shows that the new correction differs by an expression made from b of g, b of h, and b of g h. This special kind of change is called a coboundary.

Two cocycles that differ by a coboundary describe equivalent extensions with the given action. The collection of cocycles modulo coboundaries forms the second cohomology group, H two of G with coefficients in A. The zero class corresponds to an extension admitting a homomorphic section, hence to a semidirect product for that action. A nonzero class measures why there is no such splitting.

Return to the groups of order four. Let both G and A be cyclic of order two, with trivial action. For the direct product, choose the obvious representatives; multiplication introduces no correction and the cocycle is zero. For the cyclic group of order four, choose the representative of the nontrivial coset to be an element of order four. Squaring it lands in the nontrivial element of the kernel. That correction cannot be removed by changing representatives. It is the nonzero class in a cohomology group of order two.

This is an obstruction one can calculate, rather than an observation that the groups happen to look different.

## Why the other degrees appear

The second cohomology group is not isolated. Degree zero records elements of A fixed by every element of G. Degree one records crossed homomorphisms, functions that obey a modified homomorphism rule in which the action intervenes. Quotienting these functions by changes of origin gives H one. Such classes can parametrize ways of choosing complements or describing torsors, depending on the problem.

Higher cohomology appears when compatibility must be checked at yet another layer. If a candidate action of G on a nonabelian kernel is specified only up to inner automorphisms, the obstruction to constructing the desired extension can live in degree three, with appropriately chosen coefficients. This requires more hypotheses and structure than our simple abelian-kernel example. The important idea is that cohomological degree records how many layers of coherence are involved.

## An algebraic complex behind the calculation

The cocycle equation can be organized into a chain of maps between abelian groups of functions on tuples of group elements. At degree zero we have functions on a singleton, or simply elements of A. At degree one, functions on G. At degree two, functions on pairs of group elements. The differential sends a function to its failure to satisfy the next compatibility rule.

The key identity says that applying the differential twice yields zero. That is why coboundaries are automatically cocycles, and why the quotient of cocycles by coboundaries is meaningful. This is the same structural reason that homology and Ext constructions work: a complex measures the difference between being locally compatible and being globally explained by a lower-level choice.

For computations, one can construct a projective resolution of the trivial module over the group ring, apply a Hom functor, and calculate its cohomology. This relates group cohomology directly to the homological algebra already used to study modules and extensions. In standard conventions, group cohomology is Ext over the group ring.

## What the obstruction actually tells us

The point is not to classify every finite group from one formula. Cohomology depends on a specified group action and on the kind of extension being considered. But within those hypotheses it separates an arbitrary choice of representatives from the intrinsic obstruction left behind.

We began with two groups whose kernel and quotient were identical. One extension split; the other did not. The cocycle made the difference visible, and quotienting out changes of representatives made the answer independent of our bookkeeping. Group cohomology is what remains when the arbitrary choices are removed and the underlying failure to split is measured directly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let G act on an abelian group A. An extension inducing this action is \(1\to A\to E\to G\to1\). Choose a set-theoretic section \(s:G\to E\), with \(s(1)=1\). In additive notation for A define
\[s(g)s(h)=f(g,h)s(gh),\qquad f(g,h)\in A.\]
Associativity gives the **2-cocycle condition**
\[f(g,h)+f(gh,k)=g\cdot f(h,k)+f(g,hk).\]
For another section \(s'(g)=b(g)s(g)\),
\[f'(g,h)=f(g,h)+b(g)+g\cdot b(h)-b(gh).\]
Hence equivalence classes of extensions inducing the fixed G-action correspond to \(H^2(G,A)=Z^2(G,A)/B^2(G,A)\). The zero class gives a split extension (semidirect product). For trivial action and \(G=A=C_2\), \(H^2(C_2,C_2)\cong C_2\). The nontrivial class realizes \(C_4\), whereas the zero class realizes \(C_2\times C_2\).

More generally \(H^n(G,A)\cong\operatorname{Ext}^n_{\mathbb Z[G]}(\mathbb Z,A)\), with the trivial action on \(\mathbb Z\). This identity uses left-module conventions consistently.

### Exercises with answers

1. Why is A automatically a G-module when A is an abelian normal subgroup of E? **Answer:** conjugation by representatives of a coset differs by an inner automorphism of A, which is trivial because A is abelian.
2. What does a zero class in \(H^2(G,A)\) say? **Answer:** the extension admits a homomorphic splitting and is isomorphic to the semidirect product determined by the action.
3. Why does \(C_4\) not split as an extension of \(C_2\) by \(C_2\)? **Answer:** any section sending the nonidentity quotient element to a group element would need an element of order two outside the kernel; no such element exists.
4. What is \(H^0(G,A)\)? **Answer:** \(A^G=\{a:g\cdot a=a\ \forall g\}\).

### Reading and source notes

- Kenneth S. Brown, [*Cohomology of Groups*](https://link.springer.com/book/10.1007/978-1-4684-9327-6), low-dimensional group cohomology and extensions.
- [MIT OpenCourseWare, Algebra II](https://ocw.mit.edu/courses/18-702-algebra-ii-spring-2011/), background on groups and extensions.
- Charles Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), derived-functor interpretation.
