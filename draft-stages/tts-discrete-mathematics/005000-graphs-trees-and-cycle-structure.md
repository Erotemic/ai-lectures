# 005000 — Graphs, Trees, and the Structure of Cycles

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite sets, counting, mathematical induction. **Question:** how can a few local edge conditions determine the global structure of a graph?

<!-- BEGIN SPOKEN LECTURE -->

# Graphs, Trees, and the Structure of Cycles

A network of roads, dependencies, or friendships is a graph when we retain only which objects are connected. A graph has vertices and edges. For this discussion an edge joins two distinct vertices and there is at most one edge between each pair; this is a finite, simple, undirected graph. The definitions can be generalized, but specifying the model prevents small ambiguities from infecting a proof.

Graphs are interesting because several different descriptions can force the same global structure. A tree is connected and has no cycles. It is also a connected graph in which removing any edge disconnects the graph. And it is a graph in which any two vertices are joined by exactly one simple path. These do not look like identical definitions. Proving their equivalence gives a compact lesson in how graph arguments work.

## Paths and cycles

A walk is a sequence of vertices in which consecutive vertices are adjacent. It may revisit vertices and edges. A path, in the simple sense, is a walk with no repeated vertices. A cycle visits distinct vertices around a closed loop, apart from repeating its start at the end. Connectivity means that every pair of vertices can be joined by a path.

Why can we insist on a simple path rather than some complicated walk? If a walk repeats a vertex, delete the portion between the two visits. The remainder is still a walk with the same endpoints but fewer steps. Repeating this process eventually leaves a simple path. This elementary deletion argument is valuable: it turns an existential statement about arbitrary walks into one about finite, nonrepeating objects.

Now suppose a connected graph has no cycles. If two distinct simple paths joined the same pair of vertices, follow them from the start until their first divergence, and then find where they first meet again. Together those differing segments form a cycle. That contradicts acyclicity. So there is exactly one simple path between any two vertices.

Conversely, if every pair has exactly one simple path, the graph is connected by definition, and it cannot contain a cycle. Two vertices on a cycle would have two different simple routes along that cycle. We have proved the first equivalence.

## Why a tree has one fewer edge than vertices

A nonempty finite tree with v vertices has v minus one edges. The natural proof removes a leaf. A leaf is a vertex of degree one. Every finite tree with at least two vertices has at least two leaves: take a longest simple path. If one of its endpoints had a neighbor not already on the path, we could extend it; if that neighbor were already on the path, we would create a cycle. Hence each endpoint is a leaf.

Delete one leaf and its incident edge. The remaining graph stays connected and acyclic, so it is a tree with one fewer vertex and one fewer edge. Starting from a one-vertex tree with zero edges, induction gives exactly v minus one edges.

The converse needs a qualification. Having v minus one edges alone does not make a graph a tree. A triangle together with an isolated vertex has four vertices and three edges but is disconnected and has a cycle. However, a *connected* graph with v minus one edges must be a tree. To see why, begin with any connected graph and repeatedly delete edges that lie on cycles. Deleting such an edge does not disconnect the graph, because the rest of that cycle provides an alternate route. Eventually we obtain a spanning tree, which has v minus one edges. If the original graph already had exactly that many, no edge could have been deleted; it was a tree from the start.

This gives the notion of a spanning tree: a connected, acyclic subgraph containing every vertex. Every connected finite graph has one. It is a minimal structure that retains all connections.

## Handshakes and degrees

Let the degree of a vertex be the number of edges incident to it. If we add degrees over all vertices, every edge is counted twice, once at each endpoint. Thus the sum of all degrees equals twice the number of edges. This is the handshake lemma, and it immediately implies that the number of vertices of odd degree is even.

Why? The sum of all degrees is even. Contributions from even-degree vertices add to an even number. An odd number of odd summands would make the total odd, which is impossible. This argument can rule out proposed degree sequences before we attempt to draw a graph.

It also helps with traversing edges. An Euler trail uses each edge exactly once, though vertices may repeat. Except at the starting and ending vertices, each time a trail arrives it must leave along an unused edge. Edges at these internal vertices are therefore paired. Thus a connected graph with edges can have an Euler trail only if it has zero or two vertices of odd degree. Conversely, if exactly zero or two vertices are odd and all non-isolated vertices lie in one connected component, an Euler trail exists. A constructive argument repeatedly follows unused edges, forming closed walks where possible, and splices them together until every edge is used. When two vertices are odd, begin at one and end at the other. When none are odd, the trail may be closed.

## Cycles as independent choices

Suppose a graph has v vertices, e edges, and c connected components. Choose a spanning tree separately in each component. Their union is a spanning forest, containing v minus c edges. Every remaining edge, when added back to the forest, creates exactly one cycle: the unique forest path between its endpoints together with the new edge. Therefore the number of edges outside the forest is e minus v plus c.

This number is more than a count of extra connections. Over the two-element field, represent each subset of edges by a zero-one vector, and add vectors by taking symmetric difference of edge sets. The subsets in which every vertex has even degree form a vector space called the cycle space. Each nonforest edge gives a fundamental cycle, and those cycles form a basis. Independence is easy: each fundamental cycle contains a particular nonforest edge that none of the other fundamental cycles uses. They span because, after taking a suitable symmetric difference with these fundamental cycles, an even-degree edge set supported only on a forest remains; such a set must be empty, since any nonempty forest has a leaf of degree one.

So the dimension of the cycle space is e minus v plus c. The number of independent cycles is a rigorous invariant, not merely a picture-dependent guess. A graph can have many overlapping ordinary cycles, yet their even-degree combinations are controlled by a small basis.

## Why trees are the correct baseline

A graph may contain redundant routes, bottlenecks, isolated components, and cycles. The spanning forest provides a baseline from which all of those features can be counted or tested. Trees express connectivity with no redundant edges. The handshake lemma expresses global parity using local degrees. The cycle-space dimension measures how many independent ways the network can loop back on itself.

These are structural facts, not properties of a particular traversal algorithm. Once they are understood, algorithms for spanning trees, connectivity, shortest paths, and network design can exploit them rather than treating graph exploration as a collection of unrelated tricks.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(G=(V,E)\) be a finite undirected simple graph with \(v=|V|\), \(e=|E|\), and \(c\) connected components.

**Equivalent tree properties (nonempty graphs):** connected and acyclic; unique simple path between any two vertices; connected with \(e=v-1\); acyclic with \(e=v-1\). A connected graph has a spanning tree. Any spanning forest has \(v-c\) edges.

**Handshake lemma:** \(\sum_{u\in V}\deg(u)=2e\); in particular, the number of odd-degree vertices is even.

**Cycle space:** Over \(\mathbb F_2\), the incidence map \(\partial:\mathbb F_2^E\to\mathbb F_2^V\) sends each edge to the sum of its endpoints. Then \(\ker\partial\) is the even-degree edge-subset space and
\[
\dim\ker\partial=e-v+c.
\]
A fundamental-cycle basis is obtained from a chosen spanning forest and one cycle per nonforest edge.

### Exercises with answers

1. A connected graph has nine vertices and eight edges. Can it contain a cycle? **Answer:** no, it must be a tree.
2. Can a graph have exactly three odd-degree vertices? **Answer:** no, by the handshake lemma.
3. A graph has twelve vertices, fifteen edges, and two connected components. What is its cycle-space dimension? **Answer:** \(15-12+2=5\).
4. A triangle and an isolated vertex have four vertices and three edges. Why is the graph not a tree? **Answer:** it is disconnected and contains a cycle; edge count alone is insufficient.

### Reading

MIT OpenCourseWare, [Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), chapters on graph theory and trees.
