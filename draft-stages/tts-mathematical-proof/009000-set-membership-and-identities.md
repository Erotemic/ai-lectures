# 009000 — Sets and Subsets: Proving Two Collections Are Equal

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Logic and quantified definitions. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Sets and Subsets: Proving Two Collections Are Equal

A set is a collection of objects, and the most important statement about a set is whether a particular object belongs to it. That simple relation allows us to define subsets, unions, intersections, complements, and products. It also gives an efficient proof technique: to establish a set identity, reason about an arbitrary element and show that membership is equivalent on both sides.

Suppose A is the set of integers divisible by two, and B is the set of integers divisible by three. Their intersection contains the multiples of six. The union contains integers divisible by at least one of two or three. These are different operations. If an integer belongs to A intersect B, it satisfies both conditions. If it belongs to A union B, it satisfies at least one.

## Proving inclusion and equality

To prove A is a subset of B, take an arbitrary x in A and prove x is in B. To prove A equals B, prove both A is a subset of B and B is a subset of A. A one-direction argument gives only inclusion, and examples cannot establish a set identity for arbitrary sets.

Consider the distributive law: A intersect the union of B and C equals the union of A intersect B with A intersect C. Begin with an element x on the left. It belongs to A, and it belongs to B or C. If it belongs to B, then it lies in A intersect B. If it belongs to C, it lies in A intersect C. So it lies on the right. Conversely, if x lies in either A intersect B or A intersect C, then it belongs to A and to at least one of B and C, putting it on the left. The algebraic identity has become a pair of logical arguments about membership.

## Complements and De Morgan's laws

Complements are always relative to a universe U. The complement of A consists of the elements of U not in A. If we forget U, expressions such as 'everything outside A' become ambiguous. De Morgan's laws say that the complement of A intersect B is the union of the complements, and that the complement of A union B is the intersection of the complements. Translate membership in the complement into 'not,' then use the corresponding logical law.

A similar method shows that A minus B equals A intersect the complement of B, again relative to a universe containing both sets. This is not a slogan about drawing overlapping circles. It is a membership proof that works for arbitrary sets, finite or infinite, even when drawing them is impractical.

## Subsets, elements, and the empty set

Distinguish 'x is an element of A' from 'A is a subset of B.' An element is an object in a collection; a subset is itself a collection whose elements all occur in another collection. The empty set is a subset of every set because there is no element of it that violates containment. However, the empty set is not automatically an element of every set. For example, it is not an element of the set containing only the number three.

The power set of A is the set of all subsets of A. If A contains exactly two distinct objects, its power set has four members: the empty set, the first singleton, the second singleton, and A itself. For a finite set with n elements, there are two to the n subsets, because each element may independently be included or excluded. This is an elementary counting proof with the structure of a binary choice for every element.

## Why unrestricted collections need care

One might try to define a set of all sets that are not members of themselves. If such a set R belonged to itself, its defining property would say it did not. If it did not belong to itself, the defining property would say it did. This is Russell's paradox. Modern axiomatic set theory avoids allowing every verbal property to define an unrestricted set. In everyday mathematical work, we often form subsets of an already specified universe, which avoids this immediate problem.

The lesson is not that sets are unreliable. It is that the domain and the rules for forming collections are part of mathematical foundations, just as domains mattered for quantifiers. The basic proof method—start with an arbitrary member and verify its properties—remains enormously useful.

Once you are comfortable with these arguments, set operations stop being decorative notation. They become a language for logical conditions. In topology, open-set arguments use unions and finite intersections. In probability, events are sets and probabilities apply to their unions and complements. In analysis, measurability is a property of collections of subsets. In all these subjects, a set identity is proved by controlling membership, not by trusting a diagram.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Membership proof of distributivity

For any \(x\),
\[
\begin{aligned}
x\in A\cap(B\cup C)
&\iff (x\in A)\land[(x\in B)\lor(x\in C)]\\
&\iff [(x\in A)\land(x\in B)]\lor[(x\in A)\land(x\in C)]\\
&\iff x\in(A\cap B)\cup(A\cap C).
\end{aligned}
\]
As the equivalence holds for every \(x\), the sets are equal.

### Exercises with answers

1. Prove \(A\setminus B=A\cap B^c\) relative to universe \(U\). **Answer:** both sides contain exactly the elements of \(A\) that are not in \(B\).
2. Is \(\varnothing\subseteq A\) always true? **Answer:** yes; no element violates inclusion.
3. Is \(\varnothing\in A\) always true? **Answer:** no; e.g. \(A=\{3\}\).
4. List the power set of \(\{a,b\}\). **Answer:** \(\{\varnothing,\{a\},\{b\},\{a,b\}\}\).

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Set (mathematics)](https://en.wikipedia.org/wiki/Set_(mathematics)).
