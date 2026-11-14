# 016000 — Ends and Coends: Compatibility and Identification

**Track:** An Introduction to Category Theory. **Background:** products, coproducts, natural transformations, quotients, universal properties. **Theme:** two universal ways to assemble data indexed by a category.

<!-- BEGIN SPOKEN LECTURE -->

# Ends and Coends: Compatibility and Identification

Imagine a small organization that keeps two versions of a record. There is a simple summary for a public dashboard and a detailed version for its staff. Every time the detailed record changes, someone must produce the corresponding public summary. Now suppose we want to change how both versions are displayed. We could specify one transformation for the public record and another for the detailed record, but those choices cannot be independent. Transforming the detailed record and then summarizing must agree with summarizing first and then transforming the public record.

This is the familiar naturality condition. It demands a coherent family of operations across many related objects. The condition looks like a collection of equations. What if we wanted to build a single mathematical object whose elements are exactly all the families satisfying those equations? That is one motivation for an end.

There is a dual construction. Instead of selecting families whose pieces agree, suppose we gather pieces of data from many locations and identify pieces whenever a connecting map tells us that they represent the same thing. The resulting object is a quotient of a collection of pieces. A coend performs that kind of identification. Ends and coends sound like new technical names, but they express two very old mathematical habits: require compatibility, or impose identifications.

We will start with a two-stage system where the relevant equations can be written aloud, and only afterward move to the general universal properties.

## Two stages and one consistency equation

Let our category C have two objects, Detail and Summary, and one nonidentity arrow from Detail to Summary. An arrow represents the act of summarizing. It can be composed with identity arrows and obeys the usual category axioms.

Suppose a functor F assigns to each stage the available input records, and a functor G assigns to each stage the possible outputs. F and G also specify how their respective records are summarized. A transformation from F to G consists of two functions: one from detailed F records to detailed G records, and another from summary F records to summary G records.

If we chose those two functions independently, they might disagree. For a particular detailed record, we could transform it and then summarize the output. Or we could summarize the input and transform that summary. Naturality says the results must be identical, for every detailed record.

We have therefore turned the question 'which pairs of functions are allowed?' into a simple constraint. Take the set of all possible pairs of functions. Throw away the pairs that violate the commuting-square equation. The survivors are exactly the natural transformations from F to G.

This selection is a special case of an end. The general definition uses a functor with two inputs, one contravariant and the other covariant. But the purpose is already visible: compatible families are extracted from an initially larger product of choices.

## An example with numbers

Let's make the two-stage setup completely finite. At the detailed stage F has the two records zero and one, while at the summary stage F has just one record, called star. Summarizing either detailed record produces star. Let G have the same two detailed outputs and one summary output, with the same collapsing summary map.

How many natural transformations from F to G are there? At the detailed stage, we may choose any function from a two-element set to itself: there are four. At the summary stage, there is only one possible function from the singleton to itself. Every detailed function commutes with summarization, because both routes produce star. So there are four natural transformations.

Now alter G: keep two outputs at Detail but give Summary two possible labels, red and blue. Make G's summarization send both detailed outputs to red. A component at the public summary stage chooses either red or blue, while a detailed component remains one of four possible functions. Naturality forces the summary component to choose red, since summarizing the output of any detailed record always gives red. Thus four of the eight initially possible component pairs survive.

This deliberately small calculation shows why an end is an equalizer-like construction. A product gathers choices. Two different ways of transporting those choices along arrows yield two functions out of that product. The end contains precisely the choices on which those two functions agree.

## Equalizers as a familiar prototype

An equalizer of two functions from A to B is the subset of A where the functions give the same result. If the functions have no agreement points, the equalizer is empty. If they are equal everywhere, the equalizer is all of A. Equalizers are defined by a universal property: any function into A whose image satisfies the equation factors uniquely through the equalizer.

For natural transformations, there is not necessarily just one equation. Each arrow of the indexing category supplies a compatibility equation. But we can still gather all candidates into one big product, gather all comparisons into a second product, and take an equalizer of two maps between them.

For each object c of C, choose a function from F of c to G of c. That is one element of a product of function sets. Now consider an arrow from c to d. Its naturality comparison lives in the set of functions from F of c to G of d. One candidate is obtained by first applying the chosen function at c and then the G arrow. The other is obtained by first applying the F arrow and then the chosen function at d. The end keeps exactly those families for which these are equal for every arrow.

We have not yet spoken the symbol for an end, but we have already constructed an important one: the set of natural transformations. The compact notation hides the ordinary mechanism of product followed by compatibility equations.

## What the two inputs are doing

To describe general ends correctly, we need to account for arrows acting in opposite directions. Consider a rule H that accepts two objects of C and returns a set. In the first input it reverses arrows; in the second it follows arrows. Mathematicians call this a functor from the opposite of C times C into Set.

Why two inputs? Because our naturality equation combines a source index and a target index. The set of maps from F of c to G of d depends contravariantly on c and covariantly on d. An arrow that changes the source gets composed on the input side; an arrow that changes the target gets composed on the output side. These operations point in different directions.

An end of H packages a family of elements chosen from H at matching inputs, one element in H of c and c for every c. The family must satisfy the compatibility equations induced by each arrow. The result is universal among such compatible families.

The word 'universal' means more than 'collect them and hope'. Any other object equipped with a compatible family mapping into all those diagonal values must factor uniquely through the end. In Set this is usually a subset of a product. In other target categories the end need not literally be a set, but the universal property still identifies it.

There's a useful analogy to integration: the notation for an end uses an integral sign with the index below it. Yet an end is not generally the integral of a numerical function. The notation suggests combining information over all objects, while the mathematical substance is a particular kind of limit.

## Now reverse the construction

Suppose instead that we're assembling a catalog from data found at different stages. The detailed stage has two differently formatted records, while the summary stage has a canonical name for the object they both describe. We want a single collection of catalog entries, identifying any detailed record with the summary record it maps to.

The operation is no longer a subset of a product. We begin with a disjoint union of all candidates, preserving the stage where each candidate came from. Then we impose an equivalence relation generated by the indexing arrows. The quotient forgets distinctions that the structure says should not matter. This is the shape of a coend.

The distinction between a disjoint union and an ordinary union is important. Two labels that happen to be spelled the same may originally come from different stages. Disjoint union keeps their origins separate until the equations tell us to identify them. Conversely, two differently spelled labels may turn out to represent the same thing after we impose the relations.

A coend is universal for such identifications. Any collection of maps out of the diagonal pieces that respects the relations factors uniquely through the quotient. The end collected compatible input maps; the coend collects identified output classes. Their universal arrows point in opposite directions.

## A concrete coend with two objects

Take a category with objects Early and Late and one arrow from Early to Late. Let G assign a singleton to Early and the two-element set red and blue to Late. The arrow sends the unique early element to red. To collect all stages into one result, start with a disjoint union containing three tagged entries: early star, late red, and late blue.

The map from Early to Late tells us to identify early star with late red. Late blue remains separate. The quotient therefore has exactly two equivalence classes. It can be represented by red and blue. That is also the ordinary colimit of this simple diagram, and here it can be expressed as a coend with a constant contravariant weight.

Notice which information was lost. After passage to the quotient, we no longer distinguish the early star from the late red. We still distinguish blue. The categorical construction isn't deciding whether the data are 'really' the same in some external sense. It carries out precisely the identifications required by the specified maps.

If we changed the mapping so that early star went to blue, we would get a different quotient relation but still two classes. If the indexing category had two unrelated objects and no arrows between them, there would be no relations to impose, and the coend would just be a disjoint union. Those checks help ground the construction before more elaborate formulas enter.

## Coends of paired functors

One particularly useful situation starts with a contravariant functor P and a covariant functor Q, both indexed by the same category. At each object c, form pairs consisting of an element of P of c and an element of Q of c. Gather all the pairs from all objects, then identify pairs in a specific way whenever there is an arrow from c to d.

Take an element p living in P of d and an element q living in Q of c. The arrow lets us transport p backward to P of c, or q forward to Q of d. Those two transported pairs are declared equivalent. The coend is the quotient generated by all such relations.

You can think of the relation as sliding a transition from one side of a pair to the other. The point of using one contravariant and one covariant functor is that these two ways of passing across the arrow land in compatible places. If both directions were covariant, the displayed relation would not have the same types.

The construction turns up in tensor products, profunctor composition, and weighted colimits. But the general pattern is intelligible without those applications. It is a sum over intermediate states, with identifications that prevent us from counting two presentations of the same composite as different merely because we moved a transition across the boundary.

## A one-object example from algebra

Imagine the indexing category has only one object, but many arrows. Those arrows form a monoid under composition. A contravariant functor to sets is a right action of that monoid, while a covariant functor is a left action. The corresponding coend begins with pairs from the two sets and imposes the relation that acting on the right component by a monoid element is equivalent to acting on the left component in the matching way.

A familiar algebraic relative is the tensor product of a right module and a left module over a ring. There, in addition to the action identifications, one must also account for additive and scalar linearity. In the appropriate category of abelian groups, the coend description produces the usual tensor product. In Set, the analogous coend produces a balanced product of sets. We should not confuse the two simply because both are written using a tensor-like symbol.

This is a good example of a recurring theme. The universal pattern survives when we change the target category, but the actual quotient and its algebraic content depend on the target. Category theory can reveal a common construction while leaving plenty of concrete mathematics to verify.

## Multiple routes and generated equivalence relations

A quotient construction becomes more interesting when there are several ways to travel through a diagram. Suppose a middle stage can be reached by two separate arrows from an initial stage. Each arrow might transport one piece of data to a different label. In the coend, the relations generated by both arrows are imposed at once. If those relations share a representative, transitivity can force further identifications even when no single arrow explicitly stated the final equality.

For example, start with three tagged entries called first, middle, and last. One relation identifies first with middle; another identifies middle with last. The quotient has only one class, containing all three. It would be incorrect to apply the relations in isolation and report two partially merged sets. A coend uses the equivalence relation generated by all the relations: reflexivity, symmetry, and transitivity are part of the quotient operation.

The opposite kind of caution appears with ends. Suppose two component choices pass each consistency test separately but disagree on a third arrow that can be formed by composition. In a properly specified functorial system, naturality for the generating arrows implies naturality for their composites. We can therefore sometimes check fewer squares than the definition literally mentions, but only after verifying the chosen arrows really generate the category and identities behave correctly. Omitting an independent generator may admit a family that is not natural.

These observations are practical. Quotients must close identifications transitively; compatibility constraints can sometimes be reduced to generators. In each case the categorical universal property determines the completed result, while the computation can exploit a smaller presentation.


## Why the two constructions are dual

Ends and coends are dual in a formal sense. An end is a limit-like object determined by compatible arrows *into* the diagonal values. A coend is a colimit-like object determined by compatible arrows *out of* them. We can replace the target category by its opposite and switch one construction into the other, provided the needed limits or colimits exist.

The duality is easier to remember operationally. An end asks, 'Which families survive every consistency check?' A coend asks, 'Which presentations become the same after imposing every allowed identification?' Both begin with indexed pieces and turn the indexing arrows into constraints. The constraints have opposite effects: one selects a subobject, the other forms a quotient.

This also explains why natural transformations appear as an end. They are families of components that must commute with every structural arrow. And it explains why coends are natural tools for composition of generalized relations, where a composite may be represented in several ways through an intermediate object and those representations must be identified appropriately.

## What to check before using the notation

The first check is variance. A proposed end or coend requires a functor from the opposite of the indexing category times the original category into the target. The second check is size and existence. If the indexing category is large or the target category lacks needed products, coproducts, equalizers, or coequalizers, the construction may not exist in the form we want. The third check is the specific universal property: does the candidate object classify exactly the compatible families or identification-respecting maps?

For the natural-transformation example in Set, we can prove the answer from the equalizer. A pair of component functions lies in the end if and only if it satisfies every naturality square. That is both necessary and sufficient. For the two-stage quotient, we can prove that any map from the three tagged entries respecting the early-to-late identification factors uniquely through our two-element quotient. We don't have to rely on a suggestive diagram.

An often useful debugging strategy is to test the construction on a category with no nonidentity arrows. Then an end is simply a product of diagonal values, and a coend is a coproduct of them. Any formula that fails this simple test has probably assigned one of its arrows in the wrong direction.

## Why these constructions earn their place

Category theory can feel like an endless procession of names unless we know what problem each definition solves. An end packages all the compatibility equations of an indexed system into a single universal object. A coend packages all the identifications of an indexed system into another universal object. They let us reason about the completed assembly instead of continually rechecking the entire list of relations.

Both constructions also give us a way to understand higher-level category-theoretic tools. Kan extensions, which we will study through concrete data-extension problems, can be computed by colimits or by coend formulas under appropriate hypotheses. The coend does not invent the content; it organizes the fact that multiple routes of presenting the same information should be treated coherently.

Go back to the opening organization with its detailed and public records. If we want two display transformations to work together, we need an end-like compatibility condition. If we want to merge records across the two stages while treating transported copies as the same entry, we need a coend-like identification. The examples sound different because the constructions answer different questions. But both have the same governing ambition: make a collection of local maps into one mathematically controlled object.


<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For small \(C\) and a functor \(H:C^{op}\times C\to\mathbf{Set}\):

- The **end** \(\int_c H(c,c)\) is the equalizer
  \[
  \prod_{c}H(c,c)\rightrightarrows \prod_{f:c\to d}H(c,d),
  \]
  with components induced by \(H(1_c,f)\) and \(H(f,1_d)\).
- The **coend** \(\int^{c}H(c,c)\) is the coequalizer
  \[
  \coprod_{f:c\to d}H(d,c)\rightrightarrows \coprod_c H(c,c).
  \]
  The two arrows are \(H(f,1_c):H(d,c)\to H(c,c)\) and \(H(1_d,f):H(d,c)\to H(d,d)\).

For \(F,G:C\to D\) and locally small \(D\), use \(H(c,d)=D(Fc,Gd)\) to get
\[
\operatorname{Nat}(F,G)\cong\int_c D(Fc,Gc).
\]
For \(P:C^{op}\to\mathbf{Set}\), \(Q:C\to\mathbf{Set}\):
\[
\int^c P(c)\times Q(c)=\bigl(\coprod_c P(c)\times Q(c)\bigr)/\sim,
\quad (P(f)p,q)_c\sim(p,Q(f)q)_d
\]
for \(f:c\to d\), \(p\in P(d)\), \(q\in Q(c)\). The quotient is by the equivalence relation **generated** by these pairs.

### Exercises with answers

1. **Exercise:** If \(C\) is discrete on two objects, what is an end? **Answer:** The product of the two diagonal values; there are no nonidentity compatibility conditions.
2. **Exercise:** In the same discrete case, what is a coend? **Answer:** The coproduct of diagonal values.
3. **Exercise:** Why is \(\operatorname{Nat}(F,G)\) an end? **Answer:** Its elements are exactly component families satisfying \(G(f)\eta_c=\eta_dF(f)\) for each arrow.
4. **Exercise:** For Early \(\to\) Late with \(G(\mathrm{Early})=\{*\}\), \(G(\mathrm{Late})=\{r,b\}\), arrow sending \(*\mapsto r\), how many classes are in the colimit? **Answer:** Two, since the early element is identified with \(r\), leaving \(b\) separate.

### References

- Emily Riehl, *Categorical Homotopy Theory*, section on Kan extensions and coends, https://emilyriehl.github.io/files/cathtpy.pdf
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/files/context.pdf
- Fosco Loregian, *Coend Calculus* (formerly *This is the (Co)end, My Only (Co)friend*), https://arxiv.org/abs/1501.02503
- nLab, “end,” https://ncatlab.org/nlab/show/end
