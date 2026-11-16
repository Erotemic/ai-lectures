# 040000 - Hypergraph Matchings and the Absorption Method

**Track:** Discrete Mathematics. **Background:** graph matchings, hypergraphs, probabilistic combinatorics, and extremal degree conditions. **Central question:** how can an almost-perfect matching be repaired into a perfect one?

<!-- BEGIN SPOKEN LECTURE -->

# The last uncovered vertices are the hardest

Imagine a hypergraph whose edges each contain three vertices. A matching is a collection of edges with no shared vertices. We want a perfect matching: every vertex covered exactly once. Even when the hypergraph is very dense, a greedy matching may stop with a small group of vertices that cannot be covered by any available edge. Most of the task was easy; the final few vertices make it difficult.

The absorption method changes the order of the problem. Instead of using the best edges until only a few difficult vertices remain, reserve a small structure that can accommodate many possible leftovers. Then find an almost-perfect matching in the rest of the hypergraph. Finally rearrange the reserved structure to swallow the leftover vertices.

This is not a numerical optimization heuristic. It is a proof technique for establishing perfect matchings and other spanning structures under quantitative density and divisibility hypotheses.

# An absorber with six reserved vertices

Take three vertices a, b, and c that we may need to absorb. Put aside six additional vertices named x-one through x-six. Suppose the hypergraph contains two disjoint edges on the reserved vertices: the first three x vertices form an edge, and the last three form another.

Then these six vertices have a matching consisting of two edges. Nothing has been covered among a, b, and c.

Now suppose three different edges are also present: one using a, x-one, and x-two; another using b, x-three, and x-four; and a third using c, x-five, and x-six. These three edges are disjoint, and together cover the same six reserved vertices plus a, b, and c.

The reserved six-vertex set therefore has two matching states. In its original state, it covers only itself. In its absorbing state, it covers itself and the leftover triple. Switching between the states changes the number of covered vertices by exactly three while preserving the matching property.

This little gadget is the core idea. In a complete three-uniform hypergraph all the required edges exist automatically. In a merely dense hypergraph, finding many gadgets for many potential leftovers is a theorem, not a given.

# What an absorbing family must accomplish

An absorbing set cannot be chosen after we learn which leftovers remain, at least not in the standard proof architecture. It must be chosen in advance and be versatile enough to absorb every small leftover set satisfying the necessary divisibility conditions.

Typically one proves that every admissible small vertex configuration has many possible absorber gadgets. By random sampling and discarding overlaps, one selects a relatively small disjoint family of gadgets that still offers enough absorbers for any later leftover set. Each gadget has a bounded number of vertices, but collectively the family has flexibility.

The rest of the hypergraph is large and remains dense enough for a separate almost-perfect matching theorem. This second stage is often obtained by a nibble, a randomized matching process, or a deterministic covering lemma.

At the end, the unmatched vertices are divided into suitable small groups. Each group is assigned a fresh absorber. The old matching inside that absorber is replaced by the alternative matching, and the leftover vertices become covered.

# Why degree and divisibility both matter

No perfect matching exists unless the number of vertices is divisible by three. This is an obvious arithmetic obstruction, but there are subtler ones. For example, partition the vertices into two classes and allow only edges whose intersection with one class has even cardinality. If that class has odd cardinality, a perfect matching is impossible: every matching edge contributes an even number of vertices to the class, but the final total would need to be odd.

Such a parity construction can remain surprisingly dense. It warns us that naive edge density or a greedy algorithm does not prove a perfect matching.

The strongest matching theorems therefore use appropriate minimum degree or codegree conditions and account for divisibility barriers. A codegree condition counts how many edges contain a specified pair of vertices. It is often more informative for three-uniform matching questions than simply counting total edges.

The precise threshold depends on the uniformity of the hypergraph, the type of degree being bounded, and the desired conclusion. A theorem about one of those thresholds should not be quoted as if it covered every density notion.

# The nibble and the absorber play different roles

A probabilistic nibble chooses many candidate edges in rounds, discarding conflicts. Its strength is covering almost all vertices while keeping intersections controlled. It need not finish perfectly, because near the end there may be too few compatible edges to repair the tiny leftover.

Absorption is designed for that last step. Reserving absorbers seems wasteful at first, since they remove vertices that might have been used by the main matching. But the reserved portion is small enough that it does not destroy the almost-perfect matching argument. The two tools are complementary: bulk coverage and exact completion.

This distinction explains why the method has spread beyond matchings. Hamilton cycles, graph decompositions, and combinatorial designs have analogous problems where the main construction reaches nearly all required pieces but leaves a small difficult residue. An absorber stores alternative configurations that repair that residue without rebuilding everything.

# Proof architecture, not a magic gadget

The six-vertex example proves exactly one local switching identity. To prove a global perfect-matching theorem, several further obligations remain. We need plenty of absorbers for each possible leftover, a way to choose them disjointly, an almost-perfect matching in the complement, a small enough leftover, and an assignment of leftover groups to available absorbers. Divisibility must hold throughout.

Leaving out any of those steps can turn a plausible proof into a false one. In particular, the existence of one absorber for one triple is not enough. A matching method that handles most triples but fails on a special arithmetic pattern cannot claim perfection.

What absorption contributes is an elegant reversal of perspective. We plan for the final obstruction before constructing most of the solution. Then a procedure that was formerly doomed to stop just short of perfection becomes a complete spanning construction, because the last vertices were accounted for from the beginning.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `H` be a 3-uniform hypergraph. For leftover triple `T={a,b,c}` and six reserved vertices `X={x1,...,x6}`, suppose the edge set contains
\[
\{x_1,x_2,x_3\},\ \{x_4,x_5,x_6\},
\]
and also
\[
\{a,x_1,x_2\},\ \{b,x_3,x_4\},\ \{c,x_5,x_6\}.
\]
Then there are two disjoint-edge matchings, one covering exactly `X` (two edges) and one covering `X union T` (three edges). The gadget **does not** guarantee that all required edges exist in a general hypergraph. A global absorbing lemma needs a disjoint absorber family capable of handling all eligible small leftovers.

Parity barrier: partition `V=A union B`, require every edge to meet `A` in an even number of vertices, and take `|A|` odd. No perfect matching can cover `A`, since the sum of even intersection cardinalities is even. This obstruction is independent of `|V| divisible by 3`.

### Exercises with answers

1. How many matching edges are used in the two gadget states? **Answer:** two before absorption, three afterward.
2. Why must `3` divide the total vertex count for a perfect 3-uniform matching? **Answer:** disjoint triples partition the vertices.
3. Does an almost-perfect matching by itself imply a perfect one? **Answer:** No; the leftover may violate local or divisibility constraints.
4. Why reserve absorbers before running the almost-perfect matching? **Answer:** the reserve must be available for whatever small leftover remains.

### Reading and source notes

- [Keevash, Hypergraph Matchings and Designs (ICM survey)](https://people.maths.ox.ac.uk/keevash/papers/icm-survey-arxiv.pdf), thresholds, nibble, and absorption. (PDF; link is a reading reference, not reproduced here.)
- [Rödl, Ruciński and Szemerédi, Perfect Matchings in Uniform Hypergraphs with Large Minimum Degree](https://rucinski.home.amu.edu.pl/papers/82.pdf), a foundational absorption-method result.
- [Refined Absorption: a New Proof of the Existence Conjecture](https://epubs.siam.org/doi/full/10.1137/25M1805977), later applications of absorption to combinatorial designs.
