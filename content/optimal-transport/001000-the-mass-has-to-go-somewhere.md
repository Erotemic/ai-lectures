# The Mass Has to Go Somewhere: Couplings and the Transport Problem

<!-- BEGIN SPOKEN LECTURE -->

Suppose a town has two warehouses and two shops. Both warehouses have goods to send, and both shops have ordered goods to receive. A warehouse can be close to one shop and far from the other, so the cheapest shipment is not determined by the total amount of merchandise. It is determined by which shipments go where. We need a plan that satisfies both sides of a ledger: no warehouse sends more than it has, and no shop receives less than it ordered.

This is the finite transportation problem. It is also a remarkably concrete introduction to a geometry of probability distributions. We can replace goods by probability mass, replace travel costs by distances, and ask how expensive it is to transform one distribution into another. That question leads to optimal transport. It joins probability, linear programming, geometry, and algorithms without making any one of them disappear.

A probability distribution does not tell us which of its outcomes should correspond to the outcomes of another distribution. The distributions are the two ledgers. A *coupling* supplies the correspondence, possibly splitting one source mass among several destinations. This simple change in viewpoint is the beginning of the subject.

## From two ledgers to one table

Put the warehouses at positions zero and two on a road. The shops are at positions one and three. For simplicity, measure everything as fractions of a total load. Each warehouse has one half. The first shop wants one quarter; the second wants three quarters. Both totals are one, as they must be if all goods are to be shipped and none created or lost.

A transport plan is a table with two rows, one for each warehouse, and two columns, one for each shop. Its entry in row one, column two says what fraction of the total load travels from the warehouse at zero to the shop at three. Every entry is nonnegative. The first row must sum to one half, the second row to one half. The first column must sum to one quarter, and the second to three quarters.

Call that table pi. In probability language, the source distribution is mu, with mass one half at zero and one half at two. The destination distribution is nu, with mass one quarter at one and three quarters at three. Pi is a joint distribution on pairs of points. Its row totals are mu, and its column totals are nu. Those are its *marginals*. So a coupling of mu and nu is any joint distribution with those prescribed marginals.

It is worth dwelling on how much freedom this gives us. The source and destination distributions fix the totals, not the interior cells. We may send a fraction of warehouse zero's goods to either shop, as long as the second warehouse makes up the difference. Every allowed coupling describes the same two distributions but a potentially different collection of individual journeys.

Let t be the amount sent from warehouse zero to shop one. The other three entries are then forced. Warehouse zero sends one half minus t to shop three. Shop one must receive one quarter in total, so warehouse two sends one quarter minus t to shop one. Finally warehouse two sends one quarter plus t to shop three. Nonnegativity permits t between zero and one quarter. Every feasible plan is represented by exactly one t in this interval.

That little interval is the entire feasible polytope for this example. In a larger problem, the set of couplings is a polytope in many dimensions. It is cut out by linear equations for the margins and inequalities requiring each shipment to be nonnegative. There is no nonlinear optimization hiding in the finite formulation, provided the cost of sending each unit along each route is fixed.

## Put a price on the journeys

Let a unit shipment cost its travel distance. From warehouse zero to shop one costs one; from zero to three costs three. From warehouse two to one costs one, and from two to three also costs one. Read these four costs as a two-by-two matrix. The total cost of a plan is the sum over cells of amount shipped times cost per unit.

Substitute the four entries expressed in terms of t. The first shipment costs t. The second costs three times one half minus t. The third costs one quarter minus t, and the fourth costs one quarter plus t. Add them. The total is two minus two t. Larger t means lower cost, so the minimum occurs at t equal to one quarter. The optimal plan sends one quarter from zero to one, one quarter from zero to three, nothing from two to one, and one half from two to three. Its cost is one and a half.

We have solved a linear program by inspection. We did not guess a map or match individual warehouses to individual shops. We optimized over all couplings. A useful comparison is the *independent coupling*, which would choose a warehouse according to mu and a shop independently according to nu. Independence yields t equal to one eighth, and cost one and three quarters. It obeys the margins, but ignores the geometry. Feasibility and optimality are different questions.

Another comparison is sending each warehouse's entire supply to exactly one shop. That sounds like a natural map, but it is impossible here. Each warehouse carries mass one half. A map can send that whole half to a destination, but it cannot produce target masses one quarter and three quarters. The coupling can split one source atom. A deterministic map cannot.

This is the distinction between two formulations. In the classical Monge problem, we search for a map T that pushes the source distribution forward to the target. Every starting point has a single destination. In the Kantorovich problem, we search over joint measures with the prescribed marginals. Maps produce special couplings, but couplings need not be induced by maps. When a Monge map exists and is optimal, the two formulations can agree in value. In other situations, the Kantorovich formulation remains meaningful while the map formulation has no feasible solution.

## Why call this probability?

Imagine sampling a pair of random variables, X and Y, whose joint law is pi. The marginal law of X is mu and the marginal law of Y is nu. The transport cost is the expected value of the distance between X and Y. Choosing a coupling is therefore choosing how two random variables with fixed individual distributions are allowed to depend on one another.

If the variables are independent, we get the product law. If they are strongly coordinated, we may pair nearby values more often. Our optimization problem is: among all joint laws with the right marginals, which has the smallest expected cost? The choice of coupling does not change either marginal distribution. It changes only the relationship between them.

This is why coupling arguments also arise in probability without any discussion of trucks or warehouses. To compare two stochastic processes, we can sometimes construct them on one probability space so that they agree with high probability or remain close in expectation. A coupling is not a claim that the original variables were physically related. It is a mathematical construction whose marginal laws are the original distributions. Different couplings make different comparisons possible.

For arbitrary probability spaces the joint law becomes a measure on a product space rather than a finite matrix. The marginal conditions say that the measure of a set of source points, irrespective of destination, equals mu of that set, and similarly for nu. The objective becomes the integral of the cost function against the joint measure. These are the same two ledgers and the same cost calculation with sums replaced by integrals. New questions arise about existence, measurability, and integrability, but the organizing idea survives intact.

## What a cost function changes

So far we have charged one unit per unit of distance. Suppose instead we charge the square of the distance. Three units of travel now cost nine rather than three. The same source and destination are used, and the allowed couplings do not change. Only the objective changes.

For our positions zero and two, and one and three, the squared-cost matrix has entries one, nine, one, and one. The cost of the t-plan is five minus eight t. Again the minimum is at t equal to one quarter, but the minimum squared cost is three. It would be incorrect to compare this three directly with the previous one and a half as though they measured the same units. One is a mean squared travel distance, while the other is a mean travel distance. Later we will take a square root of the quadratic optimum to obtain the two-Wasserstein distance.

A cost need not even be a distance. We could assign separate prices to dangerous routes, forbid certain shipments by giving them infinite cost, or encode an asymmetric manufacturing constraint. The finite Kantorovich problem still makes sense for a general cost matrix, although its optimal value need not be a metric. That distinction becomes important whenever we use the phrase *transport distance*. The metric properties require additional structure, not just the existence of a shipment table.

Equal total mass is another structural requirement of this formulation. If warehouses have one unit but shops request only nine tenths, no nonnegative matrix can simultaneously have those row and column totals. A different problem, often called *unbalanced transport*, permits creation, destruction, or relaxed marginal constraints for a price. It is a valuable extension, not an invisible feature of ordinary balanced transport.

## The geometry behind the ledger

In a finite problem with m source points and n destination points, there are m times n candidate shipment quantities. The margin equations remove many degrees of freedom, and linear programming finds a minimum over the resulting polytope. Even before considering algorithms, this gives an existence argument: if the masses sum to the same finite total, the independent coupling is feasible; if costs are finite, the feasible polytope is nonempty and compact; a continuous linear objective attains a minimum.

Notice what this existence proof does not tell us. It does not explain why a particular plan is optimal, how to compute one efficiently, or how stable the answer is when we move a source point slightly. These require more mathematics. A dual problem will provide numerical certificates of optimality. Wasserstein geometry will study how these costs behave as distances between probability measures. Matching and flow algorithms will exploit the finite structure. Entropic regularization will trade exact sharpness for a smoother numerical problem.

The central object has already appeared, however. It is not a single trajectory from one distribution to another, and it is not a probability distribution considered in isolation. It is a *joint law with two fixed marginals*. Once that object is available, comparing distributions becomes an optimization problem with enough structure to prove something about the answer.

A warehouse ledger was enough to expose the entire architecture. Every proposed solution must first make the row and column totals agree. Its cost is then an expectation. To find the least costly coupling, we need not claim that each grain or each observation has one predetermined counterpart. We let the mathematics choose the joint relationship that is cheapest, subject to preserving both distributions exactly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For finite probability vectors \(a\in\mathbb R_+^m\), \(b\in\mathbb R_+^n\) with \(\sum_i a_i=\sum_jb_j=1\), and finite costs \(C\in\mathbb R^{m\times n}\), define
\[
\Pi(a,b)=\{P\in\mathbb R_+^{m\times n}:P\mathbf1_n=a,\ P^T\mathbf1_m=b\},\qquad
\mathrm{OT}_C(a,b)=\min_{P\in\Pi(a,b)}\langle C,P\rangle.
\]
The independent plan \(ab^T\) proves non-emptiness. The coupling polytope is compact, so for finite C the minimum is attained.

**Running example.** \(x=(0,2)\), \(y=(1,3)\), \(a=(1/2,1/2)\), \(b=(1/4,3/4)\). Feasible plans are
\[
P(t)=\begin{pmatrix}t&1/2-t\\1/4-t&1/4+t\end{pmatrix},\qquad 0\le t\le1/4.
\]
For \(C_{ij}=|x_i-y_j|\), \(C=\left(\begin{smallmatrix}1&3\\1&1\end{smallmatrix}\right)\), cost \(2-2t\), optimum \(P(1/4)\) of value \(3/2\). The independent plan \(P(1/8)\) costs \(7/4\). For squared cost \(C^{(2)}=\left(\begin{smallmatrix}1&9\\1&1\end{smallmatrix}\right)\), cost \(5-8t\), optimum \(3\).

A measurable Monge map \(T\) with \(T_\#\mu=\nu\) induces \((\mathrm{id},T)_\#\mu\in\Pi(\mu,\nu)\). Our two-atom example does not permit such a map because the source atom masses are halves while one target atom has mass a quarter.

**Exercises with solutions.** (1) Why is \(ab^T\) a coupling? *Each row sum is \(a_i\sum_j b_j=a_i\); similarly each column sum is \(b_j\).* (2) Change the long shipment's cost from three to five; how does the optimum change? *It still takes \(t=1/4\), since reducing the long shipment is even more valuable.* (3) What happens if \(\sum_i a_i\neq\sum_j b_j\)? *Summing all row and column constraints gives a contradiction, so the balanced feasible set is empty.*

### Reading

- Gabriel Peyré and Marco Cuturi, *Computational Optimal Transport* (2019): https://research.google/pubs/computational-optimal-transport/
- POT, *Python Optimal Transport*, user guide (balanced discrete transport): https://pythonot.github.io/user_guide.html

The warehouse positions, masses, and arithmetic are original instructional examples.
