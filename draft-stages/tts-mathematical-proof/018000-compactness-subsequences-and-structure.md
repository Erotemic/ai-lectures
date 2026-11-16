# 018000 — Compactness and Subsequence Proofs: From Infinity to Finite Control

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sequence limits, completeness, and elementary sets. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Compactness and Subsequence Proofs: From Infinity to Finite Control

In analysis and topology, many important conclusions come from a principle of finite control. An infinite collection of possibilities may be too large to inspect one by one, but compactness often lets us pass to finitely many pieces or extract a convergent subsequence. These two descriptions are closely related in Euclidean space. Understanding their proofs shows how definitions and completeness work together.

## An open-cover version of compactness

A collection of open sets is an open cover of a set K if every point of K lies in at least one member of the collection. A set is compact if every such cover has a finite subcollection that still covers K. The statement does not say that the original cover is finite. It says no matter how many open sets are offered, enough of them can be chosen finitely to cover the whole set.

Why is the closed interval from zero to one compact? The standard proof uses the completeness of the real numbers. Given an arbitrary open cover, define S to be the collection of points t in the interval such that the subinterval from zero through t is already covered by finitely many members of the original cover. Since some open set contains zero, a short initial interval has a finite cover, so S is nonempty. Since S is bounded above by one, let s be its supremum.

Choose an open set from the cover containing s. Because it is open, it contains a small interval around s. From the definition of supremum, some point t in S lies inside that neighborhood just to the left of s, unless s is the left endpoint, which has already been handled. A finite cover of zero through t, supplemented by the one open set containing s, extends beyond s. This contradicts maximality unless s is one. The same neighborhood argument at one then ensures the entire interval has a finite subcover. The details matter: openness is what permits extension, and completeness is what supplies the supremum.

## A bounded sequence and nested intervals

A related theorem says every bounded sequence of real numbers has a convergent subsequence. Put the sequence in some closed bounded interval. Split the interval into two halves. At least one half contains infinitely many terms of the sequence; choose it. Split that half again and choose a half containing infinitely many terms. Continue, obtaining nested closed intervals with lengths tending to zero.

Choose indices in increasing order, one from each chosen interval, using the fact that the intervals contain infinitely many terms. Completeness gives a unique point in all the nested intervals, and the selected subsequence approaches that point because its terms lie in intervals of shrinking length. The conclusion is a convergent subsequence, not convergence of the entire original sequence. Alternating one and minus one provides the distinction.

## Compactness controls continuous functions

A continuous function maps compact sets to compact sets. Here is the open-cover proof. Suppose an open cover of the image is given. Take the inverse image of each covering open set. Continuity makes these inverse images open in the domain, and together they cover the compact source set. Choose finitely many. Their corresponding image-cover members then cover the entire image. The proof is a composition of two definitions: continuity preserves openness of inverse images, and compactness supplies finiteness.

A nonempty compact subset of the real line is closed and bounded, so a continuous real-valued function on a compact set attains a maximum and a minimum. This is the extreme value theorem. The word 'attains' is stronger than merely having a finite supremum. On the open interval from zero to one, f of x equal to x has supremum one but never reaches it. Compactness closes that gap.

## Sequential and open-cover language have limits

In metric spaces, compactness and the property that every sequence has a convergent subsequence are equivalent. In arbitrary topological spaces the two notions can differ; not every topological space is characterized by sequences alone. It is therefore unsafe to transplant a sequential proof to a general topology problem without checking the space's hypotheses. This is precisely the kind of hidden prerequisite that a foundational proof course should make visible.

We now have a bridge from elementary logical form to some of the strongest statements in introductory analysis. A proof of compactness begins with an arbitrary open cover and constructs a finite subcover. A proof using subsequences begins with an arbitrary sequence and constructs a convergent subsequence. A continuity argument takes an arbitrary target cover and pulls it back. These are different objects, but they share the same discipline: read the quantifiers, produce the objects the definition requires, and justify the step where infinite data becomes finite or convergent. That discipline is what makes advanced mathematics readable.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Compactness and subsequence principles

A set \(K\) is compact if every open cover \(\{U_i\}_{i\in I}\) of \(K\) contains finitely many members still covering \(K\). In \(\mathbb R^n\), Heine–Borel says compact \(\iff\) closed and bounded. In metric spaces, compact \(\iff\) every sequence has a convergent subsequence with limit in the space.

If \(f:K\to Y\) is continuous and \(\{V_i\}\) is an open cover of \(f(K)\), then the preimages \(\{f^{-1}(V_i)\}\) form an open cover of \(K\). Finite reduction on \(K\) supplies a finite subcover of \(f(K)\). Thus continuous images of compact spaces are compact.

### Exercises with answers

1. Show \((0,1)\) is not compact. **Answer:** the open sets \(U_n=(1/n,1)\) for integers \(n\ge2\) cover \((0,1)\) but no finite subfamily covers it.
2. Find a convergent subsequence of \((-1)^n\). **Answer:** choose even indices to obtain the constant subsequence \(1\).
3. Why does a continuous real function on \([0,1]\) attain a maximum? **Answer:** its image is nonempty compact in \(\mathbb R\), hence closed and bounded and contains its supremum.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [OpenStax, Calculus Volume 1, Rice University](https://openstax.org/books/calculus-volume-1/pages/preface).
- [Wikipedia: Heine%E2%80%93Borel theorem](https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem).
