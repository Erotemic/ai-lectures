# Greedy graph structure, extremal bounds, and coloring

<!-- BEGIN SPOKEN LECTURE -->

# Greedy graph structure, extremal bounds, and coloring

## Symmetry, greedy structure, and existence obstructions

### Matroids: Why Some Greedy Algorithms Are Exactly Right

Suppose every edge of a connected graph has a cost, and we want a spanning tree of minimum total cost. A standard algorithm sorts the edges by cost, then takes each cheap edge unless it would create a cycle. It never looks ahead to all possible trees. Yet it obtains an optimal solution.

Now consider choosing research projects under a limited budget, or selecting jobs that cannot overlap on a schedule. Always picking the highest immediate reward can fail badly. The difference is not simply that some problems are easy and others are hard. There is a precise combinatorial structure under which the greedy method is guaranteed to work: a matroid.

#### Independence without vectors

Linear algebra already provides one example of an independence system. Given a finite collection of vectors, some subsets are linearly independent. Every subset of an independent set is independent. And if two independent sets have different sizes, there is at least one vector in the larger one that can be added to the smaller while preserving independence.

Forests in a graph behave the same way. A subset of the edges of a forest is still acyclic. If two forests have different numbers of edges, an edge from the larger forest can be added to the smaller while keeping it acyclic. To see why, a forest with more edges has fewer connected components on the same vertex set. At least one edge of the larger forest must cross between two components of the smaller one. Add that edge and no cycle appears.

A matroid abstracts exactly these two properties. We start with a finite ground set and a family of feasible, or independent, subsets. The empty set is independent. Subsets of independent sets remain independent. Finally, if independent set A has fewer elements than independent set B, some element of B outside A can be adjoined to A while preserving independence. This last condition is the exchange, or augmentation, axiom.

Maximal independent sets are called bases. The exchange axiom implies that every basis has the same number of elements. If one maximal independent set were smaller than another, augmentation would add an element, contradicting maximality. This common size is the rank of the matroid.

For vectors, bases are vector-space bases chosen from the ground set. For graph edges, the bases of a connected graphic matroid are spanning trees. The shared abstraction explains why both settings support similar selection arguments.

#### Make the greedy decision

Assign a real weight to each element. Consider the task of finding a maximum-weight basis. Sort the elements from largest weight to smallest. Start with the empty set. Visit the elements in that order and accept an element whenever adding it preserves independence. At the end we have a basis, and the matroid theorem says its total weight is maximum among all bases.

Why? Compare the greedy basis with an optimal basis. Suppose they agree on the elements already selected and we come to a greedy choice e that is absent from the comparison basis. The matroid basis-exchange property permits us to replace some element of the comparison basis by e, keeping a basis. Because greedy visits elements in descending weight order, and because that comparison basis cannot already contain an eligible higher-weight replacement that greedy skipped, the replaced element can be chosen with weight no greater than e. The substitution does not reduce total weight. Repeating this argument turns an optimal basis into the greedy basis without decreasing its value. Thus the greedy basis is optimal.

For spanning trees with minimum costs, reverse the order: choose cheap edges and reject cycles. Any spanning tree has the same number of edges, and one may negate the costs to apply the maximum-weight basis theorem. This is the mathematical foundation of Kruskal's algorithm, not merely a clever implementation trick.

If we instead seek a maximum-weight independent set that is not required to be a basis, we must distinguish negative from nonnegative weights. With nonnegative weights an optimal independent set can be extended to a basis without reducing its weight, so the greedy basis is still suitable. With negative weights we should stop before accepting negative-weight elements, unless a full basis is explicitly required. The objective matters as much as the exchange axiom.

#### A small failure shows what is missing

Let the available elements be a, b, and c. Allow any subset of a and b, and also allow the singleton c, but do not allow mixing c with either of the others. Give a and b weight three each, and c weight five. A greedy algorithm takes c first and then cannot add anything. Its value is five. But taking a and b yields six.

This is not a matroid. The singleton containing c is independent, as is the pair containing a and b. Yet no member of the pair can augment the singleton. The exchange axiom fails, and so does greedy optimality. The example exposes the actual reason the theorem needs its hypothesis.

#### Rank and diminishing returns

For any subset X of the ground set, define its rank as the largest cardinality of an independent subset contained in X. In a vector matroid this is the dimension of the span of the vectors in X. In a graphic matroid it is the number of vertices minus the number of connected components in the subgraph formed by those edges, counting isolated vertices.

Rank is monotone: adding possible elements cannot decrease the maximum achievable independent size. It also obeys submodularity. The rank of A plus the rank of B is at least the rank of their union plus the rank of their intersection. One interpretation is diminishing returns. An element that adds new rank when little is selected cannot become more valuable in rank when we have already selected more elements.

Submodularity appears well beyond matroids, in coverage problems, information theory, and combinatorial optimization. But a general submodular objective is not the same thing as a matroid rank function, and greedy algorithms for arbitrary submodular objectives may offer only approximation guarantees. The exact optimum for weighted matroid bases relies on the stronger exchange structure.

#### Several families, one language

In a uniform matroid, any subset of at most k elements is independent. Greedy simply takes the k largest weights when a basis is required. In a partition matroid, elements are divided into categories with a capacity for each category; independence means staying within all capacities. In a vector matroid, independence is ordinary linear independence. And in a graphic matroid, independence means having no cycles.

These examples arise from different domains, yet satisfy the same axioms. Their common feature is the ability to exchange parts of feasible solutions without losing feasibility. That is why a local sorting procedure can be globally correct.

The practical lesson is to ask a structural question before trusting a greedy rule: does the feasibility system satisfy augmentation? If so, matroid theory gives an exact theorem. If not, the same greedy algorithm may be only a heuristic, and a three-element counterexample may be enough to prove it.

### Extremal Graph Theory: How Many Edges Avoid a Clique?

A graph may have thousands of edges and still be missing a particular structure. If we forbid triangles, how many edges can we retain? If we forbid four vertices all connected to each other, can we keep more? There is a precise answer, and it is a model of extremal combinatorics: determine the largest or smallest possible quantity subject to a structural prohibition.

The simplest version has an elegant solution. A triangle-free graph on n vertices has at most the integer part of n squared divided by four edges. The bound is achieved by dividing the vertices into two groups as evenly as possible and connecting every vertex in one group to every vertex in the other. No triangle is possible, because every step along an edge changes groups, while a triangle would require an odd number of such changes and return to the starting group.

Why is a balanced bipartite graph optimal, and what happens when we forbid larger complete subgraphs?

#### Mantel's theorem from degree counting

Let m be the number of edges, and let each vertex have a degree equal to its number of neighbors. Choose any edge joining u and v. If u and v shared a neighbor, those three vertices would form a triangle. Because triangles are forbidden, the neighbors of u and the neighbors of v are disjoint sets. Their degrees therefore add to at most n.

Sum that inequality over all m edges. On the left, each vertex of degree d contributes d once for each of its d incident edges. Hence the left side is the sum of the squares of all the vertex degrees. We obtain: sum of squared degrees is at most n times m.

Now use the Cauchy–Schwarz inequality. The sum of squared degrees is at least the square of the sum of degrees divided by n. But the sum of degrees is twice m. Combining the two bounds gives four times m squared divided by n at most n times m. For a nonempty graph, cancel m and conclude that four m is at most n squared.

So the number of edges is at most n squared divided by four. Since it is an integer, we take the integer part. A complete bipartite graph with two parts as equal as possible has exactly that many edges, so the bound is sharp. This is Mantel's theorem.

The argument is worth remembering because it extracts a global extremal bound from a local obstruction. Every edge says that its endpoints cannot have a common neighbor; degree counting turns that local statement into a numerical inequality governing the whole graph.

#### Beyond triangles

Now forbid a clique on r plus one vertices: a set of r plus one vertices with every possible edge between them. The natural construction has r groups. Connect all pairs of vertices in different groups and no pairs within a group. Any clique uses at most one vertex from each group, so no clique can have r plus one vertices.

To maximize edges, balance the group sizes. If one group has at least two more vertices than another, move one vertex from the larger group to the smaller group. The number of cross-group edges increases. Therefore optimal group sizes differ by at most one. The resulting graph is the balanced complete r-partite graph, commonly called the Turán graph.

Turán's theorem says this construction is not merely one good answer. It has as many edges as any graph with no clique on r plus one vertices. In particular, the maximum is approximately one minus one over r, multiplied by n squared over two, with an exact correction determined by the remainder when n is divided by r.

For example, take seven vertices and forbid a complete graph on four vertices. We use three groups of sizes three, two, and two. Between the first and second groups there are six edges, between the first and third another six, and between the two smaller groups four. That makes sixteen edges. No four-clique occurs, and Turán's theorem says no other seven-vertex graph without a four-clique has more than sixteen edges.

#### An inductive proof of the general bound

There is a particularly instructive proof that avoids complicated rearrangements of arbitrary graphs. Fix r and suppose we have an edge-maximal graph on n vertices with no clique of size r plus one. Edge-maximal means that adding any missing edge creates a forbidden clique. We can restrict attention to such graphs because adding permissible edges can only increase the number of edges.

When n is at least r, such a graph contains a clique on r vertices. If there were a missing edge, the new forbidden clique produced by adding it would contain an r-clique already present. And if there were no missing edge, the graph is complete; because it forbids a clique of size r plus one, the case with n at least r must have n equal to r.

Choose an r-clique. Any vertex outside it can be connected to at most r minus one vertices inside. Otherwise that outside vertex and the chosen clique would make a forbidden clique of size r plus one. Thus the edges meeting our clique number at most r choose two, plus r minus one times n minus r.

The graph remaining after deleting the chosen r vertices is still free of the forbidden clique. By induction, its edge count cannot exceed that of the Turán graph on n minus r vertices. Put the bounds together. The result is exactly the number of edges in the balanced r-partite graph on n vertices: to grow that graph by r vertices, add one vertex to each part, thereby creating an r-clique among the newcomers and at most r minus one connections from each old vertex to them.

This matches the construction and proves the sharp bound. The proof works in blocks of r vertices and uses the forbidden clique to control how many new cross edges a block can contribute. It also explains why the extremal shape is multipartite, even though the argument does not need to classify every case of equality.

#### What the theorem does and does not say

A graph is clique-free here when it contains no forbidden clique as a subgraph, not merely when it contains none as an induced subgraph. Forbidding induced patterns is a different problem. Also, a graph with no four-clique may contain many triangles; it need not be triangle-free.

Turán's theorem identifies a sharp edge threshold for forcing a complete subgraph. Many other extremal questions ask what happens when the forbidden graph is a cycle, a complete bipartite graph, or a more complicated configuration. The answers can differ dramatically, and the optimizers need not be multipartite.

The deeper method is to put two tasks side by side. First construct a dense object without the forbidden pattern. Then prove no denser object is possible. When the construction and the upper bound agree, we have an exact extremal theorem rather than an approximation or an isolated example.

## Graph Coloring, Chromatic Polynomials, and Planarity

Suppose several tasks must be assigned to time slots, and two tasks connected by an edge are forbidden from occupying the same slot. Or suppose neighboring regions on a map must have different colors. Both problems ask for a proper vertex coloring of a graph: a label on every vertex so that adjacent vertices receive different labels.

The smallest number of colors that permits a proper coloring is the chromatic number. But there is a richer counting question. For each positive integer k, how many proper colorings exist when the colors are distinguished and drawn from a palette of k colors? The answer is a polynomial in k, despite the fact that colorings look like a combinatorial search problem.

### Begin with a tree

Take a tree with n vertices. Choose a root. It has k possible colors. Every other vertex has exactly one parent. Once its parent is colored, it may use any of the remaining k minus one colors. Walking outward from the root, each choice is independent of earlier nonparent choices because a tree has no cycles.

So the number of proper colorings is k times k minus one raised to the n minus one. Notice that the formula also tells us the chromatic number: any nontrivial tree is two-colorable, but not one-colorable.

For a complete graph on n vertices, every pair must have different colors, so the count is k times k minus one times k minus two and so on, with n factors. At the opposite extreme, a graph with no edges has k to the n colorings. These formulas are simple enough to verify by direct choices; the interesting part is how to handle graphs assembled from more complicated pieces.

### Deletion and contraction

Choose an edge e connecting two distinct vertices. Delete that edge. Now the endpoints are allowed to have the same color. Of the colorings of the deleted-edge graph, some assign different colors to the endpoints; those are exactly the proper colorings of the original graph. The remaining colorings assign the same color to the endpoints. If we identify the endpoints, those remaining colorings become colorings of a contracted graph.

Thus the chromatic polynomial of the original graph equals that of the graph with the edge deleted minus that of the graph with the edge contracted. Parallel edges do not change proper-coloring counts, and a loop makes proper coloring impossible. These conventions make the recurrence work cleanly.

Repeated deletion and contraction eventually reaches graphs we can count directly. The recurrence proves by induction on the number of edges that every finite loopless graph has a chromatic polynomial. It also explains some of its coefficient structure: the leading term is k to the number of vertices, and the next coefficient is minus the number of edges for a simple graph.

### Cycles are where the complication starts

For a cycle with n vertices, the chromatic polynomial is k minus one to the n, plus negative one to the n times k minus one. The extra signed term comes from the requirement that the final vertex and the first receive different colors. Unlike a tree, there is a closed consistency condition at the end.

For a triangle, the formula becomes k times k minus one times k minus two, as expected for a complete graph on three vertices. For a four-cycle and two colors, the formula gives two proper colorings, corresponding to the two alternating assignments. An odd cycle cannot be colored with two colors, because alternating along the cycle returns to the start demanding the opposite of the color already assigned.

The chromatic number therefore detects a cycle property: a graph is bipartite exactly when it contains no odd cycle. This is a structural characterization, not just a counting trick.

### Why planarity places a bound on edges

A planar graph can be drawn in the plane without edge crossings, apart from common endpoints. In a connected plane drawing, Euler's formula states that the number of vertices minus edges plus faces equals two. The outer face counts as one of the faces.

If the planar graph is simple and has at least three vertices, every face boundary has length at least three, provided we count boundary-edge incidences with multiplicity. Summing face boundary lengths counts every edge twice. Therefore three times the number of faces is at most twice the number of edges. Substitute this bound into Euler's formula, and obtain the familiar inequality: the number of edges is at most three times the number of vertices minus six.

This inequality fails for graphs with loops or sufficiently many parallel edges, which is why the hypotheses matter. For simple planar graphs it has an immediate implication: the average degree is strictly less than six. So some vertex has degree at most five.

### A coloring theorem from that inequality

Take any finite simple planar graph. Remove a vertex of degree at most five, color the smaller graph recursively using six colors, and then put the vertex back. At most five colors are used by its neighbors, leaving one of the six colors available for the vertex. This proves that every simple planar graph is six-colorable.

The argument is short because it uses only Euler's formula and induction. Stronger results exist: the five-color theorem can be proved by a more delicate recoloring argument; the four-color theorem required substantial computer-assisted proof work. We should not mistake the easy six-color induction for a proof of four-colorability. It establishes a weaker statement with a clear mechanism.

### Chromatic polynomials and planar structure

Planarity is a property of embedding; the chromatic polynomial is a graph invariant independent of a particular drawing. Their connection has fascinated mathematicians because constraints on cycles and faces influence coloring behavior. In a planar graph, a dual graph may turn questions about colorings into questions about flows, although the precise polynomial relationships require hypotheses about connectivity and the treatment of bridges and loops.

There is also a computational warning. The existence of a polynomial formula in the number of colors does not make evaluating that polynomial easy on arbitrary graphs. Deletion-contraction branches over combinatorially many subgraphs in the worst case. A neat algebraic expression and an efficient algorithm are different achievements.

The themes now meet: trees are easy because choices propagate without closing constraints; cycles introduce consistency; deletion-contraction converts graph constraints into an algebraic recurrence; and planar embeddings place global numerical restrictions on the graph itself. Coloring is not merely the assignment of labels. It is a window into what local restrictions force globally.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Symmetry, greedy structure, and existence obstructions

### Symmetry, greedy structure, and existence obstructions

#### Companions, sources, and study material (not spoken)

##### Matroids: Why Some Greedy Algorithms Are Exactly Right

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, linear independence, and basic optimization. **Central question:** what common structure makes locally best choices globally optimal?

###### Mathematical companion (not spoken)

A finite **matroid** is \(M=(E,\mathcal I)\) where \(\varnothing\in\mathcal I\), \(A\subseteq B\in\mathcal I\implies A\in\mathcal I\), and
\[
A,B\in\mathcal I,\ |A|<|B|\implies\exists b\in B\setminus A:\ A\cup\{b\}\in\mathcal I.
\]
All inclusion-maximal independent sets are bases and have equal cardinality. The **basis exchange property**: if \(B,C\) are bases and \(e\in B\setminus C\), then some \(f\in C\setminus B\) makes \((B\setminus\{e\})\cup\{f\}\) a basis.

For \(w:E\to\mathbb R\), the maximum-weight **basis** can be obtained by greedily accepting elements in nonincreasing weight order when independent. For a minimum spanning tree, process edges in nondecreasing cost order. Maximizing weights over arbitrary independent sets permits skipping negatives; requiring a basis does not.

\[
r(X)=\max\{|I|:I\subseteq X,I\in\mathcal I\},\qquad
r(A)+r(B)\ge r(A\cup B)+r(A\cap B).
\]
For a graph with fixed vertex set \(V\), the graphic matroid rank of an edge subset \(F\) is \(|V|-c(V,F)\), where \(c\) counts connected components including isolated vertices.

**Failure case:** \(E=\{a,b,c\}\), \(\mathcal I=\{\varnothing,\{a\},\{b\},\{c\},\{a,b\}\}\). Weights \(3,3,5\) give greedy value \(5\) but optimum value \(6\); augmentation from \(\{c\}\) toward \(\{a,b\}\) fails.

##### Exercises with answers

1. What are the bases of a uniform matroid of rank two on four elements? **Answer:** all six two-element subsets.
2. What is the rank of a forest with five vertices and three connected components? **Answer:** two edges in any spanning forest, so rank two.
3. Do the bases of a connected graphic matroid all have the same size? **Yes:** \(|V|-1\).
4. Is arbitrary family of downward-closed feasible sets necessarily a matroid? **No:** augmentation can fail, as in the three-element example.

##### Reading and source notes

- James Oxley, [Matroid Theory](https://repository.lsu.edu/facultybooks/466/) (2nd edition, 2011): independence axioms, rank, and greedy optimization.

##### Extremal Graph Theory: How Many Edges Avoid a Clique?

**Track:** Discrete Mathematics and Combinatorics. **Background:** simple graphs, complete graphs, counting edges, and induction. **Central question:** how dense can a graph be without containing a forbidden pattern?

###### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Find the extremal edge count for triangle-free graphs of order nine. **Answer:** \(\lfloor81/4\rfloor=20\).
2. What does forbidding \(K_4\) permit that forbidding \(K_3\) excludes? **Answer:** triangles.
3. Compute \(e(T_3(8))\). **Answer:** parts \(3,3,2\); edges \(9+6+6=21\).
4. If two parts of a complete multipartite graph have sizes \(a\) and \(b\) with \(a\ge b+2\), what happens when a vertex moves from the larger to the smaller? **Answer:** the edge count increases by \(a-b-1>0\).

##### Reading and source notes

- [Graph Theory course notes](https://cs.bme.hu/fcs/graphtheory.pdf), Section 4, Turán's theorem and its clique-removal induction proof.

### Graph Coloring, Chromatic Polynomials, and Planarity

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph terminology, counting polynomials, induction. **Central question:** how do coloring constraints interact with cycles, edge contraction, and embeddings in the plane?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. How many proper 3-colorings does a path on four vertices have? **Answer:** \(3\cdot2^3=24\).
2. Evaluate \(P_{C_4}(2)\). **Answer:** \((2-1)^4+(2-1)=2\).
3. Why is a triangle not bipartite? **Answer:** it is an odd cycle, whose alternating two-color assignment is inconsistent.
4. Give an edge bound for a simple planar graph with ten vertices. **Answer:** \(m\le24\).
5. Does the polynomial formula imply a polynomial-time exact evaluation algorithm for arbitrary input graphs? **No:** the formula counts values, but extracting them may still require exponential computation.

##### Reading and source notes

- Reinhard Diestel, [*Graph Theory*, sixth edition (2025), free chapter preview](https://diestel-graph-theory.com/basic.html?level=1), chapters on planar graphs and coloring.
- MIT OCW, [*Mathematics for Computer Science*](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), graph coloring and combinatorial counting.
