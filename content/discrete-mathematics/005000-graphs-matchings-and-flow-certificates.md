# Graphs, matchings, and flow certificates

<!-- BEGIN SPOKEN LECTURE -->

# Graphs, matchings, and flow certificates

## Graphs, Trees, and the Structure of Cycles

A network of roads, dependencies, or friendships is a graph when we retain only which objects are connected. A graph has vertices and edges. For this discussion an edge joins two distinct vertices and there is at most one edge between each pair; this is a finite, simple, undirected graph. The definitions can be generalized, but specifying the model prevents small ambiguities from infecting a proof.

Graphs are interesting because several different descriptions can force the same global structure. A tree is connected and has no cycles. It is also a connected graph in which removing any edge disconnects the graph. And it is a graph in which any two vertices are joined by exactly one simple path. These do not look like identical definitions. Proving their equivalence gives a compact lesson in how graph arguments work.

### Paths and cycles

A walk is a sequence of vertices in which consecutive vertices are adjacent. It may revisit vertices and edges. A path, in the simple sense, is a walk with no repeated vertices. A cycle visits distinct vertices around a closed loop, apart from repeating its start at the end. Connectivity means that every pair of vertices can be joined by a path.

Why can we insist on a simple path rather than some complicated walk? If a walk repeats a vertex, delete the portion between the two visits. The remainder is still a walk with the same endpoints but fewer steps. Repeating this process eventually leaves a simple path. This elementary deletion argument is valuable: it turns an existential statement about arbitrary walks into one about finite, nonrepeating objects.

Now suppose a connected graph has no cycles. If two distinct simple paths joined the same pair of vertices, follow them from the start until their first divergence, and then find where they first meet again. Together those differing segments form a cycle. That contradicts acyclicity. So there is exactly one simple path between any two vertices.

Conversely, if every pair has exactly one simple path, the graph is connected by definition, and it cannot contain a cycle. Two vertices on a cycle would have two different simple routes along that cycle. We have proved the first equivalence.

### Why a tree has one fewer edge than vertices

A nonempty finite tree with v vertices has v minus one edges. The natural proof removes a leaf. A leaf is a vertex of degree one. Every finite tree with at least two vertices has at least two leaves: take a longest simple path. If one of its endpoints had a neighbor not already on the path, we could extend it; if that neighbor were already on the path, we would create a cycle. Hence each endpoint is a leaf.

Delete one leaf and its incident edge. The remaining graph stays connected and acyclic, so it is a tree with one fewer vertex and one fewer edge. Starting from a one-vertex tree with zero edges, induction gives exactly v minus one edges.

The converse needs a qualification. Having v minus one edges alone does not make a graph a tree. A triangle together with an isolated vertex has four vertices and three edges but is disconnected and has a cycle. However, a *connected* graph with v minus one edges must be a tree. To see why, begin with any connected graph and repeatedly delete edges that lie on cycles. Deleting such an edge does not disconnect the graph, because the rest of that cycle provides an alternate route. Eventually we obtain a spanning tree, which has v minus one edges. If the original graph already had exactly that many, no edge could have been deleted; it was a tree from the start.

This gives the notion of a spanning tree: a connected, acyclic subgraph containing every vertex. Every connected finite graph has one. It is a minimal structure that retains all connections.

### Handshakes and degrees

Let the degree of a vertex be the number of edges incident to it. If we add degrees over all vertices, every edge is counted twice, once at each endpoint. Thus the sum of all degrees equals twice the number of edges. This is the handshake lemma, and it immediately implies that the number of vertices of odd degree is even.

Why? The sum of all degrees is even. Contributions from even-degree vertices add to an even number. An odd number of odd summands would make the total odd, which is impossible. This argument can rule out proposed degree sequences before we attempt to draw a graph.

It also helps with traversing edges. An Euler trail uses each edge exactly once, though vertices may repeat. Except at the starting and ending vertices, each time a trail arrives it must leave along an unused edge. Edges at these internal vertices are therefore paired. Thus a connected graph with edges can have an Euler trail only if it has zero or two vertices of odd degree. Conversely, if exactly zero or two vertices are odd and all non-isolated vertices lie in one connected component, an Euler trail exists. A constructive argument repeatedly follows unused edges, forming closed walks where possible, and splices them together until every edge is used. When two vertices are odd, begin at one and end at the other. When none are odd, the trail may be closed.

### Cycles as independent choices

Suppose a graph has v vertices, e edges, and c connected components. Choose a spanning tree separately in each component. Their union is a spanning forest, containing v minus c edges. Every remaining edge, when added back to the forest, creates exactly one cycle: the unique forest path between its endpoints together with the new edge. Therefore the number of edges outside the forest is e minus v plus c.

This number is more than a count of extra connections. Over the two-element field, represent each subset of edges by a zero-one vector, and add vectors by taking symmetric difference of edge sets. The subsets in which every vertex has even degree form a vector space called the cycle space. Each nonforest edge gives a fundamental cycle, and those cycles form a basis. Independence is easy: each fundamental cycle contains a particular nonforest edge that none of the other fundamental cycles uses. They span because, after taking a suitable symmetric difference with these fundamental cycles, an even-degree edge set supported only on a forest remains; such a set must be empty, since any nonempty forest has a leaf of degree one.

So the dimension of the cycle space is e minus v plus c. The number of independent cycles is a rigorous invariant, not merely a picture-dependent guess. A graph can have many overlapping ordinary cycles, yet their even-degree combinations are controlled by a small basis.

### Why trees are the correct baseline

A graph may contain redundant routes, bottlenecks, isolated components, and cycles. The spanning forest provides a baseline from which all of those features can be counted or tested. Trees express connectivity with no redundant edges. The handshake lemma expresses global parity using local degrees. The cycle-space dimension measures how many independent ways the network can loop back on itself.

These are structural facts, not properties of a particular traversal algorithm. Once they are understood, algorithms for spanning trees, connectivity, shortest paths, and network design can exploit them rather than treating graph exploration as a collection of unrelated tricks.

## Matchings and Hall's Marriage Theorem

Imagine four students and four available projects. Each student lists the projects they would accept. We want to give every student exactly one project, without assigning any project to more than one student. It is easy to try individual assignments and get stuck. The mathematical question is whether *some* assignment works, even if a particular greedy choice fails.

The correct model is a bipartite graph: vertices are divided into a left set of students and a right set of projects, and edges join only a student to an acceptable project. A matching is a set of edges with no shared endpoints. We want a matching that covers every vertex on the left. We do not necessarily require every right vertex to be used, because there may be more projects than students.

A condition on all subsets of students gives an exact answer. It is called Hall's marriage theorem, after Philip Hall.

### The obstruction that no clever assignment can bypass

Take any group S of students, not necessarily all of them. Let N of S be the collection of projects accepted by at least one student in S. If there are five students in S and only four projects in N of S, those five students cannot all receive distinct acceptable projects. This is a counting obstruction: each of those students would require a different project from a pool of size four.

Hall's condition says that for *every* subset S of the left vertices, the number of neighbors is at least the number of vertices in S. The theorem states that this necessary condition is also sufficient. If no group of students collectively has too few available projects, then some assignment covering every student exists.

The phrase every subset is important. Checking only that each student has at least one acceptable project is far too weak. Three students may all accept only the same two projects, even though each has multiple choices. Looking at the full set also is not enough: the total number of distinct projects may exceed the number of students while a small subgroup still has a shortage.

### Proof by splitting a tight set

We can prove sufficiency by induction on the number of left vertices. If there is one student, Hall's condition ensures at least one neighboring project, so assign it. Now suppose there are several students and every subset satisfies the condition.

First consider the case where some nonempty *proper* subset S of students has exactly as many neighboring projects as students. Call it a tight set. By induction, Hall's condition on subsets of S lets us match all students in S into its neighborhood N of S. That uses every project in N of S.

What about the remaining students? Delete S and the projects N of S. The remaining bipartite graph also satisfies Hall's condition. To see this, take any subset T of the remaining students. In the original graph, the neighborhood of S together with T has size at least the size of S plus the size of T. Since the neighborhood of S has exactly the size of S, at least the size of T neighbors lie outside the deleted neighborhood. Those are available to T in the reduced graph. Induction therefore matches the remaining students. Combining the two matchings solves the whole assignment problem.

The other case is that no nonempty proper subset S is tight. Since neighbor counts are integers, every such subset has at least one more neighbor than member. Choose any student x and any one of the projects y that x accepts. Assign x to y and delete both. For any subset T of the remaining students, the original neighborhood had at least the size of T plus one, unless T is empty. Deleting y can remove at most one project, so the remaining neighborhood still has at least the size of T. By induction we can match everyone else.

That completes the proof. Either a tight subgroup splits the problem into two smaller independent assignments, or every proper subgroup has enough slack that we may commit to one arbitrary edge. Notice the strength of this dichotomy: a naive greedy assignment can fail in general, but in the strict-slack case it cannot destroy Hall's condition.

### An alternating path repairs a bad choice

There is another way to understand matchings. Suppose we currently have a matching, but some student remains unmatched. Search for a path that starts at that student, alternates between edges not in the matching and edges in the matching, and ends at an unmatched project. Such a path is called augmenting.

Flip the status of every edge along the path: previously unmatched edges become matched, and previously matched edges become unmatched. Every internal vertex on the path still has exactly one matching edge, but both endpoints become matched. The total matching size increases by one.

Here is a concrete example. Student A accepts projects one and two. Student B accepts only project one. If we first assign A to one, B appears stuck. But the alternating path runs from B to project one, then back along A's matched edge, then from A to project two. Flip it. B gets project one and A gets project two. Nothing about the acceptable pairs changed. Only the initial choice was wrong.

This yields a useful characterization: a matching is maximum in size if and only if it has no augmenting path. One direction is immediate: an augmenting path would make the matching larger. For the other direction, compare a proposed matching with a larger one. In their symmetric difference, components are alternating paths and cycles. Because the second matching has more edges overall, some alternating path contains one more edge of the larger matching and begins and ends at unmatched vertices of the proposed matching. That is an augmenting path.

### Failure has a certificate too

If no matching covers all left vertices, Hall's theorem guarantees a set S with fewer neighbors than vertices. This set is a concise certificate of impossibility. It does not depend on guessing which assignment an algorithm ought to try. It names the collective shortage.

There is also a famous relationship between matching and vertex covers. A vertex cover is a set of vertices touching every edge. Every matching edge needs a separate covered endpoint, so any vertex cover has at least as many vertices as a matching has edges. In bipartite graphs, König's theorem says equality is always possible: the maximum matching size equals the minimum vertex-cover size.

A constructive proof starts with a maximum matching. From every unmatched left vertex, traverse alternating paths, going along unmatched edges from left to right and matching edges from right to left. Let Z be the set of vertices reached. Then take all left vertices *not* in Z together with all right vertices *in* Z. This is a vertex cover whose size equals the matching size. If the sizes differed, the alternating reachability structure would expose an augmenting path. This argument connects the matching problem to the broader idea of mathematical certificates: a feasible matching gives a lower bound, while a vertex cover gives an upper bound, and equality proves optimality.

### Where the theorem is useful

The theorem is not only about students and projects. It appears whenever scarce, distinguishable resources must be assigned injectively: jobs to machines, rooms to events, representatives to sets, or variables to constraints in a structural model. The exact same proof works with abstract finite sets, independent of the story attached to their vertices.

The condition quantifies over exponentially many subsets, so it does not itself provide the most efficient computational test by brute force. Alternating-path algorithms can construct a maximum matching and, when full coverage fails, identify a violating set. The mathematical point comes first: Hall gives a complete characterization of when distinct representatives exist, and matching algorithms exploit that structure.

## Flows and Cuts: A Combinatorial Equality with Two Certificates

Imagine sending material through a directed network. Each edge has a capacity, the most it can carry in one unit of time. Material enters at a source and leaves at a sink. Every other vertex must pass along exactly as much as it receives. Our goal is to send as much as possible.

A simple upper bound is visible from a diagram. Draw a line dividing the vertices into two groups, with the source on one side and the sink on the other. Every unit of material that reaches the sink must cross that dividing line in the forward direction at least once. It may cross backward as well, but its net passage across the boundary equals the amount sent from source to sink. Thus total flow cannot exceed the sum of capacities of edges that cross the boundary from the source side to the sink side.

We call this division a cut. Each cut gives an upper bound. The surprising fact is that the strongest such bound is always attainable. The maximum flow value equals the minimum cut capacity. This is the max-flow min-cut theorem. Its proof is a constructive argument about paths, and it also explains what a certificate of optimality looks like.

### Define flow precisely

For every directed edge, assign a nonnegative real number no greater than its capacity. At a vertex other than the source and sink, add all incoming flow values and all outgoing flow values. They must agree. The flow value is the total flow out of the source minus any flow entering it, or equivalently the net inflow at the sink.

The conservation equations are important. Without them we could send material down one edge and claim it arrives at the sink even if a middle vertex simply accumulates it. A flow is a coherent collection of edge assignments, not a set of unrelated amounts.

Consider a network with source s, sink t, and intermediate vertices a and b. The capacities are three from s to a, two from s to b, two from a to t, three from b to t, and one from a to b. We can send two units along s to a to t, one along s to a to b to t, and two along s to b to t. All capacities are respected, conservation holds at a and b, and the total flow is five.

Can we do better? The cut containing only s has capacity three plus two, which is five. Since every flow is at most five and we constructed a flow of five, both are optimal. One feasible flow is a lower certificate; one cut is an upper certificate. Their equality settles the question.

### Why an apparently full path can still be improved

A naïve strategy repeatedly finds a source-to-sink path with unused capacity and sends more along it. The strategy can get stuck if it only looks at unused capacity in the original direction.

Take a smaller network. From s there are unit-capacity edges to u and v. From u there are unit-capacity edges to v and t. From v there is a unit-capacity edge to t. Suppose we first send one unit along s to u to v to t. Now s to u is full and v to t is full. Looking only at original forward edges, no new path to t seems possible. Yet a flow of two obviously exists: use s to u to t and s to v to t.

To correct the first choice, we must undo the unit sent from u to v. Undoing is not a mistake in the mathematics; it is part of how a search should work. We build a residual network that describes every possible change to the current flow.

For an original directed edge from u to v with capacity c and current flow f, there is residual capacity c minus f in the forward direction, because we may still increase the flow. There is also residual capacity f in the reverse direction, because we may cancel that much previously chosen flow. If the original network already contains edges in both directions, these residual contributions are combined appropriately.

In our small example the residual network contains the path s to v, then v to u by canceling the flow on u to v, then u to t. Pushing one unit along that residual path rearranges the first flow and raises the total to two. The reverse residual edge was essential.

### Proving the upper bound

Choose any set S of vertices containing the source but not the sink. Sum the flow-conservation equations over all the internal vertices in S. Every edge with both ends in S appears once as incoming and once as outgoing, so its contributions cancel. What remains is the net flow leaving S. That net value is the same as the flow value at the source.

But net flow leaving S is the forward flow leaving S minus any backward flow entering S. Backward flow is nonnegative, and forward flow on each crossing edge is at most its capacity. So the flow value is at most the capacity of the cut. This proves one direction of the theorem for every feasible flow and every cut.

### Constructing a matching cut

Now suppose a flow has no residual path from source to sink. Let S be the set of vertices reachable from the source in the residual network. The sink is not in S, by assumption. Consider any original edge going from S to its complement. If it had positive unused capacity, that would be a residual edge reaching outside S, which contradicts the definition. So every edge leaving S is saturated.

Consider any original edge that enters S from outside. If it carried positive flow, the residual network would have a reverse edge from S to the outside vertex, again contradicting reachability. So all edges entering S carry zero flow.

Consequently the net flow across this cut equals the sum of capacities of the forward edges. That sum is exactly the cut capacity. We have found a flow and a cut with equal values; neither can be improved. This proves max-flow min-cut as soon as we have a maximum flow or a sequence of augmentations that reaches a state with no augmenting path.

For integer capacities, the simple augmenting-path method can start from zero and push an integer amount each time. Every augmentation increases the integer flow value by at least one. Since the value is bounded by the capacity leaving the source, this process terminates and produces an integer maximum flow. The existence of an integral optimum follows without rounding any fractional solution.

For arbitrary irrational capacities, a careless choice of augmenting paths is not covered by this termination argument. Algorithms that choose paths more systematically, such as shortest residual paths, provide polynomial-time guarantees independent of the numeric sizes of integer capacities.

### Matching, cuts, and duality

The connection to Hall's theorem is concrete. To find a matching in a bipartite graph, make an edge of capacity one from the source to every left vertex, an edge of capacity one for every allowed left-to-right pair, and an edge of capacity one from every right vertex to the sink. An integral flow selects paths corresponding to disjoint matched pairs. If the left side has n vertices, Hall's condition is exactly what prevents a cut from having capacity smaller than n.

Flow and cut are also an instance of optimization duality. A feasible flow gives a value achieved; a cut gives a bound no flow can surpass. The theorem asserts that, in this network setting, the two sides meet. We do not need to rely on an optimizer's unexplained answer. We can verify the flow constraints, verify a cut, compare two numbers, and have a complete proof of optimality.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Graphs, Trees, and the Structure of Cycles

**Track:** Discrete Mathematics and Combinatorics. **Background:** finite sets, counting, mathematical induction. **Question:** how can a few local edge conditions determine the global structure of a graph?

#### Mathematical companion (not spoken)

Let \(G=(V,E)\) be a finite undirected simple graph with \(v=|V|\), \(e=|E|\), and \(c\) connected components.

**Equivalent tree properties (nonempty graphs):** connected and acyclic; unique simple path between any two vertices; connected with \(e=v-1\); acyclic with \(e=v-1\). A connected graph has a spanning tree. Any spanning forest has \(v-c\) edges.

**Handshake lemma:** \(\sum_{u\in V}\deg(u)=2e\); in particular, the number of odd-degree vertices is even.

**Cycle space:** Over \(\mathbb F_2\), the incidence map \(\partial:\mathbb F_2^E\to\mathbb F_2^V\) sends each edge to the sum of its endpoints. Then \(\ker\partial\) is the even-degree edge-subset space and
\[
\dim\ker\partial=e-v+c.
\]
A fundamental-cycle basis is obtained from a chosen spanning forest and one cycle per nonforest edge.

##### Exercises with answers

1. A connected graph has nine vertices and eight edges. Can it contain a cycle? **Answer:** no, it must be a tree.
2. Can a graph have exactly three odd-degree vertices? **Answer:** no, by the handshake lemma.
3. A graph has twelve vertices, fifteen edges, and two connected components. What is its cycle-space dimension? **Answer:** \(15-12+2=5\).
4. A triangle and an isolated vertex have four vertices and three edges. Why is the graph not a tree? **Answer:** it is disconnected and contains a cycle; edge count alone is insufficient.

##### Reading

MIT OpenCourseWare, [Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), chapters on graph theory and trees.

### Matchings and Hall's Marriage Theorem

**Track:** Discrete Mathematics and Combinatorics. **Background:** sets, neighborhoods, paths and bipartite graphs. **Question:** when can every request be assigned a different acceptable resource?

#### Mathematical companion (not spoken)

Let \(G=(L\sqcup R,E)\) be a finite bipartite graph and \(N(S)\subseteq R\) the neighborhood of \(S\subseteq L\). **Hall:** a matching saturating all of \(L\) exists iff
\[
|N(S)|\ge |S|\qquad\text{for every }S\subseteq L.
\]

**Proof by induction:** If a nonempty proper \(S\subset L\) satisfies equality, match within \(S\cup N(S)\), then match in the remainder; Hall holds there by applying Hall to \(S\cup T\). Otherwise every nonempty proper \(S\subset L\) has \(|N(S)|\ge|S|+1\); remove any edge \(xy\) and apply induction to the remaining graph.

**Augmenting path criterion:** a matching \(M\) is maximum iff it admits no \(M\)-augmenting path. In a bipartite graph, \(\nu(G)=\tau(G)\) (König's theorem), where \(\nu\) is the maximum matching size and \(\tau\) the minimum vertex-cover size.

##### Exercises with answers

1. Three students all accept precisely two projects. Can every student be assigned a different one? **Answer:** no; their joint neighborhood has size two, violating Hall.
2. If each of four students accepts three projects and each of those projects accepts at most three students, must Hall hold? **Answer:** yes, by double counting the edges leaving any subset \(S\): at least \(3|S|\) incidences and at most \(3|N(S)|\).
3. Why does flipping an augmenting path increase matching size by one? **Answer:** it has one more previously unmatched edge than matched edge, with all internal endpoints retaining one match.
4. What proves a matching of size six is maximum when a vertex cover of size six is given? **Answer:** every matching has size at most every vertex cover's size, so both are optimal.

##### Reading

MIT OpenCourseWare, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), matching and graph-theoretic counting; MIT, [6.854 course notes](https://courses.csail.mit.edu/6.854/18/Notes/), flow and matching relationships.

### Flows and Cuts: A Combinatorial Equality with Two Certificates

**Track:** Discrete Mathematics and Combinatorics. **Background:** directed graphs, paths, Hall's theorem, and elementary linear inequalities. **Question:** why does the maximum amount that can travel through a network equal the smallest capacity of a separating cut?

#### Mathematical companion (not spoken)

For a directed graph \(G=(V,E)\) with capacities \(c:E\to\mathbb R_{\ge0}\), a feasible flow \(f\) satisfies \(0\le f_e\le c_e\) and
\[
\sum_{e\in\delta^-(v)}f_e=\sum_{e\in\delta^+(v)}f_e \quad (v\notin\{s,t\}).
\]
Its value is \(|f|=\sum_{\delta^+(s)}f_e-\sum_{\delta^-(s)}f_e\). For any \(s\)-\(t\) cut \(S\),
\[
|f|=f(\delta^+(S))-f(\delta^-(S))\le c(\delta^+(S)).
\]

**Residual cut proof.** If \(t\) is not reachable from \(s\) in the residual graph, set \(S\) equal to the reachable vertices. All forward crossing edges are saturated and all backward crossing edges carry zero flow. Hence \(|f|=c(\delta^+(S))\). Weak duality then proves both optimalities.

**Integer capacities.** Starting from zero and augmenting along residual paths by bottleneck values preserves integrality. Since each step increases the integer value by at least one and the value is at most \(\sum_{e\in\delta^+(s)}c_e\), termination follows (this bound is numeric, not strongly polynomial in bit length).

**Worked example.** Capacities \(c(s,a)=3,c(s,b)=2,c(a,t)=2,c(b,t)=3,c(a,b)=1\). A flow of five sends two along \(s\to a\to t\), one along \(s\to a\to b\to t\), and two along \(s\to b\to t\). The cut \(S=\{s\}\) has capacity five.

##### Exercises with answers

1. Why can a reverse residual edge have positive capacity even when no original reverse edge exists? **Answer:** it represents cancellation of existing forward flow.
2. In the example, why is the cut \(\{s\}\) sufficient to prove optimality? **Answer:** it has capacity five, matching a feasible flow of value five.
3. Does integrality mean *every* maximum flow is integral? **No.** It guarantees that an integral maximum flow exists when capacities are integral.
4. Can augmenting paths with arbitrary real capacities be assumed to terminate simply because every step increases the flow? **No.** The integer-step termination argument no longer applies.

##### Reading

MIT 6.854, [Network Flows and Max-Flow Min-Cut](https://courses.csail.mit.edu/6.854/21/Scribe/s6-maxflow/s6-maxflow.html), flow decomposition, residual networks, and cut certificates; MIT 6.042J, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), matchings and graph theory.
