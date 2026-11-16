# 055000 — Radon–Nikodym and Riesz: When Measurements Have Densities

**Track:** Analysis from First Principles. **Background:** Lebesgue integration, finite measures, Hilbert spaces and bounded functionals. **Central question:** When can an abstract measurement be written as an integral?

<!-- BEGIN SPOKEN LECTURE -->

# Radon–Nikodym and Riesz: When Measurements Have Densities

Suppose someone gives us a rule that assigns a number to every measurable region of a landscape. The rule might report area, mass, or the amount of a chemical substance in the region. A natural question is whether this information comes from a density: a function whose integral over each region produces the reported number.

Sometimes it does. Sometimes it cannot. The Radon–Nikodym theorem explains the dividing line. Another theorem, the Riesz representation theorem, describes when continuous linear measurements of vectors or functions can also be written as inner products or integrals. The two results share an idea: replace a rule that acts on whole objects by a representer that we can analyze point by point.

Start with two measures, which we will call mu and nu. Think of mu as ordinary length or area, and nu as mass. If a region has zero area, and every such region also has zero mass, we say nu is absolutely continuous with respect to mu. This is a statement about zero sets. It is not yet a statement about a formula.

For a finite measure nu and a sigma-finite base measure mu, the Radon–Nikodym theorem says that this condition is enough: there exists an integrable density, locally interpreted where needed, such that nu of a region equals the integral of the density over that region. When nu is a finite signed measure, the density may be negative; when nu is positive, the density is nonnegative. The density is unique up to changes on sets of mu measure zero.

An example on the unit interval helps. Let nu of a set be the integral over that set of twice x. Then nu is absolutely continuous with respect to length, with density twice x. The entire interval has mass one, but the right half contains more than half of the mass. The density records how that mass is distributed.

Now consider a measure concentrated entirely at the midpoint. It assigns mass one to any region containing the midpoint and zero to regions not containing it. The single point has length zero but mass one. No ordinary integrable density with respect to length can represent this measure. That is precisely what absolute continuity rules out. The point mass is not an exception to integration; it tells us we chose the wrong base measure if we expected an ordinary density.

Why should such a density exist whenever absolute continuity holds? The proof in a finite-measure setting uses the geometry of L two. Among all candidate densities that do not assign more mass to any region than nu, one constructs a maximal candidate. If there were leftover positive measure that the candidate failed to account for, a suitable local adjustment would improve it, contradicting maximality. An alternative proof uses the Hilbert-space representation theorem, and measures on general sigma-finite spaces can be handled by a countable exhaustion. The full argument needs care because measures and functions may be infinite on large regions; the essential idea is to turn a set-by-set compatibility condition into a globally defined function.

The name Riesz occurs in two related representation results. Let us first take a Hilbert space: a space with an inner product and complete norm. A bounded linear functional assigns a scalar to each vector, varying continuously and linearly with that vector. The Hilbert-space Riesz theorem says there is one unique vector g such that the functional of x is the inner product of x with g. Thus every continuous linear measurement of a Hilbert-space vector is itself encoded by a vector.

In ordinary two-dimensional geometry, the rule that measures the sum of the first coordinate and twice the second is represented by the vector with coordinates one and two. The inner product with that vector gives exactly the measurement. In a function space, the same idea becomes integration against a function g. If we work in L two, the functional of f can be written as the integral of f times the complex conjugate of g, with the usual convention about which argument is linear.

There is a useful geometric proof. If a bounded functional is nonzero, its kernel is a closed hyperplane. Find a unit vector perpendicular to that hyperplane. Every input decomposes into a part inside the kernel and a scalar multiple of the perpendicular vector. The functional ignores the kernel part. Its entire value is determined by the single scalar coefficient. That is exactly the representation by an inner product.

A separate Riesz representation theorem concerns continuous functions on a compact space. A positive linear functional on continuous functions can be represented by integration against a finite regular Borel measure. Here the representing object is a measure, not necessarily a density relative to length. For example, evaluation of a continuous function at a point is represented by a point mass. It is continuous in the maximum norm even though no ordinary L one density represents it relative to length.

These distinctions prevent several common confusions. The Hilbert-space theorem represents bounded functionals by vectors. The measure-theoretic Riesz theorem represents positive functionals on continuous functions by measures. Radon–Nikodym then asks whether that representing measure has a density with respect to another measure. None of these steps is automatic if we change the space or norm without checking assumptions.

Why does this matter elsewhere? When a numerical method reports a linear output, a Riesz representer identifies the direction in which the output is sensitive. When a probability law is absolutely continuous relative to another, Radon–Nikodym gives the likelihood ratio. When we describe a forcing term in a weak differential equation, we need to know whether it is represented by an ordinary function, an L two vector, or a more general distribution.

The general lesson is that a formula involving an integral is not merely notation. It is the conclusion of a representation theorem whose hypotheses tell us exactly which kinds of measurements can be compressed into a density, a vector, or a measure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Radon–Nikodym.** If \(\mu\) is sigma-finite and \(\nu\) is a sigma-finite positive measure with \(\nu\ll\mu\), then there is a measurable \(h\ge0\), finite \(\mu\)-a.e. under these hypotheses, with \(\nu(E)=\int_Eh\,d\mu\). For a finite signed or complex measure absolutely continuous with respect to \(\mu\), \(h\in L^1(\mu)\) is unique a.e. Be careful that a sigma-finite \(\nu\) need not have a globally \(L^1\) density if \(\nu(X)=\infty\).

**Hilbert-space Riesz.** Fix \(\langle x,y\rangle\) linear in \(x\). For any bounded complex-linear \(\Lambda:H\to\mathbb C\) there exists unique \(g\in H\) with \(\Lambda(x)=\langle x,g\rangle\), \(\|\Lambda\|=\|g\|\).

**Riesz–Markov.** For compact Hausdorff \(X\), each positive linear functional \(L:C(X)\to\mathbb R\) is \(L(f)=\int_X f\,d\mu\) for a unique finite regular Borel measure \(\mu\). Point evaluation is represented by \(\delta_{x_0}\).

Example: for \(d\nu=2x\,dx\) on \([0,1]\), \(\nu([1/2,1])=\int_{1/2}^1 2x\,dx=3/4\).

### Exercises with answers

1. **Point mass.** Why is \(\delta_{1/2}\not\ll dx\)? **Answer:** A singleton has Lebesgue measure zero but Dirac measure one.
2. **Hilbert representer.** Find the \(\ell^2\) representer of \(\Lambda(x)=2x_1-x_3\). **Answer:** \(g=(2,0,-1,0,\ldots)\) for real sequences.
3. **Compare the theorems.** What represents point evaluation on \(C([0,1])\)? **Answer:** A Dirac measure via Riesz–Markov, not an L-one density with respect to length.

### Reading and source notes

- [John K. Hunter, Measure Theory notes](https://www.math.ucdavis.edu/~hunter/m206/intro_measure_notes.pdf)
- [Sheldon Axler, Measure, Integration and Real Analysis](https://measure.axler.net/)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
