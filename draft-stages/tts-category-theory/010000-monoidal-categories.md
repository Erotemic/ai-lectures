# 010000 — Monoidal Categories: Composition Side by Side

**Track:** An Introduction to Category Theory. **Background:** categories, functors, natural transformations, products. **Theme:** tensor products, associators, unitors, symmetry, coherence, and resources.

<!-- BEGIN SPOKEN LECTURE -->

# Monoidal Categories: Composition Side by Side

A category lets us compose processes in sequence. A map takes an input of one kind and produces an output of another. The output of the first can become the input of the second. But many systems are assembled in two directions. We can do one task, then another. We can also do two tasks independently, side by side, and regard their combined output as one larger result.

Imagine two machines. One sorts parcels by destination. The other prints address labels. Each takes an input and returns an output. If they operate on independent batches, we can run them in parallel. What mathematical structure records the fact that the combined machine respects both machines' behavior?

Ordinary categories supply sequential composition. To describe independent parallel composition, we add a second operation, usually written as a tensor product. A **monoidal category** is a category equipped with such an operation, together with rules explaining how its grouping and identity behave. The name 'tensor' is broader than the tensor product of vector spaces. It can mean pairing data, placing systems side by side, adding resources, or composing algebraic quantities.

The crucial feature is that tensoring works on both objects and arrows. If one process changes its input while another does the same independently, their combined process has a precise meaning. We will build that meaning from finite sets, then ask why vector spaces require a different tensor, and finally see how resource arithmetic becomes categorical.

## Parallel functions

Suppose a function f converts Celsius readings to Fahrenheit, and another function g converts distances in kilometers to miles. One can apply f to a temperature and g to a distance independently. The combined input is a pair: a temperature and a distance. The combined output is a Fahrenheit value and a mileage value.

Formally, given f from A to B and g from C to D, we obtain a function from A paired with C to B paired with D. It sends the pair a,c to f of a, g of c. This is the cartesian product of functions, often written f times g.

Let's use small finite sets to calculate. Let A contain two temperatures, ten and twenty. Let C contain two distances, one and two. There are four combined inputs: ten with one, ten with two, twenty with one, and twenty with two. If f adds one and g doubles its input in this toy example, the four outputs are eleven with two, eleven with four, twenty-one with two, and twenty-one with four.

The parallel map does not need to inspect the other coordinate. Its first output depends only on A; its second output depends only on C. That independence is the structure carried by the cartesian product.

We should check how it interacts with sequential composition. Suppose f is followed by h, and g is followed by k. We could first combine f and g, then combine h and k, and compose those two parallel stages. Or we could form the composites h after f and k after g separately, then combine them. The results agree on every input pair. Both return h of f of a, alongside k of g of c.

This compatibility is sometimes called the interchange law. It is exactly the statement that taking pairs is a functor from the product category Set times Set into Set. On objects it returns cartesian products; on arrows it returns paired functions. It also preserves identity maps, because pairing two identities gives the identity on the product.

Once this law is available, a large process can be assembled by alternating sequential and parallel steps, without ambiguity about how their component functions combine.

## What happens when we regroup three inputs?

Now combine three systems A, B, and C. We could first pair A with B, and then pair the result with C. Or first pair B with C, and then pair A with the result. These are not literally the same set if we represent ordered pairs as nested objects. One has elements shaped like a pair whose first coordinate is itself a pair. The other has a pair whose second coordinate is a pair.

But there is an obvious bijection between the two shapes. Convert the nested pair containing a,b and then c into the pair containing a and the nested pair b,c. This map is called an **associator**. It changes grouping without changing any of the underlying data.

The associator must be natural. Suppose we transform a by f, b by g, and c by h. It should not matter whether we transform the three values before regrouping them or regroup first and then transform each component. Both give the same ordered triple of transformed values, displayed with the same final parentheses.

There is also an identity for parallel composition. For cartesian product in Set, use a one-element set as the unit object. Pairing A with a singleton adds an uninformative coordinate. A standard bijection removes it. Likewise, pairing a singleton with A can be unwrapped to A. These are the left and right unitors.

The unit object is not the empty set for cartesian product. Pairing A with the empty set gives the empty set, which destroys the data in A. An identity for parallel composition must allow us to recover the original object.

If your first instinct is to demand that all the reassociations be literal equality, consider how much that would make the definition depend on an arbitrary representation of nested pairs. We want the mathematics to be insensitive to those parentheses, but we must explain precisely why.

## The coherence question

With four objects, there are several ways to move parentheses. From a shape like A paired with B paired with C paired with D, different sequences of associators can lead to the same final grouping. If those sequences gave different maps, a large parallel system would depend on how the author happened to regroup it.

The associator therefore satisfies a pentagon identity: the two standard routes that change the grouping of four objects, through a pentagon of reassociations, must agree. The unitors and associator satisfy a triangle identity, expressing that introducing or removing the unit behaves consistently with regrouping.

These are not arbitrary decorations. They are the equations that make the notion of repeated tensoring usable. Mac Lane's coherence theorem says, in its standard monoidal form, that every diagram made from the specified associativity and unit isomorphisms, subject to the appropriate formal hypotheses, commutes. In practice, that allows mathematicians to suppress parentheses and unit objects when no ambiguity can result.

Suppressing them is a convenience after the theorem. It does not mean the associator was never needed. The chosen operation may not be strictly associative on its underlying representations; the coherence data tell us that all valid ways of comparing the groupings agree.

In finite sets, the theorem matches something we can check by hand: every reassociation simply moves the same ordered entries into a new pattern of nested pairs. Their order never changes. The final tuple is independent of the intermediate brackets.

## Monoidal structure beyond pairing data

Cartesian products are one example of a monoidal product. In the category of vector spaces over a fixed field, the ordinary algebraic tensor product gives another. If V has a basis of two vectors and W has a basis of three, their tensor product has a basis of six simple tensors, one for each ordered pair of basis vectors.

At first, that sounds like the cartesian product of two finite sets. But it is not. The tensor product of vector spaces has a special universal property: bilinear maps out of V times W correspond to linear maps out of V tensor W. The tensor product records the bilinear interaction of the inputs inside a linear object.

A useful calculation makes the difference clear. Suppose V and W are each two-dimensional. Their direct sum has dimension four. Their tensor product also has dimension four in this case, but that coincidence vanishes if we change dimensions: for V of dimension two and W of dimension three, the direct sum has dimension five while the tensor product has dimension six.

For linear maps f from V to V-prime and g from W to W-prime, the parallel map f tensor g acts on a simple tensor by sending v tensor w to f of v tensor g of w, then extends linearly. This rule is consistent because of the universal property of the tensor product. It is the analogue of pairing functions, but now the mathematical construction is driven by bilinearity.

The unit object is the field itself, viewed as a one-dimensional vector space. Tensoring V with the field yields a space naturally isomorphic to V. Again the unit is characterized by how tensoring behaves, rather than by having no elements.

A third example uses finite strings. The category with one object and a monoid of arrows has sequential composition given by monoid multiplication. Giving that category a second tensor operation on arrows, compatible with sequential composition, imposes extra conditions; we cannot simply announce that any two arbitrary multiplications work together. The interchange law is a real restriction.

This cautions us that the symbol tensor is not enough to create a monoidal category. The product on objects and arrows, its coherent comparison maps, and its compatibility laws are all required.

## Resources instead of functions

Let's change the setting. Suppose objects are nonnegative integers representing quantities of some resource. Declare that there is one arrow from m to n exactly when m is at most n. This is the poset of natural numbers viewed as a category. An arrow expresses an availability relation: a budget of n units suffices for a requirement of m units, given this choice of arrow direction.

Now define the parallel combination of objects by addition. Combining a requirement of two units with one of three units gives a requirement of five. Combining relations is sound because if m is at most n and p is at most q, then m plus p is at most n plus q.

The unit is zero: combining a requirement with zero changes nothing. Addition is strictly associative and commutative as an operation on numbers, so in this poset-category the associator and symmetry can be identities at equal numbers. This gives a simple **symmetric monoidal preorder**.

We can compute a practical consequence. Suppose a project demands two units of wood and another demands three. If one available supply contains four units and another contains five, we can infer the combined demand of five is within a combined supply of nine. That is the arrow from five to nine induced by the two independent arrows from two to four and from three to five.

But be careful about the interpretation. This arithmetic assumes the resources are fungible and the two uses are independent. If a piece of wood can be used in both projects, or if supply constraints depend on which machine is active, addition alone may describe the system poorly. Category theory expresses a model; it does not certify the model's empirical assumptions.

The choice of monoidal product tells us what 'together' means. With finite sets, together meant pairing independent inputs. With vector spaces, it meant a universal linearization of bilinear interactions. With resource quantities, it meant adding amounts.

## Must parallel order be interchangeable?

For products of sets, we can swap the two coordinates of a pair. There is a canonical map from A times B to B times A, sending a,b to b,a. This map is invertible and natural in both variables. It provides a **symmetry**: doing one independent task beside another can be described in either order without changing the essential data.

A monoidal category with a suitable symmetry is called symmetric monoidal. The symmetry must satisfy compatibility equations with associators and the unit, and swapping twice must bring us back to the start.

But ordinary monoidal categories need not have a swap at all. Consider words in the alphabet A and B, with concatenation as the parallel operation in a suitable discrete category of words. The word A followed by B is different from B followed by A; there is no arrow between distinct words in that discrete category. We have associative concatenation and an empty-word unit, hence a monoidal category, but not a symmetry between arbitrary pairs.

Other monoidal categories possess a braided structure. A braid lets one exchange neighboring strands, but exchanging twice need not undo the first exchange. The distinction becomes important when processes or particles have interactions that remember the route by which components pass one another. We will not assume braiding unless the categorical structure supplies it.

The order of the tensor factors is therefore mathematical data. 'Parallel' does not imply 'freely interchangeable.' A familiar cartesian product happens to have that extra structure; an arbitrary tensor product may not.

## Copying and discarding are further operations

Cartesian products of sets support two operations that are so routine we tend to overlook them. We can copy an element x into a pair x,x. And we can discard any element by mapping it to the unique element of the singleton set. Both are functions, natural in the appropriate sense.

These operations do not automatically exist for every monoidal product. In vector spaces, one might try to send v to v tensor v, but over an ordinary field that assignment is generally not linear: applying it to v plus w creates cross terms absent from the sum of the separate images. So it cannot serve as a linear copying map in the same unrestricted way.

For a numerical example, take a one-dimensional real vector space. The proposed copy sends a scalar x to x squared times a basis tensor. The copy of two is four times the basis tensor, but twice the copy of one is only two times it. The map fails linearity immediately.

This is one reason monoidal categories are useful in models of computation and physics. They let us distinguish the ability to put systems beside one another from the additional ability to duplicate or discard arbitrary states. In a cartesian category, those are closely related; in general monoidal settings, they require separate structure and may be restricted.

The examples also help explain why a picture of two wires side by side can be misleading if we interpret it too freely. Two wires say that two objects are combined. They do not say that information may be copied between wires, or that one wire may be discarded, unless the category contains maps representing those operations.

## An alternative tensor on the same category

It is instructive to see how much the tensor changes the meaning of 'together' even when the underlying category stays the same. On Set, cartesian product is a monoidal product, with a singleton as its unit. But disjoint union is also a monoidal product, with the empty set as its unit. Instead of pairing an A-value with a B-value, disjoint union stores either an A-value marked as coming from the left, or a B-value marked as coming from the right.

Take A with two elements and B with three. Their cartesian product has six elements: every choice from A paired with every choice from B. Their disjoint union has five elements: the two A-options and the three B-options, with tags so the sources do not collide. These two operations solve different mathematical problems. Cartesian product combines simultaneous information; disjoint union combines alternative possibilities.

On arrows, the disjoint-union tensor sends f on A and g on B to the function that applies f on the left-tagged elements and g on the right-tagged elements. It preserves identities and composition for the same reason paired functions do. Associators simply rebracket the tags; symmetries exchange the left and right tags. So Set carries both structures, each coherent and symmetric.

Why emphasize this? Because a monoidal category is a category together with a chosen tensor, not a category with one predetermined interpretation of parallelism. A theorem about all symmetric monoidal categories applies to both constructions, while a theorem using the universal property of cartesian products may apply to only the first. Even the unit object changes from a singleton to the empty set.

## The mathematical definition, assembled

We can now give the definition in one place. A monoidal category consists of a category C; a bifunctor from C times C to C, written tensor; a chosen unit object I; and natural isomorphisms for associativity and for the left and right units. These data obey the pentagon and triangle coherence identities.

Each part came from an obstruction. We needed a way to combine two processes, so tensor had to act on arrows. We needed to regroup more than two processes, so we introduced the associator. We needed a neutral process, so we introduced a unit object and unitors. We needed to know that regrouping could be done consistently, so we imposed coherence.

If an additional natural swap obeys the symmetry axioms, the category is symmetric monoidal. Without it, we must keep track of factor order. We can define monoidal functors that transport the tensor, with comparison maps satisfying their own compatibility equations. A strictly tensor-preserving functor is a particularly simple case, but strong monoidal functors preserve tensor up to coherent isomorphism.

Returning to our machines, a system built from sequential and parallel stages can now be expressed as a composite arrow. We can replace a subcomponent, regroup independent operations, and reason about the resulting system by categorical laws. At no point did we need to decide whether the physical system was a parcel sorter, a linear map, or a resource budget. Those interpretations supply different categories and different tensors, while the compositional principles remain shared.

That is the payoff. Ordinary categories explain what it means to follow one process with another. Monoidal categories explain what it means to build larger processes by running smaller ones together, with enough lawfulness that the assembly can be understood and checked.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Definition.** A monoidal category is \((\mathcal C,\otimes,I,\alpha,\lambda,\rho)\), where \(\otimes:\mathcal C\times\mathcal C\to\mathcal C\) is a bifunctor, \(I\) is a unit object, \(\alpha_{A,B,C}:(A\otimes B)\otimes C\to A\otimes(B\otimes C)\), \(\lambda_A:I\otimes A\to A\), \(\rho_A:A\otimes I\to A\) are natural isomorphisms satisfying pentagon and triangle coherence.

**Interchange:** \((h\otimes k)\circ(f\otimes g)=(h\circ f)\otimes(k\circ g)\) for type-compatible maps.

**Examples:** \((\mathbf{Set},\times,1)\); \((\mathbf{Vect}_k,\otimes_k,k)\); \((\mathbb N,\leq,+,0)\) as a symmetric monoidal poset. The discrete category of finite words under concatenation is monoidal and generally not braided.

**Symmetry:** Natural isomorphisms \(\sigma_{A,B}:A\otimes B\to B\otimes A\), with hexagon coherence and \(\sigma_{B,A}\circ\sigma_{A,B}=1_{A\otimes B}\).

**Copying limitation:** In \(\mathbf{Vect}_{\mathbb R}\), the diagonal-like map \(v\mapsto v\otimes v\) is not linear in general. Thus an arbitrary monoidal product does not supply cartesian copying maps.

### Exercises and answers

1. **Exercise:** Check interchange for the product of two functions on a pair. **Answer:** Both routes send \((a,c)\) to \((h(f(a)),k(g(c)))\).
2. **Exercise:** Identify the unit for tensoring vector spaces over a field \(k\). **Answer:** The one-dimensional space \(k\) with the natural unit isomorphisms.
3. **Exercise:** Why is empty set not a cartesian unit for Set? **Answer:** \(A\times\varnothing=\varnothing\), which is not isomorphic to nonempty \(A\).
4. **Exercise:** Is an associative tensor necessarily symmetric? **Answer:** No. Word concatenation is associative and unital, but reversing the order changes the word.

### References

- Saunders Mac Lane, *Categories for the Working Mathematician*, https://link.springer.com/book/10.1007/978-1-4612-9839-7
- Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality*, https://arxiv.org/abs/1803.05316
- MIT OpenCourseWare, *Applied Category Theory*, https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/pages/lecture-videos-and-readings/
- Peter Selinger, *A Survey of Graphical Languages for Monoidal Categories*, https://arxiv.org/abs/0908.3347
