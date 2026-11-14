# 035000 - Chain Complexes and Resolutions: How Algebra Measures Failed Exactness

**Track:** An Introduction to Category Theory. **Background:** abelian groups, group homomorphisms, kernels and quotients, elementary functors. **Theme:** chain complexes, homology, exactness, free resolutions, Tor, quasi-isomorphisms, and the derived viewpoint.

<!-- BEGIN SPOKEN LECTURE -->

# Chain Complexes and Resolutions: How Algebra Measures Failed Exactness

Consider the group of integers. Multiplication by two maps every integer to an even integer. We can then reduce an integer modulo two, obtaining either an even or an odd remainder. The two maps fit together: multiplying by two and then reducing modulo two always gives zero. Moreover, every integer with remainder zero is an even number. The image of the first map is exactly the kernel of the second.

This simple arrangement is called an exact sequence. Exactness says that every object killed by one operation was already produced by the operation before it. That statement has remarkable reach. In topology, homology detects loops and surfaces that fail to be boundaries. In algebra, homology detects elements killed by one map without being explained by the preceding map. In category theory, the passage from exact sequences to chain complexes allows us to replace a difficult object by a structured sequence of simpler ones and calculate how a functor behaves on that replacement.

We will study one concrete sequence involving the integers and reduction modulo two. We will use it to construct a free resolution, then tensor that resolution with the group of integers modulo two. The tensor product will turn multiplication by two into the zero map. A new homology group will appear. Its meaning is precise: tensoring has failed to preserve an injection. This is our entry point to derived functors and the broader categorical idea of replacing an object before applying a construction.

## The exactness question

Start with three abelian groups arranged in order: the integers, another copy of the integers, and the group with two elements. From the first copy to the second, use multiplication by two. From the second to the two-element group, use reduction modulo two. The first map is injective because multiplying a nonzero integer by two never gives zero. The second map is surjective because both residues are represented by ordinary integers.

The central property is exactness at the middle group. Every even integer comes from multiplication by two, and precisely the even integers become zero after reduction modulo two. So the image of the first map equals the kernel of the second. The complete sequence starts and ends with a zero group to record injectivity at one end and surjectivity at the other.

If we removed the multiplication-by-two map and looked only at reduction modulo two, we would see which integers became indistinguishable. But we would lose the description of all relations that explain that identification. The earlier map supplies those relations. Exactness ensures it supplies exactly the right amount: every element killed by the later map has an explanation from the earlier one, and the later map kills everything supplied by the earlier one.

This is a local condition at each position in a sequence. It does not require every map to be injective or every map to be surjective. Rather, the image and kernel must match at each successive group. In the middle of a long sequence, exactness answers the same question repeatedly: which elements become zero here, and were they all accounted for by what came before?

There is a reason to express this with kernels and images. The notions make sense in abelian groups, modules, and many other algebraic settings with an additive structure. We can talk about exactness without choosing coordinates or identifying the group elements with integers. That portability will become important when we treat sequences of objects as objects in their own right.

## Chains, cycles, and boundaries

A chain complex is a sequence of abelian groups or modules connected by homomorphisms called differentials. Each differential lowers degree by one, under the convention we use here. The defining rule is that two successive differentials compose to zero. Every element produced by a differential is killed by the next one.

This rule is weaker than exactness. It guarantees that the image of an incoming differential is contained in the kernel of the outgoing differential, but it does not guarantee equality. The difference between those two sets is exactly what homology measures.

An element killed by the outgoing differential is called a cycle. An element produced by the incoming differential is called a boundary. Every boundary is a cycle because two differentials compose to zero. A cycle need not be a boundary. Homology identifies cycles that differ by boundaries and records the remaining classes. At a particular degree, it is the quotient of the kernel of the outgoing differential by the image of the incoming differential.

One way to hear this definition is: a cycle is locally closed, and a boundary is locally explained. Homology records cycles that cannot be explained by the previous stage of the complex. In topology, the word boundary is literally geometric for simplicial or cellular chains. In the algebraic example we are developing, it is a name for the image of a homomorphism. The common quotient construction is what connects them.

Consider a two-stage complex consisting of the integers in degree one, the integers in degree zero, and multiplication by two as the only nonzero differential. At degree one, a cycle is an integer killed by multiplication by two, so the only cycle is zero. At degree zero, every integer is a cycle because the outgoing differential is zero. The boundaries at degree zero are the even integers. Therefore the degree-zero homology is the integers modulo the even integers, a group with two elements. Degree-one homology is zero.

The two-stage complex is therefore a more elaborate description of the two-element group. It has a larger collection of chains, but its homology remembers the desired quotient and no additional homology in higher degrees.

## Replacing an object by a free resolution

The two-element group is easy to describe as a quotient, but it is not a free abelian group. Every nonzero element of a free abelian group has infinite order, whereas the nonzero element of the two-element group becomes zero when added to itself. Free groups are easier to use in many constructions because maps out of them can be specified by freely choosing images of generators.

Instead of trying to treat the two-element group as free, we resolve it. A free resolution is an exact sequence of free modules ending in the module we want to study. In our example the resolution has a copy of the integers in degree one, another in degree zero, and multiplication by two between them. The map from degree zero to the two-element group is reduction modulo two.

This resolution is short. Exactness at degree zero says the cokernel of multiplication by two is the desired group. Exactness at degree one says multiplication by two has no kernel, so the resolution has no unwanted homology there. The zero at the left records that there are no further relation generators needed.

Why regard this as an improvement? We have replaced a small but torsion-bearing group with a diagram of free groups and maps. A construction that behaves better on free groups can be performed term by term on the resolution, and the resulting homology can reveal which properties of the construction fail to descend from the free pieces to the original quotient.

In the language of category theory, this is a controlled change of presentation. The two-element group and its resolution are not isomorphic as an individual group and a complex. They live in different categories. But the resolution has the intended group as its degree-zero homology and zero higher homology. The augmentation from the resolution to the group regarded as a complex concentrated in degree zero is a quasi-isomorphism, meaning it induces isomorphisms on all homology groups.

The choice of free resolution is generally not unique. A different resolution may have more generators or longer chains. The theory of derived functors is built to produce invariants that do not depend on an arbitrary choice of resolution, up to canonical isomorphism in the appropriate setting. Establishing that independence requires comparison and lifting arguments; it does not follow merely from writing down a complex.

## Tensoring the short exact sequence

Now consider tensor product. For abelian groups, the tensor product of A and B is an abelian group generated by formal pairs of elements, subject to bilinearity relations. It behaves like a universal recipient for bilinear maps. When A is the integers, tensoring A with B gives a group naturally isomorphic to B. When A is the integers modulo two, tensoring with B imposes the relation that twice each element of B becomes zero in the tensor product.

Tensor product is right exact. This means that if a sequence presents a quotient, tensoring preserves the corresponding cokernel description. But a right-exact functor need not preserve injections at the left of a short exact sequence. Our example shows the failure as clearly as possible.

Take the short exact sequence with multiplication by two followed by reduction modulo two. Tensor every term with the two-element group. Each free integer term becomes a copy of the two-element group. What happens to the multiplication-by-two map? On the two-element group, multiplying by two sends every element to zero. So the map that was injective between the integer groups becomes a zero map between two copies of the two-element group.

A zero map between nonzero groups is not injective. The failure is concrete: the nonzero residue class in the domain now maps to zero. Thus tensoring has not preserved the original injection. The right end still describes the correct cokernel, but the left end is no longer exact.

We could simply report that tensor product is not left exact. Homological algebra offers more information. It asks how large the failure is, how that failure behaves under maps of modules, and whether we can package it into a new functor that can be calculated with resolutions. That is where the homology of the tensored resolution enters.

## Calculating a Tor group

Take our free resolution of the two-element group and tensor its free terms with another copy of the two-element group. As just observed, we obtain a two-stage chain complex. Both groups are the two-element group, and the differential between them is zero.

Because the differential is zero, every element in degree one is a cycle. There is no incoming differential from a nonzero degree-two term, so no nonzero degree-one boundaries. The degree-one homology is therefore the entire two-element group. Degree-zero homology is also the two-element group, since the degree-zero outgoing map is zero and the preceding differential has zero image.

These two homology groups have distinct interpretations. Degree zero is the ordinary tensor product of the two input groups. Degree one is the first Tor group. In our example, Tor one of the integers modulo two with themselves is again the integers modulo two. The extra group records the failure of tensoring to preserve the injection in the free resolution.

Notice the dependence on the ambient ring. We are tensoring abelian groups over the integers. If we regarded the two-element group instead as a one-dimensional vector space over the field with two elements and performed the tensor product over that field, the situation would be different: all vector spaces are free over a field, and the corresponding higher Tor groups vanish. Writing just the word 'tensor' without specifying the base ring can conceal a change in the problem.

The same issue appears when intersecting algebraic varieties. An ordinary tensor product of coordinate rings captures a classical fiber product. A derived tensor product can retain higher Tor groups that describe relations among the defining equations. Our integer example is simpler and requires no geometry: it already shows the algebraic mechanism behind the extra homology.

## What the word derived is doing

A derived functor measures how applying an ordinary functor to a suitable resolution differs from applying it directly to the original object. For a right-exact functor such as tensor product, we use a projective or free resolution and take homology after applying the functor. The higher groups detect failures of exactness.

This description is a recipe, but the recipe needs a theorem. If two projective resolutions are used, their results must agree in a coherent way. Standard comparison theorems construct chain maps between the resolutions lifting the identity on the original module, and show these maps are unique up to chain homotopy. Consequently the induced maps on homology are independent of the chosen comparison. That is the mathematical basis for treating Tor as an invariant of the modules rather than a property of our favorite presentation.

Some categories have enough projective objects, meaning every object admits a surjection from a projective object. Module categories have this property, which makes projective resolutions available. In categories without enough projectives, one may use injective resolutions for suitable left-exact functors or other derived-category constructions. The method depends on which exactness properties and resolutions are available.

The first derived functor of tensor product is usually written Tor one. Higher Tor groups come from homology at higher degrees of a projective resolution after tensoring. Degree zero returns ordinary tensor product. Thus the derived construction enriches the original functor with a graded family of answers that respond to the algebraic structure of relations and higher relations.

This is an example of a general categorical strategy. Replace an object by one that a functor handles well, apply the functor, then retain the invariant information that survives changing the replacement. The replacement is chosen for its mathematical behavior. It is not an arbitrary rewrite that happens to resemble the original object.

## Maps between complexes and a new notion of sameness

If chain complexes are to form a useful category, we need morphisms. A chain map consists of a homomorphism in every degree, with the requirement that those maps commute with the differentials. Whether we take a differential first and then map to the other complex, or map first and then take the other differential, the result must be the same.

A chain map sends cycles to cycles and boundaries to boundaries. Therefore it induces a map on each homology group. Composition of chain maps gives composition of the induced homology maps. This functorial behavior is the reason homology is more than a numerical summary; it can track how algebraic information changes under structured maps.

A quasi-isomorphism is a chain map that induces an isomorphism on every homology group. The source and target complexes need not be isomorphic degree by degree. For instance, consider a complex with a copy of the integers in two consecutive degrees and the identity map between them. Its homology vanishes in every degree: every cycle at the lower degree is a boundary, and there are no nonzero cycles at the higher degree. The unique map from this complex to the zero complex is a quasi-isomorphism even though the first complex has nonzero underlying groups.

In this example the complex is actually contractible. We can exhibit a homotopy contracting it, using an identity map that raises degree in the appropriate place. Contractibility is stronger than simply having zero homology for arbitrary complexes over arbitrary rings. An acyclic complex need not be contractible. This distinction is one reason the derived category is constructed by formally inverting quasi-isomorphisms rather than identifying only complexes related by chain homotopies.

The phrase 'formally inverting' means that a quasi-isomorphism should act like an isomorphism in a new category even when it has no ordinary inverse chain map. This is a localization process. Its morphisms have a more intricate description than maps between the raw complexes, because we have changed which arrows count as equivalences.

## Why resolution is more than a bookkeeping trick

Return to the free resolution of the two-element group. The augmentation map from the resolution to the group concentrated in degree zero is a quasi-isomorphism. In a derived setting, those two presentations become equivalent. But applying tensor product term by term to the resolution can reveal information that applying the ordinary tensor product directly to the group would hide.

This raises a subtle question. If we are going to treat quasi-isomorphic complexes as equivalent, shouldn't tensor product preserve that equivalence? Ordinary termwise tensoring does not always do so. Our calculation of the nonpreserved injection is already a warning. A naive tensor construction can change an acyclic complex into one with nonzero homology.

The derived tensor product repairs this defect by choosing a homologically suitable replacement, for example a projective or suitably flat resolution, before tensoring. In the relevant derived category its result is defined up to the intended equivalence. Our free resolution was exactly such a replacement. The nonzero Tor one group is the degree-one homology of the derived tensor product.

One can also define derived tensor products using more flexible resolutions of complexes, rather than only short projective resolutions of modules. The homotopical framework organizes these replacements systematically. What remains invariant is the derived result, including its higher homology; the shape of the chosen resolution itself is auxiliary.

This helps clarify the connection between homological algebra and higher category theory. Ordinary derived categories identify suitable equivalences at a categorical level. Enhanced or stable infinity-categorical descriptions retain richer mapping information and coherent homotopies. To study the first Tor calculation, we need only chain complexes and their homology. To study higher coherences among constructions, the enhancement becomes more useful.

## A glimpse of simplicial methods

There is another way to see why complexes are natural inputs to higher algebra. A simplicial abelian group gives abelian groups in a sequence of dimensions, with face and degeneracy maps satisfying compatibility relations. The Dold–Kan correspondence relates simplicial abelian groups to nonnegatively graded chain complexes of abelian groups.

This is an equivalence of categories, not merely a numerical matching between their homology groups. The normalized chain complex of a simplicial abelian group and the corresponding denormalization construction preserve the algebraic information in a precise, mutually inverse way up to natural isomorphism. The nonnegative grading condition belongs to the theorem's formulation; one should not apply the statement unchanged to arbitrary unbounded complexes.

We do not need the details of the correspondence to finish the calculation at hand. Its existence shows how a diagrammatic description of higher-dimensional compatible data can turn into the more economical language of chain complexes and differentials. It also prepares a bridge from homological algebra to homotopy-coherent constructions, where maps between maps can carry information that ordinary sets of morphisms omit.

## Returning to multiplication by two

The original exact sequence said that the even integers were precisely the integers killed by reduction modulo two. Our free resolution encoded that fact using a map between free groups. Tensoring with the two-element group changed the map multiplying by two into a zero map. As a result, its degree-one kernel was no longer zero. The new homology group was the two-element group itself.

The calculation distinguished three objects that are often blurred together. The original module was the integers modulo two. Its resolution was a chain complex of free integer modules. The tensor product of that resolution with another module was a new complex whose homology contained both the ordinary tensor product in degree zero and a derived correction in degree one.

Homological algebra makes failures of exactness measurable and functorial. The chain-complex condition guarantees that boundaries are cycles. Homology records cycles not explained by boundaries. Resolutions provide presentations on which difficult functors can be applied safely, and derived functors retain the homological information that their ordinary versions discard. In our example the failure has an exact name and value: Tor one over the integers, of the two-element group with itself, is the two-element group.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

The short exact sequence over \(\mathbb Z\):
\[
 0\longrightarrow \mathbb Z\xrightarrow{\times2}\mathbb Z
 \xrightarrow{\mathrm{mod}\ 2}\mathbb Z/2\longrightarrow0.
\]
Set \(C_1=\mathbb Z\), \(C_0=\mathbb Z\), \(d_1=\times2\), and \(C_n=0\) otherwise. A chain complex has \(d_{n-1}d_n=0\), with
\[
 H_n(C)=\ker(d_n)/\operatorname{im}(d_{n+1}).
\]
For \(C\): \(H_0(C)\cong\mathbb Z/2\), \(H_1(C)=0\). The augmentation \(C\to(\mathbb Z/2)[0]\) is a quasi-isomorphism.

Tensor with \(\mathbb Z/2\) over \(\mathbb Z\):
\[
 C\otimes_{\mathbb Z}\mathbb Z/2:
 \quad 0\longrightarrow\mathbb Z/2\xrightarrow{0}\mathbb Z/2\longrightarrow0.
\]
Therefore
\[
 \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)
 \cong\mathbb Z/2,\qquad
 \operatorname{Tor}_0^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)
 \cong\mathbb Z/2.
\]
In general, for a projective resolution \(P_\bullet\to M\),
\[
 \operatorname{Tor}_n^R(M,N)=H_n(P_\bullet\otimes_R N).
\]
For arbitrary possibly noncommutative \(R\), specify the appropriate right and left module structures; over \(\mathbb Z\) both inputs are ordinary abelian groups.

A chain map \(f:C\to D\) satisfies \(d^D_nf_n=f_{n-1}d^C_n\). A quasi-isomorphism induces isomorphisms on every \(H_n\). An acyclic complex need not be chain-contractible over an arbitrary ring.

### Exercises with answers

1. **Exactness.** What is the kernel of reduction modulo two from the integers? **Answer:** the even integers, which are the image of multiplication by two.
2. **Homology.** Compute the degree-zero homology of the complex \(\mathbb Z\xrightarrow{\times2}\mathbb Z\). **Answer:** \(\mathbb Z/2\).
3. **Tensor failure.** What is multiplication by two on \(\mathbb Z/2\)? **Answer:** the zero map; its kernel is all of \(\mathbb Z/2\).
4. **Derived invariant.** What is \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)\)? **Answer:** \(\mathbb Z/2\).
5. **Base ring.** Why is it important to specify \(\mathbb Z\) in the Tor calculation? **Answer:** the result can change with the base ring; vector spaces over a field are flat and have vanishing higher Tor over that field.
6. **Quasi-isomorphism.** Does a quasi-isomorphism need to be an isomorphism of groups in each degree? **Answer:** no; only the induced homology maps must be isomorphisms.

### References

- The Stacks Project, *Homological Algebra* and *Derived Categories*: exact sequences, complexes, projective resolutions and derived tensor products.
- Charles A. Weibel, *An Introduction to Homological Algebra*, resolutions, Tor and derived functors.
- Saunders Mac Lane, *Homology*, chain complexes and homological constructions.
