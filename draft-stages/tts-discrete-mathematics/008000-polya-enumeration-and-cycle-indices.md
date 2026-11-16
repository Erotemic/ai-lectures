# 008000 — Pólya Enumeration: Counting Colorings without Double-Counting Symmetry

**Track:** Discrete Mathematics and Combinatorics. **Background:** group actions, Burnside's lemma, cycle notation, and generating functions. **Question:** how many colorings genuinely differ when rotating or reflecting an object does not produce a new design?

<!-- BEGIN SPOKEN LECTURE -->

# Pólya Enumeration: Counting Colorings without Double-Counting Symmetry

If we color the four corners of a square black or white, there are sixteen assignments when the corners are labeled. But if a painted square can be rotated or turned over, some assignments that looked different are actually the same design. The obvious strategy of dividing sixteen by eight fails: the square has eight symmetries, but some colored designs are fixed by several of them, while others are not. Different designs have orbits of different sizes.

Burnside's lemma solves the problem by averaging the number of colorings fixed by each symmetry. Pólya enumeration goes further. It organizes the symmetries by their cycle structure and produces a polynomial that can count colorings with specified numbers of each color. The method makes a complicated counting problem into substitution in a single expression.

## What a symmetry fixes

Take any permutation of the four corners. Write its action as disjoint cycles. If a permutation exchanges corners one and two, those two corners must have the same color for the coloring to remain unchanged. If a permutation cycles three corners, all three must share a color. In general, a coloring is fixed exactly when each cycle is monochromatic.

With q available colors, a permutation having c cycles fixes q to the power c colorings: there is one independent color choice for each cycle. This observation is the complete bridge from the group action to enumeration.

For the square, the identity permutation has four cycles of length one, so it fixes q to the fourth power colorings. Each quarter turn forms one cycle of length four, so it fixes q colorings. A half turn consists of two cycles of length two, so it fixes q squared colorings.

Reflections require care. A reflection across a diagonal through opposite corners fixes those two corners individually and exchanges the other two. It has three cycles and fixes q cubed colorings. A reflection across a line through the midpoints of opposite edges exchanges two disjoint pairs of corners. It has two cycles and fixes q squared colorings. There are two reflections of each type.

Add these contributions and divide by eight. We obtain q to the fourth, plus two times q, plus three times q squared, plus two times q cubed, all divided by eight. For two colors the answer is six. The six possible designs can also be classified directly: none black, all black, one black, three black, two adjacent black corners, and two opposite black corners.

For three colors the answer is twenty-one. Rotations alone would give twenty-four designs, so allowing reflections identifies some additional pairs. Which transformations are considered equivalent is part of the mathematical problem, not a minor detail.

## The cycle index records more than the answer

Rather than evaluate each number of fixed colorings immediately, assign a variable a-one to a cycle of length one, a-two to a cycle of length two, and so forth. For each symmetry multiply one variable for each of its cycles. Average the resulting monomials over the group. This is the cycle index polynomial of the action.

For the square acting on its corners, the cycle index is one eighth times the following sum: a-one to the fourth power; two times a-four; three times a-two squared; and two times a-one squared times a-two. The four terms correspond to identity, quarter turns, half turn plus two edge reflections, and the two diagonal reflections.

Why collect terms this way? Because setting every a-k equal to q recovers the number of colorings with q unrestricted colors. But we can make more informative substitutions.

Suppose we have red and blue paint and want to record how many corners receive each. Replace a-k by x to the kth power plus y to the kth power. Choosing the first term means making that cycle red, contributing k red corners. Choosing the second means making it blue, contributing k blue corners. After substitution and expansion, the coefficient of x squared y squared is the number of essentially different designs with exactly two red and two blue corners.

There are exactly two: the red corners are adjacent or opposite. The cycle-index calculation reproduces that distinction without needing to draw every assignment.

## Why Burnside's lemma is already inside Pólya's method

Burnside's lemma states that the number of orbits equals the average number of fixed objects. We can derive it by counting pairs consisting of a group element and an object fixed by that element. Count first by group elements: the result is the sum of the sizes of all fixed-point sets. Count instead by objects: each object contributes the size of its stabilizer. A whole orbit has size the group order divided by the stabilizer size, so each orbit contributes exactly the group order to the count of pairs. Dividing by the group order gives one per orbit.

Pólya enumeration uses the same double count, but the objects are colorings and their fixed-point counts depend only on cycles. Each fixed coloring contributes a product of weights, so the same argument holds for a weighted count. That is why the cycle-index substitution works: it is Burnside's averaging performed with bookkeeping variables still attached.

We can also use the method for necklaces with n beads. Rotations form a cyclic group. A rotation by k steps has greatest-common-divisor of n and k cycles, so the number of colorings up to rotation is the average, over k from zero through n minus one, of q raised to the greatest common divisor of n and k. Adding reflections changes the acting group and the corresponding terms.

The formula is valuable when n is large, because generating and sorting every coloring would require examining q to the n possibilities. Group structure can compress that count into sums indexed by divisors of n.

## From colorings to larger combinatorial structures

The same idea appears when counting molecular substitution patterns, tilings of finite regions, and many classes of labeled objects modulo automorphisms. It is tempting to say that we are simply dividing by symmetry, but that phrase conceals the delicate part. We must account for the stabilizers of different objects, and the cycle structure of each symmetry tells us which choices survive.

The important lesson is not a single formula for squares. It is a reusable method: identify the action, compute the cycle types, build the cycle index, choose weights that encode the feature you want to count, and substitute. The resulting polynomial answers not only how many distinct objects exist, but often how their colors or components are distributed.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(G\le S_n\) acting on \(n\) positions, let \(c_k(g)\) be the number of cycles of length \(k\) in \(g\). Define the cycle index
\[
Z_G(a_1,\ldots,a_n)=\frac1{|G|}\sum_{g\in G}\prod_{k=1}^n a_k^{c_k(g)}.
\]
For \(q\) available colors, the orbit count is \(Z_G(q,\ldots,q)\). For color inventory \((x_1,\ldots,x_q)\), substitute \(a_k\mapsto x_1^k+\cdots+x_q^k\); the coefficient of \(x_1^{m_1}\cdots x_q^{m_q}\) counts colorings with that inventory modulo \(G\).

**Dihedral action on a square's vertices.** With \(G=D_4\) of order eight,
\[
Z_{D_4}=\tfrac18\bigl(a_1^4+2a_4+3a_2^2+2a_1^2a_2\bigr).
\]
Thus
\[
N(q)=\tfrac18(q^4+2q+3q^2+2q^3),\quad N(2)=6,\quad N(3)=21.
\]
With red weight \(x\) and blue weight \(y\), \([x^2y^2]Z_{D_4}(x+y,x^2+y^2,x^3+y^3,x^4+y^4)=2\).

**Necklaces under rotation only.** For \(C_n\),
\[
N_{C_n}(q)=\frac1n\sum_{k=0}^{n-1}q^{\gcd(n,k)}=\frac1n\sum_{d\mid n}\varphi(d)q^{n/d}.
\]
Including reflections requires the dihedral cycle index, not the cyclic one.

### Exercises with answers

1. How many square-corner colorings with exactly one red corner exist up to all square symmetries? **Answer:** one.
2. Why does a cycle of length four permit only q fixed colorings? **Answer:** every position in that cycle must have the same color.
3. Count square colorings in three colors up to rotations only. **Answer:** \((3^4+3^2+2\cdot3)/4=24\).
4. Count length-three binary necklaces up to rotation. **Answer:** \((2^3+2+2)/3=4\).

### Reading

Sasha Patotski, [Pólya Enumeration Theorem, Cornell notes](https://pi.math.cornell.edu/~apatotski/IHS2015/Lecture%2010.pdf); MIT OCW, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), counting and group actions.
