# 023000 — Algebraic Theories: What Does It Mean to Interpret a Monad?

**Track:** Introduction to Category Theory. **Background:** functions, elementary monoids, functors, adjunctions, and monads. **Theme:** equational theories, the list monad, and Eilenberg–Moore algebras.

<!-- BEGIN SPOKEN LECTURE -->

# Algebraic Theories: What Does It Mean to Interpret a Monad?

Suppose a program receives a list of prices: three, five, and two. We can add them to obtain ten. We can instead multiply them to obtain thirty. We can keep only the largest, obtaining five. Or we can combine them into a formatted sentence. The list is the same. What changes is the rule for interpreting it.

There is a mathematical question hidden inside this ordinary choice. Which rules can interpret a list of inputs consistently when lists are nested, concatenated, or empty? A rule that produces a result from every list is not automatically consistent. It might give one answer when we process a list in one pass and a different answer when we process pieces separately. The difference is visible to a program, and category theory gives it an exact description.

A monad captures a pattern of forming structured expressions. An algebra for that monad captures a coherent way to interpret those expressions as ordinary values. In this lecture we will begin with lists, derive the algebra laws, discover monoids inside them, and then ask how much of familiar algebra can be described in this way. The path leads to equational theories, free constructions, and the Eilenberg–Moore category.

## Lists before algebraic language

Let A be a set of values. A list of elements of A might be empty, contain one element, or contain a sequence of any finite length. Write L of A for the set of all those lists. If A contains the numbers three and five, then the empty list, the one-element list containing three, and the two-element list containing three then five all belong to L of A.

A list can be nested. A list whose elements are themselves lists might consist of a two-element list followed by a one-element list. There is a natural flattening operation: concatenate the inner lists in order. The outer boundaries disappear, leaving one ordinary list. There is also a natural operation that places a single value into a singleton list.

These operations satisfy laws we already trust. If we wrap a list in one additional pair of list brackets and flatten, we get the original list. If we replace every individual entry by its singleton list and flatten those singletons, we again get the original. Finally, if a list contains lists of lists, the order in which we remove the two layers of nesting does not affect the result. We can flatten the deepest parts first or the outer parts first, as long as we preserve the order of entries.

This is the list monad. Its functor sends a function from A to B to the function that applies it to every list element. Its unit constructs a singleton. Its multiplication flattens a list of lists. The unit and associativity laws are the facts we just checked. We have produced a mathematical description of generating finite words over an alphabet of values.

## An interpreter for lists

Now choose a function a that takes any list of elements of A and produces one element of A. For addition on whole numbers, a can return the sum of the entries, with zero as the value for the empty list. For multiplication, it can return the product, with one for the empty list. We ask whether such a function treats the list structure consistently.

First, a one-element list containing x should be interpreted as x. Otherwise interpreting even a single value changes it. Second, consider a list of lists. We can flatten it and interpret the result, or interpret each inner list first and then interpret the outer list of those results. A coherent interpreter must give the same answer either way.

Take the nested list consisting of three and five in the first inner list, and two in the second. Under addition, flattening produces the list three, five, two, whose sum is ten. Interpreting the inner lists produces eight and two; interpreting their list again also gives ten. Under multiplication the two paths both give thirty. So both operations respect the nesting.

A function from lists to values can fail the law. Suppose it returns the first element if a list is nonempty, but returns a distinguished default element when a list is empty. For a nested list whose first inner list is empty and whose second inner list contains a value, flattening chooses that later value. Interpreting the inner lists first creates a first value equal to the default, and the outer interpretation chooses the default instead. Unless the two happen to agree, the answers differ. This is a concrete failure of the nesting law.

An interpreter satisfying both laws is called an algebra for the list monad. The term algebra here does not mean a pile of formulas. It means an object equipped with a structure map obeying equations that make an interpretation coherent.

## Recovering the binary operation

We can reverse the construction. Suppose we already have a coherent interpreter a for lists in A. What ordinary algebraic structure is hiding inside it?

Define a binary operation on A by taking a list with two entries, x and y, and interpreting it. Define an element e by interpreting the empty list. We claim the operation is associative and e acts as an identity.

To understand associativity, take the three-element list x, y, z. There are two natural ways to group it: the first two values together, followed by z; or x followed by the last two values grouped together. Make those groupings into nested lists. The nesting law says interpreting each group and then the list of results agrees with interpreting the flattened list. Thus both parenthesizations produce the interpretation of the same three-element list. They are equal.

For identity, compare the one-element list containing x with the nested list consisting of the empty list followed by the singleton list containing x. The flattened list contains just x. The other method first interprets the empty list as e, the singleton as x, and then combines e and x. The nesting law says this must equal x. Reversing the order of the inner lists shows that x combined with e is also x.

That is precisely a monoid: a set with an associative binary operation and a two-sided identity. Conversely, any monoid interprets lists by folding its operation from left to right, using the identity for the empty list. Associativity guarantees that a nested grouping changes nothing. We have derived a two-way correspondence between list-monad algebras and monoids.

The important point is what this correspondence does not require. Addition is one monoid operation, multiplication another, and concatenating strings another. The monad describes finite sequences before choosing an interpretation. A particular algebra supplies the interpretation. The laws ensure compatibility with the way the sequences were built.

## Maps that preserve interpretation

Suppose A is a monoid of strings under concatenation, and B is the monoid of natural numbers under addition. Define f from A to B by sending a string to its length. If we interpret a list of strings by concatenating, then measure its length, the result equals the sum of the lengths of the original strings. Doing the measuring before interpreting the list therefore gives the same answer.

The function f respects interpretation. In elementary algebra, we call it a monoid homomorphism: it sends the identity string to zero and sends concatenation to addition. For a general monad algebra, the preservation equation says that mapping a result after interpretation equals interpreting after mapping every input. The familiar homomorphism law emerges from the categorical one.

This suggests a category. Its objects are pairs consisting of a set and an algebra map from lists over the set back to the set. Its arrows are the functions preserving that algebra map. Identities preserve the interpretation, and a composite of two preserving functions preserves it too. The category is, in this example, the category of monoids and monoid homomorphisms.

For a general monad T on a category C, the same construction produces the Eilenberg–Moore category of T. An object of this category is an object A of C together with a map from T of A to A satisfying unit and multiplication laws. A morphism preserves those maps. The name is historical, referring to the categorical development of algebraic structures by Samuel Eilenberg and John Moore. The definition matters because it turns a programming pattern into a mathematical kind of structure.

## Free structures are also algebras

There is a particularly important algebra hiding in the list construction itself. Start with a set X, form all finite lists of its elements, and use flattening as an interpreter for lists of lists. This makes L of X an algebra for the list monad. It is the free monoid generated by X.

Why free? Suppose a function sends each generator x in X to an element of some monoid A. There is exactly one monoid homomorphism from the free monoid on X to A extending that function. On a list of generators, it must combine their images in order. It has no choice about the empty list, because identities must be preserved. It has no choice about concatenation, because the homomorphism law fixes what happens to each combined list. Existence is given by the fold; uniqueness follows by induction on list length.

This universal property is the source of the free-forgetful adjunction. The free functor turns a set into its free monoid. The forgetful functor sends a monoid back to its underlying set. The correspondence between functions on generators and structure-preserving maps of free monoids is an adjunction. The induced monad on sets is precisely the list monad we started with.

This gives three descriptions of the same phenomenon: an adjunction, a monad, and a category of algebras. They answer different questions. The adjunction explains the extension of assignments from generators. The monad describes syntax, singleton introduction, and flattening. The algebra describes what it means to interpret the syntax without depending on arbitrary grouping.

## Equations define kinds of algebra

The list example has one binary operation and an identity. But many structures involve different operations and equations. Groups have multiplication, identity, and inverse. Rings have addition and multiplication with distributivity. Boolean algebras have operations obeying still other equations.

An algebraic theory gives a uniform language for finitely many inputs, operations, and the equations among them. Think of a formal expression in two variables, such as multiplying the first variable by the second and then multiplying by a third. Another expression changes the parentheses. In a monoid theory, an equation declares that these two expressions have the same value under every permitted interpretation.

The categorical presentation uses a category with finite products, where distinguished objects represent finite lists of input variables. A model of the theory in sets is a functor that preserves finite products. The product preservation forces an expression in n variables to act as a function on n-tuples of actual values. Composition of arrows corresponds to substitution of expressions into expressions. Equations built into the theory become identities satisfied by every model.

This is a striking compression of universal algebra. Rather than separately define a group, a ring, and a monoid by a signature and a list of laws, we can describe each as a product-preserving interpretation of a small category of operations. The category records which formal operations can be composed and which expressions are identified by laws. The model turns that syntax into actual functions.

For ordinary single-sorted finitary algebraic theories on sets, Lawvere theories correspond to finitary monads on sets. The qualification matters: a finitary monad preserves filtered colimits, so its operations depend on finite input data in the appropriate categorical sense. Not every monad on sets is finitary. The full powerset monad, for example, represents arbitrarily large subsets and cannot be treated as a purely finitary theory without changing what is meant.

## Different monads, different algebraic structures

Consider the finite powerset construction on a set A. Instead of remembering a list with order and repetition, we remember a finite set of entries. Its unit forms a singleton, and its multiplication takes the union of a finite family of finite subsets.

A coherent interpretation of finite subsets into values induces a join operation. Because a set forgets order, the join is commutative. Because repeated elements are not duplicated in a set, join is idempotent. Because union is associative, join is associative. And because the empty finite subset exists, the algebra has a bottom element. The algebras are join-semilattices with bottom, and homomorphisms preserve finite joins including the empty one.

The ordinary list monad allows us to remember both order and repetition, producing general monoids. The finite powerset monad forgets order and repetition, producing an operation where those distinctions cannot influence the result. Here is one way to see what a monad is doing: it chooses which formal distinctions count as structure before an algebra gives those formal arrangements values.

A further caution: the full powerset monad has algebras with joins for arbitrary subsets, not just finite joins. Replacing finite powersets with all subsets changes the mathematical theory. The distinction is not cosmetic. A structure that combines every finite set of inputs need not be able to combine an arbitrary infinite set of inputs.

## The two categories associated with a monad

The Eilenberg–Moore category is one major way to read a monad. There is another, the Kleisli category. For the list monad, a Kleisli arrow from X to Y assigns to each x in X a list of Y-values. These arrows compose by applying the second map to each item and concatenating the resulting lists. This is how computations producing multiple results compose.

An Eilenberg–Moore algebra does something different. It takes structured results already present and interprets them as one value in a consistent manner. Kleisli arrows describe generating structured outputs; Eilenberg–Moore objects describe resolving structured inputs. One construction is convenient for programs that produce effects. The other is convenient for objects that know how to process those effects.

Both are related to adjunctions that induce the monad, but their universal properties point in different directions. In the Eilenberg–Moore case, we organize all algebras and their homomorphisms. In the Kleisli case, we freely introduce arrows with structured outputs. Neither category should be confused with the base category of sets on which the monad acts.

## An interpretation that almost works

Before leaving the subject, return to the first-element interpreter. It appears harmless because it works on nonempty lists. If the list is guaranteed to contain at least one element, choosing the first entry behaves well under concatenation of nonempty lists. There is even a monad of nonempty lists, whose multiplication flattens nonempty lists of nonempty lists. Its algebras need not have an identity element because there is no empty list to interpret.

The failure of the earlier first-element rule was therefore diagnostic. We were asking it to interpret an empty expression, and our arbitrary default did not respect how empty expressions interact with nesting. Changing the monad to nonempty lists changes the algebraic obligations. Under that change, the first-element operation is coherent, producing a left-zero semigroup operation in which combining x and y returns x.

This illustrates a general method for examining an abstraction. When an example fails an algebra law, identify the exact formal distinction that caused the failure. We may need to change the interpreter, change the operations allowed by the monad, or accept that the proposed structure simply does not fit the theory. Category theory makes those alternatives visible.

## Substitution of operations is the underlying composition

To see what a Lawvere theory is recording, imagine formal operations that use three named input variables, x, y, and z. One operation multiplies x and y. A second takes that result and multiplies it by z. We can describe this as substituting the expression x times y into the first input of a two-input multiplication operation. That substitution is a composite of arrows in the category of formal operations.

Now compare the expression multiplying x by the product of y and z. The associativity axiom of monoids identifies the two resulting formal arrows. A model sends both arrows to the same three-input function on its underlying set. The equation is thus preserved through every model, because it has already been encoded in the category being interpreted.

Projection operations also matter. A term may ignore its second input and return its first. Another may use the same input twice. The finite-product structure allows variables to be discarded, duplicated, and rearranged. This distinguishes ordinary algebraic theories from settings that treat resources as linear, where duplicating or discarding inputs requires different structure. Even elementary algebra contains assumptions about the allowed use of inputs.

The correspondence with finitary monads becomes more intelligible from this view. The monad builds terms from generators and handles the substitution of terms into terms. Its multiplication is substitution of one layer of terms into another, just as flattening a list substitutes the entries of inner lists into an outer one. The monad algebra evaluates a term in a model. Its multiplication law guarantees that evaluating a substituted expression agrees with evaluating its pieces before making the substitution.

Notice the qualification about free syntax. A free monoid retains distinct formal words even if two different words happen to receive the same value in a particular monoid. For example, mapping two generators to the same numerical value makes their interpretations equal without making the original generators identical. A model can identify terms beyond the equations required by the theory. The algebraic theory sets mandatory equations; an individual algebra can satisfy additional ones.

## Why this way of thinking is useful

In a parser, we often construct syntax trees first and interpret them later. In an algebraic data type, a constructor introduces structure before a fold computes a result. In an effectful program, a monad describes how structured computations are assembled before a handler gives them meaning. These are related patterns, though not every programming effect is completely captured by an ordinary set-based algebraic theory.

The mathematical value is the ability to separate the grammar of formation from the laws of interpretation. The grammar says which composite structures exist. The algebra says how to collapse them into results. The homomorphisms say which translations respect that collapse. Universal properties tell us when an interpretation is uniquely determined by what it does to elementary generators.

We began with a list containing three, five, and two. Addition, multiplication, and other folds were possible because we could choose different coherent interpretations of the same generated syntax. The monad did not choose the answer ten or thirty. It specified how lists are formed, nested, and flattened. An algebra supplied the interpretation and proved its independence from grouping. This separation between structure and meaning is one of the central uses of category theory.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Fix the list monad \(L:\mathbf{Set}\to\mathbf{Set}\):

\[
\eta_A(a)=[a],\qquad \mu_A([\ell_1,\ldots,\ell_n])=\ell_1+\cdots+\ell_n.
\]

An Eilenberg–Moore algebra is \((A,a:TA\to A)\) such that

\[
a\circ\eta_A=1_A,\qquad a\circ T(a)=a\circ\mu_A.
\]

For the list monad define \(e=a([])\) and \(x\star y=a([x,y])\). Then
\[
(x\star y)\star z=a([[x,y],[z]])=a([x,y,z])=a([[x],[y,z]])=x\star(y\star z).
\]
The identities follow using \([[],[x]]\) and \([[x],[]]\). Conversely, fold any monoid into an algebra.

A morphism \(f:(A,a)\to(B,b)\) satisfies \(f\circ a=b\circ Tf\).

The free/forgetful adjunction \(F\dashv U:\mathbf{Mon}\to\mathbf{Set}\) induces \(UF=L\), and \(\mathbf{Set}^L\simeq\mathbf{Mon}\). For the finite powerset monad \(P_f\), \(\mathbf{Set}^{P_f}\) is the category of finite-join semilattices with bottom; the full powerset monad gives complete join-semilattices.

A single-sorted Lawvere theory is a small category \(\mathbb{T}\) with distinguished object \(1\), whose objects are its finite powers \(n=1^n\). Models in Set are finite-product-preserving functors \(\mathbb{T}\to\mathbf{Set}\). Up to the usual equivalences of presentations, Lawvere theories and finitary monads on Set correspond.

### Exercises with answers

1. **List fold.** Verify the monad-algebra law for multiplication on \(\mathbb N\), including empty lists. **Answer:** multiplication of products is the product over the flattened list by associativity; the empty product is \(1\); singleton product is its entry.
2. **A failed fold.** Show that returning the first element with a fixed default for an empty list is not generally a list-monad algebra. **Answer:** use the nested list \([[],[x]]\); flattening gives \([x]\), while the staged interpreter selects the default.
3. **Monoid homomorphism.** Show that string length preserves list interpretation. **Answer:** \(|s_1\cdots s_n|=\sum_i|s_i|\), with length of empty string zero.
4. **Finite powersets.** Why is the join idempotent? **Answer:** \(\{x,x\}=\{x\}\), so interpreting either expression gives \(x\vee x=x\).

### References

- S. Eilenberg and J. C. Moore, *Adjoint Functors and Triples* (1965).
- F. William Lawvere, *Functorial Semantics of Algebraic Theories* (1963).
- Ross Tate, *Monad Algebras* (course notes, 2018).
- Tom Leinster, *Basic Category Theory*, on monads and adjunctions.
