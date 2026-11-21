# Prices That Prove a Shipment Optimal: Kantorovich Duality

<!-- BEGIN SPOKEN LECTURE -->

A transport plan is easy to criticize. Perhaps we can save money by sending less on a long route and more on a short one. Perhaps a whole cycle of shipments can be rearranged to save a fraction of a unit. With hundreds of source and destination points, testing every possible rearrangement is not a viable way to establish that our answer is best.

There is another kind of answer: a collection of prices which proves that *no* feasible plan can cost less than a stated number. If a plan meets that lower bound, we have settled optimality from two sides. The plan is a witness to what can be achieved; the prices are a witness to what cannot be beaten. This is linear-programming duality in transport clothing.

The price language is not merely a metaphor. We can assign a potential to each source and another to each destination so that their sum never exceeds the cost of connecting the two points. Those inequalities produce an aggregate lower bound. On the routes actually used by an optimal plan, the relevant inequality can be an equality. This relationship, called complementary slackness, connects the geometry of shipments to the geometry of supporting prices.

## The same two warehouses

We will reuse a small example. Warehouses at positions zero and two each have mass one half. Shops at positions one and three demand one quarter and three quarters. Distance is the per-unit cost. The four costs, by rows, are one and three for warehouse zero, and one and one for warehouse two.

We already found the cheapest plan. It sends one quarter from zero to one, one quarter from zero to three, nothing from two to one, and one half from two to three. Its total cost is one and a half. Our new task is not to search for it again. It is to prove that no other feasible shipment table is cheaper without enumerating all those tables.

Assign source potentials u-zero and u-two, and destination potentials v-one and v-three. Their values can be positive or negative. Require that each source potential plus each destination potential is no larger than the cost of that route. We have four inequalities, one per cell. For instance, u-zero plus v-three must not exceed three. U-two plus v-one must not exceed one.

Multiply each route inequality by the nonnegative amount of freight shipped on that route, then add the four inequalities. The sum of shipping costs is at least the sum over routes of shipped amount times source potential, plus shipped amount times destination potential. The first part collapses to each source potential times its available mass, because row sums are fixed. The second collapses to each destination potential times its demand, because column sums are fixed.

This lower bound is independent of the details of the plan. It depends only on the margins and the chosen potentials. That is the pivotal observation. Any potentials satisfying all route inequalities certify a lower bound for *every* admissible plan.

Choose u-zero equal to two and u-two equal to zero. Choose v-one equal to negative one and v-three equal to one. The four potential sums are, in row order, one, three, negative one, and one. Compare with the costs one, three, one, and one. Every potential sum is at most its shipping cost. Three of the constraints are tight. Only the unused route from two to one has slack, because its potential sum is negative one while its true cost is one.

Now calculate the aggregate bound. The source contribution is one half times two, plus one half times zero, giving one. The destination contribution is one quarter times negative one, plus three quarters times one, giving one half. The total lower bound is one and a half. Our feasible plan costs one and a half. So it is optimal. We have a short, independently checkable certificate.

The same proof shows a characteristic of optimal plans. A plan can put positive mass on an edge only when the corresponding dual inequality is tight, provided that plan and those potentials are both optimal. If it used the route from two to one, where the gap is two units per unit shipped, its cost would strictly exceed this particular certified lower bound. This condition does not say every tight route must be used. Some tight edges may receive no mass. It says positive flow cannot occupy a strictly slack edge at an optimal primal-dual pair.

## Where the dual problem comes from

Let us derive the dual instead of memorizing it. In a finite Kantorovich problem we minimize total cost subject to nonnegative shipments and exact row and column sums. Give each row equality its own multiplier u, and each column equality its own multiplier v. Form the Lagrangian by taking the shipping cost and adding the multipliers times the difference between desired and actual margins.

Regroup by shipment entry. The coefficient of the amount sent along route i to j becomes its cost minus u-i minus v-j. If any such coefficient is negative, we could drive the unconstrained, nonnegative shipment variable arbitrarily large and send the Lagrangian toward negative infinity. To get a finite lower bound when we minimize over shipment variables, every coefficient must be nonnegative. These are precisely the conditions that source potential plus destination potential not exceed route cost.

When those conditions hold, the infimum over nonnegative shipments is the constant consisting of source masses times u plus destination masses times v. To make that lower bound as strong as possible, we maximize it over feasible potentials. That is the dual linear program. We have moved from optimizing shipments to optimizing prices.

Weak duality is the easy inequality we have just proved: every feasible dual value is no greater than every feasible primal cost. Strong duality says that for a feasible finite linear program with a finite optimum, the best dual bound equals the best primal cost. In our finite balanced transport problem with finite costs, these requirements hold. The proof of strong duality is a theorem of linear programming, not an extra assumption that transport happened to satisfy in our example.

There is a useful freedom in the prices. Add any constant to all source potentials and subtract the same constant from all destination potentials. Every route sum remains unchanged. Since total source mass equals total destination mass, the aggregate objective also remains unchanged. So these potentials are not uniquely determined. Their differences and tightness pattern can carry more information than their absolute levels.

## A single potential in a metric space

Suppose source and destination points lie in the same metric space, and the route cost is the distance between them. For the one-Wasserstein problem there is a particularly elegant dual statement: the optimal transport cost equals the largest difference between expectations of a function that is one-Lipschitz under the two distributions. One-Lipschitz means that the function's value cannot change by more than the distance between two points.

Why should a Lipschitz function be a transport certificate? If f is one-Lipschitz, then f of x minus f of y is at most the distance from x to y. Choose the source potential as f of x and the destination potential as negative f of y. Their sum is automatically a valid lower bound for every route. Integrate against any coupling. The fixed marginals turn it into the expectation of f under mu minus its expectation under nu. The route costs bound that difference from above.

For our warehouses and shops on the real line, take f of position equal to negative position. This is one-Lipschitz. Its expected value under the source is negative one. Under the target, the expected position is one quarter times one plus three quarters times three, or two and a half, so the expected value of negative position is negative two and a half. Subtracting gives one and a half. The primal shipment has the same cost. Once again we have equality.

In general, the assertion that some one-Lipschitz function achieves the full one-Wasserstein optimum is called Kantorovich–Rubinstein duality, with the usual finite-first-moment hypotheses. The inequality from each Lipschitz function is immediate; equality is the substantive theorem. This is different from simply having two unrelated arrays of route potentials. The metric case permits a shared function on the underlying space.

This has a powerful consequence beyond freight. Suppose mu and nu describe two ways of sampling a quantity, and f is an observation whose output changes by no more than L times the input distance. Then the difference between the two expected observations is at most L times their one-Wasserstein distance. If we can find a cheap coupling, we control all such Lipschitz observations at once. If we can find a separating Lipschitz function, we prove that the distributions cannot be too close. Primal couplings and dual test functions squeeze the same quantity from opposite directions.

## Duality is not a solver by itself

It is tempting to treat an optimality certificate as the result of a particular algorithm. They are separate objects. A generic linear-programming solver may output a table of shipments and a vector of dual prices. A min-cost flow algorithm may produce residual costs that encode similar information. An exact proof assistant can check all inequalities and objective equalities without running the original optimization algorithm. For integer or rational data this certificate can be exact. With floating-point data, the inequalities and equalities generally need error analysis or rigorous bounds.

When we later use entropy to smooth transport, a different dual problem will arise. It will have exponential formulas instead of hard complementary-slackness constraints. But the basic proof method remains: define a feasible family, exhibit a lower bound, construct or approximate a plan that reaches it, and carefully distinguish mathematical equality from numerical tolerance.

The warehouse problem now has two quite different solutions on paper. One is a set of quantities moving along routes. The other is a collection of prices that makes every competing route accounting impossible to improve upon. A single equality between their objective values certifies the optimum. In optimization, that is often more informative than the plan alone.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The finite primal and dual pair is
\[
\min_{P\ge0}\sum_{ij}C_{ij}P_{ij}\quad\text{subject to }P\mathbf1=a,\ P^T\mathbf1=b;
\]
\[
\max_{u\in\mathbb R^m,v\in\mathbb R^n}\sum_i a_i u_i+\sum_jb_jv_j\quad\text{subject to }u_i+v_j\le C_{ij}.
\]
For any feasible P,u,v,
\[
\langle C,P\rangle-a^Tu-b^Tv=\sum_{ij}P_{ij}(C_{ij}-u_i-v_j)\ge0.
\]
At optimality, complementary slackness states \(P_{ij}>0\Rightarrow C_{ij}=u_i+v_j\), for an optimal primal-dual pair.

In the running example, \(a=(1/2,1/2)\), \(b=(1/4,3/4)\), \(C=\left(\begin{smallmatrix}1&3\\1&1\end{smallmatrix}\right)\),
\[
P^*=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},\quad
u=(2,0),\quad v=(-1,1).
\]
The primal objective is \(3/2\) and the dual objective is \(3/2\).

For a metric space with probability laws of finite first moment, the Kantorovich–Rubinstein formula is
\[
W_1(\mu,\nu)=\sup_{\operatorname{Lip}(f)\le1}\left(\int f\,d\mu-\int f\,d\nu\right).
\]
The example \(f(z)=-z\) yields \(3/2\), meeting the primal cost.

**Exercises with solutions.** (1) Verify the dual slack on the unused cell. *It is \(1-(0-1)=2\).* (2) Shift all source potentials up by five and destination potentials down by five. *All route sums and the objective remain unchanged because the masses on both sides agree.* (3) Suppose a feasible plan has cost \(1.6\) while a dual witness has value \(1.5\). *It is at most \(0.1\) above the optimum; equality is not certified.*

### Reading

- Peyré and Cuturi, *Computational Optimal Transport* (2019), discrete duality and transport potentials: https://research.google/pubs/computational-optimal-transport/
- POT documentation, linear and entropic transport objectives: https://pythonot.github.io/user_guide.html
- Cédric Villani, *Optimal Transport: Old and New*, Springer, 2009 (standard reference on Kantorovich duality).
