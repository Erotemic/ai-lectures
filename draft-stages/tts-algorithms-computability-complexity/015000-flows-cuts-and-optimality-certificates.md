# Flows, Cuts, and Why a Bottleneck Can Prove Optimality

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 015000  
**Preparation:** Directed graphs, conservation of quantities, and greedy counterexamples.  
**Companion:** Residual networks, max-flow/min-cut proof, matching, exercises.

<!-- BEGIN SPOKEN LECTURE -->

A city supplies water from a reservoir through a network of pipes. Each pipe has a capacity. Junctions cannot create water or destroy it, so whatever flows into an ordinary junction must flow out. How much water can the network deliver to a treatment plant? One might try to choose the widest-looking route and fill it. But a route that uses an important narrow pipe can block a better combination of several routes. We need a method that can change its mind, and a way to prove when it has found the maximum.

Model the pipes as directed edges with nonnegative capacities. Select a source, s, and a sink, t. A flow assigns a nonnegative number to each directed edge, not exceeding its capacity. At every vertex other than s and t, total incoming flow equals total outgoing flow. The value of a flow is its total net outflow from s, equal to its total net inflow into t. This conservation equation is part of the problem, not an optional engineering detail.

Let's begin with a capacity argument. Divide the vertices into two sets: one containing the source and the other containing the sink. Call this a cut. Every unit traveling from the source side to the sink side must cross its boundary. The capacity of the cut is the sum of the capacities of edges directed from the source side to the sink side. Reverse-directed edges do not add to this upper bound. By conservation, net flow across the cut equals the entire source-to-sink flow value. The net flow is at most the forward capacity. Thus every cut gives an upper bound on every possible feasible flow.

This sounds easy, but it is powerful: a proposed flow of value eight and a cut of capacity eight jointly certify optimality. The flow is a feasible lower bound on the maximum; the cut is a universal upper bound. Since they agree, there is no room for another algorithm to find a larger answer.

How can we find such a pair? Start with zero flow. An augmenting path is a route from source to sink along which additional flow can be sent. The obvious case is an original edge with unused capacity. Less obvious is that we may need to undo an earlier decision. Suppose we have sent one unit along an edge from u to v. We should be allowed to cancel part of that unit by traversing a reverse edge from v to u. This does not mean water physically flows backward through a one-way pipe. It is an accounting operation: a new assignment of flows retracts some previous assignment so a better route can use the capacity.

The residual network records both options. For an original edge from u to v, it has forward residual capacity equal to original capacity minus current flow. It also has reverse residual capacity equal to current flow. When parallel or opposite original edges exist, residual contributions must be handled without accidentally merging them incorrectly. An augmenting path follows positive residual capacities. Increase the flow along each forward use and decrease it along each reverse use by the smallest residual capacity on the path. The flow remains feasible, and its value increases by that amount.

Here is a small example where cancellation matters. Two people, Alice and Bob, can each take one job. Jobs X and Y each need one person. Alice can perform either job, and Bob can perform only X. A first search might assign Alice to X. Now Bob seems unable to take a job, while Y has no worker. In the residual network we can follow a route that gives X to Bob and frees Alice for Y. The route uses a reverse edge to cancel Alice's original assignment to X. The corrected matching has size two, though an irrevocable first choice produced only one.

The flow model is precise. Connect the source to each person with capacity one. Connect each person to each job they can do with capacity one. Connect each job to the sink with capacity one. Any integral flow corresponds to a matching: no person or job can participate more than once. Conversely, every matching produces an integral flow of equal value. Finding maximum bipartite matching is therefore an application of maximum flow, not merely an analogy.

Now for the main theorem. Suppose we repeatedly augment and eventually there is no source-to-sink path in the residual graph. Let S be the vertices still reachable from the source using positive residual edges. The sink is outside S. Look at an original edge going from S to its complement. If it had any unused forward capacity, the residual graph would let us reach its endpoint. So every such edge must be saturated. Look at an original edge going from the complement back into S. If it carried positive flow, its reverse residual edge would let us leave S, contradicting the definition of S. So every such reverse-crossing original edge must carry zero flow.

The net flow across the cut is therefore exactly the sum of capacities on forward-crossing edges. In other words, our feasible flow has value equal to this cut's capacity. Because every flow is bounded by every cut, we have constructed both an optimum and its certificate. This is the max-flow/min-cut theorem. The proof explains not just what is true, but how the algorithm knows when it is finished.

We should be careful about the word eventually. Ford-Fulkerson describes the rule 'find an augmenting path and augment.' For integer capacities, each augmentation increases an integer flow value by at least one, and the value is bounded by a finite integer cut capacity. So the process terminates. With arbitrary irrational capacities, some unfortunate choices of augmenting paths can fail to terminate. A particular implementation needs a path-selection rule and an accompanying complexity argument. The Edmonds-Karp version always chooses an augmenting path with the fewest residual edges, using breadth-first search. Its termination and polynomial bound do not rely on integer capacities, and a standard analysis gives order V times E squared operations in the graph-size parameters.

Even with integer capacities, a huge numerical capacity could make the bare 'one unit of progress' argument inefficient. Input bit length matters. An algorithm that performs a billion iterations because one input capacity is a billion is not automatically polynomial in the number of bits used to write that capacity. This is the same distinction between numerical magnitude and representation size that appears throughout computational complexity.

Another fact follows from the augmentation construction. If capacities are integers and we start from zero, every residual bottleneck and every change of flow can be chosen as an integer. So an integral maximum flow exists. This integrality property is why the matching reduction works: we do not need to interpret a half-person assigned to half a job. It does not say every feasible maximum flow is integral; fractional optimal flows can also exist. It says at least one integral optimum can be found.

Could the cut be chosen before solving the flow problem? Sometimes an obvious physical bottleneck gives a useful upper bound. But the minimum cut is generally a global property; a locally narrow edge need not limit total flow if parallel routes bypass it. The strength of the theorem is that an optimizing algorithm discovers a bottleneck whose capacity exactly matches the flow it has constructed.

There is a broader mathematical lesson here. Optimization is not only about searching for a good feasible answer. It is about finding an explanation of why nothing better can exist. A route or schedule proves feasibility. A cut, inequality, or dual variable can prove an upper bound. When the two meet, the problem is solved. Network flow is one of the clearest places to see a computational algorithm and a mathematical certificate emerge together.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

A feasible flow \(f\) satisfies \(0\le f(e)\le c(e)\) and conservation at \(v\notin\{s,t\}\). For a cut \(S\ni s\), \(t\notin S\), conservation gives
\[
|f|=\sum_{u\in S,v\notin S}f(u,v)-\sum_{u\notin S,v\in S}f(u,v)\le\sum_{u\in S,v\notin S}c(u,v)=c(S).
\]
Residual capacities are \(r(u,v)=c(u,v)-f(u,v)\) forward and \(r(v,u)=f(u,v)\) backward per original edge; opposing original arcs are treated separately or combined through explicit residual bookkeeping.

If there is no residual \(s\)-to-\(t\) path, define \(S\) as residual-reachable vertices. Forward edges across the cut are saturated and backward edges carry zero flow, yielding \(|f|=c(S)\). Together with weak duality \(|f|\le c(S')\) for every cut \(S'\), this proves the maximum-flow/minimum-cut equality.

**Matching reduction.** A bipartite graph \((L,R,E)\) becomes a capacitated directed network with \(s\to L\), \(L\to R\) for each bipartite edge, and \(R\to t\), all capacities one. Integral flow values equal matching cardinalities.

### Exercises with answers

1. **Cut.** Two edges cross from the source side to the sink side with capacities three and four; one edge with capacity ten points backward. What upper bound follows? **Answer:** Seven, not seventeen.
2. **Cancellation.** If Alice is assigned X and Bob can only do X, how can both Alice and Bob work when Y is available to Alice? **Answer:** Retract Alice-to-X by a residual reverse edge; assign Bob-to-X and Alice-to-Y.
3. **Stopping.** Why is 'no unsaturated forward path' insufficient? **Answer:** A route using reverse residual edges can rearrange previous flow and increase the value.
4. **Integer data.** Does integral capacity imply every maximum flow must use integer values? **Answer:** No; it guarantees existence of an integral optimum, not integrality of all optima.

### Reading and attribution

- Kleinberg and Tardos, *Algorithm Design*, Chapter 7; Kevin Wayne, *Network Flow I* and *Network Flow II*: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/.
- The people-and-jobs residual reassignment is an original explanatory example of a standard bipartite matching reduction.
