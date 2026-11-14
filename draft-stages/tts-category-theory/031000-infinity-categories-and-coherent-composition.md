# 031000 — Infinity-Categories: When Composition Has More Than One Witness

**Track:** Introduction to Category Theory. **Background:** categories, natural transformations, nerves, homotopy, and equivalence. **Theme:** composable arrows, simplices, coherent composition, mapping spaces, and homotopy categories.

<!-- BEGIN SPOKEN LECTURE -->

# Infinity-Categories: When Composition Has More Than One Witness

Suppose you are walking through a city from a library to a market, and then from the market to a station. One route goes down a narrow street; another passes through a public square. As paths, they are different. As ways of getting from the library to the station, they have something in common. You can ask whether the routes can be deformed continuously into one another without leaving the permitted streets. That is already more information than a simple table of starting and ending points can hold.

A category has objects, arrows, identities, and associative composition. We can call each travel path an arrow, and join paths when their endpoints agree. In topology, however, it is often important to remember the deformations between paths, and deformations between deformations. Once we keep those comparisons, strict equations between arrows become a poor language for the whole story. We need a framework that includes composition and the coherent ways composition can be compared.

An infinity-category is one answer. More precisely, the kind we will study is an infinity-one-category. Its arrows need not have a uniquely specified composite in the most literal sense, but composition exists together with enough higher information for different ways of composing to agree coherently. The word infinity refers to layers of comparison that can continue in every dimension. The word one says that comparisons above the level of ordinary arrows are invertible up to still higher comparison.

The principal difficulty is easy to misunderstand. We are not throwing away associativity. We are replacing a rigid equation with a richer, coherently organized notion of sameness. That allows ordinary categories and homotopy-theoretic objects to live inside a common theory.

## What is missing from an ordinary category?

Begin with three locations, A, B, and C. Choose a path f from A to B and a path g from B to C. An ordinary category asks for a composite from A to C. If our arrows are continuous paths, we can concatenate them: walk along f, then g. We can arrange the timing so that f is traversed during the first half of the journey and g during the second half.

Now take a third path h, from C to D. We can concatenate f and g before attaching h, or concatenate g and h before attaching f. Under a common convention for parameterizing paths, the two resulting functions from the unit interval to the city are not literally identical. They travel through the same pieces in the same order, but at different speeds. A reparameterization connects them.

There are ways to obtain strict associativity, such as using paths of variable length and then dividing out or organizing their parameterizations suitably. Those constructions are legitimate. But simply demanding strict equality can conceal the deformations we wanted to study. In a setting with spaces of paths, homotopies and higher homotopies are part of the mathematical evidence.

One solution is to regard a space as an infinity-groupoid: points are objects, paths are arrows, homotopies between paths are higher arrows, and further homotopies relate the comparisons. Unlike a general infinity-category, all the arrows in such a structure are invertible up to homotopy. A path can be reversed, and following a path by its reverse is homotopic to staying still.

This suggests a useful conceptual division. Ordinary categories record arrows and strict composites. Infinity-groupoids record spaces and all their homotopical relationships. An infinity-one-category combines the compositional character of the former with the higher comparisons of the latter, while allowing some one-dimensional arrows to be noninvertible.

## A triangle that knows how to compose

How can a mathematical object store this hierarchy? One influential model uses simplicial sets. To approach that definition, start with a triangle. Its vertices are three objects, zero, one, and two. Its edges represent an arrow from zero to one, an arrow from one to two, and an arrow from zero to two.

If the arrows are f, g, and h, the filled triangle records that h is a suitable composite of f followed by g. In an ordinary category, h would be exactly g composed with f. In a higher-categorical setting, the filled triangle can also record the witness that h represents the composite. Two different filled triangles may carry different comparison information even when their boundary edges agree.

Now move from a triangle to a tetrahedron. Its four vertices define several arrows, its triangular faces express compositions, and its filled interior expresses compatibility among those faces. In dimension four, the same idea checks compatibility among tetrahedra. Continuing this process gives higher-dimensional data for coherent composition.

A simplicial set is a collection of sets, one for each nonnegative dimension, together with maps that describe taking faces and inserting repeated vertices. A zero-simplex is a vertex; a one-simplex is an edge; a two-simplex is a filled triangle. The axioms governing faces and degeneracies ensure that the boundaries of higher-dimensional pieces fit together consistently.

We can recover any ordinary category from a simplicial set called its nerve. An n-simplex in the nerve is a sequence of n composable arrows, or equivalently a functor from the linearly ordered category on n plus one objects. All the other arrows across the simplex are determined by ordinary composition. Thus higher-dimensional simplices do not disappear in an ordinary category. Instead, they are determined uniquely by the lower data.

That observation suggests how to generalize ordinary composition: weaken uniqueness of the correct filled simplex, while keeping the requirement that compatible partial data can be completed.

## A missing face and the horn-filling idea

Imagine a triangle with its two consecutive edges drawn, one from zero to one, and one from one to two. The third edge and the interior of the triangle are missing. That partial triangle is called an inner horn. Filling it means choosing a composite edge and a triangle witnessing its relationship to the two given edges.

For an ordinary category, the filler is uniquely determined. The missing edge must be the composite, and the interior expresses the categorical composition law. For a quasi-category, we require a filler to exist, but do not require a unique one.

The definition extends to every dimension. Take an n-dimensional simplex and remove its interior and one face that is neither the first nor the last face. The union of the remaining faces is an inner horn. A simplicial set is called a quasi-category, or infinity-category in this model, when every such inner horn has a filler.

Notice what the definition does not say. It does not declare that any partial collection of faces can be filled, and it does not demand fillers for the outer horns. Those outer conditions would force more reversibility. A Kan complex, which models an infinity-groupoid, satisfies all horn-filling conditions, not just the inner ones.

The distinction is visible already in an ordinary category with a noninvertible arrow. The inner horn for two composable arrows fills because composition is defined. An outer horn can ask, in effect, for an inverse-like arrow that may not exist. Thus ordinary noninvertible mathematics belongs naturally in the quasi-category framework.

## Why three arrows matter

The triangular case supplies composition. What ensures associativity? Consider three composable arrows, f, g, and h, traveling through four objects. One composite is h after the composite of g with f. Another is the composite of h with g, after f.

A tetrahedron organizes the relevant triangles into one compatible configuration. Its horn-filling condition produces a comparison that relates the two composite routes. Higher-dimensional fillers in turn provide compatibility among these comparisons. Associativity has become coherent: the competing composites can be connected by higher equivalence, and those connections are themselves subject to consistency requirements.

This is not equivalent to saying every proposed composite has an arbitrary number of unrelated choices. The higher-categorical theory arranges choices in structured spaces; it expresses a form of uniqueness up to contractible choice in the relevant universal constructions. However, one must distinguish that conceptual slogan from the false statement that every raw horn has exactly one filler or that every set of fillers is automatically a single point.

To see the gain, think about a homotopy of continuous paths. If we identify all homotopic paths at the outset, the resulting fundamental groupoid can record which classes of paths exist. It loses information about the actual ways paths can be deformed and about the higher-dimensional topology of those deformations. The infinity-groupoid of a space retains that hierarchy instead of truncating it immediately.

## Functors and homotopies between functors

Suppose C and D are ordinary categories. A functor F from C to D sends objects to objects and arrows to arrows, preserving identities and composition on the nose. A natural transformation between two functors gives a family of arrows satisfying a commuting-square condition. These are already two dimensions of categorical structure: arrows between objects, and transformations between ways of translating categories.

In infinity-category theory, functors and natural transformations can themselves inhabit mapping spaces and functor infinity-categories. A natural transformation is not merely a family of arrows whose squares commute as literal equations. The compatibility can be encoded through coherent simplices that relate the two possible routes. When three or four composable arrows appear, those squares must be compatible with further compositions. The higher information is what keeps the entire construction consistent.

To see why this is valuable, think of a diagram of spaces. A choice of map at every vertex is insufficient to define a morphism of diagrams when the connecting maps commute only up to homotopy. One needs actual homotopies, and then compatibility among homotopies. A coherent diagram can store the complete network, while a diagram in a bare homotopy category generally records only the weaker statement that some homotopies exist.

This is a source of many apparent paradoxes in homotopy theory. A collection of individually compatible maps may fail to extend to a coherent global construction. The obstruction lives in the higher relationships, which have disappeared if we record only components. Higher-category theory tells us where those obstructions can be represented and what kind of data a solution must supply.

## Equivalence does not demand a literal inverse

Consider a category of geometric spaces. Two spaces can be homotopy equivalent even though they have very different point sets. A solid disk is homotopy equivalent to a point, because the disk can be contracted continuously. They are not homeomorphic, and their underlying sets need not be presented as identical.

An infinity-categorical equivalence generalizes this phenomenon. A map f from X to Y is an equivalence if there is a map g back and suitable homotopies exhibiting the composites as identities, with the coherence appropriate to the setting. This is a stronger and more structured claim than simply observing that two objects have the same number of connected components. It is also weaker than demanding strict inverse equations in the original presentation.

The difference matters when we compute limits and construct functors. If we replace a disk by a point inside a homotopically meaningful diagram, a properly derived construction should give an equivalent result when the replacement is made coherently. A naive strict construction may not respect that replacement. The higher viewpoint expresses the invariant requirement directly.

For practical mathematics this suggests a test: are we allowed to change a model while preserving its equivalence type? If yes, our constructions should respect equivalences, not demand particular coordinates, triangulations, or path parameterizations. The meaning of an infinity-category comes from making that test part of the foundation.

## The mapping space between objects

In an ordinary category, the arrows from A to B form a set. In an infinity-category, the arrows from A to B are organized into a space. Its points represent maps, its paths represent comparisons or homotopies between maps, and its higher structure records homotopies between those comparisons.

We call this a mapping space. It is crucial that a mapping space is more than a set of equivalence classes. Two maps may lie in the same path component while the space of ways of connecting them carries meaningful loops. Those loops may distinguish different self-homotopies of a map.

For instance, consider a category of spaces rather than a category of bare sets. Functions between spaces can be connected by continuous deformations. A mapping space of continuous maps contains whole families of maps. A homotopy category replaces each such mapping space by its set of path components, making homotopic maps equal as arrows. That is often useful, but it also throws away higher information.

The homotopy category of an infinity-category has the same objects, while its arrows are homotopy classes, or components, of mapping spaces. Composition descends to these classes. The result is an ordinary category, but it is only a shadow of the original higher structure.

An infinity-category also has equivalences. Roughly, a map is an equivalence when an inverse exists up to the relevant coherent homotopies. Not every map is an equivalence; that is why we distinguish infinity-categories from infinity-groupoids. The mapping spaces themselves nevertheless behave like spaces, with their internal higher comparisons reversible.

## A small comparison: one object with a group

There is an instructive example before we tackle arbitrary spaces. Take a group G and form a category with one object. Each element of G becomes an endomorphism of that object, and composition is group multiplication. The category is a groupoid because every group element has an inverse.

Its nerve is a Kan complex. Geometrically, it models a classifying space called B G. When G is the integers, a model for B G has the homotopy type of a circle. When G is a finite group, B G remembers the group through its loop structure even though it has only one object in the original groupoid.

At the level of isomorphism classes of objects, this example looks trivial: there is one class. At the level of the mapping groupoid, it remembers all the automorphisms. At the level of the associated space, it remembers loops. Higher-categorical methods are designed to preserve distinctions of this kind rather than treat everything as a set of representatives.

There is an important limitation: the nerve of an ordinary groupoid models a homotopy one-type, where higher homotopy groups above the first vanish. General spaces can have essential homotopy groups in every dimension. They require more general Kan complexes. That is why the nerve construction is an entry point to the theory, not the entire theory.

A practical consequence is that changing a model can simplify a proof without changing its conclusion. A triangulated surface, a smooth model of the same space, and a combinatorial description may have different literal data but equivalent homotopy types. The correct invariant should survive the comparison. One must still exhibit the relevant equivalence rather than assume all reasonable-looking models are equivalent. That requirement makes changes of presentation mathematically accountable.

## A theorem can change when equality becomes equivalence

Consider a familiar universal property. In a category of sets, a product of A and B is characterized by a bijection between maps into the product and pairs of maps into A and B. In an infinity-category, the appropriate statement is stronger in one direction and weaker in another. For every test object X, the mapping space into the product must be equivalent to the product of the two mapping spaces.

Stronger, because the whole mapping spaces must agree, including their loops and higher homotopies. Weaker, because an equivalence of spaces takes the place of a strict bijection of sets. The universal property records not only a resulting map but also its homotopical uniqueness.

This is a pattern worth carrying into all higher constructions. Limits, adjunctions, and representability can still be stated through maps. But we replace hom-set bijections with mapping-space equivalences that vary coherently with the objects involved. We have not abandoned the universal-property method; we have changed the evidence that a universal property must preserve.

For a concrete product of spaces, imagine choosing a point in A and a point in B. That yields a point in their Cartesian product. But now imagine a path in A and a path in B. These determine a path in the product. Homotopies of those paths also pair. The full product universal property accounts for every level simultaneously.

## Why a homotopy category is not enough

Suppose someone hands you just the ordinary homotopy category of spaces and asks you to reconstruct all homotopy pullbacks. Generally you cannot. The homotopy category retains maps up to homotopy but does not retain the actual spaces of homotopies needed to construct the right derived limits.

An especially sharp example will appear whenever two maps have the same target. A strict pullback insists that their outputs be equal. A homotopy pullback also records a path identifying their outputs. That path can carry winding information and can change the answer fundamentally. The set of homotopy classes of maps is insufficient to recover it without additional structure.

This shows that higher category theory is motivated by a genuine loss of information. It is possible to perform substantial homotopy theory with model categories and other frameworks, but their sophisticated replacement and coherence machinery is accounting for precisely the information that infinity-categories make intrinsic.

Nor should we conclude that infinity-categories make every difficult construction easy. The definition using simplicial sets is compact, while actual computations can demand fibrant replacements, explicit models of mapping spaces, and careful control of equivalences. The gain is conceptual organization. It tells us which information must survive when we pass between models.

## The practical question

When should a mathematician reach for this extra machinery? If the important arrows really form sets, ordinary category theory may suffice. If the important arrows form spaces of choices, with meaningful deformations among them, higher structure becomes relevant. It arises in topology, derived geometry, moduli problems, higher algebra, and interpretations of identity types where paths contain information.

The key question is whether treating two constructions as merely equal or unequal would discard evidence. An ordinary category says where arrows go and how they compose. An infinity-category can also explain the structured ways competing composites agree, and how those agreements agree with one another.

The triangle is still there. Its edges are still arrows. What changes is our respect for the filled triangle: the mathematical witness of composition, and the web of higher witnesses that makes composition coherent. That is the central idea behind the theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Let \(\Delta\) be the simplex category and \(\mathrm{sSet}=\mathrm{Fun}(\Delta^{\mathrm{op}},\mathrm{Set})\). For an ordinary category \(\mathcal C\), its nerve is \(N(\mathcal C)_n=\mathrm{Fun}([n],\mathcal C)\). An inner horn \(\Lambda_i^n\subseteq\Delta^n\) omits the interior and the face opposite vertex \(i\) with \(0<i<n\). A **quasi-category** is a simplicial set in which every inner horn inclusion admits a filler.

For an ordinary category \(\mathcal C\), every inner horn in \(N(\mathcal C)\) fills uniquely. Conversely, unique inner-horn fillers characterize nerves of ordinary categories. Kan complexes require fillers for all horns and model infinity-groupoids. In a quasi-category, each mapping object \(\mathrm{Map}_{\mathcal C}(x,y)\) may be modeled by a Kan complex, and the homotopy category satisfies
\[
  \mathrm{Hom}_{h\mathcal C}(x,y)=\pi_0\,\mathrm{Map}_{\mathcal C}(x,y).
\]
A limit \(L\) of a diagram \(D:J\to\mathcal C\) is characterized by equivalences of spaces, natural in \(X\):
\[
  \mathrm{Map}_{\mathcal C}(X,L)\simeq
  \mathrm{Map}_{\mathrm{Fun}(J,\mathcal C)}(\mathrm{const}_X,D).
\]
The right side is the space of cones with vertex \(X\), not merely a set of natural transformations modulo equality.

**Proof sketch (ordinary nerve):** A two-dimensional inner horn determines two composable arrows. Its unique filler determines their composite. Higher horns in the nerve express the associativity and identity laws already present in the ordinary category; their fillers are uniquely specified by chains of arrows. Conversely, the unique horn-fillers allow reconstruction of composition and its strict laws.

**Example:** For a discrete group \(G\), its one-object groupoid \(BG_{\mathrm{grpd}}\) has nerve a Kan complex with fundamental group \(G\) and no higher homotopy groups. For \(G=\mathbb Z\) this is a model of the circle's homotopy type, but not every Kan complex arises from an ordinary groupoid nerve.

### Exercises with answers

1. **Inner versus outer.** Which horn in dimension two witnesses composition? **Answer:** \(\Lambda_1^2\); the two edges \(0\to1\to2\) are specified.
2. **Ordinary nerve.** How many fillers does an inner horn have in a category nerve? **Answer:** exactly one.
3. **Homotopy category.** What is lost on replacing a mapping space by \(\pi_0\)? **Answer:** paths within components and higher homotopies, including loop information.
4. **Groupoid example.** What is the fundamental group of the nerve of the one-object category with automorphism group \(\mathbb Z\)? **Answer:** \(\mathbb Z\).
5. **Product.** What replaces a hom-set bijection for a product in an infinity-category? **Answer:** an equivalence of mapping spaces, coherently natural in the test object.

### References

- Kerodon, *Inner Fibrations* and *Characterization of Nerves*.
- Kerodon, *Limits and Colimits in Infinity-Categories*.
- Jacob Lurie, *Higher Topos Theory*.
- Emily Riehl and Dominic Verity, *Elements of Infinity-Category Theory*.
