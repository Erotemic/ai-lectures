# 001000 — Bijections and Double Counting: Proving Equations by Counting Objects

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite sets and basic algebra. **Question:** why can two descriptions of the same collection prove a mathematical identity?

<!-- BEGIN SPOKEN LECTURE -->

# Bijections and Double Counting

Suppose a committee of five people must choose a chair and a secretary, and the roles must go to different people. There are five choices for the chair, followed by four choices for the secretary: twenty assignments. If we reverse the order of selection, there are still twenty. That is unsurprising. But what if someone offers a much more complicated formula for the same count? Can we prove the two formulas agree without expanding them algebraically?

Combinatorics turns this into a method. Describe a finite collection of objects, count it in two ways, and use the equality of the counts to prove an identity. The power is not in clever arithmetic. It is in being precise about what constitutes one object, and about why none is omitted or counted twice.

## The product rule is a reversible description

If a construction has a first choice from a set of m possibilities, followed by a second choice from n possibilities regardless of the first, then there are m times n ordered pairs. If the second choice depends on the first, we add the number of available second choices over all first choices instead. The statement sounds obvious, but the distinction matters.

For a chair and a secretary chosen from five people, the second role has four choices after the first is fixed. The answer is five times four. We cannot use five squared because selecting the same person twice is forbidden. If we do allow the same person in both roles, we do get five squared. The numerical difference encodes a difference in the objects being counted.

A bijection is a one-to-one correspondence between two sets. If the sets are finite, a bijection proves they have the same size. A particularly useful bijection may be simple to describe even when the two sets look unrelated. For instance, a subset of a set of n labeled elements corresponds to a string of n yes-or-no choices, one per element. Every subset determines exactly one string, and every such string determines exactly one subset. There are two choices at each position, hence two to the n subsets.

Notice that the proof has two parts. We defined a map from subsets to strings and explained its inverse. Merely saying “it seems like the same information” would not be enough if different objects could lead to the same string.

## Choose k elements without remembering order

Suppose a group of n people must choose a committee of exactly k people. We can first count ordered lists of k distinct people. The first position has n choices, the second n minus one, and so on, through n minus k plus one. Each actual committee, however, gives rise to k factorial different orders. Divide by that number to count committees rather than arrangements.

This produces the binomial coefficient: n factorial divided by k factorial times n minus k factorial. The formula is valid for integers n at least zero and k between zero and n. Outside that range we may adopt the convention that the coefficient is zero, but the original combinatorial interpretation has to be stated carefully.

There is a second way to understand the same coefficient. Fix a distinguished person, call her Ada. Committees of size k split into two disjoint cases: those containing Ada and those not containing Ada. In the first case we choose k minus one more members from the other n minus one people. In the second case we choose all k from those n minus one. Therefore the number of k-subsets of n elements equals the number of k-minus-one subsets of n-minus-one plus the number of k-subsets of n-minus-one.

This is Pascal's identity. We proved it by partitioning a single collection into disjoint cases, not by simplifying factorials. The same argument generates Pascal's triangle, where each interior entry equals the sum of the two entries directly above it.

## Double count an incidence relation

Now take an undirected graph with a finite collection of vertices and edges. A vertex's degree is the number of incident edge ends; a loop contributes two, because it has two ends at the same vertex. Count all pairs consisting of a vertex and an edge end incident to it.

If we choose the vertex first, the count is the sum of the degrees of all vertices. If we choose an edge first, every edge has exactly two ends, so the count is twice the number of edges. Both procedures count exactly the same incidences. We have proved the handshake lemma: the sum of degrees in a finite undirected graph is twice the number of edges.

An immediate result is that the number of vertices of odd degree is even. The sum of all even degrees is even, and the sum of all degrees is even. So the sum of the odd degrees is even. But a sum of an odd number of odd integers is odd. Therefore there must be an even number of odd-degree vertices.

This conclusion may be used to rule out a proposed network without drawing every possible edge. A claimed graph with exactly three vertices of odd degree cannot exist. An identity obtained by counting becomes a structural constraint.

## A more demanding double count

Consider all subsets of an n-element set, and ask for the total number of times an element appears across every subset. One way to count is to look at each of the n possible elements. Once an element is required to be present, each of the other n minus one elements may be independently included or excluded. So each element occurs in two to the n-minus-one subsets. Across all n elements, the total number of element-subset incidences is n times two to the n-minus-one.

Another way is to group the subsets by their size. There are n choose k subsets containing k elements, so the total number of incidences is the sum, over k from zero to n, of k times n choose k. The two counts are equal.

That gives a binomial identity with a particularly transparent explanation. It also demonstrates how to choose the right object to count. We did not count subsets alone. We counted pairs consisting of a subset and a distinguished member of that subset. The extra mark made the identity visible.

This trick generalizes. If an identity contains a factor k, perhaps choose an object of size k and mark one of its components. If it contains a factor k times k minus one, perhaps mark an ordered pair of distinct components. The algebra can suggest which combinatorial object to invent.

## The pigeonhole principle is also counting

Suppose n plus one letters are placed in n labeled boxes. At least one box contains two or more letters. If each box contained at most one, the total number of letters would be at most n, contradicting the premise. This is the pigeonhole principle in its simplest form.

A more quantitative version says that putting N objects into m boxes forces some box to contain at least the ceiling of N divided by m objects. If every box held fewer, the total capacity would be too small.

The principle becomes powerful when boxes represent mathematical patterns. Among thirteen people, at least two were born in the same month. Among six integers, two have the same remainder modulo five. Subtract those two integers and their difference is divisible by five. We have proved the existence of a divisible difference without examining any actual values.

The second example is especially revealing. Pigeonhole does not tell us which pair works; it proves that some pair must. Combinatorial existence theorems often work this way. A construction or an algorithm might be a separate problem.

## What makes a counting proof rigorous

Every successful counting argument answers three questions. What are the objects? Why does the first procedure count every one exactly once? Why does the second procedure do the same? If we divide by a symmetry factor, why does each object have exactly that many descriptions? If we split into cases, are the cases disjoint and exhaustive? If we use a bijection, can we construct its inverse?

When those questions are settled, the identity is not a lucky algebraic simplification. It is a theorem about a finite structure.

The discipline carries into algorithm analysis, probability, graph theory, algebra, and geometry. A graph's degree sum, the coefficients in a binomial expansion, and the number of subsets containing a designated element are all instances of the same intellectual move: count what really exists, and compare two faithful descriptions of it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(0\le k\le n\),
\[
\binom nk=\frac{n!}{k!(n-k)!},\quad
\binom nk=\binom{n-1}{k-1}+\binom{n-1}k,
\quad \sum_{k=0}^n\binom nk=2^n.
\]
Double counting marked subsets gives
\[
\sum_{k=0}^n k\binom nk=n2^{n-1}\qquad (n\ge1).
\]
For a finite undirected multigraph, loops contributing degree two,
\[
\sum_{v\in V}\deg(v)=2|E|,
\]
so the number of odd-degree vertices is even.

### Exercises with answers

1. How many three-person committees contain a fixed member of a ten-person group? **Answer:** \(\binom 92=36\).
2. Why isn't the number of two-person committees \(n(n-1)\)? **Answer:** That counts both orders of each pair; divide by two.
3. Can a finite graph have exactly five vertices of odd degree? **Answer:** No, by the handshake lemma.
4. Prove there are two integers among any eight with the same remainder modulo seven. **Answer:** Eight objects occupy seven remainder classes; by pigeonhole two share a class.

### Reading

MIT 6.042J, *Mathematics for Computer Science*, chapters on graphs, cardinality rules, and combinatorial proofs.
