# DT/PT counts, Hall algebras, and stability walls

<!-- BEGIN SPOKEN LECTURE -->

# DT/PT counts, Hall algebras, and stability walls

## Stable Pairs and Donaldson–Thomas Theory: Curves as Sheaves

Imagine trying to count curves of a fixed degree in a three-dimensional algebraic variety. A naive plan is to list smooth embedded curves and divide by symmetries. But in a family, a smooth curve may degenerate into a singular curve, a union of components, or a scheme with embedded or infinitesimal structure. If we discard all those limits, our count can change when we vary the geometry slightly.

Modern enumerative geometry solves this not by pretending degenerations are simple, but by choosing a compact moduli problem that includes them in a controlled way. Donaldson–Thomas theory and stable-pair theory use sheaves to encode curves. Instead of just remembering the visible set of points, a sheaf remembers multiplicity and infinitesimal information.

Two kinds of objects will appear. An ideal sheaf records how a subscheme sits inside the ambient threefold. A stable pair is a map from the structure sheaf of the ambient space into a pure one-dimensional sheaf, with a zero-dimensional cokernel. Their moduli spaces are different, but their virtual counts are related through wall crossing.

## Why an ideal sheaf knows a subscheme

Let a closed subscheme Z sit inside a smooth projective threefold X. Its ideal sheaf contains the functions that vanish along Z. The quotient of all regular functions by that ideal is the structure sheaf of Z.

Take an ordinary line in projective three-space. It can be described by two independent linear equations, so its ideal sheaf is generated locally by those linear forms. As we vary the line, its ideal changes coherently. The family of all lines in projective three-space is a Grassmannian: each line corresponds to a two-dimensional vector subspace of a four-dimensional vector space. This family is four-dimensional, not a finite set of curves.

That example prevents a common mistake. An enumerative invariant does not say every possible curve problem should produce a finite ordinary count. Dimensions must match the insertions or the virtual degree. On a Calabi–Yau threefold, the virtual dimension for the standard ideal-sheaf Donaldson–Thomas problem is zero under its usual fixed numerical data. In projective three-space, with its different canonical bundle, the line family has positive dimension.

## Stable pairs separate a curve from its marked defects

A stable pair consists of a coherent sheaf F, pure of dimension one, together with a section from the structure sheaf of X to F. Purity means F has no nonzero subsheaf supported only at isolated points. The cokernel of the section is required to be zero-dimensional.

Intuitively the section generates F along the generic points of its one-dimensional support. It may fail to generate at finitely many points, and those defects are remembered. That is enough flexibility to compactify curve families without adding arbitrary isolated zero-dimensional subsheaves to F.

For the line L in projective three-space, take F to be the pushforward of its structure sheaf to X. Choose the section that sends the constant one to the constant one on L. Its cokernel is zero. Thus it is a stable pair. If we choose a sheaf twisted to allow an extra zero-dimensional quotient supported at points of the line, the pair can remember additional marked defect data.

These are sheaf-theoretic objects. They cannot, in general, be identified with smooth embedded curves or with maps from an abstract domain. The choice of moduli problem changes what the enumerative invariant means.

## Obstruction theory corrects dimension

Deformations of an ideal sheaf, or of the two-term complex associated with a stable pair, are governed by Ext groups. First-order deformations are tangent directions; higher Ext data supply obstructions to extending those directions. A perfect obstruction theory packages the resulting tangent-obstruction data into a virtual tangent complex.

The virtual fundamental class behaves as if the moduli space had the expected dimension, even when its actual components are larger or singular. On a projective Calabi–Yau threefold, the standard stable-pair theory yields degree-zero virtual classes for fixed curve class and Euler characteristic, so integrating one can produce a number. The number can carry signs and multiplicities imposed by the obstruction theory.

Calling it a count is useful as shorthand, but the precise mathematical object is a virtual integral. In special favorable cases, it agrees with an ordinary signed enumeration. In general, it is not obtained by listing geometric curves and adding one for each.

## Why two theories can encode related answers

An ideal-sheaf moduli problem naturally includes zero-dimensional pieces of subschemes along with curves. A stable-pair problem imposes the purity and section conditions described above. The two theories respond differently to embedded and isolated points. Their generating functions nevertheless satisfy correspondences, often expressed by separating a zero-dimensional Donaldson–Thomas contribution from a curve contribution.

The exact statement depends on the target and theory. For smooth projective threefolds with the standard numerical data, the DT/PT correspondence is established in important settings; for Calabi–Yau targets it is especially natural to express it using reduced generating series. One must check the hypotheses, conventions, and variable transformations rather than assuming an unqualified identity for any moduli stack or any dimension.

Wall crossing explains the relationship conceptually. Change the stability condition in an appropriate category of complexes or sheaves. Objects that were stable may become unstable, and new stable objects appear. The jumps in their invariants can be organized through Hall algebra or related wall-crossing formulas. Stability becomes a mathematical parameter controlling which degenerations we count.

## A line as a complete small example

Return to the line L in projective three-space. The Hilbert polynomial of its structure sheaf is m plus one, because the degree-m sections of the structure sheaf of the projective line have dimension m plus one for nonnegative m. The space of such lines is the Grassmannian of two-planes in four-space, of dimension four.

The stable pair given by O of X mapping to O of L through restriction is valid: its sheaf is pure of dimension one, and its section has zero cokernel. But no one should integrate a zero-dimensional virtual class and call the result the number of all lines in projective three-space without specifying insertions and the appropriate obstruction theory. Here the family itself already has four dimensions.

The example clarifies both the promise and the limitation of sheaf counting. We can represent degenerating curves in an algebraically stable way and compute their deformations systematically. But a virtual number is defined only after fixing the geometry, numerical invariants, stability conditions, and integration problem.

## What a curve count really records

Donaldson–Thomas and stable-pair theories enlarge the language of enumerative geometry. An ideal sheaf remembers a subscheme. A stable pair remembers a pure curve-supported sheaf and a section with finitely supported failure of generation. Perfect obstruction theory replaces naive dimension counting with a virtual class. Wall crossing connects different choices of stability.

The deeper lesson is that a good count needs a good moduli problem. When the objects can degenerate, it is the precise definition of what survives the degeneration—not a clever counting formula—that determines whether the resulting invariant is reliable.

## DT/PT Wall Crossing: Two Ways to Count Curves

Imagine drawing a curve inside a three-dimensional complex variety. If the curve is smooth and isolated, there may be little ambiguity about the geometric object. But moduli theory cannot restrict attention to that comfortable setting. Curves can become singular, nonreduced, or disconnected. Zero-dimensional pieces can appear. Families can degenerate to schemes that have the same underlying set of points but quite different algebraic structures.

To count curves in a deformation-invariant way, a theory must specify what objects are allowed and how they behave in families. Donaldson–Thomas theory and Pandharipande–Thomas theory make different choices. The surprise is that, under the appropriate threefold assumptions, the resulting generating functions are related by a precise factorization.

In Donaldson–Thomas theory, the main rank-one objects are ideal sheaves of one-dimensional subschemes. The ideal sheaf remembers equations of a subscheme, including nilpotent structure and embedded points. It places the curve in a Hilbert scheme and lets deformation theory assign a virtual count even when the geometric moduli space has the wrong ordinary dimension.

In stable-pair theory, the object is a pure one-dimensional sheaf together with a section from the structure sheaf, whose cokernel is zero-dimensional. Purity forbids a zero-dimensional subsheaf of the curve sheaf. The section singles out a generically surjective presentation. This removes a particular source of embedded-point behavior without reducing the count to only smooth embedded curves.

## The smooth-curve example is completely visible

Take a smooth connected curve C inside a smooth threefold. The ideal sheaf of C is an ordinary Donaldson–Thomas-type object. The pair consisting of the structure sheaf of C and its unit section is a stable pair: the map is surjective, so its cokernel is zero.

Now allow a finite collection of marked points on C. These points define an effective divisor D. We can form the line bundle associated with D and use the canonical section whose zeros are D. The resulting sheaf and section form a stable pair. The length of D increases the Euler characteristic of the sheaf by exactly that length.

For the projective line, every degree-d effective divisor is parametrized by a projective space of dimension d. Thus even this elementary curve has a rich family of stable pairs, and the generating variable recording Euler characteristic sees the points added along the curve.

There is an essential qualification. Those projective spaces describe a smooth-curve stratum and a simple choice of sheaves. The virtual invariant of the ambient threefold is not automatically just the ordinary number of points in such a projective space. Deformations normal to C, obstruction theories, and multiplicities affect the enumerative count.

## Why there is a degree-zero factor

Ideal sheaves can account for zero-dimensional subschemes that are not part of the one-dimensional curve class. Consequently, Donaldson–Thomas generating series have contributions from ideal sheaves of pure points, even when the curve class is zero.

Stable pairs package zero-dimensional modifications differently, through the cokernel of a section of a pure one-dimensional sheaf. When changing from ideal sheaves to stable pairs, a universal degree-zero contribution must be separated from the curve-dependent part.

For a smooth projective Calabi–Yau threefold and the conventional numerical generating series, the DT/PT correspondence says that the series for rank-one Donaldson–Thomas invariants in a fixed curve class equals the degree-zero Donaldson–Thomas series multiplied by the corresponding stable-pair series. Equivalently, reduced Donaldson–Thomas theory, after dividing out that degree-zero factor, agrees with stable-pair theory.

This is an equality of virtual-counting generating series, not a literal bijection between ideal sheaves and stable pairs of matching Euler characteristic. One side can contain embedded points that have no direct counterpart as objects on the other side. The equality is produced by a wall-crossing mechanism in a category of complexes.

## Walls come from the notion of stability

Why should a change of moduli problem yield a controlled formula? A stability condition determines which objects are regarded as stable and therefore counted. As the stability parameter varies, some objects become unstable and others become stable. At a wall, an object can decompose into pieces of equal phase or slope. The formula for how invariants jump is governed by the algebra of extensions among those pieces.

For DT/PT, an ideal sheaf and a stable pair can be placed inside a common derived-category framework. Hall-algebra identities, or their categorical descendants, organize how moduli stacks of extensions factor. Passing from those identities to numerical invariants produces the degree-zero factor that separates the theories.

There is a useful mental model: we are not changing the geometry of the underlying threefold, but we are changing the bookkeeping rules for how curve and point contributions can assemble into an object. The change has a predictable cost, expressed by another generating series.

## What a formula does and does not imply

The DT/PT correspondence has a large range of applications, but hypotheses matter. In a projective Calabi–Yau threefold, symmetric obstruction theories provide zero-dimensional virtual counts. On noncompact toric threefolds one often uses equivariant residues. For a general threefold or a different stability theory, the same numerical formula may need modifications or may not apply in the stated form.

Furthermore, multiplying generating series is not the same as multiplying individual invariant numbers. The coefficient for one Euler characteristic is a convolution: many degree-zero and stable-pair coefficients can contribute. That is why a wall-crossing identity naturally looks simple in generating-function form even though its term-by-term consequences are intricate.

It is tempting to hear the phrase counting curves and picture each curve contributing one. Virtual counts do not work that way. Signs, automorphisms, obstruction spaces, and degenerations all play roles. The moduli problem makes the count precise, and the obstruction theory makes it deformation robust.

## Two windows on one enumerative problem

Ideal sheaves are good at retaining the full scheme-theoretic curve, including embedded zero-dimensional structure. Stable pairs make the one-dimensional support pure and record zero-dimensional information through a section. Hall-algebra wall crossing relates their different assemblies. The degree-zero DT factor is not extraneous decoration; it is the price of changing what counts as an admissible object.

For a smooth curve with marked points, these ideas are accessible through line bundles and divisors. For a general Calabi–Yau threefold, they are statements about derived moduli, virtual classes, and generating functions. The underlying principle is the same: one can change a counting theory's objects without losing control of the resulting invariants, provided the change is governed by a sufficiently rich algebra of extensions.

## Motivic Donaldson-Thomas Invariants and Quantum Wall Crossing

Suppose we have a category whose objects can be added and extended. A stability condition decides which objects qualify as stable. A small change in the stability parameters can reverse the relative stability of two classes. At the critical wall, an object may break into pieces, or a new extension of those pieces may become stable.

If we count stable objects on one side of the wall and then count on the other, the numbers can differ. The problem is not merely that our count was inaccurate. We changed the rules for which objects contribute. Wall-crossing theory asks for a relation that survives this change.

Motivic Donaldson-Thomas theory answers this in a refined setting. Instead of immediately assigning a number to a moduli problem, it retains geometric information in a ring of motivic classes. In the presence of a three-dimensional Calabi-Yau categorical structure and suitable orientation data, such counts can be assembled into elements of a quantum torus. The surprising outcome is that an ordered product of these elements remains invariant as the stability condition crosses a wall, even though the individual factors can change.

## The smallest model has two building blocks

Begin with two simple objects, call them A and B. Assume there can be a nontrivial extension that puts B inside a new object E, with quotient A. The new object is not just the direct sum of A and B. Its extension class records how the two pieces are glued.

Picture a quiver with two vertices and an arrow between them. A representation assigns vector spaces to the vertices and a linear map to the arrow. Simple representations occupy just one vertex. A representation with one-dimensional spaces at both vertices and a nonzero arrow can be indecomposable. Depending on stability parameters, that indecomposable may be stable, unstable, or strictly semistable.

The wall appears when the phases of the two simple classes align. On one side, an extension of one ordering may count as stable. On the other, stability favors a different factorization. The geometry of the category has not disappeared: the extensions are still there. What changes is the order and collection of semistable contributions.

## Why ordinary multiplication loses information

If the classes A and B interacted trivially, ordinary commuting variables might be enough to record them. But extensions are directional. The number and orientation of arrows matter. Motivic DT wall crossing uses a quantum torus whose generators do not necessarily commute.

Write two generators as X and Y and suppose that multiplying X by Y produces q times the result of multiplying Y by X. This relation captures a skew pairing of their underlying charge classes. Reversing their order introduces a power of q. Therefore we cannot reorder factors carelessly, and a wall-crossing identity is not merely a rearrangement of ordinary scalar functions.

The quantum dilogarithm is a formal generating series adapted to this noncommutative multiplication. Under a standard normalization, it satisfies a pentagon identity. On one side we multiply a factor associated with X and then one associated with Y. On the other, reversing their order requires a third factor associated with their combined charge. That middle factor represents the contribution of an extension class.

The three-factor expression is a small algebraic shadow of the new stable object that can appear at the wall. The identity is often presented as one of the first nontrivial examples of the Kontsevich-Soibelman wall-crossing formula.

## What the pentagon counts

The phrase quantum dilogarithm might suggest an analytic special function with a mysterious name. For our purpose, its important feature is formal. It is an infinite power series whose coefficients encode increasingly many copies of a stable charge. The precise powers of q depend on the chosen motivic or refined normalization.

Now multiply two such series in a quantum torus. Each coefficient mixes the charges of two stable constituents. Because the variables do not commute, the order also records their antisymmetric interaction. The pentagon identity says that the result can be refactored through a combined charge. This is the algebraic fingerprint of a stability change that admits or excludes the corresponding bound state.

A warning is essential. The two-vertex quiver alone is not automatically the full three-Calabi-Yau setting required for motivic DT invariants. It is a useful model of extensions, and the quantum pentagon becomes an actual motivic wall-crossing identity after placing the example in an appropriate Calabi-Yau or quiver-with-potential framework. Without such structure, the algebraic example remains an analogy rather than a complete DT construction.

## Why a motivic count contains more than a number

An ordinary Euler characteristic replaces a variety by an integer. Many geometrically different spaces can have the same Euler characteristic. A motivic class remembers more. For example, the affine line contributes a distinguished element, often denoted by the letter L, and the class of a projective line is one plus L rather than immediately two.

This refinement lets a counting theory distinguish phenomena that disappear under numerical specialization. The category of vanishing cycles, orientation data, and motivic integration supply further structure in the full Donaldson-Thomas construction. These ingredients are not optional decoration: they account for the geometry of critical loci and the signs or weights that arise when moduli spaces are singular.

If we then pass to a suitable quasi-classical limit, quantum-torus identities can induce transformations of an ordinary Poisson torus. The limit retains wall-crossing information in symplectic or cluster-like transformations. But taking a limit requires specifying a coefficient ring and handling denominators and completions; it is not always legal to substitute q equal to one directly into every term of a quantum-dilogarithm series.

## Ordered products and sectors

The general wall-crossing formula is organized by charges and their phases. Choose a sector in the complex plane of central charges. Form an ordered product of quantum-torus elements associated with stable classes whose central charges lie in that sector, sorted by phase.

As stability varies, a ray can cross another ray and the factors may have to be rearranged. Provided the hypotheses are met and no relevant ray crosses the boundary of the chosen sector, the total ordered product stays fixed. Individual invariants may jump, but their combined transport does not.

This is why the order matters. If the algebra were commutative, rearranging the factors would convey much less information. The noncommutativity forces correction factors that register extensions. What appears as a change in enumerative numbers is constrained by a stable algebraic identity.

## A change of accounting, not a loss of structure

The small pentagon example provides a useful mental picture. Before the wall, we count two constituent types in one order. After the wall, we count them in another order, and a stable extension may contribute between them. The generating-series factors change, but a conserved product relates the two sides.

The general theory is far richer: it involves derived categories, orientation data, motives, moduli stacks, and completed quantum tori. Still, its core insight is visible already. A stability condition chooses which objects count individually. The extension algebra remembers how they can combine. Wall-crossing identities ensure that changing the choice does not erase that information; it repackages it in a controlled way.

## Hall Algebras, Extensions, and Cluster Mutations

In an ordinary group algebra, multiplication comes from a group law. In a Hall algebra, multiplication comes from counting exact sequences. The factors are algebraic objects, and their product records how many ways one can appear as a quotient of a larger object while another appears as a subobject.

This makes the algebra sensitive to extensions. Two objects may have a direct sum, but they may also fit together in a nonsplit exact sequence. Hall multiplication distinguishes these possibilities. When extension directions differ, the product becomes noncommutative. That asymmetry is exactly the information a theory of quiver representations needs.

Quivers are directed graphs, and a representation assigns a vector space to each vertex and a linear map to each arrow. They provide a manageable setting in which categories of representations have kernels, cokernels, and short exact sequences. Counting these sequences over finite fields creates finite coefficients. Under further constructions, Hall algebras connect to quantum groups, canonical bases, stability conditions, and cluster algebras.

## A two-vertex quiver reveals the mechanism

Take the simplest directed graph with one arrow from vertex one to vertex two. There are two simple representations. The first has a one-dimensional space at vertex one and zero at vertex two. The second has zero at vertex one and a one-dimensional space at vertex two.

There are also two natural representations with one-dimensional spaces at both vertices. In one, the arrow map is zero. That is the direct sum of the two simples. In the other, the arrow is an isomorphism. Call this indecomposable representation M. It cannot be decomposed into the two simples, because the nonzero arrow ties the vertex spaces together.

In M, the subspace at vertex two together with zero at vertex one forms a subrepresentation isomorphic to the second simple. The quotient is the first simple. Thus M fits into a short exact sequence with the second simple as subobject and the first simple as quotient. That exact sequence is nonsplit.

Turn the subobject and quotient around. Could the first simple appear as a subrepresentation of M? It would require the whole one-dimensional space at vertex one to map into zero at vertex two. But the arrow is an isomorphism, so that is impossible. The extension is directional.

## Compute both orders of multiplication

Choose the Hall-product convention in which the product of the class of A and the class of B counts subobjects isomorphic to B whose quotient is A. Work over a finite field, and use the untwisted basis indexed by isomorphism classes of representations.

Multiply the first simple by the second. There are two possible middle terms of dimension one at each vertex: the split sum and the nonsplit M. In each, there is exactly one subrepresentation of the required type. The product therefore contains both classes, each with coefficient one.

Now multiply in the opposite order. The split direct sum still qualifies. But M does not have the first simple as a subrepresentation. The product has only the split term. Subtract the two products and the class of M remains.

This is noncommutativity generated by extensions, not imposed by a mysterious algebraic relation. The arrow orientation determines which nonsplit sequence exists, and the Hall algebra records it as the difference between two orders of multiplication.

The coefficient one belongs to this small example and to the stated untwisted convention. Other Hall products include Euler-form twists, automorphism normalizations, or derived-category refinements. Those conventions change coefficients and sometimes signs. The categorical extension calculation remains the underlying reason the two orders differ.

## Why finite fields are convenient

Over the field with q elements, a finite-dimensional vector space has finitely many subspaces. This makes Hall counts finite. For the quiver with one vertex and no arrows, objects are just finite-dimensional vector spaces. Counting subspaces gives Gaussian binomial coefficients, which are q-analogues of ordinary binomial coefficients.

When arrows are added, the counts become sensitive to the representation maps. The Euler form of the quiver helps organize the twisted multiplication, and Green's theorem relates multiplication to compatible coproduct structures under appropriate hereditary hypotheses.

This is where quantum groups enter. The positive half of a quantized enveloping algebra can be realized through suitable Hall algebras of quiver representations. Its generators correspond to simple representations, while quantum Serre relations arise from patterns of extension counting.

The phrase “Hall algebra equals a quantum group” needs qualifications. The exact statement depends on the quiver, orientation, coefficient field, and the version of Hall algebra. A quiver of finite Dynkin type provides a particularly clear setting; loops, general categories, and derived Hall algebras require additional structure.

## Mutation changes a description, not merely a label

A cluster algebra begins with a seed: a collection of variables and an exchange matrix, often drawn as a quiver without certain short cycles or loops. Mutation changes a chosen variable according to an exchange relation and simultaneously transforms the quiver.

For a quiver with one arrow from one to two and coefficient-free cluster variables x one and x two, mutating at the first vertex replaces x one by the quotient of one plus x two over x one. The arrow reverses. Mutating again at the same vertex restores the original seed.

The exchange relation is elementary, yet repeated mutations lead to a highly structured collection of rational functions. In more elaborate settings, Hall algebras and categories of quiver representations supply a conceptual explanation for positivity, exchange relations, and wall-crossing transformations.

Not every Hall algebra comes with a canonical cluster structure, and not every cluster mutation is literally an isomorphism of categories of ordinary representations. Tilting, derived equivalences, and stability conditions often mediate the connection. The important insight is that mutation reorganizes the algebraic information without making extension phenomena disappear.

## Stability and wall crossing

Suppose quiver representations carry a stability condition. Changing that condition changes which objects count as stable. An object might be stable on one side of a parameter wall and decompose into stable factors on the other.

Hall multiplication describes how those factors assemble through extensions. Because the product is noncommutative, changing their order is consequential. Wall-crossing identities preserve a suitable total product even though the stable factors and their order change.

This is the finite-dimensional shadow of more elaborate wall-crossing theories in Donaldson–Thomas geometry. There, categories of sheaves or complexes replace elementary quiver representations, and refined invariants replace simple counts. The two-vertex example remains valuable because it displays the mechanism with no geometry hidden behind notation.

## What to retain from the example

The direct sum forgets the direction of a nonsplit extension. The Hall product does not. In the arrow-one-to-two quiver, the first simple multiplied by the second includes an indecomposable middle term, while the reverse product does not. The difference measures a genuine extension.

From that starting point, Hall algebras connect exact categories to quantum groups. Cluster mutation reorganizes quiver descriptions through exchange relations. Stability conditions explain why product identities survive when the list of stable objects changes. A small calculation with two vertices thus opens a path from linear algebra to representation theory, geometry, and wall crossing, while keeping the essential operation concrete: count the ways an object can be assembled.

## Stability Conditions, Quiver Mutations, and Wall Crossing

A representation of a quiver is a collection of vector spaces attached to vertices and linear maps attached to arrows. Whether that representation is indecomposable is an intrinsic algebraic question. Whether it is stable is different: stability depends on an additional choice of how to compare the phases of an object and its subobjects.

This distinction produces wall crossing. As the stability condition varies, a representation may stop being stable without changing its underlying vector spaces or arrow maps. The collection of stable objects can jump, and invariants that count stable objects may jump with it. The mathematics asks not merely where the jump occurs, but how to relate the counts on opposite sides of the wall.

A two-vertex quiver provides a complete example small enough to hold in mind. Put one arrow from vertex one to vertex two. Give each vertex a one-dimensional vector space and take the arrow map to be nonzero. Call the resulting representation E.

## The subobject that decides stability

There are two simple representations, one concentrated at the first vertex and one at the second. Because the arrow points from the first vertex to the second, E contains the simple object at the second vertex as a proper subrepresentation. It does not contain the simple at the first vertex as a proper subrepresentation: the nonzero arrow would leave its chosen target subspace.

Thus E sits in a short exact sequence with the second simple as subobject and the first simple as quotient. The sequence does not split. If the arrow were zero instead, the representation would be the direct sum of the two simples.

Now assign a complex number in the upper half-plane to the first simple and another to the second. This assignment is a central charge. Its argument defines a phase. For our fixed finite-length category, a stable object must have every proper nonzero subobject at strictly smaller phase than the object itself.

The only nontrivial proper subobject of E is the simple at vertex two. Therefore stability of E is decided by one inequality. All the apparent complexity of the definition collapses to a comparison of two angles.

## Walk across the wall explicitly

Give the first simple the central charge negative one plus i, and the second simple one plus i. The first phase is a hundred and thirty-five degrees; the second phase is forty-five degrees. The central charge of E is their sum, two i, whose phase is ninety degrees.

The only proper subobject has phase forty-five degrees, smaller than ninety. So E is stable.

Now reverse the two charges. The central charge of E remains two i, so its phase remains ninety degrees. But the phase of its subobject becomes a hundred and thirty-five degrees. That is larger than ninety, and E is unstable. The representation did not change. The ordering of the phases did.

At the wall, the two simple charges have the same argument. The extension object becomes semistable in the corresponding sense. The change is not a mysterious discontinuity in matrices. It is a change in which subobjects are allowed by the phase inequality.

## From one extension to a wall-crossing identity

For a two-vertex quiver there is only a small number of representations in a fixed small dimension, but Hall algebras can count how objects assemble by extensions across all dimensions. Their multiplication is organized around short exact sequences.

Changing the stability condition reorganizes which extension classes are stable. Wall-crossing identities express the same total category in different factorizations associated with the new order of phases. In refined settings, these factorizations involve quantum dilogarithms and noncommutative variables rather than ordinary sums of numerical counts.

It would be incorrect to infer a universal numerical jump from our two-vertex example alone. A Donaldson–Thomas invariant requires choices of category, stability, orientation or motivic refinement, and often finiteness and support conditions. The elementary phase comparison supplies the local mechanism, not the entire enumerative theory.

## Why quiver mutation enters

Cluster mutation changes the quiver seed by a combinatorial rule. In a two-vertex example with one arrow, mutation at one vertex reverses the arrow and replaces a cluster variable by a rational expression involving the two original variables.

In suitable derived or Calabi–Yau categorical settings, a mutation can be realized through changing the heart of a t-structure or through a related categorical operation. That is why wall crossing, cluster coordinates, and quiver mutation often occur together.

But the three are not synonyms. A wall of stability conditions concerns the phases of objects in a category. A cluster mutation is a rule on seed data. A categorical tilt changes the chosen abelian heart inside a derived category. Their compatibilities are theorems with hypotheses, not mere consequences of using the same quiver diagram.

## A geometry of choices

A space of stability conditions is divided by walls on which certain central charges align. Away from a wall, the list of stable objects of a fixed class can remain constant. Crossing the wall changes a filtration: what was stable may become an extension of stable factors in the opposite order.

The modest representation E showed all the essential pieces. There is a nontrivial extension, a specific subobject, a complex-valued charge, and a phase inequality that reverses under a parameter change. The deeper machinery of Hall algebras and cluster varieties keeps track of how that elementary event propagates through large categories.

Stability is therefore not a label permanently attached to an object. It is a relationship between the object and a chosen geometry of comparisons. Wall crossing is the study of how that relationship changes while the underlying algebraic world remains available for reinterpretation.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Stable Pairs and Donaldson–Thomas Theory: Curves as Sheaves

**Track:** Abstract Algebra. **Background:** coherent sheaves, Hilbert schemes, perfect obstruction theories, and virtual enumerative invariants. **Central question:** what should count as a curve when geometric families degenerate?

#### Mathematical companion (not spoken)

For a smooth projective threefold X and a curve subscheme Z, `0 -> I_Z -> O_X -> O_Z ->0` defines the ideal sheaf. A Pandharipande–Thomas stable pair is a morphism `s:O_X -> F` with F pure of dimension one and `coker(s)` zero-dimensional. The pair is represented by a two-term complex `I^bullet=[O_X -> F]` under standard conventions. Tangent/obstruction groups arise from the trace-free derived self-Ext complex of `I^bullet` (with shifts specified by the obstruction-theory convention).

For `X=P^3` and a line `L=P^1 subset P^3`, choose `F=i_*O_L` and `s` the restriction of one. Then `coker(s)=0`, F is pure of dimension one, and the Hilbert polynomial is `chi(O_L(m))=m+1`. The family of such lines is `Gr(2,4)` with dimension `2(4-2)=4`.

For a smooth projective Calabi–Yau threefold, the conventional PT invariants `P_{n,beta}` are virtual-degree-zero integrals over moduli with `[F]=beta` and `chi(F)=n`. The DT/PT correspondence is usually stated in terms of generating functions and **reduced** DT series after removing degree-zero contributions, with restrictions depending on the precise theorem and geometry; it is not a count of all smooth curves with unit weight.

##### Exercises with answers

1. What does purity of dimension one exclude? **Answer:** nonzero subsheaves of F supported only in dimension zero.
2. Why is `O_X -> O_L` a stable pair? **Answer:** O_L is a pure curve sheaf and the section is surjective, so the cokernel is zero.
3. How many parameters describe lines in `P^3`? **Answer:** four, because `dim Gr(2,4)=4`.
4. What corrects a moduli space of unexpected actual dimension? **Answer:** a perfect obstruction theory and its virtual fundamental class, when they exist with the required hypotheses.

##### Reading and source notes

- [Pandharipande and Thomas, Curve Counting via Stable Pairs in the Derived Category](https://arxiv.org/abs/0707.2348), definition and construction of stable pairs.
- [Thomas, A Holomorphic Casson Invariant for Calabi–Yau 3-Folds](https://arxiv.org/abs/math/9806111), ideal sheaf Donaldson–Thomas theory.
- [Behrend and Fantechi, The Intrinsic Normal Cone](https://arxiv.org/abs/alg-geom/9601010), virtual classes and obstruction theory.

### DT/PT Wall Crossing: Two Ways to Count Curves

**Track:** Abstract Algebra. **Background:** ideal sheaves, moduli spaces, stable pairs, virtual counting, and Calabi–Yau threefolds. **Central question:** why can changing the stability condition change the objects being counted while leaving a predictable relation among their generating functions?

#### Mathematical companion (not spoken)

For a smooth projective Calabi–Yau threefold X and curve class beta, write `I_n(X,beta)` for the Hilbert scheme of one-dimensional subschemes Z (possibly with zero-dimensional components) satisfying `[Z]=beta` and `chi(O_Z)=n`. A PT stable pair is `(F,s:O_X -> F)` where F is a pure one-dimensional coherent sheaf, the support has class beta, `chi(F)=n`, and `coker s` is zero-dimensional.

For a fixed smooth curve C and an effective divisor D of length d, the pair `(O_C(D), s_D)` has `coker s_D=O_D` and `chi(O_C(D))=1-g(C)+d`. When `C=P^1`, the effective divisors of degree d form `Sym^d(P^1) ~= P^d`. This is a moduli-stratum observation, **not** by itself a virtual invariant computation.

Define series `DT_beta(q)=sum_n DT_{n,beta}q^n`, `PT_beta(q)=sum_n PT_{n,beta}q^n` and `DT_0(q)=sum_{k>=0}DT_{k,0}q^k`. In the smooth projective Calabi–Yau threefold DT/PT correspondence, with consistent counting conventions,
\[
 DT_\beta(q)=DT_0(q)\,PT_\beta(q),\quad
 DT_{n,\beta}=\sum_{k\ge0}DT_{k,0}\,PT_{n-k,\beta}.
\]
This is **not** a coefficientwise equality `DT_{n,beta}=PT_{n,beta}`. The identity is a derived Hall-algebra wall-crossing result; it was conjectured by Pandharipande and Thomas and proved in numerical form through work including Bridgeland and Toda.

##### Exercises with answers

1. For a smooth genus-two curve C and divisor D of length three, calculate `chi(O_C(D))`. **Answer:** `1-2+3=2`.
2. For a stable pair, can F contain a nonzero zero-dimensional subsheaf? **Answer:** no; purity rules it out.
3. If `DT_0(q)=1+aq+...` and `PT_beta(q)=b_0+b_1q+...`, what is the q coefficient of DT? **Answer:** `b_1+ab_0`.
4. Does DT/PT identify individual ideal sheaves with individual stable pairs? **Answer:** no; it identifies virtual-counting series through a wall-crossing formula.

##### Reading and source notes

- [A. T. Ricolfi, The DT/PT correspondence for smooth curves](https://link.springer.com/article/10.1007/s00209-017-2037-2), local curve counting and the generating-series identity.
- [Pădurariu and Toda, Categorical DT/PT correspondence and quasi-BPS categories](https://www.cambridge.org/core/journals/moduli/article/categorical-dtpt-correspondence-and-quasibps-categories-for-local-surfaces/F9BEF205512AEB842BB3C2A313FA36D0), categorical wall-crossing perspective.
- [The local motivic DT/PT correspondence](https://pmc.ncbi.nlm.nih.gov/articles/PMC8596886/), definitions and a discussion of local counting formulas.

### Motivic Donaldson-Thomas Invariants and Quantum Wall Crossing

**Track:** Abstract Algebra. **Background:** stable objects in abelian and derived categories, quiver representations, Donaldson-Thomas invariants, and formal power series. **Central question:** why can a change of stability reorder quantum-dilogarithm factors without changing the total invariant?

#### Mathematical companion (not spoken)

A standard toy quantum torus has generators X,Y with `XY=q YX`. The completed algebra admits formal quantum-dilogarithm series. In one common convention, with the central variable `Z=q^(-1/2)XY`, an appropriate quantum dilogarithm E obeys a pentagon identity of the form
\[
 \mathbb E(X)\mathbb E(Y)=\mathbb E(Y)\mathbb E(Z)\mathbb E(X).
\]
**Convention warning:** products, q-powers and inverses vary with the quantum dilogarithm definition and the sign convention for the skew Euler form. One must pick a normalization before doing coefficient arithmetic. This is an identity in a completed *noncommutative* algebra, not an ordinary identity for commuting variables.

For a 3-Calabi-Yau category with charge lattice Gamma, skew pairing `\langle-,-\rangle`, suitable motivic integration, and a stability condition, the DT factors `A_gamma` form an ordered sector product. Under wall crossing, the sector product is invariant when the boundary rays remain clear; the factors and their ordering can change. The Hall algebra describes extensions and underlies the identity. For a variety `P^1`, `[P^1]=1+L` in the Grothendieck ring of varieties, where `L=[A^1]`, whereas its topological Euler characteristic is two. This exhibits the loss of information in a numerical specialization.

##### Exercises with answers

1. If `XY=qYX`, what is `YX` in terms of `XY`? **Answer:** `q^(-1)XY`.
2. Why is an extension not generally equivalent to a direct sum? **Answer:** a nonzero extension class can yield a nonsplit object.
3. What information does `[P^1]=1+L` retain that the number two forgets? **Answer:** the distinction between affine-line and point contributions in the motivic coefficient ring.
4. Can the pentagon identity be applied to an arbitrary category with two simple objects? **Answer:** not as a DT identity without the required Calabi-Yau, stability, and integration hypotheses.

##### Reading and source notes

- [Kontsevich and Soibelman, Stability Structures, Motivic Donaldson-Thomas Invariants and Cluster Transformations](https://arxiv.org/abs/0811.2435), motivic invariants, quantum tori and ordered wall crossing.
- [Kontsevich and Soibelman, Motivic DT Invariants: Summary of Results](https://arxiv.org/abs/0910.4315), accessible summary of the refined theory.
- [Kontsevich and Soibelman, Wall-Crossing Structures and Mirror Symmetry](https://arxiv.org/abs/1303.3253), wall-crossing structure and integrable systems.

### Hall Algebras, Extensions, and Cluster Mutations

**Track:** Abstract Algebra. **Background:** quiver representations, exact sequences, finite fields, and quantum groups. **Central question:** how can counting subobjects create a noncommutative algebra that remembers extensions?

#### Mathematical companion (not spoken)

Let `Q:1 -> 2` be the `A_2` quiver over `F_q`; `S_1=(F_q,0)`, `S_2=(0,F_q)`, `P_1=(F_q --id--> F_q)`, and `S_1+S_2=(F_q --0--> F_q)`. For the untwisted Hall product
\[
[A]*[B]=\sum_{[E]}\#\{U\subseteq E:U\simeq B,\ E/U\simeq A\}\,[E],
\]
subrepresentation stability under arrows yields
\[
[S_1]*[S_2]=[S_1\oplus S_2]+[P_1],\qquad
[S_2]*[S_1]=[S_1\oplus S_2].
\]
Here the counted subobject is unique in each eligible middle term. Equivalently `Ext^1(S_1,S_2) ~= F_q` and `Ext^1(S_2,S_1)=0`. Other conventions insert factors or twists. For coefficient-free cluster mutation at vertex 1 of the same quiver, the exchange relation is `x_1 x'_1=1+x_2`, with arrow reversal.

##### Exercises with answers

1. Which simple occurs as a subrepresentation of `P_1`? **Answer:** `S_2`.
2. Why is `[S_1]*[S_2]` different from `[S_2]*[S_1]`? **Answer:** the first admits the nonsplit middle term `P_1`, the reverse does not.
3. What is the first cluster-variable mutation at vertex one? **Answer:** `x'_1=(1+x_2)/x_1`.
4. Would the Hall coefficients necessarily remain one under an automorphism-normalized Hall product? **Answer:** no; the normalization changes coefficients.

##### Reading and source notes

- [Schiffmann, Lectures on Canonical and Crystal Bases of Hall Algebras](https://www-fourier.ujf-grenoble.fr/sites/ifmaquette.ujf-grenoble.fr/files/schiffmann2_rev.pdf), geometric Hall constructions and quiver categories.
- [Fomin and Zelevinsky, Cluster Algebras I: Foundations](https://arxiv.org/abs/math/0104151), exchange mutation and cluster-algebra foundations.

### Stability Conditions, Quiver Mutations, and Wall Crossing

**Track:** Abstract Algebra. **Background:** quiver representations, short exact sequences, derived categories, and Hall algebras. **Central question:** why can a representation become stable or unstable when only the notion of phase is varied?

#### Mathematical companion (not spoken)

For the quiver `1 -> 2`, take `E=(k --id--> k)`. Its only proper nonzero subrepresentation is `S_2=(0 -> k)`, and
\[
0\longrightarrow S_2\longrightarrow E\longrightarrow S_1\longrightarrow0
\]
is nonsplit. With central charges in the strict upper half-plane and `Z(E)=Z(S_1)+Z(S_2)`, the finite-length phase stability criterion is `arg Z(S_2)<arg Z(E)` (strict) for this `E`. If `Z(S_1)=-1+i` and `Z(S_2)=1+i`, the inequality reads `pi/4<pi/2`, so `E` is stable. If the charges swap, it reads `3pi/4<pi/2`, so `E` is unstable. At aligned phases the object is strictly semistable under the corresponding conditions.

For the coefficient-free cluster seed with one arrow `1 -> 2`, mutation at vertex 1 gives `x_1'=(1+x_2)/x_1` and reverses the arrow. A Bridgeland stability condition, a Hall-algebra wall-crossing identity, and a cluster seed mutation are distinct objects; relating them requires categorical/Calabi–Yau assumptions and conventions.

##### Exercises with answers

1. Why is `S_1` not a subrepresentation of `E` when the arrow is nonzero? **Answer:** the arrow sends the full source into the target, so target subspace zero is not preserved.
2. Compute `Z(E)` for `Z(S_1)=-1+i`, `Z(S_2)=1+i`. **Answer:** `2i`.
3. What is the phase of `E` in this example? **Answer:** `pi/2`.
4. Does a cluster mutation automatically mean that a representation changed stability? **Answer:** No; the connection depends on an explicit categorical model and stability parameters.

##### Reading and source notes

- [Bridgeland, Stability Conditions on Triangulated Categories](https://arxiv.org/abs/math/0212237), foundational stability framework.
- [Fomin and Zelevinsky, Cluster Algebras I: Foundations](https://arxiv.org/abs/math/0104151), seed mutation.
- [Kontsevich and Soibelman, Stability Structures and Motivic Donaldson–Thomas Invariants](https://arxiv.org/abs/0811.2435), wall-crossing identities.
