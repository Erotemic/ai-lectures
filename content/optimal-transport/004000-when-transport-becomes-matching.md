# When Transport Becomes Matching: Assignments, Flows, and Integrality

<!-- BEGIN SPOKEN LECTURE -->

Suppose every warehouse holds exactly one identical crate, every shop needs exactly one, and there are equally many warehouses and shops. Then there is a natural way to think about shipping: pair each warehouse with one shop, with no splitting at all. The problem sounds like assignment rather than transport. In fact, under these conditions, the continuous-looking transport linear program always has an optimal solution of exactly that matching form.

Why should a program that permits fractional shipments spontaneously yield an integral assignment? That is a structural theorem. It connects optimal transport to bipartite matchings and network flow, and helps explain why discrete optimization algorithms can solve a family of transport problems without enumerating arbitrary real-valued matrices.

The theorem does not say every feasible transport plan is an assignment. There are infinitely many fractional plans. It says that at least one minimum-cost plan can be chosen at an extreme point that is a permutation. To see why, we will first solve a small example, then examine the geometry of its feasible set and finally turn the problem into a flow network.

## Three people, three tasks

Imagine three researchers, Alice, Bob, and Cara, assigned to perform three experiments. Each researcher can do each experiment, but the costs differ. Alice's costs for experiments one, two, and three are four, one, and five. Bob's costs are two, three, and six. Cara's costs are seven, four, and two. The total project cost is the sum of the costs of the chosen assignments.

There are six possible one-to-one assignments. The cheapest sends Alice to experiment two, Bob to experiment one, and Cara to experiment three. The cost is one plus two plus two, or five. We can check all six permutations in this toy problem, but for a hundred researchers there are a hundred factorial permutations. This is no way to design an algorithm.

Consider the same problem as optimal transport. Give each researcher one third of the total supply and each experiment one third of the total demand. A coupling is now a three-by-three nonnegative matrix with every row sum and column sum equal to one third. Multiply that matrix by three. The result is a *doubly stochastic matrix*: all entries nonnegative, every row sum one, every column sum one.

A permutation matrix is one special doubly stochastic matrix. It has exactly one entry equal to one in each row and column, and zero elsewhere. Dividing by three gives a coupling in which every researcher sends their entire one-third unit to one experiment. But a doubly stochastic matrix can also average two assignments, splitting each researcher's mass between tasks.

The Birkhoff–von Neumann theorem says that every doubly stochastic matrix is a convex combination of permutation matrices. In other words, any fractional assignment table is an average of complete assignments, with nonnegative weights summing to one. This is a stronger statement than merely claiming that an optimal integral assignment exists.

Because the transport objective is linear, the cost of a convex average of assignments is the same convex average of their costs. Such an average cannot be strictly cheaper than all of the assignments it averages. Hence at least one permutation in that decomposition costs no more. The minimum over fractional tables equals the minimum over complete assignments. The linear relaxation has no integrality gap for this particular problem.

The scaling is worth keeping straight. Our original cost of the assignment is five. The normalized probability transport objective is one third of that, or five thirds, because every selected edge carries probability mass one third rather than a whole crate. Confusing assignment cost with probability-normalized cost leads to erroneous comparisons even when the selected pairing is right.

## Why convex averages of permutations appear

The Birkhoff theorem has a satisfying finite proof idea. Look at the graph formed by the positive entries of a doubly stochastic matrix: a row vertex is joined to a column vertex when the corresponding matrix entry is positive. Every row has total positive mass one; every column has total positive mass one. Hall's marriage theorem guarantees that this support graph contains a perfect matching. If a set of rows had fewer neighboring columns than rows, the mass leaving those rows would exceed the total mass those columns could accept. That contradicts the column-sum constraints.

Choose one perfect matching in this support. Let epsilon be the smallest matrix entry along its selected edges. Subtract epsilon from every selected edge. Each row and each column loses the same total epsilon. Divide the remaining matrix by one minus epsilon, provided epsilon is below one. We have produced another doubly stochastic matrix, and at least one positive entry has disappeared. Iterating gives a finite convex decomposition into permutation matrices. If epsilon is one, we already have a permutation.

That is the skeleton of the proof. It uses Hall's theorem to find a supported assignment and the mass constraints to peel it away. The coefficients from successive rescalings form a convex mixture. There is no need for a miraculous rounding rule; the combinatorial support and the linear equalities force the decomposition.

This fact is especially useful when studying relaxations. Many integer problems become easier after allowing fractional solutions but then suffer from an integrality gap: their fractional optimum looks too good to be realized. Balanced one-to-one assignment is different. The feasible polytope is the convex hull of integral permutation matrices. A minimum of a linear function over it is attained at a permutation. For nonlinear objectives, or when we add side constraints that destroy this structure, the conclusion can fail.

## Another optimality certificate

We can prove that our three-person assignment costs at least five without checking all six permutations. Assign a destination potential of two to experiment one, one to experiment two, and two to experiment three. Give all three researchers source potential zero. For every possible assignment, source potential plus destination potential is at most the corresponding cost. Check the smallest costs in each column: experiment one costs at least two, experiment two at least one, experiment three at least two. Those are exactly our destination potentials.

Any complete assignment uses each experiment once, so its cost is at least two plus one plus two, which is five. Our chosen assignment attains this bound. This is precisely the transport dual certificate specialized to unit masses and one-to-one assignment. An algorithm can provide primal edges and dual potentials as independently checkable evidence of correctness.

Some assignment algorithms, including the Hungarian method, maintain such potentials while they augment a partial matching. Edges where the inequality is an equality are called tight. The algorithm adjusts potentials and finds augmenting paths through appropriate tight edges until the matching becomes perfect. The correctness argument links feasibility, complementary slackness, and matching cardinality. We can study those invariants without committing to any one implementation.

## Unequal supplies lead to min-cost flow

Now remove the equal-crate assumption. A warehouse may hold one quarter of the goods and another may hold three quarters. A shop may require a different combination. There may not be any one-to-one assignment that satisfies the margins; splitting becomes essential. The natural algorithmic representation is a minimum-cost flow network.

Create a source node connected to each warehouse. The capacity on that edge is the warehouse's available supply. Connect each warehouse to each compatible shop, charging the route cost for every unit of flow. Connect each shop to a sink, with capacity equal to the shop's demand. Require a total flow equal to the common mass. If a route is forbidden, omit its edge rather than pretending a large finite penalty is literally infinity.

A feasible flow of full value corresponds to a feasible transport matrix. The warehouse-to-shop edge flows become the matrix entries. Conversely, any transport matrix induces such a network flow. The total cost is identical. This is a genuine equivalence, not just a resemblance between network pictures and tables.

The network can also use sparse permitted routes. If only a small fraction of all warehouse-shop pairs are available, we need not store a dense matrix. Feasibility is then no longer guaranteed merely by equal totals; incompatible access patterns can make the flow impossible. A max-flow or min-cut calculation can expose the obstruction.

For integral capacities and supplies, the minimum-cost flow problem admits an integral optimal flow. One way to understand this is total unimodularity of the directed network's incidence matrix. Another is that standard augmenting-path methods preserve integrality when starting from integral capacities and flows. If the masses are rational, we can sometimes scale all quantities to integers. With arbitrary real masses, integrality is not even a sensible universal requirement; the coupling genuinely has fractional entries.

An ordinary probability histogram has entries that sum to one. Calling such an object an integer assignment without specifying a common scaling is a category mistake. We must first decide whether a unit represents one discrete item or a fraction of an aggregate.

## How to choose the algorithmic viewpoint

The theoretical form of the problem helps us choose tools. If source and target are uniform collections of the same number of points and splitting offers no advantage, assignment algorithms are natural. If supplies and demands differ or capacities constrain routes, min-cost flow is natural. If both histograms are dense and approximate answers suffice, entropic matrix scaling may be attractive. If points lie on a line and costs are convex powers of distance, sorting or quantiles may solve the problem directly.

All these methods optimize over essentially the same idea: a coupling with prescribed margins. They differ in which additional structure they exploit and in what kind of numerical evidence they return. The mathematical distinction between the feasible set, objective, and algorithm keeps us from assuming that every fast method has the same hypotheses or proof obligations.

There is another conceptual connection here. A matching is not merely a way of pairing vertices. It can be a certificate that a linear relaxation has an integral optimum. The matching polytope and the transport polytope are related because their constraints are conservation equations. When such constraints have the right combinatorial form, the fractional and discrete worlds align. When they do not, approximation and integrality gaps become central topics in combinatorial optimization.

Our three-person example now has three explanations of its optimum. Direct enumeration gives five. Birkhoff's theorem guarantees that allowing fractions cannot produce a cheaper true solution. A dual potential vector gives a lower bound of five without enumeration. For a larger instance, a matching or flow algorithm can search efficiently, while its dual certificate lets another program verify the reported answer.

The same problem has become combinatorics, convex geometry, and linear programming, depending on which part we choose to understand. That is one of optimal transport's strengths as a unifying subject. The mass-conservation equations give it an algorithmic structure, and the mathematical proof tells us when a continuous-looking answer really is a discrete assignment.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Uniform assignment.** Let \(a=b=(1/n)\mathbf1\). Then \(P\in\Pi(a,b)\) iff \(Q=nP\) is doubly stochastic. The Birkhoff–von Neumann theorem gives \(Q=\sum_k\lambda_k P_{\sigma_k}\) with \(\lambda_k\ge0\) and \(\sum_k\lambda_k=1\), where \(P_{\sigma_k}\) are permutation matrices. Hence
\[
\min_{P\in\Pi(a,b)}\langle C,P\rangle=\frac1n\min_{\sigma\in S_n}\sum_i C_{i,\sigma(i)}.
\]
For \(C=\left(\begin{smallmatrix}4&1&5\\2&3&6\\7&4&2\end{smallmatrix}\right)\), \(\sigma=(2,1,3)\) in one-based destination labels has assignment cost \(5\) and normalized OT cost \(5/3\). Dual source potentials \(u=(0,0,0)\) and destination potentials \(v=(2,1,2)\) certify this optimum.

**Min-cost flow reduction.** Supply nodes \(i\) receive capacity \(a_i\) from a super-source; shipment arcs \(i\to j\) have per-unit cost \(C_{ij}\) and capacity at least total mass; demand nodes \(j\) connect to sink with capacity \(b_j\). Full-value flow and transport plans are in bijection when all allowed routes are represented. Integral supplies/capacities yield integral optimal flows; rational data may be rescaled.

**Exercises with solutions.** (1) Why does minimizing a linear cost over the convex hull of permutation matrices attain a permutation optimum? *A convex combination's cost is an average and cannot beat every constituent.* (2) Why does every supported doubly stochastic matrix have a perfect matching? *Hall's condition follows by comparing row mass from any subset to the capacity of its neighboring columns.* (3) What changes if one route is absent? *Remove that arc; equal total supply and demand alone no longer ensure feasibility.*

### Reading

- Peyré and Cuturi, *Computational Optimal Transport* (2019), assignment and discrete methods: https://research.google/pubs/computational-optimal-transport/
- POT documentation, exact Earth Mover's Distance and network-flow formulations: https://pythonot.github.io/user_guide.html
- See `discrete-mathematics:005000` and `optimization-duality:003000` for prerequisites on bipartite matching and LP duality.
