# Counting Symmetry Without Listing Every Transformation: Group Actions and Orbits

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic  
**Lecture:** 090000  
**Preparation:** The group axioms, permutations, and the eight symmetries of a square, as introduced in lecture 001000.  
**Companion:** Orbit–stabilizer, Burnside's lemma, the class equation, and a fully calculated square-coloring example.

<!-- BEGIN SPOKEN LECTURE -->

Suppose four people sit at the corners of a square table, and each corner has a colored card. Rotating the table may change which card is at the top, but not the arrangement considered as an object. Reflecting the table in a mirror might or might not count as the same arrangement, depending on the question. The number of colored cards is easy to specify. The number of genuinely different arrangements is harder, because some configurations are preserved by more transformations than others.

There is a temptation to count all the colorings and divide by eight, because a square has eight symmetries. That gives the wrong answer for almost any coloring problem. An all-red square is unchanged by every symmetry. A square with three red cards and one blue card has four possible placements for the blue card, not eight. The configurations do not come in groups of equal size.

Group actions give us an exact way to reason about this. We will develop the basic counting theorem, use it to count colorings, and then turn the same machinery inward to study the structure of a group itself.

## A group can act on objects other than itself

A group action is a rule that lets each group element transform an object in some set X. The identity transformation must leave every object alone. And performing one group element and then another must agree with performing their product. In symbols, if we use a left action, the product g h acts by first applying h and then g.

The objects in X need not be geometrical points. They can be colorings, subsets, matrices, solutions of equations, or functions. All that matters is that the transformation rule obeys those two conditions. The group tells us which operations are allowed; the set tells us what is being transformed.

Let G be the eight symmetries of a square. It acts on the four corners by moving them around. It also acts on assignments of colors to those corners. There is a minor but important convention: when a symmetry moves the card currently at corner i to corner g of i, the resulting coloring at a corner j is the old coloring at the inverse image of j. This inverse makes composition behave correctly. We can picture the physical cards moving and avoid worrying about notation until we need it.

Two objects are in the same orbit if an allowed group element carries one to the other. The orbit of a blue card sitting in one corner contains the four placements of that card. These form one orbit, even though there are eight ways to move the table. Some of the eight transformations produce the same final placement.

The collection of all orbits partitions X. Reflexivity comes from the identity, symmetry from inverses, and transitivity from multiplication. Thus being related by a symmetry is an equivalence relation. Counting inequivalent objects means counting equivalence classes under that relation.

## The transformations that leave an object fixed

For a particular object x, its stabilizer is the set of group elements that leave it unchanged. It is a subgroup. The identity fixes x. If g and h both fix x, their product fixes x. And if g fixes x, its inverse does too.

Take a particular corner of the square. Exactly two square symmetries fix that corner: the identity and the reflection across the diagonal through that corner and the opposite corner. The stabilizer has size two. Yet the orbit has size four. Four times two is eight, the size of the whole group.

That identity is not an accident. It is the orbit–stabilizer theorem. For any finite group acting on any set, the number of points in the orbit of x, multiplied by the number of transformations stabilizing x, equals the order of the group.

Here is the proof idea, which is as valuable as the formula. Consider all transformations that send x to a chosen point y in its orbit. Pick one such transformation g. Every other transformation sending x to y can be written as g followed by a transformation that fixes x. Conversely, every such composition sends x to y. Therefore there are exactly as many transformations taking x to y as there are elements of the stabilizer of x. Every y in the orbit has the same-sized collection of transformations leading to it, and these collections partition the group. Multiplying the two sizes gives the order of G.

In the language of subgroups, the orbit is in bijection with the left cosets of the stabilizer. Distinct group elements may describe the same destination, and the coset records exactly that redundancy. It is the same coset-counting idea used in Lagrange's theorem, now given a geometric meaning.

If we color one corner blue and three corners red, the coloring has stabilizer size two and orbit size four. If all four corners are red, the stabilizer is the entire group and the orbit has size one. If each corner receives a different color, only the identity fixes the coloring, so its orbit has size eight. We cannot divide the number of all colorings by one fixed orbit size, because the stabilizer changes with the coloring.

## Counting without enumerating the orbits

There is a remarkable way around the variable orbit size. Rather than listing the orbits, count all pairs consisting of a transformation and an object fixed by that transformation.

We can count those pairs by fixing the object first. A coloring x contributes as many pairs as there are group elements in its stabilizer. Sum over all colorings. If we group colorings by orbits, each orbit contributes the size of the orbit times the size of one of its stabilizers. Orbit–stabilizer tells us that this product is exactly the order of the group. So each orbit contributes precisely eight pairs for the square group, no matter how symmetrical or asymmetrical its colorings may be.

Now count the same pairs in the opposite order. Fix a group element g, then count how many colorings it fixes. Add these numbers over all g. Because each orbit contributes exactly the group order to the total, the number of orbits is the average number of fixed objects across the group.

This is Burnside's lemma. It is a double-counting theorem, not a statement that a typical coloring has a certain number of symmetries. We count the same finite set of pairs in two different ways and equate the answers.

## Three colors on four corners

Let's use three available colors and regard two colorings as equivalent when a rigid symmetry of the square takes one to the other. We have three choices at each of four corners, so there are three to the fourth, or eighty-one, labeled colorings.

A coloring is fixed by a permutation of corners precisely when all corners in each cycle of that permutation have the same color. If the permutation has k cycles, including one-element cycles, there are three to the k fixed colorings. Every cycle receives one independently chosen color.

The identity has four cycles and fixes all eighty-one colorings. A half-turn exchanges two pairs of opposite corners. It has two cycles and fixes nine colorings. Each quarter-turn cycles all four corners around; there are two quarter-turns, and each fixes three colorings, the constant ones.

The reflections have two different types. A reflection through two opposite corners fixes those two corners and exchanges the other two, giving three cycles. There are two such reflections and each fixes twenty-seven colorings. A reflection through the midpoints of opposite edges exchanges two pairs of corners, giving two cycles. There are two such reflections and each fixes nine colorings.

Add everything: eighty-one for the identity, nine for the half-turn, six for both quarter-turns, fifty-four for the two corner-axis reflections, and eighteen for the two edge-axis reflections. That is one hundred sixty-eight fixed-coloring pairs. Divide by eight. There are exactly twenty-one inequivalent colorings under all square symmetries.

Now suppose a physical square is not allowed to be flipped over. We identify colorings under rotations only. The relevant group has four elements, and only the first four fixed-coloring contributions survive: eighty-one, nine, three, and three. Their sum is ninety-six. Divide by four, obtaining twenty-four rotationally inequivalent colorings.

Twenty-four and twenty-one are both correct, for different equivalence relations. The algebra did not choose the meaning of sameness for us. We chose it by specifying the acting group.

## The same action can reveal a group's internal structure

So far the group acted on corners and colorings. A group can also act on its own elements by conjugation. The element g sends x to g x g inverse. Conjugation is an action because the identity changes nothing, and conjugating first by h and then by g is the same as conjugating by g h.

The orbit of x under this action is its conjugacy class. The stabilizer is the centralizer: all elements that commute with x. Orbit–stabilizer now says that the size of a conjugacy class is the index of its centralizer.

Return to the square group. Call a quarter-turn r and a chosen reflection s. We know that r to the fourth power is the identity, s squared is the identity, and s r s equals r inverse. Every group element can be written uniquely as a rotation or a rotation followed by s.

Under conjugation, the identity forms a class by itself. The half-turn also forms a class by itself, because it commutes with every square symmetry. The quarter-turn and three-quarter-turn form one class of size two, since reflection interchanges them. The four reflections split into two classes: the two reflections through opposite corners, and the two reflections through midpoints of opposite edges. Conjugation by a quarter-turn moves one reflection axis to the next axis of the same type, but it cannot turn a corner-axis reflection into an edge-axis reflection.

Thus the five conjugacy-class sizes are one, one, two, two, and two. Their sum is eight, as required. More importantly, the two singleton classes identify the center of the group, the elements commuting with everything: the identity and the half-turn.

This is called the class equation. It writes the group order as the size of its center plus the sizes of the noncentral conjugacy classes. It is often useful when there is no picture of a square at all. For finite groups whose order is a power of a prime, for example, the equation implies that the center contains more than just the identity. Each noncentral class size is divisible by that prime, so the size of the center must be divisible by it as well. This is a striking structural fact obtained almost entirely by counting.

## An action is also a homomorphism

Every action of G on X determines a homomorphism from G into the group of permutations of X. Send each group element to the permutation it induces. Preservation of multiplication is exactly the action law. If a group element acts as the identity on all of X, it lies in the kernel of this homomorphism.

The action is faithful when that kernel consists only of the identity. The square group's action on its four corners is faithful: no nonidentity rigid square symmetry fixes every corner. But a group might act on a smaller or less informative set, and distinct group elements could then become indistinguishable. A stabilizer concerns one particular object; the kernel concerns all objects simultaneously. Stabilizers are usually not normal subgroups, while a kernel always is.

This will connect directly to quotient groups. Whenever an action forgets some information, its kernel measures which transformations have become invisible. The image is the group of transformations actually visible on the objects.

## What counting symmetries has taught us

We began with the false shortcut of dividing all colorings by eight. A good counting argument had to distinguish an object's orbit from its stabilizer. Orbit–stabilizer described the size of each equivalence class. Burnside's lemma counted all the classes without constructing them. Conjugation turned the same machinery into a theorem about the group's own architecture. Finally, every action became a homomorphism into a permutation group.

The surprise is how little new machinery we needed. The action axioms, inverse transformations, cosets, and counting the same collection two ways were enough to move from painted squares to structural group theory. Whenever a future mathematical object has symmetries—roots of a polynomial, solutions to a system, states of a combinatorial model—we can ask the same two questions. Which transformations send this object somewhere else, and which leave it exactly where it is?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let a finite group \(G\) act on \(X\). For \(x\in X\), define
\[
G_x=\{g\in G:g\cdot x=x\},\qquad G\cdot x=\{g\cdot x:g\in G\}.
\]
The map \(G/G_x\to G\cdot x\), \(gG_x\mapsto g\cdot x\), is well-defined and bijective. Consequently
\[
|G\cdot x|=[G:G_x]=\frac{|G|}{|G_x|}.
\]
For finite \(X\), double-count \(P=\{(g,x):g\cdot x=x\}\):
\[
|X/G|=\frac{1}{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|.
\]
If \(g\) permutes \(n\) positions in \(c(g)\) cycles, the number of \(q\)-colorings fixed by \(g\) is \(q^{c(g)}\). In \(D_4\) acting on four corners, the cycle-type inventory is

| Element type | Count | Cycles | Fixed 3-colorings per element |
|---|---:|---:|---:|
| Identity | 1 | 4 | 81 |
| Half-turn | 1 | 2 | 9 |
| Quarter-turns | 2 | 1 | 3 |
| Reflections through opposite vertices | 2 | 3 | 27 |
| Reflections through opposite edges | 2 | 2 | 9 |

Thus \( (81+9+2\cdot3+2\cdot27+2\cdot9)/8=21\). Rotations alone give \((81+9+3+3)/4=24\).

For conjugation \(g\cdot x=gxg^{-1}\), the stabilizer is \(C_G(x)\), and the orbit is the conjugacy class \(\mathrm{Cl}(x)\). The class equation is \(|G|=|Z(G)|+\sum_{\text{noncentral classes}}[G:C_G(x)]\). For \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), the classes are \(\{1\}\), \(\{r^2\}\), \(\{r,r^3\}\), \(\{s,r^2s\}\), \(\{rs,r^3s\}\).

**Worked checks and exercises**

1. Two-color square colorings under rotation: \((2^4+2^2+2\cdot2)/4=6\). Under all square symmetries: \((16+4+4+2\cdot8+2\cdot4)/8=6\). The equality is specific to this small case, not a general rule.
2. Show the stabilizer of a single distinguished corner in \(D_4\) has order two and its orbit has four elements.
3. Show the center of \(D_4\) is \(\{1,r^2\}\) by checking that \(r^k\) commutes with \(s\) exactly when \(k\) is even, and no reflection commutes with \(r\).
4. Prove that the kernel of an action is the intersection of all point stabilizers. It is normal as the kernel of \(G\to\operatorname{Sym}(X)\).
5. If \(|G|=p^k\) with \(p\) prime, use class sizes to show \(p\mid |Z(G)|\); since the identity belongs to the center, the center is nontrivial.

**Source notes:** Thomas W. Judson, *Abstract Algebra: Theory and Applications* (groups and actions), https://judsonbooks.org/abstract-algebra-theory-and-applications/ ; MIT OCW Algebra I notes, https://ocw.mit.edu/courses/res-18-011-algebra-i-student-notes-fall-2021/ . Related foundational lecture: `abstract-algebra:001000`.
