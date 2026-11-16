# 010000 — Extremal Graph Theory: How Many Edges Avoid a Clique?

**Track:** Discrete Mathematics and Combinatorics. **Background:** simple graphs, complete graphs, counting edges, and induction. **Central question:** how dense can a graph be without containing a forbidden pattern?

<!-- BEGIN SPOKEN LECTURE -->

# Extremal Graph Theory: How Many Edges Avoid a Clique?

A graph may have thousands of edges and still be missing a particular structure. If we forbid triangles, how many edges can we retain? If we forbid four vertices all connected to each other, can we keep more? There is a precise answer, and it is a model of extremal combinatorics: determine the largest or smallest possible quantity subject to a structural prohibition.

The simplest version has an elegant solution. A triangle-free graph on n vertices has at most the integer part of n squared divided by four edges. The bound is achieved by dividing the vertices into two groups as evenly as possible and connecting every vertex in one group to every vertex in the other. No triangle is possible, because every step along an edge changes groups, while a triangle would require an odd number of such changes and return to the starting group.

Why is a balanced bipartite graph optimal, and what happens when we forbid larger complete subgraphs?

## Mantel's theorem from degree counting

Let m be the number of edges, and let each vertex have a degree equal to its number of neighbors. Choose any edge joining u and v. If u and v shared a neighbor, those three vertices would form a triangle. Because triangles are forbidden, the neighbors of u and the neighbors of v are disjoint sets. Their degrees therefore add to at most n.

Sum that inequality over all m edges. On the left, each vertex of degree d contributes d once for each of its d incident edges. Hence the left side is the sum of the squares of all the vertex degrees. We obtain: sum of squared degrees is at most n times m.

Now use the Cauchy–Schwarz inequality. The sum of squared degrees is at least the square of the sum of degrees divided by n. But the sum of degrees is twice m. Combining the two bounds gives four times m squared divided by n at most n times m. For a nonempty graph, cancel m and conclude that four m is at most n squared.

So the number of edges is at most n squared divided by four. Since it is an integer, we take the integer part. A complete bipartite graph with two parts as equal as possible has exactly that many edges, so the bound is sharp. This is Mantel's theorem.

The argument is worth remembering because it extracts a global extremal bound from a local obstruction. Every edge says that its endpoints cannot have a common neighbor; degree counting turns that local statement into a numerical inequality governing the whole graph.

## Beyond triangles

Now forbid a clique on r plus one vertices: a set of r plus one vertices with every possible edge between them. The natural construction has r groups. Connect all pairs of vertices in different groups and no pairs within a group. Any clique uses at most one vertex from each group, so no clique can have r plus one vertices.

To maximize edges, balance the group sizes. If one group has at least two more vertices than another, move one vertex from the larger group to the smaller group. The number of cross-group edges increases. Therefore optimal group sizes differ by at most one. The resulting graph is the balanced complete r-partite graph, commonly called the Turán graph.

Turán's theorem says this construction is not merely one good answer. It has as many edges as any graph with no clique on r plus one vertices. In particular, the maximum is approximately one minus one over r, multiplied by n squared over two, with an exact correction determined by the remainder when n is divided by r.

For example, take seven vertices and forbid a complete graph on four vertices. We use three groups of sizes three, two, and two. Between the first and second groups there are six edges, between the first and third another six, and between the two smaller groups four. That makes sixteen edges. No four-clique occurs, and Turán's theorem says no other seven-vertex graph without a four-clique has more than sixteen edges.

## An inductive proof of the general bound

There is a particularly instructive proof that avoids complicated rearrangements of arbitrary graphs. Fix r and suppose we have an edge-maximal graph on n vertices with no clique of size r plus one. Edge-maximal means that adding any missing edge creates a forbidden clique. We can restrict attention to such graphs because adding permissible edges can only increase the number of edges.

When n is at least r, such a graph contains a clique on r vertices. If there were a missing edge, the new forbidden clique produced by adding it would contain an r-clique already present. And if there were no missing edge, the graph is complete; because it forbids a clique of size r plus one, the case with n at least r must have n equal to r.

Choose an r-clique. Any vertex outside it can be connected to at most r minus one vertices inside. Otherwise that outside vertex and the chosen clique would make a forbidden clique of size r plus one. Thus the edges meeting our clique number at most r choose two, plus r minus one times n minus r.

The graph remaining after deleting the chosen r vertices is still free of the forbidden clique. By induction, its edge count cannot exceed that of the Turán graph on n minus r vertices. Put the bounds together. The result is exactly the number of edges in the balanced r-partite graph on n vertices: to grow that graph by r vertices, add one vertex to each part, thereby creating an r-clique among the newcomers and at most r minus one connections from each old vertex to them.

This matches the construction and proves the sharp bound. The proof works in blocks of r vertices and uses the forbidden clique to control how many new cross edges a block can contribute. It also explains why the extremal shape is multipartite, even though the argument does not need to classify every case of equality.

## What the theorem does and does not say

A graph is clique-free here when it contains no forbidden clique as a subgraph, not merely when it contains none as an induced subgraph. This distinction matters: forbidding induced patterns is a different problem. Also, a graph with no four-clique may contain many triangles; it need not be triangle-free.

Turán's theorem identifies a sharp edge threshold for forcing a complete subgraph. Many other extremal questions ask what happens when the forbidden graph is a cycle, a complete bipartite graph, or a more complicated configuration. The answers can differ dramatically, and the optimizers need not be multipartite.

The deeper method is to put two tasks side by side. First construct a dense object without the forbidden pattern. Then prove no denser object is possible. When the construction and the upper bound agree, we have an exact extremal theorem rather than an approximation or an isolated example.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a simple graph \(G=(V,E)\) with \(|V|=n\), \(|E|=m\), the handshake lemma gives \(\sum_v d(v)=2m\). If \(G\) is triangle-free, then for every edge \(uv\), \(N(u)\cap N(v)=\varnothing\), hence \(d(u)+d(v)\le n\). Thus
\[
\sum_v d(v)^2=\sum_{uv\in E}(d(u)+d(v))\le mn.
\]
Cauchy–Schwarz gives \(4m^2/n\le \sum_v d(v)^2\), therefore \(m\le\lfloor n^2/4\rfloor\) for \(m>0\); the case \(m=0\) is immediate. Equality is realized by \(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\).

**Turán's theorem.** For \(r\ge1\), the maximum edges in a \(K_{r+1}\)-free simple graph of order \(n\) is achieved by \(T_r(n)\), the complete \(r\)-partite graph with parts as equal in size as possible (empty parts allowed for \(n<r\)). Writing \(n=qr+s\), \(0\le s<r\), its sizes are \(q+1\) repeated \(s\) times and \(q\) repeated \(r-s\) times. Hence
\[
e(T_r(n))=\frac12\left(n^2-s(q+1)^2-(r-s)q^2\right).
\]
For \(n\ge r\), removing one vertex from each part yields the recurrence
\[
e(T_r(n))=e(T_r(n-r))+(r-1)(n-r)+\binom r2.
\]
An edge-maximal \(K_{r+1}\)-free graph of order \(n\ge r\) contains a \(K_r\). Removing any such \(K_r\), the exterior has at most \(e(T_r(n-r))\) edges by induction and at most \((r-1)(n-r)\) edges connect to the clique. The recurrence completes the proof.

**Worked example.** \(T_3(7)\) has parts \(3,2,2\), so \(e=3\cdot2+3\cdot2+2\cdot2=16\). A 7-vertex \(K_4\)-free graph cannot exceed 16 edges.

### Exercises with answers

1. Find the extremal edge count for triangle-free graphs of order nine. **Answer:** \(\lfloor81/4\rfloor=20\).
2. What does forbidding \(K_4\) permit that forbidding \(K_3\) excludes? **Answer:** triangles.
3. Compute \(e(T_3(8))\). **Answer:** parts \(3,3,2\); edges \(9+6+6=21\).
4. If two parts of a complete multipartite graph have sizes \(a\) and \(b\) with \(a\ge b+2\), what happens when a vertex moves from the larger to the smaller? **Answer:** the edge count increases by \(a-b-1>0\).

### Reading and source notes

- [Graph Theory course notes](https://cs.bme.hu/fcs/graphtheory.pdf), Section 4, Turán's theorem and its clique-removal induction proof.
