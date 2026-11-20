# The Cost of Disconnecting Two Vertices: Menger's Theorem

**Track:** Discrete Mathematics and Combinatorics  
**Lecture:** 052000  
**Preparation:** Graph paths, vertex degrees, basic network flow, and the distinction between an upper bound and a matching construction.  
**Companion:** Vertex-splitting reduction to integral max-flow/min-cut; worked connectivity certificate.

<!-- BEGIN SPOKEN LECTURE -->

Suppose two terminals in a communication network are connected by several routes. We would like the network to survive the failure of a small number of intermediate stations. It is tempting to answer by counting routes, but that can be misleading. One hundred listed routes may all pass through the same station. Removing that single station destroys them all. What provides resilience is not the number of descriptions of paths, but how much those paths overlap.

A precise way to measure this is to ask for paths from terminal s to terminal t that have no internal vertices in common. They may share their endpoints, of course; otherwise they could not all connect the same terminals. But no station strictly between s and t may lie on two of the selected paths.

There is a complementary question. What is the smallest number of intermediate vertices we must delete to disconnect s from t? Each collection of internally disjoint paths makes disconnection harder, because one removed vertex can intersect at most one of those paths. A theorem of Karl Menger says, with a necessary qualification, that the two quantities are exactly equal.

That is a remarkable kind of equality. It says a particular way of building resilience and a particular way of attacking resilience are perfectly matched. We will derive it carefully enough to understand what has been proved, where the hypotheses enter, and how a computer might return witnesses for both sides.

## Paths that do not compete for a station

Work with a finite simple undirected graph. Choose distinct vertices s and t that are *not adjacent*. Let p be the maximum number of s-to-t paths that are pairwise internally vertex-disjoint. Let k be the minimum size of a set of vertices, excluding s and t, whose deletion leaves no s-to-t path. The theorem is p equals k.

Why exclude the case where s and t have a direct edge? Because deleting internal vertices can never destroy that direct edge. There may be no separator of the stipulated kind at all. Versions of Menger's theorem accommodate adjacent terminals through slightly different formulations, but for this one we keep them nonadjacent. The restriction is mathematical content, not a footnote to be swept away.

Draw a simple example in your mind. From s one route goes through a and then reaches t. Another route goes from s through b, then c, then t. There are no other edges. The two routes are internally disjoint: one uses a, the other uses b and c. So p is at least two. The set containing a and b disconnects s from t, so k is at most two. Could one removed vertex suffice? No. Every one-vertex deletion misses at least one of the internally disjoint routes. Therefore p and k are both two.

This little proof uses the theorem's easy direction and a specific construction. Any separator must meet every s-to-t path. If we have p internally disjoint paths, one removed intermediate vertex can meet at most one of them. So every separator needs at least p vertices. This proves p is at most k.

The difficult direction is the converse. If every small set of vertices fails to disconnect s and t, can we necessarily find that many paths with disjoint internal vertices? It is not obvious. Paths can be tangled in ways that defeat a greedy selection. Choosing one seemingly attractive path may block several alternatives, although a different first choice would have allowed all of them.

To prove the converse, we will express the question as a flow problem. This is an example of reducing one mathematical problem to another while preserving the relevant witnesses.

## An ordinary flow limits edges, not vertices

In a flow network, arcs have capacities. A flow sends a quantity from a source to a sink while conserving flow at intermediate vertices and respecting capacities. The max-flow/min-cut theorem says the largest possible flow equals the smallest total capacity of an arc cut separating the source from the sink.

There is an obstruction to applying it immediately. If we give every graph edge capacity one, the resulting flow can use each edge at most once, but two units may still pass through the same intermediate vertex along different incident edges. That models *edge-disjoint* paths, not internally vertex-disjoint paths.

The solution is to split each internal vertex into two pieces. Make an entrance copy and an exit copy, connected by a special directed arc of capacity one. Every incoming original edge now leads to the entrance, and every outgoing original edge leaves the exit. Passing through the vertex requires crossing its one-unit gate. No more than one unit of flow can pass through that gate.

For an undirected original edge, include directed arcs in both directions between the appropriate exit and entrance copies. Give these travel arcs a large capacity, say n plus one, where n is the number of original vertices. The point is not that the physical network has such capacities. It is to arrange that the only inexpensive bottlenecks are the one-unit gates representing internal vertices. The terminals s and t receive no one-unit restriction. We may start at the exit copy of s and finish at the entrance copy of t.

Now every integer unit of source-to-sink flow follows a route through the split graph. Two units cannot traverse the same internal vertex gate because its capacity is one. After we discard any cycles and translate the routes back, we obtain internally vertex-disjoint paths in the original graph.

Conversely, every collection of internally vertex-disjoint paths supplies the same number of units of feasible integer flow: send one unit along each split path. We have connected the maximum number of disjoint paths with the maximum flow value.

Why can we insist on integer units rather than fractional pieces that somehow share a station? Our constructed capacities are integers. The augmenting-path proof of max-flow/min-cut begins with zero flow and increases flow by an integer bottleneck amount each time. Therefore an integral maximum flow exists. We can decompose an integral flow into integer path units and cycles; cycles are irrelevant to its source-to-sink value and may be discarded. There is no fractional cheating.

## Cuts in the split network

What does a minimum flow cut look like? The transformation must preserve not just the paths but also the vertices we can delete. Every choice of k intermediate vertices corresponds to cutting their k one-unit gate arcs. Any s-to-t route must pass through at least one of those gates, so removing them separates the source from the sink in the split graph. This shows that the minimum flow-cut value is at most k.

For the converse we need to know that an optimal split-network cut can be chosen using only the internal vertex gates. This is why we gave the travel arcs very large capacities. Because s and t are nonadjacent, deleting every neighbor of s disconnects them. That uses at most n minus two vertices. Therefore some all-gate cut has cost at most n minus two, strictly below our large travel-arc capacity of n plus one.

A minimum cut cannot contain any single large-capacity travel arc, since such a cut would already cost more than a known available cut. It therefore consists entirely of unit-capacity internal vertex gates. Read off their original vertex labels, and we obtain an s-to-t vertex separator whose size is exactly the cut capacity.

So the minimum cut capacity in the split network equals k, the smallest number of intermediate vertices needed to disconnect the original graph. The maximum flow value equals p, the largest collection of internally disjoint original paths. Max-flow/min-cut says those two numbers are equal. Hence p equals k. That is Menger's theorem in its vertex version for nonadjacent terminals.

Notice the structure of the argument. We did not assume what we wanted to prove about paths. We proved a correspondence between path packings and integer flows, then a correspondence between vertex separators and cheap cuts. The existing flow theorem supplied the equality between these two independently interpreted quantities.

## Why rerouting is essential

The network-flow reduction also explains why a greedy path-finding algorithm can fail. Suppose a first selected path winds through vertices that would best be used by two different paths. After choosing it, a naive search for another entirely unused path may get stuck. That does not show that only one path can exist.

A residual network remembers what we have already sent and, crucially, allows us to undo part of that decision. If a unit of flow traverses an arc, the residual network contains a reverse arc that can cancel that unit. An augmenting route may therefore weave forward on unused arcs and backward against earlier decisions. When the augmentation is completed, the entire flow is changed coherently, possibly replacing an earlier path with two better-arranged ones.

That is why a proof based on augmenting paths is stronger than a greedy count of paths. It certifies that when no augmenting route remains, a cut of equal capacity can be recovered from vertices reachable in the residual network. We obtain a witness of success and a witness that no further success is possible.

This dual-certificate perspective is useful far outside graph theory. A maximum matching and a minimum vertex cover in a bipartite graph obey a related equality. A maximum flow and minimum cut are equal. In each case, the lower-bound construction and the upper-bound obstruction meet at the same value. The equality makes optimality explainable rather than merely asserted.

## Vertex failures and edge failures are different

It is important not to blur the vertex version of Menger's theorem with its edge version. Two paths can be edge-disjoint even if they pass through the same intermediate vertex, provided they use different edges there. Such paths survive the loss of any one edge, but not necessarily the loss of that shared station.

The edge version says that the maximum number of edge-disjoint s-to-t paths equals the minimum number of edges whose removal separates s from t. It holds for any two distinct terminals in an undirected graph, including adjacent ones. Its standard flow reduction gives unit capacities to edges, with the minor care required for undirected arcs. The vertex version, by contrast, requires our split-vertex gates if we choose to derive it from flow.

Consider a bow-tie shape: two cycles touching at a single central vertex. There can be multiple edge-disjoint ways to travel toward or away from that central vertex, but every route between a vertex in one cycle and a vertex in the other passes through the shared center. The center is a one-vertex separator. Whatever the abundance of edges, the network is not robust against failure of that station.

The distinction is practical as well as mathematical. A transportation network may care about road closures, which resemble edge removals. A network of compute facilities may care about facility outages, which resemble vertex removals. If one model is substituted for the other, the resulting resilience claim can be wrong even though every calculation is internally correct.

## Two certificates in your hands

Return to our small example with edges s-a, a-t, s-b, b-c, and c-t. A complete answer to the optimization problem could consist of two paths, s-a-t and s-b-c-t, and the separator containing a and b. The two paths prove that no separator of size less than two works; the separator proves that no collection of more than two internally disjoint paths exists. We do not need to trust an algorithm's internal search to verify this final equality.

This gives us a valuable separation of responsibilities. A program can compute a candidate solution. A verifier can check, using the original graph, that its listed paths really connect s to t, have no repeated internal vertices, and are pairwise internally disjoint. It can also check that deleting the reported separator really destroys all s-to-t paths. If the two cardinalities agree, the theorem proves optimality.

This style of answer is especially attractive in formalization. The existence theorem, the method that computes a candidate, the decoder that reconstructs original vertex identifiers, and the verifier that checks a certificate are logically different pieces. They can be specified and proved in stages. We may trust the mathematical theorem while withholding judgment about a particular implementation's conversion and bookkeeping.

There is also a lesson about hypotheses. The assumption that the terminals are nonadjacent is exactly what allowed a finite internal-vertex separator to exist and made the all-gate cut cheaper than the large travel arcs. Drop the assumption without changing the formulation, and the proof fails for a concrete reason. Good theorems advertise the conditions under which their certificates make sense.

Menger's theorem turns a global question about many possible paths into a precise statement about a smallest obstruction. The equality is powerful, but the proof is equally instructive: choose the correct resources, construct an information-preserving reduction, use an integer optimization theorem, and decode both an optimal object and the obstruction that proves it cannot be improved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(G=(V,E)\) be a finite simple undirected graph and \(s,t\in V\) be distinct **nonadjacent** vertices. A family of \(s\)-\(t\) paths is *internally vertex-disjoint* when no vertex in \(V\setminus\{s,t\}\) belongs to more than one chosen path. A *vertex separator* \(X\subseteq V\setminus\{s,t\}\) meets every \(s\)-\(t\) path. The vertex version of Menger's theorem is

\[
\max\{|\mathcal P|:\mathcal P\text{ internally disjoint }s\text{--}t\text{ paths}\} = \min\{|X|:G-X\text{ has no }s\text{--}t\text{ path}\}.
\]

**Vertex-splitting flow reduction:** Replace each internal \(v\) with \(v_{in}\to v_{out}\) of capacity 1; put sufficiently large capacity \(M>|V|\) on arcs corresponding to graph edges, in both directions for undirected inputs; give terminals unrestricted transit and use source \(s_{out}\), sink \(t_{in}\). Since \(s,t\) are not adjacent, deleting all neighbors of \(s\) gives a separator of size at most \(|V|-2\), hence any min cut costs less than \(M\) and contains only unit vertex gates. Integral flow decomposes into internally disjoint paths. This reduces both extrema to integral max-flow/min-cut.

**Example:** \(V=\{s,a,b,c,t\}\), \(E=\{sa,at,sb,bc,ct\}\). Paths \(s-a-t\), \(s-b-c-t\) are internally disjoint; separator \(\{a,b\}\) has size 2. The pairing of two feasible certificates proves both optima equal 2.

**Exercises with solutions**

1. If two internally vertex-disjoint paths are exhibited, what is the minimum possible separator size? *Answer:* at least two.
2. Give a graph where two edge-disjoint paths share an internal vertex. *Answer:* two vertex-disjoint s-to-x paths followed by two edge-disjoint x-to-t paths, all meeting at x; any pair of concatenated routes shares x.
3. Explain why \(s\) adjacent to \(t\) breaks the stated vertex-cut definition. *Answer:* the length-one path persists after removing any set of other vertices.
4. In a vertex-split network, why is assigning capacity one to the original travel arcs not a substitute for the vertex gates? *Answer:* it bounds edge usage but permits different routes to traverse one internal vertex on distinct incident edges.
5. What evidence would let you independently certify an optimal value of three? *Answer:* three internally disjoint paths and a separator of cardinality three, both checked against the graph.

**Sources and attribution**

- Mikhail Lavrov, *Start Doing Graph Theory*, chapter on Menger's theorem: https://vertex.degree/connectivity/menger
- Reinhard Diestel, graph theory lectures on Menger's theorem, network flows, and dual certificates (author-hosted lecture series).
- Yann Disser, *Algorithmic Discrete Mathematics* (TU Darmstadt, 2024), vertex-splitting proof, Theorem 6.18: https://www2.mathematik.tu-darmstadt.de/~disser/pdfs/scripts/ADM_lecture_notes.pdf
- The concrete two-route example, certification discussion, and spoken teaching sequence are original synthesis.
