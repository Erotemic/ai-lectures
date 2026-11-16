# 021000 — Ext, Long Exact Sequences, and the Algebra of Extensions

**Track:** Abstract Algebra. **Background:** modules, exact sequences, projective resolutions, modular representations. **Central question:** how can we compute and compare ways of joining modules, including joins that do not split?

<!-- BEGIN SPOKEN LECTURE -->

# Ext, Long Exact Sequences, and the Algebra of Extensions

Suppose you know the two ends of a short exact sequence, a module A sitting inside a larger module E, and a quotient B. Do A and B tell you what E must be? In linear algebra over a field, the answer is yes up to isomorphism. Choose a basis of A, extend it to a basis of E, and the sequence splits. For modules over a general ring, that basis-extension argument can fail. The way the pieces attach is new information.

The group called Ext one of B with A measures that information. A zero element represents a split sequence. A nonzero element represents a nonsplit attachment. The power of this definition is not just that it names a phenomenon. Ext can be calculated from a presentation, fitted into a long exact sequence, and used to prove that certain extensions cannot exist.

## Start with ordinary abelian groups

Every abelian group is a module over the integers. This gives us an example where no exotic coefficients are needed. Consider the group of integers modulo four. It contains the subgroup consisting of zero and two, isomorphic to the integers modulo two. The quotient by that subgroup is again the integers modulo two. So we have a short exact sequence with two copies of the two-element group at its ends and the four-element cyclic group in the middle.

Compare it with the split sequence whose middle group is the direct product of two copies of the two-element group. The ends are identical in both sequences. But in one middle group there is an element of order four; in the other, every nonzero element has order two. No isomorphism can erase that difference.

These are two different extension classes. If we classify only the composition factors, both groups look like two copies of the same simple piece. Ext records the glue.

## Calculating Ext from a free resolution

Let B be the integers modulo n. There is an exact sequence of integer modules: one copy of the integers maps to another by multiplication by n, and the second maps onto the integers modulo n. The integers are free, so the first two terms provide a projective resolution of B.

To compute Ext one of B with A, apply the Hom functor into A. A homomorphism from the integers into A is determined by the image of one, so Hom from the integers to A is naturally A itself. The map induced by multiplying by n becomes multiplication by n on A. The first Ext group is the cokernel of that map: A modulo the subgroup of n-fold multiples.

For A equal to the integers modulo m, the answer is a cyclic group whose order is the greatest common divisor of n and m. In particular, Ext one of the two-element group with itself has two elements. One is the split class. The other is represented by our four-element cyclic group.

Notice a subtle point about the order of the inputs. Ext is computed by resolving its first argument, B, and then taking Hom into its second argument, A. In general, swapping those arguments is not an innocent operation. The groups need not agree.

## Why a sequence becomes a long sequence

Hom is left exact. It detects kernels correctly, but taking Hom does not always preserve a surjection. An extension that fails to split is precisely the sort of obstruction that appears when a desired lifting map cannot be constructed.

Start with a short exact sequence from A prime into A onto A double prime, and fix a target module T. Taking Hom into T produces arrows in the opposite direction: first Hom from A double prime into T, then Hom from A into T, then Hom from A prime into T. Those first terms form an exact sequence, but the last map may fail to be onto.

What comes after that failure? A connecting homomorphism sends a map from A prime to T to an element of Ext one of A double prime with T. If you continue, you obtain a long exact sequence involving Ext one, Ext two, and the higher derived groups. The connecting maps do not merely pad out a diagram: they turn failures of lifting into computable obstructions.

There is a complementary long exact sequence obtained by fixing the first argument and varying the target module in a short exact sequence. Because Hom into that target is covariant, its arrows have the forward direction. Always check which argument you are varying before writing the diagram.

## The connecting map as a concrete operation

Consider a short exact sequence from A prime into A onto A double prime. Suppose someone gives us a homomorphism from A prime to a target T, and asks whether it extends to a homomorphism from all of A to T. If it does, the obstruction is zero. If not, we can form an extension of A double prime by T by taking a pushout along the given map. The new middle module is built by identifying the copy of A prime inside A with its image in T.

This pushout extension represents the connecting Ext class. Its class vanishes exactly when the original map extends, under the usual module-category hypotheses. Thus an algebraic element records a very ordinary question: can a map defined on a submodule be extended?

That viewpoint gives the long exact sequence a reason to exist. Its arrows link specific extension and lifting questions; exactness says that an obstruction vanishes precisely when a prior step succeeds.

## The Yoneda description

There is another way to meet Ext one without mentioning resolutions. Take all short exact sequences with fixed ends A and B. Two sequences are equivalent if there is an isomorphism between the middle modules making the endpoint maps commute and fixing those endpoint identifications. Equivalence matters: merely knowing that two middle modules are isomorphic is not enough when the embeddings and quotients differ.

These equivalence classes can be added by a construction called the Baer sum. One combines two extensions using a pullback over B and a pushout along addition in A. The split extension is the identity. With this addition, the extension classes form an abelian group, naturally isomorphic to Ext one of B with A.

For higher Ext, equivalence classes of longer exact sequences give the Yoneda interpretation. Composing extensions resembles composing obstructions. The resolution calculation and the extension-class construction are two views of the same invariant.

## What Ext cannot tell you by itself

An Ext group classifies extensions only after the ring and both end modules have been specified. Knowing that an Ext group is nonzero does not mean every middle module is indecomposable. Knowing it is zero means every short exact sequence with those ends splits, not that every module in the category is semisimple. And the underlying set of extensions is not classified just by the sizes of their endpoints: module structure, maps, and the equivalence relation are essential.

The practical lesson is that failure to split is structured, not accidental. Free resolutions convert it into a cokernel computation. Long exact sequences transport it along other exact sequences. The Yoneda viewpoint says what the computation means: it classifies ways of fitting one module inside another. The algebraic glue can be computed as precisely as the pieces it joins.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Fix a ring \(R\) and left \(R\)-modules \(B,A\). For a projective resolution \(P_\bullet\twoheadrightarrow B\),
\[
\operatorname{Ext}^i_R(B,A)=H^i\bigl(\operatorname{Hom}_R(P_\bullet,A)\bigr).
\]
Under the usual module-category hypotheses, Yoneda equivalence classes of short exact sequences \(0\to A\to E\to B\to0\) identify naturally with \(\operatorname{Ext}^1_R(B,A)\), with zero represented by split extensions.

Over \(R=\mathbb Z\), the resolution \(0\to\mathbb Z\xrightarrow{\times n}\mathbb Z\to\mathbb Z/n\to0\) yields
\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong A/nA,\qquad
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong\mathbb Z/\gcd(n,m).
\]
The \(n=m=2\) cases include \(0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0\) (nonzero class) and \(0\to\mathbb Z/2\to(\mathbb Z/2)^2\to\mathbb Z/2\to0\) (zero class).

For \(0\to A'\to A\to A''\to0\), the **contravariant first-variable** sequence begins
\[
0\to\operatorname{Hom}(A'',T)\to\operatorname{Hom}(A,T)\to\operatorname{Hom}(A',T)
\xrightarrow{\delta}\operatorname{Ext}^1(A'',T)\to\operatorname{Ext}^1(A,T)\to\cdots.
\]
The connecting map \(\delta(f)\) is represented by the pushout of the given extension along \(f:A'\to T\). It vanishes iff \(f\) extends to \(A\to T\). Higher derived terms continue this sequence. Similarly a short exact sequence in the **second** variable gives a covariant long exact sequence.

### Exercises with answers

1. Compute \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/6,\mathbb Z/4)\). **Answer:** \((\mathbb Z/4)/6(\mathbb Z/4)\cong\mathbb Z/2\).
2. Is \(0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0\) split? **No:** there is no subgroup complementary to the unique order-two subgroup.
3. What happens when the first argument is a projective module \(P\)? **Answer:** \(\operatorname{Ext}^i_R(P,A)=0\) for every \(i>0\).
4. Why does the \(\operatorname{Hom}(-,T)\) sequence reverse arrows? **Answer:** it acts by precomposition, making Hom contravariant in its first argument.

### Reading and source notes

- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), chapters on derived functors, connecting maps, and Yoneda Ext.
- Kiran Kedlaya, [MIT 18.726 homological algebra lecture](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/resources/mit18_726s09_lec16_homalg/).
