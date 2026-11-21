# Choosing Without a Formula: The Axiom of Choice, Zorn's Lemma, and Bases

<!-- BEGIN SPOKEN LECTURE -->

Suppose someone gives you a drawer of envelopes. Every envelope contains at least one card. You must select exactly one card from each envelope. With ten envelopes, you can open them one by one and choose any card you like. With infinitely many envelopes, it is tempting to say: do the same thing. But as a proof, that phrase may conceal an assumption. What specifies all the choices simultaneously? Is there a rule that chooses a card from each envelope? If no such rule has been supplied, are we entitled to claim a global selection exists?

The axiom of choice answers yes for set-indexed families of nonempty sets. It does not provide an algorithm for choosing cards. It is an existence principle. In standard mathematics it has consequences that reach far beyond envelopes, especially in algebra, analysis, topology, and the theory of infinite structures.

One of its most useful equivalent forms is Zorn's lemma. It says, in effect, that if every linearly ordered compatible chain of partial constructions admits an upper bound, then there exists a construction that cannot be extended further. We will turn that sentence into a proof that every vector space has a basis. The proof is widely used, and its distinction between maximal and maximum is worth understanding in full.

## The choices we can already make

Choice is not required every time a mathematician says choose. If a set has a distinguished least element, select that. If each envelope contains positive integers, choose the least positive integer in it. If each envelope contains a unique red card, choose the red one. These are specified rules. If the family is finite, finite choice follows from ordinary set theory and finite induction.

The axiom becomes interesting for arbitrary families of nonempty sets with no distinguished members. Index them by a set I. For each index i, let A of i be nonempty. A choice function is a function c on I such that c of i belongs to A of i for every index. The axiom of choice asserts existence of such a c for every set-indexed family.

One standard shorthand says that the product of a family of nonempty sets is nonempty. A member of the product is exactly such a choice function. This formulation is familiar in topology, where products of spaces appear, but the set-theoretic content lies in the act of choosing one coordinate value from each factor.

Several surprising consequences are equivalent to the axiom over ZF. Every set can be well-ordered. Every vector space over a field has a basis. Zorn's lemma holds. Equivalence does not mean these statements sound the same or have the same computational content. It means that, within ZF, each can be proved from the others. When mathematicians invoke Zorn's lemma, they are using the strength of choice even if the word choice never appears.

## A partially ordered world of partial answers

Imagine building a basis for a vector space V over a field F. A basis must satisfy two conditions. Its vectors are linearly independent, and every vector of V is a finite linear combination of them. For finite-dimensional spaces, familiar elimination procedures produce a basis. For an arbitrary space that may have no given finite spanning list, those procedures do not immediately reach every vector.

We can instead consider all linearly independent subsets of V. Order them by inclusion. The objects in our partially ordered set are partial attempts at a basis. A smaller independent set can be extended to a larger one by adding a vector outside its span. A maximal independent set should therefore span everything. The difficulty is showing that at least one maximal independent set exists.

Zorn's lemma gives a condition under which this happens. Let P be a nonempty partially ordered set. Suppose that every chain in P has an upper bound in P. A chain is a subset of P in which every two members are comparable under the order. Then P has a maximal element. A maximal element has no strictly larger element above it. It need not dominate every member of P, since the order may have incomparable objects.

That last point is often misunderstood. In the collection of subsets of a two-element set ordered by inclusion, both singleton subsets are maximal among proper subsets if we restrict to proper subsets. Neither is a maximum, because neither contains the other. The word maximal says no extension is possible inside the specified partially ordered set; maximum says greater than or equal to every member. Zorn's lemma promises the former, not the latter.

## Why a chain has a union

Let P be the family of all linearly independent subsets of V. It is nonempty, because the empty set is linearly independent. Take any chain C in P, perhaps an infinite one. Form the union U of all sets in the chain. We claim U is linearly independent.

Suppose not. Then some finite collection of distinct vectors in U satisfies a nontrivial linear relation. Each of those finitely many vectors belongs to some member of the chain. Because the chain is linearly ordered by inclusion, among finitely many relevant members one is large enough to contain all those vectors. That member is linearly independent. It cannot contain the alleged nontrivial relation. Contradiction. Therefore U is independent.

So U belongs to P and contains every member of the chain. It is an upper bound. We have checked Zorn's hypothesis, including the empty chain, whose upper bound can be any member of P. Thus there exists a maximal independent set B.

Now show it spans. Suppose a vector v lies outside the span of B. Then adding v to B preserves linear independence. Any hypothetical relation involving v with a nonzero coefficient would express v as a combination of vectors in B, contrary to assumption. A relation with zero coefficient on v would already violate independence of B. So B union the singleton v is independent and strictly larger. That contradicts maximality. Hence no vector lies outside the span of B. We have constructed, by an existence theorem, a basis.

This proof has a pleasing economy. Independence survives unions of chains because any failure of independence is witnessed by a finite linear relation. Maximality forces spanning because any missing vector could be added. The entire theorem rests on those two local observations plus Zorn's lemma.

## Why maximal extension methods keep recurring

The same architecture appears elsewhere. To extend a consistent collection of formulas, consider consistent partial theories ordered by inclusion. To extend a proper ideal in a ring to a maximal ideal, order proper ideals by inclusion and show unions of chains remain proper. If a chain union contained the multiplicative identity, that identity would already have belonged to one ideal in the chain, making it the whole ring, contradiction. Therefore the union of a chain of proper ideals remains proper. Zorn yields a maximal ideal.

Notice that maximal ideals are not simply maximal subsets of the ring. They are maximal among proper ideals. Changing the partially ordered set changes the conclusion. If we included the whole ring, Zorn would return the whole ring, which is maximal as an ideal but not a proper maximal ideal. Mathematical existence arguments demand that the ambient collection be defined with care.

Another lesson concerns the meaning of an upper bound. For a chain of independent sets, the union itself belongs to the permitted family. For a chain of partial functions, the union is a function only if the partial functions agree wherever their domains overlap. A chain under extension guarantees that agreement. For a chain of finite partial functions, however, the union may be infinite and leave the family of finite functions. That poset would not satisfy the needed chain-bound condition. A tempting Zorn proof can therefore fail at the closure step.

## Where the computational intuition stops

One may be tempted to visualize Zorn's lemma as an algorithm: start with a partial solution, add something while possible, and eventually stop. That picture needs caution. There may be no prescribed choice of what to add, and an infinite sequence of additions indexed by the natural numbers need not reach a maximal object. Even taking limits after such a sequence may leave many possible extensions. Zorn is not merely a while-loop whose termination has been proved.

Transfinite recursion and well-ordering can be used to prove versions of these maximality results, but the required well-ordering is itself equivalent to choice. Without that assumption, one cannot generally convert a set of arbitrary alternatives into a determinate sequence of decisions. The existential proof is still mathematically valid within ZFC; it simply supplies less operational information than an algorithm.

This distinction is significant in constructive mathematics and formal verification. A proof assistant may accept the axiom of choice, allowing a theorem of existence. But if our goal is to extract an algorithm that produces a basis from an effective description of an infinite vector space, additional representation and computability hypotheses are needed. A verified existence proof is not automatically executable code. Conversely, finite-dimensional Gaussian elimination has a constructive proof requiring none of the general axiom-of-choice machinery.

## What if we do not assume choice?

ZF without the axiom of choice is a coherent setting for studying which familiar claims require extra assumptions. Some statements that seem innocuous with finite collections are no longer universally available. In models of ZF where choice fails, there can be families of nonempty sets without a choice function. The assertion that every set can be well-ordered is then false. We should not interpret this as a paradox. It means the familiar general existence principle is independent of the other axioms, subject to standard relative-consistency results.

For ordinary work, many mathematicians adopt ZFC because the choice principle enables an enormous body of useful constructions. Others study the precise amount of choice needed for a result. Countable choice and dependent choice are weaker principles that often suffice in analysis. The difference can change which conclusions survive in more constructive foundations.

The point is not to attach a philosophical label to every proof. It is to know where the power comes from. In the basis theorem, the linear algebra was the simple extension argument. The global existence step was Zorn's lemma. Keeping those parts separate makes the proof easier to understand and easier to adapt.

If we remember one pattern from this lecture, it should be this: define partial solutions, order them by extension, prove every chain has a legal upper bound, obtain a maximal solution, and show a non-complete maximal solution could still be extended. That is a strong proof technique, and it is also a precise statement of the nonconstructive assumption on which it relies.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Axiom of Choice (AC).** For a set-indexed family \((A_i)_{i\in I}\) of nonempty sets, \(\prod_{i\in I} A_i\ne\varnothing\). Equivalent over ZF to the well-ordering theorem and Zorn's lemma.

**Zorn's lemma.** Every nonempty poset in which each chain (including the empty chain) has an upper bound has a maximal element. Some formulations omit explicit nonemptiness because requiring an upper bound for the empty chain forces nonemptiness.

**Vector-space basis.** Let \(P=\{S\subseteq V:S\text{ is linearly independent}\}\), ordered by inclusion. If \(C\subseteq P\) is a chain, then \(U=\bigcup C\) is independent: any dependency uses finitely many vectors, all in one chain member. Zorn yields maximal \(B\). If \(v\notin\operatorname{span}(B)\), then \(B\cup\{v\}\) is independent, contradicting maximality. Therefore \(\operatorname{span}(B)=V\).

**Maximal ideal sketch.** In a nonzero commutative ring with identity, let \(P\) be the set of proper ideals. For a chain \(C\), \(\bigcup C\) is an ideal and remains proper: otherwise it contains \(1\) already in some proper member. Hence Zorn gives a maximal proper ideal.

**Exercises with solutions.** (1) Give a maximal element that is not a maximum. *Answer:* either singleton of a two-element set among its proper subsets ordered by inclusion. (2) Why is the union of a chain of finite sets not necessarily finite? *Answer:* take \(\{1,\dots,n\}\) for each positive integer \(n\). (3) Does a basis of a finite-dimensional space require AC? *Answer:* no; elementary finite-dimensional elimination suffices. (4) Find the exact step in the basis proof using AC. *Answer:* applying Zorn's lemma to obtain a maximal independent set.

### Sources and reading

- Stanford Encyclopedia of Philosophy, *The Axiom of Choice*: https://plato.stanford.edu/entries/axiom-choice/
- Open Logic Project, *Set Theory*: https://builds.openlogicproject.org/content/set-theory/set-theory.pdf
- Stanford Encyclopedia of Philosophy, *Set Theory*: https://plato.stanford.edu/entries/set-theory/
