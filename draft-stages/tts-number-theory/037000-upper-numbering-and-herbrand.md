# 037000 — Upper Ramification Numbering: A Clock That Respects Quotients

**Track:** Number Theory from First Principles. **Background:** 036250–036750 (lower groups, Hilbert's formula, cyclotomic jumps). **Aim:** construct the Herbrand change of variables, calculate it in cyclotomic towers, and state the precise quotient theorem with its proof boundary.

<!-- BEGIN SPOKEN LECTURE -->

# Upper Ramification Numbering: A Clock That Respects Quotients

When we study one local Galois extension, the lower ramification groups have a clear meaning. Group G sub i contains automorphisms that fix every integer through i plus one powers of a uniformizer. The index i counts digits in the largest field, and Hilbert's different formula turns those groups into the exponent of the different.

But suppose we study several fields in a tower. The units of measurement change from field to field, because each field has its own normalized valuation. A difference with valuation eight in a large, highly ramified field may have valuation four in a smaller one. A lower index is therefore tied to the field in which it is measured. It behaves well when we restrict automorphisms to a subgroup, but not generally when we pass to a quotient Galois group.

The remedy is to build a new clock. We will slow down the clock when many automorphisms survive and speed it up when few survive, in just the proportion needed for the quotient theory. Its time is called upper numbering. We can calculate it with an integral of group sizes, and in cyclotomic towers its jumps become strikingly simple.

## Why subgroup behavior is easy

Let L over K be a finite Galois extension and let H be a subgroup of its Galois group. The fixed field of H lies between L and K. The extension L over that fixed field uses the same top field L, the same integers, and the same normalized valuation. The test that an element fixes every integer modulo pi to a given power is exactly the same test. Therefore its lower ramification groups are the intersections of H with the lower ramification groups of L over K.

This is an exact compatibility rule. It requires no index adjustment. We have retained the top field and merely restricted which automorphisms we consider.

If instead we pass from L to an intermediate field M that is Galois over K, we replace the top field. Its uniformizer may have a different valuation in L, and applying the quotient map to G sub i generally does not produce the group of M over K with the same lower index. We need a different scale.

## Extend the index from integers to real numbers

The lower filtration has integer indices. To change its scale, imagine that each group stays constant between successive integer indices, using the group G sub one on the open interval just above zero through one, G sub two from just above one through two, and so forth. At zero itself we use inertia G zero. Endpoint conventions matter only at jumps, and we will state our convention in the mathematical companion.

Define a function phi of t, for nonnegative t, by integrating from zero to t the ratio of the size of G sub s to the size of inertia G zero. In ordinary words, the speed of this new clock is the fraction of inertia still present at the current lower level. This fraction is positive and at most one. The function starts at zero, increases continuously, and is piecewise linear. Once every nonidentity automorphism has disappeared, the group has size one and the clock continues at a constant positive rate.

We extend phi to the interval from minus one to zero by setting phi of t equal to t. The function is strictly increasing and tends to infinity. It therefore has an inverse, traditionally called psi. The upper group at time u is defined as the lower group at time psi of u. We write it G superscript u to distinguish it from lower G sub i.

These definitions may look like notation for its own sake. Their purpose is that the upper filtration, unlike the lower one, behaves well with Galois quotients. That fact is Herbrand's theorem. We will state it precisely after seeing the calculation that motivates it.

## Rescale the ninth-root example

For the field obtained by adjoining a primitive ninth root of unity to the 3-adics, inertia has six members. The group immediately after lower time zero has three members. That group persists through lower time two. Therefore the new clock runs at half speed for its first two lower units: phi of t equals t divided by two for t between zero and two. At lower time two, upper time is one.

After that, the only surviving automorphism is the identity. The clock runs at one sixth of the original speed, because the ratio is one over six. The nontrivial upper filtration has a single positive jump at upper time one. More concretely, for upper times greater than zero but at most one, the group has three members; above one it is trivial. At upper time zero, the group still has all six members.

The lower jump occurred at two; the upper jump occurs at one. The tame part is separated immediately at time zero. The wild part lasts for one unit in the adjusted clock.

## Rescale the sixteenth-root example

For a primitive sixteenth root over the 2-adics, inertia has eight elements. Its lower groups have size eight at indices zero and one; size four at indices two and three; size two at indices four, five, six, and seven; and size one at index eight onward.

Between lower times zero and one, the clock runs at full speed, since all eight elements survive. Thus phi of one is one. Between one and three, half of inertia survives, so two more lower units contribute one upper unit. Thus phi of three is two. Between three and seven, a quarter of inertia survives, so four lower units contribute another upper unit. Thus phi of seven is three.

The large lower jumps at one, three, and seven have become upper jumps at one, two, and three. This is not a numerical coincidence. In the general 2-power cyclotomic tower, the lower jumps grow like successive powers of two minus one, but the upper jumps lie at successive integers. For odd primes, a similar rescaling takes the lower jumps at p minus one, p squared minus one, and onward to upper jumps one, two, and onward.

Why does this matter? Suppose we pass from the sixteenth-root field to the eighth-root field. The quotient Galois group forgets the distinction between automorphisms that differ only modulo sixteen. The sixteenth-root field has upper jumps one, two, and three, while the eighth-root field has only one and two. The final upper layer lies in the kernel of the quotient, so it disappears exactly where it should. The earlier layers project to the corresponding upper layers of the smaller field.

## Herbrand's quotient theorem

Here is the general statement. Suppose L over K is finite Galois, and H is a normal subgroup of G. Let M be the fixed field of H, so M over K is also Galois. At every upper index u, the image of G superscript u under the quotient map to G modulo H is exactly the upper ramification group of M over K at that same u.

The same-index clause is the important part. Ordinary quotient groups always exist. Herbrand's theorem says that the upper filtration commutes with them: take the upper group and then pass to the quotient, or pass to the quotient field and then take its upper group, and you get the same result.

This is a substantial general theorem. Our construction of phi alone does not prove it; the proof requires comparing ramification indices of lifts of automorphisms through the fixed-field tower. We are recording it as a cited theorem here. What we can prove directly, using our explicit cyclotomic formula, is the full quotient compatibility for the chain of prime-power cyclotomic fields. In those fields the quotient maps are reduction of unit classes modulo a smaller power of p, and the upper groups are exactly the congruence subgroups at corresponding powers of p. Reducing those congruences gives the predicted groups.

The distinction between proving the cyclotomic instance and citing the general quotient theorem is important. The cyclotomic calculation illustrates and verifies the theorem in a rich infinite family; it is not a replacement for a proof for every finite Galois local extension.

## What Hasse–Arf adds

In our examples, the upper jumps are integers. You may wonder whether upper jumps must always be integers. The answer is no for arbitrary Galois groups: nonabelian extensions can have fractional upper breaks. But for an abelian extension of local fields with finite residue field, the Hasse–Arf theorem says all upper ramification breaks are integers.

We will not prove Hasse–Arf here. Its proof requires more than the change-of-variables definition, and it can be approached through characters and conductors. We now have the motivation for that approach. Characters of an abelian Galois group see each step of the upper filtration, and their conductors record the last nontrivial layer. Integrality of the resulting conductor exponents is connected to integrality of the upper breaks.

## The two clocks serve different tasks

Lower numbering remains the right language for Hilbert's different formula. The sum of lower group sizes minus one is directly an integer valuation of the different. Lower numbering is also simple when restricting automorphisms to a subgroup that fixes an intermediate field.

Upper numbering is the right language for quotient fields and ramification conductors. Its speed depends on how much of inertia survives, so it compensates for the changing valuation scale in towers. In our cyclotomic examples, upper time records the number of nontrivial prime-power congruence stages, rather than their exponentially growing lower depths.

There is no reason to throw away either description. They represent the same filtration at different resolutions. The lower clock measures p-adic accuracy in the largest field. The upper clock measures ramification in a scale stable under Galois quotient maps. With both clocks available, we can ask a more refined question: what does a particular representation of the Galois group detect, and how much ramification does it contribute to an arithmetic invariant?

That question leads to Artin and Swan conductors.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For finite Galois `L/K`, extend the lower filtration by `G_t=G_ceil(t)` for `t>0` and `G_0` at `t=0`, and set
\[
\varphi_{L/K}(t)=\int_0^t\frac{|G_s|}{|G_0|}\,ds\quad(t\ge0),
\qquad \varphi(t)=t\quad(-1\le t\le0).
\]
This is continuous strictly increasing; put `psi=phi^{-1}` and `G^u=G_{psi(u)}`. Lower numbering respects subgroups: `H_i=H cap G_i` using valuations in the same field L.

**Herbrand quotient theorem (cited, not proved generally here):** for `H normal in G`, `M=L^H`,
\[
\boxed{(G/H)^u=G^uH/H.}
\]
The lecture proves this compatibility explicitly for cyclotomic quotient towers via congruence subgroups.

| Extension | lower breaks | positive upper breaks |
|---|---|---|
| `Q_3(zeta_9)/Q_3` | 2 | 1 |
| `Q_2(zeta_8)/Q_2` | 1,3 | 1,2 |
| `Q_2(zeta_16)/Q_2` | 1,3,7 | 1,2,3 |
| `Q_p(zeta_{p^n})/Q_p`, `n>=2` | `p^k-1`, `1<=k<n` | `k`, `1<=k<n` |

`Hasse-Arf (cited, not proved):` in finite abelian local extensions, upper breaks are integers; this need not hold for nonabelian extensions.

### Exercises

1. Calculate `phi(t)` piecewise for `Q_3(zeta_9)/Q_3`, including the segment after the last break.
2. Calculate `phi(1), phi(3), phi(7)` for `Q_2(zeta_16)/Q_2`.
3. Verify quotient compatibility for the reduction `(Z/16Z)^× -> (Z/8Z)^×` at each upper interval.
4. Check the `p^k-1` to `k` rescaling for `Q_5(zeta_125)`.
5. Explain why an arbitrary same-index lower quotient rule cannot be assumed simply from the filtration definition.

## Sources and reading

- Leonard Tomczak, *Local Fields*, upper numbering and Herbrand quotient theorem: https://math.berkeley.edu/~ltomczak/notes/Mich2022/LF_Notes.pdf
- Kiran S. Kedlaya, *Local Fields*, Herbrand-function comparison: https://kskedlaya.org/math201a-win10/math201a.pdf
- Romyar Sharifi, *Algebraic Number Theory*, section 9.6: https://www.math.ucla.edu/~sharifi/notes/algnum-ch09.html
- Wikipedia: [Ramification group](https://en.wikipedia.org/wiki/Ramification_group), [Hasse–Arf theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Arf_theorem).
