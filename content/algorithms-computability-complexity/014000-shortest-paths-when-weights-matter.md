# Shortest Paths When the Edges Have Weights

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 014000  
**Preparation:** BFS, graph paths, and the notion of a loop invariant.  
**Companion:** Relaxation, Dijkstra, Bellman-Ford, a worked graph, and exercises.

<!-- BEGIN SPOKEN LECTURE -->

Suppose a delivery driver must travel from a depot to every address in a road network. Each road has a travel time. A road can be short in distance but slow to travel; two roads can be faster than one. The question is not how many roads the driver crosses, but what total travel time is smallest. Breadth-first search solved shortest paths by counting edges. We now need shortest paths when each edge has its own numerical weight.

A weighted directed graph assigns a real number to each directed edge. The weight of a path is the sum of its edge weights. For now, assume that there are finitely many vertices. We seek the minimum path weight from a fixed source to each reachable vertex. An unreachable vertex has infinite distance in our bookkeeping, though infinity here is a sentinel rather than a road we can traverse.

The central operation is relaxation. For each vertex keep a tentative distance, initially zero at the source and infinity elsewhere. If an edge runs from u to v with weight w, and the current tentative distance to u is d, then traveling along that edge gives a candidate route to v with weight d plus w. Replace v's tentative distance if that candidate is smaller. Crucially, a finite tentative distance is not an optimistic guess. Every finite tentative label is backed by a concrete path assembled through earlier relaxations. The label is an upper bound on the true shortest-path cost. Relaxation can improve a label but does not invent a physically nonexistent route.

Consider four vertices, A, B, C, and D. From A to B costs four; from A to C costs one; from C to B costs two; from B to D costs one; from C to D costs six. The direct first step from A to B seems reasonable, but the route A to C to B costs three, which is better. Then A to C to B to D costs four, beating A to C to D, which costs seven. If a method permanently accepts the first route it sees, it may be wrong. A shortest-path algorithm needs a proof of when a tentative label becomes final.

Dijkstra's algorithm supplies that proof when all edge weights are nonnegative. Start at the source. Among vertices not yet finalized, choose the vertex with the smallest tentative label. Finalize it, then relax every outgoing edge. Repeat until no reachable tentative vertex remains. In our example, A is finalized first. Its edges give B label four and C label one. C is next. Its edge to B improves B to three, and its edge to D gives D seven. B is next, improving D from seven to four. D is last, with shortest distance four.

Why is it safe to finalize the smallest label? Suppose all previously finalized distances are correct, but the newly chosen vertex u has a genuinely cheaper route than its tentative label. Follow such a cheaper route from the source. Look for the first vertex y on that path that has not yet been finalized, and let x be the predecessor of y, which has already been finalized. The algorithm relaxed the edge from x to y. Since the path prefix to x cannot cost less than the true distance to x, and the true distance to x has already been found, the candidate label of y is no greater than the cost of that prefix to y. With nonnegative weights, completing the rest of the path from y to u cannot make the full path cheaper than its prefix to y. Therefore y has a tentative label no greater than the supposed cheaper route to u. But u was chosen with the smallest tentative label. This contradicts the assumption that u's current label was too large.

The argument has one load-bearing hypothesis: the remaining edges on the path must not have negative weight. If a future edge could reduce a path's cost, the earliest unsettled prefix might look expensive even though the complete route is cheap. Consider A to B with cost two, A to C with cost five, and C to B with cost negative four. Dijkstra finalizes B at cost two before it ever processes C. But A to C to B costs one. Some variants of the algorithm may update a finalized label, but once the proof of finality is abandoned, the usual correctness and efficiency claims no longer apply. The safe rule is simple: standard Dijkstra requires nonnegative edge weights.

An implementation must still find the next smallest tentative label. Scanning every vertex each time yields quadratic time in the number of vertices, plus edge scanning. With adjacency lists and a binary heap priority queue, a common implementation runs in time proportional to vertices plus edges, multiplied by a logarithmic factor in the vertex count. A heap may contain stale entries when a label improves. We can discard a popped entry when its distance is no longer the current best label, or use a data structure supporting decrease-key. The exact complexity bound depends on the choice of data structure and how often it processes entries.

What if edges can be negative? Negative weights are not automatically nonsensical. In a transformed optimization model, a negative edge might represent a discount or a gain. The danger is a path that becomes cheaper each time it loops. A reachable directed cycle with negative total weight permits the cost of walks that go through that cycle to decrease without limit. If that cycle can also reach a destination, there is no finite minimum walk cost to that destination. If the cycle cannot reach a particular destination, it does not affect the minimum for that destination.

Bellman-Ford handles arbitrary edge weights when a finite shortest path exists and identifies reachable negative cycles. It starts with the same tentative labels and relaxes every edge repeatedly. A simple shortest path with finite optimum never needs a repeated vertex: a repeated segment would be a cycle, and in the absence of a usable negative cycle such a segment cannot be needed to lower the optimum. A simple path has at most the number of vertices minus one edges. After one full pass, every path using one edge can have its cost reflected in the labels. After two passes, paths using at most two edges can. Continue until there have been as many passes as vertices minus one.

This is dynamic programming viewed through a graph. Each pass propagates the consequences of one more edge, regardless of whether an early temporary label looks expensive. In our negative-edge example, the second pass can discover the route through C even if the order of edges was unfortunate. If an additional full pass can still strictly improve a reachable label, some reachable negative cycle must exist. With an extra propagation step, we can also mark destinations reachable from such a cycle as having no finite minimum walk cost. Bellman-Ford typically takes time proportional to the number of vertices multiplied by the number of edges. On a large network it may be slower than Dijkstra, but it solves a more general problem.

There is a useful third case. When the directed graph has no cycles, a topological ordering lets us process each vertex after all of its predecessors. One relaxation per edge is enough, even with negative edge weights, because there is no way for a later path to return and alter an earlier decision. This yields time proportional to vertices plus edges. The topological-order algorithm is another example of how structural knowledge about a problem changes which general machinery we need.

All three methods use the same physical operation: take a known path to u, append one edge, and see whether it improves the known path to v. They differ in why an edge will no longer need reconsideration. Dijkstra relies on nonnegative future costs and a minimum tentative label. Bellman-Ford relies on a bound on the number of edges in a simple path. Acyclic shortest paths rely on a precedence order. The implementation follows the proof, not the other way around.

A final distinction concerns paths and walks. When all weights are nonnegative, a shortest route can be taken without cycles, apart from ties involving zero-weight cycles. With negative edges but no relevant negative cycle, a finite optimal walk can again be reduced to a simple path. When a relevant negative cycle exists, asking for the cheapest walk has no finite answer. Demanding a simple path instead produces a different, generally harder problem. A reliable algorithm begins by stating which object is being optimized.

Weighted graph search is a good example of how a small change to a mathematical model can change an algorithmic theorem. The graph has not changed its shape. We have added costs, and that addition changes what can be finalized, what can be certified, and even whether an optimum exists.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For every edge \((u,v)\) with cost \(w(u,v)\), relaxation performs \(d(v)\leftarrow\min(d(v),d(u)+w(u,v))\) if \(d(u)\) is finite. Each finite label has a witnessed source-to-vertex walk. In the graph \(A\to B:4\), \(A\to C:1\), \(C\to B:2\), \(B\to D:1\), \(C\to D:6\), shortest costs are \(0,3,1,4\) for \(A,B,C,D\).

**Dijkstra invariant.** After extracting the minimum unsettled \(u\), its label equals \(\delta(s,u)\) if all edge weights are nonnegative. A hypothetical better route has a first unsettled vertex \(y\) preceded by settled \(x\). Relaxation from \(x\), plus nonnegative suffix costs, would force \(d(y)\le\delta(s,u)<d(u)\), contradicting selection of \(u\).

**Bellman-Ford pass invariant.** After \(k\) complete passes over all edges, labels are at most the weights of all source paths using at most \(k\) edges, and no label is less than a witnessed walk weight. A finite optimum without relevant negative cycles has a simple optimal path with at most \(|V|-1\) edges. Improvement after that many passes implies a reachable negative cycle; not every destination need be reachable from that cycle.

### Exercises with answers

1. **Dijkstra.** On the four-node positive graph, which vertex is finalized second? **Answer:** C, with label one.
2. **Negative edge.** For A to B cost two, A to C cost five, and C to B cost negative four, what is the optimal A-to-B cost? **Answer:** one, so prematurely finalizing B at two is wrong.
3. **Negative cycle.** If a reachable negative cycle cannot reach vertex t, does it make the optimal cost to t negative infinity? **Answer:** No. Only destinations reachable from a usable negative cycle are affected.
4. **Acyclic graph.** Why can a topological pass handle negative edges? **Answer:** Every predecessor is processed before its target, and later vertices cannot return to change earlier labels.

### Reading and attribution

- MIT OpenCourseWare, *Introduction to Algorithms*, Lectures 15-17 on shortest paths: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/.
- Kleinberg and Tardos, *Algorithm Design*, Chapters 4 and 6; Kevin Wayne's course slides: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/.
- The four-node worked example and negative-edge counterexample are original teaching calculations.
