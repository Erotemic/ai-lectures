# 064000 — Stable Pairs and Donaldson–Thomas Theory: Curves as Sheaves

**Track:** Abstract Algebra. **Background:** coherent sheaves, Hilbert schemes, perfect obstruction theories, and virtual enumerative invariants. **Central question:** what should count as a curve when geometric families degenerate?

<!-- BEGIN SPOKEN LECTURE -->

# Counting curves that refuse to stay smooth

Imagine trying to count curves of a fixed degree in a three-dimensional algebraic variety. A naive plan is to list smooth embedded curves and divide by symmetries. But in a family, a smooth curve may degenerate into a singular curve, a union of components, or a scheme with embedded or infinitesimal structure. If we discard all those limits, our count can change when we vary the geometry slightly.

Modern enumerative geometry solves this not by pretending degenerations are simple, but by choosing a compact moduli problem that includes them in a controlled way. Donaldson–Thomas theory and stable-pair theory use sheaves to encode curves. Instead of just remembering the visible set of points, a sheaf remembers multiplicity and infinitesimal information.

Two kinds of objects will appear. An ideal sheaf records how a subscheme sits inside the ambient threefold. A stable pair is a map from the structure sheaf of the ambient space into a pure one-dimensional sheaf, with a zero-dimensional cokernel. Their moduli spaces are different, but their virtual counts are related through wall crossing.

# Why an ideal sheaf knows a subscheme

Let a closed subscheme Z sit inside a smooth projective threefold X. Its ideal sheaf contains the functions that vanish along Z. The quotient of all regular functions by that ideal is the structure sheaf of Z.

Take an ordinary line in projective three-space. It can be described by two independent linear equations, so its ideal sheaf is generated locally by those linear forms. As we vary the line, its ideal changes coherently. The family of all lines in projective three-space is a Grassmannian: each line corresponds to a two-dimensional vector subspace of a four-dimensional vector space. This family is four-dimensional, not a finite set of curves.

That example prevents a common mistake. An enumerative invariant does not say every possible curve problem should produce a finite ordinary count. Dimensions must match the insertions or the virtual degree. On a Calabi–Yau threefold, the virtual dimension for the standard ideal-sheaf Donaldson–Thomas problem is zero under its usual fixed numerical data. In projective three-space, with its different canonical bundle, the line family has positive dimension.

# Stable pairs separate a curve from its marked defects

A stable pair consists of a coherent sheaf F, pure of dimension one, together with a section from the structure sheaf of X to F. Purity means F has no nonzero subsheaf supported only at isolated points. The cokernel of the section is required to be zero-dimensional.

Intuitively the section generates F along the generic points of its one-dimensional support. It may fail to generate at finitely many points, and those defects are remembered. That is enough flexibility to compactify curve families without adding arbitrary isolated zero-dimensional subsheaves to F.

For the line L in projective three-space, take F to be the pushforward of its structure sheaf to X. Choose the section that sends the constant one to the constant one on L. Its cokernel is zero. Thus it is a stable pair. If we choose a sheaf twisted to allow an extra zero-dimensional quotient supported at points of the line, the pair can remember additional marked defect data.

These are sheaf-theoretic objects. They cannot, in general, be identified with smooth embedded curves or with maps from an abstract domain. The choice of moduli problem changes what the enumerative invariant means.

# Obstruction theory corrects dimension

Deformations of an ideal sheaf, or of the two-term complex associated with a stable pair, are governed by Ext groups. First-order deformations are tangent directions; higher Ext data supply obstructions to extending those directions. A perfect obstruction theory packages the resulting tangent-obstruction data into a virtual tangent complex.

The virtual fundamental class behaves as if the moduli space had the expected dimension, even when its actual components are larger or singular. On a projective Calabi–Yau threefold, the standard stable-pair theory yields degree-zero virtual classes for fixed curve class and Euler characteristic, so integrating one can produce a number. The number can carry signs and multiplicities imposed by the obstruction theory.

Calling it a count is useful as shorthand, but the precise mathematical object is a virtual integral. In special favorable cases, it agrees with an ordinary signed enumeration. In general, it is not obtained by listing geometric curves and adding one for each.

# Why two theories can encode related answers

An ideal-sheaf moduli problem naturally includes zero-dimensional pieces of subschemes along with curves. A stable-pair problem imposes the purity and section conditions described above. The two theories respond differently to embedded and isolated points. Their generating functions nevertheless satisfy correspondences, often expressed by separating a zero-dimensional Donaldson–Thomas contribution from a curve contribution.

The exact statement depends on the target and theory. For smooth projective threefolds with the standard numerical data, the DT/PT correspondence is established in important settings; for Calabi–Yau targets it is especially natural to express it using reduced generating series. One must check the hypotheses, conventions, and variable transformations rather than assuming an unqualified identity for any moduli stack or any dimension.

Wall crossing explains the relationship conceptually. Change the stability condition in an appropriate category of complexes or sheaves. Objects that were stable may become unstable, and new stable objects appear. The jumps in their invariants can be organized through Hall algebra or related wall-crossing formulas. Stability becomes a mathematical parameter controlling which degenerations we count.

# A line as a complete small example

Return to the line L in projective three-space. The Hilbert polynomial of its structure sheaf is m plus one, because the degree-m sections of the structure sheaf of the projective line have dimension m plus one for nonnegative m. The space of such lines is the Grassmannian of two-planes in four-space, of dimension four.

The stable pair given by O of X mapping to O of L through restriction is valid: its sheaf is pure of dimension one, and its section has zero cokernel. But no one should integrate a zero-dimensional virtual class and call the result the number of all lines in projective three-space without specifying insertions and the appropriate obstruction theory. Here the family itself already has four dimensions.

The example clarifies both the promise and the limitation of sheaf counting. We can represent degenerating curves in an algebraically stable way and compute their deformations systematically. But a virtual number is defined only after fixing the geometry, numerical invariants, stability conditions, and integration problem.

# What a curve count really records

Donaldson–Thomas and stable-pair theories enlarge the language of enumerative geometry. An ideal sheaf remembers a subscheme. A stable pair remembers a pure curve-supported sheaf and a section with finitely supported failure of generation. Perfect obstruction theory replaces naive dimension counting with a virtual class. Wall crossing connects different choices of stability.

The deeper lesson is that a good count needs a good moduli problem. When the objects can degenerate, it is the precise definition of what survives the degeneration—not a clever counting formula—that determines whether the resulting invariant is reliable.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth projective threefold X and a curve subscheme Z, `0 -> I_Z -> O_X -> O_Z ->0` defines the ideal sheaf. A Pandharipande–Thomas stable pair is a morphism `s:O_X -> F` with F pure of dimension one and `coker(s)` zero-dimensional. The pair is represented by a two-term complex `I^bullet=[O_X -> F]` under standard conventions. Tangent/obstruction groups arise from the trace-free derived self-Ext complex of `I^bullet` (with shifts specified by the obstruction-theory convention).

For `X=P^3` and a line `L=P^1 subset P^3`, choose `F=i_*O_L` and `s` the restriction of one. Then `coker(s)=0`, F is pure of dimension one, and the Hilbert polynomial is `chi(O_L(m))=m+1`. The family of such lines is `Gr(2,4)` with dimension `2(4-2)=4`.

For a smooth projective Calabi–Yau threefold, the conventional PT invariants `P_{n,beta}` are virtual-degree-zero integrals over moduli with `[F]=beta` and `chi(F)=n`. The DT/PT correspondence is usually stated in terms of generating functions and **reduced** DT series after removing degree-zero contributions, with restrictions depending on the precise theorem and geometry; it is not a count of all smooth curves with unit weight.

### Exercises with answers

1. What does purity of dimension one exclude? **Answer:** nonzero subsheaves of F supported only in dimension zero.
2. Why is `O_X -> O_L` a stable pair? **Answer:** O_L is a pure curve sheaf and the section is surjective, so the cokernel is zero.
3. How many parameters describe lines in `P^3`? **Answer:** four, because `dim Gr(2,4)=4`.
4. What corrects a moduli space of unexpected actual dimension? **Answer:** a perfect obstruction theory and its virtual fundamental class, when they exist with the required hypotheses.

### Reading and source notes

- [Pandharipande and Thomas, Curve Counting via Stable Pairs in the Derived Category](https://arxiv.org/abs/0707.2348), definition and construction of stable pairs.
- [Thomas, A Holomorphic Casson Invariant for Calabi–Yau 3-Folds](https://arxiv.org/abs/math/9806111), ideal sheaf Donaldson–Thomas theory.
- [Behrend and Fantechi, The Intrinsic Normal Cone](https://arxiv.org/abs/alg-geom/9601010), virtual classes and obstruction theory.
