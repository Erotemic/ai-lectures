# 062000 — Borel–Weil–Bott: Finding Representations in Line-Bundle Cohomology

**Track:** Abstract Algebra. **Background:** representations of reductive groups, algebraic line bundles, projective spaces, and sheaf cohomology. **Central question:** why does a geometric space of flags encode highest-weight representations?

<!-- BEGIN SPOKEN LECTURE -->

# Geometry as a representation factory

Suppose we want to construct every finite-dimensional irreducible representation of a complex semisimple Lie group. Pure algebra says to classify highest weights, build a highest-weight vector, and act with lowering operators. Geometry offers another answer. Put a suitable line bundle on the space of all flags in a vector space, take the cohomology of that line bundle, and let the group act on the result.

For dominant weights, the space of global sections produces a representation. For non-dominant weights, the correct cohomology can appear in a higher degree. The Borel–Weil–Bott theorem organizes both phenomena and explains why the Weyl group enters the calculation with a shift by the vector called rho.

The smallest complete example is the projective line, which is also the flag variety for the group of two-by-two matrices of determinant one. Working this example gives us an entire table of representations and cohomology groups that can be checked without abstract machinery.

# The projective line carries the group action

The group SL two acts on the two-dimensional complex vector space. It therefore acts on the collection of one-dimensional subspaces, because multiplying a line by an invertible matrix gives another line. That collection is the projective line.

A line bundle over the projective line assigns a one-dimensional vector space to each point. The bundles named O of n, for integers n, are fundamental. For nonnegative n, a global section of O of n can be represented by a homogeneous polynomial of degree n in two variables. Substitute the transformed coordinates into the polynomial, and the group moves sections into sections. The space of homogeneous degree-n polynomials is exactly the symmetric-power representation, up to the standard choice of dual action.

Count monomials. Degree zero gives one constant. Degree one gives two linear forms. Degree two gives three quadratic monomials. In general the dimension is n plus one. In the highest-weight classification of SL two, that is the irreducible representation of highest weight n.

The geometry has manufactured a representation from functions that vary coherently over a space of lines. No basis-dependent matrix formula had to be guessed.

# Why negative degree changes the answer

There are no nonzero global holomorphic sections of a negative-degree line bundle on the projective line. A putative section would need poles to compensate for its negative twisting, but a global holomorphic section cannot acquire those poles. Thus for n less than zero, degree-zero cohomology vanishes.

That does not mean the bundle contains no representation-theoretic information. The first cohomology group measures the failure to glue local sections into one global section. For n equal to negative one, both the zeroth and first groups vanish. For n equal to negative two, the first cohomology has dimension one. For n equal to negative three, it has dimension two. In general, when n is at most negative two, the dimension of the first cohomology is minus n minus one.

This is precisely the representation that a reflected highest weight predicts. The two-dimensional representation returns at n equal to negative three, not in global sections but in first cohomology. The line bundle has changed degree, and the representation has moved to a different cohomological degree.

# A gluing calculation explains the jump

Cover the projective line with two copies of the affine line. Their overlap is the punctured affine line. A line bundle is trivial on each chart, but the two trivializations differ by a power of the overlap coordinate. A global section is a compatible pair of polynomials, one on each chart. First cohomology is the space of overlap data modulo differences of chartwise data.

If the twisting degree is minus two, one Laurent monomial survives this quotient. If it is minus three, two independent Laurent monomials survive. More negative twisting allows more of these gluing obstructions. That count gives the first-cohomology dimensions just stated.

Serre duality offers another check. The canonical bundle of the projective line is O of negative two. Consequently the first cohomology of O of negative n minus two is dual to the global sections of O of n for n nonnegative. A degree-n polynomial representation and its cohomological partner have the same dimension, as they must.

# From one reflection to a Weyl group

In a higher-rank reductive group the flag variety is the space of Borel subgroups, or equivalently the homogeneous space G modulo a Borel subgroup. Characters of the Borel define equivariant line bundles. Their cohomology groups inherit group actions.

The theorem starts with a weight lambda and adds rho, half the sum of positive roots. If lambda plus rho lies on a Weyl reflection hyperplane, every cohomology group vanishes. Otherwise one can reflect lambda plus rho into the dominant chamber using a unique Weyl-group element. Exactly one cohomology degree survives, and that degree is the length of the reflection element. Its nonzero group is an irreducible representation of the resulting dominant highest weight, with a dual convention depending on the line bundle definition.

Why the rho shift? Even for SL two, the shift explains the exceptional weight negative one, where everything vanishes. Reflection about negative one sends an integer n to negative n minus two. That is exactly the symmetry seen between the positive-degree global sections and the negative-degree first cohomology.

# What the theorem does and does not say

This calculation is powerful because it integrates topology, algebraic geometry, and representation theory. The same Weyl group that classifies chambers in root space dictates which cohomology degree appears. The Euler characteristic of a line bundle recovers the alternating character calculation underlying the Weyl character formula.

But not every vector bundle on an arbitrary variety has one nonzero cohomology group. This theorem is tied to homogeneous flag varieties, equivariant line bundles, and reductive symmetry, with an appropriate base field and hypotheses. For more complicated bundles, cohomology can occur in several degrees. In positive characteristic the characteristic-zero statement needs care.

On the projective line the entire pattern can be heard as one rule: positive twisting gives polynomial sections, twisting by negative one gives silence, and more negative twisting produces representations one degree higher. Borel–Weil–Bott recognizes the same pattern across all flag varieties by replacing the single reflection with an entire Weyl group.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `G=SL_2(C)` and `G/B=P^1`, standard line bundles satisfy
\[
H^0(\mathbf P^1,\mathcal O(n))\cong\begin{cases}\operatorname{Sym}^n(\mathbb C^2)^*&n\ge0,\\0&n<0,\end{cases}\quad
H^1(\mathbf P^1,\mathcal O(n))\cong\begin{cases}0&n\ge-1,\\ H^0(\mathbf P^1,\mathcal O(-n-2))^*&n\le-2.\end{cases}
\]
Here duals depend on the convention for the SL2 linearization, and SL2 irreducibles are self-dual. The second identity is Serre duality with `K_{P1}=O(-2)`.

For a connected, simply connected, complex semisimple G, a weight lambda and its equivariant line bundle `L_lambda` on `G/B`, the Borel–Weil–Bott statement (with compatible sign convention) is: if `lambda+rho` is singular, all `H^i` vanish; if regular, the unique w taking `lambda+rho` to the dominant chamber yields one nonzero cohomology group in degree `ell(w)`, of highest weight `w(lambda+rho)-rho`. This is the dot action `w·lambda=w(lambda+rho)-rho`.

**Čech count:** on affine charts U0 and U∞, gluing is by a monomial of degree n. The quotient of Laurent polynomials on their overlap by extendible chartwise sections has basis represented by `z^{-1},...,z^{-m+1}` for `n=-m` and `m>=2`; its dimension is `m-1`. Equivalent powers depend on the chosen trivialization.

### Exercises with answers

1. Give dimensions of `H0(O(4))` and `H1(O(-5))`. **Answer:** five and four, respectively.
2. Why is n=-1 exceptional? **Answer:** it is the singular shifted weight; both cohomology groups vanish.
3. What is the highest weight associated to `H1(O(-4))` for SL2? **Answer:** two, with a three-dimensional irreducible representation.
4. If lambda+rho lies on a reflection wall, does a different cohomology degree necessarily rescue it? **Answer:** no; all cohomology vanishes in the characteristic-zero theorem.

### Reading and source notes

- [Serganova, Lectures in Lie Groups and Quantum Groups, Borel–Weil–Bott](https://math.berkeley.edu/~serganov/261/part1.pdf), general theorem and SL2 calculations.
- [University of Michigan seminar, Borel–Weil–Bott for SL2](https://websites.umich.edu/~charchan/seminar/20210927.pdf), projective-line model.
- [Stacks Project, Cohomology of Schemes](https://stacks.math.columbia.edu/download/cohomology.pdf), sheaf cohomology and base-change context.
