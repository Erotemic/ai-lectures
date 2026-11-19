# 019000 — Profunctors: Relations That Know How to Compose

**Track:** An Introduction to Category Theory. **Background:** sets, functions, categories, natural transformations and coends, with each recalled from an example. **Theme:** profunctors as generalized relationships and their composition by coends.

<!-- BEGIN SPOKEN LECTURE -->

# Profunctors: Relations That Know How to Compose

A library catalog connects books to subjects. A job-search service connects applicants to positions. A train timetable connects one city to another, sometimes through an intermediate station. These are relationships between two kinds of objects, and a relationship is more flexible than a function. One book may have several subjects. Several people may be qualified for the same job. Several routes may connect the same endpoints. We need a way of composing such relationships without pretending that every input has exactly one output.

Ordinary category theory handles functions and arrows extremely well. The idea we'll develop today extends it to relations that themselves respond to arrows. A relationship between a source object and a destination object can have several witnesses, and those witnesses must transform coherently when we change the source or destination. Such a structure is called a profunctor.

The payoffs are substantial. Relational composition becomes a special case. A representable profunctor recovers an ordinary functor. Composing profunctors leads naturally to coends. And the ordinary hom sets of a category act like identity relationships. We will derive all of this from a small library example before writing the general formula.

## From a catalog to a family of witnesses

Imagine two categories. The first contains reading requests. The second contains catalog descriptions. For now, each category has one object, and the only arrow is its identity. Between a request and a catalog description, we may have zero, one, or several matching records. Perhaps one request is satisfied by two editions of a book. The match is best represented by a set of witnesses. The empty set means no match; a two-element set means two specific ways the request can be satisfied.

Since there are no nontrivial arrows inside either category, nothing else needs to be specified. A profunctor between these one-object categories is simply a set. This extremely small example tells us why profunctors are sometimes called many-valued or generalized arrows. One ordinary arrow records a particular passage; a profunctor can record all the ways to pass.

Now give the catalog more structure. Suppose a description can be refined: a general subject entry can be mapped to a more specific subject entry. A request also can be modified. If we promise that a relationship is mathematically well behaved, changing a description or changing a request must induce transformations on its witnesses. A witness cannot be merely an isolated annotation; it must participate in a consistent pattern.

To see the direction, take a catalog arrow from general to specific. We can send a match with the general description forward to a match with the specific description, provided our catalog semantics has defined that action. A change on the request side acts in the opposite direction: if one request maps to another, a witness for the latter can be pulled back to a witness for the former. The asymmetry is the clue that one argument will be contravariant and the other covariant.

## The definition, once its roles are visible

Let C be a category of source objects and D a category of destination objects. A set-valued profunctor from C to D assigns a set P of c and d to every source object c and destination object d. It also specifies how these sets respond to arrows, contravariantly in the C variable and covariantly in the D variable. In symbols in the companion, this is a functor from C opposite times D into the category of sets.

The word opposite is a direction marker. If a source arrow goes from c prime to c, then a witness relating c to d produces a witness relating c prime to d. If a destination arrow goes from d to d prime, a witness relating c to d produces one relating c to d prime. These actions must respect identity arrows and composition. They must also commute with one another, since the source and destination updates concern independent variables.

This is more specific than an arbitrary table of sets. In a general table, matching witnesses at neighboring cells may have no relationship at all. In a profunctor, the categories' arrows dictate how data moves around the table. The construction respects what the two mathematical worlds already regard as legitimate transformations.

There are different conventions in books and programming libraries for which variable comes first, and some authors write a profunctor from C to D with the reverse-looking expression. We will use P of c and d with the source c contravariant and destination d covariant. Whenever you see a profunctor formula, inspect the types before trusting the order of the printed symbols.

## Ordinary relations as a special case

Let's temporarily forget the arrows and make C and D discrete categories. Discrete means the only arrows are identities. Assign to each pair of objects either an empty set or a one-element set. A one-element set means the objects are related; an empty set means they are not. We have recovered an ordinary binary relation.

The set-valued version is richer because it remembers the number and identity of witnesses. Suppose a student qualifies for a seminar by having either completed a mathematics course or obtained an instructor's permission. The relation between student and seminar is true either way. But a witness-bearing relation can retain which condition established eligibility. That distinction is useful when we later compose relationships and want to know how a result was justified.

This also explains why replacing every profunctor set by a Boolean truth value loses information. The Boolean shadow can answer whether a composite relation exists, but it cannot generally tell us how many composite witnesses exist, which two witnesses are identified by an intermediate transformation, or what labels those witnesses carry.

The additional information is worth the effort only when it serves the problem. For a reachability question, Boolean relations may be enough. For proof objects, paths, database records, or ways of implementing an interface, witness sets can be essential.

## Composition in a middle category without arrows

Introduce a third category E. A profunctor P connects C to D, and a profunctor Q connects D to E. We want a composite relationship from C to E.

For an ordinary relation, c is related to e when there exists some d in the middle such that c is related to d and d is related to e. For witness sets, select a witness p connecting c to d and a witness q connecting d to e. The pair is a witness to the composite. Then gather all such pairs over the possible middle objects.

Take a source category containing a single request, a middle category with two catalog entries called blue and green, and an output category with one successful response. Assume the middle category is discrete. There are two witnesses connecting the request to blue and one connecting blue to success. That makes two pairs. There is one witness connecting the request to green and two connecting green to success. That makes two more pairs. The composite has four distinct witnesses.

If we kept only truth values, we would get the single answer yes: there exists at least one route. With witness sets, the count four is retained. This is the set-valued version of matrix multiplication, with disjoint union playing the role of addition and Cartesian product playing the role of multiplication. In the Boolean version, existential or plays addition and logical and plays multiplication.

But this construction is incomplete. If D has arrows between middle objects, counting every two-stage representation as different can count the same underlying composite several times. A categorical middle object is more than a bare label. Its arrows can express equivalent ways of factoring a witness.

## The identification that makes composition categorical

Suppose blue has an arrow to green. A first-stage witness p from the request to blue can be pushed along that arrow to a first-stage witness ending at green. And a second-stage witness q from green to success can be pulled backward along the same arrow to a second-stage witness starting at blue.

These give two ways of describing the same composite: first use p, then the pulled-back q; or first push p forward, then use q. The middle arrow is an internal change of description. We should not treat the two factorizations as genuinely different composite evidence when one is simply the transformation of the other.

So we begin with every pair of first-stage and second-stage witnesses, tagged by its chosen middle object. Then we identify the pairs generated by sliding a middle arrow from one side of the pair to the other. We finally take all identifications forced by these elementary moves. The result is a quotient set.

That quotient is precisely the coend of the product of P and Q over the middle category. The coend was introduced as a way to collect representatives while imposing a compatibility relation. Profunctor composition gives that abstract construction a purpose you can picture. We are making intermediate descriptions invisible while preserving information about the completed relationship.

An important point: the relation is generated by the middle arrows; it is not a claim that every pair with the same endpoints becomes equal. Two genuinely distinct witnesses may survive composition. The coend identifies only what the categories and their actions require.

## A tiny non-discrete calculation

Let's make the quotient tangible. D now has two objects, blue and green, and one nonidentity arrow from blue to green. The first stage has two ways to reach blue, call them p one and p two. It has one way to reach green, r. P sends both p one and p two forward to r.

The second stage has one way to go from blue to success, call it s, and two ways from green to success, call them q one and q two. Pulling either q one or q two backward gives s. Before imposing the coend relation we have four pairs: p one with s, p two with s, r with q one, and r with q two.

Now slide the blue-to-green arrow across the intermediate boundary. The pair p one with s is identified with r with q one, and also with r with q two. The same is true for p two with s. All four representatives lie in one equivalence class. The composite set has exactly one element.

The discrete and non-discrete calculations started with the same numbers of local witnesses but produced different composite cardinalities: four versus one. The difference came entirely from the arrows in the middle category. This is why a profunctor is more than a decorated relation table. The middle category contributes an actual equivalence theory for the intermediate representation.

You can test the construction by changing one of the witness actions. If a particular arrow fails to connect two families, those pairs may remain distinct. But the actions are functions with specified domains and codomains, not optional narrative associations. The result of the quotient is determined by the actual functor data.

## Why hom sets act as identities

In ordinary function composition, the identity function changes nothing. What is the appropriate identity relationship for a whole category C? It is the hom profunctor: the set of arrows from c to c prime. A witness from c to c prime is just an arrow already present in C.

Here is the key calculation in words. Compose a profunctor P from C to D with the hom profunctor on D. A representative of the result contains a P witness arriving at some intermediate d, followed by a D arrow from d to the requested final object. Apply the destination action of P to that arrow. This produces one direct P witness with the final destination.

Why is this an inverse correspondence? Any direct P witness can be represented by choosing the identity arrow as the second stage. And if we first choose some other intermediate arrow and then use the direct action, the coend identification says that this alternative representation belongs to the same class as the identity representation. Exactly the required redundancies have been removed.

This is a co-Yoneda calculation. Yoneda tells us that representable hom functors recover evaluations. The identity law for profunctor composition is another face of that result. We also have a corresponding identity on the source side, using the contravariant action of P.

The identities are canonical isomorphisms of profunctors, rather than literal equality under every concrete choice of quotient-set construction. Similarly, composition of three profunctors is associative by a canonical isomorphism: whichever pair you compose first, you end up with the same three-stage witnesses, modulo the same intermediate relations. The coherent system formed by categories, profunctors, and their natural transformations is called a bicategory.

## Functors live inside this more flexible world

A functor F from C to D already sends each source object to a destination object. It can produce a profunctor by assigning to c and d the set of D arrows from F of c to d. This is a relationship represented by F of c, rather than an arbitrary family of matches.

Why bother with this embedding? Because it lets us compare exact transformations and relational processes using a common language. The functor commits to a chosen object F of c. The profunctor then records ways of reaching each d from that chosen object. A general profunctor may have no single representative object from which all of its matches arise.

The distinction resembles the difference between a data transformation that returns one canonical result and a query that may return many possible results. The second includes the first as an important special case, but not every query can be reduced to a single chosen answer without losing information or making unjustified choices.

There is also a second profunctor associated with a functor, formed from arrows going into F of c. The two constructions have related categorical properties, but their variance directions differ. It is safer to derive them from the domains and codomains than memorize a decorative arrow notation.

## Where this perspective helps, and where it stops

Profunctors are useful when composition involves interfaces, relations, profiled information, or generalized processes. They also arise in the formal study of program optics and lenses, where a complex transformation is described by composing and hiding intermediate interfaces. Some applications require enriched or higher-categorical variants; the set-valued theory is the starting point, not an automatic solution to all such problems.

One can also see a profunctor as a functor assigning to each source object a presheaf-like family on the destination side, after checking the correct opposite category. That viewpoint makes the connection to Yoneda and presheaf categories close. It is especially helpful when you want to replace an ambiguous phrase such as 'generalized arrow' with an exact, typed construction.

The bicategory language has a practical lesson for formalization. If two composites are canonically isomorphic, it is a mistake to assert they are definitionally identical in every representation. The proof obligations involve natural associators and unitors, and the coherence laws governing them. The set quotients make this distinction concrete: the bracketed equivalence classes can be constructed in different orders while still describing isomorphic composite relationships.

## A direct check of three-stage composition

The bicategory claim deserves one more calculation. Suppose we have P from C to D, Q from D to E, and R from E to F. A fully expanded three-stage witness consists of a first step from c to some d, a second step from that d to some e, and a third step from e to f. Two middle categories are involved, and we must allow an arrow in D to move across the first internal boundary and an arrow in E to move across the second.

We could first compose P with Q, obtaining equivalence classes of first-and-second-stage pairs, then compose with R. Or first compose Q with R, obtaining classes of second-and-third-stage pairs, then compose with P. Both procedures begin with the same triples. Both quotient by the identifications generated at the D boundary and at the E boundary. Because applying the two kinds of identification in either order generates the same final equivalence relation, the resulting quotient sets have a natural bijection.

Notice what we proved and what we did not. We did not prove that the internal objects holding quotient representatives are definitionally the same. Depending on how we encode a nested quotient, one construction can carry a class of pairs of classes while the other carries a class of classes of pairs. We proved that there is a canonical, reversible transformation between them. To complete the bicategory structure, we also need the coherence equations: when four stages are combined in different parenthesizations, the resulting associativity isomorphisms must agree. Those equations hold because every route is sent to the same equivalence class of its fully flattened list of witnesses.

This is an excellent example of why strict equality can be a poor expectation for a useful mathematical data structure. The compositional content is invariant; the chosen presentation may vary. In a formal proof assistant we would model the correct isomorphism and verify its laws, rather than inserting an unsafe conversion that assumes nested quotient representations are literally identical.

## When collapsing to a Boolean relation changes the question

There is a final experiment we can perform with our catalog. Define a simpler yes-or-no relation by asking whether each set P of c and d is inhabited. If there is a witness, record true; otherwise record false. Over a discrete middle category, the truth value of the composite is exactly the ordinary relational composite. There exists some intermediate d, a first witness, and a second witness.

Over a middle category with arrows, the coend may identify many witnesses, but if it is inhabited before quotienting it remains inhabited afterward. So at the level of mere existence, the same relational question is still answered by a two-stage path. The arrows become important when we ask a finer question: not only whether a match exists, but which equivalence classes of matches remain.

This is a distinction between existence and evidence. Suppose two independent books really satisfy the same query. They should remain distinct witnesses unless an appropriate identification is justified. If we forget all evidence immediately, we cannot later reconstruct which edition was supplied or whether an internal normalization transformed one description into another. Conversely, if an application only needs to decide reachability, preserving every witness may impose unnecessary computational work.

The mathematical framework tells us exactly where the information loss occurs. Replacing a set by its inhabited-or-empty truth value discards distinctions between witnesses. Taking the coend does something else: it identifies witnesses along morphisms that the middle category has already declared legitimate. Those operations need not have the same meaning, and using the appropriate one is a modeling decision.

## The result of the construction

A profunctor assigns sets of witnesses to pairs of objects and transports them coherently along arrows. Two profunctors compose by pairing their witnesses across a middle category and then identifying factorizations related by middle arrows. Discrete middle categories give a disjoint union of products. Non-discrete middle categories introduce genuine quotient identifications. The hom profunctor serves as the identity, by co-Yoneda, and associative composition holds up to coherent isomorphism.

That gives us a more expressive notion of correspondence without sacrificing compositional laws. It also illustrates a recurring method in category theory: begin with a familiar operation, discover why its naive version overcounts or fails to be invariant, and use a universal construction to impose precisely the identifications the mathematics demands.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Use the convention that a profunctor \(P:\mathcal C\nrightarrow\mathcal D\) means a functor \(P:\mathcal C^{op}\times\mathcal D\to\mathbf{Set}\). For \(P:\mathcal C\nrightarrow\mathcal D\) and \(Q:\mathcal D\nrightarrow\mathcal E\), define
\[
(Q\odot P)(c,e)=\int^{d\in\mathcal D}P(c,d)\times Q(d,e).
\]
The coend is the quotient of \(\coprod_d P(c,d)\times Q(d,e)\) by the equivalence generated by
\[
(P(c,u)(p),q)_{d'}\sim(p,Q(u,e)(q))_d
\quad (u:d\to d',\ p\in P(c,d),\ q\in Q(d',e)).
\]
This formulation requires the relevant categories to be small, or suitable size assumptions. For discrete \(\mathcal D\), the quotient is just \(\coprod_dP(c,d)\times Q(d,e)\).

The identity profunctor \(I_{\mathcal D}(d,d')=\mathcal D(d,d')\) satisfies
\[
I_{\mathcal D}\odot P\cong P,\qquad P\odot I_{\mathcal C}\cong P,
\]
via co-Yoneda. Composition is associative up to natural isomorphism; with natural transformations as 2-cells this forms the bicategory \(\mathbf{Prof}\). A functor \(F:\mathcal C\to\mathcal D\) yields a representable profunctor \(P_F(c,d)=\mathcal D(Fc,d)\).

**Finite calculation:** Let \(\mathcal D\) be the walking arrow \(b\xrightarrow{u}g\). Define \(P(c,b)=\{p_1,p_2\}\), \(P(c,g)=\{r\}\), \(P(u)(p_i)=r\); let \(Q(b,e)=\{s\}\), \(Q(g,e)=\{q_1,q_2\}\) and \(Q(u)(q_i)=s\). The coend presents the four pairs \((p_1,s),(p_2,s),(r,q_1),(r,q_2)\), all equivalent. Hence the composite has one witness.

### Exercises with answers

1. **Exercise:** For discrete \(\mathcal D\) with two objects, if witness cardinalities are \((2,1)\) and \((3,4)\), how large is the composite? **Answer:** \(2\cdot3+1\cdot4=10\).
2. **Exercise:** What relation is generated by a middle arrow \(u:d\to d'\)? **Answer:** \((P(u)p,q)\sim(p,Q(u)q)\), with the representatives living over \(d'\) and \(d\), respectively.
3. **Exercise:** Why does the hom profunctor act as an identity? **Answer:** Its arrow witness can be absorbed by a profunctor action, and the identity arrow supplies the inverse class; co-Yoneda verifies the two directions.
4. **Exercise:** Why is \(\mathbf{Prof}\) a bicategory rather than generally a strict 2-category? **Answer:** Composition and units satisfy laws up to coherent natural isomorphism, not necessarily literal equality of the chosen quotient constructions.

### References

- Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality*, https://arxiv.org/abs/1803.05316
- Fosco Loregian, *Coend Calculus*, https://arxiv.org/abs/1501.02503
- Mathlib, `CategoryTheory.Profunctor.Comp`, https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Profunctor/Comp.html
- James Hefford, doctoral thesis (Part II: profunctorial methods), https://www.cs.ox.ac.uk/people/aleks.kissinger/theses/hefford-thesis.pdf
