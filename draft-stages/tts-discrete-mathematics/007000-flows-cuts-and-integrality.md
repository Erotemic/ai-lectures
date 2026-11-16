# 007000 — Flows and Cuts: A Combinatorial Equality with Two Certificates

**Track:** Discrete Mathematics and Combinatorics. **Background:** directed graphs, paths, Hall's theorem, and elementary linear inequalities. **Question:** why does the maximum amount that can travel through a network equal the smallest capacity of a separating cut?

<!-- BEGIN SPOKEN LECTURE -->

# Flows and Cuts: A Combinatorial Equality with Two Certificates

Imagine sending material through a directed network. Each edge has a capacity, the most it can carry in one unit of time. Material enters at a source and leaves at a sink. Every other vertex must pass along exactly as much as it receives. Our goal is to send as much as possible.

A simple upper bound is visible from a diagram. Draw a line dividing the vertices into two groups, with the source on one side and the sink on the other. Every unit of material that reaches the sink must cross that dividing line in the forward direction at least once. It may cross backward as well, but its net passage across the boundary equals the amount sent from source to sink. Thus total flow cannot exceed the sum of capacities of edges that cross the boundary from the source side to the sink side.

We call this division a cut. Each cut gives an upper bound. The surprising fact is that the strongest such bound is always attainable. The maximum flow value equals the minimum cut capacity. This is the max-flow min-cut theorem. Its proof is a constructive argument about paths, and it also explains what a certificate of optimality looks like.

## Define flow precisely

For every directed edge, assign a nonnegative real number no greater than its capacity. At a vertex other than the source and sink, add all incoming flow values and all outgoing flow values. They must agree. The flow value is the total flow out of the source minus any flow entering it, or equivalently the net inflow at the sink.

The conservation equations are important. Without them we could send material down one edge and claim it arrives at the sink even if a middle vertex simply accumulates it. A flow is a coherent collection of edge assignments, not a set of unrelated amounts.

Consider a network with source s, sink t, and intermediate vertices a and b. The capacities are three from s to a, two from s to b, two from a to t, three from b to t, and one from a to b. We can send two units along s to a to t, one along s to a to b to t, and two along s to b to t. All capacities are respected, conservation holds at a and b, and the total flow is five.

Can we do better? The cut containing only s has capacity three plus two, which is five. Since every flow is at most five and we constructed a flow of five, both are optimal. One feasible flow is a lower certificate; one cut is an upper certificate. Their equality settles the question.

## Why an apparently full path can still be improved

A naïve strategy repeatedly finds a source-to-sink path with unused capacity and sends more along it. The strategy can get stuck if it only looks at unused capacity in the original direction.

Take a smaller network. From s there are unit-capacity edges to u and v. From u there are unit-capacity edges to v and t. From v there is a unit-capacity edge to t. Suppose we first send one unit along s to u to v to t. Now s to u is full and v to t is full. Looking only at original forward edges, no new path to t seems possible. Yet a flow of two obviously exists: use s to u to t and s to v to t.

To correct the first choice, we must undo the unit sent from u to v. Undoing is not a mistake in the mathematics; it is part of how a search should work. We build a residual network that describes every possible change to the current flow.

For an original directed edge from u to v with capacity c and current flow f, there is residual capacity c minus f in the forward direction, because we may still increase the flow. There is also residual capacity f in the reverse direction, because we may cancel that much previously chosen flow. If the original network already contains edges in both directions, these residual contributions are combined appropriately.

In our small example the residual network contains the path s to v, then v to u by canceling the flow on u to v, then u to t. Pushing one unit along that residual path rearranges the first flow and raises the total to two. The reverse residual edge was essential.

## Proving the upper bound

Choose any set S of vertices containing the source but not the sink. Sum the flow-conservation equations over all the internal vertices in S. Every edge with both ends in S appears once as incoming and once as outgoing, so its contributions cancel. What remains is the net flow leaving S. That net value is the same as the flow value at the source.

But net flow leaving S is the forward flow leaving S minus any backward flow entering S. Backward flow is nonnegative, and forward flow on each crossing edge is at most its capacity. So the flow value is at most the capacity of the cut. This proves one direction of the theorem for every feasible flow and every cut.

## Constructing a matching cut

Now suppose a flow has no residual path from source to sink. Let S be the set of vertices reachable from the source in the residual network. The sink is not in S, by assumption. Consider any original edge going from S to its complement. If it had positive unused capacity, that would be a residual edge reaching outside S, which contradicts the definition. So every edge leaving S is saturated.

Consider any original edge that enters S from outside. If it carried positive flow, the residual network would have a reverse edge from S to the outside vertex, again contradicting reachability. So all edges entering S carry zero flow.

Consequently the net flow across this cut equals the sum of capacities of the forward edges. That sum is exactly the cut capacity. We have found a flow and a cut with equal values; neither can be improved. This proves max-flow min-cut as soon as we have a maximum flow or a sequence of augmentations that reaches a state with no augmenting path.

For integer capacities, the simple augmenting-path method can start from zero and push an integer amount each time. Every augmentation increases the integer flow value by at least one. Since the value is bounded by the capacity leaving the source, this process terminates and produces an integer maximum flow. The existence of an integral optimum follows without rounding any fractional solution.

For arbitrary irrational capacities, a careless choice of augmenting paths is not covered by this termination argument. Algorithms that choose paths more systematically, such as shortest residual paths, provide polynomial-time guarantees independent of the numeric sizes of integer capacities.

## Matching, cuts, and duality

The connection to Hall's theorem is concrete. To find a matching in a bipartite graph, make an edge of capacity one from the source to every left vertex, an edge of capacity one for every allowed left-to-right pair, and an edge of capacity one from every right vertex to the sink. An integral flow selects paths corresponding to disjoint matched pairs. If the left side has n vertices, Hall's condition is exactly what prevents a cut from having capacity smaller than n.

Flow and cut are also an instance of optimization duality. A feasible flow gives a value achieved; a cut gives a bound no flow can surpass. The theorem asserts that, in this network setting, the two sides meet. We do not need to rely on an optimizer's unexplained answer. We can verify the flow constraints, verify a cut, compare two numbers, and have a complete proof of optimality.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Why can a reverse residual edge have positive capacity even when no original reverse edge exists? **Answer:** it represents cancellation of existing forward flow.
2. In the example, why is the cut \(\{s\}\) sufficient to prove optimality? **Answer:** it has capacity five, matching a feasible flow of value five.
3. Does integrality mean *every* maximum flow is integral? **No.** It guarantees that an integral maximum flow exists when capacities are integral.
4. Can augmenting paths with arbitrary real capacities be assumed to terminate simply because every step increases the flow? **No.** The integer-step termination argument no longer applies.

### Reading

MIT 6.854, [Network Flows and Max-Flow Min-Cut](https://courses.csail.mit.edu/6.854/21/Scribe/s6-maxflow/s6-maxflow.html), flow decomposition, residual networks, and cut certificates; MIT 6.042J, [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), matchings and graph theory.
