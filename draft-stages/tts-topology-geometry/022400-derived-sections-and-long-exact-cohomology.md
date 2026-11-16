# 022400 — Why Sheaf Cohomology Is Derived: A Global Logarithm That Fails

**Track:** Topology and Geometry. **Background:** sheaves, exact sequences, Čech one-cocycles. **Central question:** why can a sequence be exact locally but fail to be exact after taking global sections?

<!-- BEGIN SPOKEN LECTURE -->

# Why Sheaf Cohomology Is Derived: A Global Logarithm That Fails

We often take a local fact and assume it remains true globally. Sheaf theory provides a precise warning against that assumption. A sequence of sheaves can be exact at every point, meaning every local problem has the expected solution, while the sequence of their global sections is no longer exact.

The higher cohomology groups of a sheaf measure that failure. They are called the right derived functors of global sections. We will motivate the terminology using a circle-valued function that has local logarithms but no global real logarithm.

## The exponential sequence

On a smooth manifold M, consider smooth real-valued functions. Exponentiating two pi i times such a function produces a smooth function into the unit circle. The kernel consists of integer-valued smooth functions. Since an integer-valued smooth function is locally constant, the kernel is the constant sheaf of integers.

Locally, every smooth circle-valued function has a smooth real argument. To see this, restrict to a small arc of the target circle where an angle can be chosen continuously. Thus the exponential map is surjective on stalks: every local circle-valued section has a local real lift.

We obtain a short exact sequence of sheaves: locally constant integers, then smooth real functions, then smooth circle-valued functions. The word exact is a local statement here.

## A global lift can fail

Take M itself to be a circle. Consider the function that sends each point to itself on the unit circle. It has winding number one. On small arcs we can choose real angles for it, but after going once around we would need the angle to increase by one full turn, not return to its original real value.

There is no globally defined smooth real function f whose exponential equals this identity circle map. If there were, it would lift a degree-one map through the real line, forcing a contradiction with winding number.

Thus a map of global sections that is locally surjective is not globally surjective. The missing information is topological. The exact sequence of sheaves makes the failure precise rather than leaving it as an isolated curiosity.

## How cohomology detects the obstruction

A short exact sequence of abelian sheaves produces a long exact sequence in sheaf cohomology. The first portion begins with global sections, then a connecting map into first cohomology of the kernel sheaf.

For the exponential sequence, a global circle-valued function is sent by the connecting map to an integer cohomology class. This class measures how its locally chosen real logarithms differ on overlaps. On the circle, the identity map goes to the generator of first integral cohomology.

If that class vanishes, the overlap differences can be corrected by changing the local real lifts, and a global real logarithm exists. If it does not vanish, no choice of local branches will fix the obstruction.

Notice how closely this resembles our previous Čech calculation with two overlapping arcs. There, one surviving difference between overlap constants measured a hole. Here the differences are integers because two real arguments of the same circle-valued function differ by a whole number of turns.

## Why the global-section functor needs repair

The functor taking a sheaf to its global sections is left exact: injectivity and exactness at the first stages survive. But surjectivity can fail. To measure its failure systematically, algebraic homological methods replace the sheaf by a resolution of better-behaved sheaves, for example injective sheaves, and take global sections of the resulting complex.

The zero-th cohomology of that complex is ordinary global sections. The higher groups record the information lost by demanding global sections too early. This is what it means to derive the global-section functor.

The language is abstract, but the problem it solves is concrete. We are not making a mysterious new kind of cohomology. We are applying the kernel-modulo-image construction to a resolution chosen so that local exactness can be studied globally without discarding obstruction data.

## Acyclic sheaves and useful resolutions

Some sheaves have no higher sheaf cohomology. On a paracompact smooth manifold, the sheaf of smooth real-valued functions is fine: partitions of unity allow local corrections to be assembled. Fine sheaves are acyclic for global sections under the standard hypotheses.

This makes the exponential sequence especially informative. Its connecting homomorphism associates to a circle-valued function a class in first integral cohomology, and that class accounts for the global logarithm obstruction. More generally, exact sequences and acyclic resolutions produce long exact sequences that allow one to compute unknown cohomology from known pieces.

Holomorphic functions behave differently from smooth functions. There are no arbitrary smooth partitions of unity that preserve holomorphicity. Consequently the sheaf of holomorphic functions can have nonzero higher cohomology, even on compact complex manifolds. That difference is exactly why complex geometry produces interesting indices and line-bundle cohomology.

## The general lesson

The phrase exact locally is not the phrase solvable globally. A sheaf sequence can be exact on every stalk and still fail after applying global sections. Derived sheaf cohomology preserves the lost information and places it into higher degrees.

The identity map of a circle is a complete foundational example: local logarithms exist, their discrepancies are integer-valued, and a winding number prevents their global merger. Whenever a later lecture invokes an obstruction class, a connecting map, or a derived functor, it is using this local-to-global pattern in a richer setting.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On a paracompact smooth M, the sheaf exponential sequence is exact on stalks:

\[
0\to\underline{\mathbb Z}_M\to\mathcal C_M^\infty(\mathbb R)
\xrightarrow{f\mapsto e^{2\pi if}}\mathcal C_M^\infty(S^1)\to0.
\]

The connecting morphism `δ:H^0(M,C∞(S¹))→H^1(M,Z)` sends a smooth circle-valued map to its homotopy/winding obstruction to a global logarithm. For M=S¹ and g(t)=e^{2πit}, δ[g] generates `H¹(S¹;Z)=Z`. Since `C∞_M(R)` is fine on paracompact smooth M, its higher sheaf cohomology vanishes, and the resulting long exact sequence describes such obstructions. In general `H^q(M,F)=R^qΓ(M,F)` for abelian sheaves F on a suitable site; this definition is not merely the Čech groups of one arbitrary cover.

### Exercises with answers

1. Why is the exponential map surjective as a sheaf map? **Answer:** every point has a neighborhood on which a smooth circle-valued function admits a smooth real argument.
2. Why does the identity map S¹→S¹ lack a global real logarithm? **Answer:** its winding number is one.
3. What does the connecting homomorphism measure? **Answer:** the class of the overlap differences between local logarithms.
4. Why is a short exact sheaf sequence not necessarily short exact on global sections? **Answer:** taking global sections preserves left exactness but can lose surjectivity.

### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), sheaf-cohomology comparisons.
- Ravi Vakil, [The Rising Sea](https://math.stanford.edu/~vakil/preprints.html), sheaves and homological algebra.
- [Sheaf cohomology](https://en.wikipedia.org/wiki/Sheaf_cohomology); [Exponential sheaf sequence](https://en.wikipedia.org/wiki/Exponential_sheaf_sequence).
