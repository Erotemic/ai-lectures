# 025000 — Identity Types: When Equality Has Structure

**Track:** Introduction to Category Theory. **Background:** dependent types, substitution, basic category and groupoid language. **Theme:** intensional identity, transport, path induction, and categorical models.

<!-- BEGIN SPOKEN LECTURE -->

# Identity Types: When Equality Has Structure

Take a map of a city. Two people leave the same square and arrive at the same museum. One walks through the park; the other follows the river. Their starting points match, and their destinations match, but their routes are different. We should be able to distinguish the two journeys even when they have the same endpoints.

Mathematical equality is ordinarily more rigid than this. When we write that x equals y in set theory, we mean that the objects are identical, and we do not usually record a route from x to y. Yet in dependent type theory, an equality assertion has a type of possible proofs. Under a homotopical interpretation, those proofs can be understood as paths. Some models retain genuinely different ways of identifying objects, and the differences become mathematical information.

This is an entry point to identity types. We will begin with familiar substitutions, derive transport along an equality proof, introduce the basic rule called path induction, and then ask how categories and groupoids can interpret equality. The aim is to understand why the word equality can refer to several related structures, and which claims are justified by each one.

## Equality in a changing type

Suppose A is a collection of places, and for each place x we have a type P of x describing something available there. At a train station the type could contain platform tickets; at a museum it might contain admission tickets. A term of P of x is meaningful only relative to x.

Now suppose we have evidence that x and y are equal. What should happen to a value of P of x? If the two base points are identified, we expect to transport the value into the fiber P of y. In a dependent type system this idea is expressed by a function called transport: given a proof p that x equals y and a term u of P of x, it produces a term of P of y.

At first this sounds trivial. If x and y are literally the same expression, the two fibers agree automatically. But dependent types have to deal with equalities that are *proved*, not merely apparent from reducing expressions. A proof may be needed to explain why an object has a property at one description of a value and therefore has it at another.

For a simple arithmetic example, suppose a list of length n carries a type that records its exact length. A computation proves that n equals m. We can use that equality to regard the length-n list as a length-m list. The entries need not move; what changes is the type under which the list is regarded. The proof certifies that this change is legitimate.

The ability to move information along equalities is one of the central operations in dependent mathematics. It is also a source of many subtle questions about the meaning of equality itself.

## Reflexivity and the elimination rule

Every element x has an elementary proof that x equals itself. This constructor is called reflexivity. But an identity type is not defined merely by listing a proof called reflexivity. We need a rule explaining how to reason from *any* equality proof.

The rule is often called J, or identity elimination, and its conceptual version is path induction. Suppose we want to establish a property of every pair x,y and every proof p of equality between them. Path induction says it is enough to construct the property in the case where the endpoints are the same and p is the reflexivity proof, provided the property is formulated with the appropriate dependent motive.

The words 'appropriate dependent motive' are important. We are not allowed to take an arbitrary predicate about the written syntax of proofs and assert it follows from inspecting reflexivity. The elimination rule has a precise type, and it works because it is built into the theory of identity types. The companion displays the complete rule.

One consequence is transport. For a family P, specify what transport does when p is reflexivity: it returns its input unchanged. Path induction then extends that operation to arbitrary equality proofs. The construction is general. It works for a family of sets, a family of propositions, or a more structured family, as long as the underlying type theory has the required identity-elimination rule.

The computation rule is particularly clear in the reflexivity case. Transport along reflexivity reduces to the original term. For a nontrivial proof, transport may be defined by elimination even when the resulting expression does not reduce to a simpler normal form without additional information.

## Symmetry and composition from induction

Ordinary equality is symmetric: if x equals y, then y equals x. How does a proof-based system obtain the reverse direction? Use path induction. In the reflexivity case, reversing the proof changes nothing. The general symmetry operation is then obtained by the elimination rule.

Similarly, if p proves x equals y and q proves y equals z, we can combine them to prove x equals z. This is the transitivity or concatenation operation. Its construction can also be reduced by induction to a reflexivity case. There is an identity proof for each object, an inverse operation reversing an equality proof, and a composition operation joining compatible proofs.

These are the familiar ingredients of a groupoid: objects, arrows, identities, inverses, and composition. But we should not assert that identity types form an ordinary strict groupoid with all groupoid laws holding as literal definitional equalities. In intensional type theory, associativity, left and right identity, and inverse laws are generally witnessed by *higher equality proofs*.

That distinction is the beginning of higher structure. An equality between two proofs of equality can itself have proofs. The laws of composition need not erase the difference between paths; instead, they tell us how paths are identified one level higher.

## Two routes between the same points

Think again of two paths from the square to the museum. We can write p for the route through the park and q for the route along the river. If we work in a topological space, these paths can be different maps from a time interval to the space. We may ask whether one path can be continuously deformed into the other while keeping the endpoints fixed.

In a region containing a lake, one path may pass clockwise around the lake while another passes counterclockwise. Without crossing the obstacle, they may fail to be deformable into each other with endpoints fixed. The topology records the difference. If we instead go to a simply connected region, more of these differences may disappear.

The point is that endpoint equality by itself discards route information. A path model of identity retains at least some of that information. When paths are treated as equality witnesses, a homotopy between paths can become a witness that two equality proofs are equal. Iterating this reasoning gives higher paths between higher paths.

This is an analogy that can be made precise in homotopy-theoretic models. It does not mean every programming-language equality proof is literally a geometric footpath. It means that identity-type rules admit mathematical interpretations in which proofs have the algebra of paths. Those interpretations reveal structure that a purely extensional equality model can collapse.

## What uniqueness of identity proofs would say

There is a principle called uniqueness of identity proofs, often shortened to UIP. It states that for fixed x and y, any two proofs of x equals y are themselves equal. In a theory satisfying UIP, p and q cannot carry distinguishable higher identity information once their endpoints are fixed.

A stronger-sounding but closely related perspective appears in proof-irrelevant propositions: all proofs of the same proposition are indistinguishable for the purposes of the theory. But one must distinguish a proof-irrelevant proposition universe from an arbitrary identity type in a homotopy-theoretic setting. The equality principles depend on the type theory and universe structure being used.

Intensional Martin–Löf type theory does not, by its basic identity rules alone, derive UIP for every type. Hofmann and Streicher's groupoid model demonstrates this by interpreting a type as a groupoid in which there can be several arrows between two objects. Different arrows may represent distinct identity proofs. The model supports the identity-type rules while invalidating universal uniqueness of proofs.

This was an important development because it showed that the basic dependent-type syntax permits more models than the interpretation where every identity proof collapses. Equality can be proof-relevant without making the logical system incoherent. The categorical semantics demonstrates the consistency of the distinction relative to the model's metatheory.

## Groupoids as a model of identities

A groupoid is a category in which every arrow is invertible. Think of objects as possible states and arrows as reversible identifications between them. A groupoid may have several distinct arrows from one object to another, and an object can have nontrivial automorphisms—arrows from the object back to itself that are not its identity.

Here is a finite example. Consider a one-object groupoid whose automorphisms form the two-element group. There is the identity arrow and a second arrow whose composite with itself is the identity. The two arrows have the same source and target, yet they are distinct. If equality proofs are represented by arrows, the groupoid offers two different proofs of the object's equality with itself.

In the bare set model, there is only one identification of an element with itself. In the groupoid model, the same identity type can have nontrivial structure. We should not conflate this with ordinary equality *of the two arrows as set-theoretic objects in the metatheory*. The arrows are distinct meta-level elements; they are used to interpret different object-level identity proofs.

The formal interpretation of dependent types over a groupoid must also handle how families vary along isomorphisms. It uses functorial families or groupoid-indexed structures. The existence of nontrivial arrows alone does not magically give a full dependent type theory. The necessary substitution and identity elimination laws must be verified.

## Path objects and the diagonal

There is a geometric way to express the same idea using a diagonal map. For an object A, the diagonal sends each point x to the pair x,x in A times A. If we want to represent not just identical pairs but paths between pairs of points, we seek a path object P of A.

The path object maps to A times A by remembering the two endpoints. The original diagonal factors through P of A by assigning each point its constant path. In suitable homotopical settings, the map assigning constant paths is a weak equivalence, and the map remembering endpoints is a fibration.

The picture is: the diagonal splits into a map that inserts constant paths followed by a map that reports endpoints. It resembles the identity-type constructor followed by the process of asking which two points are identified. But the categorical factorization requires suitable additional structure to interpret the identity eliminator and its computation rules.

A mere factorization of the diagonal in an arbitrary category is not enough. Different type theories require different notions of fibrations, weak equivalences, lifting properties, and coherence. In particular, some path-object semantics validate the computation rule only up to propositional equality rather than as a strict definitional reduction.

The mathematical companion records that caution because confusing a weak equivalence with literal equality would undo the very distinction the lecture is trying to explain.

## Transport as a functorial action of paths

Return to a family P of fibers over points of A. If p is a path from x to y, transport carries an element in the fiber at x to one in the fiber at y. If q runs from y to z, transporting along p and then q should agree with transporting along the concatenated path.

In intensional type theory, this agreement is generally a proposition supported by another equality proof. It need not hold by definitional reduction for arbitrary p and q. The same distinction appears in categorical geometry: a family varying over a base can be described by reindexing along base arrows, with composition laws that may be strict or only coherent up to isomorphism.

We can interpret transport as a kind of action of the path groupoid on the fibers. Following a reversed path should undo transport along the original path, at least up to the appropriate identity evidence. This tells us that fibers over identified points are equivalent in a coherent way.

A concrete example is a family of coordinate descriptions for a geometric object. Move from one chart to an overlapping chart and translate the coordinates. Move again and translate again. A coherent system should make the two-stage translation agree with translation along the combined change. In differential geometry this often becomes equality of transition functions; in higher settings the comparisons may themselves carry structure.

## Higher identifications and the hierarchy of levels

If an equality proof is a path, then an equality between equality proofs is a path between paths, often called a two-path. We can then ask for a three-path between two-paths, and continue. The resulting hierarchy is one of the motivations for higher category theory.

There is an important distinction between an ordinary groupoid and an infinity-groupoid. An ordinary groupoid has objects and invertible arrows, with associativity and identity holding as strict equations in the metatheory. In the homotopical interpretation of a general type, the associativity and identity data can be witnessed by higher paths, and the witnesses satisfy further coherence relationships. An infinity-groupoid provides a language for this repeated structure.

Some types exhibit only one relevant level of equality information. Other types can carry nontrivial higher paths. In homotopy type theory, this motivates the concept of truncation levels. A proposition-like type has at most one inhabitant up to identification; a set-like type has equality propositions; a groupoid-like type may have nontrivial first-level identifications but no essential higher ambiguity. These are mathematical properties of a type, not just labels chosen by a programmer.

One must not assume that all type theories automatically admit every homotopical principle, such as univalence or higher inductive types. Those are additional axioms or constructions with precise semantic requirements. The basic identity elimination rule provides paths and their algebraic operations, but it does not by itself prove the stronger statements.

## Definitional equality and propositional equality

A dependent type checker relies on definitional equality: it can simplify expressions by computation and identify expressions through the built-in conversion relation. For example, applying a lambda expression to an argument reduces to substituting that argument into the body. No separately named proof term needs to be supplied for that reduction.

Propositional equality is different. It is a type whose inhabitants provide evidence of equality. An expression may require a theorem before its equality is known, even though a person can see that the two expressions represent the same mathematical object. The identity eliminator provides rules for using such evidence. This distinction is essential in proving programs correct.

Different proof assistants choose different foundational rules. Lean's dependent type theory uses a proof-irrelevant universe of propositions and an inductive equality proposition with its own eliminator. The ordinary Lean equality type should therefore not simply be identified with the proof-relevant path type of univalent homotopy type theory. The categorical constructions can illuminate the shared ideas, but a faithful semantic claim needs to respect the actual kernel rules and universe distinctions of the system being modeled.

In particular, groupoid countermodels to UIP for general intensional identity types do not imply that Lean has nontrivial distinguishable proofs of its built-in propositional equality. The model and the implemented type theory make different foundational choices. We can learn from the comparison without treating them as interchangeable.

## A worked transport proof

Suppose a vector has a length index n and a second vector has length m. Assume we have a proof p that n equals m. A transport operation can move the first vector into the family of vectors indexed by m. The proof of transport's correctness is immediate in the reflexivity case: the indices are literally the same, so the vector is unchanged.

By path induction, the operation extends to arbitrary p. To show that transporting forward along p and back along the inverse of p yields the original vector, perform induction on p. The reflexivity case becomes the statement that transporting a vector along reflexivity twice returns the vector, which follows from the computation rule. The general case is then witnessed by the induction principle.

This proof has a recognizable shape. Rather than inspect the internal code of p, we reduce the goal to the identity case using the universal eliminator. It is a pattern that appears constantly in theorem proving. The method is valid because the motive is chosen to depend on the equality proof in exactly the way the eliminator permits.

We should distinguish the result from a literal reduction of a complicated transport expression. The theorem proves equality of the transported expression with the original; it does not assert that all transport along nontrivial evidence is definitionally the identity function.

## A limitation of the route metaphor

There is one more distinction worth making before we return to the city map. In a topological space, the set of all continuous paths between two points is generally enormous. Paths have shapes and speeds. But many homotopy constructions identify paths that can be continuously deformed into one another. The fundamental groupoid, for example, uses homotopy classes of paths, with endpoints held fixed. It therefore forgets much geometric detail while retaining whether a path can wind around an obstruction.

An intensional identity type is defined by inference rules, rather than by declaring that its inhabitants are some particular collection of geometric curves. In one model, identity proofs may behave like arrows of a groupoid. In another, they may behave like paths in a homotopy-theoretic structure. These are mathematical interpretations of the rules, and their validity must be established for every operation the type theory supports.

For a concrete test, consider the circle. There are paths that go once around the circle, twice around, or not at all. Their winding numbers distinguish their homotopy classes of loops. The fundamental group records those classes with composition given by concatenation. This shows how an equality-like path structure at one point can retain information even though there is only one starting and ending point.

Nothing in this example means that an integer proof of equality in a conventional proof assistant is secretly a loop around a circle. The lesson is methodological: an identity type's elimination rules determine what models are possible, and a given model determines what counts as distinguishable identity evidence. We should use the model to illuminate the rules, without silently treating model-specific objects as the definition of equality itself.

## What equality can carry

Our original picture had two routes with the same endpoints. In ordinary set-theoretic reasoning, the endpoint equality was all we needed. In dependent type theory, it is fruitful to consider evidence of equality as a thing we can compose, invert, transport along, and compare with other evidence. In categorical models, that evidence can behave like an arrow or a path.

The central lesson is not that all proofs must be geometric journeys. It is that the rules for equality determine how much structure a mathematical theory retains. If equality proofs collapse, we get one kind of semantics. If they retain path-like distinctions, we get another. Dependent types and their categorical models give us precise ways to compare the possibilities, while keeping separate what is definitional, what is proved, and what extra axioms have been assumed.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

In intensional MLTT, \(\mathrm{Id}_A(x,y)\) is generated by \(\mathsf{refl}_x:\mathrm{Id}_A(x,x)\). The eliminator \(J\) has the schematic form:

\[
\begin{gathered}
C: \prod_{x,y:A}\mathrm{Id}_A(x,y)\to \mathrm{Type},\quad d:\prod_{x:A}C(x,x,\mathsf{refl}_x),\\
J_C(d):\prod_{x,y:A}\prod_{p:\mathrm{Id}_A(x,y)} C(x,y,p),\\
J_C(d,x,x,\mathsf{refl}_x)\equiv d(x).
\end{gathered}
\]

Transport for \(P:A\to\mathrm{Type}\) is
\[
\mathrm{transport}_P(p):P(x)\to P(y),\quad \mathrm{transport}_P(\mathsf{refl}_x,u)\equiv u.
\]

Inverse \(p^{-1}\), composition \(p\cdot q\), and groupoid laws can be derived by \(J\); generic associativity is expressed via higher identities and not necessarily judgmental equality.

A path-object factorization has the form \(A\xrightarrow{r} PA\xrightarrow{(s,t)}A\times A\), with \((s,t)r=\Delta\). To model intensional identity types one typically needs fibrations/weak equivalences, lifting and stable choices, and careful handling of the computation rule.

**Foundational warning:** ordinary Lean equality lies in a proof-irrelevant `Prop`; the groupoid model's nontrivial identity witnesses belong to a different intensional theory. Do not infer higher path structure of Lean's equality from the groupoid interpretation alone.

### Exercises with answers

1. **Transport.** Construct transport by induction on identity proofs. **Answer:** choose motive \(C(x,y,p)=P(x)\to P(y)\), with identity as the reflexivity case.
2. **Reverse.** Prove \(p^{-1}\cdot p\) equals reflexivity in the appropriate path order. **Answer:** path induction on \(p\), then reflexivity computation.
3. **Groupoid example.** Give two different arrows with the same endpoints. **Answer:** in the one-object groupoid from \(\mathbb Z/2\mathbb Z\), the identity and nontrivial group element are distinct arrows.
4. **Two equalities.** Why does path-object factorization not automatically prove strict computation for J? **Answer:** the factorization lacks the required stable lifting/coherence and judgmental reduction data by itself.

### References

- Martin Hofmann and Thomas Streicher, *The Groupoid Interpretation of Type Theory* (1998).
- Steve Awodey and Michael Warren, *Homotopy Theoretic Models of Identity Types* (2009).
- The Univalent Foundations Program, *Homotopy Type Theory* (2013), Chapters 1–2.
- Stanford Encyclopedia of Philosophy, *Intuitionistic Type Theory*.
