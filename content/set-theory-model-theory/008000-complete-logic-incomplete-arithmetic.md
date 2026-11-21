# Complete Logic, Incomplete Arithmetic: What Gödel Actually Proved

<!-- BEGIN SPOKEN LECTURE -->

Two famous statements about mathematical logic seem to collide. The completeness theorem says that first-order logic can prove every semantic consequence of a set of first-order premises. The incompleteness theorem says that sufficiently strong arithmetic cannot prove every mathematical statement or its negation. How can a system be complete and incomplete?

The answer depends on which object is being judged. First-order completeness is a theorem about a proof calculus: does formal derivability capture the consequences true in all models of the premises? Incompleteness is a theorem about particular effective theories: can their axioms settle every sentence of arithmetic? These are different questions. We will reconstruct the distinction, then follow the central idea of Gödel's proof: arithmetic can encode statements about its own finite proofs.

This is an important topic for anyone formalizing mathematics. A proof assistant can check a derivation exactly. It cannot thereby guarantee that its chosen axioms settle every interesting claim. Nor does an independent sentence show that mathematical reasoning has failed. It shows exactly where an axiom system cannot choose between possibilities.

## Three meanings that should not be merged

Start with consistency. A theory T is consistent if it does not prove a contradiction, or equivalently, in classical logic, if there is no sentence phi for which it proves both phi and not phi. A consistent theory may prove many statements and leave others undecided.

Now define syntactic completeness of a theory. T is complete if for every sentence phi in its language, T proves phi or T proves not phi. This does not require a decision algorithm that rapidly tells us which one is provable. For an effectively axiomatized consistent complete theory, however, we can enumerate proofs until one side appears, giving a decision procedure in principle. That may be impractically slow, but it terminates.

Finally define semantic completeness of a deductive calculus. If a sentence follows in every model from a collection of premises, the calculus proves it from those premises. The first-order completeness theorem asserts this equality of semantic and syntactic consequence. It does not say any particular theory T proves one side of every sentence. When models of T disagree on phi, neither phi nor not phi follows from T; a complete proof calculus correctly proves neither.

The theory of simple undirected graphs is an immediate example. Some models contain triangles and some do not. The proof calculus is complete, but the graph axioms do not decide whether a triangle exists. There is no contradiction. First-order logic can faithfully represent an underdetermined specification.

## Arithmetic becomes able to discuss proofs

Gödel's key insight was to turn finite strings into numbers. A symbol gets a numerical code. A finite sequence of symbols gets a code using a fixed effective encoding scheme. A proposed formal proof is a finite sequence of formulas, so it too can be assigned a natural-number code. We can then pose arithmetic questions about codes: is this number the code of a formula? Does this code represent a valid inference step? Does a sequence of coded lines end with a specified sentence?

For a recursively axiomatizable theory with effectively checkable proof rules, the relation saying p is the code of a valid T-proof of sentence number q can be represented arithmetically. The details require careful computability and representability results; assigning numbers to strings alone is not sufficient. Once they are available, an arithmetic formula can assert that there exists a number coding a proof of a given sentence. Call that the provability predicate for T.

An important asymmetry now appears. If we possess an actual proof, we can point to its finite code and verify it. If there is no proof, the assertion that no code works is a universal claim over all numbers. No finite search for a proof can certify its permanent absence by simply running longer. That asymmetry creates room for formal incompleteness.

## A diagonal sentence about its own provability

Recall Cantor's diagonal: given a proposed list, construct an object that disagrees with its own indexed entry. Arithmetic has a related phenomenon. The diagonal lemma says, under suitable coding conditions, that for a formula P of one numerical variable there is a sentence G whose equivalence with P applied to G's own code can be proved within the theory.

Choose P to say the sentence with this code is not provable in T. The resulting sentence G satisfies, inside T, an equivalence of the form: G if and only if G has no T-proof. In informal English people say G asserts its own unprovability. That is a useful memory aid, but the real result is a precise formal equivalence established by the diagonal lemma.

Suppose T actually proved G. Then there would be a concrete finite proof code. Because T can verify coded proofs of its own sentences, it would also prove that G has a T-proof. But from G and the diagonal equivalence, T would prove that G has no T-proof. That gives a contradiction. Thus, if T is consistent and satisfies the needed representability assumptions, T cannot prove G.

Can T prove not G? For the original Gödel construction, showing that it cannot requires a stronger hypothesis than simple consistency, often formulated using omega-consistency or an appropriate one-consistency condition. Rosser later modified the construction by comparing proofs of a statement and its negation, obtaining undecidability from consistency alone for a broad class of effectively axiomatized theories extending weak arithmetic. This technical distinction is important. A careful statement of the first incompleteness theorem invokes the hypotheses under which both unprovability directions are established; it does not silently apply the simple argument for the first direction to the second.

One standard formulation is: any consistent recursively axiomatizable theory strong enough to represent a modest amount of arithmetic, for example an appropriate extension of Robinson arithmetic, is incomplete. There is a sentence it neither proves nor refutes. The proof is not based on vague human creativity. It is a precise construction exploiting finite proof codes, self-reference through the diagonal lemma, and a contradiction argument.

## True in which model?

A sentence can be true in the standard natural numbers without being provable in a particular theory. For an appropriate Gödel sentence G associated with a consistent theory such as Peano arithmetic, the external absence of a proof makes the intended no-proof assertion true in the standard natural numbers. But the theory itself cannot derive G under the stated conditions.

Now use first-order completeness. If a theory T does not prove G, then T together with not G is syntactically consistent, by the deduction principle. Completeness gives a model of T plus not G. This model is not the standard arithmetic structure when G is true there. In a nonstandard model, an internal number may satisfy the encoded predicate for being a proof even though it is not the code of any externally existing finite T-proof. The model's quantifiers range over its own natural-number domain. We should not import external proof-code intuitions without checking the interpretation.

This reconciles the two Gödel theorems. Completeness says an unprovable consequence is not true in all models of the premises. Incompleteness says an effective arithmetic theory leaves a sentence unsettled. The models witnessing this underdetermination may be nonstandard. There is no contest between the theorems: they describe different levels of the same formal picture.

## What the second incompleteness theorem adds

The first theorem constructs a sentence a theory cannot settle. The second concerns the theory's own assertion of consistency. For suitable consistent, effectively axiomatized theories containing enough arithmetic and using a standard arithmetization of provability, the theory cannot prove its formalized consistency statement. The theorem requires precise derivability conditions; it is not a claim that no one can ever reason about a theory's consistency in stronger mathematics.

For example, one can study the consistency of a weak theory in a stronger theory. That is common in proof theory. But if a strong theory proves a weaker theory consistent, the result rests on the stronger assumptions. The second incompleteness theorem restricts a sufficiently strong system's ability to provide its own certificate, not every possible external or relative consistency argument.

This is relevant whenever someone says a proof assistant guarantees the truth of its results. A kernel checks that a proposed proof follows declared inference rules and axioms. That is a concrete and valuable guarantee. Whether the axioms are consistent and whether their intended interpretations are correct are further mathematical questions. Different formalizations may adopt classical choice, quotient principles, large-cardinal hypotheses, or other assumptions. A proof checker does not erase those choices.

## Undecidable statements and undecidable problems

The word undecidable is used in two related but distinct senses. A particular sentence is independent of a theory if neither it nor its negation is provable from that theory. A decision problem is algorithmically undecidable if no algorithm always decides membership in the specified set of instances. Those ideas interact but should not be merged.

For example, the halting problem is algorithmically undecidable: no program correctly decides for every possible program and input whether execution eventually halts. Gödel-style incompleteness concerns derivability of individual sentences in formal arithmetic. The methods overlap through computation and encoding, but the conclusions have different quantifiers. An individual independent sentence is not itself a decision problem over all programs.

A related result in set theory is that the continuum hypothesis is independent of ZFC if ZFC is consistent. Gödel established its relative consistency with the axioms, and Cohen later established the relative consistency of its negation. These are results about models of set theory and cannot be derived merely from the general incompleteness theorem. Gödel's theorem ensures some arithmetic statements are independent under its hypotheses; it does not single out every famous unresolved mathematical conjecture as independent.

## What a rigorous formalization should leave us with

When reading a formal proof, ask first what is being stated: semantic validity in all models, syntactic derivability, existence of a model, consistency of an axiom set, or correctness of an algorithm with respect to a specification. None of these can be substituted for another without a theorem connecting them.

A proof assistant excels at making those connections explicit. One can formalize soundness of a proof calculus, construct terms of a model, verify a completeness argument, or state an arithmetized provability predicate. But checking an instance of a theorem never proves that a chosen formal system can express all mathematics we might want. Completeness of first-order logic and incompleteness of arithmetic show why there is room for both exact formal verification and genuine mathematical independence.

The larger story of set theory and model theory is now visible. Axioms govern what structures exist. Cardinality compares their sizes. Ordinals support induction and recursion beyond finite stages. Choice supplies maximal objects when no selection rule is given. First-order semantics connects sentences to structures; compactness turns locally satisfiable descriptions into models; Löwenheim–Skolem reveals how a language can admit models of very different sizes. Finally, incompleteness shows that effectively axiomatized arithmetic cannot settle every sentence about its own domain.

This is not a failure of mathematical precision. It is precision applied to the reach of mathematics itself. We can name exactly what has been assumed, what has been proved, what models satisfy the result, and where a stronger theorem would require genuinely stronger information. That is a powerful foundation for reading research papers and for formalizing them responsibly.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Three definitions.** (i) Consistency: \(T\not\vdash\bot\). (ii) Syntactic theory completeness: for each sentence \(\varphi\), \(T\vdash\varphi\) or \(T\vdash\neg\varphi\). (iii) First-order semantic completeness of a proof system: \(T\models\varphi\Rightarrow T\vdash\varphi\). Distinguish these from algorithmic decidability of the theorem set.

**Gödel coding and fixed points.** A recursive proof predicate \(\operatorname{Prf}_T(p,q)\) is arithmetized; \(\operatorname{Prov}_T(q)\equiv\exists p\operatorname{Prf}_T(p,q)\). By the diagonal lemma one obtains \(G_T\) with \(T\vdash G_T\leftrightarrow\neg\operatorname{Prov}_T(\ulcorner G_T\urcorner)\). For suitable \(T\), consistency implies \(T\not\vdash G_T\). The original argument for \(T\not\vdash\neg G_T\) uses stronger consistency assumptions; Rosser's refinement yields incompleteness under mere consistency for suitable effective extensions of weak arithmetic.

**First-order completeness is compatible with incompleteness.** If \(T\not\vdash G_T\), then by the deduction theorem \(T\cup\{\neg G_T\}\) is consistent, and by the first-order completeness theorem has a model. It need not be the standard natural numbers.

**Second incompleteness theorem.** Under its standard effective arithmetization and strength assumptions, consistent \(T\) does not prove \(\operatorname{Con}(T)\), the internal statement that no \(T\)-proof of contradiction exists.

**Exercises and solutions.** (1) Can a semantically complete first-order calculus coexist with an incomplete graph theory? *Answer:* yes; graph models disagree on triangle existence. (2) Why does proof coding help diagonalization? *Answer:* syntax and proofs become arithmetical objects to which a fixed-point formula can refer. (3) Does unprovability of \(G_T\) by itself show no theory can prove it? *Answer:* no; provability is always relative to stated axioms. (4) Does second incompleteness rule out relative consistency proofs in stronger theories? *Answer:* no; the hypotheses and system doing the proving differ.

### Sources and reading

- Stanford Encyclopedia of Philosophy, *Gödel's Incompleteness Theorems*: https://plato.stanford.edu/entries/goedel-incompleteness/
- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/
- Open Logic Project, *About*: https://openlogicproject.org/about/
