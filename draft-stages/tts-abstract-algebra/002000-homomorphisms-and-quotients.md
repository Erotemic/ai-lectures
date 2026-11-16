# 002000 — Homomorphisms, Kernels, and Quotients: The Structure a Map Preserves

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** groups and function composition. **Question:** what does it mean to simplify a group without lying about multiplication?

<!-- BEGIN SPOKEN LECTURE -->

# Homomorphisms, Kernels, and Quotients

There is a clock with twelve marked positions. If we advance its hand seven hours and then another eight hours, the final hand position is the same as advancing fifteen hours and reducing by twelve. Ordinary integer addition and clock arithmetic differ in the numbers they remember, but they agree about composition. We can forget the number of complete revolutions without breaking addition.

That controlled forgetting is a homomorphism. It is one of algebra's most powerful constructions, because it lets us compare complicated objects through simpler ones while tracking exactly what has been lost.

## Preserve the operation, not the labels

A homomorphism from a group G to a group H is a function phi such that phi of a times b equals phi of a combined with phi of b, for all elements a and b of G. We use multiplication language for a general group, even when the example is addition. The equation says that combining first and mapping later gives the same answer as mapping first and then combining.

For the integers under addition and the twelve clock positions under addition modulo twelve, phi sends each integer to its remainder modulo twelve. Phi of seven plus eight is the residue three. Phi of seven plus phi of eight is also three on the clock. The map is many-to-one: zero, twelve, twenty-four, and negative twelve all point to the same clock position.

Why care about the preserving equation? Because it carries proofs. If phi is a homomorphism, it sends the identity of G to the identity of H. To see this, phi of the identity multiplied by phi of any element equals phi of that element. Since phi of an identity times an element is the element itself, cancellation in H forces phi of the identity to equal H's identity. A similar argument shows that the image of an inverse is the inverse of the image.

Thus the homomorphism cannot preserve multiplication while arbitrarily scrambling the meaning of doing nothing or undoing an action. Those features come along automatically.

## What disappears is the kernel

The kernel of a homomorphism consists of all elements of G mapped to the identity of H. For the reduction map from integers to a twelve-hour clock, the kernel is the multiples of twelve. They are precisely the changes that the clock cannot detect.

For a second example, let a permutation have sign plus one if it can be written as an even number of pair swaps, and minus one if that number is odd. The parity of the number of swaps is well-defined despite there being many ways to express a permutation. Taking the sign of a composition multiplies the signs. The sign map from permutations of three objects to plus or minus one under multiplication is a homomorphism. Its kernel consists of the even permutations. The map forgets which even permutation we performed, retaining only parity.

The kernel is a subgroup. If two elements map to the identity, their product does too; the identity maps to the identity; and the inverse of an element in the kernel remains in the kernel. There is a stronger property that we will need. If k is in the kernel and g is any group element, then g times k times the inverse of g also maps to the identity. This follows by applying the homomorphism to the three factors: phi of g, followed by the identity, followed by phi of g inverse. They cancel.

A subgroup preserved under every such conjugation is called normal. Every kernel is normal. It is normality, rather than merely being a subgroup, that allows a collection of elements to be collapsed into an identity in a way consistent with multiplication.

## Cosets as indistinguishable cases

Take the integers again. Two integers have the same remainder modulo twelve exactly when their difference is divisible by twelve. Equivalently, they differ by an element of the kernel. This divides the integers into twelve classes. One class contains all multiples of twelve. Another contains numbers one more than a multiple of twelve, and so forth.

In a general group, fixing a subgroup N, a left coset g N is the collection of products g n as n ranges through N. If N is the kernel of phi, every member of g N has the same image under phi as g. Conversely, if phi of g equals phi of h, then the inverse of h times g lies in the kernel, so g is in h N. Thus the fibers of a homomorphism are exactly the kernel cosets, at least when we look at the part of H actually reached by the map.

This is a proof that the kernel measures the collapse. Not every difference between two elements is lost; precisely those in the same kernel coset are identified.

We want to multiply cosets by choosing representatives: take the coset of g and the coset of h, combine their representatives, and declare the answer to be the coset of g h. But what if someone chooses other representatives of the same two cosets? A mathematical operation must not change because of an arbitrary choice of notation.

For a normal subgroup N, that problem is solved. Replacing g with g n and h with h m changes the product to g n h m. Move n past h by rewriting it as h times h inverse n h. Since N is normal, the conjugated factor remains in N. So the new product differs from g h by a factor belonging to N. Both representative choices yield the same coset. The set of cosets with this operation is a group, written G modulo N.

## Why normality is necessary

Consider the symmetries of a square and choose the two-element subgroup containing the identity and one particular reflection s. If we conjugate that reflection by a quarter-turn, we generally obtain a reflection across a different axis. It is not in our chosen two-element subgroup. So the subgroup is not normal.

We can form a collection of left cosets as sets, but the proposed multiplication of cosets need not be well-defined. We cannot legitimately declare the reflection s to be the identity while leaving the rest of the group unchanged. Because conjugation moves it to another reflection, the group multiplication would force additional identifications. A quotient must respect all of the original relations.

This is the algebraic reason that simply putting elements into boxes does not automatically produce a new group. The boxes must cooperate with the operation.

## The first isomorphism theorem

An isomorphism is a bijective homomorphism: a way to relabel one group as another without changing its multiplication structure. The first isomorphism theorem says that a homomorphism phi from G to H identifies the quotient G by its kernel with the image of phi inside H.

We can prove the essential claim in a few steps. From a coset g times the kernel, define a map to phi of g. It is well-defined because any two representatives of the same coset have the same image. It preserves multiplication because phi does. It is onto the image of phi by the very definition of image. It is injective because if phi of g equals phi of h, then g and h belong to the same kernel coset. Hence the quotient and the image have exactly the same group structure.

For the clock, this says the integers divided by the multiples of twelve form the group of residues modulo twelve. For permutation signs, the group of all permutations modulo the even permutations has two elements and is isomorphic to the two-element sign group. Both examples are cases of the same theorem.

The theorem does not say that G and H are isomorphic. A homomorphism may reach only a subgroup of H, and it may identify many elements in G. The correct statement specifies both the kernel and the image. Leaving either out produces a stronger claim that need not be true.

## From arithmetic to algebraic architecture

We have a useful triangle of ideas. A group gives us operations that can be combined and undone. A homomorphism gives us a translation that respects those operations. A normal subgroup records exactly what that translation can erase. The quotient then describes the surviving information, while the first isomorphism theorem confirms that the surviving structure matches the image.

These ideas recur far beyond group theory. Kernels and images occur in linear algebra. Ideals are the right kind of kernels for rings. Exact sequences, later, make the relationship among images and kernels a subject in its own right. The common theme is not forgetting everything: it is forgetting only what the structure allows us to forget.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A group homomorphism \(\varphi:G\to H\) satisfies \(\varphi(gh)=\varphi(g)\varphi(h)\). Define
\[
\ker\varphi=\{g\in G:\varphi(g)=e_H\},\qquad
\operatorname{im}\varphi=\{\varphi(g):g\in G\}.
\]
For all \(g\in G\) and \(k\in\ker\varphi\), \(\varphi(gkg^{-1})=e_H\); hence \(\ker\varphi\trianglelefteq G\). If \(N\trianglelefteq G\), the product \((gN)(hN)=(gh)N\) is well-defined.

**First isomorphism theorem.** \(G/\ker\varphi\cong\operatorname{im}\varphi\) by \(g\ker\varphi\mapsto\varphi(g)\). For \(\mathbb Z\to\mathbb Z/12\mathbb Z\), the kernel is \(12\mathbb Z\). For the sign homomorphism \(S_3\to\{\pm1\}\), the kernel is \(A_3\), the alternating group.

### Exercises with answers

1. What is the kernel of reduction \(\mathbb Z\to\mathbb Z/5\mathbb Z\)? **Answer:** \(5\mathbb Z\).
2. If a homomorphism has trivial kernel, is it injective? **Answer:** Yes; equal images imply the quotient of the inputs lies in the kernel, hence the inputs agree.
3. Must a homomorphism be surjective? **Answer:** No; the inclusion of a subgroup into a larger group is a homomorphism.
4. Why can an arbitrary subgroup fail to yield a quotient group? **Answer:** Different coset representatives may give different products; normality is the condition that prevents this.

### Reading

Judson, *Abstract Algebra: Theory and Applications*, group homomorphisms and quotient groups; Artin, MIT 18.701, homomorphisms, cosets, and correspondence theorem.
