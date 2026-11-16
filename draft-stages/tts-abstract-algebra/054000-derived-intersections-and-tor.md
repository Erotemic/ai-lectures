# 054000 — Derived Intersections: Where Hidden Multiplicity Lives

**Track:** Abstract Algebra. **Background:** tensor products, Tor, affine schemes, regular sequences, and cotangent complexes. **Central question:** what information is lost when two geometric pieces meet nontransversely?

<!-- BEGIN SPOKEN LECTURE -->

# Two lines can meet too much

Imagine two lines crossing in the plane. The intersection is a point, and the defining equations remove two independent directions. Now imagine intersecting a line with itself. As a set, the answer is still the line. But the two equations are not independent. If we count equations as constraints, we expected something of lower dimension. Where did the missing constraint go?

In ordinary algebraic geometry, an intersection of affine schemes is represented by a tensor product of coordinate rings. This faithfully constructs the ordinary fiber product. Yet an ordinary tensor product does not always preserve the homological information that tells us why the intersection has greater dimension than expected.

A derived tensor product retains that information. The purpose is not to replace the visible geometric intersection with an entirely different picture. It is to add the homological structure that the ordinary intersection forgot.

# A calculation with one equation

Let R be the polynomial ring in one variable t over a field k. A point at the origin corresponds to the quotient R modulo t, which is just k. Intersect that point with itself over the affine line. The ordinary tensor product of k with k over R is again k. It records a single reduced point.

Now resolve one copy of k by free R-modules. The resolution has two terms: a copy of R mapped to another copy of R by multiplication by t. Tensor this complex with the second copy of k. Multiplication by t becomes zero, because t acts as zero on k. So the resulting two-term complex has zero differential.

The homology in degree zero is k, just as for the ordinary intersection. But there is also k in homological degree one. That extra k is the first Tor group. It measures that both copies imposed the same equation. The equation was not independent the second time.

We can describe this as an excess-intersection direction. The visible point remains, but its derived structure records how it was produced. An ordinary point and the self-intersection of a point inside a line are not equivalent as derived intersections.

# Transversality is a vanishing condition

Now consider two different coordinate axes inside the affine plane. One is described by x equals zero, the other by y equals zero. Their coordinate rings are R modulo x and R modulo y, where R is the polynomial ring in x and y. When we resolve one quotient and tensor with the other, multiplication by x remains injective on the ring of the other axis. No positive Tor survives. The derived intersection is equivalent to the ordinary one.

That is the algebraic content of transversality in this example. The two constraints interact without redundancy. More generally, a pair of modules or algebras is Tor-independent over a base if their higher Tor groups vanish. Under suitable hypotheses, Tor-independence is what allows ordinary fiber products to behave as expected under base change.

Notice the difference between an ordinary intersection being nonempty and its having excess homology. Intersections can be nonempty and perfectly transverse. Tor is not a test for whether two sets meet; it tests the homological independence of the equations used to produce the meeting.

# The Koszul picture

With several defining equations, the Koszul complex offers a computational model. It combines the equations with exterior generators and a differential that inserts each equation. If the equations form a regular sequence, the Koszul complex resolves the quotient: positive homology vanishes. If they fail to be regular, higher Koszul homology can reveal the redundancy.

For example, take one equation t, then impose t again. The second constraint contributes no new ordinary restriction after the first quotient. The Koszul or derived-tensor calculation records the dependence in degree one. With more repeated or dependent constraints, several homological degrees can appear.

This is why derived intersection theory is useful in enumerative geometry. When we count solutions, the ordinary set of solutions may have positive-dimensional components where isolated answers were expected. A derived model can carry obstruction data that makes an expected-dimensional or virtual count possible, under additional hypotheses.

# A warning about multiplicity

We should not make the claim that the dimension of Tor alone gives the intersection multiplicity in every setting. Classical local intersection multiplicity is often expressed as an alternating sum of lengths of Tor groups. To use such a formula, we need conditions ensuring that the relevant lengths are finite and that we are in the appropriate regular local setting. The sign and the alternating sum both matter.

For two transverse axes, higher Tor vanishes, and the degree-zero tensor has length one: the local intersection number is one. For an isolated tangency between curves, the ordinary tensor may already have length greater than one. For self-intersections or other excess-dimensional situations, additional geometric machinery is needed. Derived homology gives the right raw information, but turning it into a number still requires a theory of integration or intersection classes.

# Why this matters beyond algebraic geometry

The same pattern occurs in algebra. Tensor product is right exact, not generally exact. Its derived functors, the Tor groups, quantify the failure of exactness. Derived intersections translate that algebraic phenomenon into geometry: a failure of independent constraints becomes nontrivial higher homology.

The central lesson is that a space is not always determined by the points it contains. It may matter how that space arose, especially when equations are repeated, redundant, or singular. A derived fiber product retains this construction data in an invariant form. The same viewpoint also applies to moduli problems: families of complexes can carry deformation directions, automorphisms, and higher obstructions invisible in an ordinary set of isomorphism classes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `R=k[t]`, consider the free resolution of `k=R/(t)`:
\[
0\longrightarrow R\xrightarrow{t}R\longrightarrow k\longrightarrow0.
\]
After tensoring over R with k, the differential becomes zero:
\[
k\otimes_R^{\mathbf L}k\simeq[k\xrightarrow{0}k].
\]
Thus `Tor^R_0(k,k)=k` and `Tor^R_1(k,k)=k`, with higher Tor zero. Ordinary `k\otimes_R k=k` keeps only degree zero.

For `R=k[x,y]`, `A=R/(x)`, `B=R/(y)`, the resolution `[R --x--> R]` tensored with B becomes `[k[x] --x--> k[x]]`, which has no positive homology because x is a nonzerodivisor. Hence `Tor_i^R(A,B)=0` for `i>0` and `A\otimes_R B=k`.

Under suitable finite-length conditions for finitely generated modules over a **regular local ring**, Serre's intersection multiplicity takes the form
\[
\chi(M,N)=\sum_{i\ge 0}(-1)^i\operatorname{length}_R\operatorname{Tor}_i^R(M,N).
\]
Do not apply this expression as a finite number when tensor products or Tor groups do not have finite length. A Koszul complex on a regular sequence is a free resolution of its quotient; for a nonregular sequence, positive Koszul homology need not vanish.

### Exercises with answers

1. Compute `Tor_1^{k[t]}(k[t]/(t),k[t]/(t))`. **Answer:** k, using the two-term resolution.
2. Why do two transverse coordinate axes have no positive Tor in the given model? **Answer:** x acts injectively on `R/(y)=k[x]`.
3. Is positive Tor required for an intersection to be nonempty? **Answer:** no; a transverse point has no positive Tor.
4. Why is `dim_k Tor_1` not in general an intersection multiplicity? **Answer:** proper definitions may require an alternating sum of finite lengths and suitable regularity/properness conditions.

### Reading and source notes

- [The Stacks Project, More on Algebra](https://stacks.math.columbia.edu/download/more-algebra.pdf), Tor, Koszul complexes and regular sequences.
- [The Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), multiplicities, excess intersection and intersection products.
- [Toën, Higher and Derived Stacks: A Global Overview](https://arxiv.org/abs/math/0604504), derived fiber products and intersection-theoretic motivation.
