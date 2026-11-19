# 037500 — Évariste Galois II: Prison, the Chevalier letter, and the afterlife of an idea

**Track:** History · People and ideas. **Theme:** republican politics, manuscripts, radical solvability, and Galois groups. **Background:** elementary algebra and the root-permutation examples in Part I.

<!-- BEGIN SPOKEN LECTURE -->

In May eighteen thirty-one, Évariste Galois joined a republican dinner celebrating the acquittal of National Guard artillery officers charged with conspiracy. During a toast to the new king, Louis-Philippe, he held a knife, and accounts describe the words and gesture as threatening. He was arrested, tried, and acquitted in June. This was not merely adolescent theater detached from political risk. The July Revolution had created a monarchy that relied on suppressing some of the republicans who had helped to bring down its predecessor.

A second arrest followed a republican demonstration on Bastille Day, July fourteenth. Galois was accused of offenses involving a prohibited uniform and weapons. He was eventually convicted and remained confined in Sainte-Pélagie prison. He was still not twenty. The political story is sometimes compressed into the phrase revolutionary mathematician, as though a label explained a life. Here it meant police, courts, loss of freedom, and the practical question of how to keep working when one could not freely visit teachers, collaborators, or libraries.

Before that second arrest, on July fourth, the Academy of Sciences had issued a negative report on a memoir Galois had sent in January. Siméon-Denis Poisson and Sylvestre-François Lacroix found the exposition insufficient for a confident judgment. There is a difference between failing to understand a novel idea and refusing to consider a fully demonstrated theorem. Galois had good reason to be frustrated by repeated obstacles. The academicians also had an obligation to ask for an argument other specialists could follow. A productive historical account need not make either side a caricature.

Accounts of his imprisonment describe loneliness, confrontations, drinking, and severe distress, including a reported attempt at self-harm. These reports should be treated as evidence of suffering in confinement, not as a romantic explanation for creative thought. Even in prison he remained connected to political and mathematical conversations outside its walls. His closest associates were not mythical witnesses to a solitary flash of inspiration. They were people who could receive messages, preserve manuscripts, and eventually put work into print.

In March eighteen thirty-two a cholera epidemic swept Paris. Galois was moved from Sainte-Pélagie to a private establishment that housed some prisoners. There he became involved with Stéphanie-Félicie du Motel, and surviving fragments of correspondence suggest an unhappy and complicated attachment. The evidence does not firmly establish what caused the duel in which he was shot. Accounts differ about political motives, romantic jealousy, and the identities and intentions of those involved. Treating any one conjecture as the settled explanation would give us more dramatic certainty than the records contain.

The duel took place on May thirtieth. Wounded, Galois died the next day, May thirty-first, eighteen thirty-two, at twenty years old. The night before the duel, he had written to Auguste Chevalier, a trusted friend in his political and intellectual circle. The letter summarized discoveries and asked that qualified mathematicians judge their importance. It was a serious act of communication and preservation. It was not the occasion on which the whole mathematical theory was suddenly invented. The papers that matter most had histories stretching back through eighteen twenty-nine, eighteen thirty, and eighteen thirty-one.

Chevalier published the letter later in eighteen thirty-two and safeguarded the papers. In eighteen forty-three he passed manuscripts to Joseph Liouville, who presented an edition in eighteen forty-six. The fourteen-year interval between Galois's death and that publication matters: mathematical reputations are made through editors, readers, teachers, and subsequent reconstructions. Camille Jordan's systematic development of permutation groups in eighteen seventy helped make the new algebra part of an accessible research tradition. Peter Neumann's later work with Galois's surviving manuscripts also reminds us that a printed edition is an editorial interpretation of crossings-out, additions, unfinished pages, and different versions.

Seen through this chain of witnesses, Galois was not an anonymous victim of institutions that later discovered a treasure. He was a talented and often difficult young man who found supporters as well as critics, wrote some work clearly enough for publication, and left other work in forms that could not be immediately assimilated. His circumstances were shaped by the restored monarchy, the July Revolution, an intensely hierarchical system of education, and a mathematical community wrestling with questions inherited from the eighteenth century.

We can now examine more closely the mathematics that passed through those relationships and manuscripts. The longer account follows modern algebraic language where it is useful. In particular, speaking of splitting fields, automorphism groups, normal-subgroup chains, or the complete Galois correspondence is a retrospective way to develop and teach ideas whose nineteenth-century formulations were not identical to ours.

We begin with a brief reminder of the problem. A polynomial equation has several roots, and the coefficients impose algebraic relationships among them. Gather the roots into the smallest field containing the original coefficients and all the roots. Its symmetries, the field automorphisms fixing the coefficients, can permute the roots only when every arithmetic relation is preserved. Because these operations compose and can be reversed, they form a group. Galois used permutations to study the possibilities for solving equations. The modern field-theoretic formulation helps us explain his insights precisely, but it must not be mistaken for a word-for-word reconstruction of his manuscripts.

Galois also developed mathematics beyond the theory of equations. In eighteen thirty Galois published on the theory of numbers, describing what we now recognize as important steps toward finite-field theory. This is another side of his achievement. Arithmetic modulo a prime behaves like arithmetic in a small field. For example, modulo five, the numbers zero through four can be added and multiplied, and every nonzero number has a multiplicative inverse. More surprisingly, there are fields with four, eight, nine, and other prime-power numbers of elements. Their structure can be understood through polynomial equations over smaller fields.

To see the idea, work modulo two, so one plus one equals zero. Consider the polynomial t squared plus t plus one. It has no root among zero and one, because substituting either gives one. We can therefore introduce a new symbol alpha satisfying alpha squared plus alpha plus one equals zero. In characteristic two, that says alpha squared equals alpha plus one. The resulting field has four elements: zero, one, alpha, and alpha plus one. Multiplication simplifies using alpha squared equals alpha plus one. This concrete construction shows how adjoining a root creates a larger arithmetic universe with its own symmetries.

In that four-element field, squaring is itself an automorphism. It leaves zero and one fixed, sends alpha to alpha squared, and sends alpha squared back to alpha. The reason is that squaring respects addition in characteristic two: the cross term two a b vanishes. In general, raising to the p-th power is the Frobenius map in characteristic p. For a finite field with p to the n elements, successive Frobenius powers generate a cyclic Galois group of order n over its prime field. Galois's original work predates today's polished vocabulary, but this thread connects his name to the arithmetic of finite fields used throughout modern coding theory, cryptography, and computational algebra.

Return to the original problem of radical formulas. Why should the structure of the group decide whether radicals will work? Taking a square root introduces a very controlled kind of ambiguity: the result can be either of two signs. Taking an n-th root introduces a finite family of choices differing by roots of unity. By adjoining radicals one at a time, we build a tower of field extensions. After adjoining the necessary roots of unity, the automorphism groups of these stages are abelian, meaning their operations commute. The cumulative symmetry group can therefore be broken into a chain whose successive quotients are abelian. Groups with such a chain are called solvable groups.

This is the algebraic heart of the criterion: for a polynomial over a field of characteristic zero, solvability by radicals is equivalent to solvability of its Galois group. A full proof needs careful treatment of splitting fields, roots of unity, normal extensions, and the correspondence between fields and subgroups. But the basic mechanism is already visible. Each radical extraction permits a limited kind of symmetry. A long tower can combine those symmetries, yet it cannot generate arbitrary algebraic complexity. If the full symmetry group is too entangled to be decomposed into abelian stages, no radical recipe can capture all its roots.

Why does a ladder of fields translate into a ladder of groups? Imagine starting from rational numbers, then adjoining the square root of two, and then adjoining the square root of three. At the first step the sign choice for square root of two creates a symmetry of order two. After the second step there is another independent sign choice. The whole construction has four automorphisms, and they form a commutative group. This is a particularly simple radical tower. More elaborate towers may have noncommuting groups overall, but they have a chain that can be analyzed through successive abelian pieces. That chain is what solvability formalizes.

The converse is equally important. If the group has an appropriate solvable chain, Galois theory lets us construct a tower of radical extensions sufficiently large to contain the roots. The proof is not merely the observation that known formulas happen to produce solvable groups. It is a classification: the algebraic symmetry is enough to tell us when radicals are possible. The word possible refers to expression by a finite sequence of allowed operations, not to the efficiency or simplicity of the resulting expression. A solvable polynomial may still have a dreadful-looking formula.

The group S three is solvable. It has a normal subgroup A three containing the three even permutations, which is cyclic of order three. The quotient S three over A three has order two. We therefore obtain a chain of groups in which the successive quotients have orders three and two, both abelian. That matches the existence of cubic formulas. S four is also solvable, though its normal-subgroup chain is longer. This matches Ferrari's formula for quartics. But for degree five a different phenomenon becomes possible.

Inside S five sits A five, the group of all even permutations of five objects. It has sixty elements. Unlike the smaller alternating group A four, A five is a nonabelian simple group: it has no nontrivial proper normal subgroup. Its operations do not all commute, and it cannot be broken into a chain of normal subgroups with abelian quotients. Since A five is a normal subgroup of S five, S five is not solvable. Thus any polynomial whose Galois group is the full S five cannot have all its roots expressed by radicals over the rationals.

Why does A five create such a strong obstruction? Its simplicity is the key. In a group, a normal subgroup is a collection preserved by conjugation, the process of transporting an operation by another group operation and its inverse. Normal subgroups are what allow quotient groups to be formed. If there are no nontrivial proper normal subgroups, there is no way to decompose the group through intermediate normal stages. A five has that property, and it is noncommutative. So any attempted solvable series for A five would be forced to stop at a nonabelian quotient.

One can even see the outline of a proof from counting. The sixty elements of A five divide into conjugacy classes of sizes one, fifteen, twenty, twelve, and twelve. A normal subgroup has to be a union of conjugacy classes and must contain the identity. Its size must divide sixty by Lagrange's theorem. Try adding the numbers fifteen, twenty, twelve, and twelve to the mandatory one, in any proper combination. None of the resulting proper sums is a divisor of sixty. The only possible normal-subgroup sizes are one and sixty. This is a striking instance in which a concrete finite count rules out an entire hierarchy of algebraic constructions.

The modern definition of solvability is also more flexible than the older question about radicals. A group is solvable if its derived series eventually reaches the identity, where the derived subgroup is generated by commutators. A commutator measures the failure of two group elements to commute. For A five, the derived subgroup is all of A five, so repeatedly taking commutators never reduces its complexity. This makes the impossibility intuitive: the noncommutativity is structurally persistent.

This is a remarkable kind of negative knowledge. Rather than trying every clever formula and failing again and again, one can prove that the entire class of formulas is insufficient. The obstruction is not computational weakness. You could calculate a quintic root to a million digits and still be unable to express it in a finite radical formula. Numerical approximation and algebraic solvability ask different questions.

Let us examine a particular quintic so the statement has a definite object. Consider x to the fifth minus six x plus three. Eisenstein's irreducibility criterion with the prime three tells us this polynomial cannot factor into lower-degree rational polynomials: all the nonleading coefficients are divisible by three, while the constant term three is not divisible by nine. Irreducibility forces its Galois group to act transitively on its five roots. Since the group order is divisible by five, it contains a five-cycle.

Next look at the graph of the polynomial on the real line. Its derivative is five x to the fourth minus six. This derivative has exactly two real zeros, one negative and one positive, so the polynomial has two turning points. The values at suitable intervals show it crosses the axis three times. That leaves two nonreal roots, which form a complex-conjugate pair. Complex conjugation fixes the three real roots and swaps the two nonreal roots, giving a transposition in the Galois group. A five-cycle together with a transposition generates the full symmetric group in this prime-degree setting, so the Galois group is S five. No solution by radicals exists for this particular polynomial.

The example deserves a caution about what the result says. It does not assert that every equation of degree five is unsolvable by radicals. The equation x to the fifth minus thirty-two equals zero has the real root two, and its other roots are obtainable using fifth roots of unity. Special quintics have solvable Galois groups. The result is that there is no formula by radicals that works for arbitrary quintics, and many concrete quintics, including the one we just studied, are not solvable by radicals at all.

There is a second caution about history. The compact modern presentation through splitting fields, automorphism groups, normal subgroups, and the fundamental theorem of Galois theory developed through later generations. Galois introduced the essential group-theoretic analysis of equations, but the definitions and proofs familiar from a current algebra textbook were refined by mathematicians such as Jordan, Dedekind, and Artin. History is more exact when it traces both the originating idea and its later formalization.

The fundamental theorem of Galois theory expresses a beautiful reversal. Suppose L is a finite Galois extension of a base field K, and G is its group of automorphisms fixing K. Every intermediate field between K and L corresponds to a subgroup of G, and every subgroup corresponds to an intermediate field. Larger fields correspond to smaller subgroups. Normal intermediate extensions correspond to normal subgroups, and their Galois groups are the appropriate quotients. This gives two parallel ways to navigate the same structure: add numbers to a field, or remove symmetries from a group.

The field-group correspondence gives a way to draw an abstract algebraic map. Put the large splitting field at the top of a page, the rational numbers at the bottom, and the intermediate fields in between. Then draw the subgroup lattice upside down. Every intermediate field appears opposite the group of symmetries that fixes it. Taking a fixed field loses symmetries as it adds numbers. Taking a subgroup preserves only those automorphisms compatible with the additional equations. This dual organization is one reason the theory is so powerful. It converts questions about algebraic expressions into finite combinatorial structure, and sometimes converts finite group questions into questions about field extensions.

A small example makes that reversal audible. Consider a field containing both square root of two and square root of three. Starting from the rationals, adjoining both gives four combinations: a plus b square root of two plus c square root of three plus d square root of six. There are four automorphisms, determined by choosing the signs of the two independent square roots. They form a group in which every operation has order at most two. The intermediate field containing only square root of two corresponds to the two automorphisms that leave square root of two fixed while possibly changing the sign of square root of three. Add the second square root, and the permitted symmetry shrinks to the identity. Enlarging a field reduces its remaining symmetries.

For the field generated by square root of two and square root of three, the three proper quadratic intermediate fields are generated by square root of two, square root of three, and square root of six. The last one is easy to forget: multiplying the two radicals produces another quadratic extension. The four-element automorphism group has three different subgroups of order two, and the three quadratic fields correspond to them. This small lattice is a complete, concrete instance of the fundamental theorem.

There is also a computational story here. If we can factor a polynomial modulo carefully chosen primes, the factor degrees often reveal cycle patterns in its Galois group. For example, a factorization into one irreducible quadratic and one irreducible cubic modulo a suitable prime corresponds to an element whose permutation has a two-cycle and a three-cycle. Cubing that element leaves a transposition. An irreducible reduction of a quintic modulo another suitable prime gives a five-cycle. These observations can help certify that a polynomial's group is S five without ever writing exact formulas for its roots. A nineteenth-century idea becomes a practical method in modern computational algebra.

Finite fields reappear here for a second reason. In a finite field, the Frobenius automorphism acts on the roots of a polynomial, and its cycles correspond to degrees of irreducible factors. So factoring an integer polynomial modulo primes samples the arithmetic symmetry of its roots. This is not identical to the finite-field construction from Galois's early paper, but it shows how different branches of his work meet in later mathematical practice.

The conceptual power is easy to miss if we treat this as only a recipe for solving polynomials. A root is an object whose definition is constrained by algebraic equations. Instead of staring at an object directly, study all transformations that preserve the relations defining it. Then translate those transformations into structural information about the object. That strategy reaches far beyond nineteenth-century algebra. Symmetry groups would later organize geometry, physics, topology, and number theory.

Let us make a final comparison between equations and geometry. Suppose I hand you a square. You can describe it by its four corners and four sides. Or you can describe it by the eight rigid symmetries that preserve it: four rotations and four reflections. The second description does not replace the first. It reveals organization that a list of coordinates may conceal. Galois proposed an analogous viewpoint for polynomial roots. The roots may be algebraically inaccessible as individual formulas, yet their permissible exchanges can still be studied exactly.

That change of viewpoint answers the guiding question. Why can some equations never be solved by radicals? Because the form of solution you permit has an algebraic structure, and the equation's root symmetries may exceed that structure. A failure to find a formula can be elevated to a proof that no such formula exists. The mathematics is powerful because it tells us what can be done, what cannot be done, and which property makes the difference.

Nothing in these calculations requires us to imagine that twenty-year-old Galois wrote a modern algebra textbook. His historical achievement was to make permutations of roots into a powerful organizing tool at a time when even the right form of a general answer was contested. The fact that his ideas became clearer through other people's editorial and mathematical labor is part of the story, not a subtraction from his accomplishment. His life was short. The work that survived depended on a series of human decisions extending well beyond it.

<!-- END SPOKEN LECTURE -->

## Display-only mathematical companion

### Roots and automorphisms

For a separable polynomial \(f\in K[x]\), let \(L\) be its splitting field. The Galois group is

\[
\operatorname{Gal}(L/K)=\{\sigma:L\to L\mid \sigma\text{ is a field automorphism},\ \sigma|_K=\operatorname{id}\}.
\]

Each automorphism permutes the roots, but only permutations preserving all polynomial relations over \(K\) can occur.

### Running examples

For \(f=x^2-2\), \(L=\mathbb Q(\sqrt2)\), and
\[
\operatorname{Gal}(L/\mathbb Q)=\{\operatorname{id},\sigma\},\qquad \sigma(\sqrt2)=-\sqrt2.
\]

For \(f=x^3-2\), \(L=\mathbb Q(\sqrt[3]2,\omega)\), \(\omega^2+\omega+1=0\), and \(\operatorname{Gal}(L/\mathbb Q)\cong S_3\).

### Four-element field

\[
\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1),\qquad
\alpha^2=\alpha+1,\qquad \operatorname{Gal}(\mathbb F_4/\mathbb F_2)=\langle x\mapsto x^2\rangle\cong C_2.
\]

### Radical-solvability criterion

Over a field of characteristic zero, \(f\) is solvable by radicals if and only if its splitting-field Galois group is solvable. A finite group \(G\) is solvable when there is a chain
\[
G=G_0\triangleright G_1\triangleright\cdots\triangleright G_r=\{e\}
\]
with abelian quotients \(G_i/G_{i+1}\).

\(S_3\triangleright A_3\triangleright\{e\}\) is solvable; \(S_5\) is not solvable since its nonabelian simple normal subgroup \(A_5\) is not solvable.

### An unsolvable quintic

\[
f(x)=x^5-6x+3.
\]

By Eisenstein at \(p=3\), \(f\) is irreducible over \(\mathbb Q\). Its derivative \(5x^4-6\) has two real critical points, and the signs of the local extrema show that \(f\) has exactly three real roots. Complex conjugation therefore acts as a transposition on the remaining two roots. Transitivity and the degree-five condition yield a five-cycle; in degree five, any subgroup containing a five-cycle and a transposition is \(S_5\). Consequently its roots are not all expressible by radicals.

### Fundamental theorem of Galois theory

For a finite Galois extension \(L/K\), the map \(H\mapsto L^H\) reverses inclusions, establishing a bijection between subgroups \(H\leq\operatorname{Gal}(L/K)\) and intermediate fields \(K\subseteq E\subseteq L\).

### Historical reference pointers

MacTutor biography; Peter M. Neumann's historical edition and editorial analysis; Galois's 1832 letter and the 1846 Liouville publication; specialist algebra exposition on the \(S_5\) example. The numbered claim anchors and source records are maintained in `metadata/037500.json`.

### Historical source notes: human-portrait revision

The additional biographical scenes in the spoken lecture are grounded in the following documentary records. They concern historical context; the mathematical calculations and theorem hypotheses are unchanged.

- `history-galois-1846` — Évariste Galois, Œuvres mathématiques (Liouville edition, 1846). https://www.numdam.org/item/JMPA_1846_1_11__381_0.pdf
- `history-galois-bio-context` — MacTutor History of Mathematics: Évariste Galois, biographical detail. https://mathshistory.st-andrews.ac.uk/Biographies/Galois/
- `history-galois-mactutor` — MacTutor: Évariste Galois biography. https://mathshistory.st-andrews.ac.uk/Biographies/Galois/

Source claims are indexed by exact spoken anchors in `metadata/037500.json`.

### Dates and evidentiary distinctions

- **May 1831:** Arrest after a republican dinner; acquittal in June. **July 1831:** Academy referees' negative report and a second arrest.
- **March 1832:** Transfer from Sainte-Pélagie amid the Paris cholera epidemic. **29 May:** letter to Auguste Chevalier. **30–31 May:** duel and death.
- **September 1832:** Chevalier published the testamentary letter. **1846:** Liouville published substantial writings. **1870:** Jordan's treatise helped systematize the theory.
- The duel's motive remains contested; the 1832 letter is not evidence that the entire theory was invented on one evening.

### Further reading

- [Évariste Galois (Wikipedia)](https://en.wikipedia.org/wiki/%C3%89variste_Galois) and [Galois theory (Wikipedia)](https://en.wikipedia.org/wiki/Galois_theory) for orientation.
- [Neumann, the editors and editions of Galois](https://www.sciencedirect.com/science/article/pii/S0315086012000043) for manuscript transmission.
- [The 1846 Liouville edition](https://www.numdam.org/item/JMPA_1846_1_11__381_0.pdf) for the historical document.
