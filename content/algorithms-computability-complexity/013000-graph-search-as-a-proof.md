# Finding Your Way Through a Graph: Search as a Proof

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 013000  
**Preparation:** Finite sets, loops, induction, and elementary asymptotic reasoning.  
**Companion:** Exact algorithms, invariants, examples, and exercises.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a network of rooms, connected by doors. You know which rooms are joined, but you do not know whether the exit is reachable. At each room you can inspect the neighboring rooms. What would count as an answer? Finding a route is one answer. Demonstrating that no route exists is another, and the second demands a proof that your search has not simply overlooked a doorway.

A graph is a mathematical model of this situation. Its vertices are rooms and its edges are connections. In an undirected graph each edge can be traversed both ways. In a directed graph an arrow from one vertex to another permits movement only in the arrow's direction. A path is a sequence of adjacent vertices; in a directed graph every step must follow an arrow. A graph may be disconnected, and even a directed graph whose underlying undirected picture looks connected may have vertices that cannot be reached from your starting point.

Before choosing an algorithm, we choose a representation. An adjacency list stores, for each vertex, the vertices it can reach in one step. An adjacency matrix uses a square table with a cell for every ordered pair of vertices. The matrix makes a particular adjacency query cheap, but even an almost empty graph occupies space proportional to the square of its vertex count. An adjacency list uses storage proportional to the number of vertices plus the number of stored edges, with the conventional representation counting both directions of an undirected edge. A search should pay for the connections that exist, not for every connection that might have existed.

Breadth-first search begins at a source vertex. Put the source in a queue, mark it discovered, and give it distance zero. Remove a vertex from the front of the queue. For each of its outgoing neighbors not yet discovered, record the current vertex as that neighbor's parent, give the neighbor distance one more than the current distance, and append the neighbor to the queue. Repeat until the queue is empty. The queue is first in, first out: vertices discovered earlier are processed earlier.

Try a small example. From A there are connections to B and C. From B, there is a connection to D. From C, there are connections to D and E. Suppose we inspect B before C. Initially A has distance zero. Processing A discovers B and C at distance one. Processing B discovers D at distance two. Processing C finds D already discovered and discovers E at distance two. Reaching D through C would also take two steps, but we do not need to replace its parent. If we only care about finding one shortest route, either shortest route will do.

Why are those distance labels correct? Every discovered vertex has a path from A of the recorded length: follow its parent backward to A. Thus the label cannot be smaller than the true shortest-path distance without violating the definition of shortest distance. The other inequality is the interesting one. The queue processes vertices in nondecreasing order of their recorded distances. All distance-one vertices enter after A and before any distance-two vertex. In general, when a vertex at level k is processed, each newly found neighbor enters at level k plus one, after the vertices already waiting at level k. Consequently the search never jumps ahead to a longer route while an undiscovered shorter route is still available through an earlier level. Combining the constructed paths and the queue order proves the labels equal the shortest number of edges from the source.

We have just proved something stronger than reachability. Breadth-first search constructs a shortest-path tree for every reachable vertex, where shortest means fewest edges, not least physical distance or least travel time. If a road takes eight hours and another takes one minute, counting each road as one edge ignores that difference. Weighted shortest paths require a different method.

What proves that an unreachable vertex is unreachable? Consider the set of discovered vertices after the queue empties. Every discovered vertex has had all its outgoing neighbors inspected. Therefore no outgoing edge leads from that discovered set to any undiscovered vertex. If an undiscovered vertex were reachable, a path from the source to it would have to cross from the discovered set to the undiscovered set at some first edge. But we have checked every such outgoing edge, and none exists. The absence of a path now has a finite certificate: an explored set closed under outgoing neighbors, containing the source but excluding the destination.

Depth-first search arranges the exploration differently. Rather than keeping a queue of frontier vertices, it enters one unvisited neighbor immediately, then a neighbor of that neighbor, following a chain until no further unvisited neighbor remains. It then backs up to the last vertex with an unexplored outgoing edge. The recursion stack, or an explicit stack in an iterative implementation, remembers where to return. Depth-first search can still establish reachability and produce a path, but its first discovered path need not be a shortest one.

To see the distinction, give A a direct edge to E, and also a chain A to B, B to C, C to D, D to E. A depth-first search that visits B before E might discover E by four edges, even though the direct edge uses only one. A breadth-first search discovers E at level one. Neither algorithm is better in every sense. Breadth-first search organizes the reachable graph by distance. Depth-first search exposes the nesting of exploration and the structure of cycles.

That nesting yields another theorem. In a directed graph, color each vertex white before discovery, gray while its recursive exploration is active, and black once all its outgoing edges have been considered. If we encounter an edge from a gray vertex to another gray vertex that is an ancestor on the active recursion stack, the edge closes a directed cycle. Conversely, in a directed cycle, a depth-first search that reaches a vertex of that cycle will eventually encounter a back edge to a gray ancestor. Thus the directed graph has a cycle exactly when DFS discovers such a back edge in a complete traversal.

A directed acyclic graph has no such cycles. When depth-first search finishes exploring a vertex, every vertex it can reach directly has already finished. Put vertices into a list at finishing time, then reverse the list. For every directed edge from u to v, u appears before v in this reversed list, provided the graph is acyclic. That is a topological order: a schedule satisfying all the precedence arrows. The proof uses the absence of back edges. An arrow from u to v either leads DFS into v, which then finishes before u, or points to a vertex already finished. It cannot point to a still-active ancestor in an acyclic graph.

Search has an important cost argument too. With an adjacency-list representation, each vertex is marked once. We inspect each stored outgoing adjacency entry once, when its source vertex is processed. For a directed graph there are as many entries as edges; for a conventional undirected list there are twice as many. Either way, a complete search requires time proportional to vertices plus edges. There is no hidden loop over all possible pairs of vertices. With a matrix representation, scanning all possible neighbors of each visited vertex can instead cost time proportional to the square of the vertex count. An asymptotic claim without its representation and cost model is incomplete.

There are useful implementation traps. Mark a vertex discovered when it enters the queue, not when it leaves. Otherwise a densely connected frontier can insert the same vertex many times. Do not infer a shortest route from DFS parent pointers. For directed cycle detection, a visited mark alone is insufficient: an edge to a finished vertex is not the same as an edge to an active ancestor. In an undirected graph, the edge back to a vertex's parent is not by itself evidence of a nontrivial cycle. And if your algorithm is supposed to examine a disconnected graph, restart the traversal from every still-unvisited vertex.

Return to the network of rooms. A concrete list of doors supplies an algorithmic specification, a traversal supplies a witness when the exit is reachable, and the closed explored set supplies a witness when it is not. This is a recurring pattern in algorithms: a procedure is trustworthy when we can explain what remains true at every step and why the completed computation answers the question we actually asked.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For directed graph \(G=(V,E)\) and source \(s\), BFS maintains a queue \(Q\), `seen`, integer distances \(d\), and parent pointers. Initialize \(d(s)=0\), enqueue \(s\), and for each dequeued \(u\), set \(d(v)=d(u)+1\), `parent[v]=u`, and enqueue \(v\) for each previously unseen edge \((u,v)\). Every vertex enters the queue at most once, and every adjacency entry is inspected once: \(O(|V|+|E|)\) time and \(O(|V|)\) auxiliary memory, excluding adjacency storage.

**BFS distance proof.** The parent chain certifies a path of length \(d(v)\), hence \(\delta(s,v)\le d(v)\). Queue monotonicity implies vertices are processed in nondecreasing label order. An induction on \(\delta(s,v)\) shows every vertex at distance \(k\) is discovered with label no greater than \(k\): a shortest-path predecessor at distance \(k-1\) is processed before all potential labels greater than \(k\). Hence equality.

**No-path certificate.** At termination the visited set \(S\) contains \(s\) and satisfies \(N^+(S)\subseteq S\). Any path starting in \(S\) stays in \(S\). So any \(t\notin S\) is unreachable from \(s\).

**DFS finish order.** For a DAG, if \((u,v)\in E\), the DFS finish time of \(u\) is strictly after that of \(v\); otherwise \(v\) would be gray when examined, exhibiting a cycle. Reversing finish order is a topological sort.

### Exercises, with answers

1. **Queue order.** On directed edges A to B, A to C, B to D, C to D, and C to E, with alphabetical neighbor order, list BFS discoveries and labels from A. **Answer:** A at 0; B and C at 1; D and E at 2. Parents of D and E are B and C respectively.
2. **Two meanings of shortest.** Two A-to-Z routes have edge-counts two and three but costs nine and four. Which does BFS select? **Answer:** The two-edge route. Weighted costs are outside its promise.
3. **Directed cycle.** Why is any edge to a previously visited vertex not automatically a cycle proof? **Answer:** The target may be black (finished), not a gray ancestor; a back edge to the active DFS stack is the directed cycle witness.
4. **Representation.** A graph has one million vertices and only two million directed edges. Why might an adjacency matrix be unsuitable? **Answer:** It has a trillion entries while an adjacency list has storage linear in the vertices plus edges.

### Reading and attribution

- MIT OpenCourseWare, *Introduction to Algorithms*, Lecture 13 (BFS) and Lecture 14 (DFS and topological sorting): https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/.
- Kleinberg and Tardos, *Algorithm Design*, Chapter 3; course slides by Kevin Wayne: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/.
- The room-network example and the explicit two-sided reachability certificate are original worked exposition.
