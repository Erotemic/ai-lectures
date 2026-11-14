# 003000 - Dependent Functions and Quantifiers: What Does a Witness Contain?

**Track:** Logic, Type Theory, and Constructive Mathematics. **Background:** functions, implication, mathematical quantifiers. **Theme:** dependent products and sums, universals, existentials, specification, and the computational role of witnesses.

<!-- BEGIN SPOKEN LECTURE -->

# Dependent Functions and Quantifiers: What Does a Witness Contain?

Consider two statements about natural numbers. The first says that for every number, there is a larger one. The second says that there is a number larger than every natural number. They use nearly the same words. Both contain "for every" and "there exists." Yet the first is true, while the second is false. The difference is entirely in the order in which the obligations are placed on us.

If I choose a number first and you are allowed to answer afterward, you can always add one. But if you have to select your number first and then defeat every number I might choose, you cannot succeed. The mathematical difference between these statements has the shape of an interaction: who chooses what, and when? Dependent type theory gives that interaction an exact representation. It can encode what information is available when a witness is constructed, and what evidence must accompany the witness.

Our goal is to understand the mathematical content of universal and existential quantification, their corresponding type constructions, and the precise boundary between proving that something exists and supplying data that software can compute with. The subject reaches into formal proof, mathematical specification, verified algorithms, and even the logic of games.

## An ordinary function is uniform in its contract

A conventional function takes an input of some type and returns an output of another type. If it accepts an integer and returns a Boolean, the returned Boolean type does not change when the input changes. Different inputs may produce different values, but the output contract stays the same.

Now consider a function that takes a natural number n and returns a vector containing exactly n elements. For n equal to zero, the output must be empty. For n equal to three, it must contain exactly three entries. The type of the output depends on the input. We are describing a dependent function.

This dependency is mathematical, rather than merely a runtime convention. We can write the contract so that a term claiming to be a vector of length n cannot accidentally contain a different number of entries. To type-check the function, we must verify that for every permitted input n, the result has the corresponding indexed type.

There is a logical interpretation. Suppose P of n is a proposition asserting some property of n. A proof that P holds for every natural number n is like a dependent function. It accepts an arbitrary n and returns evidence specifically for P of that n. The conclusion may change with the input, and the proof must follow it.

For example, the claim that every natural number is less than its successor is proved by an argument that takes n and gives a proof of n less than n plus one. We do not prove a single isolated fact and announce that it works everywhere. We construct a rule that is valid for an arbitrary input. The universal quantifier specifies the scope of that rule.

## The meaning of arbitrary

In a classroom proof, someone may say, "Let n be arbitrary." This is a compact but demanding phrase. It means the argument must not exploit a special feature of one chosen n. You may use properties that hold for every natural number, such as the existence of its successor. You may not assume without justification that n is even, positive, or smaller than ten unless those restrictions were included in the statement.

Dependent function notation makes the discipline explicit. We introduce n as a variable in the context. With only the permitted assumptions about n, we construct a term of the type required at that n. Then we close the variable and obtain one dependent function that works for all n. If the body contains an illicit assumption, the construction fails to type-check.

Universal elimination is equally ordinary. Given evidence that every natural number has the property P, we can supply the particular input seven and obtain evidence of P of seven. A universal proof must be applicable. The demand to be applicable to any eligible input is what distinguishes it from a collection of favorable examples.

There is a caveat about mathematical equality here. If someone proves a universal proposition using a classical axiom, the logical statement remains a universal claim, but the proof term need not be computable as a program returning ordinary runtime data. In Lean, proofs in `Prop` are treated differently from computational values in `Type`. The analogy between proof and function tells us about construction rules; whether we can execute or extract the term requires a second analysis.

## Existence asks us to name something

For existential quantification, begin with a very concrete statement: there exists a natural number greater than ten. One constructive proof is to name eleven and explain why eleven is greater than ten. The witness and the supporting proof come together. We could choose many other witnesses, but one is enough.

An existence claim can be thought of as a package. Inside is a value x, plus evidence that x meets the advertised condition. The type of the evidence depends on x: if x changes, the proposition to be proved changes with it. This is the structure of a dependent pair, often called a sigma type.

For ordinary pairs, both fields have fixed types. A pair of an integer and a Boolean contains an integer and a Boolean regardless of which integer is stored. In a dependent pair, the second field's type may change according to the first field. A pair whose first field is a length n and whose second field is a vector of length n is a useful example. The first component tells us how to interpret and check the second.

The existential quantifier follows the same introduction pattern: provide a witness and a proof of its property. But the resemblance does not erase the distinction between an existential proposition and a data-bearing dependent pair. In Lean, `Exists` lives in `Prop`; sigma types live in computational universes. General-purpose elimination from `Exists` into arbitrary computational data is restricted. Otherwise a classical existence theorem could be abused as though it supplied an executable algorithm to obtain its witness.

That distinction is important for specifications. A theorem that some optimal solution exists may be enough to establish a mathematical fact. A program that must actually return a solution needs a stronger interface, one that identifies the returned value and allows the caller to inspect it. Merely moving from a theorem to code does not create the missing algorithm.

## The order of the quantifiers changes the world

Return to our opening examples. "For every natural n there exists a natural m greater than n" is satisfied by the rule m equals n plus one. Because m is selected after seeing n, it can depend on n. We can write down a witness-producing function: on input n, output n plus one and a proof of the inequality.

"There exists a natural m such that for every n, m exceeds n" is different. We must choose one fixed m before n is revealed. The next person may respond with n equal to m. The required inequality fails. The impossibility is a simple proof by contradiction, but its intuitive force lies in the dependency: m cannot see n.

The same distinction appears in numerical algorithms. "For every input, there exists a good output" says the problem is solvable, perhaps without saying how. "There is one output that works for all inputs" asserts a uniform constant solution. Neither is necessarily what we need. Frequently the software contract is "there exists a function that, for every input, computes a good output." That introduces a new object, the algorithm itself, and demands a single method valid throughout the input space.

Even more subtle are claims about choosing witnesses from a family of nonempty sets. One formulation provides separate existence proofs for each input. Another seeks one function selecting an element from each set. Moving from the first to the second is related to the axiom of choice. Whether that move is valid depends on the ambient logic and on how the existence statements are represented.

If the witnesses are encoded as computational sigma pairs, we can take the first field of each pair and construct a choice function directly. If we have only propositional existence in a system that treats proofs as irrelevant, the same extraction is not automatic. This is a technical distinction with an everyday analogy: a certificate saying that every locked room contains a key is not itself a procedure for finding all the keys.

## From informal prose to a checked contract

Imagine we are implementing a search algorithm on finite graphs. It accepts a graph and two vertices, and claims to return a path if one exists. That statement contains a conditional existence obligation. A precise specification needs to identify what counts as a path, how endpoints are represented, and what the function does when no path exists.

One interface might return an optional path: either a path value or an explicit failure result. Then a theorem can assert that when the algorithm returns a path, its edges are legal and its endpoints match the requested vertices. A separate theorem may assert completeness: if a path exists in the graph, the function will not report failure. The two properties describe different aspects of correctness.

Another interface returns a path together with proof of validity, provided the caller supplies evidence that the requested vertices are connected. Here the precondition is explicit. The function's dependent result carries the valid path. If the caller cannot establish reachability, they cannot call the function through that contract. In practice we may prefer an optional result so the program can handle negative instances gracefully, but the proof obligations remain the same.

Notice how easy it would be to claim too much. A returned sequence of vertices is not necessarily a valid path. A valid path is not necessarily shortest. A shortest path need not be unique. Every extra adjective in the specification requires either a representation that enforces it or a theorem proving it. Dependent types let us express these properties accurately; they do not establish them automatically.

This precision becomes valuable when porting a mathematical algorithm between languages. The original program may compute a value without an explicit theorem about that value. The formalization must decide which properties are essential and which behaviors are accidents of one implementation. The type is a place to write down that choice so it can be inspected and tested.

## A historical road to dependence

The idea of structuring mathematics around explicit constructions has several roots. Constructive mathematicians were interested in what it takes to establish existence, rather than merely denying the alternative. Type theory offered one way to express those commitments with formal rules for building mathematical objects.

Per Martin-Lof's work in the 1970s and 1980s developed intuitionistic type theory as a foundational language in which propositions and mathematical constructions could be related systematically. Later proof assistants adopted differing versions of dependent type theory, with important variations concerning universes, inductive families, computation, and classical reasoning. It would be a mistake to treat all these systems as interchangeable because they share the word "type."

The history is also a reminder that foundations are engineering choices as well as philosophical ones. A type theory powerful enough to express a rich specification may be difficult to decide algorithmically. A simpler theory can make certain computations and checks straightforward while making some mathematics laborious to encode. The design of a proof assistant negotiates between expressiveness, trustworthy checking, automation, and usability.

For a working mathematician, the immediate advantage is that the distinctions between data, evidence, and assumptions become concrete. A universal theorem exposes what is held fixed and what may vary. An existential theorem exposes the location of a witness. A dependent function describes an output whose permitted form genuinely changes with the input.

## Proof by construction and proof by contradiction

Suppose we want to show that some natural number is not less than itself. A direct constructive proof proceeds by using the properties of the strict ordering. Now imagine a different statement: there exists a natural number with a certain complicated property, but we only know that assuming none exists leads to contradiction.

In classical logic, deriving a contradiction from the negation is sufficient to establish the existence claim. That proof may be mathematically correct, yet provide no method for computing the witness. In constructive logic, the inference from double negation to existence is not automatic for arbitrary predicates. This is one reason a type-theoretic course should pay attention to logical principles rather than using the word "constructive" as a synonym for rigorous.

Sometimes a classical existence proof can be transformed into a constructive algorithm after additional work. Perhaps the search space is finite and equality of candidates is decidable. Perhaps a numerical bound limits how long a search may run. Perhaps a proof contains a hidden witness that can be extracted through a more careful representation. These are mathematical results about the particular problem, not general gifts supplied by classical logic.

As an example, if we know there is an even number between ten and fourteen, we can search that tiny finite interval and find twelve. But the successful search depends on the finiteness of the range and on the ability to test evenness. If the domain is an infinite space of arbitrary mathematical objects, neither property follows just because a witness exists.

## Specifications that look similar but mean different things

Suppose an algorithm receives an integer array and returns an index. A weak claim says that if the array is nonempty, there exists an index whose entry is maximal. For a finite nonempty array, this is true. But the specification of a callable algorithm must be more concrete. It should accept the array, return an index within its bounds, and establish that every other entry is no larger than the selected entry. The returned index depends on the array; the proof of maximality depends on both the array and the index.

We might encode the result as a dependent pair: the first component is a valid index, and the second component is evidence that its entry dominates the others. Alternatively, the function could return an ordinary index and we could prove a separate theorem connecting the result with its input. Both designs can be sound, and choosing between them is partly an engineering decision about interfaces and proof reuse.

Now consider the type of an index. If the input array has length n, a valid index belongs to the finite type of numbers smaller than n. That type is empty when n is zero. A function returning a valid index for every possible array must therefore address empty arrays explicitly. It might require a nonemptiness argument or return an optional result. A dependent type can make the missing case impossible to overlook, but it cannot invent an index in an empty array.

The distinction illustrates a broader principle: quantifiers specify control over inputs and outputs. "For every nonempty array there exists a maximal index" is a theorem about mathematical existence. "There is an algorithm that returns such an index for every nonempty array" is a theorem about uniform computation. "This particular program returns such an index" is a correctness theorem about a concrete implementation. These claims are related, but proving the first does not automatically prove the last two.

## Which information survives into execution?

Type theory includes both proofs and ordinary computational data. That division is especially important when we want to extract certified results from a proof assistant. Consider a theorem that some real number is a root of a polynomial. If the theorem uses a classical existence result on an abstract real-number domain, it may contain no effective procedure for approximating that root. A program requiring numerical output needs additional structure: an algorithm, an approximation representation, and a theorem about approximation error.

For a finite set of integer candidates, the situation may be simpler. We can decide a predicate by checking each candidate. If at least one candidate satisfies it, exhaustive search can return one, along with an elementary correctness proof. The finite domain and the decidable predicate are the reasons the witness becomes computable. The existence theorem alone is not the whole story.

One common interface uses a subtype: an ordinary value of type A packaged with proof that it satisfies predicate P. Another uses a dependent sum with richer output data. Yet another returns a value and a separate theorem whose statement mentions that value. We should select the form that makes the intended guarantee easy to consume and the implementation reasonable to maintain. More dependent syntax does not necessarily mean a better API.

A good test is to imagine a caller using the result. Does the caller need to inspect the witness at runtime? Does it need the proof only for verification? Can the caller legitimately assume that the result exists for every input, or must it handle failure? Answering those questions before designing the type prevents an elegant theorem from becoming a misleading software contract.

## Why dependency is more than elaborate syntax

A nondependent function promises the same kind of output for every input. A dependent function can promise a result precisely suited to the input. An ordinary pair packages two independently typed objects. A dependent pair packages an object with information whose type is determined by that object. Universal quantification and constructive existence arise as logical readings of these structures.

This changes what we can ask the checker to verify. Instead of returning a bare matrix and hoping its dimensions are correct, a routine can return a matrix with dimensions tied to the inputs. Instead of returning a supposed root and relying on a comment, it can return a candidate with a proof of its defining equation. Instead of stating that an algorithm works for a handful of test instances, we can state a property quantified over every valid instance.

The cost is that meaningful dependency requires meaningful mathematics. We must decide what the inputs really are, which assumptions apply to them, which witnesses we can construct, and how the outputs are proved valid. The type system will keep the bookkeeping consistent once the arguments exist. It will not replace the need to invent the arguments.

The opening question about two nearly identical quantifier statements gives the enduring lesson. In one, your output may depend on my input. In the other, it may not. Dependent types make such relationships part of the mathematical object being described. Once we can see those dependencies, we can reason about proof, computation, and specification with substantially greater precision.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Products, sums, and quantifiers

For a family `B : A -> Type`, a dependent function has type `(a : A) -> B a` (Pi); a dependent pair has type `Sigma B`. When `P : A -> Prop`, `forall a : A, P a` lives in `Prop`, as does `Exists P`; the computational and proof-irrelevant constructions must be distinguished.

### Quantifier order

```
forall n : Nat, exists m : Nat, n < m     -- true, witness n + 1
exists m : Nat, forall n : Nat, n < m     -- false, take n = m
```

Constructive proof terms do not automatically entail runtime witness extraction from arbitrary `Prop` statements in Lean.

### Lean examples

```lean
example : forall n : Nat, exists m : Nat, n < m := by
  intro n
  exact ⟨n + 1, Nat.lt_succ_self n⟩

example : not (exists m : Nat, forall n : Nat, n < m) := by
  intro h
  rcases h with ⟨m, hm⟩
  exact (Nat.lt_irrefl m) (hm m)
```

### Exercises and answers

1. **Quantifier swap:** Interpret `forall x, exists y, y = x + 1` and `exists y, forall x, y = x + 1`. **Answer:** The first permits a different successor per x; the second demands an impossible constant y over the natural numbers.
2. **Choose a return type:** A search either returns a valid path or reports failure. **Answer:** An option or sum return type, with a soundness theorem for the success case.
3. **Witness versus existence:** Can arbitrary `Exists` evidence in Lean be projected into `Type`? **Answer:** No, general elimination from `Prop` into unrestricted data is restricted.
4. **Dependent pair:** Give an example. **Answer:** `Sigma (fun n : Nat => Fin n)` with the caveat that `Fin 0` is empty and not every index n admits a value.

### References

- Per Martin-Lof, *Intuitionistic Type Theory* (1984).
- *Theorem Proving in Lean 4*, "Quantifiers and Equality": https://lean-lang.org/theorem_proving_in_lean4/Quantifiers-and-Equality/
- Stanford Encyclopedia of Philosophy, "Intuitionistic Type Theory": https://plato.stanford.edu/entries/type-theory-intuitionistic/
- Benjamin C. Pierce, *Types and Programming Languages* (2002), dependent typing background.
