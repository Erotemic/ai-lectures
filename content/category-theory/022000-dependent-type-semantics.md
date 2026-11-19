# 022000 — Dependent Types: Contexts, Substitution, and Comprehension

**Track:** An Introduction to Category Theory. **Background:** functions, products, logical quantifiers, and typed terms; no familiarity with implementation details of a proof assistant required. **Theme:** categories with families and the categorical semantics of types that depend on values.

<!-- BEGIN SPOKEN LECTURE -->

# Dependent Types: Contexts, Substitution, and Comprehension

Imagine a function that receives the number of seats in a vehicle and then returns a list containing exactly that many passenger names. The length of the list depends on the input. A programming language with only a single undifferentiated list type can represent the data, but it does not automatically encode the relationship between the number of seats and the number of names. A dependent type can express that relationship as part of the type itself.

There is a mathematical question beneath this programming convenience. When a type depends on a value, what does it mean to substitute one value for another? How should a variable context change when we add a dependent variable? And how can proofs involving such variables be interpreted in a model whose objects and arrows satisfy explicit equations?

Category theory provides one answer through structures called categories with families, and related structures called comprehension categories. We will build a small finite model first. The model will make types into families of sets, terms into selections from those families, and substitutions into reindexing operations. Then we will see how dependent sums, dependent products, and equality arise, and why the semantic structure must be richer than an ordinary cartesian closed category.

## What changes when a type depends on a value?

Let a context Gamma contain the names of two people, Ada and Bo. Think of Gamma as the set of possible assignments for a variable p standing for a person. Now give each person a set of admissible access levels. Ada has two possible levels, zero and one. Bo has three, zero, one, and two.

In an ordinary simply typed setting, we might choose one access-level type shared by everyone. But that would either omit one of Bo's levels or allow Ada an extra level that is not valid for her. Instead, define a type A depending on p. At Ada, A is a two-element set. At Bo, A is a three-element set.

Now the expression 'a is an access level for p' is meaningful only when p and a are considered together. This is the essential feature of a dependent type. It assigns a type to each possible value of another variable, and the terms belonging to that type depend on the particular value selected.

We should distinguish a family of types from a term of such a family. The family A tells us that Ada has two possibilities and Bo has three. A term t in the context Gamma selects a valid possibility for each person. For example, t could select level one for Ada and level two for Bo. In the elementary set model, this is a function choosing one element from each fiber.

The choice of a finite toy example is deliberate. It lets us calculate every object without having to rely on a type-checker implementation. Once the substitution laws become visible, the same abstract structure can support much more sophisticated forms of dependency.

## Context extension as a collection of valid pairs

Suppose our original context contains p, and we want to extend it with a variable a that has type A of p. What is the set of valid assignments for both variables? It contains the pairs Ada with zero, Ada with one, Bo with zero, Bo with one, and Bo with two. There are five valid pairs.

This new context is often written Gamma extended by A. The projection back to Gamma forgets the chosen access level and retains the person. It sends both Ada pairs to Ada and all three Bo pairs to Bo. The fiber over each person is exactly the set assigned by A at that person.

That projection has an important universal property. To give a function from some other set Delta into Gamma extended by A is to give two pieces of data: a function sigma from Delta to Gamma telling us which person each input chooses, and a dependent term assigning a valid access level for that chosen person. These two components are exactly what a pair of a person and an access level contains.

The pairing works in both directions. Given a map into the extended context, project out the person and level. Given a person assignment and a valid level assignment, combine them into a map into the extended context. These operations are inverse. This is context comprehension in its simplest set-theoretic form.

The name comprehension reflects the construction's role in collecting assignments satisfying a typing relation. Notice that the new context is not necessarily the product of Gamma with one fixed access-level set. Its fibers have different cardinalities. The total number of valid pairs is two plus three, rather than two times a common number.

## Substitution must update types as well as terms

Now introduce a second context Delta containing three shifts: morning, afternoon, and evening. Define a function sigma that assigns Ada to morning, Bo to afternoon, and Ada to evening. We have a substitution from Delta into Gamma: for each shift, it tells us which value of p to use.

What happens to the dependent type A? It is pulled back along sigma. The new type over Delta assigns a two-element access-level set to morning, a three-element set to afternoon, and a two-element set to evening. The types were transported by following the person assignment. We have not invented any new access levels.

A term also reindexes. Recall the term selecting level one for Ada and level two for Bo. After substitution it chooses level one for morning, level two for afternoon, and level one for evening. The type of the resulting term is the reindexed family. If we forgot to reindex the type, we could end up claiming that a term belongs to a fiber belonging to the wrong person.

This is one of the central type-checking obligations in dependent mathematics. In an expression where the type refers to a variable, changing that variable changes what type is being asserted. Substitution operates coherently on both the type and its inhabitants.

There are two laws that we want before discussing any sophisticated type formers. Substituting the identity assignment changes nothing. And substituting twice agrees with substituting the composite assignment once. The same laws must hold both for families of types and for terms of those families. They are the categorical identity and associativity laws expressed as equations of reindexing.

## The pullback hidden inside substitution

The relation between context extension and substitution is geometrically neat. Begin with the original projection from Gamma extended by A back to Gamma. Then pull this projection back along sigma from Delta to Gamma. The resulting set contains pairs consisting of a shift and an access level valid for the person assigned to that shift.

In our numerical example, the pullback has two valid pairs over morning, three over afternoon, and two over evening. Its total cardinality is seven. But that is exactly the context obtained by extending Delta with the reindexed family A after sigma.

There is a canonical correspondence between these two descriptions. A shift with an allowed access level can be sent to the pair consisting of its assigned person with that level, together with the shift that selected the person. Conversely, any pullback pair contains precisely a shift and a compatible access level. The correspondence is invertible and respects the projections.

This pullback square explains why types are often modeled as display maps or fibrations. A type over a context is displayed as a map whose fibers are its possible values. Substitution pulls that map back. Type dependency becomes a property of how objects vary over a base, and the basic substitution equations become functoriality of pullback.

It also exposes a precise limitation. Pullbacks are often unique only up to a canonical isomorphism. A syntactic type system, however, may require strict substitution equations that hold literally. Categories with families package chosen substitution operations with strict functorial laws. Other categorical semantics may use a weaker, up-to-isomorphism structure and then require a coherence or strictification argument to interpret definitional equality.

## What a category with families records

We can now describe the general structure. There is a category C whose objects are contexts and whose arrows are substitutions. The category has a terminal object representing the empty context. For each context Gamma, we have a collection of types valid there. For each type A in Gamma, we have a collection of terms inhabiting A in Gamma.

Every substitution from Delta to Gamma reindexes a type over Gamma into a type over Delta. It also reindexes a term, landing in the reindexed type. Identities and composites act as expected. Finally, for every Gamma and A, there is a context extension Gamma dot A with a projection to Gamma and a distinguished generic term of the pulled-back type. Any substitution together with a term of the appropriately reindexed type factors uniquely through this extension.

A compact definition expresses this as a functor from the opposite of the context category into a category of families of sets, supplemented by terminal context and comprehension structure. The details in the mathematical companion make the domain and codomain of each operation explicit.

The phrase category with families describes an abstract presentation of substitution and context extension. It does not automatically equip the model with dependent function types, identity types, inductive types, or universes. Those require additional semantic operations and laws. We should be careful whenever a definition is followed by a long list of structures that one hopes to interpret: the mere existence of contexts and substitution does not prove those structures are present.

## Dependent sums as collecting all possibilities

Return to the two-person context and its access-level family. Sometimes we want the type of all pairs consisting of a person and one of their valid access levels. This is a dependent sum. In our example, it has five inhabitants, the five pairs we enumerated when extending the context.

Write the dependent sum as summing A over every p in Gamma. It is a disjoint union of the fibers, remembering which person each access level belongs to. The same numeric level one occurring under Ada and Bo gives different pairs, because the person is part of the result.

Dependent sums generalize ordinary Cartesian products. If every person has the same fixed access-level set S, then summing that constant family over Gamma gives Gamma times S. If the sizes differ, the construction is a disjoint union with varying fiber sizes, often called a dependent pair or sigma type.

A sigma type has introduction and elimination principles. To introduce an inhabitant, provide a value p and a term of A of p. To use an inhabitant, unpack those two components while respecting the dependence of the second on the first. The categorical semantics encodes these rules through context extension and, in appropriate comprehension categories, left adjoints to reindexing with compatibility equations.

## Dependent products as choosing one value in every fiber

There is a different question we can ask of the same family. Rather than choosing one person and one level, choose a valid level for every person at once. We then need two choices for Ada and three for Bo, so there are two times three, or six, global assignments.

This is a dependent product. It consists of functions that, given any person p, return an element of A of p. In an ordinary product, the type of the returned value is independent of the input. In a dependent product, the output type changes with the input.

The distinction is visible in the counts. The dependent sum of our family has five elements; the dependent product has six. These are separate universal constructions. The first enumerates tagged choices from any one fiber. The second packages a coherent selection across all fibers. In other contexts, especially infinite ones, the existence of such a global selection can involve mathematical choice principles that the finite example hides.

The term formers mirror ordinary function abstraction and application. If in context Gamma extended by A we can construct a term of B, then under appropriate dependent-product structure we can abstract over the A-variable to obtain a dependent function in context Gamma. Applying that function to a term of A substitutes the argument and yields a term in the corresponding B fiber.

In categorical semantics, dependent products are often right adjoints to reindexing along context projections, subject to stability conditions. Dependent sums are often left adjoints. These adjunctions must respect substitution in the appropriate way, commonly expressed by Beck–Chevalley conditions. Without that compatibility, an interpretation may behave correctly in one fixed context but fail when variables are substituted.

## The role of equality and proof relevance

What about a type asserting that two values are equal? In a simple model based on sets, equality can be represented by the diagonal relation: the pairs whose two components are identical. It can support an extensional interpretation of identity. But intensional identity types in dependent type theory may preserve distinctions between proofs of equality, and their elimination rules require additional structure.

It would be a mistake to infer that a category with families automatically interprets every identity-type rule used in a proof assistant. A model may support some type formers and not others. Its identity types may satisfy extensionality principles that are not derivable in a chosen intensional calculus. Homotopical models and higher-categorical semantics capture other interpretations where equalities themselves can carry nontrivial structure.

For the same reason, nothing we have said implies that Lean's entire dependent type theory is modeled by this five-element example. The example illustrates the structural core: contexts, type families, terms, substitution, and comprehension. Actual foundational systems also have universes, inductive families, computation rules, and specific logical axioms whose semantics requires careful additional work.

The distinction between definitional equality and proved equality is especially important in formalization. A definitional equality is handled by the system's computational conversion rules. A proposition asserting equality can require an explicit proof term. A categorical model must respect the equations that are meant to hold definitionally, while interpreting propositional equality according to the intended identity structure.

## Why strict laws matter to an implementation

Imagine a compiler that translates contexts and substitutions into a semantic model. If applying the identity substitution alters the representation of a type, the compiler must provide a conversion showing why the result is still the intended type. If composing substitutions produces multiple representations that are merely isomorphic, every use of the corresponding term may demand an explicit coherence witness.

Some categorical models manage these conversions through chosen pullbacks, cleavage data, or strictification constructions. Others use richer equality structures and accept coherence up to equivalence. Those are design choices with proof obligations, and the chosen semantics must match the rules of the source type theory.

Our finite family model is pleasantly strict. Reindexing is just function composition. If sigma assigns shifts to people, and tau assigns time slots to shifts, pulling a family first along sigma and then along tau literally produces the same fibers as pulling it once along the composite sigma after tau. The equations hold by ordinary associativity of functions. That is why the set-family model is such a good place to learn the mechanics.

In larger formal developments, that convenience may disappear. The challenge is to recover a coherent interpretation without assuming that every mathematical isomorphism should become a definitional equality. Understanding this is useful when designing a formal language, choosing semantic abstractions, or proving an interpretation sound.

## Contexts as a mathematical form of scope

One reason the categorical viewpoint is productive is that it treats the scope of variables as mathematical data. A statement such as 'given a person p and an access level a valid for p' carries a dependency graph in its context. Substitution changes the assignment to p, and therefore the allowed type of a. Context comprehension adds a variable together with the constraint that makes its use valid.

A common programming error is to construct a record whose fields happen to be individually well typed but are inconsistent with one another. For example, a list of five passengers paired with a length field declaring six. A dependent pair can express the constraint that the length field and passenger list agree. Constructing the record then requires a value of the relevant fiber, so the inconsistency is rejected at the type level in an appropriate dependent type system.

The semantic lesson goes beyond compiler correctness. Dependency forces us to distinguish a family of propositions from one global proposition. A statement may be meaningful only relative to a particular assignment, and a proof inhabiting that statement must be transported when the assignment changes. Category theory makes this transport explicit through functorial reindexing.

This is closely connected to the mathematical semantics of quantifiers. An existential statement can ask for a dependent pair, a witness together with evidence that it satisfies a predicate. A universal statement can ask for a dependent function, assigning evidence to every input. These interpretations are especially natural in constructive type theory, where proving existence includes providing a witness and proving a universal proposition involves constructing an appropriate function.

## A complete substitution check

Before finishing, let's verify a law with our actual finite numbers. Begin with Gamma equal to Ada and Bo. Let Delta be morning, afternoon, evening, and sigma map those shifts to Ada, Bo, Ada. Let Theta consist of two meeting slots, first and second. Let tau map the first slot to morning and the second to evening.

Pull A along sigma. It becomes a family with fiber sizes two, three, two over the three shifts. Now pull that family along tau. The first meeting slot gets the two-element morning fiber; the second gets the two-element evening fiber. So the result has sizes two and two.

Alternatively, compose sigma with tau. Both meeting slots are sent directly to Ada. Pull the original A along that composite. Again each meeting slot gets Ada's two-element set. The fibers agree exactly. The same happens to the term that selects level one for Ada and level two for Bo: after either substitution route, both meeting slots receive level one.

This is the substitution law made visible. It tells us that we can change context in stages or in one step without changing the meaning of types and terms. In a proof assistant, the corresponding laws underpin reliable elaboration and the interpretation of dependent expressions. In a mathematical model, they ensure that substitution is truly a functorial operation.

## The construction we can now use

A dependent type can be seen as a family of possible values indexed by a context. A term is a coherent selection from that family. A substitution changes the context and reindexes both types and terms. Context comprehension packages a variable together with a value of its dependent type; the universal property of that extension describes pairing and projection. Dependent sums collect tagged possible values, while dependent products select one value in every fiber.

Categories with families state the core laws exactly. Comprehension categories and related structures express similar ideas through fibrations and pullbacks. Additional categorical structure is required to interpret the rest of a type theory, and the difference between strict equalities and coherent isomorphisms cannot be ignored.

The central insight is that variables, types, and substitution can be given a compositional mathematical semantics. The dependency of a type on a value then becomes part of the structure being modeled, with equations that can actually be checked. That is a useful bridge between abstract category theory, constructive mathematics, and the formal verification of programs and proofs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

A **category with families** includes a category \(\mathcal C\) of contexts and substitutions, a terminal context \(1\), a strictly functorial assignment of types and terms to contexts, and comprehension. Write \(\mathrm{Ty}(\Gamma)\) for the set of types over \(\Gamma\), and \(\mathrm{Tm}(\Gamma,A)\) for the set of terms of \(A\in\mathrm{Ty}(\Gamma)\). If \(\sigma:\Delta\to\Gamma\), then
\[
A[\sigma]\in\mathrm{Ty}(\Delta),\qquad
 t[\sigma]\in\mathrm{Tm}(\Delta,A[\sigma]),
\]
with \(A[\mathrm{id}]=A\), \(A[\sigma][\tau]=A[\sigma\circ\tau]\) and corresponding term laws. For \(A\in\mathrm{Ty}(\Gamma)\), comprehension provides
\[
p_A:\Gamma.A\to\Gamma,\qquad q_A\in\mathrm{Tm}(\Gamma.A,A[p_A])
\]
with unique pairing \(\langle\sigma,t\rangle:\Delta\to\Gamma.A\) such that \(p_A\circ\langle\sigma,t\rangle=\sigma\) and \(q_A[\langle\sigma,t\rangle]=t\).

**Set-family model:** For a set \(\Gamma\), a type is a family \(A:\Gamma\to\mathbf{Set}\), a term is a section \(t(\gamma)\in A(\gamma)\), and
\[
\Gamma.A=\{(\gamma,a):\gamma\in\Gamma,\ a\in A(\gamma)\},\quad
A[\sigma](\delta)=A(\sigma\delta).
\]
For \(\Gamma=\{\mathrm{Ada},\mathrm{Bo}\}\) with fiber sizes 2 and 3, \(|\Gamma.A|=5\); sections are \(2\cdot3=6\) in number. Under \(\sigma:\Delta\to\Gamma\) with assignments Ada, Bo, Ada, the reindexed sizes are 2,3,2, and \(|\Delta.A[\sigma]|=7\). The canonical square formed by the two context projections and \(\sigma\) is a pullback in Set.

For an appropriate family semantics, \(\Sigma_{\gamma\in\Gamma}A(\gamma)\) is the disjoint union and \(\Pi_{\gamma\in\Gamma}A(\gamma)\) the set of sections. In locally cartesian closed settings, dependent sums and products correspond to left and right adjoints to pullback along context projections, with substitution compatibility. A bare CwF does not automatically supply these or intensional identity types, universes, or inductive types.

### Exercises with answers

1. **Exercise:** A family over two points has fiber sizes two and three. Count elements of its dependent sum and dependent product. **Answer:** Five and six, respectively.
2. **Exercise:** Why must reindexing a term reindex its type? **Answer:** A term over \(\Gamma\) selects an element of \(A(\gamma)\); after \(\sigma:\Delta\to\Gamma\) the selected element lives in \(A(\sigma\delta)\), the fiber of \(A[\sigma]\).
3. **Exercise:** What universal property does \(\Gamma.A\) satisfy? **Answer:** Maps into it correspond uniquely to substitutions into \(\Gamma\) paired with a term of the pulled-back type.
4. **Exercise:** Why is ordinary set equality not a complete model of all intensional identity types? **Answer:** It can impose extensional equality principles and lacks the further proof-relevant or homotopical structure required by many intensional interpretations.

### References

- Stanford Encyclopedia of Philosophy, *Intuitionistic Type Theory*, https://plato.stanford.edu/entries/type-theory-intuitionistic/
- Simon Castellan, Pierre Clairambault, and Peter Dybjer, *Categories with Families*, https://perso.ens-lyon.fr/pierre.clairambault/cwfs.pdf
- Bart Jacobs, *Comprehension Categories and the Semantics of Type Dependency*, https://doi.org/10.1016/0304-3975(93)90169-T
- Greta Coraglia and Jacopo Emmenegger, *A 2-Categorical Analysis of Context Comprehension*, https://www.tac.mta.ca/tac/volumes/41/42/41-42abs.html
