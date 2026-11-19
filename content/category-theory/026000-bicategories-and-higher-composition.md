# 026000 — Higher Categories: When Compositions Have Their Own Comparisons

**Track:** Introduction to Category Theory. **Background:** functors, natural transformations, monoidal categories, profunctors, and basic universal properties. **Theme:** 2-categories, bicategories, coherence, and higher morphisms.

<!-- BEGIN SPOKEN LECTURE -->

# Higher Categories: When Compositions Have Their Own Comparisons

Imagine three teams transferring information. The first team's records can be translated into the second team's format. The second team can then translate them into a third format. There may be several ways to implement either translation, and we may want a comparison between two implementations. If the implementations are mathematical functors, the comparisons can be natural transformations.

Ordinary category theory describes an arrow connecting one object to another. But here the objects are themselves categories, the arrows are functors, and the comparisons between arrows are natural transformations. We have arrows between arrows. Those comparisons can also be composed, and their composition interacts with the composition of functors. This is the beginning of higher category theory.

The goal is to understand this extra dimension without treating it as an infinity of mysterious diagrams. We will first see how natural transformations give a completely concrete strict 2-category. Then we will construct an example in which ordinary associativity works only up to a specified isomorphism. That example leads to bicategories and their coherence laws. Finally, we will explain what remains when we continue adding higher-dimensional comparisons.

## From arrows to arrows between arrows

Take two categories C and D. A functor F from C to D translates objects and arrows while respecting identities and composition. Another functor G may perform a different translation. A natural transformation alpha from F to G supplies, at each object x of C, an arrow in D from F of x to G of x. These component arrows must be compatible with every arrow of C.

We thus have three levels. At the bottom are categories, which we will call zero-cells. The functors between categories are one-cells. The natural transformations between parallel functors are two-cells. Parallel means that the two functors share a source category and a target category; otherwise the component arrows would not even have matching types.

As a specific example, let C be the category of sets, and let F send a set X to its product with a singleton. Let G be the identity functor on sets. For each X, projection from X times the singleton to X is a function. These projections form a natural transformation because applying a function to the X-coordinate before projecting gives the same result as projecting first and then applying the function.

There is an inverse natural transformation sending an element x to the pair x with the unique singleton element. The two transformations exhibit a natural isomorphism between F and G. We have compared two entire functors, not merely two individual outputs.

## Vertical composition

Suppose alpha is a natural transformation from F to G and beta is one from G to H. At each object x we can compose alpha at x with beta at x, producing an arrow from F of x to H of x. The componentwise composites form a natural transformation from F to H.

This is called vertical composition. It is the most direct way of composing comparisons: first change one implementation into another, then change that implementation into a third. Naturality of the composite follows from the naturality squares of alpha and beta. At each source arrow, we can move the beta component past the transformed arrow, then move the alpha component past it. The two paths around the large diagram agree.

Vertical composition is associative because ordinary arrow composition in D is associative. The identity two-cell on a functor has identity arrows at every object. Thus for each pair of categories C and D, the functors from C to D and their natural transformations form an ordinary category. The collection of possible one-cells has itself acquired categorical structure.

This suggests a useful slogan: in a 2-category, the arrows between two zero-cells form a category, not merely a set. The richer hom-objects remember comparisons between possible arrows.

## Horizontal composition

There is another way to compose natural transformations. Let F and G be functors from C to D, with alpha comparing them. Let H and K be functors from D to E, with beta comparing those. We can compose functors along the chain from C through D to E. The question is how to compare the composite H after F with the composite K after G.

At an object x of C, begin with H of F of x. One route first applies H to alpha at x, reaching H of G of x, then applies beta at G of x, reaching K of G of x. Another route first applies beta at F of x, reaching K of F of x, then applies K to alpha at x. Naturality of beta says the two routes are equal.

That common arrow is the component of a horizontal composite two-cell. The process is called horizontal because we are composing the underlying functors along successive stages, rather than stacking transformations with the same endpoints.

Vertical and horizontal compositions interact through an interchange law. If we have two vertically composable comparisons at the first stage and two at the second, then composing vertically before composing horizontally equals composing horizontally before composing vertically, with the appropriate typing. In the category of categories, functors, and natural transformations, this law follows from ordinary functoriality and naturality.

The interchange law is not just a convention for arranging pictures. It certifies that a square of comparisons can be assembled in either permitted order without changing the resulting two-cell. It is one of the algebraic reasons diagrams with boxes and regions can be manipulated consistently.

## A strict 2-category

The collection of small categories, functors, and natural transformations is called Cat, regarded as a strict 2-category. Composition of functors is literally associative. Identity functors are literally units. The two kinds of composition of natural transformations satisfy their expected identities and interchange laws as equalities.

Strictness is useful but not universal. It describes a setting where all the comparison laws for composing one-cells are literal equations. When objects represent more flexible mathematical processes, composition may be associative only by a specified isomorphism rather than by equality.

To see why that happens, consider joining relations or spans. Suppose we have sets A, B, and C. A span from A to B consists of a set S of witnesses together with functions from S to A and B. It is like a relation that remembers evidence for each related pair, perhaps more than one witness for the same pair.

Compose a span from A to B with a span from B to C by taking compatible pairs of witnesses. Formally, this is a pullback over B. An element of the composite consists of one witness for the first span and one for the second, with the middle B-values matching.

This construction has a natural next step: compose with a third span from C to D. It seems associative, because a complete three-stage witness is just a triple of compatible pieces. But the two ways of forming nested pullbacks produce differently parenthesized sets of pairs. One contains elements of the form an ordered pair whose first component is itself a pair; the other contains a pair whose second component is a pair.

These sets are canonically isomorphic, by reassociating the parentheses, but they need not be literally equal as sets of nested tuples. The difference is small yet mathematically real when equality of constructions is required.

## Bicategories and associators

A bicategory retains the levels of objects, one-cells, and two-cells but weakens the associativity and unit requirements for one-cell composition. Instead of demanding that the two parenthesizations of a three-stage composite be identical, it supplies an invertible two-cell called the associator that compares them.

For spans, the associator sends the witness represented as first compose S and T, then U, to the same triple of compatible witnesses represented as first S, then compose T and U. The assignment is reversible. It preserves the endpoints and is natural in the spans involved.

There are also left and right unitors. The identity span on a set B consists of B with identity maps to both endpoints. Composing it with another span gives a pullback whose elements can be canonically identified with the original span's witnesses. Again the comparison is an isomorphism, not necessarily a literal equality of the chosen representations.

A bicategory is therefore not a category with sloppy equations. It explicitly records the comparisons that replace those equations, and it imposes laws ensuring that the comparisons themselves fit together. The familiar laws are the pentagon identity for associators and the triangle identity linking associators and unitors.

## Why a pentagon appears

Take four composable spans S, T, U, and V. There are five ways to parenthesize their composite. We can move between parenthesizations by applying associators to neighboring groups. Two different sequences of such moves begin with the fully left-associated composite and end with the fully right-associated composite.

The pentagon identity says those two sequences of comparison isomorphisms must agree. Without that equation, the meaning of a four-stage composite could depend on which sequence of harmless-looking reassociations we chose. The bicategory would carry too much arbitrary ambiguity.

For spans, both routes ultimately take a nested expression of four compatible witnesses to the same four witnesses with new parentheses. The pentagon commutes because those reassociations agree. The general axiom requires the same coherence without assuming that all arrows are built out of sets and tuples.

The triangle law handles units. If we insert an identity one-cell into a two-stage composite, we can remove it before or after changing the grouping. The triangle says the results agree. These constraints are the minimum discipline needed to make higher composition manageable.

The point is worth stressing. An associator may be canonical, but the existence of a canonical isomorphism does not exempt us from checking coherence. The pentagon and triangle are separate equations about composites of comparisons.

## Profunctors as another bicategory

There is another instructive example. A profunctor from a category C to a category D can be viewed as a generalized relation that records not just whether an object of C is related to an object of D, but a set of witnesses for that relationship, naturally acted on by arrows in C and D.

Two profunctors compose through a coend. The coend takes pairs of intermediate witnesses and identifies pairs related by changes of intermediate presentation. When we compose three profunctors, the two parenthesizations produce related coend expressions. Under ordinary smallness assumptions, the relevant coend interchanges provide canonical isomorphisms between them.

So profunctors form a bicategory, not merely an ordinary category whose composition is forced to be strict by notation. Its two-cells are natural transformations between profunctors. The associators and unitors come from universal properties of the coends. Their coherence follows from how the universal identifications compose.

This is an important contrast with Cat, where functor composition is strictly associative. In profunctors and spans, the universal constructions used in composition are unique up to canonical isomorphism, and that level of freedom has to be represented. Bicategories allow us to use the natural construction without pretending two different realizations are literally the same.

## A monoidal category hides a bicategory

An ordinary monoidal category has an operation called tensor, a unit object, an associator, and unitors satisfying coherence. We can view it as a bicategory with exactly one zero-cell. The objects of the monoidal category become one-cells from that zero-cell to itself. The morphisms of the monoidal category become two-cells. Tensor product becomes horizontal composition of one-cells.

This is a useful conceptual check. In a one-object bicategory, the associator for one-cell composition is precisely the associator for tensor products. The pentagon and triangle are the same coherence laws. We have not invented a new pattern; we have recognized a familiar one at a higher categorical level.

Conversely, the category of endomorphism one-cells of a chosen object in a bicategory carries a monoidal structure under composition, with the identity one-cell serving as the unit. The passage between one-object bicategories and monoidal categories gives a concrete bridge between tensor calculus and higher morphisms.

For example, the monoidal category of vector spaces under tensor product can be seen as a one-object bicategory. Vector spaces are the one-cells, linear maps are the two-cells, and tensoring vector spaces is one-cell composition. This viewpoint is useful when generalizing algebraic constructions to settings where composition itself has a categorical layer.

## The question of strictification

If weak associativity is so common, why not choose representations that make all composites strictly equal? In many two-dimensional settings a coherence theorem says that every bicategory is biequivalent to some strict 2-category. This is a form of strictification.

The wording matters. Biequivalence is a higher-categorical notion of sameness. The theorem does not say that our original pullback constructions suddenly become literally equal without changing their presentation. It says we can replace the bicategory by a suitable strict model while preserving its structure up to the appropriate equivalence.

That replacement may be mathematically convenient, but the original flexible construction often remains more natural. If the objects are geometric correspondences, forcing all composites into a particular strict presentation can obscure their intended meaning. Coherence allows us to work directly with the weak structure while controlling ambiguity.

One should also avoid extrapolating a two-dimensional strictification theorem to every possible higher category. At higher dimensions, strict and weak models can behave differently, and blanket strictification statements require careful hypotheses. Higher category theory develops multiple models precisely because controlling all those coherence levels is a substantive problem.

## Beyond two dimensions

In a 2-category we have objects, one-cells, and two-cells. But once associators are themselves two-cells, we can ask for comparisons between comparisons. In a three-category there may be three-cells between parallel two-cells. Continue, and we reach the broad idea of an infinity-category, with morphisms and coherences at arbitrarily high dimensions.

The phrase infinity-category describes a family of rigorous frameworks rather than one definition that can be written in a sentence. One widely studied kind is an infinity-one category, where morphisms above dimension one are invertible in a homotopical sense. Examples can be presented using quasicategories, complete Segal spaces, or other models linked by suitable comparisons.

What matters at an introductory level is the problem these structures solve. Mathematical constructions often compose in ways determined only up to equivalence, and the equivalences themselves can be compared. Higher categories retain those comparisons instead of discarding them prematurely. The ordinary category is recovered as a simpler situation where the higher comparison information is trivial or omitted.

A homotopy type illustrates why that extra information can matter. Points are zero-dimensional data. Paths connect points. Homotopies compare paths. Homotopies between homotopies provide another level. An infinity-groupoid packages those invertible path-like structures. Infinity-categories extend the picture by allowing noninvertible one-dimensional arrows as well.

## One precise place to stop

It is tempting to say that a proof assistant with dependent types is automatically an infinity-category, or that every identity proof is a geometric path. Neither claim follows without specifying a semantic interpretation. An intensional type theory can admit homotopy-theoretic models, while a particular proof assistant's equality may be proof-irrelevant. The distinction between syntax and a chosen categorical model remains essential.

Likewise, an ordinary database join need not involve a bicategory in its implementation. The categorical insight is that witness-bearing joins often have canonical comparison maps that make different groupings equivalent. Whether the software must retain those witnesses or comparisons depends on the semantics of the application.

These qualifications preserve the real gain. Higher category theory supplies mathematical language when transformations themselves have transformations, when composition is only coherent up to isomorphism, and when a hierarchy of comparisons cannot be erased without losing information.

## Two-cells in the bicategory of spans

The span construction also clarifies what the second dimension is actually comparing. Suppose S and T are two spans from A to B. A map of spans from S to T is a function on their witness sets that respects both endpoint maps. It may identify some witnesses or translate their representation, but it must never change which pair of endpoints a witness connects.

These witness maps are the two-cells between spans. Vertical composition is ordinary composition of functions on witness sets. Horizontal composition is induced by pullbacks: given a compatible pair of witnesses in two composable spans, apply the two witness maps and obtain another compatible pair. This is well-defined because the endpoint maps commute. It illustrates a genuine interaction between the two levels of composition.

Consider a relation from customers to products. One span might record every individual order as a witness. Another might record just a distinct customer-product pair. A map of spans can send each order record to its associated pair. It forgets multiplicity while preserving endpoints. If we later compose with a supplier-to-product matching span, the induced map on compatible pairs forgets the order identifier but retains the matching relation.

This is the kind of comparison higher category theory is designed to keep. We can reason both about which customers and suppliers are connected and about the evidence by which the connection was established. An ordinary Boolean relation would collapse the witness information from the start. A span and a map of spans preserve two levels of description.

## Coherence is a mathematical obligation

It helps to separate three assertions that sound similar in ordinary speech. First, two constructions may be isomorphic. Second, there may be a preferred natural isomorphism between them. Third, collections of such isomorphisms may satisfy coherence equations when several comparisons are composed. A bicategory needs all the relevant structure and laws, not only the statement that useful isomorphisms exist somewhere.

In the pullback example, the associator maps one nested compatible triple to the other nesting. For four spans, we can apply that reassociation in several orders. The pentagon says that two specified routes through the five parenthesizations agree. If they did not, a computation's result could depend on the history of how we repeatedly regrouped it, even when each individual regrouping had appeared legitimate.

This explains why coherence theorems are valuable. They license families of transformations that would otherwise demand a separate diagram chase every time. But they do so because the coherence equations are established. Their force comes from proof, not from an informal feeling that all the diagrams should be obvious.

## The final shape of composition

We began with two teams translating records and comparing implementations. Functors gave the translations, natural transformations compared them, and the strict 2-category Cat organized both layers. Spans showed why composition can be associative by a canonical reassociation rather than by literal equality. Bicategories recorded the reassociation and imposed the pentagon and triangle to guarantee consistency. Monoidal categories appeared as the one-object special case, and higher categories extended the idea to additional levels of comparison.

The underlying question is stable across these examples: when we compose mathematical processes, what kind of sameness should we require between different ways of composing them? Sometimes equality is appropriate. Sometimes a natural isomorphism is the right notion. Sometimes even that comparison has higher structure. Category theory gives us a disciplined way to choose the level of structure that the mathematics actually needs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

In the strict 2-category \(\mathbf{Cat}\): objects are small categories, 1-cells functors, 2-cells natural transformations. If \(\alpha:F\Rightarrow G\) and \(\beta:G\Rightarrow H\), vertical composition is \((\beta\circ_v\alpha)_x=\beta_x\circ\alpha_x\). Given \(\alpha:F\Rightarrow G:C\to D\) and \(\beta:H\Rightarrow K:D\to E\), horizontal composition has component
\[
(\beta\star\alpha)_x=\beta_{Gx}\circ H(\alpha_x)=K(\alpha_x)\circ\beta_{Fx}.
\]
The equality follows by naturality of \(\beta\). The interchange law follows from functoriality and naturality.

In \(\mathbf{Span}(\mathbf{Set})\), a 1-cell \(A\to B\) is \(A\xleftarrow{s}S\xrightarrow{t}B\); composition uses pullback \(S\times_B T\). The associator compares \((S\times_B T)\times_C U\) with \(S\times_B(T\times_C U)\) by reassociation of compatible triples. The two functors of a fourfold composite satisfy Mac Lane's pentagon identity; the identity spans supply unitors satisfying the triangle identity.

A bicategory \(\mathcal B\) has hom-categories \(\mathcal B(x,y)\), horizontal composition functors, identity 1-cells, and invertible coherent associators and unitors. Any monoidal category \((M,\otimes,I)\) yields a one-object bicategory \(BM\), with 1-cells the objects of \(M\) and 2-cells its morphisms. Every bicategory is biequivalent to a strict 2-category, but not canonically identical to one.

### Exercises with answers

1. **Naturality.** Show projections \(X\times1\to X\) define a natural isomorphism. **Answer:** for any \(f:X\to Y\), both composite maps send \((x,*)\) to \(f(x)\).
2. **Horizontal composition.** Explain why its two component formulas are equal. **Answer:** apply naturality of \(\beta\) to the arrow \(\alpha_x\).
3. **Spans.** Identify a witness of \((S\times_B T)\times_C U\). **Answer:** a compatible triple \((s,t,u)\); reassociation maps to \((s,(t,u))\).
4. **One-object bicategory.** Identify the pentagon. **Answer:** it is precisely the associator pentagon of the corresponding monoidal category.

### References

- Tom Leinster, *Higher Operads, Higher Categories* (2004), on bicategories and coherence.
- Jean Bénabou, *Introduction to Bicategories* (1967).
- Saunders Mac Lane, *Categories for the Working Mathematician*, on coherence.
- nLab, 2-category and bicategory.
