# 024000 — Fibrations: How Categories Vary with Their Contexts

**Track:** Introduction to Category Theory. **Background:** categories, functors, pullbacks, reindexing. **Theme:** indexed categories, cartesian arrows, and Grothendieck construction.

<!-- BEGIN SPOKEN LECTURE -->

# Fibrations: How Categories Vary with Their Contexts

Consider a small organization with two teams. Each team has its own set of documents, and each document comes with permitted ways to transform it: editing it, restricting what it contains, or translating it into another format. If someone changes teams, the documents available to them also change. We need to talk about the transformation of documents and the change of context in which a document lives.

Ordinary category theory handles either kind of change comfortably. One category can describe contexts; another can describe documents and their transformations. But the two kinds of change are coupled. A document meaningful in one context may have to be pulled back or reinterpreted in another. How do we express the dependence without losing the distinction between a change of context and a change of object within a context?

A Grothendieck fibration is one answer. The name carries substantial machinery, but its purpose is practical: it organizes a family of categories that varies over the objects and arrows of a base category. We will construct one using ordinary sets and functions, understand which arrows deserve to be called cartesian, and then see why the entire construction can be read either as one category over another or as a system of reindexing functors.

## A family of sets over a context

Begin with a context set Gamma containing Ada and Bo. Give Ada a two-element set of available roles and Bo a three-element set. The family is simply a function that assigns to each person a set. Collect all valid pairs, consisting of a person and one of their allowed roles, into one total set E. There are five such pairs. The projection from E to Gamma remembers only the person.

Now imagine a second context Delta consisting of morning, afternoon, and evening shifts. A function sigma assigns a person to each shift: Ada in the morning, Bo in the afternoon, Ada in the evening. We want to reexpress the original role family over shifts. The result has two roles over morning, three over afternoon, and two over evening.

There is a set-theoretic way to get exactly that result. Form the pullback of the role projection E to Gamma along sigma from Delta to Gamma. An element of the pullback is a shift together with a role valid for the person assigned to that shift. It has seven elements. The pullback comes with a map to Delta, making it a family over the new context.

The same operation works for every function of contexts and every family over the target context. The direction is important: sigma goes from Delta to Gamma, but it transforms families over Gamma into families over Delta. The reindexing operation is contravariant in the context arrow.

This concrete operation is the foundation of the theory. A change of context should not demand that we rebuild all the mathematics of the relevant objects. It should tell us how to transport them along the change.

## Slices as categories of context-dependent objects

For a fixed context Gamma, consider not just one family but every set equipped with a function to Gamma. Such an object could be the role family, a family of device settings, or a family of allowed responses. A map between two families over Gamma is a function between their total sets that preserves the context coordinate. If an element lies above Ada, its image must also lie above Ada. This is a slice category, written Set over Gamma.

The word over indicates that every object carries a map to Gamma. A map in the slice category cannot arbitrarily send a role assigned to Ada into one assigned to Bo. It must commute with the two projections. Thus the slice category remembers the internal transformations available while the context is held fixed.

What happens when Gamma changes? Our earlier pullback operation transports an entire family over Gamma to a family over Delta. It also transports every map of families. Given a context-preserving function h between total sets, send an element of the pulled-back source family to the same shift paired with the image under h. That is a map of the pulled-back families. Identities and compositions are preserved, so reindexing is a functor from Set over Gamma to Set over Delta.

Notice the two levels. Within a context we have objects and arrows of a slice category. Between contexts we have a reindexing functor connecting the slice categories. This is a category-valued version of an indexed collection. Instead of assigning each context a plain set, we assign it a whole category.

## Why the direction reverses

Suppose we have a chain of contexts: a schedule of daily shifts maps to the employees assigned to those shifts, and each employee maps to the department employing them. We can start with a family of permissions indexed by department. Pull it back to employees, then pull the result back to shifts. Or we can compose the shift-to-employee map with the employee-to-department map and pull the permission family back in one step.

Both constructions describe the same assignments: a shift and a permission allowed for the department of its assigned employee. In elementary set theory they are canonically isomorphic. With a systematic choice of concrete representations, we can make a corresponding strictly functorial version, but ordinary pullbacks chosen one at a time are generally canonical only up to coherent isomorphism.

The categorical slogan is that a context map from Delta to Gamma induces a reindexing functor in the opposite direction, from the category of objects over Gamma to the category of objects over Delta. A composite context map induces the composite reindexing operation with the order reversed. Identity context maps act as identity reindexing, either strictly in a split presentation or up to coherent isomorphism in the more general setting.

This reversal is not an oddity imposed by abstract notation. It is what happens whenever information is indexed by a variable and then the variable is replaced by an expression. The expression goes from a new context into an old one; the old indexed family is reinterpreted in the new context.

## One total category instead of many slices

We can now ask whether all these separate slice categories can be assembled into one ordinary category. It would contain every family over every context, along with maps that may change the context and transform the family at the same time.

An object is a pair consisting of a context Gamma and a family over Gamma. An arrow from a family over Delta to a family over Gamma includes a function sigma from Delta to Gamma and a function from the total set over Delta into the total set over Gamma that commutes with the projections. This is an arrow between families that covers sigma.

There is an obvious functor from the large category to the category of contexts. It sends each family to its underlying context and each family map to the context map it covers. We can think of the large category as the total category and the smaller one as the base.

This packaging is helpful because it makes two different kinds of arrows live in one place. A vertical arrow stays over an identity context map: it transforms a family without changing the context. A nonvertical arrow changes context as well. But among the context-changing arrows, some have an especially strong universal property. Those are the cartesian arrows.

## The cartesian arrow from a pullback

Take sigma from Delta to Gamma and a family E over Gamma. Pull E back to Delta. The resulting family sigma-star E comes with a canonical map into E that covers sigma. This map is cartesian.

To understand that word, imagine another context Theta, a map from Theta to Delta, and a family Z over Theta. Suppose we already have a map from Z into E whose underlying context map is the composite from Theta through Delta to Gamma. We want to factor the family map through sigma-star E, using the Theta-to-Delta context map.

The pullback property says there is exactly one such factorization. A point of Z knows its Theta-context, hence its Delta-context, and it already has an image in E that lies over the corresponding Gamma-context. Those two pieces of data form exactly one point in the pullback family. There is no ambiguity.

This lifting property is the definition of a cartesian arrow in a fibration, expressed at the level of the total category and its projection. A Grothendieck fibration is a projection functor for which, given any base arrow pointing to the context of an object, an appropriate cartesian arrow above it exists.

The word cartesian does not require that the entire total category be a cartesian product. It refers to the universal property of certain lifts. Those lifts are what allow us to transport objects back along arbitrary base arrows.

## Checking the uniqueness in an example

Let Gamma have Ada and Bo, and let E consist of the five person-role pairs. Let Delta have the three shifts from before, and sigma assign each shift a person. The pulled-back family has seven shift-role pairs.

Suppose Theta consists of two work tickets, one assigned to the morning shift and one to the afternoon shift. A map from the ticket family Z into E assigns to each ticket a role permitted for the person on the corresponding shift. To factor through the pullback, the ticket must map to a shift-role pair. The shift coordinate is forced by the given ticket-to-shift map. The role coordinate is forced by the given map into E. Hence there is one and only one possible factorization.

Notice that this universal property is stronger than simply having the same number of objects after reindexing. It asserts that any compatible map from any other family factors uniquely. Counting seven shift-role pairs is a useful check, but cardinality alone cannot establish the cartesian property.

We also see why a random context-changing map need not be cartesian. If it discards two valid roles over a shift, another family may try to map to one of those missing roles in E. The required factorization will not exist. If it duplicates a role in a way that creates two choices, uniqueness can fail. The cartesian condition captures faithful reindexing of the entire family.

## The Grothendieck construction

We can now build the total category in a second way. Start not with one category of arrows over all contexts, but with an indexed category F. For each context b, F of b is a category of objects living at b. For each base arrow u from b to c, there is a reindexing functor u-star from F of c to F of b.

The Grothendieck construction assembles these into a total category. Its objects are pairs: a context b and an object x in F of b. An arrow from the pair b,x to c,y consists of a base arrow u from b to c and an arrow in F of b from x to the reindexed object u-star y.

This formula tells us exactly where the comparison arrow lives: in the source fiber, over b. We first pull the target object back along u, and then compare the source object to that pullback within one category. We do not attempt to draw an arrow directly between objects that inhabit different fibers without first specifying how the fibers relate.

For our family-of-sets example, F of b is the slice category Set over b. An object of the assembled category is a context and a family over it. An arrow is a context map plus a map into the pulled-back target family. By the universal property of pullback, that is equivalent to a commuting square between the original total sets. We have recovered the earlier category of families over changing contexts.

## Composition in the assembled category

Suppose x lies over a, y lies over b, and z lies over c. Let u take a to b and v take b to c. A morphism from a,x to b,y consists of u and an arrow from x to u-star y. A morphism from b,y to c,z consists of v and an arrow from y to v-star z.

To compose, first reindex the second fiber arrow along u, obtaining an arrow from u-star y to u-star of v-star z. Compose it with the first fiber arrow. Then use the coherent comparison between pulling back twice and pulling back along the composite v after u. The result is an arrow from x to the pullback of z along the composite base map.

The operation is associative because the reindexing comparisons satisfy coherence equations. If the indexed categories are strictly functorial, these equations simplify to ordinary equalities. For a pseudofunctor they are natural isomorphisms subject to compatibility laws. Keeping that distinction is essential when the models involve choices of pullback objects.

We can also identify the cartesian arrows directly. For a base arrow u from b to c and an object y over c, take the source object to be u-star y and the fiber arrow to be its identity. The resulting total-category arrow covers u and has exactly the universal lifting property described earlier.

## The equivalence of two descriptions

A fibration can be regarded as a collection of fibers with reindexing between them, or as one category E equipped with a projection to a base B and enough cartesian arrows. These are equivalent presentations, with qualifications about the choices of cartesian lifts and pseudofunctor coherence.

To recover an indexed category from a fibration, take the fiber over each base object. For a base arrow, choose cartesian lifts, and use their universal properties to define how objects and morphisms reindex. Different choices of lifts lead to canonically isomorphic reindexing data. To go the other direction, apply the Grothendieck construction we just worked through. Under the appropriate notion of morphism between structures, these procedures give an equivalence of the relevant two-dimensional categories.

This equivalence is useful because the two pictures support different kinds of reasoning. When you care about substitution of contexts, the indexed picture makes contravariant reindexing easy to see. When you care about factorization and universal arrows, the total-category picture is more natural. You can move between them without abandoning the mathematical content.

## A set-valued special case

There is an illuminating simpler version. Start with a presheaf P on a category C: each context c gets a set P of c, and each arrow u from b to c induces a function P of c to P of b. Regard each set as a discrete category, where only identity arrows exist.

The Grothendieck construction then has objects consisting of a context and an element of the set assigned to that context. An arrow from b,x to c,y exists over u precisely when x equals the restriction of y along u. This is the category of elements of the presheaf.

There are no interesting vertical transformations because the fibers are discrete. Yet the same local-to-global machinery is already visible: a value at one context can restrict to another, and compatible restrictions determine the arrows of the category of elements. General fibrations replace each discrete set with a category containing its own nontrivial morphisms.

This is also why the category of elements appears when expressing presheaves as colimits of representables and when calculating Kan extensions. The construction provides a way to turn indexed information into a category whose arrows remember both the base change and the compatibility condition.

## Why vertical maps are needed too

A presheaf gives a set of possible values for each context and functions that restrict values along context maps. That is enough for many counting and membership questions. But sometimes the objects living over a context have their own meaningful arrows. A report may be summarized into a shorter report while staying under the same department. A configuration may be refined while its environment remains unchanged. A proof may be transformed into a simpler proof with the same assumptions.

In the total category, those are vertical arrows. If the base context is unchanged, the projection sends the arrow to an identity. In the indexed picture, vertical arrows are just morphisms inside the fiber category. A change of context must reindex the vertical arrow as well as its source and target objects. That requirement explains why an indexed category assigns functors, rather than merely assigning sets of objects.

Take two role families E and H over Gamma and a context-preserving map that assigns to every E-role a compatible H-role. Pull both families back along sigma from Delta to Gamma. The original map induces a new map between the pulled-back families over Delta. Its value on a pair consisting of a shift and a role is the same shift paired with the mapped role. This construction respects the context projection automatically. With three shifts, it works independently in each of the two, three, and two-element fibers of our running example.

The example shows a useful difference between reindexing and changing an object. Reindexing changes which context is used to interpret a role. A vertical transformation changes the role-valued data while leaving the context fixed. A general arrow in the total category combines these operations, and the cartesian property lets us factor that combination in a controlled way.

## Where dependent types enter

In dependent type theory, a type is allowed to depend on the values of variables in a context. A substitution assigns terms to those variables. Reindexing a family along the substitution produces the type that should be used in the new context. This is exactly the direction of the pullback operation.

A context-indexed category can contain not only a collection of possible types but also morphisms between structured objects over a context. A comprehension-category model selects projections that represent adding dependent variables to contexts. Such models require more structure than the bare fibration property if we want to interpret specific type formers and their computation rules.

One must also distinguish strict and weak substitution. A syntax may assert that substituting an identity or composing substitutions gives literally equal terms. An arbitrary fibration often supplies reindexing only up to coherent isomorphism. Obtaining a model of the strict syntactic equations may therefore require chosen, coherent structure. The difference becomes important in computer-checked mathematics, where definitional equality and propositional equivalence play separate roles.

## The outcome of the construction

Return to the organization with contexts and document families. Instead of pretending all documents inhabit one undifferentiated universe, we organize a category of objects for each context and reindex it when the context changes. The Grothendieck construction turns those many categories into one total category and singles out cartesian arrows as the correct way to transport information across contexts.

The most important calculation is simple enough to retain: a change of context points from Delta to Gamma, while reindexing objects points from the category over Gamma back to the category over Delta. A cartesian lift turns that backward transportation into a universal arrow in the total category. And the two descriptions, indexed and fibered, encode the same kind of mathematical dependence.

This provides language for dependent types, presheaves, geometry, databases, and other settings where what counts as an object depends on where one is standing. The construction does not eliminate those dependencies. It records them so that transporting, comparing, and composing dependent objects become disciplined mathematical operations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For \(B=\mathbf{Set}\) let \(F:B^{op}\to\mathbf{Cat}\) send \(\Gamma\mapsto \mathbf{Set}/\Gamma\) and \(\sigma:\Delta\to\Gamma\) to the pullback functor \(\sigma^*\). Arbitrarily selected pullbacks give a pseudofunctor; a split presentation requires choices with strict identity/composition equations.

For a pseudofunctor \(F:B^{op}\to\mathbf{Cat}\), objects of \(\int_BF\) are \((b,x)\), \(x\in F(b)\). A morphism \((b,x)\to(c,y)\) is \((u:b\to c,\ f:x\to F(u)(y))\) with \(f\in F(b)\). If \((v,g):(c,y)\to(d,z)\), composition is represented by
\[
x\xrightarrow{f}F(u)y\xrightarrow{F(u)g}F(u)F(v)z\xrightarrow{\cong}F(vu)z.
\]

A morphism \(q:e'\to e\) of \(E\) over \(u:b'\to b\) is \(p\)-cartesian if, for any \(g:z\to e\) over \(u v\), where \(v:p(z)\to b'\), there exists a unique \(h:z\to e'\) over \(v\) with \(qh=g\). A fibration has cartesian lifts for every such \(u,e\).

For \(P:B^{op}\to\mathbf{Set}\), the category of elements has \((b,x\in P(b))\) as objects, and \(u:(b,x)\to(c,y)\) iff \(x=P(u)(y)\).

### Exercises with answers

1. **Count a pullback.** Ada has two roles, Bo three; shifts map Ada, Bo, Ada. **Answer:** total pullback cardinality \(2+3+2=7\).
2. **Factorization.** Explain why the pullback arrow is cartesian. **Answer:** every compatible pair of maps into its legs defines a unique mediating map.
3. **Direction.** For \(\Delta\xrightarrow{u}\Gamma\xrightarrow{v}\Theta\), compare \((vu)^*\) and \(u^*v^*\). **Answer:** canonically isomorphic; equal in a suitable split presentation.
4. **Discrete fibers.** Show that \(\int P\) has at most one arrow over a fixed base arrow between two given objects. **Answer:** its fibers are discrete; the only condition is the restriction equation.

### References

- Alexander Grothendieck, *Catégories fibrées et descente* (1960–61).
- Bart Jacobs, *Categorical Logic and Type Theory* (1999).
- Michael Abbott, *Categories of Containers*, Chapter 3 (2003 dissertation).
- nLab, Grothendieck construction and Grothendieck fibration.
