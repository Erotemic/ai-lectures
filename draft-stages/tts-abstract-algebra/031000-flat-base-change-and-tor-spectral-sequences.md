# 031000 — Flat Base Change and Tor Spectral Sequences

**Track:** Abstract Algebra. **Background:** tensor products, short exact sequences, flatness, projective resolutions, spectral sequences. **Central question:** what must be corrected when an algebraic calculation is transported to a new ring?

<!-- BEGIN SPOKEN LECTURE -->

# Flat Base Change and Tor Spectral Sequences

Suppose we have solved a problem over one ring and want to solve its counterpart over another. We might reduce integer coefficients modulo a prime, extend scalars from real to complex numbers, or specialize a polynomial parameter. Tensor products are the algebraic machinery behind these operations. But there is a trap: transporting objects is easier than transporting the exact relationships between them.

The word flatness names the condition that avoids that trap. When flatness fails, Tor groups keep track of the correction. When several layers of corrections interact, spectral sequences organize them.

## A short exact sequence that breaks

Start with the integers and the map that multiplies an integer by two. This map is injective. Its cokernel is the integers modulo two, so we have a short exact sequence: integers, multiplied by two into integers, followed by reduction modulo two.

Now tensor each term with the integers modulo two. Both copies of the integers become the two-element module. Multiplication by two becomes the zero map. The resulting sequence cannot be exact at its first nonzero term: a zero map is not injective.

The failure is structural, not a small computational error. Tensor product always preserves cokernels and hence right exactness. It does not, in general, preserve injections. A module F is called flat when tensoring with F preserves every short exact sequence. A flat change of scalars therefore keeps the exact relationships that define kernels, images, and quotients.

Localization is a basic source of flat modules. Passing from the integers to the rational numbers, or inverting powers of a chosen integer, preserves exact sequences. But preservation is not the same as preserving every nonzero element: localization can kill torsion. An injection remains an injection after flat base change, even if both sides of a particular torsion sequence become zero.

## Tor records the missing information

Tensoring is right exact, so homological algebra derives it on the left. Choose a projective or free resolution of one input, tensor that resolution with the other, and compute homology. In degree zero the result is the ordinary tensor product. In higher degrees the groups are called Tor.

Take the earlier resolution of the integers modulo two, using multiplication by two between two copies of the integers. Tensor with the integers modulo two. The differential becomes zero, so its first homology is another copy of the integers modulo two. That group is Tor in degree one. It measures exactly the injection that tensoring destroyed.

If an input is flat, its positive-degree Tor groups vanish against every module. Conversely, vanishing of all first Tor groups against a module characterizes flatness. This makes flatness observable by a family of homological tests.

## A change of rings has two routes

Let R map to a ring S. Suppose M is an R-module, while N is an S-module, and therefore also an R-module by restriction. We can try to calculate Tor over R between M and N directly. Or first transport M from R to S, and then calculate Tor over S.

If we simply replace M by its ordinary tensor product with S, the second approach may lose information. The base change itself could have higher Tor. The correct first stage is derived tensoring, which remembers an entire complex rather than only its degree-zero quotient.

There is a change-of-rings spectral sequence whose second page consists of Tor over S applied to the Tor groups over R of M with S. It converges, with standard boundedness conventions, to Tor over R of M with N. The page has two indices because one index measures the cost of base change and the other measures the Tor computation performed afterward.

This formula is not a mysterious extra theorem bolted onto tensor product. Build a free resolution of M over R. Tensor it with S, then resolve the resulting S-complex when necessary and tensor with N. The resulting double complex can be read in two directions. One filtration computes the intermediate Tor groups; the other leads to the desired total homology. A spectral sequence is the bookkeeping system for comparing the two routes.

## The smallest counterexample

Here is a calculation that makes the correction visible. Take R to be the polynomial ring in one variable over a field k. Let S be the quotient obtained by setting that variable to zero, so S is k. Take M and N both to be k, with their natural module structures.

Over R, the module k has a two-term free resolution: multiplication by the polynomial variable between two copies of R. After tensoring with k, the variable acts as zero, and we obtain two nonzero Tor groups, one in degree zero and one in degree one.

But over S, which is itself the field k, higher Tor groups vanish. If we first replaced M by its ordinary base change, we would see only the degree-zero k and miss the degree-one result entirely.

The change-of-rings spectral sequence retains the missing k in a second row. There are no possible further differentials in this simple example, so the two classes survive and reproduce the calculation over R. The added homological grading has paid for itself.

## Flat base change simplifies the picture

When S is flat over R, Tor over R of M with S vanishes in positive degrees. Then the change-of-rings spectral sequence collapses to its single remaining row. Under the usual module conditions, Tor over R of M with N can be computed as Tor over S of the base-changed M with N.

There is a related flat-base-change statement for a pair of R-modules M and N: after tensoring their Tor groups with a flat R-algebra S, one obtains the corresponding Tor groups over S of their scalar extensions. The exact formulation depends on which variables are being transported, but the principle is constant. Flatness means no hidden derived corrections appear merely because the coefficient ring changed.

This is why flatness is central in algebraic geometry, where families are studied over varying base rings. It marks a setting in which algebraic behavior changes without unpredictable loss of exactness.

## Why retain the machinery

A module is not just a collection of elements. Its relations are part of the object. Plain tensor products may erase some relations in ways that destroy kernels, while derived tensor products remember the loss. Tor makes the correction measurable. Spectral sequences make multiple corrections composable.

So the right question after a change of coefficients is not merely, “What do the generators become?” It is, “Which exact properties survive, and what derived information measures what did not?” The distinction becomes indispensable in algebraic geometry, topology, and modern approaches to computation with chain complexes.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an \(R\)-module \(F\), flatness means \((-\otimes_R F)\) is exact, equivalently \(\operatorname{Tor}_1^R(M,F)=0\) for all \(M\). For a multiplicative set \(U\subset R\), the localization \(U^{-1}R\) is flat.

**Loss of injectivity:** \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) is exact. Tensoring with \(\mathbb Z/2\) gives a zero map \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\), so injectivity is lost and \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2\).

**Change-of-rings spectral sequence:** for a commutative ring map \(R\to S\), an \(R\)-module \(M\), and an \(S\)-module \(N\), a homological convention yields
\[E^2_{p,q}=\operatorname{Tor}^S_p(\operatorname{Tor}^R_q(M,S),N)\Longrightarrow\operatorname{Tor}^R_{p+q}(M,N).\]
Standard convergence/boundedness and indexing conventions apply. When \(S\) is \(R\)-flat this collapses to \(\operatorname{Tor}^R_n(M,N)\cong\operatorname{Tor}^S_n(M\otimes_R S,N)\).

**Worked example:** \(R=k[x]\), \(S=R/(x)=k\), \(M=N=k\). The free resolution \(0\to R\xrightarrow{x}R\to k\to0\) gives \(\operatorname{Tor}_0^R(k,k)=k\), \(\operatorname{Tor}_1^R(k,k)=k\), all higher Tor zero. Its base change to \(S\) has zero differential. Since \(\operatorname{Tor}_p^k(-,k)=0\) for \(p>0\), the spectral sequence has \(E^2_{0,0}=E^2_{0,1}=k\), matching the abutment.

### Exercises with answers

1. Does tensoring preserve surjections? **Yes:** tensor product is right exact.
2. Can a flat base change kill a nonzero torsion module? **Yes:** \(\mathbb Z/2\otimes_{\mathbb Z}\mathbb Q=0\), but exactness is still preserved.
3. What is \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,A)\)? **Answer:** the \(n\)-torsion subgroup \(\{a\in A:na=0\}\).
4. Which term of the change-of-rings spectral sequence is missed if one simply substitutes \(M\otimes_R S\)? **Answer:** all \(q>0\) terms \(\operatorname{Tor}_q^R(M,S)\).

### Reading and source notes

- [Stacks Project, Spectral sequences for Tor](https://stacks.math.columbia.edu/tag/061Y), change-of-rings spectral sequence with index conventions.
- [Stacks Project, Tor independence](https://stacks.math.columbia.edu/tag/065Y), derived versus ordinary base change.
- [Stacks Project, Computing Tor](https://stacks.math.columbia.edu/tag/064F), projective resolutions and derived tensor products.
