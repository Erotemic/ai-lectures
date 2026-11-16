# Reductions: How One Impossible Decision Problem Reveals Another

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 006000 — Computability and Mathematical Limits  
**Assumed background:** Basic sets, a recognizer versus a decider, and the undecidability of the halting problem (reintroduced here).  
**Companion:** Formal mapping reductions, two constructive reductions, Rice's theorem proof, counterexamples, and source map.

<!-- BEGIN SPOKEN LECTURE -->

You know how to solve one kind of puzzle, and someone hands you a different one. Perhaps you can transform the new puzzle into a form your existing method understands. If every step of that transformation is effective and the answer survives the translation, you have reduced one problem to another.

This is the fundamental idea of a *reduction*. A reduction is more than saying that two problems seem similar. It is a precise construction that transports an answer from one problem to another. That transport can establish that a new problem is easy enough to solve, or that a new problem is at least as hard as an already impossible one.

The direction matters. If problem A reduces to problem B, then a solution to B provides a solution to A. Think of B as the resource you are allowed to call. To prove that B is undecidable, we start with some A already known to be undecidable and reduce A *to* B. If B had a decider, the reduction would give A a decider. That contradicts the known impossibility of deciding A.

Students often reverse that arrow. They show that their new problem can be translated into the halting problem and announce that the new problem must be undecidable. But this does not follow. Every decidable problem can be mapped to some easy subset of a harder problem under suitable conditions. Being solvable by a powerful hypothetical oracle does not make the original task hard. The impossible task must reduce into the task whose impossibility we wish to establish.

Let us state a particularly clean kind of reduction, a *mapping reduction*. Each decision problem is represented as a language, a set of finite strings that count as yes instances. A mapping reduction from A to B is an algorithm that computes a string f of x for every input x, always finishes, and has this exact property: x belongs to A if and only if f of x belongs to B.

Three conditions deserve attention. The transformation must itself be computable. It must work on every admissible input, not merely on examples that are convenient. And it must preserve both answers: yes turns into yes, and no turns into no. A transformation that preserves only positive instances may be useful for another purpose, but it has not established this form of reduction.

We can prove the basic transfer theorem immediately. Suppose A reduces to B using f, and suppose B has a decider. To decide whether x belongs to A, compute f of x, run B's decider on the result, and return that answer. Both stages terminate, and the membership equivalence makes the answer correct. Therefore if A is undecidable and A reduces to B, B must be undecidable too.

A similar transfer works for recognition. If B has a recognizer and A maps to B, compute f of x and run B's recognizer. On members of A it eventually accepts; on nonmembers it never falsely accepts. Therefore A is recognizable. Taking the contrapositive, if A is *not* recognizable and A reduces to B, then B cannot be recognizable. These are different conclusions from the undecidability transfer, and they require us to keep the one-sided and two-sided guarantees separate.

Now we will construct a real reduction instead of treating the arrow as a decorative symbol.

Define the acceptance problem: given a description of a machine M and an input w, does M eventually reach an accepting state on w? Call the corresponding language A-T-M. Define the halting problem: given M and w, does M reach *any* halting state, accepting or rejecting? Call that language Halt-T-M. These questions are not identical. A rejecting machine halts without accepting, and a looping machine does neither.

We know the general halting problem is undecidable. Is the general acceptance problem undecidable too? One way to prove it is to reduce halting to acceptance.

Given an arbitrary machine M and input w, mechanically construct a new machine N. N ignores whatever input it is given. It simulates M on the fixed input w. If the simulated M ever halts, whether by accepting or rejecting, N accepts. If M never halts, N continues the simulation forever and therefore never accepts.

We have constructed a finite description of N from the descriptions of M and w. We do not run M to completion while constructing N; doing so could make the transformation itself loop. Instead we write a program that will perform the simulation *later*, when N is run. This compile-now, simulate-later distinction is what makes the reduction a total effective transformation.

The equivalence is exact. M halts on w if and only if N accepts its designated input. Thus the halting problem maps to the acceptance problem. If acceptance were decidable, halting would be decidable. Since halting is not decidable, acceptance is not decidable either.

We can also construct the reduction in the other direction. Given M and w, create a new machine N that simulates M on w. If M accepts, N halts. If M rejects, N enters a deliberate infinite loop. If M itself continues forever, N keeps simulating it forever. N therefore halts exactly when M *accepts*. So the acceptance problem reduces to the halting problem.

The two problems are equivalent under these computable mapping reductions as decision problems. But this does not mean their yes and no cases have literally the same operational meaning. The reductions deliberately transform rejection behavior to control the correspondence. A proof about one decision problem must still state what has been encoded into the other.

Next consider a semantic property of a program. Ask whether a machine accepts *at least one* input. This is the nonemptiness problem for its accepted language. We might hope that it is easier than predicting a particular execution, because it asks only whether some input works. In fact, it is undecidable.

Given a machine M and an input w, build N as follows. On every input x, N first simulates M on the fixed input w. If M ever accepts w, N accepts x. If M rejects w, N never accepts x; for example, it can enter an endless loop. If M never halts on w, N also never accepts x. So if M accepts w, N accepts every possible input. Otherwise N accepts none.

In other words, the accepted language of N is the entire input universe in the yes case and the empty set in the no case. The transformation from M and w to N is algorithmic; again, it does not wait for M to finish. Therefore the acceptance problem reduces to the nonemptiness problem. Were nonemptiness decidable, acceptance would be decidable, which we already know is impossible.

There is a useful subtlety here. The same construction maps an accepted instance to a *nonempty* language and a rejected instance to an *empty* language. It therefore directly reduces acceptance to nonemptiness, not to emptiness. Of course, if emptiness had a decider we could invert its yes-or-no output to decide nonemptiness. So emptiness is undecidable too. But claiming that the original construction directly maps acceptance to emptiness would get the arrow's membership condition wrong.

Notice what these reductions do not depend on. They do not know whether M accepts w. They must not know. Their job is to build N in a way that *allows the outcome* of M's execution to determine the corresponding property of N. A reduction is a construction with a proof of behavior, not a solver hidden inside a compiler.

This example leads to a sweeping theorem about program semantics. Suppose you are interested in a property determined solely by the language a Turing machine accepts. Perhaps the property is that the language is empty, finite, infinite, regular, contains a particular string, or contains at least one string. If the property distinguishes between at least two languages that Turing machines can recognize, then there is no algorithm that decides, for every machine, whether its accepted language has that property.

This is the familiar language-property formulation of *Rice's theorem*, named for H. Gordon Rice, whose nineteen fifty-three paper studied decision problems for classes of recursively enumerable sets. It is a powerful result, but it has a carefully defined scope. Let us prove a version rather than leave it as a black box.

Call the property P. It applies to recognized languages, not to the syntax of one implementation. Assume P is *nontrivial*: among the languages recognized by Turing machines, there is at least one language with P and at least one without P. Our goal is to show that the set of machine descriptions whose accepted languages have P is undecidable.

First suppose the empty language does not have P. Since P is nontrivial, some machine T recognizes a language that does have P. Fix that machine T once and for all.

Now take any instance M and w of the acceptance problem. Construct N so that, on an input x, it simulates M on w. If M accepts w, N proceeds to simulate T on x, accepting exactly when T accepts. If M rejects, N enters a deliberate loop; if M loops, N keeps waiting. Nothing in N accepts until the simulation of M has accepted.

What language does N recognize? If M accepts w, the initial simulation eventually finishes in acceptance, after which N behaves like T on each x. So N recognizes exactly the same language as T, which has P. If M does not accept w, the first stage never opens the path to an accepting state, so N recognizes the empty language, which does not have P.

Therefore M accepts w if and only if the recognized language of N has P. That is a mapping reduction from the acceptance problem to deciding P. Since acceptance is undecidable, P is undecidable.

What if the empty language *does* have P? Then consider the complementary property, 'does not have P.' The complementary property is also nontrivial, and the empty language does not have it. By the argument we just gave, that complementary property is undecidable. If P had a decider, we could swap yes and no to decide its complement. That is impossible. So P is undecidable in this case too.

This completes the proof. The proof's architecture is worth remembering: choose two behaviors distinguished by the property; build a machine whose recognized language switches between them depending on an arbitrary acceptance computation; obtain a contradiction if the property has a universal decider.

It is essential not to overextend the theorem. The condition is that P depends only on the *accepted language*. Whether a source file contains a certain variable name is not a language property. Whether a given machine description has an even number of states is not a language property. Whether a machine halts on every input is a property of its execution behavior, and two machines can recognize exactly the same language while differing on that behavior. Rice's theorem, in the version we just proved, does not directly apply to those questions. Some are decidable by inspecting syntax; others are undecidable by separate arguments.

A short example makes the distinction precise. One machine rejects every input immediately. Another machine loops forever on every input. Both recognize the empty language: neither accepts any string. Yet one halts on every input, while the other halts on none. Any property that distinguishes those two machines cannot be solely a property of their accepted languages.

On the other hand, whether the accepted language is regular *is* a language property. Every finite-state language can be recognized by some Turing machine, and some Turing-recognizable languages are not regular. It is therefore nontrivial, and Rice's theorem tells us there is no decider for regularity of arbitrary Turing-recognized languages. This should not be confused with asking whether a language given *as a deterministic finite automaton* is regular; by that representation's definition, the answer is always yes.

We can now recognize several ways a reduction proof can fail. The transformation might secretly run the original machine to termination and therefore fail to produce an output on some inputs. The yes-to-yes direction may hold while the no-to-no direction fails. The target problem might be restricted to a class that does not contain the constructed machine. Or the proof may use a theorem about accepted languages to conclude something about syntactic text or operational timing without showing that the theorem's hypotheses apply.

There is also a broader landscape. For decidability, mapping reductions only need to be computable; they need not be efficient in the sense of polynomial running time. In complexity theory, when we later study NP-completeness, the reduction itself must obey an explicit resource bound, usually polynomial time. A transformation that takes an astronomical or even superpolynomial amount of work may be acceptable for proving undecidability, but it may prove nothing about polynomial-time hardness. The word 'reduction' carries a cost model and a purpose.

This gives us a practical proof checklist. Define the source problem and the target problem exactly. State the known impossibility of the source. Construct an effective total mapping from source instances to target instances. Prove the equivalence for yes and no cases separately. Check that every generated instance belongs to the target's declared input domain. Only then take the contrapositive: a decider for the target would decide the source, so no such target decider exists.

The achievement is not a growing list of unsolvable tasks. It is a reusable method for discovering mathematical structure. The halting theorem gives one obstruction. Mapping reductions carry that obstruction into many other settings. Rice's theorem packages a large family of such constructions into a general principle about semantic questions. Together, they tell us which universal automation goals are impossible, and they encourage us to replace them with sound, restricted, and precisely stated goals that really can be achieved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — reductions with precise domains

Let `Σ*` be finite strings with an effective encoding of pairs and machine descriptions. For languages `A,B ⊆ Σ*`, write `A ≤ₘ B` iff there is a **total computable** `f:Σ*→Σ*` such that for all `x`, `x ∈ A ⇔ f(x) ∈ B`.

1. **Transfer:** `A ≤ₘ B` and `B` decidable ⇒ `A` decidable. If `A` is undecidable, then `B` is undecidable. Likewise, `B` recognizable ⇒ `A` recognizable. In the latter case if `A` is not recognizable, neither is `B`.
2. **HALT → A_TM:** Given `⟨M,w⟩`, construct `N` ignoring its own input `z` and simulating `M(w)`; if the simulation halts in either accepting or rejecting state, `N` accepts. If it diverges, `N` diverges. Then `⟨M,w⟩ ∈ HALT ⇔ ⟨N,ε⟩ ∈ A_TM`.
3. **A_TM → HALT:** Construct `N` that simulates `M(w)`. On simulated acceptance it halts. On simulated rejection it loops. A divergent simulation stays divergent. Then `⟨M,w⟩ ∈ A_TM ⇔ ⟨N,ε⟩ ∈ HALT`.
4. **A_TM → NONEMPTY_TM:** Define `NONEMPTY_TM = {⟨N⟩ : L(N) ≠ ∅}`. Given `⟨M,w⟩`, construct `N(x)` to simulate `M(w)`, and after acceptance to accept `x`; after rejection to loop, and on divergence to diverge. Hence `L(N)=Σ*` if `M` accepts `w`, and `L(N)=∅` otherwise. This is a mapping reduction to **nonemptiness**. It is not a mapping reduction to `EMPTY_TM` with the same membership orientation.
5. **Rice's theorem (recognized-language version):** For a predicate `P` on Turing-recognizable languages that is extensional (`L(M)=L(N) ⇒ P(L(M))=P(L(N))`) and nontrivial (some recognizable language has P and some does not), the index set `{⟨M⟩ : P(L(M))}` is undecidable. Proof given in narration: if `P(∅)` false, reduce `A_TM` using a fixed witness machine `T` with P; if true, apply the argument to `¬P`. Assume a conventional total handling of syntactically invalid encodings.
6. **Nonapplicability example:** `M_reject` (immediately rejects everything) and `M_loop` (never halts) both recognize `∅` but differ on totality. Thus totality is not extensional with respect to accepted languages. It remains undecidable by separate reductions, not by the language version of Rice's theorem alone.

**Witness that regularity is a nontrivial semantic property:** A machine recognizing `Σ*` recognizes a regular language. A machine can also decide `L = {0^n1^n : n≥0}` by checking a block of zeros followed by an equally long block of ones. This language is **not regular**: if it had pumping length `p`, consider `0^p1^p`; every pumping decomposition with `|xy|≤p` and `|y|>0` makes `y` all zeros. Removing `y` makes the counts unequal, contradicting the pumping lemma. Thus Rice applies to regularity of languages presented by *arbitrary Turing machines*, but not to the trivial question of whether a language presented explicitly by a finite automaton is regular.

**Totality needs a separate reduction:** For any `⟨M,w⟩` build `N(x)` which ignores `x`, simulates `M(w)`, and halts if and only if that simulation halts. This transformation is total; `N` halts on *all* inputs iff `M` halts on `w`. Thus `HALT ≤ₘ TOT`, proving undecidability of `TOT` without misapplying Rice's language-property theorem. This is an additional original teaching derivation.

**Ill-formed encodings:** To make every reduction total on *all* finite strings, define a decidable validity check for the source encoding, and map an invalid input to a fixed negative instance of the target. For example, a machine that loops and never accepts supplies a fixed no-instance of acceptance and halting, when paired with an input. This extends each construction from well-formed pairs to a total map on strings without altering the proof on well-formed pairs.

### Practice problems

1. Prove why `A ≤ₘ B` and `B` recognizable imply `A` recognizable. Is the converse guaranteed?
2. In the reduction `A_TM ≤ₘ NONEMPTY_TM`, what is `L(N)` when `M` rejects `w`? When `M` loops on `w`?
3. Show independently that `TOT = {⟨M⟩ : M halts on every input}` is undecidable, by reducing `HALT` to `TOT`. State the construction and both cases. Explain why the accepted-language version of Rice's theorem is not the right citation.
4. Is 'recognizes a finite language' within the scope of Rice's theorem? Is 'contains the byte sequence ABC in source code'? Is 'runs for exactly seven steps on the empty input'?
5. Find the incorrect statement: 'If an undecidable problem B reduces to A, then A is undecidable' versus 'If A reduces to an undecidable problem B, then A is undecidable.' Explain by writing the contrapositive transfer theorem.

## Source-to-claim reading map (non-spoken)

- **H. Gordon Rice (1953),** *Classes of Recursively Enumerable Sets and Their Decision Problems*, *Transactions of the American Mathematical Society* 74(2), 358–366. Original author for the named semantic-property theorem; DOI verifies journal attribution and chronology. [Publisher DOI](https://doi.org/10.1090/S0002-9947-1953-0053041-6). Full original paper was not treated as read text; the proof above is self-contained.
- **Emil Post (1943, 1944):** *Formal Reductions of the General Combinatorial Decision Problem* (1943), and *Recursively Enumerable Sets of Positive Integers and Their Decision Problems* (1944), acknowledged for historical work on reductions and enumerability. [1944 paper DOI](https://doi.org/10.1090/S0002-9904-1944-08111-1). This manuscript does not claim Post introduced the exact modern notation used here.
- **MIT 6.045J Spring 2011,** official lecture notes index, specifically lecture 9, *Mapping reducibility and Rice’s theorem* (courtesy Prof. Nancy Lynch); lecture 7 for decidability. [Open course index](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/). The index was checked; the slide PDF is not claimed to have been read in full.
- **Stanford Encyclopedia of Philosophy, *Turing Machines*,** section 2.4 for the mathematical role of undecidability reductions, and *Computability and Complexity*, section 4.1 for reductions and completeness. [Turing Machines](https://plato.stanford.edu/entries/turing-machine/) and [Computability and Complexity](https://plato.stanford.edu/entries/computability/).
- **Independent construction:** The `HALT`, `A_TM`, nonemptiness, and Rice cases here are original pedagogical derivations of standard results. Soundness depends on the explicit constructions, not on program testing. `examples/finite_reductions_lab.py` checks the direction of the first two constructions on selected tiny finite programs; it is **not** a formal proof for all Turing machines.

See `metadata/006000.json` for exact anchors and provenance.
