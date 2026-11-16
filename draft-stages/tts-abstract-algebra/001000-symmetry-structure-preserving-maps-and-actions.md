# Symmetry, structure-preserving maps, and actions

<!-- BEGIN SPOKEN LECTURE -->

# Symmetry, structure-preserving maps, and actions

## Symmetry and Groups: Why Composition Creates Structure

Imagine a square drawn on a transparent sheet. Rotate it by a quarter turn. The square still fits exactly on its original outline, though its corners have moved. Reflect it across a vertical line through the center. Again the outline matches. These are symmetries: transformations that preserve the structure we have decided to study.

A symmetry is not merely a property of a single movement. We can perform one movement and then another. Once we begin composing movements, a small collection of geometric tricks becomes an algebraic system. The important question is no longer just, “Which motions leave the square unchanged?” It is, “What happens when those motions are combined?”

### Eight motions, not infinitely many

Label the vertices of the square one, two, three, and four, in clockwise order. Every rigid symmetry of the square must send a vertex to another vertex and preserve adjacency. There are four choices for the destination of vertex one. Once it has been placed, there are two choices for where an adjacent vertex goes: clockwise or counterclockwise around the new position. The remaining vertices are forced. Four times two makes eight symmetries.

Four are rotations: doing nothing, turning one quarter, turning one half, and turning three quarters. Four are reflections, with axes through opposite vertices or through midpoints of opposite edges. Our counting argument did more than offer a list: it explained why a ninth rigid symmetry cannot exist.

Let r mean a quarter-turn counterclockwise and let s mean reflection in a fixed horizontal axis. If we carry out s and then r, the result need not be the same as r and then s. You can test this with a labeled corner. The geometry satisfies an especially useful equation: reflecting, rotating, and reflecting again produces the inverse rotation. In symbols we would write s r s equals r inverse, provided we agree that compositions act from right to left. Equivalently, s r equals r inverse s.

That relation tells us why the square's symmetries are not just the four rotations with some reflections attached. Their order matters. For a typical group of transformations, composition is not commutative.

### What a group is

We can now remove the square from the story. A group is a set of elements with a way to combine any two elements, subject to four conditions. First, combining two members produces another member of the same set. Second, combination is associative: when three elements are combined in the same order, changing the parentheses does not change the result. Third, there is an identity element that leaves every member unchanged. Fourth, every element has an inverse that undoes its effect.

Notice what is absent. We do not require that combining a with b give the same result as combining b with a. When that stronger rule happens to hold, the group is called abelian, or commutative. The rotations of a square form an abelian group; the entire collection of eight symmetries does not.

For transformations, the axioms have tangible explanations. The identity is doing nothing. The inverse of a rotation is a rotation in the opposite direction. The inverse of any reflection is the same reflection performed again. Associativity comes from composition of functions: applying a, then b, then c has the same overall action no matter where we put the parentheses. Closure follows because doing two symmetries in succession still preserves the square.

One subtlety: closure is a genuine requirement, not a formality. Consider the positive whole numbers under ordinary subtraction. Subtracting five from two gives negative three, which is outside the set. Even if we expanded the set to all integers, subtraction would still fail associativity. The familiar arithmetic operation is not automatically a group operation on every familiar set.

### A group that has no obvious picture

The integers under addition form a group. The identity is zero, the inverse of seven is negative seven, and associativity is the ordinary rule for addition. The positive integers do not form a group under addition because they lack additive inverses. The nonzero real numbers under multiplication form a group: the inverse of three is one third. All real numbers under multiplication do not form a group because zero cannot be multiplied by anything to produce one.

These examples also show why an abstract definition earns its keep. A rotation, an integer addition, and multiplication by a nonzero real number look completely different. The same short arguments apply to all three because they use only the group axioms.

For example, cancellation is a theorem, not an extra axiom. Suppose a combined with b equals a combined with c. Combine both sides on the left with the inverse of a. Associativity lets us regroup. The inverse followed by a becomes the identity, leaving b equals c. This proves left cancellation in every group. Right cancellation follows similarly. We did not assume commutativity, and we did not need to know what the elements looked like.

An immediate consequence is that the identity is unique. If e and f were both identities, combining e with f would have to give f because e is an identity, and e because f is an identity. Therefore e equals f. The inverse of any element is also unique by cancellation. Such arguments are small, but they teach the discipline of asking what the axioms truly force.

### The smaller groups inside a group

A subgroup is a subset that itself forms a group under the same operation. Inside the eight symmetries of the square, the four rotations form a subgroup. The identity and the half-turn form another subgroup of size two. Each reflection together with the identity forms a subgroup of size two as well.

Subgroups matter because they reveal structure at different resolutions. A group can be complicated while an individual subgroup is simple. If we choose an element a and repeatedly combine it with itself, include the identity, and include inverse powers, we get the cyclic subgroup generated by a. The half-turn generates only two motions. The quarter-turn generates all four rotations. An element's order, in a finite group, is the first positive number of repetitions required to return to the identity.

Why does the repetition eventually return? In a finite group, there are only finitely many elements but an endless list of powers: identity, a, a squared, a cubed, and so on. Two powers must coincide. Cancellation of the earlier power tells us that a positive power equals the identity. This argument relies on finiteness; the element one in the additive integers has infinite order.

The distinction between an element's order and the group's size is useful. The quarter-turn has order four in a group of eight symmetries. Each reflection has order two. The identity has order one. Later we can prove that in a finite group, the order of an element divides the size of the group. That fact is not evident from the definition, and it will emerge by counting cosets.

### Transformations versus descriptions

One can describe the square's symmetries without drawing them. A transformation permutes the labels one through four; preserving the square imposes restrictions on which permutations are allowed. More generally, the set of all permutations of n objects forms a group under composition, called the symmetric group. It has n factorial members because the first object has n possible destinations, the second has n minus one, and so on.

A geometric symmetry group sits inside a permutation group. A group of numerical operations can also be represented by permutations, though the construction is less obvious. This points toward a fundamental idea: algebra investigates the rules of composition, while the objects being composed can be motions, substitutions, matrices, or actions on entirely different sets.

There is one more caution about representation. Two different written instructions can describe the same transformation. Turning a square a full circle is not a new symmetry distinct from doing nothing. If our objects are transformations, we identify instructions when they have exactly the same effect on every point of the square. Counting expressions instead of distinct actions would give the wrong group.

### What the definition buys us

The square gave us eight motions, a multiplication rule, an identity, inverses, noncommutativity, and subgroups. The abstract axioms extracted precisely the parts of that account that carry over to other systems. We can now ask which apparently different groups have the same structure, which transformations preserve that structure, and what information is lost when a complicated group is compressed into a simpler one.

This is the intellectual move of abstract algebra: stop cataloging isolated tricks and begin proving what follows from structure. A group is a disciplined answer to the question, “What changes when operations can be combined and undone?”

## Homomorphisms, Kernels, and Quotients: The Structure a Map Preserves

There is a clock with twelve marked positions. If we advance its hand seven hours and then another eight hours, the final hand position is the same as advancing fifteen hours and reducing by twelve. Ordinary integer addition and clock arithmetic differ in the numbers they remember, but they agree about composition. We can forget the number of complete revolutions without breaking addition.

That controlled forgetting is a homomorphism. It is one of algebra's most powerful constructions, because it lets us compare complicated objects through simpler ones while tracking exactly what has been lost.

### Preserve the operation, not the labels

A homomorphism from a group G to a group H is a function phi such that phi of a times b equals phi of a combined with phi of b, for all elements a and b of G. We use multiplication language for a general group, even when the example is addition. The equation says that combining first and mapping later gives the same answer as mapping first and then combining.

For the integers under addition and the twelve clock positions under addition modulo twelve, phi sends each integer to its remainder modulo twelve. Phi of seven plus eight is the residue three. Phi of seven plus phi of eight is also three on the clock. The map is many-to-one: zero, twelve, twenty-four, and negative twelve all point to the same clock position.

Why care about the preserving equation? Because it carries proofs. If phi is a homomorphism, it sends the identity of G to the identity of H. To see this, phi of the identity multiplied by phi of any element equals phi of that element. Since phi of an identity times an element is the element itself, cancellation in H forces phi of the identity to equal H's identity. A similar argument shows that the image of an inverse is the inverse of the image.

Thus the homomorphism cannot preserve multiplication while arbitrarily scrambling the meaning of doing nothing or undoing an action. Those features come along automatically.

### What disappears is the kernel

The kernel of a homomorphism consists of all elements of G mapped to the identity of H. For the reduction map from integers to a twelve-hour clock, the kernel is the multiples of twelve. They are precisely the changes that the clock cannot detect.

For a second example, let a permutation have sign plus one if it can be written as an even number of pair swaps, and minus one if that number is odd. The parity of the number of swaps is well-defined despite there being many ways to express a permutation. Taking the sign of a composition multiplies the signs. The sign map from permutations of three objects to plus or minus one under multiplication is a homomorphism. Its kernel consists of the even permutations. The map forgets which even permutation we performed, retaining only parity.

The kernel is a subgroup. If two elements map to the identity, their product does too; the identity maps to the identity; and the inverse of an element in the kernel remains in the kernel. There is a stronger property that we will need. If k is in the kernel and g is any group element, then g times k times the inverse of g also maps to the identity. This follows by applying the homomorphism to the three factors: phi of g, followed by the identity, followed by phi of g inverse. They cancel.

A subgroup preserved under every such conjugation is called normal. Every kernel is normal. It is normality, rather than merely being a subgroup, that allows a collection of elements to be collapsed into an identity in a way consistent with multiplication.

### Cosets as indistinguishable cases

Take the integers again. Two integers have the same remainder modulo twelve exactly when their difference is divisible by twelve. Equivalently, they differ by an element of the kernel. This divides the integers into twelve classes. One class contains all multiples of twelve. Another contains numbers one more than a multiple of twelve, and so forth.

In a general group, fixing a subgroup N, a left coset g N is the collection of products g n as n ranges through N. If N is the kernel of phi, every member of g N has the same image under phi as g. Conversely, if phi of g equals phi of h, then the inverse of h times g lies in the kernel, so g is in h N. Thus the fibers of a homomorphism are exactly the kernel cosets, at least when we look at the part of H actually reached by the map.

This is a proof that the kernel measures the collapse. Not every difference between two elements is lost; precisely those in the same kernel coset are identified.

We want to multiply cosets by choosing representatives: take the coset of g and the coset of h, combine their representatives, and declare the answer to be the coset of g h. But what if someone chooses other representatives of the same two cosets? A mathematical operation must not change because of an arbitrary choice of notation.

For a normal subgroup N, that problem is solved. Replacing g with g n and h with h m changes the product to g n h m. Move n past h by rewriting it as h times h inverse n h. Since N is normal, the conjugated factor remains in N. So the new product differs from g h by a factor belonging to N. Both representative choices yield the same coset. The set of cosets with this operation is a group, written G modulo N.

### Why normality is necessary

Consider the symmetries of a square and choose the two-element subgroup containing the identity and one particular reflection s. If we conjugate that reflection by a quarter-turn, we generally obtain a reflection across a different axis. It is not in our chosen two-element subgroup. So the subgroup is not normal.

We can form a collection of left cosets as sets, but the proposed multiplication of cosets need not be well-defined. We cannot legitimately declare the reflection s to be the identity while leaving the rest of the group unchanged. Because conjugation moves it to another reflection, the group multiplication would force additional identifications. A quotient must respect all of the original relations.

This is the algebraic reason that simply putting elements into boxes does not automatically produce a new group. The boxes must cooperate with the operation.

### The first isomorphism theorem

An isomorphism is a bijective homomorphism: a way to relabel one group as another without changing its multiplication structure. The first isomorphism theorem says that a homomorphism phi from G to H identifies the quotient G by its kernel with the image of phi inside H.

We can prove the essential claim in a few steps. From a coset g times the kernel, define a map to phi of g. It is well-defined because any two representatives of the same coset have the same image. It preserves multiplication because phi does. It is onto the image of phi by the very definition of image. It is injective because if phi of g equals phi of h, then g and h belong to the same kernel coset. Hence the quotient and the image have exactly the same group structure.

For the clock, this says the integers divided by the multiples of twelve form the group of residues modulo twelve. For permutation signs, the group of all permutations modulo the even permutations has two elements and is isomorphic to the two-element sign group. Both examples are cases of the same theorem.

The theorem does not say that G and H are isomorphic. A homomorphism may reach only a subgroup of H, and it may identify many elements in G. The correct statement specifies both the kernel and the image. Leaving either out produces a stronger claim that need not be true.

### From arithmetic to algebraic architecture

We have a useful triangle of ideas. A group gives us operations that can be combined and undone. A homomorphism gives us a translation that respects those operations. A normal subgroup records exactly what that translation can erase. The quotient then describes the surviving information, while the first isomorphism theorem confirms that the surviving structure matches the image.

These ideas recur far beyond group theory. Kernels and images occur in linear algebra. Ideals are the right kind of kernels for rings. Exact sequences, later, make the relationship among images and kernels a subject in its own right. The common theme is not forgetting everything: it is forgetting only what the structure allows us to forget.

## Group Actions, Orbits, and Counting Symmetry

Suppose you have four beads, each painted one of three colors, arranged around a circular bracelet. Two color arrangements count as the same if turning the bracelet makes one arrangement look exactly like the other. How many genuinely different bracelets are there?

The naive count is three choices for each of four positions, or eighty-one. But eighty-one counts the same arrangement repeatedly under rotation. Dividing by four might seem sensible, because there are four possible turns. That would give twenty and a quarter bracelets, a sure sign that something has gone wrong. Some arrangements are fixed by rotations; they do not occur in groups of four distinct versions.

To solve the problem we need a language for a group acting on a set, and two counting theorems that emerge from that language.

### What it means to act

Let G be a group and X be a set. An action assigns to every element g of G a transformation of X, written g acting on x, such that the identity leaves every x unchanged and the action of a product g h agrees with applying h and then g. The conditions are precisely what is needed for the group multiplication table to describe real transformations.

For example, the eight symmetries of a square act on its four vertices. They also act on its four edges, on its diagonals, and on all the possible ways to color its corners. These are different actions of the same group. A vertex and a coloring are not the same kind of object, but an action uses only the rules of the group and the chosen set.

A group action also tells us how to treat equivalence under symmetry. Two elements x and y of X lie in the same orbit if some group element sends x to y. Orbits form disjoint classes that cover X. In the bead problem, an orbit collects all arrangements reachable from one another by rotating the bracelet. Counting bracelets means counting orbits.

### The orbit and its stabilizer

Fix a point x. Its stabilizer is the set of group elements that leave x unchanged. It forms a subgroup: the identity fixes x, two transformations fixing x still fix it when combined, and the inverse of a transformation fixing x must fix x too.

The orbit tells us how many places x can go. The stabilizer tells us how many distinct group elements fail to move it. These quantities satisfy an exact relationship in a finite group: the number of points in the orbit times the number of elements in the stabilizer equals the number of elements in the group.

Here is the reason. For each target y in the orbit, choose a transformation g that sends x to y. Any other transformation h sending x to the same y differs from g by an element that fixes x: the inverse of g followed by h fixes x. Conversely, combining g with any stabilizer element still sends x to y. Thus exactly the size of the stabilizer many group elements send x to each particular orbit point. These fibers partition G, so multiplying their common size by the number of orbit points gives the group size.

That is the orbit-stabilizer theorem. It is more informative than “divide by the number of symmetries,” because it tells us when such division is valid and when some objects have more symmetry than others.

For the action of the square symmetry group on its vertices, the orbit of each vertex contains all four vertices. Exactly two group elements fix any chosen vertex: the identity and reflection through the diagonal containing that vertex. Four times two is eight, matching the size of the symmetry group.

### Count fixed points in two ways

To count all the orbits, consider the collection of pairs consisting of a group element g and an object x fixed by g. We can count these pairs by choosing g first. For each g, count how many objects it fixes, then add those counts over G.

Or we can choose an object x first. Every x contributes the size of its stabilizer. Group the objects by orbit. If an orbit has k points, orbit-stabilizer says each stabilizer has size the group size divided by k. Adding across that orbit yields exactly the size of G. So every orbit contributes the same number of fixed pairs: the size of the group.

We have counted the same set two ways. Therefore the number of orbits equals the average, over all group elements, of the number of objects each group element fixes. This is Burnside's counting lemma, sometimes called the orbit-counting theorem. Its proof is simply double counting reinforced by orbit-stabilizer.

It is important to count fixed *objects*, not fixed positions. In our bracelet problem, the object is an entire coloring. A rotation may permute positions yet leave a coloring unchanged when those positions share colors.

### Solve the four-bead problem

We are counting colorings of four labeled positions, identifying those related by rotations only. The rotation group has four elements: the identity, a quarter-turn, a half-turn, and a three-quarter-turn.

The identity fixes all eighty-one colorings. A quarter-turn fixes only the three monochromatic colorings, because every position cycles through all four places and must have the same color. The three-quarter-turn similarly fixes three. A half-turn swaps opposite pairs of positions. It fixes colorings in which each opposite pair is monochromatic, giving three choices for one pair and three for the other, or nine fixed colorings.

Burnside's lemma tells us to add eighty-one, three, nine, and three, then divide by four. The answer is twenty-four distinct bracelets under rotation. This count is an integer because we have not approximated symmetry by a fraction; we have proved the orbit count equals that average.

What if flipping the bracelet over should also count as the same arrangement? Then the acting group is larger; it contains reflections as well as rotations, so we must recompute the fixed-coloring counts. The choice of what constitutes the “same bracelet” is part of the mathematical problem. It cannot be decided by the counting formula alone.

### Symmetry can simplify problems besides counting

A group action may have a kernel: group elements that fix *every* object in X. An action is faithful if only the identity acts as the identity transformation. The square group acting on its vertices is faithful, because no nonidentity symmetry fixes all four corners. A group may act nonfaithfully on a smaller or coarser set, and then some transformations become observationally indistinguishable.

The orbits also give an organizing principle for solving equations and classifying structures. If two candidate configurations lie in the same orbit, any property preserved by the action takes the same value on both. Rather than examine every configuration, we can choose one representative of each orbit. A good classification theorem then explains which invariants distinguish the orbits and which do not.

The stabilizer describes the symmetry that remains after choosing a particular object. A generic coloring of four beads might be fixed only by the identity rotation. A monochromatic coloring is fixed by every rotation. Highly symmetric objects are exactly where naive division by the group size breaks.

### The larger lesson

Orbit-stabilizer explains why group order, subgroup size, and orbit size are linked. Burnside's lemma turns those links into a practical counting method. Both are consequences of a simple idea: when a group acts, we can count either what moves or what stays fixed.

Group actions are the point at which abstract algebra becomes an active language for combinatorics, geometry, and classification. The abstract multiplication table now organizes a concrete universe of objects, and careful counting replaces guesses about how much symmetry has been removed.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Symmetry and Groups: Why Composition Creates Structure

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** elementary functions, and willingness to follow a proof. **Question:** which features of symmetry survive when we forget the picture?

#### Mathematical companion (not spoken)

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

##### Exercises and short answers

1. Why are all reflections of a square of order two? **Answer:** Performing the same reflection twice returns every point to itself, and a reflection is not itself the identity.
2. Is \((\mathbb Z,\times)\) a group? **Answer:** No, integers such as two have no multiplicative inverse within the integers; zero has none anywhere.
3. Can a group have two distinct identities? **Answer:** No; if \(e,f\) are identities, \(e=ef=f\).
4. Calculate \((rs)^2\) in \(D_4\). **Answer:** \(rsrs=r(srs)=rr^{-1}=e\); every reflection is an involution.

##### Reading

Thomas W. Judson, *Abstract Algebra: Theory and Applications*, sections on groups, symmetry and permutation groups; Michael Artin's MIT 18.701 Algebra I course, early lectures on groups and generators.

### Homomorphisms, Kernels, and Quotients: The Structure a Map Preserves

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** groups and function composition. **Question:** what does it mean to simplify a group without lying about multiplication?

#### Mathematical companion (not spoken)

A group homomorphism \(\varphi:G\to H\) satisfies \(\varphi(gh)=\varphi(g)\varphi(h)\). Define
\[
\ker\varphi=\{g\in G:\varphi(g)=e_H\},\qquad
\operatorname{im}\varphi=\{\varphi(g):g\in G\}.
\]
For all \(g\in G\) and \(k\in\ker\varphi\), \(\varphi(gkg^{-1})=e_H\); hence \(\ker\varphi\trianglelefteq G\). If \(N\trianglelefteq G\), the product \((gN)(hN)=(gh)N\) is well-defined.

**First isomorphism theorem.** \(G/\ker\varphi\cong\operatorname{im}\varphi\) by \(g\ker\varphi\mapsto\varphi(g)\). For \(\mathbb Z\to\mathbb Z/12\mathbb Z\), the kernel is \(12\mathbb Z\). For the sign homomorphism \(S_3\to\{\pm1\}\), the kernel is \(A_3\), the alternating group.

##### Exercises with answers

1. What is the kernel of reduction \(\mathbb Z\to\mathbb Z/5\mathbb Z\)? **Answer:** \(5\mathbb Z\).
2. If a homomorphism has trivial kernel, is it injective? **Answer:** Yes; equal images imply the quotient of the inputs lies in the kernel, hence the inputs agree.
3. Must a homomorphism be surjective? **Answer:** No; the inclusion of a subgroup into a larger group is a homomorphism.
4. Why can an arbitrary subgroup fail to yield a quotient group? **Answer:** Different coset representatives may give different products; normality is the condition that prevents this.

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, group homomorphisms and quotient groups; Artin, MIT 18.701, homomorphisms, cosets, and correspondence theorem.

### Group Actions, Orbits, and Counting Symmetry

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** group axioms and basic counting. **Question:** how do abstract groups act on concrete objects, and what does symmetry do to counting?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. A group of order twelve acts transitively on four objects. How large is each stabilizer? **Answer:** Three.
2. What colorings of four beads are fixed by a half-turn? **Answer:** Those with colors equal on opposite positions; there are \(3^2=9\).
3. Why is dividing eighty-one by four wrong? **Answer:** Some colorings have nontrivial stabilizers, so their orbits have fewer than four members.
4. A group acts trivially on every point. How many orbits are there? **Answer:** One orbit for each point; Burnside returns \((|G|\cdot|X|)/|G|=|X|\).

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, group actions and counting; MIT RES.18-011 student Algebra I notes, section on group actions and the counting formula.
