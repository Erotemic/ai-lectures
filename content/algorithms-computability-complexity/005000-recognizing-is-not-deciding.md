# Recognizing an Answer Is Not the Same as Deciding It

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 005000 — Computability and Mathematical Limits  
**Assumed background:** Basic program execution, sets of finite strings, and the idea that some programs never halt.  
**Companion:** Recognition/decision definitions, dovetailing proof, enumeration theorem, and evidence map.

<!-- BEGIN SPOKEN LECTURE -->

Imagine two tasks. In the first, someone gives you a finite mathematical proof, and you must check whether each step follows the rules of a specified formal system. In the second, someone gives you a mathematical claim, and you must either find a proof or establish that no proof exists. These tasks sound related, but they ask for very different forms of computation.

Checking a proposed finite proof can often be an algorithmic task. Searching for a proof might also be effective: list candidate strings, check each candidate, and stop if one succeeds. But if the search finds nothing, what does that mean? Maybe there is no proof. Or maybe a proof exists and occurs much later in the search. An algorithm that eventually confirms every positive case need not be able to resolve every negative case.

Computability theory formalizes exactly this distinction. A program that can eventually establish membership in a set is called a *recognizer*. A program that can always establish membership or nonmembership is called a *decider*. The second is more demanding than the first.

To avoid ambiguity, let us begin with a universe of finite strings over a fixed finite alphabet. A *language* is simply a set of such strings; it need not be human language. A machine recognizes a language L when it accepts every string in L, and never accepts a string outside L. On a string outside the language, the recognizer is allowed either to reject and halt, or to continue forever. On a string inside L, it must eventually accept.

A decider for L always halts. It accepts the strings in L and rejects the strings outside L. Every decider is therefore a recognizer. Not every recognizer is a decider.

What makes the definitions slippery is that programmers routinely use the word *reject* to mean several different things. A machine may execute a reject instruction and stop. It may reach an exception state treated as rejection in a particular model. Or an observer may simply decide, after a timeout, that nothing has happened. In the mathematical definition we are using, a genuine rejecting halt is an observable finite event. Silence after an arbitrary number of steps is not an answer about infinite execution.

Take the general halting language. Its members are encodings of a program paired with an input on which that program eventually stops. The natural recognizer is simple. Decode the pair, simulate the program, and accept if the simulation halts. A program that does halt supplies a finite witness: its complete terminating execution. If the program never halts, the recognizer continues to simulate it forever.

Thus the halting language is recognizable. It is not decidable. We know that from the diagonal argument: if a total program always decided whether another program halted, constructing a program that reverses the prediction on its own description would lead to a contradiction.

Let us turn that contrast into an important theorem. A language is decidable if and only if *both it and its complement are recognizable*.

The complement of a language contains precisely the strings in our chosen universe that are not in the language. Suppose first that L has a decider. To recognize L, just run that decider and accept when it accepts. To recognize the complement, run the same decider and exchange its accepting and rejecting outcomes. Since the decider always terminates, both machines recognize what they are supposed to recognize. This proves one direction.

Now suppose we have only two recognizers. Call them R for L and S for the complement of L. We cannot safely run R and wait for it to finish before starting S. If the input is outside L, R may never finish. S could be ready to accept almost immediately, yet our serial procedure would never give it a turn.

Instead we interleave the simulations. Give R one step, then S one step. Give R another step, then S another step, and continue. If R accepts, declare that the input belongs to L. If S accepts, declare that it does not belong to L. If either machine rejects, we can ignore that event in this construction. An explicit rejection is genuine evidence of nonmembership for that recognizer, but the recognizer is not required to reject every nonmember. Our combined proof relies only on the guaranteed acceptance from one side.

Why does this interleaving always finish? Every string is either in L or in its complement. In the first case R must eventually accept, after some finite number of its own simulated steps. In the second case S must eventually accept after some finite number of its steps. Our alternating schedule eventually supplies any requested finite number of steps to both machines. Therefore one of them accepts, and the combined procedure halts with the correct membership decision.

This construction is called *dovetailing*. It replaces a dangerous commitment to one potentially infinite computation with a fair schedule in which each of finitely many active computations receives arbitrarily much time, eventually. For a countable family of computations, the scheduling principle generalizes: at stage one, give the first computation a step; at stage two, give the first two computations another step each; and so on. Every fixed computation eventually receives as many steps as needed for any finite witness it may produce.

The theorem is both useful and sharp. It does not say that two arbitrary recognizers will decide a language. They must recognize complementary sets. If both recognize the same language, running them in parallel gains no magical access to nonmembers. The correctness argument depends on the fact that every input is guaranteed to be a positive case for exactly one of the two recognized languages.

Now return to the halting language. We have a recognizer for halting, but no decider. By the theorem, its complement—the set of program-and-input pairs on which the program never halts—cannot be recognizable. If it had a recognizer, dovetailing the two would give a halting decider, which is impossible.

This is a stronger statement than saying that nontermination is difficult to detect. It says that there cannot even be a universal program guaranteed eventually to *confirm* every genuine nonhalting case without ever mistakenly confirming a halting case, assuming the usual effective model. Individual nontermination certificates remain entirely possible. The impossibility concerns one complete, reliable recognizer for all negative instances.

A language may therefore occupy one of several positions. It may be decidable: both membership and nonmembership can be settled. It may be recognizable but not decidable, like the halting language. It may be co-recognizable but not decidable, like the complement of the halting language. And there are languages that are neither recognizable nor co-recognizable. That last claim can be established by a counting argument: there are only countably many finite program descriptions, hence only countably many recognizable languages and only countably many complements of recognizable languages, but uncountably many subsets of the set of all finite strings.

The names can mislead. *Co-recognizable* does not mean that a single program proves nonmembership for every language. It means the *particular language under discussion* has a recognizable complement. For the complement of the halting language, that complement is the halting language itself, so co-recognizability is straightforward. The property belongs to a set of strings and depends on what counts as the universe of possible strings.

There is another mathematical characterization worth understanding. A language is recognizable exactly when a computational process can *enumerate* its members. In older literature such sets are called *recursively enumerable*. The modern term *computably enumerable* often refers to the same class.

Suppose a machine recognizes L. List all finite strings in a systematic order. We cannot run the recognizer on the first string to completion and then move to the second, because the first computation might never stop. Instead, at each stage, launch another input and give a bounded amount of additional simulation time to every previously launched input. Whenever a simulation accepts, print that input. Every member of L is eventually printed because it appears somewhere in the list and its recognizer eventually accepts. No nonmember is printed because the recognizer never accepts a nonmember. The procedure may print duplicates; that does not change the set of strings it enumerates.

Conversely, suppose we have a program that systematically prints exactly the members of L, eventually printing each member. To recognize whether a proposed string x belongs to L, run the enumerator and watch its outputs. If x appears, accept. If it never appears, keep watching. This is a recognizer: on members it eventually says yes, and on nonmembers it never falsely says yes.

This equivalence makes the concept of recognition concrete. An enumeration is a way to discover positive instances one by one without knowing when the entire search is complete. In the special case of the empty language, an enumerator may print nothing forever, while a recognizer may simply reject every input. No contradiction arises: the range of emitted strings is empty in both descriptions.

Consider again formal proofs. If there is a mechanical checker for finite proofs, one can enumerate strings that pass it. Under a sound and complete proof system for a particular logic, this enumerates all its theorems. But the enumeration by itself does not tell us, after any finite waiting period, that a formula never appears. The relation between proof systems and decidability requires further theorems and depends on the logic being studied. In first-order logic, for example, completeness of a proof system does not make general validity decidable.

Now consider the question, 'Does a given program ever accept at least one input?' We can recognize yes instances. Enumerate all possible inputs and dovetail simulations of the program on each input. If any simulation accepts, the answer is yes. This gives us a general recognizer for nonemptiness of a machine's accepted language. But if the machine accepts no input, the search may run forever. Later we will show that no general decider exists for this property.

The word *exists* often signals why recognizability is possible. If there exists a finite witness that a program accepts, and we can check that witness effectively, we can search for it. But the absence of a witness is not necessarily demonstrated by failing to find one. This is not a complete general criterion for recognizability, and the details of what counts as an effectively checkable witness matter. Still, it is a powerful instinct when designing semidecision procedures.

There is a corresponding distinction in everyday experimental work. A test can demonstrate that a particular program has reached an error state, or that a certain counterexample exists, because one actual execution supplies the evidence. A test suite can never conclude that no counterexample exists in an unbounded input universe merely because none has been observed. That may motivate invariant proofs, type-system guarantees, abstract interpretation, restricted-domain exhaustive checks, or other sound methods. But none of those techniques eliminates the mathematical boundary we just established.

At this point we can make three increasingly demanding promises about a problem. First, we might be able to identify some positive instances; a practical heuristic can do that without covering every positive case. Second, we might have a recognizer that is guaranteed eventually to identify *all* positive instances and never accepts a negative one. Third, we might have a decider that always finishes with the correct yes-or-no result. These are genuinely different promises. Calling them all 'an algorithm that solves the problem' conceals what has been established.

The deepest lesson is the importance of the missing answer. A program's silence is not an ordinary third truth value in the specification of a decision problem. It is a failure to supply a required answer. Recognition permits that failure on negative inputs. Decision does not. Dovetailing shows exactly when two complementary one-sided guarantees can be combined into a complete result—and the halting theorem shows a natural case where the required second guarantee cannot exist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — exact statements

Fix a finite alphabet `Σ`. A deterministic Turing machine `M` *recognizes* `L ⊆ Σ*` iff for every `w`, `M(w)` accepts iff `w ∈ L` (on `w ∉ L` it may reject or diverge). It *decides* `L` iff it recognizes `L` and halts on every `w`. A language is *co-recognizable* iff its complement relative to `Σ*` is recognizable.

**Theorem:** `L` is decidable ⇔ `L` and `Σ* \ L` are recognizable.

**Proof:** The forward direction follows by using a decider for `L` and a decider obtained by flipping accept/reject. For the reverse direction, let `R` and `S` recognize `L` and its complement. On `w`, at stage `t = 1,2,...`, simulate one more step of each, retaining configurations. If `R` accepts, accept; if `S` accepts, reject. Exactly one of the two recognizes a set containing `w`, hence it accepts after finitely many simulated steps. Termination is ensured by fair scheduling, not by either recognizer rejecting on all nonmembers.

**Corollary:** `HALT` is recognizable but undecidable, so `Σ* \ HALT` is not recognizable. Conversely `Σ* \ HALT` is co-recognizable but undecidable. Invalid encodings can be fixed to reject in `HALT` by convention.

**Enumeration theorem:** `L` is recognizable ⇔ some effective enumerator prints exactly elements of `L` and eventually prints each `w ∈ L` (duplicates allowed, no requirement to halt). Dovetailing is necessary in the recognizer-to-enumerator direction. The empty language may be enumerated by printing nothing.

**Counting observation:** There are countably many machine descriptions (finite strings), so at most countably many recognizable and co-recognizable languages; `P(Σ*)` is uncountable when `Σ*` is infinite. Therefore there are languages in neither class. This is an existence result, not a practical method for naming a natural such language.

### Concept checks

1. Suppose a recognizer for L halts and rejects a string. Can that string belong to L? Can another string outside L cause the same recognizer to loop?
2. In the two-recognizer decider, why is running R to completion before launching S incorrect? Give an input demonstrating the failure.
3. Does replacing a missing answer by a timeout change recognizability or decidability? What new bounded property can the timeout decide?
4. If a program enumerates every member of a language twice, and no nonmembers, is it still an enumerator for that language?
5. Which parts of the two-recognizer theorem fail if R and S overlap or leave some input in neither recognized set?

## Source-to-claim reading map (non-spoken)

- **Emil Post, 1944:** *Recursively Enumerable Sets of Positive Integers and Their Decision Problems*, *Bulletin of the AMS* 50(5), 284–316, for historical terminology and original development of r.e. sets. [Publisher DOI](https://doi.org/10.1090/S0002-9904-1944-08111-1). Publisher bibliography was verified; this manuscript does not claim direct inspection of each historical proof.
- **Stanford Encyclopedia of Philosophy, *Computability and Complexity*:** sections 2.3–2.4, for enumerability and the diagonal halting set. [Open entry](https://plato.stanford.edu/entries/computability/).
- **Stanford CS103 course reference:** entries *Recognizable*, *Decider*, *Co-Recognizable*, *Complement*, and discussion of the halting language. [Course reference](https://web.stanford.edu/class/archive/cs/cs103/cs103.1152/reference/). The reference listing is secondary teaching support; the formal theorem's proof above is presented explicitly rather than attributed to a single course.
- **MIT 6.045J course, 2011:** Lecture 7 (decidability), Lecture 8 (undecidability), Lecture 9 (mapping reducibility). [Official lecture index](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/).
- **Original derivations and applications:** Dovetailing constructions, proof-search examples, and the recognizer-to-enumerator proof are mathematical expositions built from stated definitions. Their correctness rests on the displayed proof arguments; citation metadata records the sources informing those arguments.

See `metadata/005000.json` for exact anchors and provenance.
