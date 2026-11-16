# 040000 — Sheaf Cohomology and the Failure of Global Sections to Be Exact

**Track:** Abstract Algebra. **Background:** sheaves and quasi-coherent modules, homological algebra, the projective line. **Central question:** how do we measure the failure of locally solvable equations to have global solutions?

<!-- BEGIN SPOKEN LECTURE -->

# Sheaf Cohomology and Global Sections

Sometimes every part of a mathematical problem has a solution, but the solutions refuse to agree. On each coordinate chart we can choose the function or section we want. On an overlap the choices differ. We try to correct them, only to find that the corrections themselves cannot be chosen consistently.

Sheaves organize such local data. Cohomology measures the obstructions to patching them into global data. In algebraic geometry it is also the mechanism behind the correction term in Riemann–Roch. To understand that connection, begin with a simple failure of exactness.

A short exact sequence of sheaves says, roughly, that one collection of local sections injects into another and that a third collection is obtained as a quotient. Surjectivity here is a local statement: a section in the quotient may have a lift on every sufficiently small neighborhood. But it may lack a single lift over the entire space.

Take global sections of that exact sequence. Injectivity survives. What fails is the expectation that the final global-section map is necessarily surjective. Local solutions exist, but the lifts disagree on overlaps. This is the precise gap that the first cohomology group records.

## An algebraic example on the projective line

The projective line has two standard affine coordinate charts. On either one, many calculations are easy: modules over the chart's coordinate ring replace abstract sheaf sections. The difficulty lies in compatibility across their overlap, where the coordinate is invertible.

Consider a line bundle whose transition function imposes a negative twist. On each affine chart it is locally just a free rank-one module. Yet the bundle called O of minus two has no nonzero global section. Its first cohomology group, however, is one-dimensional.

We can calculate that dimension explicitly using Laurent polynomials on the overlap. Sections on the two charts provide two families of Laurent terms. After we subtract terms arising from either chart, one Laurent monomial survives as an obstruction. The apparent freedom to work locally has left one globally irreducible mismatch.

This is not pathological behavior. It is the simplest concrete instance of derived global sections. The first cohomology group is not another collection of ordinary global sections; it is the quotient of overlap discrepancies by those discrepancies that can be repaired with local choices.

## From a functor to a sequence of obstructions

The global-section operation is called a left-exact functor. Homological algebra supplies its right derived functors, denoted H zero, H one, H two, and so on. H zero is the familiar space of global sections. Higher groups record increasingly structured failures of gluing.

A short exact sequence of sheaves produces a long exact sequence of cohomology groups. The connecting map takes a global section of the quotient, chooses local lifts, and turns their differences into a first-cohomology class. When that class vanishes, the local lifts can be adjusted to agree globally. When it does not vanish, the proposed global lift does not exist.

On an affine scheme, higher cohomology of quasi-coherent sheaves vanishes. This is one reason affine algebraic geometry behaves so well: the local-to-global obstruction disappears for that class of sheaves. But projective spaces are covered by affine charts without themselves being affine, and the overlap information can survive.

One must keep both qualifications. The vanishing statement concerns quasi-coherent sheaves, not arbitrary sheaves. And a cover by affine charts is not the same as the space itself being affine. The difference is exactly where the gluing problem lives.

## Recovering Riemann–Roch

On a smooth projective curve, cohomology of a line bundle only occurs in degrees zero and one. The difference between their dimensions is its Euler characteristic. For the line bundle associated to a divisor, Riemann–Roch computes that difference as the degree of the divisor plus one minus the genus.

So the dimension of permitted rational functions is not magically corrected by genus. The correction is the dimension of a genuine obstruction space. Serre duality then identifies that space with sections of a complementary line bundle related to differential forms.

This provides a coherent picture. Divisors specify local pole conditions. Line bundles encode how their local descriptions glue. Global sections are actual solutions. First cohomology measures why certain locally conceivable solutions fail to exist. Riemann–Roch balances the two dimensions.

The same derived-functor method extends far beyond curves. On a surface, second cohomology can contribute; on higher-dimensional schemes, still more groups appear. The curve formula is special precisely because there are only two terms to balance.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a sheaf F of O_X-modules, \(\Gamma(X,F)=H^0(X,F)\) is left exact. Its right derived functors are \(R^i\Gamma(X,F)=H^i(X,F)\). From \(0\to F'\to F\to F''\to0\) one obtains
\[0\to H^0(F')\to H^0(F)\to H^0(F'')\xrightarrow{\delta}H^1(F')\to H^1(F)\to\cdots.\]
The connecting homomorphism \(\delta\) measures the obstruction to gluing local lifts. For quasi-coherent F on \(\operatorname{Spec}R\), \(H^i(X,F)=0\) for \(i>0\). This does **not** hold for every sheaf and is not a claim that all spaces covered by affines are acyclic.

**Čech computation on P^1.** Write \(P^1_k=U_0\cup U_1\), with \(U_0\simeq\operatorname{Spec}k[t]\), \(U_1\simeq\operatorname{Spec}k[t^{-1}]\), and overlap \(\operatorname{Spec}k[t,t^{-1}]\). Taking suitable trivializations of O(n), the Čech complex computes
\[h^0(\mathbf P^1,\mathcal O(n))=\max(n+1,0),\quad h^1(\mathbf P^1,\mathcal O(n))=\max(-n-1,0).\]
For O(-2), the quotient of the Laurent overlap sections by both chart images is one-dimensional, represented (in a standard convention) by the class of \(t^{-1}\). For O(-1) both cohomology groups vanish.

**Explicit failure of right exactness:** the standard exact sequence
\[0\longrightarrow\mathcal O(-2)\longrightarrow\mathcal O(-1)^{\oplus2}\xrightarrow{[x\ y]}\mathcal O\longrightarrow0\]
is exact as sheaves on P^1. The map on global sections \(H^0(\mathcal O(-1)^{\oplus2})=0\to H^0(\mathcal O)=k\) is not surjective; its connecting map identifies k with \(H^1(\mathcal O(-2))\). On a smooth projective curve C, \(\chi(O_C(D))=h^0-h^1=\deg D+1-g\).

### Exercises with answers

1. What is \(h^1(P^1,O(-3))\)? **Answer:** 2.
2. Why can't local surjectivity of sheaves imply surjectivity on global sections? **Answer:** the local lifts may disagree on intersections; the obstruction is the connecting class in first cohomology.
3. Why is the analogous obstruction absent for quasi-coherent sheaves on an affine scheme? **Answer:** higher cohomology vanishes on affines for quasi-coherent sheaves.
4. Compute \(\chi(O_{P^1}(4))\). **Answer:** 5, with \(h^0=5\) and \(h^1=0\).

### Reading and source notes

- [Stacks Project, Cohomology of quasi-coherent sheaves](https://stacks.math.columbia.edu/tag/03OY), covering affine vanishing and Čech comparisons.
- [Stacks Project, Cohomology and projective twists](https://stacks.math.columbia.edu/tag/0D8P), exercises on O(n) over projective space.
- [Stacks Project, Riemann–Roch](https://stacks.math.columbia.edu/tag/0B5B), Euler characteristics of line bundles on curves.
