# 026000 — Flat Modules: When Tensor Products Preserve Exactness

**Track:** Abstract Algebra. **Background:** tensor products, modules, localization, exact sequences, Tor. **Central question:** what property of a module prevents tensoring from destroying injections?

<!-- BEGIN SPOKEN LECTURE -->

# Flat Modules: When Tensor Products Preserve Exactness

Tensor products let us change coefficients. A vector space over the reals becomes a complex vector space when we tensor with the complex numbers. An integer module can be turned into a rational vector space by tensoring with the rationals. In geometry, the same operation lets us pass from a global ring to a ring of functions near one point.

But tensor products do not always preserve the information we started with. A nonzero element can disappear after changing coefficients. An injection can stop being an injection. The precise condition that prevents this failure is flatness.

## The warning example: reducing modulo two

Start with the inclusion of the even integers into all integers. We can identify it with the map from the integers to themselves that multiplies by two. This map is injective: if twice an integer is zero, that integer must be zero.

Now tensor the entire map over the integers with the integers modulo two. Both source and target become two-element groups. But the induced map is multiplication by two modulo two, and that is the zero map. It sends every element to zero; in particular it is no longer injective.

Nothing went wrong in the mechanics of tensoring. The issue is that reducing coefficients modulo two discards exactly the distinction that made multiplication by two injective. The tensor functor is right exact: whenever a map is onto, its tensor version remains onto, and cokernels are preserved. What may fail is preservation of kernels, and therefore preservation of injections.

## Flatness stated as a test

Let R be a commutative ring and M an R-module. We say M is flat when tensoring an exact sequence of R-modules with M keeps it exact. Because tensor product is always right exact, it is enough to check that tensoring any injection stays injective.

Every free module is flat. Indeed, tensoring with one copy of R changes nothing, and tensoring with a direct sum of copies of R forms a direct sum of the original sequence. Direct sums preserve exactness for modules. Every projective module is flat as well, since a projective module is a direct summand of a free one.

The converse is false. Flat modules need not be projective, and they certainly need not be free. This is more than a technical wrinkle: localization gives a prominent source of flat modules that are often not projective.

## Why localization is flat

Let S be a multiplicatively closed subset of R, with zero excluded in the nondegenerate case. Localizing a module N means allowing denominators from S. There is a natural isomorphism between the localization of N and the tensor product of N with the localized ring S inverse R. Therefore we can express localization as a change of coefficients.

Suppose a map from A to B is injective. Why is the induced map between their localizations also injective? An element a over s becomes zero in B localized at S only if some t in S annihilates its image in B. Because the original map was injective, the same t must annihilate a already in A. Therefore a over s was zero in the localization of A. Injectivity survives.

This argument does not require the original ring to be a domain. It proves the general fact that localization is an exact functor and that S inverse R is flat as an R-module.

Consider the map from the integers to the rationals. The rationals are obtained by inverting all nonzero integers, so they form a flat module over the integers. Yet tensoring a finite torsion group with the rationals gives zero. Flatness does not promise that every nonzero module stays nonzero. That stronger requirement is called faithful flatness. The rational numbers are flat over the integers, but not faithfully flat.

## A computation with Tor

There is a useful derived functor that measures precisely the failure of tensor product to be left exact. It is called Tor. The simplest computation comes from resolving the cyclic module Z modulo n by a two-term free resolution: multiply the integers by n, then take the quotient.

Tensor that resolution with an arbitrary abelian group A. The induced differential is multiplication by n on A. Its kernel is exactly the elements of A killed by n. That kernel is Tor one of Z modulo n with A.

Choose A to be the integers modulo m. The elements annihilated by n form a cyclic group of order the greatest common divisor of n and m. Thus Tor one of Z modulo n with Z modulo m is Z modulo the greatest common divisor. In particular, Tor one of Z modulo two with itself is nonzero. The failure we saw with multiplication by two is not an accident; Tor measures it systematically.

For a flat module M, Tor one of every module with M vanishes. The full converse also holds in the ordinary module category: Tor one vanishing against all modules is a characterization of flatness.

## Over a PID, torsion-free is enough

There is a particularly useful simplification over the integers, and more generally over a principal ideal domain. An R-module is flat if and only if it is torsion-free. Here torsion-free means that multiplying a nonzero element of the module by a nonzero ring element cannot give zero.

One direction follows from the same injection test: if M is flat, then tensoring multiplication by a nonzero scalar on R must remain injective on M, so M has no such torsion. For the other direction, a PID has enough structure to test flatness using injections of finitely generated ideals, all of which are principal. Torsion-freeness supplies the required injectivity.

Do not carry this equivalence to every domain. Over more general integral domains, torsion-free modules can fail to be flat. An ideal need not be principal or projective. Flatness controls how *all* relations behave, not just whether a single scalar annihilates an element.

## Local tests and geometric meaning

Flatness is local. An R-module M is flat if and only if, for every prime ideal p, the localization M at p is flat over the local ring R at p. This is one reason flatness is so valuable in algebraic geometry: a property about all modules can be checked one neighborhood at a time.

Informally, a flat family of geometric objects avoids certain kinds of algebraic jumps as parameters vary. But flatness should not be identified simply with constant fiber dimension; that equivalence requires specific finiteness and geometric hypotheses. The exact definition is tensor exactness, not a visual slogan about smoothly varying shapes.

The lesson connects three parts of our curriculum. Tensor products change coefficients; Tor records what that change loses; flatness guarantees that injections and short exact sequences survive. It lets algebra move between global and local viewpoints without accidentally destroying the relations we are trying to study.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a commutative ring \(R\), an \(R\)-module \(M\) is **flat** iff \(-\otimes_R M\) is exact. Tensor is always right exact, so it suffices that it preserve monomorphisms. Free and projective modules are flat. For multiplicative \(S\subseteq R\),
\[S^{-1}N\cong N\otimes_R S^{-1}R,\]
and localization is exact, hence \(S^{-1}R\) is flat.

**Failure of left exactness:** tensor \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) with \(\mathbb Z/2\). The first map becomes \(0:\mathbb Z/2\to\mathbb Z/2\), not a monomorphism.

**Tor:** the free resolution \(0\to\mathbb Z\xrightarrow{\times n}\mathbb Z\to\mathbb Z/n\to0\) gives
\[\operatorname{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)=\ker(n:A\to A)=A[n].\]
For \(A=\mathbb Z/m\) this is isomorphic to \(\mathbb Z/\gcd(n,m)\). Flatness of \(M\) is equivalent to \(\operatorname{Tor}_1^R(N,M)=0\) for all \(R\)-modules \(N\).

**Cautions:** \(\mathbb Q\) is flat but not faithfully flat over \(\mathbb Z\): \((\mathbb Z/p)\otimes_{\mathbb Z}\mathbb Q=0\). Over a PID, flat is equivalent to torsion-free (including non-finitely generated modules). Over general domains, torsion-free need not imply flat. A standard local criterion is \(M\) flat over \(R\) iff \(M_{\mathfrak p}\) flat over \(R_{\mathfrak p}\) for each prime \(\mathfrak p\).

### Exercises with answers

1. Is \(\mathbb Z/7\) flat as a \(\mathbb Z\)-module? **No:** it has nonzero torsion, and \(\mathbb Z\) is a PID.
2. Is \(\mathbb Z[1/6]\) flat over \(\mathbb Z\)? **Yes:** it is a localization.
3. Compute \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/8,\mathbb Z/12)\). **Answer:** \(\mathbb Z/4\), the subgroup killed by eight.
4. If localization kills an \(R\)-module, must the original module have been zero? **No:** \(\mathbb Z/2\) becomes zero over \(\mathbb Z[1/2]\).

### Reading and source notes

- [Stacks Project, Section 10.39, Flat modules and flat ring maps](https://stacks.math.columbia.edu/tag/00H9), definitions, localization, and local flatness criteria.
- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), flatness, Tor, and derived functors.
