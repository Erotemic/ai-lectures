# 025400 — Fredholm Index and Transversality: Counting Dimensions Before Curves

**Track:** Topology and Geometry. **Background:** Riemann surfaces, elliptic operators, bundles and characteristic classes, implicit function theorem. **Central question:** how can topology predict the dimension of a space of solutions to a nonlinear PDE?

<!-- BEGIN SPOKEN LECTURE -->

# Fredholm Index and Transversality: Counting Dimensions Before Curves

Suppose we want to count holomorphic spheres in a symplectic manifold. Before finding even one, there is a more basic question. Should we expect isolated solutions, a family with several continuous parameters, or no solutions at all?

An elliptic index gives a first approximation. It measures the difference between the number of infinitesimal solutions and the number of infinitesimal obstructions. This is not automatically the actual number of independent solutions. But it is a computable, topological quantity that guides the analysis.

## A linear operator with two finite dimensions

Take one holomorphic curve u. Perturb it by a small vector field along the curve. Linearizing the Cauchy-Riemann equation produces an elliptic operator. Its kernel consists of first-order deformations that continue to satisfy the equation to first order.

A nonzero cokernel represents obstructions: infinitesimal errors that cannot be corrected by any first-order deformation. The Fredholm index is the real dimension of the kernel minus the real dimension of the cokernel.

Ellipticity on a compact domain makes both dimensions finite. The index is stable under continuous perturbations of lower-order terms. That stability allows topology, rather than detailed coefficients, to determine the answer.

## Riemann–Roch as a dimension formula

Let the domain be a closed Riemann surface of genus g, and suppose the target has complex dimension n. The linearized operator acts on sections of the pullback tangent bundle. Its real index has two contributions.

The first depends on the Euler characteristic of the domain, which is two minus two g, multiplied by n. The second is twice the first Chern number of the target tangent bundle evaluated on the curve's homology class.

Think of the first term as the number of directions available from the basic topology of the domain. Think of the Chern term as measuring the twisting of the complex vector bundle along the map. This is a version of the Riemann–Roch theorem for Cauchy-Riemann operators.

That formula applies to the parameterized curve problem with a fixed complex structure on the domain. It is not yet the expected dimension of the space of unparameterized geometric curves.

## Count projective lines in the complex projective plane

Consider the complex projective plane, which has complex dimension two. Its lines are themselves copies of the Riemann sphere. A projective line represents the basic degree-one homology class.

The target tangent bundle has first Chern number three on that class. The domain is a sphere, so its Euler characteristic is two. The real Fredholm index is therefore two times two, plus two times three: ten.

Why ten and not four, the familiar real dimension of the family of projective lines? Because the operator treats differently parameterized copies of the same sphere as distinct. The Riemann sphere has a six-real-dimensional group of holomorphic automorphisms. Subtract those reparameterizations, assuming the action behaves well, and ten minus six is four.

Indeed, projective lines in the projective plane form another projective plane, the dual projective plane. It has complex dimension two, or real dimension four. Our index calculation has matched the geometry exactly.

## The hidden hypothesis: regularity

The computation worked because the holomorphic line is regular. The linearized Cauchy-Riemann operator has no obstruction space beyond those already accounted for, and quotienting by reparameterization is well-behaved in this example.

For an arbitrary J-holomorphic map, the actual dimension can differ from the expected one. The cokernel might be nonzero. Multiple covers can have stabilizers or fail generic transversality. Constant maps create their own automorphism complications. Merely subtracting six from every sphere index would be wrong.

A powerful method is to choose a generic compatible almost-complex structure J. Under appropriate hypotheses, moduli spaces of somewhere-injective, or simple, curves become regular. In functional-analytic language, this uses a version of Sard's theorem for infinite-dimensional spaces, together with a carefully constructed universal moduli space.

This does not automatically regularize every multiply covered curve. Those are among the reasons modern theories sometimes require virtual fundamental cycles or related perturbation machinery. We should not present the word generic as a universal solvent.

## What the index cannot tell us

A predicted dimension of zero does not prove that a solution exists. It says that if solutions exist and are regular, we expect them to be isolated after quotienting symmetries. A predicted negative dimension often suggests that generic simple curves in that class are absent, but exceptional maps or nongeneric data still require care.

Nor does index zero imply a finite count. An infinite sequence of isolated solutions might escape through bubbling or degeneration. Compactness is a logically separate ingredient. Orientations are also needed for integer counts, or one can sometimes work with coefficients modulo two.

The full path to an invariant therefore has several steps: define a geometric equation, compute the linearized index, obtain transversality, control degenerations, quotient symmetries, and only then count solutions.

## Why this prepares us for Floer theory

For a Floer cylinder, the same principle applies with a noncompact domain. The index is related to a spectral-flow or Conley–Zehnder index difference between its limiting periodic orbits. We must additionally account for translation of the cylinder along its length.

As with spheres, a zero-dimensional quotient space is where a numerical count becomes plausible. A one-dimensional quotient space is where its boundary can encode an algebraic identity. But both dimensions are only predictions until we establish regularity and compactness.

The projective-line calculation gave an encouraging example: algebraic topology predicted exactly the dimension of a classical geometric family. The advanced theory will reuse this logic, while facing harder analytic and symmetry problems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a closed genus-\(g\) Riemann surface \(\Sigma\), a fixed domain complex structure \(j\), and \(u:\Sigma\to M^{2n}\) in homology class \(A\), the real index of the linearized Cauchy–Riemann operator is
\[
\operatorname{ind}_{\mathbb R}D_u=n(2-2g)+2\langle c_1(TM,J),A\rangle.
\]
For unparameterized genus-\(g\) simple curves with \(k\) marked points and the stable-domain setup, the standard expected real dimension is \((2n-6)(1-g)+2c_1(A)+2k\). The distinction includes variations in complex structure and quotienting automorphisms. For \(\mathbb{CP}^2\), \(n=2\), \(g=0\), and a line \(A=[\mathbb{CP}^1]\), \(c_1(T\mathbb{CP}^2)(A)=3\), hence fixed-domain parameterized index \(4+6=10\). Subtracting the free six-dimensional sphere-automorphism action gives \(4\), matching the dual projective plane parameterizing lines.

Regularity requires surjectivity of \(D_u\); for simple curves, generic \(J\) can produce transversality under appropriate setup. Multiple covers, automorphisms, compactness, and orientations require separate handling. Index is a virtual dimension, not an existence statement.

### Exercises with answers

1. **Line index.** Compute the parameterized real index of a degree-one sphere in \(\mathbb{CP}^2\). **Answer:** \(2(2)+2(3)=10\).
2. **Unparameterized.** Why does the dimension drop from ten to four for a projective line? **Answer:** quotient by the real six-dimensional \(\mathrm{PSL}_2(\mathbb C)\) parameterization symmetry.
3. **Index zero.** Does a zero Fredholm index guarantee a nonempty finite moduli space? **Answer:** no; existence, regularity, and compactness are independent issues.
4. **Cokernel.** If \(\dim\ker D=7\) and \(\dim\operatorname{coker}D=2\), what is its index? **Answer:** five.

### Sources and further reading

- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), Fredholm and transversality chapters.
- Chris Wendl, [Lectures on Holomorphic Curves](https://arxiv.org/abs/1011.1690), index, simple curves, and moduli spaces.
- [Riemann–Roch theorem](https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem); [Fredholm operator](https://en.wikipedia.org/wiki/Fredholm_operator).
