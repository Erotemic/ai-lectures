# 011000 — Equivalence Relations: Building New Objects by Identifying Old Ones

**Track:** Mathematical Reasoning and Proof from First Principles. **Background:** Sets and functions. **Purpose:** teach an actual proof obligation and the reasoning required to discharge it.

<!-- BEGIN SPOKEN LECTURE -->

# Equivalence Relations: Building New Objects by Identifying Old Ones

Sometimes different descriptions represent the same mathematical object. The fractions one half and two quarters are different ordered pairs of integers, but they represent the same rational number. The clock readings one o'clock and thirteen o'clock denote the same hour modulo twelve. In geometry, points on the two ends of a strip may be identified to make a cylinder. To reason rigorously about such constructions, we need equivalence relations and quotient sets.

An equivalence relation on a set satisfies three properties. Every element is related to itself; this is reflexivity. If a is related to b, then b is related to a; this is symmetry. If a is related to b and b is related to c, then a is related to c; this is transitivity. These are not arbitrary decorations. They guarantee that 'being the same for the purpose at hand' behaves consistently.

## Congruence as a complete example

On the integers, define a relation: a is equivalent to b when a minus b is divisible by three. Reflexivity holds because a minus a is zero, which is divisible by three. Symmetry holds because if a minus b equals three k, then b minus a equals three times minus k. Transitivity holds because if a minus b and b minus c are multiples of three, their sum a minus c is also a multiple of three.

The integers fall into three equivalence classes: those congruent to zero, one, and two modulo three. We can give each class a convenient representative, but a class contains every integer related to that representative. The quotient set consists of classes, not of a particular three-element list chosen by fiat.

## Why 'well-defined' deserves a proof

We want to add two congruence classes by choosing representatives, adding the integers, and taking the class of the sum. But what if we choose different representatives? Suppose a is congruent to a prime and b to b prime, modulo three. Then a minus a prime and b minus b prime are multiples of three. Their sum is a plus b minus a prime minus b prime, also a multiple of three. Thus both choices produce the same output class. Addition on the quotient is well-defined.

The word 'well-defined' means the rule depends only on the mathematical object, not on the accidental description we used to compute it. This is a frequent issue in advanced mathematics. A vector in a quotient space has many representatives. A differential form's coordinate formula varies across charts. A function on equivalence classes must give the same answer no matter which representative is used.

## Not every proposed operation descends

Suppose we try to assign to a congruence class modulo three the ordinary integer 'the square of its representative' rather than the square class. Zero and three represent the same class, but their integer squares are zero and nine. The proposed integer-valued rule is not well-defined. If instead we take the class of the square, it is well-defined, because congruent integers have congruent squares. The target of an operation matters as much as its formula.

A quotient is not simply permission to erase distinctions. It is permission to erase distinctions that a carefully checked construction does not depend on. Whenever you encounter a new quotient, ask what its elements are, what relation defines them, and why later formulas respect that relation.

## Partitions and equivalence relations

The equivalence classes form a partition of the original set: every element lies in a class, no class is empty, and two classes are either identical or disjoint. Conversely, a partition into nonempty pieces defines an equivalence relation by declaring two objects equivalent exactly when they belong to the same piece. This duality explains why quotient sets are a natural way to organize all the possibilities.

The relation need not come from arithmetic. Two words may be equivalent if one is an anagram of the other. Two paths may be identified if they can be continuously deformed into each other under specified endpoint restrictions. Two functions may be considered equivalent if they differ only on a set of measure zero. Each of those cases requires care in defining the relation and proving the three properties.

Equivalence relations connect basic logic to algebra and topology. A quotient construction is a definition combined with a proof obligation: show the identification is coherent, then show the operations you wish to use descend to the identified objects. Once that obligation is satisfied, the quotient becomes a legitimate mathematical space rather than a shorthand for inconsistent choices.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (not spoken)

### Congruence and quotient operations

Define \(a\sim b\iff3\mid(a-b)\) on \(\mathbb Z\). The relation is reflexive, symmetric, and transitive. Classes are \([0],[1],[2]\). For addition,
\[
[a]+[b]:=[a+b].
\]
If \(a\sim a'\) and \(b\sim b'\), then
\[
(a+b)-(a'+b')=(a-a')+(b-b')
\]
is a multiple of three; hence the operation is independent of representatives. By contrast, \([a]\mapsto a^2\in\mathbb Z\) is not well-defined because \([0]=[3]\) but \(0^2\neq3^2\).

### Exercises with answers

1. Show that congruence modulo \(m>0\) is an equivalence relation. **Answer:** use divisibility of \(0\), closure under negation, and closure under addition.
2. Is \([a]\mapsto[a^2]\) well-defined modulo three? **Answer:** yes, as \(a^2-b^2=(a-b)(a+b)\) is divisible by three whenever \(a-b\) is.
3. Why must equivalence classes be either disjoint or equal? **Answer:** a shared element \(z\) yields \(a\sim z\sim b\) and hence each representative is related to the other.

### Sources and further reading

- [Richard Hammack, Book of Proof, third edition (current online edition)](https://richardhammack.github.io/BookOfProof/).
- [Eric Lehman, F. Thomson Leighton and Albert R. Meyer, Mathematics for Computer Science, MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/).
- [Wikipedia: Equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation).
