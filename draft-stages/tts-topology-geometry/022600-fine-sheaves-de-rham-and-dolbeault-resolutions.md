# 022600 — Fine Resolutions: Why de Rham and Dolbeault Compute Sheaf Cohomology

**Track:** Topology and Geometry. **Background:** local Poincaré lemma, sheaf cohomology, smooth and holomorphic forms. **Central question:** why can globally defined differential forms calculate an obstruction theory built from local sheaves?

<!-- BEGIN SPOKEN LECTURE -->

# Fine Resolutions: Why de Rham and Dolbeault Compute Sheaf Cohomology

There is a tension in the study of cohomology. Sheaf cohomology begins by examining all open sets and their compatibility, while differential-form cohomology begins with globally defined forms and a differential operator. Why should the two constructions ever agree?

The answer comes from a particular kind of resolution. Locally, the Poincaré lemma makes the de Rham complex exact after the constants. Globally, partitions of unity make the sheaves of smooth forms acyclic. Put those two facts together, and global differential forms calculate the sheaf cohomology of the constant real sheaf.

## Exactness is a local statement

Take a smooth manifold. The de Rham sequence begins with locally constant real functions, then smooth functions, then smooth one-forms, two-forms, and so on, connected by the exterior derivative.

The exterior derivative of a constant function is zero. Conversely, a smooth function whose exterior derivative vanishes is locally constant. More generally, the Poincaré lemma says that a closed differential k-form is locally exact for positive k: near any point, on a sufficiently small contractible coordinate neighborhood, it has a local primitive.

So as a sequence of sheaves, the constant real sheaf followed by the de Rham complex is exact. We have resolved a sheaf by sheaves of differential forms.

But taking global sections does not necessarily preserve exactness. That is the entire source of interesting de Rham cohomology. On a circle, a globally closed one-form may have no global primitive. Its local primitives exist, but their overlap differences cannot be globally corrected.

## Why smooth forms are easy to assemble

A smooth partition of unity is a collection of smooth functions adapted to an open cover whose sum is one. It lets us blend local constructions into global ones. Multiplying a differential form by a partition-of-unity function preserves smoothness, so the sheaf of smooth differential forms is fine.

On a paracompact smooth manifold, fine sheaves have vanishing higher cohomology. This is their key computational property. A resolution by such sheaves is acyclic for the global-section functor. Therefore the derived cohomology of the original constant sheaf can be computed simply by taking global sections of the de Rham complex and finding its cohomology.

That conclusion is the de Rham theorem in a sheaf-theoretic form. The first cohomology of the constant real sheaf is the quotient of globally closed one-forms by globally exact one-forms. On a circle, both viewpoints give one real generator.

## Holomorphic functions create a parallel story

On a complex manifold, consider the sheaf of holomorphic functions. A smooth complex-valued function is holomorphic exactly when its derivative in the antiholomorphic directions vanishes. This operator is written d bar, or partial bar.

The Dolbeault complex starts with smooth complex-valued functions, then smooth forms of type zero-one, zero-two, and so on, connected by partial bar. The local partial-bar Poincaré lemma makes this complex a resolution of the holomorphic-function sheaf.

The sheaves of smooth forms of type zero-q are fine, because multiplication by a smooth partition of unity preserves their type as forms and does not need to preserve holomorphicity. Thus the Dolbeault complex is another acyclic resolution.

The result is Dolbeault's theorem: the q-th sheaf cohomology of holomorphic functions is isomorphic to the q-th cohomology of the global partial-bar complex.

## Why holomorphic functions are different from smooth functions

It is tempting to ask why we did not simply use partitions of unity inside the sheaf of holomorphic functions itself. The reason is that a nonconstant smooth bump function is not holomorphic. On a connected complex manifold, a holomorphic function that vanishes on a nonempty open set vanishes everywhere. We cannot freely localize holomorphic data using compactly supported holomorphic cutoffs.

This failure is not an inconvenience to be swept aside; it is where higher holomorphic sheaf cohomology gets room to exist. The sheaf of holomorphic functions is generally not fine. The smooth forms in its Dolbeault resolution are fine, and they calculate the missing higher groups.

Take the projective line with the holomorphic line bundle O of minus two. We already calculated that the space of global holomorphic sections is zero and the first sheaf cohomology has dimension one. Dolbeault's theorem says that the corresponding first Dolbeault cohomology group, built from global zero-one forms with values in O of minus two, is one-dimensional. A nontrivial global obstruction survives even though every local partial-bar problem can be solved.

## Twisting by a bundle

For a holomorphic vector bundle E, replace functions by holomorphic sections of E and ordinary zero-q forms by zero-q forms with values in E. The partial-bar operator uses the holomorphic structure of E. Its cohomology computes sheaf cohomology of the holomorphic section sheaf.

The elliptic operator partial bar plus its formal adjoint is a Dolbeault-type Dirac operator. On a compact complex manifold, its index is the alternating sum of the dimensions of the holomorphic sheaf cohomology groups. On the projective line with O of k, that alternating sum is k plus one.

This identifies the exact point where sheaf theory enters elliptic index theory. We can count analytic kernel and cokernel spaces, compute sheaf cohomology with a cover, or apply a topological characteristic-class formula. Each method describes a different aspect of the same invariant.

The reusable strategy is this: find a locally exact resolution of the sheaf of interest, choose terms whose higher cohomology vanishes, and take global sections to compute the derived information. de Rham and Dolbeault are two especially important versions of that strategy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For smooth paracompact M, the Poincaré lemma gives the exact sheaf resolution

\[
0\to\underline{\mathbb R}_M\to\Omega_M^0\xrightarrow d\Omega_M^1\xrightarrow d\cdots.
\]

The sheaves Ω^k are fine, hence acyclic for Γ. Therefore `H^q(M;R_M)≈H^q(Ω^*(M),d)`.

For a complex manifold X and a holomorphic vector bundle E, the Dolbeault resolution is

\[
0\to\mathcal O(E)\to\mathcal A^{0,0}(E)
\xrightarrow{\bar\partial_E}\mathcal A^{0,1}(E)\to\cdots,
\]

where the sheaves of smooth (0,q)-forms with values in E are fine. Consequently `H^q(X, O(E))≈H_{\bar∂}^{0,q}(X,E)`. On compact complex X, the Dolbeault index is `Σ_q (-1)^q dim H^q(X,O(E))`, subject to the usual Fredholm/elliptic hypotheses.

### Exercises with answers

1. Why is the de Rham sequence exact as a sequence of sheaves? **Answer:** the local Poincaré lemma produces primitives on sufficiently small neighborhoods.
2. Why are smooth form sheaves fine? **Answer:** partitions of unity act on smooth forms and supply local-to-global endomorphisms.
3. Why does the holomorphic-function sheaf not admit the same partition-of-unity argument? **Answer:** smooth bump functions are generally not holomorphic.
4. What is `H_{\bar∂}^{0,1}(CP¹,O(-2))`? **Answer:** a complex vector space of dimension one.

### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), acyclic resolutions.
- [Dolbeault cohomology](https://en.wikipedia.org/wiki/Dolbeault_cohomology); [de Rham theorem](https://en.wikipedia.org/wiki/De_Rham_theorem).
