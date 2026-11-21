# When a Sentence Meets a Structure: The Mathematics of Models

<!-- BEGIN SPOKEN LECTURE -->

Consider two diagrams of points and connecting lines. In the first, every point is connected to every other point. In the second, some connections are missing. We can say, in ordinary English, that every pair of distinct points in the first diagram shares an edge. But what would it take for a formal language to express that property precisely? And what would it mean for one diagram to satisfy a statement written in that language?

This is the beginning of model theory. It studies mathematical structures as interpretations of formal languages, and it asks what can be expressed, what follows from a collection of sentences, and what different structures can satisfy the same sentences. It offers an important shift in perspective. A theorem is no longer only a statement about the intended natural numbers or a favorite class of graphs. It is a relationship between formulas and all the structures in which those formulas hold.

To see the machinery working, we will use graphs. The examples are familiar enough to visualize, but they can reveal surprising limitations of first-order language. The point is not to make ordinary graph theory more complicated. It is to discover exactly what a logical sentence sees and what it cannot see.

## We first choose a vocabulary

A formal language has symbols, but a symbol is not yet an object. For graphs, choose one binary relation symbol E. We intend E of x and y to mean that x is connected to y. We can also use equality, logical connectives such as and, or, not, and implies, and quantifiers for every and there exists. Variables such as x, y, and z are placeholders for vertices.

A structure for this language chooses a nonempty domain of objects and interprets E as a binary relation on that domain. For an undirected simple graph, we would additionally ask that the interpretation be symmetric and irreflexive. Those conditions can themselves be expressed as first-order sentences. Symmetry says for all x and y, if E of x and y then E of y and x. Irreflexivity says for every x, E of x and x is false.

A complete graph satisfies the sentence: for every x and y, if x is different from y, then E of x and y. A graph with no isolated vertices satisfies: for every x, there exists y distinct from x such that E of x and y. A graph containing a triangle satisfies: there exist three pairwise distinct vertices x, y, z with E of x and y, E of y and z, and E of z and x.

Notice that the first two statements speak about all vertices, while the last needs witnesses. The same sentence can be true in many different structures. Every complete graph with at least two vertices satisfies the no-isolated-vertex sentence, but many non-complete graphs satisfy it too. A sentence can constrain a structure without describing it uniquely.

## Syntax is not truth

The string for all x there exists y E of x and y is a formula assembled according to grammatical rules. Its grammatical legitimacy is a syntactic fact. Whether it is true is a semantic fact depending on a structure. In a graph with no isolated vertices and with a loopless edge relation, it is true. In an edgeless nonempty graph, it is false.

What about the expression E of x and y, with x and y left free? That is a formula but not a sentence. It does not have a truth value in a structure until we give an assignment of values to the free variables. Assign x to Alice and y to Bob, and it says whether those two vertices share an edge. Change the assignment and the truth value may change. A sentence has no free variables, so it can be evaluated in a structure without an extra assignment.

A precise semantics proceeds recursively. An atomic relation statement is evaluated using the relation chosen by the structure. A negation is true when its subformula is false. A conjunction is true when both parts are true. An existential quantifier is true when there exists a domain element that makes its body true under the updated assignment. A universal quantifier is true when every domain element makes its body true.

These rules look almost obvious. Their importance is that every formula has a determinate interpretation given a structure and assignment. This is the satisfaction relation, often written M satisfies phi. It is not the same thing as derivability from axioms. We need to preserve that distinction from the beginning.

## A small change in quantifiers changes the mathematics

Consider two statements. The first says: for every person, there exists someone they admire. The second says: there exists someone whom everyone admires. In the first, the chosen admired person may depend on the admirer. In the second, one witness must work simultaneously for all people. These are different logical conditions.

For a graph, compare every vertex has a neighbor with there is a vertex adjacent to every other vertex. A cycle with four vertices satisfies the first statement. Each vertex has two neighbors. It fails the second because every vertex has a nonneighbor. A star with a central vertex satisfies both, assuming at least two vertices.

Quantifier order also explains why a proof in one mathematical context may not transfer to another. For all inputs, there exists a good output is a weaker assertion than there exists a single output that is good for every input. Numerical optimization, analysis, and mathematical logic repeatedly hinge on such dependencies. Formal semantics forces us to name them.

## Theories are collections of constraints

A theory is a set of sentences in a chosen language. We say a structure is a model of the theory if it satisfies every sentence in the set. For example, the theory of undirected simple graphs contains the symmetry and irreflexivity axioms. It does not fix the number of vertices or demand connectivity. An edge-free graph is a model, and so is a triangle.

We can add sentences to narrow the class. Add that every vertex has a neighbor, and edge-free graphs disappear. Add that no three distinct vertices form a triangle, and triangles disappear. The remaining structures need not all look alike. A long cycle, a collection of disjoint edges, and many infinite graphs could still satisfy the strengthened theory.

Say T semantically entails phi if every model of T satisfies phi. The notation is often T double-turnstile phi. By contrast, T proves phi means there is a formal derivation of phi from T in a specified proof system; that is written with a single turnstile. Soundness says derivability implies semantic entailment. The completeness theorem for first-order logic says semantic entailment implies derivability. That result will need a proof, but the two definitions must remain separate even after we know they coincide extensionally for first-order consequence.

There are also theories in languages richer than graph adjacency. A group uses multiplication, an identity constant, and possibly inverse. An ordered field uses addition, multiplication, order, constants zero and one, and equations expressing their relationships. First-order logic provides a common language in which these different structures can be studied.

## What a sentence cannot look at

For finite graphs, connectivity is a familiar property: there is a path between every pair of vertices. Could we write one first-order sentence saying a graph is connected, regardless of its size? We can describe a path of length one, or two, or three, using finitely many existentially quantified intermediate vertices. We can describe a path of length at most n for each fixed n. But connectedness permits arbitrarily long finite paths, and a single first-order formula has finite length.

That observation alone is not a proof that connectivity is undefinable, because a clever formula might express the property indirectly. The proper proof uses compactness. Briefly, introduce two distinguished vertices a and b, demand that the graph be connected, and also add for each natural n a sentence saying no path of length at most n connects a to b. Any finite fragment of these demands can be satisfied by a sufficiently long finite path. If connectedness were expressible by one first-order sentence, compactness would provide a model satisfying all demands. Then a and b would be connected by some finite path and by no finite path. Contradiction.

The important subtlety is that this argument works for arbitrary graphs. Among finite graphs, there are separate results about definability and logical resources; compactness itself produces an infinite model and does not directly settle a finite-only definability claim. We should always state the class of structures over which a definability assertion is made.

The same example shows why first-order logic is both expressive and limited. We can write intricate sentences about local relations, and we can specify infinite theories with infinitely many constraints. But a single finite sentence need not capture a global property requiring arbitrarily long finite witnesses.

## Isomorphic structures agree on first-order sentences

Suppose two graph structures differ only in the names assigned to their vertices. One uses Alice, Bob, and Carol; the other uses zero, one, and two. If a bijection between the domains preserves and reflects adjacency, they are isomorphic. They must satisfy exactly the same first-order sentences in that language.

This is not merely intuitive. Prove it by induction on formulas. Atomic adjacency is preserved by the defining property of the isomorphism. Equality is preserved because a bijection is injective. Connectives preserve truth when their subformulas do. For an existential quantifier, transport a witness through the bijection; for a universal quantifier, use the fact that the bijection is onto. The induction also handles formulas with free variables under corresponding assignments.

The theorem says that first-order language cannot distinguish structures differing only by a renaming. That is exactly what we should want from a mathematical notion of structure. But the converse is not generally true for infinite structures: two nonisomorphic structures may satisfy all the same first-order sentences. A central theme of model theory is deciding when a theory determines one structure up to isomorphism and when it leaves many possibilities.

We have built the key ingredients: a language, an interpretation, truth under an assignment, models of a theory, logical consequence, and isomorphism. The mathematical question has shifted from what is this object to what can this formal language establish about the object, and about every other object satisfying the same axioms? That shift will make finite proof systems and infinite models interact in ways that are hard to anticipate from a single diagram.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Graph signature.** \(L=\{E\}\), one binary relation, with equality as logical equality. A simple undirected graph model satisfies
\[
\forall x\,\neg E(x,x),\qquad\forall x\forall y\,(E(x,y)\to E(y,x)).
\]
Other examples: \(\forall x\exists y\,(x\ne y\wedge E(x,y))\) (no isolated vertices); \(\exists x\exists y\exists z\,(x\ne y\wedge y\ne z\wedge z\ne x\wedge E(x,y)\wedge E(y,z)\wedge E(z,x))\) (a triangle).

**Semantics.** \(\mathcal M,s\models\exists x\,\psi\) iff for some \(a\in M\), \(\mathcal M,s[x\mapsto a]\models\psi\). A *sentence* has no free variables. \(T\models\varphi\) means every model of \(T\) satisfies \(\varphi\); \(T\vdash\varphi\) means there is a formal derivation in a specified proof calculus.

**Isomorphism invariance.** If \(h:\mathcal M\cong\mathcal N\), then \(\mathcal M,s\models\psi\) iff \(\mathcal N,h\circ s\models\psi\), proved by structural induction on \(\psi\). Hence \(\mathcal M\equiv\mathcal N\) (same first-order theory) is necessary but not sufficient for isomorphism among arbitrary infinite structures.

**Connectivity nondefinability.** For each \(n\) let \(\neg\mathrm{Path}_{\le n}(a,b)\) be a finite sentence about a bounded path. If \(\mathrm{Conn}\) were a first-order sentence defining connected graphs, the theory \(\{\mathrm{Conn}, a\ne b\}\cup\{\neg\mathrm{Path}_{\le n}(a,b):n\in\mathbb N\}\) would be finitely satisfiable by long paths but globally unsatisfiable, contradicting compactness. The auxiliary constants \(a,b\) are part of an expanded language.

**Exercises and solutions.** (1) Express at least three distinct vertices. *Answer:* \(\exists x\exists y\exists z\,(x\ne y\wedge y\ne z\wedge z\ne x)\). (2) Give a graph where every vertex has a neighbor but none is adjacent to all others. *Answer:* a cycle with four vertices. (3) Why does an isomorphism preserve existential sentences? *Answer:* transport a witness via the bijection and use the induction hypothesis. (4) Is a free-variable formula simply true or false in a structure? *Answer:* not until a variable assignment is supplied.

### Sources and reading

- Open Logic Project, *Sets, Logic, Computation*: https://slc.openlogicproject.org/
- Open Logic Project, *First-Order Logic*: https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf
- Stanford Encyclopedia of Philosophy, *Model Theory*: https://plato.stanford.edu/entries/model-theory/
