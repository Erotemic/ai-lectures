# 011000 — String Diagrams: Proving Equations by Following Wires

**Track:** An Introduction to Category Theory. **Background:** monoidal categories, functors, natural transformations. **Theme:** graphical calculus, interchange, coherence, symmetry, and the limits of pictures.

<!-- BEGIN SPOKEN LECTURE -->

# String Diagrams: Proving Equations by Following Wires

Mathematical notation can make a simple pattern hard to see. Consider a system with two independent inputs. We transform the first input, transform the second input, and then send the two outputs into separate additional steps. We can write the whole process as a nested formula with tensor products and composition symbols. But there is another way to describe it: draw two wires, put two boxes on them, then put two more boxes downstream.

The picture is not just decoration. Given the right mathematical setting, it is a representation of a morphism. Two ways of drawing the same network can express an equation, and the allowable redrawings correspond to algebraic laws. This is the idea of a **string diagram**.

Our task is to make that statement precise enough to trust. We need a convention for what wires and boxes mean, a rule for parallel and sequential composition, and a clear boundary between legal transformations and attractive but false pictures. We will also see how diagrams help with proofs that are cumbersome in symbolic notation.

## One wire, one function

Take a function f from a set A to a set B. Draw a wire labeled A entering a box labeled f, and a wire labeled B leaving it. Read time down the page: input at the top, output at the bottom. The box represents f, not a machine with physical pipes. The wire label represents the type of value accepted or returned.

If another function g goes from B to C, place the g box below the f box and connect the B wire from f to the input of g. The picture is a single path through two stages. Its mathematical interpretation is g after f, a function from A to C.

Now draw two separate wires, one labeled A and one labeled X. Put f on the first and a function h from X to Y on the second. The picture has two input wires and two output wires. It represents the tensor product of f and h, an arrow from A tensor X to B tensor Y.

In the category of sets with cartesian product, that tensor is simply the paired function sending a,x to f of a, h of x. In another monoidal category, the interpretation of parallel wires may be different. The diagram's syntax is the same, but its meaning comes from the category and tensor we specify.

We have now assigned meanings to the two fundamental ways of assembling diagrams. Stacking boxes means sequential composition. Placing them side by side means tensor composition. A diagrammatic language becomes reliable when these constructions can be combined without contradiction.

## An equation you can see

Let f go from A to B and g from C to D. Let h go from B to E and k from D to F. There are two ways to assemble the network. One is to place f and g side by side, then place h and k side by side below them. Algebraically this is h tensor k, composed after f tensor g.

The other is to compose h after f along the left wire and k after g along the right wire, and then put those two composites side by side. Algebraically this is h after f, tensor k after g.

Both represent the same diagram. If we slide the left-hand boxes vertically past the right-hand boxes without changing which wires they connect to, nothing changes about the overall process. This is the interchange law of a monoidal category.

Let's calculate it for paired functions. Start with the input a,c. In the first organization, f and g produce f of a, g of c. Then h and k produce h of f of a, k of g of c. In the second organization, the left composite produces h of f of a and the right composite produces k of g of c. The paired output is identical.

The diagram lets us perceive why the equation holds even before evaluating the particular functions. The left and right components are independent, so their vertical placement relative to each other cannot change the result. The algebraic law formalizes that intuition.

This kind of argument scales. A complicated expression may contain many alternating tensor and composition symbols. Once we know its wiring pattern, we can often read the equality from a simpler diagram transformation.

## Identity wires and the role of parentheses

An identity morphism is represented by a plain wire without a box. Passing a value along the wire leaves it unchanged. Put an identity segment above or below f, and the path still represents f. This matches the left and right identity laws of a category.

A more subtle simplification concerns grouping. An expression such as A tensor B tensor C may be parenthesized in different ways. A monoidal category includes associator isomorphisms that convert those groupings. In diagrams we commonly place three wires side by side without drawing the parentheses. This convenience is justified by coherence: standard ways of regrouping by associators and unitors agree.

A diagrammatic proof is therefore using real mathematical results behind the page layout. Wires can be moved around to adjust spacing; parentheses can be suppressed; empty identity segments can be inserted. But none of those freedoms lets us exchange the order of wires unless a suitable exchange morphism exists.

For a monoidal category with noncommutative word concatenation, the order A followed by B has a different meaning from B followed by A. Drawing A on the left and B on the right is not interchangeable with the reverse arrangement. A careless picture that swaps them has changed the object.

That gives us a practical discipline. Begin by fixing the direction of reading and the order of boundary wires. Each diagram has an explicit source object and target object, obtained by tensoring the boundary labels in their stated order. Every box must have a matching input and output type. With those constraints, the picture becomes a typed expression rather than an illustration.

## Crossings mean something

Suppose the category is symmetric monoidal, like Set with cartesian product. Then there is a natural swap arrow from A tensor B to B tensor A. We can depict it by crossing two wires. The left input travels to the right output, and the right input travels to the left output.

For sets, this arrow sends a,b to b,a. If we cross the wires twice, the final output returns to a,b. That is the involutive law of symmetry. A crossing is therefore not an accidental feature of the drawing. It represents a specific morphism of the category.

Consider two functions f from A to C and g from B to D. There are two ways to apply them while exchanging the order of components. First apply f and g separately, then swap the outputs. Or first swap the inputs, then apply g and f in the new left-to-right order. Both return g of b, f of a. The equality is the naturality of the symmetry.

The string diagram makes this naturality equation easy to remember. You can move a pair of boxes across a crossing, provided each box stays on its own strand and the box labels are interpreted with the right types. The result is one underlying network viewed at two different heights.

But in a braided monoidal category, a crossing may not be its own inverse. One crossing can pass a strand over another, and a second crossing of the same orientation may produce a nontrivial twist. A braid needs a crossing and its actual inverse to undo the exchange. This is why a proof valid in symmetric monoidal categories may fail in braided ones.

A plain monoidal category may not have any crossing arrow. If the diagram language draws one anyway, the picture contains an operation whose existence has not been established. The drawing cannot justify that missing operation.

## Copying and deleting are not background graphics

Consider a set-valued function on one input. Suppose we want to use the same input twice: once in f and once in g. The intended output is a pair containing f of x and g of x. To build it from parallel boxes, we need an operation that duplicates x into two copies.

In Set, the diagonal map sends x to x,x. A string diagram draws this as a single input wire splitting into two output wires. The split is a node in the diagram, and its interpretation is a particular arrow, not the geometry of a wire that forks freely.

There is also a deletion map from any set to the singleton. We may depict it by ending a wire at a discard node. These operations have laws: copying in either order produces the same triple, and deleting one of the two copies after a split leaves the original value on the other wire.

Take an explicit set A containing zero and one. Copying one produces the pair one,one. Applying f to the first and g to the second produces f of one, g of one. If we omit the copy node and simply draw a free Y-shaped wire, we have hidden the crucial map that enables the two uses of the same input.

In the category of vector spaces with the usual tensor product, sending v to v tensor v is generally not linear. So an unrestricted split node cannot be assumed. This distinction has direct implications for how graphical languages model linear resources and quantum states. A category of quantum processes may support a different collection of allowed operations from a category of ordinary sets. The wiring language must respect those restrictions.

## A graphical proof using a diagonal

Let's prove a small naturality equation. For a function f from A to B, compare two routes from A to B paired with B. The first copies an A-value and then applies f to both copies. The second applies f once and then copies the B-value.

On an input a, the first route produces a,a and then f of a, f of a. The second produces f of a and then f of a, f of a. The outputs agree. Hence copying is natural with respect to every function in Set.

The corresponding string diagrams say that a function box can be moved through a copying node, provided it is duplicated onto both outgoing wires. This is a lawful diagram rewrite because the diagonal is natural in Set.

Now change the setting to a monoidal category with a chosen family of comultiplication maps on some objects. Such a family might fail to be natural with respect to arbitrary arrows. It may satisfy copying laws for selected maps or states only. The same visual movement of boxes is then not valid without an explicit theorem.

A diagrammatic calculation is never more general than its algebraic assumptions. This makes diagrams excellent at exposing hidden hypotheses: if a proof requires a wire split, it is asking for a diagonal-like map; if it requires a crossing, it is asking for a braiding or symmetry; if it requires bending a wire into a loop, it is asking for still more structure.

## Can we bend a wire backwards?

Some string diagrams show a wire curving around so that an output can be regarded as an input in a dual object. This is natural in linear algebra, where a finite-dimensional vector space has a dual space of linear functionals. But not every object of every monoidal category has such a dual.

In a rigid or compact closed setting, appropriate evaluation and coevaluation maps allow wires to bend, subject to identities sometimes called snake or zigzag identities. A bent wire then represents an honest composite of those maps. The picture can simplify expressions involving duals and pairings.

Here is the elementary finite-dimensional intuition. Let V have basis e-one through e-n and let V-star contain dual functionals. An evaluation map takes a functional and a vector and returns a scalar. The coevaluation map packages a sum of basis vectors paired with their dual functionals. If we evaluate one leg of that sum against a vector, the resulting combination reconstructs the original vector.

Diagrammatically, this is the straightening of a wire that bends around through a cup and a cap. But for arbitrary vector spaces of infinite dimension using the algebraic tensor product, this construction does not generally give a dualizable object in the same sense. The finite-dimensional hypothesis matters.

Likewise, drawing a feedback loop may require a trace operator or some other structure; an arbitrary monoidal category does not provide such loops automatically. The physical analogy of a cable returning to its own input can suggest a calculation, but the category must provide the arrow that interprets it.

## What is actually proved by deformation?

There is a mathematical theorem behind these pictures, commonly called a graphical coherence theorem. In the appropriate free monoidal or symmetric monoidal setting, diagrammatic deformations of the permitted kind correspond to equations forced by the axioms. Peter Selinger's survey collects graphical languages for many flavors of monoidal category and carefully distinguishes their scopes.

The phrase 'permitted kind' is indispensable. For plain monoidal categories, diagrams may be deformed without introducing crossings or reversing wire order. For symmetric categories, crossings are available and satisfy stronger equations. For braided categories, crossings obey braid relations but retain over-under information. For categories with duals, cups and caps become available under specific laws.

A diagram made from a specified signature of generators is interpreted by replacing each generating box with its morphism and composing according to the wiring. A sound rewrite gives the same morphism under every interpretation satisfying the axioms. Conversely, coherence theorems of the relevant kind tell us when the graphical language captures all equational consequences of those axioms.

This is not the same as saying that two diagrams that look similar must be equal. If one contains a generator f and another contains a different generator g, changing the drawing style cannot establish f equals g. If two wires cross differently in a braided setting, their pictures may record different braids. The theorem concerns precise topological or combinatorial equivalences under a specified language.

We can test a proposed rewrite on a simple model. If someone claims a free wire crossing is harmless in every monoidal category, take the discrete category of words with concatenation. No morphism exists from word AB to word BA when the words are distinct, so the alleged crossing cannot even be typed. A counterexample this small is enough to reject the general claim.

## A circuit assembled from components

Let us finish with a concrete system. An input is a pair consisting of a number and a Boolean flag. The left branch doubles the number. The right branch negates the flag. A following stage on the left adds three. A following stage on the right turns true into the word 'yes' and false into the word 'no.'

Using ordinary functions, we can compute this system by first taking the product of doubling and negation, then the product of adding three and converting the flag to text. Or we can compose the left-hand functions into 'double, then add three' and compose the right-hand functions into 'negate, then name,' and then take their product.

Feed in the number four and the flag true. The first route doubles four to eight and negates true to false. The second stage adds three to get eleven and names false as 'no.' The final output is eleven, 'no.' The second organization gives exactly the same answer. We have verified interchange on a particular input while the monoidal axioms show it for every type-compatible input.

What if we now want the text label to depend on whether the processed number exceeds ten? Then the branches are no longer independent. We need a new box that accepts both outputs, or a connection that routes numerical information into the labeling operation. The diagram must change to represent the dependency. We cannot keep two separate wires and pretend the right output knows the value on the left.

That is a powerful discipline for designing systems. A string diagram forces us to state what information enters each component. The laws tell us which rearrangements preserve meaning. The missing connections reveal when a proposed implementation depends on information it has not been given.

## A matrix calculation behind the picture

One way to check a string-diagram identity is to translate it into matrices. In the category of finite-dimensional vector spaces over a fixed field, a linear map becomes a matrix after choosing bases. Sequential composition becomes matrix multiplication. Parallel composition through the tensor product becomes a Kronecker product of matrices.

Suppose A is a two-by-two matrix and B is a three-by-three matrix. Their Kronecker product acts on a six-dimensional tensor-product space. Now suppose C and D are compatible output maps, of sizes two-by-two and three-by-three respectively. Applying A tensor B and then C tensor D produces the same matrix as applying C after A on the first factor and D after B on the second. Symbolically, the product of C tensor D with A tensor B equals C A tensor D B.

This is the interchange law seen in coordinates. Its validity is a consequence of how simple tensors behave: a vector v tensor w first becomes A v tensor B w, then becomes C A v tensor D B w. Either grouping gives the same result, and linearity extends the equality to every vector in the tensor product.

The visual diagram tells us the equation is structurally inevitable. The matrix calculation verifies it in a familiar numerical model. But it also shows why type labels are indispensable: if matrix dimensions do not match, the composites are not defined. A diagram with incompatible input and output wires is no more meaningful than an invalid matrix product.

## Read the wiring, respect the algebra

String diagrams make category theory visible by turning tensor into horizontal placement and composition into vertical connection. Identities become plain wires. Associativity coherence allows harmless regrouping. Symmetry becomes an explicit crossing. Copying, discarding, duality, and feedback require further operations and laws.

The best way to use a diagram is to treat it as a compressed proof obligation. Label the inputs and outputs. Name the category and its tensor. Identify the structural maps that the drawing uses. Then move boxes and wires only by equations that are valid in that setting.

If a calculation has five stages on three wires, symbolic notation can bury the idea under parentheses. A diagram exposes the interconnections. If a diagram invites an unjustified crossing or split, the algebra prevents it. The two representations work together: one makes structure easier to see, and the other states exactly why a visual transformation is correct.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Convention:** Inputs at top, outputs at bottom. Vertical stacking means \(g\circ f\); horizontal juxtaposition means \(f\otimes g\). A plain wire is an identity arrow. Boundary wires, read left to right, determine the ordered tensor product of the domain and codomain.

**Interchange law:** \((h\otimes k)\circ(f\otimes g)=(h\circ f)\otimes(k\circ g)\).

**Naturality of symmetry:** For \(f:A\to C\), \(g:B\to D\), \(\sigma_{C,D}\circ(f\otimes g)=(g\otimes f)\circ\sigma_{A,B}\). In a symmetric monoidal category \(\sigma_{B,A}\circ\sigma_{A,B}=1\).

**Copying in Set:** \(\Delta_A:A\to A\times A\), \(\Delta_A(a)=(a,a)\). Then \((f\times f)\circ\Delta_A=\Delta_B\circ f\). This is not automatic for a general monoidal category.

**Finite-dimensional duality:** A coevaluation \(k\to V\otimes V^*\) maps \(1\mapsto\sum_i e_i\otimes e^i\), and evaluation \(V^*\otimes V\to k\) maps \(\phi\otimes v\mapsto\phi(v)\); appropriate compositions satisfy snake identities. This uses finite-dimensionality for the standard dualizability claim.

### Exercises and answers

1. **Exercise:** Why can we slide independent boxes on different wires past each other? **Answer:** Bifunctoriality gives the interchange equation.
2. **Exercise:** Does a plain monoidal category license a wire crossing? **Answer:** No. A crossing requires a specified braiding or symmetry.
3. **Exercise:** Is drawing a Y-junction a legitimate copy map in every monoidal category? **Answer:** No; it must represent a morphism with the desired domain, codomain, and laws.
4. **Exercise:** Why does \(v\mapsto v\otimes v\) not provide a canonical linear duplication map for all vector spaces? **Answer:** It generally fails additivity and homogeneity, so is not a linear morphism.

### References

- Peter Selinger, *A Survey of Graphical Languages for Monoidal Categories*, https://arxiv.org/abs/0908.3347
- Brendan Fong and David I. Spivak, *Seven Sketches in Compositionality*, https://arxiv.org/abs/1803.05316
- Saunders Mac Lane, *Categories for the Working Mathematician*, https://link.springer.com/book/10.1007/978-1-4612-9839-7
- MIT OpenCourseWare, *Applied Category Theory*, https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/pages/lecture-videos-and-readings/
