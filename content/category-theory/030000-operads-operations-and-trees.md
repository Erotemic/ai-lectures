# 030000 — Operads: How Operations Compose Inside Operations

**Track:** Introduction to Category Theory. **Background:** functions, monoids, category composition, symmetric monoidal categories, and trees. **Theme:** many-input operations, substitution, associativity, and topological operads.

<!-- BEGIN SPOKEN LECTURE -->

# Operads: How Operations Compose Inside Operations

Take three numbers: two, three, and four. You can add all three, giving nine. You can multiply all three, giving twenty-four. You can first multiply two and three, then add four, giving ten. If you organize the calculation differently, you may obtain a different answer. To reason about these calculations, we need to record not only the operation applied, but also the number and order of its inputs, and the way one operation has been inserted into another.

Ordinary category theory is built around arrows with one input object and one output object. Composition joins two arrows end to end: the output of one becomes the input of the next. But algebraic operations often have several inputs. Addition takes two numbers. A three-way merge combines three records. A tree-shaped computation can take many inputs, route them through several intermediate operations, and produce one output.

An operad captures the grammar of these many-input operations and the laws governing their substitution. It is a compact way to describe structured computation, algebraic multiplication, and composition in settings where operations themselves have slots. Operads also connect algebra to topology, because the ways geometric configurations can be inserted into one another carry continuous families of operations and higher symmetries.

## From a binary operation to a tree

Begin with a binary operation m on a set A. It accepts two elements and returns one. To apply m to three elements we need two copies of m. We can combine the first two inputs and then combine the result with the third, or combine the last two and then combine that result with the first.

If m is addition, both trees produce the same answer. For two, three, and four, the left tree gives two plus three equals five, then five plus four equals nine. The right tree gives three plus four equals seven, then two plus seven equals nine. Associativity says that these two composite operations are equal for every triple of inputs.

If m is subtraction, the trees differ. The left tree gives two minus three equals negative one, then negative one minus four equals negative five. The right tree gives three minus four equals negative one, then two minus negative one equals three. An operad should be able to describe both trees before imposing any equation between them. The algebraic structure we choose determines whether the trees evaluate equally.

This separation between formal syntax and interpretation is familiar from free algebras and monads. Operads emphasize the shape of multi-input composition. They tell us how an operation with k slots can accept another operation inside each slot, producing a larger operation whose input count is the sum of the inner input counts.

## Count the slots before composing

Suppose f is an operation with two input slots. Suppose g takes three inputs, and h takes two. If we place g in the first slot of f and h in the second, the resulting composite takes five inputs. Its value on five entries is obtained by passing the first three to g and the last two to h, then passing the two results to f.

This count gives a useful invariant. The outer operation has two slots, but after substitution they have expanded into three and two slots, making five. In general, an operation with k slots accepts k inner operations of arities n one through n k, and the composite has arity equal to their sum.

Substitution has associativity laws of its own. We might first construct the inner subtrees and then insert the results into an outer tree, or substitute all the small operations in one larger step. Both descriptions should produce the same composite operation. There is also a one-input identity operation, which changes nothing when inserted into a slot.

These are the core laws of an operad. They resemble category associativity and identity, but at the level of operations with multiple inputs. The pictures are rooted trees: leaves are inputs, internal vertices are operations, and the root is the output. Tree substitution expresses the algebraic composition.

## A nonsymmetric operad

Let us begin without allowing input permutations. A nonsymmetric, sometimes called planar, operad has a collection of operations for each number of ordered input slots, including possibly zero slots. It has a distinguished one-input identity and substitution operations obeying associativity and unit laws.

The word planar means that the order of inputs matters and is preserved in the syntax. In a tree drawn on paper, the left-to-right order of the leaves is part of its structure. We do not assume that swapping the first and second inputs is permitted or that it leaves an operation unchanged.

Consider the simplest nonsymmetric operad with exactly one operation of each arity, including arity zero. Since there is only one possible operation for each number of inputs, substitution is forced by arity counting. Its algebras in sets are monoids: the unique binary operation becomes multiplication, the zero-input operation selects the identity, and the operad laws force associativity and the unit equations.

Why does the same description work for noncommutative monoids? Because we have not introduced a rule for permuting input slots. A string monoid concatenates words in a specific order. The product of a then b is not generally the product of b then a. The nonsymmetric operad remembers the order and therefore allows this distinction.

## The algebra of an operad

An operad is a collection of abstract operations. To use it, we choose a mathematical object A and assign to each abstract operation a concrete operation on A. Such an assignment must preserve the identity operation and substitution. This is called an algebra over the operad.

For the associative operad, choosing an algebra means choosing a multiplication and an identity satisfying the familiar laws. For a different operad, the abstract operations may encode a Lie bracket, a commutative product, or a system of compatible operations with several kinds of inputs. The general principle is that the operad defines the allowed syntax and equations while the algebra interprets them in a particular setting.

There is a useful operad already associated with any set A: the endomorphism operad of A. Its operations of arity n are all functions from the n-fold Cartesian product of A to A. Composing operations means ordinary function substitution. For n equal zero, a function from the one-point set to A amounts to choosing a constant of A.

To make A into an algebra over an operad P is equivalent to giving a map of operads from P into this endomorphism operad. Each abstract operation is sent to an actual function on A, and the preservation laws ensure that every tree of formal operations evaluates consistently. The interpretation is compositional by construction.

## Why symmetry changes the story

Now suppose we want to reorder inputs. A symmetric operad allows the symmetric group on n letters to act on the n-ary operations. For a binary operation, swapping the two slots turns the operation that evaluates x followed by y into the operation that evaluates y followed by x. It does not automatically say these two operations are equal.

That distinction is crucial. A symmetric operad can describe a noncommutative operation precisely because it remembers the reordered operation as potentially different. To describe a commutative operation we impose an equation saying that swapping its inputs leaves its interpretation unchanged.

In the standard symmetric associative operad on sets, the operations of arity n can be indexed by permutations of n inputs. An algebra may multiply its inputs in each specified order. These operations become equal only when the chosen monoid happens to be commutative. By contrast, the commutative operad has exactly one operation for each arity and a trivial action by permutations. Its algebras are commutative monoids.

This is one of the subtle distinctions worth remembering. A symmetric structure provides the ability to express permutations; a commutative algebra asserts invariance under those permutations. Having wires that can cross in a diagram does not, by itself, prove multiplication commutes.

## Another familiar description: multiplication without parentheses

In an associative monoid, a product of four elements can be evaluated through several binary trees. Associativity says that changing parentheses has no effect, as long as the input order is fixed. So there is a well-defined four-input multiplication. Similarly there is a multiplication for any finite number of inputs, with the empty product interpreted as the identity.

The nonsymmetric associative operad packages all these multiplications into one system. Rather than state associativity separately for every new number of inputs, it records one general substitution law that implies all the parenthesization agreements.

This is why operads are useful for describing algebraic structure: they are systematic about how the number of inputs changes. A monad on sets also describes freely generated algebraic expressions, and finitary algebraic theories can encode familiar operations. Operads focus particularly on operations assembled through tree substitution. They work naturally in symmetric monoidal categories where combining inputs need not mean taking Cartesian products.

For example, in vector spaces the inputs of a multilinear map combine through a tensor product. An operad in vector spaces can specify compatible multilinear operations, not merely ordinary functions of sets. This provides a common language for associative, commutative, Lie, and other algebraic structures.

## What trees permit and what they do not

A useful test of an algebraic formalism is to ask which manipulations of variables it can express. In an operadic tree, each input leaf feeds into one designated slot. Substitution grafts one tree into another, respecting the list of input positions. Permutations can reorder the leaves in a symmetric operad, but they do not automatically create extra copies of a leaf or discard one.

For example, the operation that takes two numbers x and y and returns x plus y has two input slots. We can compose it with other operations and obtain a larger tree. But the expression x plus x duplicates the same input variable. To represent that expression as an operation on just one variable, we need a diagonal map sending x to the pair x,x, or another mechanism that explicitly supports copying.

Operads and algebraic theories handle copying and discarding differently. In a Lawvere theory based on finite products, diagonal and projection maps provide copying and discarding, so equations may repeat variables or omit them. A plain operad organizes many-input operations and their substitutions; its trees naturally use each leaf once. In a cartesian setting an algebra may of course evaluate the same value at two leaves, but the duplication is supplied by the ambient product structure rather than by the bare operadic substitution rule.

The distinction is a source of expressive power, not a defect. In linear algebra or resource-sensitive computation, copying an input may be restricted or costly. Operadic composition can describe the legal multi-input wiring without silently assuming unlimited duplication or deletion. It lets us study operations in symmetric monoidal categories whose tensor product does not provide natural diagonal maps.

## Colored operads and types

So far every operation has inputs of the same general kind and an output of that kind. But real workflows often have several kinds of objects. An operation may take one image and one configuration file and produce a rendered frame. Another may take two frames and produce a comparison result. A third may convert a comparison into a report.

These operations have typed slots. We cannot insert a report where an image is required merely because both are represented by some software object. A colored operad assigns a color, or type, to every input and output. Substitution is permitted when the output color of an inner operation matches the color of the slot it is inserted into.

A colored operad is closely related to a multicategory. In an ordinary category, an arrow has one source and one target. In a multicategory, an arrow can have a list of source objects and one target. Composition substitutes many-source arrows into the input positions of another arrow.

This extends the idea of typed composition without assuming that all the inputs can first be packaged into a product object. It is a useful language for multilinear algebra, physical processes, and typed computation. The types prevent invalid combinations, and the operad laws express how valid combinations associate.

## A concrete permutation calculation

Let A be the set of strings. Use concatenation as multiplication. Take the two strings a b and c. Their product in that order is a b c. Swap the two inputs, and the product becomes c a b. They are not the same string.

A symmetric associative operad has one operation for the original order and another for the reversed order. The action of the two-element permutation group interchanges them. An algebra sends the first to ordinary concatenation and the second to reversed concatenation. The equivariance condition says that permuting the inputs before evaluation agrees with using the permuted abstract operation.

Now take ordinary integer addition. The original and reversed operations evaluate equally, because x plus y equals y plus x. The symmetric associative operad can still act on that commutative monoid; some distinct abstract operations have the same interpretation. To specify commutativity as part of the theory rather than as a happy accident of one example, use the commutative operad.

This calculation separates three ideas that are often conflated: an operation, a way to permute its input positions, and an equation making the operation insensitive to those permutations. The distinctions continue to matter in topological operads, where operations can move continuously rather than simply being permuted discretely.

## Geometric operations: little disks

Imagine a large circular disk on a tabletop. Inside it place two smaller, disjoint disks. Now place three tiny disks inside the first small disk and two tiny disks inside the second. If we rescale and insert those arrangements into the original little disks, we obtain an arrangement of five disjoint disks in the large one.

This is operadic substitution made physical. The outer two-disk configuration has two slots. The inner configurations have three and two slots. Inserting them produces a five-disk configuration. The positions and sizes vary continuously, so the collection of operations is a topological space rather than a discrete set.

In the little two-disks operad, the allowed operations are arrangements of disjoint embedded disks, with substitution defined by rescaling and insertion. There are versions in other dimensions, with one-dimensional intervals, two-dimensional disks, three-dimensional balls, and so on. Their homotopy-theoretic structures differ because the configurations can move around one another differently in different dimensions.

For two disks in a plane, one disk can travel around the other along a loop without the disks colliding. Such loops lead toward braid-group behavior. In one dimension, intervals cannot pass one another while remaining disjoint and preserving their order. In higher dimensions the relationship between motion, permutation, and homotopy changes again.

## The meaning of E one and E infinity

The operad of little one-dimensional intervals supplies a homotopy-coherent form of associativity. Its algebras in suitable spaces are called E one algebras. One often thinks of them as spaces with multiplication associative up to coherent homotopy rather than necessarily on the nose.

Little two-disks lead to E two algebras. Here the operations have room for planar configurations and their braiding phenomena. This is a richer structure than one-dimensional multiplication. It still does not assert that every product is strictly commutative as a literal equality of points in a space.

An E infinity operad encodes a homotopy-coherent form of commutativity. Its algebras can have coherent paths, higher homotopies, and comparisons corresponding to all permutations. In homotopy theory, these distinctions preserve important structure that would be erased by insisting every associative or commutative equation be strictly true at the point-set level.

The exact definition of E infinity uses conditions on the spaces of operations and their symmetric-group actions. It is not enough to label an arbitrary operad E infinity because its operations look flexible. The mathematical companion gives a precise model-independent description and notes the required hypotheses for typical statements about its algebras.

## Checking a tree substitution law

Let's follow one calculation through three levels of operations. Let f accept two inputs. Let g and h also accept two inputs, and let k accept three. First insert g and h into f. That makes a four-input operation. Then insert k into the first of those four leaves, leaving each of the other three leaves filled by the one-input identity. The result has six input positions: three from k and one from each remaining original leaf.

Alternatively, first insert k into the first input slot of g. That turns g into a four-input operation. Then insert this modified g and the original h into f. Again we obtain an operation with six inputs. Both constructions have the same rooted tree after all substitutions are performed, even though we performed the steps in a different order.

The operad associativity law says that these two composites are equal. This is a higher-arity version of ordinary function composition associativity. It guarantees that we do not have to record an accidental construction history for each compound operation: once the tree and its labeled vertices are specified, successive substitution can be evaluated in either permitted grouping.

There is also a concrete type check. If a colored operad gives k an output type that does not match the chosen input type of g, the first insertion is undefined. The entire composite tree is then ill-typed. Associativity relates only legal substitution paths. This is a helpful rule in programming-language semantics, where operation composition must preserve the types of every slot.

## A bridge to higher category theory

Why does this belong after lectures on higher categories? Because operads show how coherence appears even when the basic operations have several inputs. An ordinary associative law compares two binary trees. In topology, that comparison may be a path rather than an equality. Choices of paths can themselves be related by homotopies. Higher coherence records how all those comparisons fit together.

An ordinary monoidal category is an example of an algebraic environment where operations combine side by side. Operads organize the multi-input operation shapes that can live inside such an environment. Higher operads and infinity-operads then enrich the substitution laws with homotopical information.

That said, one should not conclude that every operad is a higher category or every monad is an operad. They are related but different tools. An operad can be viewed as a single-output multicategory with one color. A monad captures a broader algebraic pattern of endofunctor, unit, and multiplication. In suitable finitary contexts, operads give rise to monads, but the concepts should not be identified without construction.

The concrete connection is easy to remember: an operad makes trees of many-input operations composable. A monad describes a type of structured expression and how nested expressions flatten. Both encode composition and laws, but organize the inputs differently.

## What an operad lets us see

We began with three numbers and two subtraction trees that gave different answers. Those trees were not errors; they were distinct composites. An associative algebra identifies some trees, a commutative algebra identifies additional operations obtained by permuting inputs, and a topological algebra may relate operations through coherent paths rather than literal equality.

Operads provide a clean vocabulary for these distinctions. Arity counts inputs. Substitution builds a larger operation from smaller ones. The identity and associativity laws make that substitution consistent. Symmetric actions let us track rearrangements, and colored versions ensure type compatibility.

The gain is practical as well as conceptual. Whenever an operation must compose with operations of varying input count, we can ask what tree shapes are allowed and what equations they satisfy. Those questions arise in algebra, topology, geometry, and typed computation. An operad packages the answers so they can be transported from one mathematical setting to another without rebuilding the grammar each time.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

A **nonsymmetric operad** \(P\) in \(\mathbf{Set}\) has sets \(P(n)\), an identity \(1\in P(1)\), and substitution maps
\[
\gamma:P(k)\times P(n_1)\times\cdots\times P(n_k)\longrightarrow P(n_1+\cdots+n_k),
\]
obeying tree-substitution associativity and unit laws. A symmetric operad additionally has compatible right actions of \(\Sigma_n\) on \(P(n)\).

For an object A in a symmetric monoidal category \((\mathcal V,\otimes,I)\), the endomorphism operad has
\[
\operatorname{End}_A(n)=\mathcal V(A^{\otimes n},A),
\]
with \(A^{\otimes0}=I\) and composition given by substitution. A P-algebra is an operad morphism \(P\to\operatorname{End}_A\) (with suitable enrichment if P is not set-valued).

The **planar associative operad** has \(\mathrm{Ass}_{\rm ns}(n)=\{*\}\) for each \(n\ge0\); its Set-algebras are monoids. The **symmetric associative operad** has \(\mathrm{Ass}(n)=\Sigma_n\), whereas \(\mathrm{Com}(n)=\{*\}\) with trivial symmetric action; their Set-algebras are respectively monoids and commutative monoids. Conventions about nullary operations distinguish unital and nonunital versions.

For the little d-disks operad \(E_d\), \(E_d(n)\) parametrizes configurations of n disjoint labeled little disks embedded into a unit d-disk, with composition by rescaling and substitution. An \(E_\infty\) operad is a symmetric topological operad with contractible operation spaces and free \(\Sigma_n\)-actions (in a common standard model). These notions support coherent, rather than necessarily strict, commutativity in spaces or chain complexes.

### Exercises with answers

1. **Arity.** Substitute a three-input and a two-input operation into a two-input operation. What is the resulting arity? **Answer:** five.
2. **Associativity.** Compare \(m(m(x,y),z)\) and \(m(x,m(y,z))\) for addition and subtraction on integers. **Answer:** addition agrees by associativity; subtraction can differ, e.g. at 2,3,4 it gives -5 and 3.
3. **Symmetric versus commutative.** Why may a symmetric operad have a noncommutative algebra? **Answer:** the group action tracks permuted operations; it does not require them to be equal.
4. **Nullary operations.** What structure is encoded by the unique zero-input operation of the unital associative operad? **Answer:** a selected unit element of the algebra.
5. **Colors.** When can \(g\) be inserted in an input slot of \(f\) in a colored operad? **Answer:** when the output color of g matches the required input color of that slot.

### References

- J. P. May, *The Geometry of Iterated Loop Spaces* (1972).
- Jean-Louis Loday and Bruno Vallette, *Algebraic Operads* (2012).
- Tom Leinster, *Higher Operads, Higher Categories* (2004).
- nLab articles on operads, associative operads, and little disks.
