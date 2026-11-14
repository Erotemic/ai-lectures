# 005000 — Limits and Colimits: Solving an Entire Diagram

**Track:** An Introduction to Category Theory. **Background:** products and universal properties. **Theme:** equalizers, pullbacks, pushouts, cones, limits, colimits, and preservation.

<!-- BEGIN SPOKEN LECTURE -->

# Limits and Colimits: Solving an Entire Diagram

A database contains students, courses, and enrollments. One table records which student an enrollment belongs to; another records which course it belongs to. Suppose we want the set of enrollment records for students in a particular department and courses in a particular semester. We are asking for records satisfying several compatibility conditions at once. Some pieces of information must agree after traveling through different maps.

Mathematics meets similar problems whenever two descriptions of the same object must agree. Two measurements may need to return the same value. Two projections of a structured record may need to identify the same person. Two functions from different sets may need to land at the same target value. Category theory captures these tasks with constructions called equalizers, pullbacks, and more generally limits.

A product pairs independent outputs: we have a map to A and a map to B, so we bundle them. A pullback adds a constraint: the A-output and B-output must become the same after being sent to some common target C. An equalizer asks where two competing maps give the same result. The extra equations are the heart of the new construction.

Our goal is to derive the general picture from small examples. Every example will have a universal property, and every universal property will specify both a way to build a candidate solution and a condition showing that the solution is unique. We will then turn arrows around to understand colimits, where components are glued together rather than jointly constrained.

## Equalizers: where two descriptions agree

Take functions f and g from a set A to a set B. We want to isolate exactly those elements of A for which f and g return the same value. The answer is the subset E containing the a's satisfying f of a equals g of a. Include E into A by the ordinary inclusion map.

Let's calculate a finite example. Let A be the integers zero, one, two, and three. Let f send a to its parity, even or odd. Let g send zero and one to even, and two and three to odd. At zero, both say even. At one, f says odd while g says even. At two, f says even while g says odd. At three, both say odd. Therefore the equalizer set E contains zero and three.

Why is the inclusion of E into A a universal solution? Any function h from a test set X to A with the property that f after h equals g after h must land entirely inside E. Thus h can be regarded as a function from X into E followed by the inclusion. This factorization exists, and it is unique because the inclusion distinguishes the elements of E.

The categorical definition does not explicitly mention subsets or individual elements. An equalizer of parallel arrows f and g is an arrow e from E to A satisfying f after e equals g after e, universal among all arrows with that property. That definition works in categories where objects are not sets and arrows are not ordinary functions.

In the category of vector spaces and linear maps, an equalizer of two linear maps from V to W is the kernel of their difference, included in V. Indeed, f of v equals g of v exactly when f minus g sends v to zero. We can solve an equalizer problem by linear algebra.

For example, take V to be the plane. Let f send the pair x,y to x plus y, and g send it to twice x. Equality requires x plus y equals two x, or y equals x. The equalizer is the diagonal line through the origin, with inclusion into the plane. Any linear map into the plane whose image lies on that line factors uniquely through the diagonal line.

## Pullbacks: two pieces sharing a value

Now take a function f from A to C and a function g from B to C. We want pairs consisting of an a in A and a b in B such that f of a equals g of b. The set of compatible pairs is a subset of the Cartesian product A times B. We call it the pullback.

Consider the set A of employees and the set B of building passes, with C the set of department identifiers. Let f assign each employee a department and g assign each pass the department that issued it. A pullback pair is an employee together with a pass issued by that employee's department. This does not certify that the pass is valid for the employee; it enforces precisely the equality of department labels. If we need more constraints, we must include them explicitly.

Use a tiny example to see the numbers. Suppose A has employees Ada, Ben, and Cy. Ada and Ben belong to research; Cy belongs to operations. Suppose B has passes R-one and O-one, issued by research and operations respectively. The compatible pairs are Ada with R-one, Ben with R-one, and Cy with O-one. There are three, even though the Cartesian product would have six pairs.

The pullback comes with two projection maps: one to A and one to B. Their composites to C agree, because each pair was selected to have the same department. If another set X has functions into A and B whose department outputs agree, then there is a unique function from X into the pullback that pairs those two outputs.

This is the universal property of a pullback. It looks much like the universal property of a product, but it includes an agreement condition in C. We can think of a product as a pullback over a terminal object, when such an object exists, because every map to the terminal object is automatically compatible.

A powerful special case comes from the preimage of a subset. Let B be a subset of C, included by g. For f from A to C, the pullback A times over C with B is the set of elements of A whose f-images lie in B, represented as compatible pairs. Up to the evident isomorphism, this is the ordinary inverse image of B under f.

In topology and geometry, pullbacks appear whenever we restrict a structure along a map. The details of what counts as a pullback depend on the category, and properties like continuity or smoothness must be checked. The categorical pattern says what a solution must do; it does not automatically guarantee existence in a chosen setting.

## What is a limit of an arbitrary diagram?

Products solve independent pairing problems. Equalizers solve parallel agreement problems. Pullbacks solve a fork-shaped agreement problem. We can see them as different diagram shapes with a common universal pattern.

A diagram assigns objects to the vertices of a small directed shape and arrows to its edges, respecting any compositional relations in that shape. A cone over the diagram consists of a candidate object X and compatible arrows from X to every object in the diagram. Compatibility says that whenever the diagram has an arrow from one vertex to another, following the corresponding cone arrow and then that diagram arrow agrees with the cone arrow directly into the target vertex.

A limit is a cone through which every other cone factors uniquely. It is a universal compatible vantage point on the whole diagram. In Set, one can often construct a limit by taking a product of all the vertex sets and keeping only tuples that satisfy every agreement equation. The indexing diagram must be small enough for the relevant constructions, and we assume the needed products exist.

The definition may feel larger than the examples, so return to the employee-pass problem. Our diagram has A and B both pointing to C. A cone from X chooses an employee and a pass for each element of X, plus a compatible department value in C. The compatibility equations say that the employee and pass assignments yield the same department. A limit object collects all pairs meeting that condition. Every other compatible collection maps uniquely into it.

In a poset viewed as a category, a limit of a finite discrete diagram is a greatest lower bound, or meet. A limit of a whole ordered diagram is a greatest lower bound of the objects in that diagram, with conditions already encoded by the order. Again, a set-theoretic tuple becomes an order-theoretic bound when we change categories.

## Reverse arrows: gluing and identifying

Colimits reverse the cone arrows. Instead of maps from a candidate object into the vertices, we have maps from the vertices into a candidate object. Compatibility requires that two routes through a diagram produce the same map into the candidate. A colimit is universal among such compatible receiving objects.

The simplest example is a coproduct, a disjoint union in Set. We put several sets side by side, keeping their elements tagged. But sometimes we want to identify elements across sets. A pushout performs controlled gluing along a common source.

Suppose a set C has two maps: one to A and one to B. A pushout of those maps receives injections from A and B, and it identifies the image of every c in C under the two maps. In Set, we start with the disjoint union of A and B, then take the quotient by the equivalence relation generated by those identifications.

Build a concrete example. Let A contain the labels north, center; B contain center, south; and let C be a singleton whose image in each set is the corresponding center label. The pushout has three elements, one for north, one shared center, and one for south. The two original center labels become the same element in the result.

The crucial word is generated. If multiple identifications overlap, transitivity may force further elements to become equal. Merely pairing the explicitly mentioned elements may not produce an equivalence relation. The quotient must enforce all consequences of symmetry and transitivity.

The pushout's universal property says that if functions from A and B into X agree on the shared C, then they extend uniquely to a function from the glued set into X. As with products, the universal rule captures the glue without prescribing the particular representation of equivalence classes.

## Coequalizers: force two maps to agree

An equalizer selects inputs on which two maps already agree. A coequalizer instead creates a quotient of the target so that two maps become equal after passage to that quotient.

Let f and g go from A to B. Form an equivalence relation on B generated by requiring f of a equivalent to g of a for every a in A. The quotient map q from B to the equivalence classes then satisfies q after f equals q after g. Any other map out of B that makes f and g equal factors uniquely through q.

For an explicit calculation, let A have two elements, one and two. Let B have symbols p, q, r, and s. Suppose f sends one to p and two to q, while g sends one to q and two to r. The relations force p equivalent to q and q equivalent to r, hence p, q, r all equivalent. The symbol s remains separate. The coequalizer is the two-element set consisting of the class p-q-r and the class s.

In groups and other algebraic categories, analogous quotients have to respect the algebraic operations. We cannot take an arbitrary equivalence relation on a group and expect the quotient to inherit a group structure. The relevant relation must be a congruence, or, for groups, arise from a normal subgroup. Category theory names the universal problem; algebra supplies the valid construction.

Products and equalizers can be used to build all small limits in categories that have the needed products and equalizers. Dually, coproducts and coequalizers can be used to build small colimits. This is a structural theorem about constructing a complex compatible diagram from simpler operations. Its proof organizes equations for each arrow into one equalizer between products; the companion states the construction.

## Pullbacks as a way to compose constraints

A pullback lets us combine two pieces of data that share a common value. What happens when three pieces must agree? Instead of inventing a new construction from scratch, we can compose pullbacks.

Suppose A is the set of employees, B the set of building passes, and C the set of department identifiers. The first pullback selects employee-pass pairs with matching departments. Now suppose D is the set of scheduled shifts and each shift is assigned a department. We can form another pullback between the set of compatible employee-pass pairs and D, using their shared department labels.

The result contains triples consisting of an employee, a pass, and a shift, all associated with the same department. We could instead first pair employees with shifts and then combine with passes. In Set, these two procedures produce canonically isomorphic collections of compatible triples. The ordering of the data in their nested representations may differ, but the agreement equations are the same.

This is an instance of the pasting property of pullback squares. Under appropriate hypotheses, putting two pullback squares side by side produces a larger pullback rectangle. Conversely, in the standard horizontal pasting arrangement, if the outer rectangle and the right-hand square are pullbacks, then the left-hand square is a pullback. The converse with the left-hand square cannot be asserted without additional assumptions. These facts let mathematicians construct large diagrams from reliable small pieces.

We can see the associativity-like behavior explicitly. Let maps f from A to C, g from B to C, and h from D to C assign department labels. One construction selects a pair a,b with f of a equals g of b, then pairs it with d satisfying the same label. Another selects b,d first and then pairs with a. Both parameterize exactly the triples a,b,d for which all three department labels are equal.

Of course, this does not establish that arbitrary data constraints can be rearranged without care. If one condition refers to a particular intermediate result, or if we change the maps to C, the final solution set can change. The theorem concerns specified commuting diagrams with specified pullbacks.

## A linear-algebra calculation with pullbacks

Take A and B to be copies of the real line, and C another copy of the real line. Define f of x to be twice x, and g of y to be three times y. Their pullback in real vector spaces consists of pairs x,y satisfying twice x equals three times y.

We can parameterize every solution by a number t: set x equal to three t and y equal to two t. This produces a one-dimensional vector subspace of the plane. The projection to A returns three t, and the projection to B returns two t. Their images in C agree because both are six t.

Now suppose another vector space X has linear maps p to A and q to B such that twice p equals three times q. There is a unique linear map from X into our solution line that sends a vector to the pair p of that vector, q of that vector. This is the pullback universal property in action.

The calculation is also an example of a linear constraint system. Multiple equations can be assembled into a combined matrix, and their common solution space is a kernel. This gives another connection: finite limits in categories of vector spaces can often be calculated using products and kernels. The categorical language organizes the constraints; linear algebra performs the arithmetic.

## Quotients are more subtle than deleting information

The coequalizer construction takes a relation generated by pairs of values and forces those pairs to become equal in a quotient. It is tempting to regard this as simple information loss. But a quotient has a particular universal role: it is the most general target in which the specified equalities hold.

Take B containing four symbols p, q, r, s, and require p equal to q and q equal to r. The quotient has two classes, one for p,q,r and one for s. Any function from B to X that sends p,q,r to the same value factors uniquely through the quotient. If somebody chooses a function that also sends s to that same value, the factorization still exists. The coequalizer does not force s to remain distinct in every subsequent target; it imposes only the necessary identifications itself.

This is the difference between a universal quotient and an arbitrary collapse. An arbitrary function may identify many unrelated values. The quotient determined by a relation identifies the values compelled by the relation, together with its equivalence consequences, and no others at the quotient stage.

In algebra this idea becomes even more powerful. For groups, forcing a relation such as a squared equals the identity requires quotienting by the normal subgroup generated by that relation, not merely identifying two raw elements as sets. Normality ensures that multiplication remains well-defined on equivalence classes. A categorical coequalizer in groups builds the algebraic congruence needed for the quotient to remain a group.

## Limits and computation

Many database joins resemble pullbacks of sets. A relational join on matching keys pairs rows whose key values agree. If each input table has a function assigning a key, the compatible rows form the pullback of those key functions. This gives a clean mathematical description of one kind of join.

The analogy has boundaries. Real databases can use multisets rather than sets, may allow null values with special comparison rules, and can attach ordering or update semantics. A categorical pullback in Set will not automatically model those details. But it can clarify the core equality constraint and expose exactly where operational features require additional structure.

The same point applies to software interfaces, geometry, and physical systems. We should not call every operation that joins two things a pullback. We should write down the diagram and verify that the proposed object satisfies its universal mapping property. Once verified, the properties of pullbacks become available as theorems rather than design metaphors.

A construction's universal property can also reveal its behavior under translation. The forgetful functor from groups to sets creates no problem for ordinary products and equalizers, but a functor that discards essential agreement information may fail to preserve a pullback. Preservation claims need proofs, often using an adjunction or a direct universal-property calculation.

## Preservation is a separate question

Suppose F is a functor between categories, and L is a limit of a diagram in the source. Does F of L give a limit of the translated diagram? Sometimes yes, sometimes no. When it always does for the relevant class of diagrams, we say F preserves those limits.

Consider the forgetful functor from groups to sets. It preserves products: the underlying set of the direct product of groups is a Cartesian product. It also preserves equalizers, because the elements on which two homomorphisms agree form an equalizer subgroup with exactly the expected underlying set. Therefore it preserves all small limits that exist in groups.

The same forgetful functor does not generally preserve coproducts. The coproduct of two groups is their free product, whose underlying set is not the disjoint union of the two underlying sets. A functor's treatment of composition and identity does not determine how it handles every universal construction.

There is a deep theorem tying this distinction to adjunctions: right adjoints preserve limits, while left adjoints preserve colimits, whenever those constructions exist. That theorem offers an efficient way to prove preservation results without reconstructing each limit from scratch. The statement has hypotheses about which functor is adjoint and which limits exist; its usefulness comes from those exact hypotheses.

## A warning about diagrams as pictures

A commuting square is more than four nodes connected by arrows. Its meaning depends on the category. A pullback square of sets can be verified with compatible pairs. The same picture in topological spaces requires a topology on those pairs and continuity of the structural maps. In groups it requires a group structure on the compatible pairs. A square that is a pullback in one category may cease to be one after we change the allowed arrows.

Likewise, a pushout should not be imagined as ordinary gluing in every setting. Topological gluing can produce quotient spaces with delicate separation properties. Algebraic pushouts can require free constructions and relations. The categorical definition transfers the universal pattern, while the details of existence and behavior come from the mathematical context.

This is part of the theory's strength. It provides a stable question that can be investigated separately in many fields. We can ask whether a particular limit exists, calculate it in a chosen category, then ask whether a functor preserves it. Each question is precise and can have a different answer.

## What we have actually built

The original database problem asked for compatible records. The equalizer retained precisely the inputs where two reports agree. The pullback paired records only when they shared a specified value. A general limit collected the information needed to satisfy every arrow equation in a diagram. Reversing the arrows led to colimits, quotients, and gluing.

Every construction came with the same structural demand: the proposed object must solve a mapping problem, and every other solution must factor through it uniquely. That uniqueness tells us how to compare two constructions. The shape of the diagram tells us which compatibility conditions we are solving.

Limits and colimits are a way to compute with entire networks of relationships, not merely isolated objects. They become especially powerful when combined with functors that preserve them, and with adjunctions that explain why those preservation laws hold. The techniques began with concrete pairings and equalities; they have grown into a language for systematically solving diagrams.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Equalizer:** \(e:E\to A\) of \(f,g:A\rightrightarrows B\) satisfies \(fe=ge\), and every \(h:X\to A\) with \(fh=gh\) factors uniquely through \(e\).

**Pullback:** For \(A\xrightarrow f C\xleftarrow g B\), in Set, \(A\times_C B=\{(a,b):f(a)=g(b)\}\), with projections \(p_A,p_B\) satisfying \(fp_A=gp_B\) and the universal property of compatible pairs.

**Pushout:** In Set, the pushout of \(A\xleftarrow i C\xrightarrow j B\) is \((A\amalg B)/{\sim}\), where \(\sim\) is the equivalence relation generated by \(i(c)\sim j(c)\) for all \(c\in C\).

**Small limits from products and equalizers:** Given \(D:J\to\mathcal C\) and all relevant products, form \(P=\prod_{j\in\operatorname{Ob}J} D(j)\) and \(Q=\prod_{(u:i\to j)\in\operatorname{Mor}J} D(j)\). Define \(s,t:P\rightrightarrows Q\) componentwise using \(D(u)\pi_i\) and \(\pi_j\). Their equalizer is the limit, provided products and the equalizer exist.

### Exercises and answers

1. **Exercise:** What is the pullback of a function \(f:A\to C\) and the inclusion \(B\subseteq C\)? **Answer:** The inverse-image subset \(f^{-1}(B)\), with its induced map to B.
2. **Exercise:** If two parallel functions are identical, what is their equalizer? **Answer:** The identity arrow of their common domain.
3. **Exercise:** How is a pushout different from a disjoint union? **Answer:** A pushout imposes identifications along the common source, whereas a disjoint union keeps summands tagged and separate.

### References

- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Saunders Mac Lane, *Categories for the Working Mathematician*, https://link.springer.com/book/10.1007/978-1-4612-9839-7
