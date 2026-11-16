# 003000 — Group Actions, Orbits, and Counting Symmetry

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** group axioms and basic counting. **Question:** how do abstract groups act on concrete objects, and what does symmetry do to counting?

<!-- BEGIN SPOKEN LECTURE -->

# Group Actions, Orbits, and Counting Symmetry

Suppose you have four beads, each painted one of three colors, arranged around a circular bracelet. Two color arrangements count as the same if turning the bracelet makes one arrangement look exactly like the other. How many genuinely different bracelets are there?

The naive count is three choices for each of four positions, or eighty-one. But eighty-one counts the same arrangement repeatedly under rotation. Dividing by four might seem sensible, because there are four possible turns. That would give twenty and a quarter bracelets, a sure sign that something has gone wrong. Some arrangements are fixed by rotations; they do not occur in groups of four distinct versions.

To solve the problem we need a language for a group acting on a set, and two counting theorems that emerge from that language.

## What it means to act

Let G be a group and X be a set. An action assigns to every element g of G a transformation of X, written g acting on x, such that the identity leaves every x unchanged and the action of a product g h agrees with applying h and then g. The conditions are precisely what is needed for the group multiplication table to describe real transformations.

For example, the eight symmetries of a square act on its four vertices. They also act on its four edges, on its diagonals, and on all the possible ways to color its corners. These are different actions of the same group. A vertex and a coloring are not the same kind of object, but an action uses only the rules of the group and the chosen set.

A group action also tells us how to treat equivalence under symmetry. Two elements x and y of X lie in the same orbit if some group element sends x to y. Orbits form disjoint classes that cover X. In the bead problem, an orbit collects all arrangements reachable from one another by rotating the bracelet. Counting bracelets means counting orbits.

## The orbit and its stabilizer

Fix a point x. Its stabilizer is the set of group elements that leave x unchanged. It forms a subgroup: the identity fixes x, two transformations fixing x still fix it when combined, and the inverse of a transformation fixing x must fix x too.

The orbit tells us how many places x can go. The stabilizer tells us how many distinct group elements fail to move it. These quantities satisfy an exact relationship in a finite group: the number of points in the orbit times the number of elements in the stabilizer equals the number of elements in the group.

Here is the reason. For each target y in the orbit, choose a transformation g that sends x to y. Any other transformation h sending x to the same y differs from g by an element that fixes x: the inverse of g followed by h fixes x. Conversely, combining g with any stabilizer element still sends x to y. Thus exactly the size of the stabilizer many group elements send x to each particular orbit point. These fibers partition G, so multiplying their common size by the number of orbit points gives the group size.

That is the orbit-stabilizer theorem. It is more informative than “divide by the number of symmetries,” because it tells us when such division is valid and when some objects have more symmetry than others.

For the action of the square symmetry group on its vertices, the orbit of each vertex contains all four vertices. Exactly two group elements fix any chosen vertex: the identity and reflection through the diagonal containing that vertex. Four times two is eight, matching the size of the symmetry group.

## Count fixed points in two ways

To count all the orbits, consider the collection of pairs consisting of a group element g and an object x fixed by g. We can count these pairs by choosing g first. For each g, count how many objects it fixes, then add those counts over G.

Or we can choose an object x first. Every x contributes the size of its stabilizer. Group the objects by orbit. If an orbit has k points, orbit-stabilizer says each stabilizer has size the group size divided by k. Adding across that orbit yields exactly the size of G. So every orbit contributes the same number of fixed pairs: the size of the group.

We have counted the same set two ways. Therefore the number of orbits equals the average, over all group elements, of the number of objects each group element fixes. This is Burnside's counting lemma, sometimes called the orbit-counting theorem. Its proof is simply double counting reinforced by orbit-stabilizer.

It is important to count fixed *objects*, not fixed positions. In our bracelet problem, the object is an entire coloring. A rotation may permute positions yet leave a coloring unchanged when those positions share colors.

## Solve the four-bead problem

We are counting colorings of four labeled positions, identifying those related by rotations only. The rotation group has four elements: the identity, a quarter-turn, a half-turn, and a three-quarter-turn.

The identity fixes all eighty-one colorings. A quarter-turn fixes only the three monochromatic colorings, because every position cycles through all four places and must have the same color. The three-quarter-turn similarly fixes three. A half-turn swaps opposite pairs of positions. It fixes colorings in which each opposite pair is monochromatic, giving three choices for one pair and three for the other, or nine fixed colorings.

Burnside's lemma tells us to add eighty-one, three, nine, and three, then divide by four. The answer is twenty-four distinct bracelets under rotation. This count is an integer because we have not approximated symmetry by a fraction; we have proved the orbit count equals that average.

What if flipping the bracelet over should also count as the same arrangement? Then the acting group is larger; it contains reflections as well as rotations, so we must recompute the fixed-coloring counts. The choice of what constitutes the “same bracelet” is part of the mathematical problem. It cannot be decided by the counting formula alone.

## Symmetry can simplify problems besides counting

A group action may have a kernel: group elements that fix *every* object in X. An action is faithful if only the identity acts as the identity transformation. The square group acting on its vertices is faithful, because no nonidentity symmetry fixes all four corners. A group may act nonfaithfully on a smaller or coarser set, and then some transformations become observationally indistinguishable.

The orbits also give an organizing principle for solving equations and classifying structures. If two candidate configurations lie in the same orbit, any property preserved by the action takes the same value on both. Rather than examine every configuration, we can choose one representative of each orbit. A good classification theorem then explains which invariants distinguish the orbits and which do not.

The stabilizer describes the symmetry that remains after choosing a particular object. A generic coloring of four beads might be fixed only by the identity rotation. A monochromatic coloring is fixed by every rotation. Highly symmetric objects are exactly where naive division by the group size breaks.

## The larger lesson

Orbit-stabilizer explains why group order, subgroup size, and orbit size are linked. Burnside's lemma turns those links into a practical counting method. Both are consequences of a simple idea: when a group acts, we can count either what moves or what stays fixed.

Group actions are the point at which abstract algebra becomes an active language for combinatorics, geometry, and classification. The abstract multiplication table now organizes a concrete universe of objects, and careful counting replaces guesses about how much symmetry has been removed.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An action is \(G\times X\to X\), \((g,x)\mapsto gx\), with \(ex=x\) and \((gh)x=g(hx)\). Define
\[
Gx=\{gx:g\in G\},\qquad G_x=\{g\in G:gx=x\}.
\]
For finite \(G\), \(|Gx|\,|G_x|=|G|\). Orbit-stabilizer counts each fiber of \(g\mapsto gx\) as a coset of \(G_x\).

**Burnside's lemma:**
\[
|X/G|=\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}_X(g)|.
\]
For four positions colored from a three-color palette under cyclic rotations,
\[
|X/C_4|=\frac{3^4+3+3^2+3}{4}=24.
\]
This is necklaces modulo rotations, not dihedral bracelets modulo reflections; state the chosen equivalence relation before counting.

### Exercises with answers

1. A group of order twelve acts transitively on four objects. How large is each stabilizer? **Answer:** Three.
2. What colorings of four beads are fixed by a half-turn? **Answer:** Those with colors equal on opposite positions; there are \(3^2=9\).
3. Why is dividing eighty-one by four wrong? **Answer:** Some colorings have nontrivial stabilizers, so their orbits have fewer than four members.
4. A group acts trivially on every point. How many orbits are there? **Answer:** One orbit for each point; Burnside returns \((|G|\cdot|X|)/|G|=|X|\).

### Reading

Judson, *Abstract Algebra: Theory and Applications*, group actions and counting; MIT RES.18-011 student Algebra I notes, section on group actions and the counting formula.
