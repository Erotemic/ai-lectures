# 027000 — Beck's Monadicity Theorem: When Structure Can Be Recovered from a Monad

**Track:** Introduction to Category Theory. **Background:** functions, monoids, adjunctions, monads, and coequalizers. **Theme:** comparison functors, presentations, reflection of isomorphisms, and Beck's criterion.

<!-- BEGIN SPOKEN LECTURE -->

# Beck's Monadicity Theorem: When Structure Can Be Recovered from a Monad

Suppose someone hands you an unfamiliar mathematical object. It has elements, and a map from finite lists of elements back into the object. The map knows what to do with the empty list and with nested lists. You never see the word monoid in the specification. Could you still discover that the object has a multiplication and an identity? And could you prove that every compatible map between these objects preserves that multiplication?

The answer is yes. The operation that interprets a two-element list acts as multiplication. The interpretation of the empty list acts as the identity. The laws for nested lists force associativity. This is an example of a remarkable phenomenon: all the information about a familiar algebraic category can be reconstructed from a monad on a category of underlying objects.

But this happy outcome is not automatic. A monad constructed from an adjunction always remembers something about the adjunction. It does not always remember everything. Jon Beck's monadicity theorem tells us what additional structure must survive if the original category is to be recovered as the category of algebras for that monad. The theorem has the feel of a reconstruction test: do we have enough information to build the structures back, and do the operations used to identify equivalent descriptions behave correctly?

## A familiar experiment with words

Start with an ordinary set X of letters, perhaps the set containing only a and b. A free monoid on X consists of all finite words in those letters. The empty word is allowed, and we combine two words by writing one immediately after the other. If the first word is a b and the second is b a, their product is a b b a. Concatenation is associative, and the empty word is the identity.

There is a forgetful functor U from monoids to sets. It takes a monoid and reports its underlying set; a structure-preserving function is reported as an ordinary function. There is a free functor F going the other way, sending a set to its words. Giving a monoid homomorphism from the free monoid on X to a monoid M amounts to choosing one image in M for each letter of X. Once the images are chosen, the homomorphism must evaluate an arbitrary word by multiplying the images of its letters.

This correspondence is an adjunction. Now take the two functors in order: free first, forget second. The resulting endofunctor T on sets sends X to the underlying set of finite words over X. The unit puts each letter into a one-letter word. The multiplication flattens a word of words. That is precisely the list monad.

An algebra for this monad consists of a set A together with a coherent evaluator from words in A back to A. We already saw that coherent evaluators are exactly monoid structures. More strongly, the functions that preserve evaluation are exactly monoid homomorphisms. Thus the entire category of monoids can be recovered from the monad on sets.

## What recovery means

Now imagine an arbitrary adjunction, with a left adjoint F from a category C to a category D, and a right adjoint U back from D to C. Think of C as a category of visible data, and D as a category of objects with some additional structure. The monad on C is T equals U after F. Its unit comes from the adjunction unit, and its multiplication comes from applying U to the counit at a free object.

Every object d of D determines an algebra for T. Its underlying object is U of d. To evaluate a free T-expression over that object, first use F and then the adjunction counit to interpret the freely generated structure inside d. The resulting structure map is U of the counit at d. The adjunction identities guarantee the two algebra laws.

A morphism in D becomes a morphism of these algebras. So there is a canonical functor K from D to the category of T-algebras. Mathematicians call K the comparison functor. It compares the original category of structured objects with the category constructed from the monad itself.

For monoids, K is an equivalence. Every list-algebra comes from a monoid, and every list-algebra homomorphism comes from a monoid homomorphism. In general, K may fail to be essentially surjective, or fail to capture all relevant morphisms. When K is an equivalence, we say the right adjoint U is monadic. The name means that the monad on C really does determine D up to categorical equivalence.

## An adjunction that loses too much

A left adjoint is not sufficient for monadicity. To see the problem without a forest of symbols, let C be the terminal category. It has exactly one object and one arrow, the identity. Let D be the category of sets. There is a functor U from sets to C sending every set to the only object and every function to the identity arrow.

Does U have a left adjoint? Yes. Send the only object of C to the empty set. A function from the empty set to any set exists and is unique. That matches the unique arrow in C, so the required hom-set correspondence holds. This is a legitimate adjunction, even though it looks much less interesting than free monoids.

Now form its monad T on C. There is only one possible endofunctor on the terminal category, and it is the identity. Its Eilenberg–Moore category also has one object and one arrow. The comparison functor K sends every set, empty or nonempty, to this single algebra. It cannot be an equivalence of categories: the hom-set of functions from a one-element set to a two-element set contains two maps, while the corresponding hom-set in the terminal category contains only one. The proposed reconstruction has lost morphism information.

The failure is even easier to see with isomorphisms. The inclusion from the empty set to a one-element set is not invertible, but U sends it to the identity, which is invertible. So U is not conservative. A functor is conservative when a map whose image is an isomorphism was already an isomorphism. Conservativity is a way of asking whether the underlying-data view can at least distinguish a reversible transformation from an irreversible one.

The lesson is that an adjunction produces a monad, but does not promise that the monad remembers its source. We need a reconstruction criterion. First, the functor must detect when a map really is invertible. Second, it must support the relevant identification of freely generated expressions. Those are precisely the two roles that appear in an equivalent formulation of Beck's theorem.

## Conservativity and why it is necessary

Why must a monadic functor reflect isomorphisms? Suppose a map between T-algebras has an underlying isomorphism in C. Can its inverse be made into an algebra morphism? Yes. Write the algebra-homomorphism equation for the original map. Compose with the inverse on the appropriate sides, and use functoriality of T. The inverse satisfies the same preservation law. Thus an underlying isomorphism between T-algebras was already an algebra isomorphism.

An equivalence between D and the category of T-algebras preserves and reflects isomorphisms. Therefore any monadic U must reflect isomorphisms. That gives our first practical test. For monoids to sets, a bijective monoid homomorphism has a homomorphic inverse, so U is conservative. The same argument works for groups, rings with unit, and many other familiar varieties of algebra.

But conservativity is only a necessary test. Knowing when a map is invertible does not tell us how to construct every object from generators and relations. For that we need one more categorical operation: a way to identify two maps while preserving exactly the equations they impose.

## A quotient presented by two arrows

Suppose we freely generate words over two letters a and b, then require a b and b a to represent the same word. The resulting object is no longer the ordinary free monoid. It is the free commutative monoid on those two generators, whose elements can be described by pairs of natural numbers recording the number of a's and b's. Here multiplication adds the counts. A word a a b and a word b a a give the same pair: two a's and one b.

This construction is a quotient. We are identifying words according to a relation that must be stable under adding more words on either side. Merely declaring one pair equal is not enough. The smallest compatible congruence also identifies every consequence of the declared equation. In a category, a coequalizer of parallel arrows is a universal way to force their images to agree.

A monoid quotient can therefore be described as a coequalizer of suitable monoid homomorphisms. The universal property says that any homomorphism from the original monoid which respects the relation factors uniquely through the quotient. This is familiar from algebraic presentations: specify generators, specify relations, and require the resulting object to be universal among interpretations satisfying those relations.

What could go wrong when we forget the monoid structure? The ordinary set-theoretic coequalizer of the underlying pair need not automatically inherit the desired multiplication. Unless the equivalence relation is compatible with multiplication, taking equivalence classes can destroy the operation. Beck's criterion asks about pairs for which the underlying category offers especially well-behaved quotient information and whether that information can be lifted back into D.

## Split coequalizers and visible quotients

A split coequalizer is a coequalizer furnished with extra maps witnessing its behavior by explicit equations. For a parallel pair from X to Y, imagine a quotient map from Y to Q, a section choosing a representative in Y for each class in Q, and another map that witnesses how the pair relates the chosen representatives to arbitrary elements. The split identities make the quotient absolute: every functor preserves a split coequalizer.

This is stronger than merely knowing that a quotient exists. A quotient may exist in one category without being preserved by a functor. Splitness gives explicit algebraic evidence of preservation. A pair of arrows in D is called U-split when its image under U participates in a split coequalizer in C. The qualification describes the underlying diagram, not a demand that the original pair have a split coequalizer in D.

The key question is then: whenever the underlying data has such a well-controlled quotient, can we form the corresponding quotient in the structured category, and does U report the same quotient? If the answer is yes in the appropriate universal sense, U creates coequalizers of U-split pairs.

Here creation has more content than preservation. A preserved quotient begins with a quotient upstairs and checks what happens below. Creation says that the downstairs quotient information can be lifted to a universal quotient upstairs. Combined with the adjunction, it lets us reconstruct interpretations rather than merely observe them.

## Beck's theorem, stated carefully

We now have all the pieces. Let U from D to C be a right adjoint, with left adjoint F. Form the induced monad T equals U F and its comparison functor K from D to T-algebras in C. Beck's monadicity theorem says that K is an equivalence exactly when U creates coequalizers of U-split pairs.

There is a commonly useful alternative formulation. It is enough that U have a left adjoint, reflect isomorphisms, and that D admit coequalizers of U-split pairs which U preserves. Precisely which existence and preservation clauses one uses depends on the version of the theorem, so those hypotheses should be stated rather than hidden behind the word monadic.

This result is striking because it replaces a global comparison of two categories with tests on the behavior of one functor. We do not have to enumerate every T-algebra and guess an original object for it. We can test whether the right adjoint detects isomorphisms and whether its appropriate quotients can be lifted and preserved.

The theorem is not saying that all quotients must exist, nor that every underlying set quotient of a structured object automatically carries structure. The specified class of U-split diagrams matters. Requiring arbitrary set coequalizers to lift would be much stronger and is false for many monadic forgetful functors.

## How a reconstruction is built

Here is the central proof idea. Take a T-algebra, consisting of an object A and a map a from T A back to A satisfying the monad laws. The algebra structure says how to evaluate a freely generated expression. But we want an object of D, not just an equation on C.

There are two natural free objects in D connected to this algebra: F of A and F of T A. From the latter to the former we have two maps. One is the counit of the adjunction at the free object F of A. The other applies F to the algebra evaluator a. Intuitively, these two maps encode two ways of interpreting an expression built from generated expressions.

Form their coequalizer in D. The quotient forces the two interpretations to agree. Because the pair is U-split, Beck's hypothesis ensures this coequalizer exists with the right behavior when viewed in C. The reconstructed object now has underlying algebra equivalent to our original T-algebra. In short, every algebra becomes a quotient of free algebras, and the liftability of these quotients supplies the missing objects of D.

There is a second half. Start with an object d already in D. Apply the comparison functor to view it as an algebra, then reconstruct it by the same quotient. The adjunction counit provides the comparison map back to d. The universal properties, together with the quotient conditions, show that this map is an isomorphism. The two constructions are inverse up to natural isomorphism.

This is a proof sketch rather than an attempt to hide all the diagram chasing. The mathematical companion records the two parallel arrows and their algebraic identities. The conceptual hinge is the presentation of an arbitrary algebra by free algebras and the ability to transport that presentation through the right adjoint.

## A concrete case: monoids again

Return to monoids and sets. A bijective monoid homomorphism is invertible as a monoid homomorphism. That checks conservativity. For a U-split pair of monoid homomorphisms, the split set coequalizer can be equipped with a unique monoid structure making the quotient map a monoid homomorphism. The split maps supply the well-behaved relations needed to check the product and identity operations. Thus the forgetful functor creates the relevant coequalizers.

We can also avoid the abstract criterion in this example by directly building an equivalence between monoids and list-algebras. Both arguments are valuable. The explicit equivalence shows what the answer looks like. Beck's theorem explains which features of the forgetful functor make the same kind of reconstruction possible in other settings.

The criterion is useful especially when the algebras are not obviously word operations. A right adjoint might arise from geometry, representation theory, or a category of structured spaces. We can ask if it is monadic without already knowing how to describe the resulting algebras in elementary terms.

## What is special about the split condition?

It is helpful to compare a U-split coequalizer with a familiar quotient from school algebra. If we declare two words equivalent, the quotient set exists: take their equivalence classes. But that does not imply that multiplication of classes is well-defined. Replacing a representative on the left or right may change the product unless the relation is a congruence. Ordinary quotients can therefore ask more of a forgetful functor than it is able to provide.

A split coequalizer carries explicit maps that witness how the quotient is assembled. Those identities survive application of any functor. In Beck's setting we know the split identities only after forgetting structure. The theorem's demand is that such a quotient lift back upstairs with the right universal property. This is a deliberately restricted test, designed to detect whether the operations of the monad can be interpreted as actual structure.

The phrase creates coequalizers is easy to mishear as a demand to construct every conceivable quotient. It means something more exact: for the designated underlying split diagrams, a universal quotient must be available in the structured category and must be respected by the forgetful functor. This is enough because every algebra has the specific free-algebra presentation used in the reconstruction proof. The theorem tests precisely the quotients needed to present all algebras.

## A comparison with descent

A different but related problem appears when one object is described only after passing to a covering family. We receive pieces and consistency maps on overlaps; we want to know whether they descend to a global object. In such questions it is often a comonad, rather than a monad, that organizes the data. The categorical pattern is nevertheless recognizable: a comparison functor, a category of coherent descent data, and hypotheses ensuring that the comparison is an equivalence.

The dual of Beck's theorem is a comonadicity theorem. It concerns left adjoints and equalizers of appropriately split pairs. The switch from quotient-like coequalizers to compatibility-like equalizers is not cosmetic. Algebraic presentations identify expressions; descent matches pieces that must agree on overlaps. The two reconstruction problems are different, and the adjunction formalism describes both.

For now, keep the comparison simple. Monadicity asks whether a category of structures can be recovered from algebra operations encoded by a monad. Descent asks whether global objects can be recovered from compatible local data. Both ask what must be preserved when information passes through a functor.

## What the theorem gives us

We began with finite lists and discovered monoids by coherent interpretation. That concrete reconstruction was possible because every monoid is controlled by generators and operations, with equations identifying equivalent expressions. Beck's theorem generalizes the pattern. It replaces the apparent task of guessing an inverse comparison functor with precise conditions on isomorphisms and certain universal quotients.

The price is that we must be exact about what is being recovered. A right adjoint can lose information; a quotient can fail to preserve operations; an arbitrary adjunction can induce a monad whose algebras do not reproduce the original category. Beck tells us how to recognize the situation in which those failures are ruled out.

The deeper idea is that an object can be known from how freely generated expressions evaluate, provided the rules for identifying expressions lift correctly. That is the mathematical content behind the word monadicity. The theorem does not produce structure from an informal resemblance. It gives conditions under which reconstruction is forced.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(F:\mathcal C\rightleftarrows\mathcal D:U\) be an adjunction with unit \(\eta\) and counit \(\varepsilon\). The induced monad is
\[
T=UF,\quad \mu_A=U\varepsilon_{FA}:UFUFA\to UFA.
\]
The comparison functor \(K:\mathcal D\to\mathcal C^T\) acts by
\[
K(D)=(UD,U\varepsilon_D:TUD\to UD),\qquad K(f)=Uf.
\]

**Beck's monadicity theorem (one standard form).** For a right adjoint \(U\), the functor \(K\) is an equivalence iff \(U\) creates coequalizers of \(U\)-split pairs. An equivalent formulation requires \(U\) to reflect isomorphisms and \(\mathcal D\) to have and \(U\) to preserve coequalizers of all \(U\)-split pairs. A pair \(f,g:X\rightrightarrows Y\) in \(\mathcal D\) is \(U\)-split if \((Uf,Ug)\) extends to a split coequalizer in \(\mathcal C\).

A **split coequalizer** of \(f,g:X\rightrightarrows Y\) comprises \(q:Y\to Q\), \(s:Q\to Y\), \(t:Y\to X\) such that
\[
qf=qg,\quad qs=1_Q,\quad ft=1_Y,\quad gt=sq.
\]
These equations imply the coequalizer universal property and are preserved by any functor.

For a T-algebra \((A,a:TA\to A)\), the pair of maps in \(\mathcal D\)
\[
FTA\ \substack{\xrightarrow{\varepsilon_{FA}}\\[-.7ex]\xrightarrow[F a]{} }\ FA
\]
has underlying image \(TTA\rightrightarrows TA\), namely \(\mu_A\) and \(Ta\), respectively. With the order \(f=\mu_A, g=Ta\), the algebra map \(a:TA\to A\) gives a split coequalizer of these maps in \(\mathcal C\), using section \(\eta_A\) and suitable \(\eta_{TA}\). Under Beck's hypothesis, lift the coequalizer and obtain the object corresponding to \((A,a)\).

**Failure case.** \(U:\mathbf{Set}\to\mathbf{1}\) has left adjoint sending the sole object to \(\varnothing\). Its induced monad on \(\mathbf 1\) is the identity, and the comparison \(\mathbf{Set}\to\mathbf 1\) is not an equivalence. The functor does not reflect isomorphisms.

### Exercises with answers

1. **Conservative forgetful functor.** Show that a bijective monoid homomorphism has homomorphic inverse. **Answer:** for \(x=f(a),y=f(b)\), \(f^{-1}(xy)=f^{-1}(f(ab))=ab=f^{-1}(x)f^{-1}(y)\), and similarly for the unit.
2. **Monad algebra relation.** Verify \(a\circ Ta=a\circ\mu_A\) for the list fold on a monoid. **Answer:** both interpretations multiply the entries in their original order; associativity makes the nesting irrelevant.
3. **Reconstruction pair.** Identify the two arrows \(FTA\rightrightarrows FA\) used for a T-algebra. **Answer:** \(Fa\) and \(\varepsilon_{FA}\); under \(U\) these become \(Ta\) and \(\mu_A\).
4. **A failing adjunction.** Why does \(\mathbf{Set}\to\mathbf 1\) fail conservativity? **Answer:** it sends the nonbijective inclusion \(\varnothing\to\{*\}\) to an identity map.

### References

- Jonathan Mock Beck, *The Tripleableness Theorem* (original 1960s manuscript, reprinted in *Reprints in Theory and Applications of Categories*).
- Emily Riehl, *Category Theory in Context*, Section 5.5.
- Saunders Mac Lane, *Categories for the Working Mathematician*, monadicity chapter.
- The nLab article on Beck's monadicity theorem (for equivalent versions and split-coequalizer conventions).
