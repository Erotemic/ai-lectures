# 018000 — Categorical Semantics: Types, Programs, and Universal Laws

**Track:** An Introduction to Category Theory. **Background:** products, functors, exponentials, typed functions, lambda notation explained in narration. **Theme:** the semantics of simply typed functional programs in cartesian closed categories.

<!-- BEGIN SPOKEN LECTURE -->

# Categorical Semantics: Types, Programs, and Universal Laws

Suppose you write a small program that takes a pair of Boolean values and returns their conjunction. You can write it as a function of two arguments, or you can write a function that takes the first Boolean and returns a new function waiting for the second. A programmer would say that one representation is curried. A mathematician might say that the two descriptions are related by a natural correspondence between certain function sets.

Category theory reveals that this relationship is one instance of a universal property. In a suitable category, maps out of a product can be converted into maps into an object of functions, and back again, with precise equations. From that correspondence we can give semantics to a language of typed programs. We can explain what variables, pairs, function abstraction, and function application mean using categorical arrows rather than relying on one particular machine or programming language.

This is called categorical semantics. The main question isn't whether programs are literally arrows drawn on paper. It is how the rules of a typed language can be interpreted in mathematical structures, and which program equations follow from the structure. We'll build the interpretation from a two-Boolean calculation and then make the general rules explicit.

## A Boolean program with two forms

Let A and B both be the set containing false and true. Define a function h on pairs by saying h of a and b is true exactly when both a and b are true. There are four possible input pairs. False with false gives false. False with true gives false. True with false gives false. True with true gives true.

Now convert that function into a different shape. For each value a, define a function h of a that is still waiting for b. If a is false, the resulting function always returns false. If a is true, the resulting function returns b unchanged. The original two-input function and the new function-producing function contain exactly the same information.

The set of all functions from B into the two-element result set is itself a set. It contains four functions, corresponding to the four possible truth tables on one Boolean argument. Our curried h is a function from A into this function set. Applying the curried h to a produces one of those four functions; applying that function to b recovers h of a and b.

We can also reverse the process. Given any function from A to the set of functions from B to the result set, evaluate it on a and then b. That recovers a function on pairs. The conversions are inverse and work naturally with the functions involved. This is the mathematical substance of currying.

## Products already explain variable contexts

In a simply typed programming language, a typing judgment says that a term has a specified type, given assumptions about the types of its available variables. For example, given a variable a of type Boolean and b of type Boolean, the expression 'a and b' has type Boolean.

We can interpret the entire list of variable assumptions as a product object. Two Boolean variables correspond to the product of the Boolean object with itself. A term in that context corresponds to an arrow from the product into the result type. In ordinary sets, that arrow is simply a function on pairs. In a more abstract category, the objects need not literally be sets, but the product's universal property still supplies projections.

The first variable is interpreted by the first projection from the context product. The second variable is interpreted by the second projection. Pairing two terms is interpreted by the universal arrow into a product. These choices are forced by the types and the product equations. We are not inventing a separate semantic operation for each variable name.

This is already a useful check on implementation. If a compiler's intermediate language represents a context as a product of inputs, renaming a bound variable should not alter the mathematical map being represented. The identity of a local spelling has no effect on the projection it denotes, once the context positions and binding structure have been fixed.

## Why exponentials are the right function objects

A category with finite products does not automatically contain an object representing all maps from B into C. To interpret function types, we need more structure. An exponential object, usually read 'C to the B,' is an object that behaves like a space of functions from B to C. It comes with an evaluation arrow from that exponential paired with B into C.

The defining property is the currying correspondence: arrows from A times B to C correspond naturally and bijectively to arrows from A into the exponential. In Set the exponential literally is a set of functions. In another category, it may have a different representation, but the universal correspondence is still the definition.

A category with finite products and exponentials for all pairs is called cartesian closed. The category Set is cartesian closed. A suitable category of domains or sheaves can be cartesian closed as well, though its internal meaning of function can differ from ordinary set-based functions.

It is important to distinguish a function type from one particular function. The exponential object represents *all* arrows of the appropriate shape in a controlled way. A curried program is a particular arrow into that object. Evaluation then applies the represented function to an argument. The universal property explains both operations and their agreement.

## Lambda abstraction is currying

In a simply typed lambda calculus, writing 'lambda b, expression' means a function that accepts b and evaluates the expression. Suppose we have a term t of result type C in a context with variables from A and an additional variable b of type B. Its semantic arrow goes from A times B into C.

Lambda abstraction over b converts this arrow into one from A into the exponential C to the B. That is exactly currying. The variable b disappears from the external list of inputs because it has become the argument accepted by the produced function. The remaining context A supplies whatever other information the function body needs.

Application goes the other direction. If a term produces a function from B to C, and another term produces a B argument, their application is interpreted by pairing those two results and passing the pair through evaluation. The categorical formula ensures that application has the right input and output types.

We can recover the original conjunction example immediately. The expression 'lambda b, a and b', in the context containing a, denotes a function from the first Boolean input to the object of functions on the second. Applying it to b recovers the original conjunction on the pair. That recovery will be one of the key equations of the language.

## Beta reduction as a mathematical equation

A familiar evaluation step in programming is to apply a lambda expression to an argument: the argument is substituted for the bound variable in the function body. In lambda calculus this is called beta reduction. The program '(lambda b, t) applied to u' reduces to the body t with u substituted for b.

In category theory, the corresponding law says that evaluating a curried arrow with its argument gives the original uncurried arrow. This follows directly from the exponential's universal property. It is one of the triangle-shaped equations associated with the currying bijection.

Return to the Boolean program. Fix a to false. The curried function associated with false is constant false. Applying it to either Boolean b gives false, exactly as direct evaluation of conjunction would. Fix a to true. The curried function acts as the identity on b. Again, application agrees with the original two-variable program for both possible arguments.

The calculation may sound elementary, but the categorical result is much stronger. It applies to every arrow in every cartesian closed category, not only Boolean conjunction in Set. The typed program equation is sound because the semantic structure enforces it.

## Eta as the other direction

There is a second principle, often called eta. If we already have a function, we can form a new function that takes an argument and immediately applies the original function to that argument. Eta says that this round trip gives us the same function, provided the usual typing and binding conditions hold.

In our Boolean example, take a function g from Boolean to Boolean. Consider the function 'lambda b, g applied to b.' For each input b it produces exactly what g would produce. In Set these two functions agree pointwise. The exponential's universal property gives the categorical equation in any cartesian closed category.

Beta and eta together say that currying and uncurrying are mutual inverses. This is stronger than a mere implementation optimization. It tells us how to recognize certain typed program expressions as denoting the same mathematical map. Different syntactic trees can express the same operation.

However, the meaning of 'same' must be stated carefully. Beta-eta equality is an equational theory of the simply typed lambda calculus. A particular semantic model might identify additional terms that the basic theory does not prove equal. To recover exactly the syntactic equivalences, we use an appropriate free or syntactic cartesian closed category and a corresponding completeness argument. We must not assume any chosen Set interpretation distinguishes every inequivalent program.

## Pairing and projections are just as important

A typed language with pair types has its own equations. If we form a pair from terms t and u, projecting the first component returns t and projecting the second returns u. Conversely, given a term p of product type, pairing its first and second projections recovers p. These are the product analogues of beta and eta.

The equations follow from the universal property of a product. An arrow into A times B is determined uniquely by its compositions with the two projections. If two candidates have the same first and second projections, they are the same arrow. This is what gives product types their characteristic reasoning principles.

The relationship with proof theory is close. A conjunction of propositions behaves like a product of evidence: to establish A and B, supply evidence for A and evidence for B; from a proof of A and B, recover either component. But the Curry–Howard correspondence between propositions and types requires decisions about the logical system. The categorical interpretation we are discussing is specifically suited to the simply typed, intuitionistic setting with products and function types.

It does not mean that all philosophical claims about proof and computation can be read off from a product diagram. The structure tells us exactly which introduction and elimination rules are valid and how their equations interact.

## Interpreting a whole typed language

Let's assemble the pieces. Choose a cartesian closed category and an object interpreting each primitive type. Interpret the unit type by a terminal object. Interpret product types by categorical products. Interpret function types by exponentials. A context of variables becomes a product of the objects interpreting their types.

Every correctly typed term then receives an arrow from the context object to its result-type object. Variables become projections; the unit term becomes the unique arrow to the terminal object; pairing becomes a product arrow; lambda abstraction becomes currying; and application becomes evaluation composed with pairing.

The fundamental requirement is that substitution of terms corresponds to composition of the appropriate categorical arrows. This is why categories are a good semantic language for programs. Program substitution has an associative structure, and identity substitutions do nothing. Those are precisely the kinds of laws captured by categorical composition and identity.

A soundness theorem can then be proved by induction on typing and equality derivations: whenever the syntactic rules assert two well-typed terms equal, their semantic arrows are equal in every model of the specified kind. Each syntactic equation is justified by one of the categorical laws we've already examined.

## A small soundness proof in words

Suppose t depends on a context A and a variable b of type B. Its interpretation is an arrow from A times B to C. The abstraction over b is its curry, an arrow from A into C to the B. If we then immediately apply that abstraction to the b supplied as the second component of the context, evaluation composed with curry recovers the original arrow.

That is the categorical interpretation of a beta step. The proof does not inspect the code inside t. It uses only the universal defining equation of the exponential. Therefore the proof applies uniformly to every possible body t, including bodies built from nested products, function calls, and earlier abstractions.

This is a major benefit of semantics based on universal properties. We prove a general law once and use it everywhere. A compiler transformation preserving beta-equivalent terms can be justified independently of the superficial spelling of their source programs. Of course, real-world languages contain effects, partiality, and evaluation-order issues that may change the applicable equations. The clean theorem belongs to the specified pure typed calculus.

## Where the simple model stops

The simply typed lambda calculus in its basic pure form is strongly normalizing: its well-typed terms reduce to normal forms rather than running forever. A cartesian closed category by itself does not provide an arbitrary fixed-point operator that would model general recursion. If a language includes nontermination, mutable state, exceptions, nondeterministic choice, or input and output, we need additional semantic structure and may need to distinguish different notions of program equivalence.

Monads provide one way to organize certain computational effects. Domain theory supplies models for recursive and partial computation. Linear and symmetric monoidal categories can model resource-sensitive type systems where copying or discarding inputs is controlled. Dependent type theories generally require richer categorical structures, such as locally cartesian closed categories or categories with families, with their own coherence issues.

None of those extensions is automatic from the fact that we can draw a diagram. The basic cartesian closed story establishes a foundation. It tells us how pure function types, pairing, and substitution can be interpreted. Each additional feature demands new axioms and new proofs of soundness.

This matters for formal methods. A proof assistant such as Lean has dependent types and elaborate rules for definitional equality and computation. A simple cartesian closed category is an illuminating starting model, but it is not a complete account of Lean's kernel. To understand a particular type theory, we must match its exact syntax, inference rules, universes, and computational behavior to an appropriate semantics.

## The historical bridge from logic to categories

The lambda calculus grew out of foundational work by Alonzo Church and others on functions and formal systems. The Curry–Howard correspondence connects constructive proofs with typed programs, while categorical work associated with Joachim Lambek and subsequent researchers clarified how these systems can be understood through cartesian closed structure.

This development did not mean that earlier mathematicians had been unconsciously writing categorical programs all along. It supplied a new mathematical translation between several already active subjects: logic, computation, and abstract structure. Each translation could expose the same equation from a different viewpoint.

The conjunction example illustrates why the connection is substantive. In programming, currying transforms how arguments are supplied. In logic, implication corresponds to an operation on proofs. In category theory, an exponential object is characterized by the bijection between maps out of products and maps into function objects. The relationships are established by precise rules and proofs, not by verbal resemblance.

## The difference between equations and evaluation strategy

It is tempting to read beta reduction as a command about exactly how a computer must execute a program. The categorical law is more abstract. It tells us that two well-typed expressions denote the same arrow under the chosen pure semantics. It does not prescribe machine instructions, memory layout, or the number of evaluation steps.

In a pure strongly normalizing calculus, different reduction sequences may lead to the same normal form. That supports equational reasoning. But if a practical language evaluates arguments eagerly, uses exceptions, or performs input and output, replacing one expression by another may change when an effect occurs. Even when the result type looks identical, the operational behavior may not be. A correct semantic model has to say what observations count as equal.

For example, imagine an expression that computes a number while also printing a message. Duplicating the expression inside a pair might print the message twice. In a mathematical function model that records only the final number, those two programs can appear identical. In an effect-aware semantics, the difference can be visible. This is one reason to distinguish denotational equivalence in a stated model from contextual equivalence in a programming language.

The lesson for formal verification is to specify the language and the observations before appealing to a categorical equation. Universal properties give powerful reusable theorems, but the theorem's assumptions are part of what makes it true.


## How to use the semantic viewpoint

When confronted with a proposed program rewrite, begin with a typing judgment. What is the context, and what is the result type? Translate the context into a product of input objects. Translate the term into an arrow. If the rewrite involves pairing, check the product equations. If it involves abstraction or application, check the exponential equations. If it involves substitution, check that categorical composition gives the same map.

If the rewrite involves state or exceptions, stop before applying equations from the pure calculus without qualifications. An expression that appears to be a harmless rearrangement can duplicate an effect or change evaluation order in a language where those effects are observable. The categorical framework can still be useful, but only after the semantic structure includes those operations.

This approach provides a disciplined relation between abstract mathematics and software engineering. The types identify the legal connections. The universal properties supply the equations. A soundness proof explains which transformations preserve denotation. Implementation work still has to address runtime cost, representation, and correctness of concrete compilation steps.

## Closing the circuit

We began with the ordinary Boolean function that returns true only when two arguments are true. We rewrote it as a function taking one Boolean and returning a function of the other. That reversible change of viewpoint is the exponential universal property in Set.

From it we obtained the semantics of lambda abstraction and application. Products explained contexts, variables, and pairing. Beta and eta expressed the round trips between representations. Category theory then gave a systematic way to interpret an entire pure simply typed language and to justify its basic program equalities.

The result is a clear boundary between a mathematical specification and a particular piece of executable code. Typed syntax describes legal expressions; categorical semantics assigns them meaning; and universal laws explain when different expressions denote the same operation. It is a foundation for thinking about verified programs, logical proofs, and later categorical models of computation, provided we keep the assumptions of each interpretation explicit.


<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

A **cartesian closed category** \(\mathcal C\) has finite products and exponentials. The exponential \(C^B\) is equipped with evaluation \(\mathrm{ev}:C^B\times B\to C\) and a natural bijection
\[
\mathcal C(A\times B,C)\cong\mathcal C(A,C^B).
\]
For \(f:A\times B\to C\), denote the transpose by \(\Lambda f:A\to C^B\). The defining equations are
\[
\mathrm{ev}\circ(\Lambda f\times \mathrm{id}_B)=f,\qquad
\Lambda(\mathrm{ev}\circ(g\times\mathrm{id}_B))=g.
\]
Contexts \(\Gamma=x_1:A_1,\ldots,x_n:A_n\) are interpreted as \(\prod_i\llbracket A_i\rrbracket\). A term \(\Gamma\vdash t:B\) is an arrow \(\llbracket\Gamma\rrbracket\to\llbracket B\rrbracket\). Product introduction is pairing, elimination is projection, lambda abstraction is transposition, and application uses evaluation. Soundness of beta/eta follows from the displayed equations. The **free** cartesian closed category on primitive types and operations gives a syntactic setting in which equality corresponds to the chosen equational theory; an arbitrary particular model can satisfy extra equalities.

### Exercises with answers

1. **Exercise:** How many functions are in \(2^2\) for a two-element set? **Answer:** Four.
2. **Exercise:** What is the curried form of conjunction? **Answer:** It sends false to the constant-false function and true to the identity function.
3. **Exercise:** Which categorical law interprets applying an abstraction to its argument? **Answer:** \(\mathrm{ev}\circ(\Lambda f\times\mathrm{id})=f\), the beta equation.
4. **Exercise:** Why does a cartesian closed category alone not model arbitrary nontermination? **Answer:** It specifies products and exponentials, but supplies no general fixed-point operator or additional partial-computation structure.

### References

- Steve Awodey, *Introduction to Categorical Logic*, https://awodey.github.io/catlog/
- Stanford Encyclopedia of Philosophy, “Category Theory,” https://plato.stanford.edu/entries/category-theory/
- Stanford Encyclopedia of Philosophy, “The Lambda Calculus,” https://plato.stanford.edu/entries/lambda-calculus/
- H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*.
- Joachim Lambek and Philip Scott, *Introduction to Higher-Order Categorical Logic*.
