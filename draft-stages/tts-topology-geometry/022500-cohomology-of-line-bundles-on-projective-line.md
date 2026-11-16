# 022500 — Holomorphic Line Bundles on the Projective Line: Counting H-Zero and H-One

**Track:** Topology and Geometry. **Background:** sheaves, Čech cochains, projective coordinates, Laurent series. **Central question:** can we calculate an elliptic index by explicitly computing the sections and obstructions of a holomorphic line bundle?

<!-- BEGIN SPOKEN LECTURE -->

# Holomorphic Line Bundles on the Projective Line: Counting H-Zero and H-One

An index formula can seem distant from the objects it counts. For a Dolbeault operator on a complex curve, the index is the number of independent holomorphic sections minus the number of independent first-cohomology obstructions. We will calculate both numbers for every holomorphic line bundle O of k on the complex projective line, using only two coordinate charts and Laurent series.

This is a calculation that can be checked at each step. It also explains the k plus one in Riemann–Roch, including negative values of k.

## Two charts and one transition function

The complex projective line has a chart U zero where the first homogeneous coordinate is nonzero, with affine coordinate z equal to Z one divided by Z zero. It has another chart U infinity where the second homogeneous coordinate is nonzero, with coordinate w equal to Z zero divided by Z one. On the overlap, w equals one over z.

Both charts look like the complex plane, and their overlap looks like the punctured complex plane. The line bundle O of k is given by a transition factor z to the k between the two local trivializations, with a fixed convention for which chart's coefficient is being expressed in which frame.

A holomorphic global section consists of holomorphic functions f zero of z and f infinity of w that agree through this transition. In our convention, f zero of z equals z to the k times f infinity of one over z. We must find all pairs satisfying this identity.

## Positive k gives polynomials

Suppose k is a nonnegative integer. Expand f infinity as a power series near w equals zero. After replacing w by one over z and multiplying by z to the k, we obtain a Laurent series in z with powers k, k minus one, k minus two, and so on.

For the expression to extend holomorphically across z equals zero, all negative powers must cancel. Thus only the first k plus one coefficients may remain. The resulting f zero is a polynomial of degree at most k.

There are k plus one independent monomials: one, z, through z to the k. So the vector space of holomorphic global sections has dimension k plus one. For k equals zero, only constants remain. For k equals one, we get two independent linear sections. For k equals two, three quadratic sections.

If k is negative, the matching condition demands a holomorphic function at z equals zero represented by only negative powers. The only such function is zero. Thus there are no nonzero global holomorphic sections when k is negative.

## Where first cohomology appears

To compute H one, use the two-chart Čech complex. A one-cochain is a holomorphic function on the overlap, expressed in the U zero trivialization. Because the overlap is punctured complex plane, it has a Laurent series with positive and negative powers.

A coboundary is the difference between a holomorphic function on U zero and a transformed holomorphic function on U infinity. The first supplies every nonnegative power of z. The second supplies powers k, k minus one, k minus two, and so on.

Which Laurent powers cannot be removed by those two kinds of terms? They must be negative, because U zero handles all nonnegative powers. They must also be greater than k, because U infinity handles powers k and below.

When k is minus one or greater, there is no integer strictly between k and zero. Every one-cochain is a coboundary, so H one vanishes.

When k equals minus two, exactly one power survives: z to the minus one. Therefore H one has dimension one. When k equals minus three, two powers survive: z to the minus two and z to the minus one. In general, if k is at most minus two, H one has dimension minus k minus one.

This calculation is not just formal cancellation of finite Laurent polynomials. Holomorphic Laurent series converge on the overlap, and splitting them into the relevant parts supplies holomorphic representatives on the two charts. The cover is acyclic for these coherent holomorphic sheaves, by the Stein nature of its nonempty intersections and the appropriate vanishing theorem. Those facts justify using the Čech complex for sheaf cohomology.

## The index is always k plus one

Now subtract dimensions. For nonnegative k, H zero has dimension k plus one and H one vanishes, so the difference is k plus one.

For k equals minus one, both groups vanish, and the difference is zero, again k plus one. For k at most minus two, H zero vanishes while H one has dimension minus k minus one, so zero minus that number is k plus one.

The same formula holds for every integer k. The negative results are meaningful: the cokernel of the Dolbeault operator can have larger dimension than its kernel.

We can compare with the topological Riemann–Roch calculation. The Chern character of O of k contributes k times the positive generator of second cohomology. The Todd class of the projective line contributes one additional copy. Their product integrates to k plus one. We have verified that the topological integral counts exactly the same alternating dimensions as the explicit holomorphic Čech complex.

## Why the example belongs in several subjects

The calculation is simultaneously a demonstration of sheaf cohomology, complex analysis, line-bundle geometry, and elliptic index theory. The same line bundle is represented by a clutching function, by its first Chern number, by transition functions for holomorphic sections, and by a Dolbeault operator.

The power of the index theorem becomes clearer when the simple coordinates disappear. On an arbitrary compact complex manifold, we may not be able to write the global sections as elementary polynomials. But characteristic classes and a pushforward can still calculate their alternating total, provided the relevant hypotheses hold.

The essential bridge is now explicit: holomorphic sections are global compatible local functions; first sheaf cohomology measures overlap classes that cannot be corrected; their difference is the elliptic index. Riemann–Roch computes that difference from topological data.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On `CP¹`, use `U_0={Z_0≠0}`, `U_∞={Z_1≠0}`, `z=Z_1/Z_0`, `w=1/z`. Choose the transition convention `f_0(z)=z^k f_∞(1/z)` for O(k). Then

\[
h^0(\mathbb{CP}^1,\mathcal O(k))=\max(k+1,0),\qquad
h^1(\mathbb{CP}^1,\mathcal O(k))=\max(-k-1,0).
\]

The Čech one-cochains on the overlap are Laurent series modulo `f_0(z)-z^k f_∞(1/z)`. The obstruction exponents are integers `k<n<0`, giving `-k-1` surviving modes when k≤-2. These charts and all nonempty finite intersections are Stein, so Cartan's theorem B supplies cover acyclicity for coherent sheaves, and Čech equals derived cohomology here. The Dolbeault index is `χ(O(k))=h⁰-h¹=k+1`, equal to `∫_{CP¹}ch(O(k))Td(TCP¹)`.

### Exercises with answers

1. Calculate h-zero and h-one for O(2). **Answer:** 3 and 0.
2. Calculate them for O(-1). **Answer:** 0 and 0.
3. Calculate them for O(-4). **Answer:** 0 and 3; the surviving Laurent exponents are -3,-2,-1.
4. What is chi of O(-4)? **Answer:** -3, consistent with k+1.

### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), acyclic-cover comparison.
- Ravi Vakil, [The Rising Sea](https://math.stanford.edu/~vakil/preprints.html), line bundles and projective geometry.
- [Cohomology of line bundles on projective space](https://en.wikipedia.org/wiki/Line_bundle#Line_bundles_on_projective_space); [Riemann–Roch theorem](https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem).
