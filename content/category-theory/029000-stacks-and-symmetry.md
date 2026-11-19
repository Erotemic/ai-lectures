# 029000 — Stacks: Gluing Objects Without Forgetting Their Symmetries

**Track:** Introduction to Category Theory. **Background:** categories, groupoids, sheaves, fibrations, and descent. **Theme:** automorphisms, stacks in groupoids, principal bundles, and quotient stacks.

<!-- BEGIN SPOKEN LECTURE -->

# Stacks: Gluing Objects Without Forgetting Their Symmetries

Suppose we are cataloging geometric objects. For every location on a space, we record which kind of object exists there. Maybe the objects are lines, bundles, or configurations. We might try to make a table of possible objects and cross out duplicates whenever two objects are isomorphic. That seems efficient: why keep two copies of the same thing?

But sometimes the maps identifying two copies carry essential information. A circle with a marked orientation has different allowable self-maps from a circle without that mark. A principal bundle can have transformations that preserve its fibers while changing the local coordinates. If we record only one label per isomorphism class, those transformations disappear. Then, when we try to glue local descriptions, we may find that our catalog has thrown away the very maps needed to glue them.

A stack is a categorical way to keep that information. It assigns not merely a set of local possibilities, but a category of local objects and their maps, in a way that is compatible with restriction and descent. Today we will focus on stacks in groupoids. A groupoid is a category in which every arrow is invertible. This is the right starting point when we care about objects up to isomorphism and all the ways they can be identified.

## One object can have many self-maps

Begin with a simple object: a set consisting of two points. It has one identity bijection and one bijection that swaps the points. If we put all two-point sets into a groupoid, any bijection is an arrow, and the two-point set has an automorphism group of size two. An isomorphism class tells us that the set has two elements, but it does not record the swapping symmetry.

Now consider an object with no nontrivial automorphisms, such as a singleton set. Its group of bijections is trivial. The two objects have different sizes, certainly, but the bigger distinction for our purposes is that a general object may admit multiple self-identifications. A classification by equivalence classes cannot express which identifications exist or how they compose.

This point becomes sharper for a principal bundle. Think of a principal bundle with structure group G as a family of copies of G over a base space, arranged so that G acts freely and transitively on each fiber. Locally, every fiber looks like G; globally, the gluing may twist. A morphism of principal bundles is a continuous map respecting both the base projection and the group action.

Even the trivial principal bundle can have automorphisms. For a discrete two-element group on a connected base, multiplying every fiber by the nonidentity group element supplies a nontrivial automorphism. The base points and the isomorphism class of the bundle have not changed, but the object has an extra symmetry. If we collapse the bundle to a single catalog entry, that symmetry has vanished.

## From sets to groupoids

A sheaf of sets assigns a set of possible observations to every open region. Restrict a section from a larger region to a smaller one, and you get a compatible observation. When local observations agree on overlaps, the sheaf axiom says they glue uniquely to a global observation.

For objects such as bundles, there are usually no canonical equalities between the chosen local presentations. A vector bundle described in one frame may look different from the same bundle described in another frame. The correct relationship is an isomorphism. To retain those isomorphisms, assign a groupoid to each open region: its objects are the bundles over that region, and its arrows are the bundle isomorphisms.

Restriction now acts on both objects and arrows. When we restrict a bundle, we also restrict its isomorphisms. But there is a subtlety: if we choose a pullback construction separately for each inclusion of open regions, composing two restrictions may agree only through a canonical isomorphism rather than literal equality. So this family of groupoids is naturally described as a pseudofunctor into groupoids, or equivalently by a category fibered in groupoids over the category of regions.

The word pseudofunctor acknowledges coherent comparison isomorphisms between composite restrictions. It is not an excuse for arbitrary inconsistencies. The comparisons must satisfy explicit coherence laws. Those laws make repeated restriction reliable despite noncanonical choices of concrete presentations.

## What a stack asks us to glue

Cover a region U by smaller regions U i. Choose a principal G-bundle P i on each U i. On an intersection U i with U j, choose an isomorphism from the restriction of P i to the restriction of P j. On triple intersections, require that the direct comparison equal the comparison through the intermediate region.

The data must include those actual isomorphisms, not merely the statement that the bundles happen to be isomorphic. If a bundle has two automorphisms, they can produce different descent data even when all local isomorphism classes agree. The cocycle equations tell us whether the comparisons describe a consistent global object.

A stack in groupoids has two major descent properties. First, its isomorphisms form sheaves: compatible local isomorphisms between two fixed objects glue uniquely to a global isomorphism. Second, every valid family of local objects and transition isomorphisms is effective: it arises from some global object, up to isomorphism compatible with the given data.

These are often called descent for morphisms and descent for objects. Together they say that the natural functor from global objects to the groupoid of descent data is an equivalence of groupoids. That is the categorical upgrade of the ordinary sheaf axiom. A sheaf of sets can be seen as a special case where each local groupoid has only identity arrows.

## A bundle whose twist is stored in a map

Return to a circle covered by two overlapping arcs. Use the group with two elements, which we may write as positive one and negative one under multiplication. On both arcs, take the trivial principal bundle. On one component of their overlap, use the identity group element as a transition; on the other use negative one.

The resulting principal bundle is nontrivial. Just as with the Möbius real line bundle, the relative sign records a twist that cannot be removed by a continuous change of local coordinates on the two connected arcs. The local objects on each arc are individually trivial. What makes the global object different is the transition isomorphism.

This is the first reason groupoids are necessary. A gluing problem does not ask only whether a pair of locally trivial bundles can be assembled. It asks how the chosen local identifications behave, and which changes of local description should count as the same gluing. Both questions are about arrows in a groupoid.

There is a second reason. Suppose we construct the trivial principal bundle globally. It has an automorphism corresponding to the group element negative one applied uniformly in every fiber. This automorphism does not produce a different isomorphism class, but it is still a genuine arrow in the groupoid. A stack retains it. A mere classification set does not.

## A first calculation with principal bundles

For a finite group G, consider a trivial principal G-bundle over a single point. As an object, it is simply a set equipped with a free transitive right action of G. Choose any point p in the fiber; then every other point is uniquely p times g for some g in G. This is what it means to be a G-torsor.

Any equivariant automorphism of this torsor is determined by where it sends p. We can send p to p times h for any h in G. Once that image is chosen, equivariance forces the image of p times g to be p times h times g. Therefore the automorphism group is isomorphic to G after choosing p, though the identification depends on that choice.

If G has three elements in a cyclic group, the torsor has three automorphisms. The set of isomorphism classes of G-torsors over a point still has only one member. This is the clearest possible example of why classification by a set loses information. The missing information is an entire group of automorphisms, not a minor detail of notation.

One can package this groupoid under the name B G, the classifying stack of G. Over an arbitrary space U, B G assigns the groupoid of principal G-bundles over U. Over a point, it is equivalent to the one-object groupoid whose automorphism group is G. The geometry is simple enough to calculate, yet it carries the categorical feature we need for more elaborate moduli problems.

## A cocycle with automorphisms

We can calculate a small part of the groupoid structure explicitly. Take our two overlapping arcs on a circle and the two-element group G. The transition function is specified by a sign on each connected overlap component. There are four possible pairs: positive positive, positive negative, negative positive, and negative negative.

A change of local trivialization on a connected arc is, for this discrete group, multiplication by a constant sign. Changing one local trivialization reverses both overlap signs. Thus positive positive and negative negative describe isomorphic bundles; likewise positive negative and negative positive describe isomorphic bundles. There are exactly two isomorphism classes in this example, represented by the trivial and nontrivial bundles.

But the classification cannot stop there. Even after fixing one pair of transition signs, we can change both local trivializations by the same sign. That preserves the transition functions. It is an automorphism of the descent datum. For either of our two classes, the resulting automorphism group has two elements.

So a simple description of the groupoid contains two pieces of information: two isomorphism classes and a two-element automorphism group attached to each class. Taking a set of isomorphism classes retains the first count and discards the second. Both are meaningful and both arise from the very same two-chart calculation.

This exercise also reveals why a moduli stack has more geometry than its underlying set of points. A point in the moduli problem can represent an object with symmetries, and those symmetries influence how families of objects deform and glue. The stack carries that information through its morphisms.

## Why the word classifying is justified

A principal G-bundle may be described by local trivializations and transition functions. The transition functions satisfy cocycle conditions, and two choices related by gauge transformations describe isomorphic bundles. Thus a suitable collection of local functions and their transformations encodes the groupoid of principal G-bundles.

If we record only cocycles modulo equivalence, we obtain isomorphism classes. That quotient is useful for some classification questions, but it discards stabilizers: the automorphisms of particular objects. In a moduli problem, these stabilizers may vary from object to object and affect geometry. A stack organizes the objects, their isomorphisms, and their behavior under change of base.

For example, imagine studying families of curves with symmetries. A curve admitting a reflection has different automorphism data from a curve of the same broad numerical type with no nontrivial automorphisms. If we classify curves only by a coordinate label, the two may look like ordinary points of a space, but local families can behave differently around their symmetries. Stack language was developed partly to capture precisely these moduli phenomena.

The scope matters. Not every stack is an algebraic stack, and not every category-valued assignment is automatically a stack. Algebraic stacks require additional representability and geometric hypotheses. Our groupoid-valued example is a conceptual entry point rather than a license to treat all moduli problems as solved.

## The quotient stack construction

Suppose a group G acts on a space X. A familiar operation is to form the orbit space: two points are declared equivalent when one can be moved to the other by the action of G. This quotient tells us which orbits exist, but it can forget how many group elements fix a given point.

Consider the simplest case: X is a single point and G acts trivially. The ordinary orbit space is again a single point, regardless of G. If G has two elements, ten elements, or infinitely many, that ordinary quotient looks exactly the same as a point. Yet the action has different symmetry in each case.

The quotient stack, written in mathematical notation as X modulo G in square brackets, remembers that symmetry. Over a test space U, an object of this quotient stack consists of a principal G-bundle over U together with an equivariant map from the bundle to X. For X a point, the equivariant map is automatic, so the quotient stack is B G. It still remembers the torsors and their automorphisms.

When G acts freely and the quotient is well behaved, the quotient stack can often be represented by the ordinary quotient space. When stabilizers are present, that reduction may lose information. The distinction between an orbit space and a quotient stack is thus a difference in what is being classified, not a matter of adding formal decoration.

## The two layers of compatibility

Let us connect this to the ordinary sheaf axiom with a small thought experiment. Suppose two people measure a temperature field on overlapping regions. They record a numerical function, and on the overlap they compare numbers. If the functions agree, there is a unique glued function. The objects being glued are sections, and equality is enough.

Now suppose each person is using a different coordinate frame for the same local bundle. They cannot compare numerical coordinates directly. First they need a frame-change isomorphism. Two different frame-change maps may yield the same local isomorphism class but different global objects. The gluing datum has moved from values to objects and arrows.

Finally suppose the frame changes themselves can be modified by automorphisms. We need to track how changes of presentation transform all transition maps. In stacks, this is still handled by categories and functors rather than by declaring two object descriptions literally equal. It is the reason stacks are close relatives of higher category theory: morphisms of objects become indispensable data.

A stack in groupoids does not automatically require all higher homotopies. We are using a two-level categorical situation: objects, isomorphisms, and equivalences between groupoid-valued descriptions. Derived and higher stacks retain further levels of homotopical information, but those are genuinely additional structures.

## Can a stack fail to be a sheaf of isomorphism classes?

Yes, and principal bundles give a useful warning. One might try to take the assignment sending U to the set of isomorphism classes of principal G-bundles on U. Is this necessarily a sheaf of sets? No. If all local bundles are trivial, their local isomorphism classes are identical. But different transition cocycles can produce globally nonisomorphic bundles, as our two possible signs on the circle demonstrated.

The local class in each arc fails to remember which isomorphism was used on the overlap. The information lost by taking isomorphism classes is exactly what distinguishes the cylinder from the twisted bundle. Thus the assignment of isomorphism classes may fail the ordinary sheaf gluing property even though the groupoid of bundles forms a stack.

This is a decisive reason for using stack theory. The correct local-to-global statement sometimes lives at the level of categories rather than sets. One cannot repair the loss merely by writing a longer list of invariants for each local isomorphism class; the compatibility maps themselves must be retained.

The same issue appears in moduli of representations, connections, or geometric structures with gauge transformations. Their symmetries are part of the geometry. A useful mathematical treatment should remember them whenever they influence how local data combine.

## Prestack versus stack

There is a useful halfway stage in this construction. Suppose we assign groupoids of local objects and arrange restrictions coherently, but only know that isomorphisms between fixed objects satisfy the sheaf gluing rule. We can combine compatible local arrows into a global arrow whenever their source and target are already global objects. Such a structure is often called a prestack, in a common convention.

A prestack may still fail to glue objects. Perhaps we have local bundles with correct isomorphisms on every overlap, but no global object in our chosen category realizes them. The missing property is effective descent for objects. A stack adds exactly that existence requirement.

This two-stage definition gives a useful way to audit a geometric construction. First check that the categories of morphisms restrict and glue correctly. Next check whether every coherent local object arises globally. Both parts can be difficult, but they are separate mathematical tasks. This also explains why one often proves stack conditions by first establishing that the relevant isomorphism presheaves are sheaves and then proving an effective-descent theorem.

A stackification process can repair a prestack under appropriate assumptions, much as sheafification repairs a presheaf of sets. But the output generally introduces new objects by gluing and retains their automorphisms. It is not simply the operation of replacing a category with its set of isomorphism classes.

## A note on equivalence rather than equality

A global bundle reconstructed from local data is ordinarily determined up to isomorphism, and an isomorphism itself may not be unique if the object has automorphisms. The statement that global objects and descent data form equivalent groupoids packages these facts precisely. It identifies the right notion of mathematical sameness while keeping the arrows visible.

This also explains a phrase that can sound contradictory. Descent is often said to be unique up to unique isomorphism, yet an object can have nontrivial automorphisms. The correct uniqueness statement refers to a reconstruction with a specified identification to the given descent datum. Without that specified comparison, the underlying global object may well have automorphisms. In categorical language, the fiber of the comparison over a fixed datum is contractible when the comparison is an equivalence, while the datum's automorphism group may still be nontrivial.

These distinctions are important in formal proof systems as well. A proof that two presented objects are isomorphic is not automatically a proof that the presentations are definitionally identical. The categorical account records the comparison maps instead of assuming they are invisible.

## What stacks accomplish

The initial problem was simple: how do we classify objects without losing their symmetries? A set of names or isomorphism classes cannot retain every map between presentations. A groupoid can. A stack makes such groupoids vary over spaces and requires compatible local objects and isomorphisms to assemble globally.

The principal-bundle example showed the gain. A trivial bundle over a point can have a nontrivial automorphism group. A nontrivial bundle over a circle can be built from locally trivial pieces using transition maps that a set-valued summary would omit. The classifying stack B G retains both pieces of information: which bundles exist and how they can be mapped to one another.

Stacks are useful because they treat symmetry as mathematical data. That becomes essential in moduli problems, where the objects being classified may admit their own transformations. The category theory is not a replacement for geometric calculations; it is the framework that prevents those calculations from discarding information needed for reconstruction.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

A **stack in groupoids** over a site \((\mathcal C,J)\) is a category fibered in groupoids \(p:\mathcal S\to\mathcal C\) such that for every \(U\) and \(x,y\in\mathcal S_U\), \(\operatorname{Isom}(x,y)\) is a sheaf on \(\mathcal C/U\), and all descent data for all covers are effective. Equivalently the canonical comparison functor to the descent groupoid is an equivalence.

For a cover \(\{U_i\to U\}\), descent data consist of objects \(x_i\in\mathcal S_{U_i}\) and isomorphisms on overlaps
\[
\phi_{ij}:x_i|_{U_{ij}}\xrightarrow{\sim}x_j|_{U_{ij}},\qquad \phi_{jk}\phi_{ij}=\phi_{ik}\text{ on }U_{ijk}.
\]
The assignment \(U\mapsto\mathrm{Bun}_G(U)\) of principal G-bundles and their equivariant isomorphisms is a stack for open covers on suitable topological spaces, including ordinary paracompact spaces.

The **classifying stack** \(BG\) assigns the groupoid of G-torsors to a test object. At a point, its fiber is equivalent to the one-object groupoid with automorphism group G (noncanonically identified after choosing a torsor point).

For a G-action on X, the quotient stack \([X/G]\) has, over a test space S, objects \((P\to S, f:P\to X)\) with P a principal right G-bundle and f an equivariant map (for the chosen left/right action convention). Taking \(X=*\) yields \([*/G]\simeq BG\).

### Exercises with answers

1. **Automorphisms.** Count equivariant self-maps of a torsor for the cyclic group of order three over a point. **Answer:** three; choose the image of a single point and extend equivariantly.
2. **Why ordinary classes fail.** Explain why local isomorphism classes of the trivial Z/2-bundle on two arcs cannot distinguish trivial and twisted global bundles. **Answer:** both local classes are trivial, but their overlap transition functions differ by a nontrivial cocycle.
3. **Quotient comparison.** For X a point with a trivial G-action, compare X/G and [X/G]. **Answer:** the ordinary orbit space is a point, while the quotient stack is BG with automorphism group G at a chosen trivial torsor.
4. **Two descent conditions.** State what must be checked to show an assignment is a stack in groupoids. **Answer:** locally compatible isomorphisms glue uniquely and every consistent family of local objects with transition isomorphisms is effective.

### References

- The Stacks Project, Chapter 8, Sections 8.4 and 8.5 (tags 0268 and 02ZH).
- Angelo Vistoli, *Notes on Grothendieck Topologies, Fibered Categories and Descent Theory*.
- Jean Giraud, *Cohomologie non abélienne*.
- David Mumford, John Fogarty, and Frances Kirwan, *Geometric Invariant Theory* (background on quotients and moduli).
