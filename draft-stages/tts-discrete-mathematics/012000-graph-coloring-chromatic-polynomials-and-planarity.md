# 012000 — Graph Coloring, Chromatic Polynomials, and Planarity

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph terminology, counting polynomials, induction. **Central question:** how do coloring constraints interact with cycles, edge contraction, and embeddings in the plane?

<!-- BEGIN SPOKEN LECTURE -->

# Graph Coloring, Chromatic Polynomials, and Planarity

Suppose several tasks must be assigned to time slots, and two tasks connected by an edge are forbidden from occupying the same slot. Or suppose neighboring regions on a map must have different colors. Both problems ask for a proper vertex coloring of a graph: a label on every vertex so that adjacent vertices receive different labels.

The smallest number of colors that permits a proper coloring is the chromatic number. But there is a richer counting question. For each positive integer k, how many proper colorings exist when the colors are distinguished and drawn from a palette of k colors? The answer is a polynomial in k, despite the fact that colorings look like a combinatorial search problem.

## Begin with a tree

Take a tree with n vertices. Choose a root. It has k possible colors. Every other vertex has exactly one parent. Once its parent is colored, it may use any of the remaining k minus one colors. Walking outward from the root, each choice is independent of earlier nonparent choices because a tree has no cycles.

So the number of proper colorings is k times k minus one raised to the n minus one. Notice that the formula also tells us the chromatic number: any nontrivial tree is two-colorable, but not one-colorable.

For a complete graph on n vertices, every pair must have different colors, so the count is k times k minus one times k minus two and so on, with n factors. At the opposite extreme, a graph with no edges has k to the n colorings. These formulas are simple enough to verify by direct choices; the interesting part is how to handle graphs assembled from more complicated pieces.

## Deletion and contraction

Choose an edge e connecting two distinct vertices. Delete that edge. Now the endpoints are allowed to have the same color. Of the colorings of the deleted-edge graph, some assign different colors to the endpoints; those are exactly the proper colorings of the original graph. The remaining colorings assign the same color to the endpoints. If we identify the endpoints, those remaining colorings become colorings of a contracted graph.

Thus the chromatic polynomial of the original graph equals that of the graph with the edge deleted minus that of the graph with the edge contracted. Parallel edges do not change proper-coloring counts, and a loop makes proper coloring impossible. These conventions make the recurrence work cleanly.

Repeated deletion and contraction eventually reaches graphs we can count directly. The recurrence proves by induction on the number of edges that every finite loopless graph has a chromatic polynomial. It also explains some of its coefficient structure: the leading term is k to the number of vertices, and the next coefficient is minus the number of edges for a simple graph.

## Cycles are where the complication starts

For a cycle with n vertices, the chromatic polynomial is k minus one to the n, plus negative one to the n times k minus one. The extra signed term comes from the requirement that the final vertex and the first receive different colors. Unlike a tree, there is a closed consistency condition at the end.

For a triangle, the formula becomes k times k minus one times k minus two, as expected for a complete graph on three vertices. For a four-cycle and two colors, the formula gives two proper colorings, corresponding to the two alternating assignments. An odd cycle cannot be colored with two colors, because alternating along the cycle returns to the start demanding the opposite of the color already assigned.

The chromatic number therefore detects a cycle property: a graph is bipartite exactly when it contains no odd cycle. This is a structural characterization, not just a counting trick.

## Why planarity places a bound on edges

A planar graph can be drawn in the plane without edge crossings, apart from common endpoints. In a connected plane drawing, Euler's formula states that the number of vertices minus edges plus faces equals two. The outer face counts as one of the faces.

If the planar graph is simple and has at least three vertices, every face boundary has length at least three, provided we count boundary-edge incidences with multiplicity. Summing face boundary lengths counts every edge twice. Therefore three times the number of faces is at most twice the number of edges. Substitute this bound into Euler's formula, and obtain the familiar inequality: the number of edges is at most three times the number of vertices minus six.

This inequality fails for graphs with loops or sufficiently many parallel edges, which is why the hypotheses matter. For simple planar graphs it has an immediate implication: the average degree is strictly less than six. So some vertex has degree at most five.

## A coloring theorem from that inequality

Take any finite simple planar graph. Remove a vertex of degree at most five, color the smaller graph recursively using six colors, and then put the vertex back. At most five colors are used by its neighbors, leaving one of the six colors available for the vertex. This proves that every simple planar graph is six-colorable.

The argument is short because it uses only Euler's formula and induction. Stronger results exist: the five-color theorem can be proved by a more delicate recoloring argument; the four-color theorem required substantial computer-assisted proof work. We should not mistake the easy six-color induction for a proof of four-colorability. It establishes a weaker statement with a clear mechanism.

## Chromatic polynomials and planar structure

Planarity is a property of embedding; the chromatic polynomial is a graph invariant independent of a particular drawing. Their connection has fascinated mathematicians because constraints on cycles and faces influence coloring behavior. In a planar graph, a dual graph may turn questions about colorings into questions about flows, although the precise polynomial relationships require hypotheses about connectivity and the treatment of bridges and loops.

There is also a computational warning. The existence of a polynomial formula in the number of colors does not make evaluating that polynomial easy on arbitrary graphs. Deletion-contraction branches over combinatorially many subgraphs in the worst case. A neat algebraic expression and an efficient algorithm are different achievements.

The themes now meet: trees are easy because choices propagate without closing constraints; cycles introduce consistency; deletion-contraction converts graph constraints into an algebraic recurrence; and planar embeddings place global numerical restrictions on the graph itself. Coloring is not merely the assignment of labels. It is a window into what local restrictions force globally.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a finite graph \(G\), the **chromatic polynomial** \(P_G(k)\) counts proper vertex maps \(V(G)\to\{1,\ldots,k\}\). For a non-loop edge \(e\),
\[
P_G(k)=P_{G-e}(k)-P_{G/e}(k).
\]
Loops imply \(P_G=0\); parallel edges may be simplified because they impose identical inequalities. Important examples:
\[
P_{K_n}(k)=k(k-1)\cdots(k-n+1),\quad
P_{T_n}(k)=k(k-1)^{n-1},\quad
P_{C_n}(k)=(k-1)^n+(-1)^n(k-1).
\]
A finite graph is bipartite iff it has no odd cycles.

For a finite connected **simple** planar graph with \(n\ge3\) vertices, Euler's formula \(n-m+f=2\) and face-degree counting give
\[
3f\le2m\quad\Longrightarrow\quad m\le3n-6.
\]
The same edge bound holds for disconnected simple planar graphs with \(n\ge3\) by adding edges to connect components in a planar embedding. Thus every simple planar graph has a vertex of degree at most five; inductively \(\chi(G)\le6\). This is not a proof of the four-color theorem.

### Exercises with answers

1. How many proper 3-colorings does a path on four vertices have? **Answer:** \(3\cdot2^3=24\).
2. Evaluate \(P_{C_4}(2)\). **Answer:** \((2-1)^4+(2-1)=2\).
3. Why is a triangle not bipartite? **Answer:** it is an odd cycle, whose alternating two-color assignment is inconsistent.
4. Give an edge bound for a simple planar graph with ten vertices. **Answer:** \(m\le24\).
5. Does the polynomial formula imply a polynomial-time exact evaluation algorithm for arbitrary input graphs? **No:** the formula counts values, but extracting them may still require exponential computation.

### Reading and source notes

- Reinhard Diestel, [*Graph Theory*, sixth edition (2025), free chapter preview](https://diestel-graph-theory.com/basic.html?level=1), chapters on planar graphs and coloring.
- MIT OCW, [*Mathematics for Computer Science*](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), graph coloring and combinatorial counting.
