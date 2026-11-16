# 001000 — Symmetry and Groups: Why Composition Creates Structure

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** elementary functions, and willingness to follow a proof. **Question:** which features of symmetry survive when we forget the picture?

<!-- BEGIN SPOKEN LECTURE -->

# Symmetry and Groups: Why Composition Creates Structure

Imagine a square drawn on a transparent sheet. Rotate it by a quarter turn. The square still fits exactly on its original outline, though its corners have moved. Reflect it across a vertical line through the center. Again the outline matches. These are symmetries: transformations that preserve the structure we have decided to study.

A symmetry is not merely a property of a single movement. We can perform one movement and then another. Once we begin composing movements, a small collection of geometric tricks becomes an algebraic system. The important question is no longer just, “Which motions leave the square unchanged?” It is, “What happens when those motions are combined?”

## Eight motions, not infinitely many

Label the vertices of the square one, two, three, and four, in clockwise order. Every rigid symmetry of the square must send a vertex to another vertex and preserve adjacency. There are four choices for the destination of vertex one. Once it has been placed, there are two choices for where an adjacent vertex goes: clockwise or counterclockwise around the new position. The remaining vertices are forced. Four times two makes eight symmetries.

Four are rotations: doing nothing, turning one quarter, turning one half, and turning three quarters. Four are reflections, with axes through opposite vertices or through midpoints of opposite edges. Our counting argument did more than offer a list: it explained why a ninth rigid symmetry cannot exist.

Let r mean a quarter-turn counterclockwise and let s mean reflection in a fixed horizontal axis. If we carry out s and then r, the result need not be the same as r and then s. You can test this with a labeled corner. The geometry satisfies an especially useful equation: reflecting, rotating, and reflecting again produces the inverse rotation. In symbols we would write s r s equals r inverse, provided we agree that compositions act from right to left. Equivalently, s r equals r inverse s.

That relation tells us why the square's symmetries are not just the four rotations with some reflections attached. Their order matters. For a typical group of transformations, composition is not commutative.

## What a group is

We can now remove the square from the story. A group is a set of elements with a way to combine any two elements, subject to four conditions. First, combining two members produces another member of the same set. Second, combination is associative: when three elements are combined in the same order, changing the parentheses does not change the result. Third, there is an identity element that leaves every member unchanged. Fourth, every element has an inverse that undoes its effect.

Notice what is absent. We do not require that combining a with b give the same result as combining b with a. When that stronger rule happens to hold, the group is called abelian, or commutative. The rotations of a square form an abelian group; the entire collection of eight symmetries does not.

For transformations, the axioms have tangible explanations. The identity is doing nothing. The inverse of a rotation is a rotation in the opposite direction. The inverse of any reflection is the same reflection performed again. Associativity comes from composition of functions: applying a, then b, then c has the same overall action no matter where we put the parentheses. Closure follows because doing two symmetries in succession still preserves the square.

One subtlety: closure is a genuine requirement, not a formality. Consider the positive whole numbers under ordinary subtraction. Subtracting five from two gives negative three, which is outside the set. Even if we expanded the set to all integers, subtraction would still fail associativity. The familiar arithmetic operation is not automatically a group operation on every familiar set.

## A group that has no obvious picture

The integers under addition form a group. The identity is zero, the inverse of seven is negative seven, and associativity is the ordinary rule for addition. The positive integers do not form a group under addition because they lack additive inverses. The nonzero real numbers under multiplication form a group: the inverse of three is one third. All real numbers under multiplication do not form a group because zero cannot be multiplied by anything to produce one.

These examples also show why an abstract definition earns its keep. A rotation, an integer addition, and multiplication by a nonzero real number look completely different. The same short arguments apply to all three because they use only the group axioms.

For example, cancellation is a theorem, not an extra axiom. Suppose a combined with b equals a combined with c. Combine both sides on the left with the inverse of a. Associativity lets us regroup. The inverse followed by a becomes the identity, leaving b equals c. This proves left cancellation in every group. Right cancellation follows similarly. We did not assume commutativity, and we did not need to know what the elements looked like.

An immediate consequence is that the identity is unique. If e and f were both identities, combining e with f would have to give f because e is an identity, and e because f is an identity. Therefore e equals f. The inverse of any element is also unique by cancellation. Such arguments are small, but they teach the discipline of asking what the axioms truly force.

## The smaller groups inside a group

A subgroup is a subset that itself forms a group under the same operation. Inside the eight symmetries of the square, the four rotations form a subgroup. The identity and the half-turn form another subgroup of size two. Each reflection together with the identity forms a subgroup of size two as well.

Subgroups matter because they reveal structure at different resolutions. A group can be complicated while an individual subgroup is simple. If we choose an element a and repeatedly combine it with itself, include the identity, and include inverse powers, we get the cyclic subgroup generated by a. The half-turn generates only two motions. The quarter-turn generates all four rotations. An element's order, in a finite group, is the first positive number of repetitions required to return to the identity.

Why does the repetition eventually return? In a finite group, there are only finitely many elements but an endless list of powers: identity, a, a squared, a cubed, and so on. Two powers must coincide. Cancellation of the earlier power tells us that a positive power equals the identity. This argument relies on finiteness; the element one in the additive integers has infinite order.

The distinction between an element's order and the group's size is useful. The quarter-turn has order four in a group of eight symmetries. Each reflection has order two. The identity has order one. Later we can prove that in a finite group, the order of an element divides the size of the group. That fact is not evident from the definition, and it will emerge by counting cosets.

## Transformations versus descriptions

One can describe the square's symmetries without drawing them. A transformation permutes the labels one through four; preserving the square imposes restrictions on which permutations are allowed. More generally, the set of all permutations of n objects forms a group under composition, called the symmetric group. It has n factorial members because the first object has n possible destinations, the second has n minus one, and so on.

A geometric symmetry group sits inside a permutation group. A group of numerical operations can also be represented by permutations, though the construction is less obvious. This points toward a fundamental idea: algebra investigates the rules of composition, while the objects being composed can be motions, substitutions, matrices, or actions on entirely different sets.

There is one more caution about representation. Two different written instructions can describe the same transformation. Turning a square a full circle is not a new symmetry distinct from doing nothing. If our objects are transformations, we identify instructions when they have exactly the same effect on every point of the square. Counting expressions instead of distinct actions would give the wrong group.

## What the definition buys us

The square gave us eight motions, a multiplication rule, an identity, inverses, noncommutativity, and subgroups. The abstract axioms extracted precisely the parts of that account that carry over to other systems. We can now ask which apparently different groups have the same structure, which transformations preserve that structure, and what information is lost when a complicated group is compressed into a simpler one.

This is the intellectual move of abstract algebra: stop cataloging isolated tricks and begin proving what follows from structure. A group is a disciplined answer to the question, “What changes when operations can be combined and undone?”

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the square's dihedral group, use the presentation
\[
D_4=\langle r,s\mid r^4=e,\;s^2=e,\;srs=r^{-1}\rangle,
\qquad D_4=\{e,r,r^2,r^3,s,rs,r^2s,r^3s\}.
\]
Here \(D_4\) means the group of eight symmetries of a square; conventions for subscripts differ across books. Multiplication is function composition, rightmost factor applied first. In particular \(sr=r^{-1}s\), and since \(r\ne r^{-1}\), the group is nonabelian.

A group \((G,\cdot)\) obeys closure, associativity, existence of an identity \(e\), and inverses. For cancellation,
\[
ab=ac\implies a^{-1}(ab)=a^{-1}(ac)\implies b=c.
\]
For finite \(G\), repetitions of \(a\) produce \(a^i=a^j\), \(i<j\), whence \(a^{j-i}=e\). Infinite groups need not have elements of finite order.

### Exercises and short answers

1. Why are all reflections of a square of order two? **Answer:** Performing the same reflection twice returns every point to itself, and a reflection is not itself the identity.
2. Is \((\mathbb Z,\times)\) a group? **Answer:** No, integers such as two have no multiplicative inverse within the integers; zero has none anywhere.
3. Can a group have two distinct identities? **Answer:** No; if \(e,f\) are identities, \(e=ef=f\).
4. Calculate \((rs)^2\) in \(D_4\). **Answer:** \(rsrs=r(srs)=rr^{-1}=e\); every reflection is an involution.

### Reading

Thomas W. Judson, *Abstract Algebra: Theory and Applications*, sections on groups, symmetry and permutation groups; Michael Artin's MIT 18.701 Algebra I course, early lectures on groups and generators.
