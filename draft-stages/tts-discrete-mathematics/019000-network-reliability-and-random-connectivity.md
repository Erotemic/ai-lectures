# 019000 — Network Reliability and Random Connectivity

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, independent random variables, inclusion–exclusion, concentration and thresholds. **Central question:** how many independent links does a network need before all its vertices are connected?

<!-- BEGIN SPOKEN LECTURE -->

# Network Reliability and Random Connectivity

A network can have hundreds of edges and still become useless when one critical connection fails. Another network with fewer edges can survive many failures because it has alternative routes. Counting edges is not the same as counting reliable paths. To measure reliability, we have to ask which combinations of surviving edges leave the network connected.

Start with three vertices arranged in a path. There are two required links. If each survives independently with probability p, both must survive, so the probability of connectivity is p squared. Now connect the endpoints, turning the path into a triangle. Any two of its three links suffice. The reliability becomes three times p squared minus two times p cubed. At a survival probability of one half, the path is connected only one quarter of the time; the triangle is connected one half of the time.

That difference is redundancy expressed as a polynomial. The triangle has three separate ways for exactly two edges to survive, and it also succeeds when all three survive. We are not adding probabilities of paths directly, because path events overlap. Correct counting handles the overlaps.

## The reliability polynomial

Fix an undirected graph with a given set of possible links. Suppose every link survives independently with the same probability p. For each subset of surviving edges, ask whether it connects all the vertices. Add the probability of that subset over all connected subsets. The result is the graph's all-terminal reliability polynomial.

The formula is finite and exact. It also becomes expensive for a large graph, because the number of edge subsets grows exponentially. Structural information can help. A bridge must survive in every connected realization, so its survival probability factors out. A cut is a collection of edges whose complete failure disconnects the graph. Small cuts often dominate failure probability when links are individually reliable.

There is a second, useful question. Instead of keeping a graph fixed and randomly deleting links, start with a set of n vertices and include each possible edge independently with probability p. This is the Erdős–Rényi random graph model. Now we ask how p should scale with n for the entire graph to be connected with high probability.

## Why one isolated vertex controls the threshold

Choose a particular vertex. It has n minus one possible neighbors. To be isolated, all those potential edges must be absent. The isolation probability is one minus p, raised to the n minus one power.

Multiply by n and we get the expected number of isolated vertices. If p is roughly a constant divided by n, the graph may already contain a giant connected component, but it still has many isolated vertices. The giant component is not the whole graph.

A different scale emerges when p is approximately log n divided by n. At that scale, the probability of one given vertex being isolated is roughly one over n. With n possible vertices, the expected number of isolated vertices is roughly one. The logarithm appears because the problem is not to connect a typical vertex, but to prevent even one vertex from being left behind.

Suppose p equals log n plus a fixed constant c, all divided by n. Then the number of isolated vertices approaches a Poisson distribution with mean the exponential of minus c. Consequently, the probability of having no isolated vertices approaches the exponential of minus the exponential of minus c.

The remarkable theorem is that, in this critical window, the probability the entire graph is connected approaches the same expression. Showing that there are no isolated vertices is not by itself sufficient: one must also rule out disconnected components of size two or more. The theorem says their remaining probability becomes negligible in this window.

## A transition, not a fixed safe percentage

If p is a fixed fraction smaller than log n divided by n, the graph is disconnected with probability tending to one as n grows. If p is a fixed fraction larger, it is connected with probability tending to one. This is a threshold phenomenon: the relevant scale shifts as the system grows.

It would be a mistake to say every real network has this threshold. The independent-edge model permits every possible connection and makes all those connections equally likely. Physical and communication networks have geography, correlated failures, designed redundancy, and constraints that are not present in this model.

Even within the model, reliability at a finite n is a probability, not a guarantee. A network with p above the asymptotic threshold can still disconnect. The sharp threshold tells us how the probability behaves for large n, not which specific sample must work.

## What this viewpoint teaches us

The exact reliability polynomial answers the question for a fixed graph. Random graph theory answers what happens for a growing family of graphs. Cut sets explain particular vulnerabilities. Isolated vertices explain the connectivity threshold. These are complementary viewpoints, and each exposes a different reason that redundancy matters.

The deepest lesson is that connecting almost everybody and connecting everybody are mathematically different tasks. The last isolated vertex can require a logarithmic increase in the number of links per node. A robust network must be designed and analyzed for the guarantee it actually needs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a fixed connected-or-not graph G=(V,E), m=|E|, with iid edge-survival probability p, its all-terminal reliability is
\[R_G(p)=\sum_{A\subseteq E\, :\, (V,A)\text{ connected}}p^{|A|}(1-p)^{m-|A|}.\]
For the path P_3, \(R_{P_3}(p)=p^2\). For the triangle C_3, \(R_{C_3}(p)=3p^2(1-p)+p^3=3p^2-2p^3\). At p=1/2 these are 1/4 and 1/2.

Let G(n,p) be the random graph with independent edges. If I_n is the number of isolated vertices, then
\[\mathbb E I_n=n(1-p)^{n-1}.\]
For \(p=(\log n+c)/n\) and fixed real c, \(\mathbb EI_n\to e^{-c}\). More strongly, \(I_n\Rightarrow\mathrm{Poisson}(e^{-c})\) and the **connectivity window theorem** gives
\[\Pr\big(G(n,p)\text{ connected}\big)\longrightarrow e^{-e^{-c}}.\]
In particular, for constant \(a<1\), p=a log(n)/n gives probability tending to zero; for constant a>1 it tends to one. The proof of the limiting formula also controls components of size two through n/2; convergence of the isolated-vertex count alone does not prove connectivity.

An elementary failure bound for a fixed graph uses cuts: for any specified cut C, all its edges failing has probability \((1-p)^{|C|}\), giving a **lower** bound on the probability of disconnection. A union bound over cuts gives an upper bound, but generally overcounts overlapping events.

### Exercises with answers

1. Evaluate triangle reliability at p=3/4. **Answer:** \(3(9/16)-2(27/64)=54/32-27/32=27/32\).
2. Why does every bridge factor p out of all-terminal reliability? **Answer:** every connected surviving-edge set must contain the bridge.
3. If p=log(n)/n, to what constant does the connectivity probability converge? **Answer:** \(e^{-1}\), since c=0.
4. Does the existence of one giant component imply connectivity? **Answer:** no; isolated vertices and other small components can remain.

### Reading and source notes

- [Richard Durrett, Erdős–Rényi Random Graphs, Chapter 1](https://services.math.duke.edu/~rtd/DoG/Chapter1.pdf), especially the connectivity window proof.
- [Ryan O'Donnell, Probability and Computing lecture notes](https://www.cs.cmu.edu/~odonnell/papers/probability-and-computing-lecture-notes.pdf), random graph threshold examples.
