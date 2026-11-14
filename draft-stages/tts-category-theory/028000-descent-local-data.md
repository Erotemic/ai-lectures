# 028000 — Descent: Reconstructing Global Objects from Local Data

**Track:** Introduction to Category Theory. **Background:** sets, functions, sheaves, bundles, pullbacks, and elementary category theory. **Theme:** overlap isomorphisms, cocycles, effective descent, and comonadic reconstruction.

<!-- BEGIN SPOKEN LECTURE -->

# Descent: Reconstructing Global Objects from Local Data

Think of a circle drawn on a table. You can cover it with two open arcs, each slightly longer than a semicircle. On each arc you can draw a perfectly ordinary strip of paper: a thin ribbon with no twist. If you are only allowed to see one arc at a time, every part of the ribbon looks like an ordinary rectangle. Yet when you bring the pieces together, you may obtain a cylinder or a Möbius strip. Both are locally strips; they differ in the way those strips are attached.

That difference is the beginning of descent theory. Local observations do not always determine a global object merely by looking at each piece. We also need instructions for comparing the pieces on overlaps, and those instructions must satisfy consistency laws. Even that is not always sufficient: the kind of object we are studying must permit compatible local descriptions to be reconstructed globally.

Sheaf theory teaches how compatible local sections become a section. Descent theory asks the corresponding question for entire objects: bundles, modules, spaces, or other structures. A global object is pulled back to each local region. We try to reverse that operation. Which collections of local objects with compatibility maps actually come from something global?

## Two arcs and two choices of joining

Picture two connected open arcs U and V covering a circle. Arrange them so that their intersection has two separate connected components, one near the top and one near the bottom of the circle. Over each of U and V, place a trivial real line bundle: at every point there is a one-dimensional line, with a coordinate that allows us to call a vector positive or negative.

We must say how the line coordinate on U is related to the coordinate on V where the arcs overlap. On the top component let the relation be multiplication by positive one. On the bottom component let it be multiplication by negative one. These are continuous and invertible coordinate changes on their respective overlap components.

If we choose positive one on both components, the two local strips join into a cylinder. With a positive sign on one component and a negative sign on the other, the strip turns over once around the circle and joins into a Möbius line bundle. A local observer sees an ordinary real line at every point, with no visible twist. The twist is encoded by the transition instructions between local views.

Why can't we change coordinates on U and V to make both transition functions positive? Each connected arc permits a continuous change of frame by a nonzero real function. The sign of such a function cannot change along a connected arc. Changing the U frame and V frame therefore multiplies both overlap signs by the same overall sign. Their relative difference remains. So the positive and negative transition data cannot both be converted into positive data by continuous changes of local frames.

Here is a global fact detected from local information plus compatibility: the Möbius bundle admits no continuous nowhere-zero global section. Such a section would supply a global frame and hence a trivialization, contradicting the sign calculation. The bundle is a real mathematical object whose twist is invisible on the pieces but visible in their gluing data.

## The seam can move, but the twist remains

We can test the ribbon classification without any picture by keeping track of a sign. Choose a point on the top overlap and a point on the bottom overlap. At the top our coordinate systems agree, so the first transition sign is positive. At the bottom they disagree, so the second is negative. Multiply the two signs. The result is negative one. If we had used positive transition signs at both places, the product would be positive one.

Now reverse the chosen frame on U. Every transition sign is reversed. The pair positive and negative becomes negative and positive. Their product is still negative. Reversing the frame on V has the same effect. Reversing frames on both regions changes neither sign. These are exactly the possible sign changes induced by continuous nonzero frame rescalings on connected arcs. The product is therefore an invariant of this two-chart presentation.

We can describe that invariant as the holonomy of a discrete sign convention around the circle, or more precisely as the first Stiefel–Whitney class of the line bundle. Those are richer mathematical languages for the same test. We do not need them to perform the calculation: one reversal around a loop cannot be removed by changing local coordinates.

This suggests an important distinction. Local geometry tells us what a bundle looks like in a neighborhood. Transition maps encode what happens when neighborhoods are compared along a loop. Global topology can be present entirely in that comparison information. In descent theory, the transition data are first-class mathematical objects rather than annotations on the pieces.

## The elementary gluing equations

Let X be a space covered by open sets U one, U two, and so on. Suppose an object E exists over X. Restrict it to each U i, producing objects E i. On an overlap U i intersect U j, both E i and E j arise by restricting the same global E. There is consequently a canonical isomorphism comparing them. Call it phi i j.

The isomorphisms have to agree with themselves. On U i intersect U i, the comparison is the identity. Reversing i and j gives the inverse map. On a triple overlap, comparing from i to j and then from j to k must give the same result as comparing directly from i to k. With consistent composition conventions, phi j k after phi i j equals phi i k.

These are called the cocycle conditions. They are simple equations, but they do crucial work. If we move from the coordinate system of patch one to patch two and then to patch three, the result cannot depend on which intermediate patch we used. Otherwise a single global object could have two incompatible meanings at one point.

A collection of local objects E i together with isomorphisms phi i j satisfying those equations is a descent datum. It is the candidate description of a global object. Notice that the local pieces alone are not a descent datum. The overlap maps are part of the information, and two choices of overlap maps can define nonisomorphic global objects.

## Constructing the ribbon by a quotient

For the ribbon example, we can construct the global object directly. Take the disjoint union of the two local products, U times the real line and V times the real line. A point in a local product is a pair consisting of a base point x and a fiber coordinate t. Whenever x belongs to an overlap, identify the point represented in the U chart with the corresponding point represented in the V chart after applying the transition sign.

If the sign is positive, identify coordinate t with the same coordinate t. If the sign is negative, identify coordinate t with minus t. The cocycle equation ensures that, with more than two charts, making identifications through different intermediate patches yields consistent results. The quotient space carries a map to the original circle, and locally that map looks like an ordinary product with the real line.

This construction is a concrete gluing procedure for vector bundles. The topology on the quotient and the continuity of the transition maps must be checked; the result is more than a set of equivalence classes. The important fact is that a compatible family of vector-bundle transition functions on an open cover determines a vector bundle, up to isomorphism.

For this kind of object and this kind of cover, descent is effective. The term effective means the compatibility data really come from a global object. It does not mean a computer can necessarily calculate the answer efficiently. It is a statement that the desired mathematical reconstruction exists.

## Triple overlaps check consistency

With two charts there are only two main overlaps, so the cocycle equation may appear almost automatic. Consider instead three open regions U, V, and W, all sharing a common small patch. Suppose the coordinate change from U to V multiplies vectors by two, and the change from V to W multiplies them by three. Then the direct change from U to W must multiply them by six. If someone wrote five instead, the same vector could acquire two different coordinates in W depending on the route of translation.

The failure is detectable at a single point of the triple overlap. Start with the coordinate one in the U frame. Translate through V, obtaining two, then through W, obtaining six. Direct translation gives five. The two results cannot describe the same consistently glued vector. The contradiction is not something a clever quotient construction can repair while retaining all the original transition instructions.

A cocycle condition rules out precisely this ambiguity. For vector-bundle coordinate changes, the same test works with invertible matrices: the matrix for the transition from U to W must be the product of the matrix from V to W with the matrix from U to V. Matrix multiplication is associative, so consistency across four or more charts follows from the appropriate pairwise and triple-overlap laws.

Notice what the equation does and does not say. It ensures that comparison maps compose consistently. It does not prove that the resulting topological or algebraic object exists. For vector bundles over open covers, a gluing theorem supplies that existence. Keeping these two steps separate is a safeguard against overstating what a cocycle alone can accomplish.

## Morphisms must glue as well

There are two distinct parts to a descent theorem. We need to reconstruct objects, such as our ribbon. But we also need to reconstruct maps between objects. If we have two global bundles E and F, then a bundle map from E to F restricts to a local bundle map on each patch. These local maps must agree under the corresponding transition functions.

Conversely, if local maps satisfy the overlap compatibility, can they be assembled into a global map? For ordinary vector bundles on open covers, yes. The glued map sends the equivalence class of a local vector to the equivalence class of its local image, and compatibility guarantees independence of the chart used. Continuity and fiberwise linearity can be checked locally.

This distinction matters categorically. A correspondence that reconstructs every global object but loses maps is not an equivalence of categories. A proper descent theorem must be fully faithful on morphisms and essentially surjective on objects. Fully faithful here is the precise way of saying that maps can be recovered uniquely from compatible local maps. Essentially surjective says that any valid local object with descent data is isomorphic to something pulled back from the global space.

We therefore package descent data into a category. Its objects are local families plus transition isomorphisms; its arrows are compatible families of local maps. The restriction functor from global objects to that descent category is the descent comparison functor. Effective descent, in its categorical formulation, is the statement that this comparison is an equivalence.

## A counterexample: forgetting the overlap instructions

Imagine two copies of the ordinary real-line bundle, one on U and one on V. If we specify only these local objects, the cylinder and Möbius ribbon are indistinguishable. Both restrict to the same trivial-looking bundles on each arc. Thus restriction to a cover is not simply a function that reports an unordered list of pieces. It must also retain the comparison maps.

This is analogous to trying to reconstruct a group from a list of its elements while discarding the multiplication table. The elements are necessary information, but they do not determine the structure. For descent, the omitted structure is the way local observations agree on shared regions.

Even overlap maps that satisfy cocycle laws need not glue in every category and for every covering notion. The statement that they do glue is a theorem about the particular class of objects and the specified covers. A mathematician studying schemes, modules, manifolds, or sheaves must justify the appropriate descent property instead of treating the word gluing as a universal permission.

This is where descent theory becomes more than visual intuition. The same equations appear in geometry, algebra, and topology, but their effectiveness depends on precise hypotheses. In algebraic geometry, for instance, faithfully flat maps serve as a powerful generalization of covering families; they allow local descriptions even when the local pieces are not literally open subsets of a topological space.

## Faithfully flat descent in algebra

Suppose A is a commutative ring and B is an A-algebra. Think of replacing a module over A by a module after extending scalars to B. Given an A-module M, we can form B tensor over A with M. This process is a change of base. It can make a problem easier, just as passing to a chart makes a bundle look trivial.

But after changing base, how do we recognize whether a B-module really came from an A-module? We need a compatibility isomorphism between its two pullbacks to the overlap algebra B tensor over A with B. The two pullbacks correspond to the two ways of viewing B over A, just as two charts meet on an intersection. On a triple tensor product, those comparison maps must satisfy a cocycle equation.

If B is faithfully flat over A, compatible modules with such descent data are equivalent to A-modules. Flatness ensures that tensoring with B preserves exact sequences, while faithfulness prevents the change of base from concealing nonzero information. Both properties matter in the reconstruction theorem.

For an elementary picture, take A to be the real numbers and B to be a product of two copies of the reals, with A mapped diagonally. This is a faithfully flat algebra. A B-module amounts to a pair of real vector spaces. Descent data link the two components so that they come from one underlying real vector space. With suitable compatibility, the pair is the duplicate presentation of the same global information.

That is a toy model, not a proof of faithfully flat descent in general. The full theorem reconstructs modules by an equalizer of two maps involving B and the descent isomorphism. The formal companion writes that equalizer and states the algebraic hypotheses.

## Why comonads appear

Recall that an adjunction can generate a monad. The same adjunction also generates a comonad in the opposite order. Given an adjunction between global objects and local presentations, we may restrict global objects to the local side and then perform an appropriate right-adjoint or extension operation. Repeating that operation produces comparison maps. The counit and comultiplication express compatibility under repeated passage between global and local descriptions.

A coalgebra for the resulting comonad is an object equipped with coherent instructions describing how it reappears under the local-to-global-to-local round trip. In favorable situations those instructions encode descent data. Then a comonadicity theorem says that the category of global objects is equivalent to the category of coalgebras for the comonad.

This is the formal dual of the algebraic reconstruction problem. In monadicity we build objects from free expressions and take coequalizers to impose equations. In descent we look for objects satisfying matching constraints, and equalizer-like constructions naturally appear. There is genuine mathematical content in this duality: it predicts the shape of the reconstruction, though each application still needs its own existence conditions.

Be careful about the location of the adjunction. One cannot start with any restriction operation, call it a comonad, and conclude that descent holds. The comparison functor and the relevant adjoints must be specified, and effective descent is precisely what needs to be proved.

## What the descent category remembers

It helps to describe the arrows of the descent category in one concrete calculation. Suppose E is given locally by two trivial real line bundles with transition sign g, and F is given locally with transition sign h. A local fiberwise linear map from E to F is multiplication by a continuous real function on each chart. Call the two functions a on U and b on V.

On the overlap the map has to give the same result in either coordinate system. Translating an input from U to V and then applying b must agree with applying a in U and translating the result with h. In the scalar case the equation is b times g equals h times a. If both bundles use the same transition sign, the condition simply says a and b agree after the coordinate conventions are reconciled.

This is the morphism-level counterpart of the cocycle law for objects. We have converted the question of whether two local maps assemble into a global map into an equation on overlaps. The equation also tells us why a category of descent data is more informative than a collection of isomorphism classes: it stores actual maps compatible with the chosen transitions.

The same idea explains the word fully faithful in the comparison theorem. A global map restricts to a compatible pair; given such a pair, gluing recovers the global map. No maps are missed, and no two distinct maps are accidentally identified. That is a stronger result than showing only that the local pieces determine an isomorphism class of global objects.

## Uniqueness does not mean unique presentation

Return to the Möbius line bundle. We could cover the circle with three arcs instead of two. We could move the seam, reverse the orientation of a local frame, or choose smooth transition functions rather than constant signs. The resulting collections of numbers and charts might look quite different.

Does the construction depend on those choices? At the level of a literal chart list, yes. A particular set of transition functions is a presentation, and changing a local frame changes the presentation. But if two systems are connected by compatible changes of coordinates, they describe isomorphic bundles. The global bundle is well-defined up to isomorphism.

This is why descent is naturally categorical. The correct notion of sameness is often an isomorphism of objects, not equality of presentations. Indeed, an object may have automorphisms: maps from the object to itself which preserve its structure. Those symmetries become central when the objects being glued are themselves classified only up to isomorphism.

There is a further consequence. If we attempt to study a family of geometric objects by recording only the set of isomorphism classes, we may erase precisely the maps needed for correct gluing. The correct next language is a family of groupoids, each remembering not just objects but their isomorphisms. That observation leads directly to stacks.

## What we have established

A local description of a mathematical object has two levels. It says what exists on each piece, and it says how the descriptions agree where pieces overlap. The cocycle conditions make those agreements coherent. A descent theorem goes further: it proves that every compatible local description is realized by a global object and that maps between global objects can be recovered from compatible local maps.

Our circle supplied both a success and a warning. The Möbius ribbon is assembled from locally trivial pieces, but its transition signs obstruct a global trivialization. Local simplicity does not imply global simplicity. The faithfully flat example showed how the same question reappears when the local change is algebraic rather than geographic.

Descent is therefore a reconstruction theory. It tells us what information must be retained when passing from global objects to local views, and when that information is sufficient to build the global object back. It also prepares a new question: what if the local objects have symmetries that should survive the reconstruction? That is the problem for which stacks were invented.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

For an open cover \(X=\bigcup_i U_i\), a vector-bundle descent datum consists of vector bundles \(E_i\to U_i\) and isomorphisms
\[
\phi_{ij}:E_i|_{U_{ij}}\xrightarrow{\sim}E_j|_{U_{ij}},\qquad
\phi_{ii}=1,\quad\phi_{ji}=\phi_{ij}^{-1},\quad
\phi_{jk}\circ\phi_{ij}=\phi_{ik}\text{ on }U_{ijk}.
\]
Morphisms of descent data are families \(f_i:E_i\to F_i\) with \(\psi_{ij} f_i=f_j\phi_{ij}\). Vector bundles satisfy effective descent for open covers, giving an equivalence
\[
\operatorname{Vect}(X)\simeq\operatorname{Desc}(\{U_i\},\operatorname{Vect}).
\]

For a circle covered by two connected arcs with two connected overlap components, \(g_{UV}\in\{\pm1\}\) on the components gives a real line bundle. The choice \((+1,+1)\) is trivial, while \((+1,-1)\) has nontrivial first Stiefel–Whitney class and is the Möbius bundle. A change of frame multiplies both signs by the same sign on each connected patch; hence their relative product is invariant.

For a faithfully flat ring map \(A\to B\), a B-module N with descent isomorphism
\[
\varphi:B\otimes_A N\xrightarrow{\sim}N\otimes_A B
\]
(over \(B\otimes_A B\), using a consistent tensor ordering) satisfying the cocycle condition descends to an A-module. With the convention of Stacks Project tag 03O6, the recovered module can be expressed as
\[
M=\ker\bigl(N\rightrightarrows B\otimes_A N\bigr),\qquad
n\mapsto 1\otimes n,\quad n\mapsto\varphi(n\otimes1).
\]
Precise module actions and tensor-factor placements must be maintained in an implementation; the displayed expression uses the conventional identifications.

### Exercises with answers

1. **Two-chart cocycle.** If an overlap map is multiplication by \(-1\), what is the reverse transition? **Answer:** also multiplication by \(-1\), its own inverse.
2. **Gauge change.** Why can two connected chart-wise frame changes not turn the two signs \((+1,-1)\) into \((+1,+1)\)? **Answer:** each gauge function has constant sign on its connected chart, so the relative product of the two overlap signs is invariant.
3. **Map descent.** Given maps \(f_i\) compatible with transition functions, describe the glued map on equivalence classes. **Answer:** \([x,v]_i\mapsto[x,f_i(v)]_i\); compatibility makes the definition independent of i.
4. **Underlying data.** Why do local bundles without transition maps fail to determine a global bundle? **Answer:** the same pair of trivial local bundles glues as either a cylinder or Möbius bundle with different transitions.

### References

- The Stacks Project, *Stacks* and *Descent* chapters, especially tags 0268 and 03O6.
- Jean Giraud, *Cohomologie non abélienne*, on descent and stacks.
- Angelo Vistoli, *Notes on Grothendieck Topologies, Fibered Categories and Descent Theory*.
- Emily Riehl and Dominic Verity, notes on monadicity, comonadicity, and descent.
