# 037250 — Artin and Swan Conductors: Ramification Seen by a Representation

**Track:** Number Theory from First Principles. **Background:** 016000 (finite-group characters), 036250–037000 (lower and upper ramification). **Aim:** define conductor exponents, derive their basic algebra, and calculate character conductors in explicit local cyclotomic fields.

<!-- BEGIN SPOKEN LECTURE -->

# Artin and Swan Conductors: Ramification Seen by a Representation

Two different equations may describe the same field extension but respond differently to its ramification. One equation might involve all the Galois automorphisms. Another might involve only a one-dimensional character, a rule assigning a complex root of unity to each automorphism. That character can be insensitive to an entire subgroup. If we want an arithmetic invariant attached to a representation, we should measure only the ramification that the representation actually detects.

This is the idea of an Artin conductor. The higher ramification groups tell us how long automorphisms continue to fix p-adic digits. A representation tells us whether those automorphisms act trivially on a vector space, or whether they genuinely move some vectors. The conductor combines the depth of the group with the number of independent directions that it moves.

The part measured at the initial inertia group is the tame contribution. The remaining part is the Swan conductor, measuring wild ramification. We will define both, prove their elementary properties, and use the ninth- and sixteenth-root fields as explicit examples.

## From a Galois group to a vector space

Let L over K be a finite Galois extension of local fields with residue characteristic p. Write G for its Galois group and G sub i for its lower ramification groups. A finite-dimensional complex representation rho assigns to every sigma in G an invertible linear map of a complex vector space V, in a way compatible with multiplication in G.

For a subgroup H of G, define V fixed by H to be the vectors that every element of H leaves unchanged. It is a linear subspace. Its codimension is the dimension of V minus the dimension of that fixed subspace. This codimension is zero exactly when H acts trivially on all of V. If H moves one independent direction, the codimension is at least one; if it moves every direction with no common fixed vector, the codimension is the whole dimension.

Every lower group gives us a fixed subspace. As the groups shrink, those subspaces can only grow. Eventually the ramification groups are trivial and every vector is fixed. Thus only finitely many groups can contribute to a sum of codimensions.

## Define the Artin conductor exponent

The local Artin conductor exponent is the sum, over i from zero onward, of the codimension of the vectors fixed by G sub i, multiplied by the size of G sub i divided by the size of G zero. The weighting is important. At level zero, the ratio is one. At deeper levels it is the fraction of inertia that survives at that depth.

Separate the first term. The codimension of the inertia-fixed subspace is the tame contribution. The remaining weighted sum over i at least one is called the Swan conductor. Thus the Artin conductor is the tame contribution plus the Swan conductor.

Both quantities are visibly nonnegative. The Swan conductor vanishes if wild inertia acts trivially on the representation. That can happen even in a wildly ramified field extension, because the representation may factor through a quotient in which the wild part disappears. Conversely, a nonzero Swan conductor certifies that the representation detects genuinely wild ramification.

A representation of a completely unramified extension may be nontrivial: a Frobenius automorphism can act by a nontrivial matrix. But its inertia group is trivial, so its Artin conductor is zero. A conductor does not measure every kind of Galois action. It measures ramification, not the unramified Frobenius action.

## Why the formula is compatible with direct sums

Suppose V is a direct sum of two G-stable spaces, corresponding to representations rho one and rho two. The vectors fixed by any subgroup are precisely the direct sum of the fixed subspaces in the two pieces. Dimensions and codimensions add. Multiply by each weight and sum: the conductor of the direct sum is the sum of the two conductors. The same argument works separately for the Swan parts.

We can check fixed-space dimensions without choosing a basis adapted to every subgroup. For a finite subgroup H, average the representation matrices over H, dividing by the order of H. This averaging operator is a projection onto the H-fixed subspace. It acts as the identity on fixed vectors and kills an invariant complement. Its trace is therefore exactly the dimension of V fixed by H. This observation connects conductors to character theory: the dimension of fixed vectors is the average of the character values over H.

These facts are elementary consequences of the definition. The general theorem that the Artin conductor exponent is an integer, even for representations of nonabelian Galois groups, is deeper. We record that integrality theorem as an external result rather than pretending it follows just from seeing rational weights in the sum. For one-dimensional characters of our cyclotomic examples we can compute the exponents explicitly and see the integers for ourselves.

## One-dimensional characters simplify the formula

Now take V to be one-dimensional. The representation is a character chi mapping G into complex roots of unity. For any subgroup H, the fixed space is all of V when chi is trivial on H and zero when chi is nontrivial on H. So the codimension is either zero or one.

The conductor exponent is then the sum of the group-size ratios over exactly those lower groups on which the character remains nontrivial. Since the groups descend, there is a last level at which a given ramified character sees something. For an unramified character there is no contributing level, and its conductor exponent is zero. A nontrivial character of inertia that is already trivial on G one has conductor exponent one: it is tamely ramified.

Suppose a character is nontrivial on G zero and its last nontrivial lower group is G sub b, where b is at least one. Its exponent is one plus the sum, over i from one through b, of the size of G sub i divided by the size of inertia. But that sum is precisely the Herbrand function phi evaluated at b, with our piecewise-linear convention. So for a ramified one-dimensional character, the conductor exponent is one plus its final upper ramification break.

This is the link between character conductors and upper numbering. The conductor sees the last stage on which a character still notices the Galois action, measured on the clock that respects quotient fields.

## Three kinds of characters in the ninth-root field

Consider once more the primitive ninth-root field over the 3-adics. Its Galois group is the six-element group of units modulo nine. Inertia is the whole group. Its lower groups have sizes six at level zero, three at levels one and two, and one thereafter.

The trivial character has conductor exponent zero. A character that is nontrivial on the six-element group but trivial on the three-element wild subgroup sees only G zero. Its exponent is one. This is the nontrivial character of the tame quotient of order two. It corresponds to the nontrivial character of the units modulo three.

There are also characters that remain nontrivial on the order-three wild subgroup. For each such character, the conductor sum is one plus three over six plus three over six. That is two. In the language of Dirichlet characters, these are the four characters modulo nine with exact conductor nine. The tame character has exact conductor three, so its conductor exponent is one. The exponents are not arbitrary labels: they are the powers of three in those minimal moduli.

Notice the Swan contribution for the wildly ramified characters. It is the sum of the two one-half weights, equal to one. Their total Artin conductor exponent is two: one tame unit plus one wild unit. The word tame here refers to the level-zero contribution, even though the underlying representation is itself wildly ramified.

## Why the prime two starts at exponent two

In the field of sixteenth roots of unity over the 2-adics, the first two ramification groups are equal: G zero equals G one, both of size eight. Every ramified character is therefore nontrivial at both of these levels. Its Artin conductor exponent is at least one plus one, or two. There is no character of exact conductor two among characters of the units modulo sixteen, because the group of units modulo two is trivial.

A character that becomes trivial after G one has exponent two and factors through the units modulo four. A character nontrivial through G three but trivial on G four has exponent one plus one plus one-half plus one-half, equal to three; its exact modulus is eight. A character that remains nontrivial through G seven has exponent four; its exact modulus is sixteen.

This gives the possible conductor exponents zero, two, three, and four, and explains why a primitive character modulo sixteen has exponent four. The weighted lower sum measures exactly how deep the character survives in the higher congruence filtration.

## What a conductor says, and what it leaves open

The definition already tells us which pieces of ramification a representation can detect. It is additive under direct sums, vanishes when inertia acts trivially, and separates tame from wild action. For abelian cyclotomic extensions, it reduces to a calculation with characters and congruence subgroups. The resulting exponents agree with the familiar minimal moduli of Dirichlet characters.

There are broader claims here that we have not proved. General integrality of Artin conductors, the Hasse–Arf theorem, and the compatibility with local reciprocity for all abelian local extensions require deeper arguments. Nor have we built the full representation-theoretic ramification theory of arbitrary nonabelian fields.

But we can already do something significant with the definition: sum the conductors of every character in an abelian Galois group. Because the characters form the regular representation when taken together, their total conductor must agree with a quantity computed from all the ramification groups at once. That quantity will turn out to be the discriminant exponent. This is the conductor–discriminant formula, the next goal.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a finite complex representation `rho:G->GL(V)` of a finite Galois local extension, define
\[
a(\rho)=\sum_{i\ge0}\frac{|G_i|}{|G_0|}\,\operatorname{codim}V^{G_i},\qquad
\operatorname{Sw}(\rho)=\sum_{i\ge1}\frac{|G_i|}{|G_0|}\,\operatorname{codim}V^{G_i}.
\]
Then `a(rho)=codim V^{G_0}+Sw(rho)`, and both invariants are additive under direct sums. For each subgroup `H`, the averaging idempotent
\[
P_H=\frac1{|H|}\sum_{h\in H}\rho(h),\quad \operatorname{tr}(P_H)=\dim V^H.
\]
For a one-dimensional ramified character `chi`, with last nontrivial lower group `G_b`,
\[
a(\chi)=1+\sum_{i=1}^b\frac{|G_i|}{|G_0|}=1+\varphi(b).
\]
If `chi` is unramified, `a(chi)=0`; if tame nontrivial, `a(chi)=1`.

| `L/K` | Type of one-dimensional character | `a(chi)` | `Sw(chi)` |
|---|---|---:|---:|
| `Q_3(zeta_9)/Q_3` | trivial | 0 | 0 |
| same | tame, factors mod 3 | 1 | 0 |
| same | primitive mod 9 | 2 | 1 |
| `Q_2(zeta_16)/Q_2` | factors through mod 4, nontrivial | 2 | 1 |
| same | exact conductor 8 | 3 | 2 |
| same | exact conductor 16 | 4 | 3 |

**Proof boundary:** Integrality of the general nonabelian Artin conductor and general Hasse–Arf are cited theorems. Additivity and all tabulated cyclotomic formulas are derived directly here.

### Exercises

1. Prove `P_H` is an idempotent and its image is `V^H`.
2. Show conductor and Swan conductor are additive on direct sums.
3. Compute the conductor for a one-dimensional character that is trivial on inertia but nontrivial on Frobenius.
4. Verify all character-conductor exponents for ninth roots from the group sizes `6,3,3,1`.
5. Explain why a ramified character in `Q_2(zeta_16)` must have conductor exponent at least two.

## Sources and reading

- LMFDB, *Conductor of an Artin representation* (reviewed by Sutherland, Jones, and Booker): https://www.lmfdb.org/knowledge/show/artin.conductor
- Romyar Sharifi, *Algebraic Number Theory*, ramification and Artin conductors: https://www.math.ucla.edu/~sharifi/notes/algnum-ch09.html
- Kiran S. Kedlaya, *Local Fields*, ramification filtrations: https://kskedlaya.org/math201a-win10/math201a.pdf
- Wikipedia: [Artin conductor](https://en.wikipedia.org/wiki/Artin_conductor), [Swan conductor](https://en.wikipedia.org/wiki/Swan_conductor).
