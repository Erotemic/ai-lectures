# 037500 — The Conductor–Discriminant Formula: One Field, Many Characters

**Track:** Number Theory from First Principles. **Background:** 016000 (character orthogonality), 035000–036000 (different and discriminants), 036500 (Hilbert's formula), 037250 (Artin conductors). **Aim:** prove the regular-representation conductor identity, derive the abelian local formula, and recover prime-power cyclotomic discriminants by counting character conductors.

<!-- BEGIN SPOKEN LECTURE -->

# The Conductor–Discriminant Formula: One Field, Many Characters

The discriminant belongs to a field extension. A conductor belongs to a representation of its Galois group. These appear to be invariants of entirely different objects. Yet if we take every one-dimensional character of an abelian Galois group and multiply their conductors, we get the absolute discriminant of the field.

We can understand this identity rather than simply memorize it. The crucial observation is that the direct sum of every irreducible character of an abelian group is the regular representation. That representation sees every automorphism. Its conductor therefore measures all ramification, not just the part visible to one character. Hilbert's formula already measures all ramification through the different. The two totals must agree because they are, after a short calculation, the same sum.

We will prove the local identity in full and then use it to recover the ninth- and sixteenth-root discriminants. Finally, we will distinguish the local formula from the global statement for abelian number fields, which uses an additional identification with primitive Dirichlet character conductors.

## The regular representation sees every automorphism

Let L over K be a finite Galois extension of local fields with Galois group G. Form a complex vector space with one basis vector for every element of G. The group acts by left multiplication on those basis vectors: sigma sends the basis vector labeled by tau to the one labeled by sigma times tau. This is the regular representation.

Its dimension is the order of G. If H is a subgroup, what vectors are fixed by every element of H? Consider a vector as a list of complex coefficients indexed by G. Invariance under H says those coefficients must be constant on each left H-coset. Each coset supplies one independent choice. Thus the dimension of the H-fixed subspace is the number of cosets, or the order of G divided by the order of H.

Apply this to each lower ramification group G sub i. The codimension of the fixed space is the order of G minus the order of G divided by the size of G sub i. Substituting that expression into the Artin conductor formula causes a cancellation: multiply by the size of G sub i over the size of inertia, and the result is the order of G over the size of inertia, times the size of G sub i minus one.

That factor is independent of i. Pull it outside the sum. The remaining sum is exactly Hilbert's different formula. We have proved that the Artin conductor exponent of the regular representation equals the order of G divided by the order of inertia, times the different exponent.

The order of G is the ramification index times the residue degree, while the size of inertia is the ramification index. Their ratio is the residue degree f. So the conductor of the regular representation is f times the different exponent d.

But f times d is precisely the valuation in K of the relative discriminant ideal, because that ideal is the norm of the different. We have reached a complete local identity: the regular representation's Artin conductor exponent equals the discriminant exponent.

Nothing about this calculation assumed that the extension was abelian. We used only dimensions of fixed spaces in the regular representation, the definition of the Artin conductor, and Hilbert's different formula.

## Where the characters enter

Now suppose G is abelian. Every irreducible complex representation of a finite abelian group is one-dimensional. There are exactly as many distinct characters as there are elements of G. Character orthogonality tells us that the regular representation decomposes as the direct sum of every character, once each.

We proved that conductor exponents add under direct sums. Therefore the conductor exponent of the regular representation is the sum of the conductor exponents of all the one-dimensional characters. Combining that with the local identity gives the local conductor–discriminant formula: the exponent of the relative discriminant ideal is the sum of the local conductor exponents of all characters of the abelian Galois group.

This argument is quite short once all its ingredients are in place, but every ingredient does work. The regular representation translates a group-size computation into fixed-space dimensions. Hilbert's formula translates the same group sizes into the different. Character orthogonality splits the regular representation into individual contributions. Additivity then makes the field discriminant equal the total character conductor.

A field invariant has become a sum of representation invariants.

## Recover the ninth-root discriminant by character counting

Take L equal to the 3-adic field of primitive ninth roots of unity. The Galois group has six characters. There is one trivial character, whose conductor exponent is zero. There is one nontrivial character factoring through the units modulo three, with conductor exponent one. And there are four primitive characters modulo nine, each with conductor exponent two.

Sum the exponents. We get zero plus one plus four times two, equal to nine. The local discriminant is therefore a power of three with exponent nine. We have recovered exactly the value that the polynomial derivative and the higher ramification groups gave us.

There are three ways to see that same nine. The derivative of the ninth cyclotomic polynomial has valuation nine. Hilbert's formula gives five plus two plus two. The character conductor sum gives one plus four times two. These are not separate mathematical coincidences. The regular-representation computation proves that the last two counts are equivalent, and the derivative proof identifies them with the same trace-theoretic ideal.

## Recover the sixteenth-root discriminant

For the field of primitive sixteenth roots over the 2-adics, the Galois group has eight characters. One has conductor exponent zero. Exactly one character has exact modulus four, two have exact modulus eight, and four have exact modulus sixteen. Their conductor exponents are two, three, and four respectively.

Thus the conductor sum is one times two, plus two times three, plus four times four. The answer is twenty-four. Again this matches Hilbert's sum of seven, seven, three, three, and four ones, as well as the derivative formula for the sixteenth cyclotomic polynomial.

Notice what these examples reveal about the arithmetic of the prime two. There is no nontrivial character of the unit group modulo two, so no character with exact 2-power conductor exponent one. The first ramified character appears at conductor four. This is mirrored by the fact that the whole inertia group survives to G one in a wildly ramified 2-power cyclotomic field.

## A formula for every prime-power cyclotomic field

We can do the conductor calculation without listing characters individually. For modulus p to the n, there are phi of p to the n Dirichlet characters. Those that factor through modulus p to the k are exactly phi of p to the k in number. For k at least one, the number whose exact conductor is p to the k is therefore phi of p to the k minus phi of p to the k minus one. The trivial character has conductor one.

To obtain the exponent of p in the product of all conductors, multiply the number of characters of exact conductor p to the k by k, and sum over k from one to n. A summation-by-parts rearrangement makes this n times phi of p to the n minus the sum of phi of p to the j for j from zero to n minus one. That remaining totient sum is p to the n minus one, because the units of successive prime-power moduli divide the residues into disjoint exact-order layers.

We obtain n times phi of p to the n minus p to the n minus one. This is precisely the prime-power cyclotomic discriminant exponent derived from the derivative and from Hilbert's formula. It holds for odd primes and for two, including the small trivial boundary case.

The conductor calculation is especially revealing because it divides a large discriminant exponent among characters of different minimal moduli. There is one field, but its ramification is being distributed among all possible one-dimensional viewpoints.

## From local exponents to a global discriminant

Let F be a finite abelian number field over the rational numbers. We can attach a group of Dirichlet characters to F by embedding F into a cyclotomic field. The fact that every finite abelian extension of the rationals admits such an embedding is the Kronecker–Weber theorem; we are using that theorem here, not proving it.

For each such character chi, take its primitive conductor, the smallest positive modulus through which it factors. The global conductor–discriminant formula says that the absolute value of the discriminant of F is the product of those positive conductors. The sign of the discriminant is negative one to the number of conjugate pairs of complex embeddings. The sign is separate from the positive character conductors.

Here is how the local proof leads to the global one. Fix a rational prime p and a prime of F above it. Restrict every global Galois character to the local decomposition group. The global regular representation, restricted to that decomposition group, is a direct sum of as many regular local representations as there are primes of F above p. Thus the sum of local character conductor exponents is the correct number of copies of the local discriminant exponent, exactly the contribution of p to the global discriminant.

To identify that local conductor exponent with the exponent of p in a primitive Dirichlet conductor, we use the cyclotomic ramification filtration together with its compatibility under Galois quotients. This identification is standard. We checked it explicitly for prime-power cyclotomic fields; for arbitrary abelian subfields we are invoking the general quotient compatibility theorem from the upper-numbering discussion. The global formula is therefore derived from local calculations subject to that cited theorem and to Kronecker–Weber, not presented as a proof of either prerequisite.

## Two quadratic checks

Take the Gaussian number field, the rationals with a square root of negative one. Its Galois group has two characters: the trivial character of conductor one and the nontrivial character of conductor four. Their product is four. The field discriminant is negative four, so the absolute discriminant agrees exactly.

Take the field obtained by adjoining a square root of five. Its Galois group again has two characters. The nontrivial quadratic character has conductor five. The product of conductors is five, agreeing with the discriminant of the integer basis using one plus square root of five over two.

These examples are small enough to calculate by hand, but they fit the same pattern as the much larger cyclotomic fields. The conductor–discriminant formula is not about the numerical accident that a particular prime occurs to a particular power. It expresses the arithmetic complexity of a field as the sum of all the ramification detected by its characters.

## The next threshold

The formulas here have been proved at a useful level of generality. The regular-representation identity works for every finite Galois extension of local fields. Its character decomposition gives the abelian local conductor–discriminant identity. The cyclotomic examples give complete and explicit character-conductor counts.

The remaining work is structural. We have not proved the general Herbrand quotient theorem, the Kronecker–Weber theorem, or the local reciprocity map identifying all finite abelian local extensions with quotients of the multiplicative group. Those theorems explain why conductors and unit filtrations fit together beyond our explicit cyclotomic calculations. The Hasse–Arf theorem also remains a cited boundary.

For now, we can see the architecture. A local automorphism is measured by how many digits it fixes. Those depths form ramification groups. The groups sum to a different exponent. A representation sees only part of each group, and its conductor weights that part. Summing over all characters recovers the field's full discriminant. A sequence of ideas that began with divisibility of integers has reached a precise bridge between field arithmetic and representation theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `L/K` be finite Galois local, `G=Gal(L/K)`, `e=|G_0|`, `f=|G|/e`, `d=v_L(D_{L/K})`. Let `Reg_G` denote the complex regular representation. For any subgroup `H`,
\[
\dim(\mathrm{Reg}_G)^H=[G:H]=|G|/|H|.
\]
Consequently
\[
\begin{aligned}
a(\mathrm{Reg}_G)&=\sum_{i\ge0}\frac{|G_i|}{|G_0|}\left(|G|-\frac{|G|}{|G_i|}\right)\\
&=\frac{|G|}{|G_0|}\sum_{i\ge0}(|G_i|-1)
=f\,d=v_K(\mathfrak d_{L/K}).
\end{aligned}
\]
When `G` is abelian, `Reg_G` is the direct sum of all distinct one-dimensional characters, each once, hence
\[
\boxed{v_K(\mathfrak d_{L/K})=\sum_{\chi\in\widehat G}a(\chi)}.
\]

For `L=Q_p(zeta_{p^n})`, the number of characters of exact primitive conductor `p^k` is `phi(p^k)-phi(p^(k-1))` for `1<=k<=n`, with `phi(1)=1`. Therefore
\[
\sum_{\chi}v_p(f_\chi)=\sum_{k=1}^n k\big(\varphi(p^k)-\varphi(p^{k-1})\big)
=n\varphi(p^n)-p^{n-1}.
\]

**Global abelian formula:** for an abelian number field `F/Q`, let `X_F` be its associated primitive Dirichlet characters. Using Kronecker–Weber and local character-conductor identification:
\[
|\Delta_F|=\prod_{\chi\in X_F}f_\chi,\qquad
\operatorname{sgn}(\Delta_F)=(-1)^{r_2(F)}.
\]

| Field | Exact character conductors | Absolute discriminant |
|---|---|---|
| `Q(zeta_9)` | `1,3,9,9,9,9` | `3^9` |
| `Q(zeta_16)` | `1,4,8,8,16,16,16,16` | `2^24` |
| `Q(i)` | `1,4` | `4` |
| `Q(sqrt(5))` | `1,5` | `5` |

**Proof boundary:** local regular and abelian conductor identities are proved. For arbitrary global abelian fields, the argument uses the cited Kronecker–Weber and general Herbrand quotient theorems to identify character conductors; neither theorem is proved here.

### Exercises

1. Prove the dimension of the `H`-invariant subspace of the regular representation by counting left cosets.
2. Derive `a(Reg_G)=fd` directly from Artin and Hilbert's formulas without assuming `G` abelian.
3. Use Dirichlet character counts to obtain the different exponent for a primitive twenty-fifth root field.
4. Count primitive characters modulo thirty-two by exact conductor and verify `|disc(Q(zeta_32))|`.
5. Explain why the global signed discriminant needs an archimedean sign beyond the product of positive conductors.

## Sources and reading

- LMFDB, *Conductor of an Artin representation* (reviewed): https://www.lmfdb.org/knowledge/show/artin.conductor
- Romyar Sharifi, *Algebraic Number Theory*, local class field theory and ramification: https://www.math.ucla.edu/~sharifi/notes/algnum-ch09.html
- Hasse and Artin conductor–discriminant identity, encyclopedic statement and literature: https://en.wikipedia.org/wiki/Conductor%E2%80%93discriminant_formula
- Wikipedia: [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character), [Kronecker–Weber theorem](https://en.wikipedia.org/wiki/Kronecker%E2%80%93Weber_theorem), [Cyclotomic field](https://en.wikipedia.org/wiki/Cyclotomic_field).
