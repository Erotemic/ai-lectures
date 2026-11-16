# 042000 — Adjunction Inequalities and Smooth Genus Bounds

**Track:** Topology and Geometry. **Background:** four-manifold intersection forms, Chern classes, and Seiberg–Witten invariants. **Central question:** how can gauge-theoretic invariants bound the genus of an embedded surface?

<!-- BEGIN SPOKEN LECTURE -->

# The same homology class can be represented differently

Suppose a two-dimensional surface sits smoothly inside a four-dimensional manifold. It determines a homology class. But homology alone does not tell us the genus of the surface. We might represent the same class by surfaces with additional handles, increasing the genus without changing the class.

The more difficult question runs in the opposite direction. How simple can the surface be? Is there a lower bound on its genus that depends only on the homology class and the smooth structure of the ambient four-manifold?

The answer is often yes. Gauge theory supplies adjunction inequalities that constrain the minimal genus. These inequalities are striking because they connect a geometric field equation, which lives on the entire four-manifold, to the topology of a particular embedded surface.

# Start with the complex adjunction formula

For a smooth complex curve inside a complex surface there is an exact formula. The canonical class of the ambient complex surface, evaluated on the curve, plus the self-intersection of the curve, equals twice the genus minus two.

Self-intersection needs explanation. Push the curve slightly in a normal direction and count the signed intersections with the original curve. This number is also the Euler number of the oriented normal bundle. In a complex surface the normal bundle has a natural complex structure, which makes the algebraic and topological descriptions agree.

The canonical class records the first Chern class of the bundle of holomorphic two-forms. The adjunction formula says that the canonical bundle of the curve is obtained by restricting the ambient canonical bundle and tensoring with the curve's normal bundle. Taking degrees gives the numerical identity.

On a K3 surface the canonical class is zero. Consequently a smooth holomorphic curve of genus g has self-intersection twice g minus two. An elliptic curve has self-intersection zero. A smooth genus-two curve has self-intersection two. These are equalities, not approximations.

# Why a smooth surface needs an inequality

A smooth embedded surface in a four-manifold need not be complex. There may be no preferred holomorphic tangent line, so the complex adjunction formula no longer applies as an identity.

Seiberg–Witten theory can nevertheless recover a lower bound. Let K be a Seiberg–Witten basic class. Under the usual hypotheses—including a closed oriented four-manifold with sufficiently large positive second Betti number and a connected embedded surface of positive genus with nonnegative self-intersection—an adjunction inequality says that twice the genus minus two is at least the self-intersection plus the absolute value of the pairing with K.

The absolute value appears because the bound must not depend on choosing an orientation for the surface in a way that artificially improves the inequality. This formula has variants with different hypotheses, and it must not be applied indiscriminately to spheres of negative self-intersection or four-manifolds with wall-crossing complications.

# Work through K3 again

Take a K3 surface, whose Seiberg–Witten basic class zero is nontrivial. The inequality reduces to twice the genus minus two being at least the self-intersection, for a connected positive-genus surface of nonnegative self-intersection.

Suppose a homology class has square two. Then every such smooth connected representative must have genus at least two. A smooth holomorphic genus-two curve in that class reaches the bound exactly. That does not merely calculate the genus of the holomorphic example; it proves the holomorphic representative has minimal genus among all smooth connected representatives meeting the hypotheses.

This is the conceptual leap. Algebraic geometry constructs one surface and proves an equality for it. Gauge theory tells us that no smooth competitor in the same homology class can be simpler.

# What is visible to smooth topology

Why isn't this just an inequality about the intersection form? Because the basic class K enters from a smooth gauge-theoretic invariant. Different smooth structures on a topological four-manifold can support different gauge-theoretic constraints. Thus minimal genus can carry information beyond ordinary homology and intersection numbers.

But one should also avoid an opposite overstatement. Knowing a lower bound does not automatically construct a representative achieving it. Sometimes the bound is sharp, as in holomorphic examples. Sometimes a separate geometric construction is needed, or the true minimal genus is larger.

The result is also sensitive to the ambient hypotheses. If the four-manifold has positive second Betti number equal to one, the Seiberg–Witten invariant may depend on a chamber. If the surface has negative square, blow-up and exceptional-curve phenomena require a different formulation. A slogan about genus cannot replace the actual theorem.

# From a surface to a constraint on the manifold

Adjunction inequalities demonstrate a productive dialogue between topology and analysis. A surface presents a geometric challenge: can this homology class be realized with fewer handles? The Seiberg–Witten equations supply global restrictions. The canonical class and intersection pairing translate those restrictions into an integer inequality.

The K3 example is especially clear. Genus two and self-intersection two fit the complex adjunction formula exactly. The Seiberg–Witten inequality then forbids a connected smooth genus-one representative in that same class. We have learned something about all possible smooth representatives by studying one algebraic representative and a gauge invariant of the ambient space.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth irreducible complex curve `C\subset X` in a smooth complex projective surface, adjunction says `K_C\cong(K_X\otimes\mathcal O_X(C))|_C`. Taking degrees gives
\[
2g(C)-2=C^2+K_X\cdot C.
\]
For a K3 surface `K_X=0`, so `2g(C)-2=C^2`.

A standard Seiberg–Witten adjunction inequality: if `X` is a smooth closed oriented 4-manifold with `b_2^+(X)>1` and SW basic class `K`, and `\Sigma\subset X` is a smoothly embedded closed connected oriented surface with `g(\Sigma)>0`, `[\Sigma]^2\ge0`, then under the standard basic-class hypotheses,
\[
2g(\Sigma)-2\ge [\Sigma]^2+|\langle K,[\Sigma]\rangle|.
\]
The nonnegative self-intersection and positive-genus hypotheses are substantive; variants for negative squares and other `b_2^+` require additional conditions. For K3, the zero basic class yields `2g-2\ge [\Sigma]^2`. A class with square two therefore satisfies `g\ge2`; a smooth genus-two holomorphic curve realizes equality if that class admits one.

### Exercises with answers

1. If a smooth holomorphic curve on a K3 has genus three, what is its square? **Answer:** `4`.
2. For a K3 class of square six, what genus lower bound does the inequality give? **Answer:** `g\ge4` for a connected positive-genus nonnegative-square representative.
3. Does the inequality by itself prove a representative attaining the bound exists? **Answer:** No.
4. Why not apply this formulation unchanged to an exceptional sphere of square `-1`? **Answer:** it violates both positive-genus and nonnegative-square hypotheses.

### Reading and source notes

- [Edward Witten, Monopoles and Four-Manifolds](https://arxiv.org/abs/hep-th/9411102), Seiberg–Witten invariants and four-manifold constraints.
- [Konno, A Cohomological Seiberg–Witten Invariant Emerging from the Adjunction Inequality](https://doi.org/10.1112/topo.12215), modern extension and a discussion of adjunction constraints.
