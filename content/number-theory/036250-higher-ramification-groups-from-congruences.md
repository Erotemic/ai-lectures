# 036250 — Higher Ramification Groups: How Closely an Automorphism Fixes an Integer

**Track:** Number Theory from First Principles. **Background:** 030750 (p-adic integers), 031750–032000 (local extensions and Eisenstein generators), 035250 (tame and wild different). **Aim:** construct the lower filtration and prove its inertia and tame/wild properties without treating the groups as an unexplained definition.

<!-- BEGIN SPOKEN LECTURE -->

# Higher Ramification Groups: How Closely an Automorphism Fixes an Integer

An automorphism of a number field can move an element without moving it very far. In an ordinary absolute value, this sounds paradoxical: either a number changes or it does not. In a p-adic field, a change can be divisible by the prime once, twice, ten times, or a hundred times. The more divisible the change, the smaller its p-adic size. We can use that observation to measure an automorphism, not by whether it fixes an element exactly, but by how many digits of every algebraic integer it fixes.

That is what a higher ramification group does. The first such group records which automorphisms leave the residue field alone. Deeper groups record successively stronger congruences. The first layer detects ordinary ramification; the deeper layers detect its wild portion. The surprising conclusion is that these deeper symmetries are compelled to be groups of prime-power order.

## A finite extension and its residue field

Let K be a finite extension of the p-adic numbers, and let L over K be a finite Galois extension. Write G for its finite group of K-automorphisms. The ring of integers of L consists of elements with nonnegative valuation. Its unique maximal ideal consists of elements with positive valuation. We choose the normalized valuation on L so that a uniformizer pi has valuation one. Reduction modulo the maximal ideal gives a finite residue field, which we will call little k of L.

Every automorphism in G preserves the valuation. It must preserve the ring of integers and its maximal ideal, so it induces an automorphism of the residue field. This gives a homomorphism from G to the Galois group of the residue-field extension. Its kernel is inertia, conventionally called G zero. A member of inertia may still move an integer, but its movement is always divisible by pi. Put another way, inertia consists exactly of the automorphisms that act as the identity modulo pi on every integral element.

We also name the whole Galois group G minus one. This is an indexing convention, not subtraction. It permits us to see both residue-field automorphisms and ramification in one descending sequence: G minus one contains G zero, and G zero will contain still smaller groups.

## Measuring the first changed digit

For a nonidentity automorphism sigma, consider the smallest valuation of sigma of x minus x as x runs over every algebraic integer of L. Call that number i of sigma. Because the values are nonnegative integers, the minimum exists. If sigma is the identity, set i of sigma equal to infinity.

Why minimize over all integers? If we tested just one arbitrarily chosen number, a sigma might happen to fix it. Testing every integer gives a property of the automorphism itself. If sigma moves some residue class, we can choose an integer whose difference has valuation zero, so i of sigma is zero. If sigma fixes the residue field, all the differences have valuation at least one, so i of sigma is at least one.

Now define G sub i, for an integer i at least zero, to consist of those sigma with i of sigma at least i plus one. Thus G zero fixes every integer modulo the first power of pi. G one fixes every integer modulo pi squared. G two fixes every integer modulo pi cubed, and so on. The condition becomes increasingly strong. Since G is finite and no nonidentity sigma fixes every integer exactly, the groups eventually become trivial.

These are genuinely groups, not arbitrary sets. If two automorphisms fix every integer modulo pi to a chosen power, their composition does too: subtract the original integer after applying the two maps and use the ultrametric inequality. The inverse has the same property, by applying it to an appropriately moved integer. Conjugation preserves the condition because automorphisms preserve valuations and permute the integral elements. Consequently every G sub i is a normal subgroup of the entire Galois group.

## Why a uniformizer is enough inside inertia

The definition appears to demand an impossible amount of checking, one test for every integral element. We can reduce it to a single number. Let K nought be the maximal unramified intermediate field of L over K. Its automorphism-fixed group is inertia. The extension L over K nought is totally ramified, and the uniformizer pi generates its integer ring as an algebra: every algebraic integer in L is a polynomial in pi with coefficients in the integers of K nought.

For sigma in inertia, the coefficients of that polynomial are fixed. The difference between its values at sigma of pi and pi is divisible by sigma of pi minus pi, by the elementary factorization of a difference of polynomial values. Thus every difference sigma of x minus x has valuation at least the valuation of sigma of pi minus pi. Equality is obtained by choosing x equal to pi itself. Therefore, for sigma in inertia, i of sigma is precisely the valuation of sigma of pi minus pi.

This one calculation is the working form of the filtration. We must keep its hypothesis: outside inertia, the automorphism can act nontrivially on residue-field coefficients, and testing a uniformizer alone need not detect that action. This is why we began with an intrinsic definition.

## The first quotient is multiplicative

Consider sigma in inertia. Both pi and sigma of pi are uniformizers, so their quotient is a unit. Reduce sigma of pi divided by pi modulo the maximal ideal. We obtain a nonzero element of the residue field. The assignment from sigma to this residue class is a group homomorphism on inertia, because inertia acts trivially on the residue field.

What is its kernel? The quotient is congruent to one exactly when sigma of pi minus pi is divisible by pi squared. That is precisely membership in G one. So G zero modulo G one embeds into the multiplicative group of the finite residue field.

The multiplicative group of a field with q elements has q minus one elements. Since q is a power of p, q minus one is not divisible by p. Therefore the quotient of inertia by G one has order prime to p. This is the tame part of inertia. If there is no deeper subgroup G one, all inertia is tame.

## The deeper quotients are additive

Now suppose i is at least one, and sigma belongs to G sub i. Divide sigma of pi minus pi by pi to the i plus one, and reduce the quotient modulo pi. This time the answer is allowed to be zero. Its kernel consists of automorphisms for which the difference is divisible by one further power of pi: exactly G sub i plus one.

The assignment is additive modulo pi. To see why, write the action of sigma on pi as pi plus a multiple of pi to the i plus one. Do the same for tau, compose the substitutions, and discard terms divisible by pi to the i plus two. Because i is positive, the cross-terms are too highly divisible to survive. The surviving coefficient is the sum of the two original coefficients. Thus G sub i modulo G sub i plus one embeds into the additive group of the residue field.

The additive group of a field of characteristic p has exponent p. Every deeper quotient is therefore an elementary abelian p-group. Since the filtration ends in the identity, building upward shows that G one itself is a p-group. We call G one the wild inertia subgroup.

This proves a structural assertion, not merely a vocabulary rule: wild inertia is a p-group because its successive changes of p-adic digits live in additive groups of characteristic p.

## A first explicit test

Let L be the field obtained from the 3-adic rationals by adjoining a primitive ninth root of unity, zeta. The extension has degree six. Its local uniformizer is zeta minus one. A Galois automorphism is determined by sending zeta to zeta to the a, where a is one of the six invertible residue classes modulo nine.

Take the automorphism with a equal to two. Its difference on the uniformizer is zeta squared minus zeta, which is a unit times zeta minus one. That difference has valuation one. So the automorphism is in G zero but not G one.

Now take a equal to four. The difference is zeta to the fourth minus zeta, a unit times zeta cubed minus one. The cube of a primitive ninth root is a primitive third root. Inside the ninth-root field, one minus that third root has valuation three. So this automorphism fixes every integer modulo pi cubed, but not modulo pi to the fourth. It belongs to G zero, G one, and G two, but not G three.

The entire group will have six automorphisms at level zero, three at levels one and two, and only the identity at level three. We will calculate this precisely in a worked cyclotomic lecture. Already we can see the story: some automorphisms stop moving the residue classes, some even stop moving the next two pi-adic digits, and their different rates of movement record the depth of wild ramification.

## What the filtration is for

In a tame totally ramified extension, only the first nontrivial layer survives. The next group is the identity. In a wild extension, G one is nontrivial, and the chain may persist for several levels. The length and sizes of those layers are numerical information. They turn out to compute the exponent of the different ideal exactly, without any approximate estimate.

It is worth remembering the distinctions we have proved. The full Galois group also sees the unramified residue extension. Inertia is the kernel of the residue action. The tame quotient of inertia is multiplicative. Wild inertia and its deeper quotients are governed by additive residue-field arithmetic. A valuation turns an apparently qualitative question—does sigma move this number?—into a finely graded measurement of how far it moves it.

That measurement is the foundation for the formula connecting wild symmetry with discriminant exponents.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `L/K` be finite Galois local with group `G`, uniformizer `pi` in `L`, normalized `v_L(pi)=1`, and residue field `k_L` of cardinality `q=p^f`.

For nonidentity `sigma` put
\[
i_G(\sigma)=\min_{x\in\mathcal O_L}v_L(\sigma x-x),\quad i_G(1)=\infty,
\qquad G_{-1}=G,\quad G_i=\{\sigma: i_G(\sigma)\ge i+1\}\;(i\ge0).
\]

- `G_0` = inertia = kernel of `G -> Gal(k_L/k_K)`.
- For `sigma in G_0`, the maximal unramified subfield `K_0` satisfies `O_L=O_{K_0}[pi]`, hence `i_G(sigma)=v_L(sigma(pi)-pi)`.
- `G_i` is normal in `G` and eventually trivial.
- The multiplicative homomorphism `G_0 -> k_L^×`, `sigma |-> overline{sigma(pi)/pi}`, has kernel `G_1`; thus `|G_0/G_1|` divides `q-1`.
- For `i>=1`, `G_i -> (k_L,+)`, `sigma |-> overline{(sigma(pi)-pi)/pi^{i+1}}`, has kernel `G_{i+1}`. Hence `G_i/G_{i+1}` is an elementary abelian p-group and `G_1` is a finite p-group.

For `L=Q_3(zeta_9)`, `pi=zeta_9-1`, `i_G(sigma_a)=v_L(zeta_9^{a-1}-1)`. The nonidentity values are: `i(2)=i(5)=i(8)=1`, `i(4)=i(7)=3`.

### Exercises

1. Prove directly that the congruence condition for `G_i` is stable under conjugation.
2. Verify the kernel of `sigma |-> overline{sigma(pi)/pi}` is exactly `G_1`.
3. In the additive quotient argument, calculate the error term for `sigma(tau(pi))` through order `pi^{i+2}`.
4. In `Q_5(zeta_5)`, show all nonidentity automorphisms have displacement valuation one. Identify `G_0` and `G_1`.
5. Explain why the uniformizer-only test can fail for a residue-field automorphism in an unramified extension.

## Sources and reading

- Kiran S. Kedlaya, *Math 201A: Local Fields*, sections on ramification filtrations: https://kskedlaya.org/math201a-win10/math201a.pdf
- Leonard Tomczak, *Local Fields lecture notes* (based on Rong Zhou's course), ramification groups: https://math.berkeley.edu/~ltomczak/notes/Mich2022/LF_Notes.pdf
- Romyar Sharifi, *Algebraic Number Theory*, local ramification chapters: https://www.math.ucla.edu/~sharifi/notes/algnum-ch06.html
- Wikipedia: [Ramification group](https://en.wikipedia.org/wiki/Ramification_group), [Inertia group](https://en.wikipedia.org/wiki/Inertia_group).
