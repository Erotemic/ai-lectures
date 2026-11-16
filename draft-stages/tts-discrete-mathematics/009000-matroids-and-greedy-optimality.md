# 009000 — Matroids: Why Some Greedy Algorithms Are Exactly Right

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, linear independence, and basic optimization. **Central question:** what common structure makes locally best choices globally optimal?

<!-- BEGIN SPOKEN LECTURE -->

# Matroids: Why Some Greedy Algorithms Are Exactly Right

Suppose every edge of a connected graph has a cost, and we want a spanning tree of minimum total cost. A standard algorithm sorts the edges by cost, then takes each cheap edge unless it would create a cycle. It never looks ahead to all possible trees. Yet it obtains an optimal solution.

Now consider choosing research projects under a limited budget, or selecting jobs that cannot overlap on a schedule. Always picking the highest immediate reward can fail badly. The difference is not simply that some problems are easy and others are hard. There is a precise combinatorial structure under which the greedy method is guaranteed to work: a matroid.

## Independence without vectors

Linear algebra already provides one example of an independence system. Given a finite collection of vectors, some subsets are linearly independent. Every subset of an independent set is independent. And if two independent sets have different sizes, there is at least one vector in the larger one that can be added to the smaller while preserving independence.

Forests in a graph behave the same way. A subset of the edges of a forest is still acyclic. If two forests have different numbers of edges, an edge from the larger forest can be added to the smaller while keeping it acyclic. To see why, a forest with more edges has fewer connected components on the same vertex set. At least one edge of the larger forest must cross between two components of the smaller one. Add that edge and no cycle appears.

A matroid abstracts exactly these two properties. We start with a finite ground set and a family of feasible, or independent, subsets. The empty set is independent. Subsets of independent sets remain independent. Finally, if independent set A has fewer elements than independent set B, some element of B outside A can be adjoined to A while preserving independence. This last condition is the exchange, or augmentation, axiom.

Maximal independent sets are called bases. The exchange axiom implies that every basis has the same number of elements. If one maximal independent set were smaller than another, augmentation would add an element, contradicting maximality. This common size is the rank of the matroid.

For vectors, bases are vector-space bases chosen from the ground set. For graph edges, the bases of a connected graphic matroid are spanning trees. The shared abstraction explains why both settings support similar selection arguments.

## Make the greedy decision

Assign a real weight to each element. Consider the task of finding a maximum-weight basis. Sort the elements from largest weight to smallest. Start with the empty set. Visit the elements in that order and accept an element whenever adding it preserves independence. At the end we have a basis, and the matroid theorem says its total weight is maximum among all bases.

Why? Compare the greedy basis with an optimal basis. Suppose they agree on the elements already selected and we come to a greedy choice e that is absent from the comparison basis. The matroid basis-exchange property permits us to replace some element of the comparison basis by e, keeping a basis. Because greedy visits elements in descending weight order, and because that comparison basis cannot already contain an eligible higher-weight replacement that greedy skipped, the replaced element can be chosen with weight no greater than e. The substitution does not reduce total weight. Repeating this argument turns an optimal basis into the greedy basis without decreasing its value. Thus the greedy basis is optimal.

For spanning trees with minimum costs, reverse the order: choose cheap edges and reject cycles. Any spanning tree has the same number of edges, and one may negate the costs to apply the maximum-weight basis theorem. This is the mathematical foundation of Kruskal's algorithm, not merely a clever implementation trick.

If we instead seek a maximum-weight independent set that is not required to be a basis, we must distinguish negative from nonnegative weights. With nonnegative weights an optimal independent set can be extended to a basis without reducing its weight, so the greedy basis is still suitable. With negative weights we should stop before accepting negative-weight elements, unless a full basis is explicitly required. The objective matters as much as the exchange axiom.

## A small failure shows what is missing

Let the available elements be a, b, and c. Allow any subset of a and b, and also allow the singleton c, but do not allow mixing c with either of the others. Give a and b weight three each, and c weight five. A greedy algorithm takes c first and then cannot add anything. Its value is five. But taking a and b yields six.

This is not a matroid. The singleton containing c is independent, as is the pair containing a and b. Yet no member of the pair can augment the singleton. The exchange axiom fails, and so does greedy optimality. The example exposes the actual reason the theorem needs its hypothesis.

## Rank and diminishing returns

For any subset X of the ground set, define its rank as the largest cardinality of an independent subset contained in X. In a vector matroid this is the dimension of the span of the vectors in X. In a graphic matroid it is the number of vertices minus the number of connected components in the subgraph formed by those edges, counting isolated vertices.

Rank is monotone: adding possible elements cannot decrease the maximum achievable independent size. It also obeys submodularity. The rank of A plus the rank of B is at least the rank of their union plus the rank of their intersection. One interpretation is diminishing returns. An element that adds new rank when little is selected cannot become more valuable in rank when we have already selected more elements.

Submodularity appears well beyond matroids, in coverage problems, information theory, and combinatorial optimization. But a general submodular objective is not the same thing as a matroid rank function, and greedy algorithms for arbitrary submodular objectives may offer only approximation guarantees. The exact optimum for weighted matroid bases relies on the stronger exchange structure.

## Several families, one language

In a uniform matroid, any subset of at most k elements is independent. Greedy simply takes the k largest weights when a basis is required. In a partition matroid, elements are divided into categories with a capacity for each category; independence means staying within all capacities. In a vector matroid, independence is ordinary linear independence. And in a graphic matroid, independence means having no cycles.

These examples arise from different domains, yet satisfy the same axioms. Their common feature is the ability to exchange parts of feasible solutions without losing feasibility. That is why a local sorting procedure can be globally correct.

The practical lesson is to ask a structural question before trusting a greedy rule: does the feasibility system satisfy augmentation? If so, matroid theory gives an exact theorem. If not, the same greedy algorithm may be only a heuristic, and a three-element counterexample may be enough to prove it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What are the bases of a uniform matroid of rank two on four elements? **Answer:** all six two-element subsets.
2. What is the rank of a forest with five vertices and three connected components? **Answer:** two edges in any spanning forest, so rank two.
3. Do the bases of a connected graphic matroid all have the same size? **Yes:** \(|V|-1\).
4. Is arbitrary family of downward-closed feasible sets necessarily a matroid? **No:** augmentation can fail, as in the three-element example.

### Reading and source notes

- James Oxley, [Matroid Theory](https://repository.lsu.edu/facultybooks/466/) (2nd edition, 2011): independence axioms, rank, and greedy optimization.
