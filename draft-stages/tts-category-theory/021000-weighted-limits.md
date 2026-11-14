# 021000 — Weighted Limits: When a Diagram Asks More Than One Question

**Track:** An Introduction to Category Theory. **Background:** functions, products, pullbacks, functors and naturality, developed from finite tables. **Theme:** weights specify how many compatible probes each part of a diagram requires; enriched weighted limits generalize the construction.

<!-- BEGIN SPOKEN LECTURE -->

# Weighted Limits: When a Diagram Asks More Than One Question

A database contains a table of people and a table of departments. Every person belongs to a department. Suppose a reviewer asks for two people, possibly the same person, who belong to the same department. We can express the task directly: choose a first person, choose a second person, and require that their department labels agree.

This is a pullback calculation. But what if we want to describe the request without building the pullback diagram from scratch? Could we keep the original diagram of people mapping to departments, then attach a separate description of how we want to probe it? That is the motivation for a weighted limit.

Ordinary limits ask for compatible values across every object of an indexing diagram. Weighted limits separate the diagram of available data from a weight describing the shape of the query. The distinction becomes clearer with a finite example: one original arrow, a weight containing two requests at its source and one at its target, and a five-element answer set.

## A diagram with one arrow

Let A be the set of three employees, numbered zero, one, and two. Let B be the set containing two departments, called East and West. A function f from A to B records where each employee works. Employees zero and two belong to East; employee one belongs to West.

This data is a diagram of shape one arrow. There are two positions in the indexing category, call them zero and one, with one nonidentity arrow from zero to one. At position zero the diagram stores A. At position one it stores B. Along the arrow it stores f.

If we take the ordinary limit of this arrow-shaped diagram, what is the result? A cone from a set X consists of a function from X to A and a function from X to B whose values agree after applying f. Once the function to A is chosen, the function to B is forced to be f composed with it. So the ordinary limit is isomorphic to A itself.

This is mathematically correct, but it does not answer our request for a pair of employees in the same department. That request has two independent choices of employee and one shared choice of department. The original diagram has only one source slot. We could manually duplicate the source object and construct a span with two arrows from A to B, then take a pullback. A weighted limit does this duplication in a controlled way while keeping the original indexing diagram intact.

## Attaching a weight to the diagram

A weight is another functor on the same indexing category, but with values in sets. At the zero position, give it a two-element set. Think of the elements as the first employee slot and the second employee slot. At the one position, give it a one-element set representing the department slot. Along the indexing arrow, send both employee slots to that single department slot.

The original diagram tells us what data exists and how its objects relate. The weight tells us how many questions we want to ask of each piece and which questions must correspond under the diagram's arrows. We need two people and one department, and both people are required to report to that same department.

To evaluate the weighted limit, first pretend the answer set L exists and ask what a function from any test set X into L should provide. For every employee slot in the weight, it must provide a function from X to A. For the department slot, it must provide a function from X to B. And these choices must be natural with respect to the arrow: applying f to either employee-valued function must give the same department-valued function.

For the simplest test set containing only one element, this means selecting a first employee a, a second employee a prime, and a department b with f of a equal to b and f of a prime equal to b. Eliminating b leaves exactly the pairs of employees with the same department. So L should be the fiber product of A with itself over B.

## Counting the five answers

Let's enumerate the answers rather than trust the notation. Employee zero and employee two share East, so both ordered pairs zero with two and two with zero are allowed. Each employee can be paired with themselves, so zero with zero, one with one, and two with two are allowed. That is five pairs in total.

What about zero with one? They belong to different departments, so it is excluded. One with two is excluded for the same reason. A two-element ordered pair is not a set of two people. The order of the slots is meaningful: zero with two and two with zero occupy different points of the answer set. We explicitly permit the two slots to contain the same employee. If a problem required distinct employees, we would add an inequality condition not encoded by the present pullback.

This little calculation illustrates how much a weight specifies. The two source elements in the weight label two independent variables. The single target element identifies their outputs. The arrow in the original indexing category supplies the function f. The naturality requirement forces the equations. The weighted limit packages the resulting five-element set and its universal property.

If we replaced the source weight by a one-element set and kept one department slot, the request would simply choose one employee and report their department. We would recover the ordinary arrow limit, which is A. If we changed the target weight to two separate department slots and matched each employee slot to its own target slot, there would be no requirement that the employees belong to the same department. The answer set would be A times A, with nine ordered pairs. The difference between five and nine is precisely the compatibility required by the shared target slot.

## The universal property behind the count

Counting singleton-valued answers is useful, but a limit is defined by how it interacts with every test object. For an arbitrary set X, a function from X into the five-element pair set amounts to choosing two functions a and a prime from X to A that satisfy f after a equals f after a prime, point by point.

Why is this an exact correspondence? Given a map X into the pair set, project each pair onto its first and second coordinates. The two projections are functions into A. Because every chosen pair shares a department, the required equation holds. Conversely, given two functions into A satisfying that equation, send each x in X to the ordered pair of their values. Every such pair belongs to our five-element set. The two constructions are inverse.

Moreover, they commute with changing the test set X by a function. If we precompose a map X to L with a function from Y to X, the projected employee functions are simply precomposed with that same function. This naturality in X is what makes the correspondence a universal property rather than a coincidence for one input size.

The weighted-limit definition abstracts precisely this behavior. It says that maps from any test object into the weighted limit correspond naturally to compatible maps from the weight into the diagram's hom-sets. In the category of sets, those compatible maps are natural transformations of functors on the indexing category.

That sounds like a larger amount of structure than our five answers need. But the additional structure is what makes the construction portable. We can replace our specific A, B, and f with other sets and functions and keep the same weight. The universal property then determines the appropriate compatibility object, without rewriting the selection procedure by hand.

## How ordinary limits fit inside

Ordinary limits are weighted limits for the constant singleton weight. At every index position, the weight has one point, and every indexing arrow sends that point to the point at its target. A natural map from this weight into a hom-valued diagram chooses one compatible map into each diagram object. That is exactly a cone.

The constant singleton weight does not mean that every ordinary limit is a terminal object. It means the weight requires one component at each position, with compatibility across the arrows. The answer still depends on the original indexing diagram. For a discrete two-object diagram it gives a product. For a parallel-pair diagram it gives an equalizer. For a span it can give a pullback.

This observation is valuable because it explains ordinary limits as one particularly symmetric kind of request. Nothing in the categorical machinery forces us to give every position exactly one query slot. We may need zero slots, several slots, or more structured collections of slots. The weight formalism lets the same universal-property language handle these cases.

The weights themselves must be functorial. If the indexing diagram has two composable arrows, the slot transport along their composite must agree with transporting first along one and then along the other. Otherwise the query would give contradictory instructions about which slots are supposed to represent the same information.

## The category of elements removes the mystery

There is another way to understand a set-valued weight. Replace every slot in the weight by its own indexing position. In our example, the two employee slots become two separate nodes, and the shared department slot becomes a third node. Each employee slot has an arrow to the department slot, because the weight sends both of them to the same target slot.

This new three-node shape is the category of elements of the weight. It turns the weighted query into an ordinary diagram: two copies of A with arrows to one copy of B. The ordinary limit of that span is exactly our same-department pair set.

That gives us a rigorous construction technique. For weights valued in ordinary sets and under the appropriate smallness assumptions, the weighted limit can be computed as an ordinary limit after pulling the original diagram back along the projection from the category of elements of the weight. The weight does not create a new supernatural kind of limit; it specifies an indexing category built from the slots and their transport.

This translation also makes it easier to debug examples. If you are uncertain about the abstract natural-transformation formula, draw one node for each slot and one arrow for each required slot mapping. Evaluate the original diagram on those nodes and arrows, and take an ordinary compatible family. For a small finite weight, the result is often a familiar product, pullback, or equalizer.

The categorical language becomes especially useful when many examples share the same weight. We can prove a single property of the query shape instead of proving independent facts about every copied diagram we construct.

## A weight that evaluates a diagram

A second important example is almost the opposite of duplication: a weight can select the value of a diagram at one designated index. Fix an index object j. Let the weight at another object k be the set of arrows from j to k. An element of the weight represents a way to reach k from the chosen index.

Now a natural map from this representable weight into the diagram's hom-sets is determined by its component at the identity arrow of j. This is exactly the ordinary Yoneda argument. The resulting weighted limit is isomorphic to the diagram's value at j.

For our arrow-shaped index, choose j equal to the source. The representable weight has one slot at the source and one at the target, with the obvious transport. Its weighted limit is A. Choose j equal to the target. The representable weight has no slots at the source and one at the target, so its weighted limit is B.

This is a useful mental distinction. The constant singleton weight asks for a cone. A representable weight asks for evaluation. Our earlier two-to-one weight asked for two compatible employees. All three use the same original diagram, but they ask different questions. The mathematics of the answer is controlled by both the diagram and the weight.

Yoneda appears here because a representable weight is a canonical way of probing a functor. Weighted limits generalize that idea from one distinguished probe to an entire functor of probes.

## Why introduce weights if everything is still a limit?

In the category of sets, one can often replace a weighted limit by an ordinary limit indexed by a larger category. That could make weights appear like a verbose shortcut. Their deeper purpose is to expose structure that would otherwise be hidden in a complicated indexing construction, and to generalize correctly to categories enriched over something other than sets.

Suppose a category's morphisms carry a topology, an order, a linear structure, or a metric-like quantity. A diagram is then an enriched functor. A weight also takes values in the enriching category. The compatibility between them is expressed through enriched natural transformations, whose comparisons themselves live in that enriching category.

Ordinary unweighted indexing categories may not capture all these enriched requirements. For instance, a power of an object indexed by a set of labels is a weighted limit in the set-enriched setting. In a more general enriching category, an analogous power or cotensor may ask for a genuinely structured family of probes, not simply a collection of independent copies.

The general formula requires a closed symmetric monoidal enriching category and appropriate ends and enriched hom-objects, or sufficient hypotheses in another suitable setting. It is not correct to write down the same expression and assume the weighted limit exists in every enriched category. Existence is a theorem to establish or a condition to assume.

## Duality with weighted colimits

We can reverse the construction. Ordinary colimits identify data along arrows rather than select compatible tuples. Weighted colimits attach a weight telling us how components contribute and how their representations are glued together. They can be described using an enriched coend when the requisite structure exists.

In sets, a copower by a two-element set gives two disjoint copies of an object, whereas a power by a two-element set gives ordered pairs of elements. You can hear the duality: a power asks us to choose a value for each slot; a copower provides a copy labeled by each slot. Products and coproducts, ends and coends, limits and colimits all participate in the same pattern.

Our employee example was a weighted limit because we were collecting compatible choices. If we instead wanted to assemble records from sources while identifying records that describe the same underlying entity, the weighted-colimit perspective might be appropriate. The exact equivalence relation would need to be supplied by a diagram or a weight; the construction does not magically decide which records refer to the same person.

This connection helps with Kan extensions, too. Pointwise Kan extensions are built from diagrams of limits and colimits. Weighted versions can be expressed by ends and coends that look like integrating a diagram against a hom-valued weight. The family of constructions that can seem unrelated in separate chapters is really a set of variations on compatibility and identification.

## A parallel-arrow weight and an equalizer

There is another illuminating finite query. Suppose the indexing category has two parallel arrows from object zero to object one. A diagram assigns a set A to zero, a set B to one, and two functions f and g from A to B. The ordinary limit is the set of elements a of A for which f of a equals g of a. That is an equalizer.

Take A to be the integers zero, one, and two, and B the integers zero and one. Let f return the remainder upon division by two, so its values are zero, one, zero. Let g always return zero. The equalizer contains zero and two. We can compute this by taking a constant singleton weight on the parallel-arrow indexing category. A natural choice of a map from X into A must be compatible with both arrows to B; therefore f after that map equals g after it.

What if the weight at the source has two labeled slots, while the target has one slot, and both parallel arrows send both source slots to the target slot? Then the weighted limit asks for two potentially different elements of the equalizer. For these particular functions, both equalizer elements have the same output zero, so its answer is the square of the equalizer: zero with zero, zero with two, two with zero, and two with two. For a different pair of functions, the weight would additionally require the two chosen equalizer elements to have the same image in B. In this example the same weight does two jobs. It imposes the equalizer condition on each source slot and it allows the slots to vary independently once that condition has been met.

The exercise helps expose a misconception. A weight with two source slots does not automatically mean 'take the product of two copies of A and stop'. The arrows in the indexing category determine whether the two choices are required to satisfy additional equations. A weight provides slots and their transport. A diagram supplies operations, and the naturality equations link them.

## When the indexing choices are genuine modeling choices

There are two separate design decisions when one writes down a weighted limit. First choose the category J describing the structure of the available diagram. Then choose a weight W describing which compatible probes to ask of that diagram. The same raw data can be indexed in different ways, but those choices are not innocent if they encode different transformations.

For instance, storing employee assignments as an unstructured table of pairs gives us a set of records. Treating them as a function from employees to departments gives us a diagram with one arrow. If we also know that departments are organized by region, we can add another object and another arrow. A weight can then ask for two employees in the same department, or for employees whose departments lie in the same region, by giving appropriate slots and maps into the deeper diagram.

This creates a disciplined way to express relational queries. The labels in a weight carry the roles of variables, while the arrows explain how equalities must be propagated. The universal property guarantees that every compatible assignment is represented once by a map into the answer object. For set-valued examples, one can check the answer by constructing the category of elements and computing an ordinary limit, making the query independently testable.

## What we have established

We began with one simple function from three employees to two departments. The ordinary limit of that arrow is essentially the employee set itself. A two-to-one weight asks a different question: choose two employees whose department assignments agree. Its weighted limit is a five-element pullback, and its universal property says every compatible pair of functions factors uniquely through that answer set.

The weight is a functor of query slots. The diagram is a functor of data. Natural transformations between the weight and the diagram's hom-valued probes encode the compatibility equations. Constant singleton weights recover ordinary limits; representable weights recover evaluation; and the category of elements turns set-weighted limits back into familiar ordinary diagrams.

Weighted limits are therefore a way to state which relationships a construction is supposed to preserve. They allow us to reuse a diagram while changing the question we ask of it. In enriched settings, they extend the same idea to structured notions of relationship, provided the necessary enriched limits exist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(J\) be small, \(D:J\to\mathcal C\), and \(W:J\to\mathbf{Set}\) a weight. A Set-weighted limit \(\{W,D\}\) represents the functor
\[
\mathcal C(X,\{W,D\})\cong [J,\mathbf{Set}](W,\mathcal C(X,D-))
\]
naturally in \(X\). The weight variance is **covariant** for limits with this convention. With constant singleton \(W=1\), this is the usual conical limit. For representable \(W=J(j,-)\), Yoneda gives \(\{W,D\}\cong Dj\).

**Finite kernel-pair calculation:** Let \(J=(0\xrightarrow{u}1)\), \(D0=A=\{0,1,2\}\), \(D1=B=\{E,W\}\), \(D(u)=f\) with \(f(0)=E,f(1)=W,f(2)=E\). Let \(W0=\{s,t\}\), \(W1=\{*\}\), with both slots mapping to \(*\). Then
\[
\{W,D\}=A\times_B A=\{(0,0),(0,2),(1,1),(2,0),(2,2)\}.
\]
For any set \(X\), a natural transformation \(W\to\mathbf{Set}(X,D-)\) is exactly a pair \((a_s,a_t):X\to A\times A\) satisfying \(f\circ a_s=f\circ a_t\); hence the universal property.

Let \(\mathrm{el}(W)\) denote the category of elements of the covariant functor \(W\); projection \(\pi:\mathrm{el}(W)\to J\) makes \(\{W,D\}\cong\lim_{\mathrm{el}(W)}D\circ\pi\), where these limits exist. For this weight \(\mathrm{el}(W)\) is \(s\to *\leftarrow t\), recovering a pullback.

For a complete suitable symmetric monoidal closed enriching category \(\mathcal V\), the enriched weighted limit satisfies
\[
\mathcal C(X,\{W,D\})\cong[J,\mathcal V](W,\mathcal C(X,D-))
\]
as an isomorphism **in \(\mathcal V\)**. Conditions on size, ends and existence matter.

### Exercises with answers

1. **Exercise:** Why does the employee weight give five ordered pairs rather than nine? **Answer:** Both slots map to one department slot, imposing \(f(a)=f(a')\).
2. **Exercise:** What does the constant singleton weight recover? **Answer:** The ordinary conical limit of the diagram.
3. **Exercise:** What does \(W=J(j,-)\) compute? **Answer:** Evaluation at \(j\), so \(\{W,D\}\cong D(j)\).
4. **Exercise:** What is the category of elements for the two-to-one weight? **Answer:** A span of two source slots both pointing to one target slot, whose pulled-back diagram is \(A\to B\leftarrow A\).

### References

- G. Tendas, *Enriched Categories: Theory and Examples*, https://gtendas.github.io/pdfs/ECTE.pdf
- F. W. Lawvere, *Metric Spaces, Generalized Logic and Closed Categories*, https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- Saunders Mac Lane, *Categories for the Working Mathematician*, https://link.springer.com/book/10.1007/978-1-4612-9839-7
