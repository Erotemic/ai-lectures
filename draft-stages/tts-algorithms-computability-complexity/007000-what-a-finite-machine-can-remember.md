# What a Finite Machine Can Remember

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 007000 — Finite-State Computation  
**Assumed background:** Finite sets, functions, and induction. No prior automata theory.  
**Companion:** Transition tables, proofs, state distinguishability, finite-state decision algorithms, and reading map.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a machine reading a message that might be ten characters long or ten billion. It receives each character in order. It cannot go backward, and it does not store the message. It has only a small collection of internal conditions. Depending on its present condition and the next character, it moves to another condition. At the end, it answers yes or no.

Can this machine recognize a message ending in zero followed by one? Yes. Can it recognize a message containing a multiple of three occurrences of one? Yes. Can it recognize precisely those messages that begin with some number of zeros and end with the same number of ones? The answer is no, and the reason will teach us what a finite amount of memory can and cannot accomplish.

Let us make the model exact. First, an alphabet is a finite set of symbols. We will use the alphabet consisting of zero and one. A word is a finite sequence of symbols from this alphabet. The empty word contains no symbols at all; it is a word, even though there is nothing to read. A language is a set of such words. It may contain no words, finitely many words, or infinitely many words.

A deterministic finite automaton, often abbreviated D-F-A, consists of five pieces. There is a finite set of states. There is the input alphabet. There is a transition function that, for every state and every alphabet symbol, specifies exactly one next state. There is one initial state. And there is a subset of accepting states. The machine starts in the initial state, reads the symbols from left to right, performs one transition per symbol, and accepts precisely when its final state is accepting.

Deterministic means that the machine has no choice about its next state. Finite refers to the number of states, not the possible length of its input. An automaton with three states can inspect an input of arbitrary finite length. But it cannot distinguish more than three internal situations after reading a prefix.

Here is a first example. We wish to accept binary words whose number of ones is divisible by three. There are exactly three distinctions worth remembering: the count so far has remainder zero, one, or two upon division by three. Name the states remainder zero, remainder one, and remainder two. Start in remainder zero. Reading zero leaves the state unchanged. Reading one advances to the next remainder, wrapping from two back to zero. Accept only in remainder zero.

The empty word is accepted, because it contains zero ones, and zero is divisible by three. The word one-one-zero-one is also accepted: it contains three ones. The word one-zero-one is rejected: two ones leave the machine in remainder two. The machine never stores the count itself. If the input contains a million ones, three states still suffice, because only the remainder matters.

Why is this machine correct? Not because a diagram looks right, and not because we tested several words. After reading any prefix, assert that its state is exactly the remainder, modulo three, of the number of ones in that prefix. At the beginning both are zero. A zero changes neither count nor state. A one increases the count by one and advances the state by one modulo three. By induction, the assertion holds for every prefix. The final-state test is therefore equivalent to the original condition. This is a proof about every word, not merely about short examples.

Now consider a different language: all binary words ending in zero-one. Think about the part of the ending that might still grow into the desired pattern. We need three states. In the first state, the currently read prefix has no useful trailing zero and does not end in zero-one. In the second, it ends in zero. In the third, it ends in zero-one. Accept only in the third.

When the machine reads zero, no matter which state it occupied, it moves to the state meaning 'ends in zero.' When it reads one, the 'ends in zero' state becomes 'ends in zero-one.' In either other state, reading one moves to the state with no useful trailing zero. The word zero-one is accepted. The word one-zero-one is accepted. The word zero-one-one is rejected, because the final one destroys the required ending.

Notice that the first description of the initial state needed a little care. A state does not carry a mystical memory of the whole history. Its meaning is a proposition about the prefix. In the first state, the prefix ends neither in zero nor in zero-one. In the second it ends in zero. In the third it ends in zero-one. Those three propositions are disjoint and cover every prefix. Each transition preserves the interpretation. Again, induction supplies the correctness proof.

A language recognized by some finite automaton is called regular. Regular does not mean small, simple to a human, or restricted to finitely many words. Our divisible-by-three language is infinite: add three more ones to any accepted word, and the result is still accepted. Yet the computation needs only three states.

Regularity is a statement about how many distinguishable situations must be remembered, not about how many possible inputs exist. It helps to separate these ideas because an input can be vastly longer than the machine's memory without making recognition impossible.

Suppose we need both conditions at once: a word must end in zero-one, and its number of ones must be divisible by three. We can build a new machine whose state records two things: one state from the first automaton and one from the second. A pair of states changes by advancing both component machines on each input symbol. At the end, we accept only if both components accept. Three states times three states gives at most nine paired states, although some may be unreachable.

This is a product construction. It proves that the intersection of two regular languages is regular. Changing the final test from 'both' to 'at least one' proves that the union of two regular languages is regular. And if a deterministic machine has a transition defined for every state and symbol, swapping accepting states with rejecting states recognizes the complement of its language. That last qualification matters: if transitions are missing, we must first specify where an unhandled symbol leads, usually to a rejecting sink state.

Closure constructions are not just formal decorations. They let us assemble independently verified requirements and reason about their combination. At the same time, their costs matter: a direct product can multiply state counts, even though reachable-state construction or later minimization may keep the practical machine smaller.

Here is a useful decision procedure that is possible for this restricted machine model. Given the entire finite transition table of a D-F-A, can we decide whether it accepts at least one word? Regard states as vertices of a directed graph and transitions as edges. Starting at the initial state, explore every reachable state. If any accepting state is reachable, follow the path labels to obtain an accepted word. If none is reachable, no input can take the automaton into acceptance. The finite search terminates.

We can even decide whether two finite automata recognize exactly the same language, without trying every word. Run their product machine and mark a pair accepting when precisely one component accepts. If that disagreement state is reachable, the path to it is a counterexample word. If no disagreement state is reachable, the machines agree on every word. This procedure is a proof of equivalence using a finite graph, and it can return the shortest counterexample by exploring transitions breadth first.

Contrast that with a general program. Asking whether two arbitrary Turing machines accept exactly the same language is not in general decidable. The finite automaton is less expressive, but precisely because its behavior is summarized by finitely many states, we can answer strong questions about all of its possible inputs. Restricted expressive power sometimes buys us tractable verification.

Where does the limitation appear? Take the language of a block of zeros followed by exactly the same number of ones. The empty word qualifies. Zero-one qualifies. Zero-zero-one-one qualifies. Zero-zero-zero-one-one-one qualifies. Suppose a finite automaton with, say, a hundred states recognizes this language. Look at the hundred and one prefixes consisting of zero zeros, one zero, two zeros, and so on up to a hundred zeros.

Two of those prefixes must leave the automaton in the same state. Call their lengths i and j, with i smaller than j. Now append exactly i ones to both prefixes. Starting from the same state, the machine must make the same transitions on the common suffix, so it must give the same answer for both completed words. But the shorter word, consisting of i zeros and i ones, belongs to the language, while the longer word, j zeros and i ones, does not. We have a contradiction.

This is the pigeonhole principle transformed into a statement about memory. It does not matter whether the automaton has three states, a hundred states, or an astronomically large but fixed number. There are always more distinguishable zero-prefix counts than its finite state set can represent.

Be careful with the conclusion. We have not shown that no computer can recognize equal counts. A computer with an unbounded counter can scan the zeros, increment a count, and then scan the ones while decrementing it. Nor have we shown that finite machines cannot recognize any balanced pattern. They can recognize equal counts within a fixed bound, because that requires only finitely many distinctions. What they cannot recognize is unbounded equality of two counts in this single-pass finite-state model.

The distinction between bounded and unbounded memory is the point of this lecture. A finite automaton makes one transition per input character, so its running time is linear in the number of characters once its transition table is available. Its stored state belongs to a fixed finite set, independent of input length. But a general-purpose implementation might spend time decoding characters or looking up transitions; our statement is about the stated abstract cost model, not a promise about every software library.

Historically, Stephen Kleene studied regular events in finite automata in work published in nineteen fifty-six. Michael Rabin and Dana Scott's nineteen fifty-nine paper developed finite automata and their decision problems, including the role of nondeterminism. The mathematics did not emerge fully formed from one author's notation. It was part of a broader investigation of what abstract machines can describe and decide.

The practical lesson is that a machine's state should represent exactly the information its future decisions need. Too little information makes the specification impossible. Too much may create a cumbersome machine. The next mathematical question is more subtle: when are two pasts genuinely equivalent, because no possible future input can tell them apart? That question leads toward minimal automata and the precise boundary of regular languages.

<!-- END SPOKEN LECTURE -->

## Formal companion: models and invariants

Let `Σ={0,1}`, with `Σ*` including the empty word `ε`. A DFA is `M=(Q,Σ,δ,q₀,F)` with total `δ:Q×Σ→Q`. Extend `δ` to words by `δ*(q,ε)=q` and `δ*(q,wa)=δ(δ*(q,w),a)`. Define `L(M)={w:δ*(q₀,w)∈F}`.

**Divisible-by-three example:** states `r0,r1,r2`, start `r0`, accept `F={r0}`; `δ(ri,0)=ri`, `δ(ri,1)=r(i+1 mod 3)`. Invariant after prefix `w`: current state is `r(#₁(w) mod 3)`.

**Ends-in-01 example:** state `s0` means prefix ends neither in `0` nor in `01`; `s1` means ends in `0`; `s2` means ends in `01`.

| state | on 0 | on 1 | accepting |
|---|---|---|---|
| `s0` | `s1` | `s0` | no |
| `s1` | `s1` | `s2` | no |
| `s2` | `s1` | `s0` | yes |

Proof: the interpretations are mutually exclusive and cover all prefixes. The empty prefix is in `s0`. Each transition matches the effect of appending the indicated symbol. Acceptance is exactly `endswith("01")`.

**Product:** Given complete DFAs `A,B`, form `Q_A×Q_B`, initial `(qA,qB)`, and componentwise transitions. Use `F_A×F_B` for intersection and `{(p,q):p∈F_A or q∈F_B}` for union. Complement a *complete* DFA by replacing `F` with `Q\F`. For equivalence, use accepting pairs with exactly one component accepting; its language is the symmetric difference. A graph search finds a reachable disagreement iff the original languages differ.

**Nonregularity proof (direct):** Suppose a `k`-state DFA recognizes `L={0ⁿ1ⁿ:n≥0}`. Among `0⁰,…,0ᵏ`, choose `i<j` with equal reached states. Because `δ*` from equal states on a common suffix agrees, `0ⁱ1ⁱ` and `0ʲ1ⁱ` receive the same verdict. Exactly one is in `L`, contradiction. This does not invoke the pumping lemma and makes no unproved assertion about loops.

**Complexity qualification:** A transition is one abstract step; processing `n` symbols takes `Θ(n)` transition steps for a fixed DFA. Its machine state requires `⌈log₂|Q|⌉` bits in a direct encoding; this excludes the fixed read-only transition table and representation of the input. DFA emptiness via reachability is `O(|Q|+|δ|)` on an explicit graph, including processing of transition edges.

## Questions and derivations

1. Show that `001001` is accepted by the ends-in-01 machine, but not by the divisible-by-three machine. What is its final product state?
2. Construct the complement of the ends-in-01 machine. Why does the proof depend on transitions being total?
3. Explain why two states representing a different count of ones may still be equivalent for the divisible-by-three language.
4. Prove that if two states have equal behavior on every possible remaining suffix, merging them cannot change the recognized language.
5. Show that `L={0ⁿ1ⁿ:0≤n≤100}` is regular, without constructing all its states explicitly.

## Source-to-claim reading map (non-spoken)

- **Stephen C. Kleene,** “Representation of Events in Nerve Nets and Finite Automata,” in *Automata Studies* (1956), pp. 3–41, esp. introduction and regular-events result. Primary historical source; attribution verified from the bibliographic and opening text available through an institutional mirror. [University-hosted copy](https://www2.fiit.stuba.sk/~kvasnicka/CognitiveScience/2.prednaska/kleene56representation%5B1%5D.pdf).
- **Michael O. Rabin and Dana S. Scott,** “Finite Automata and Their Decision Problems,” *IBM Journal of Research and Development* 3(2) (1959), pp. 114–125. Attribution and scope from publisher record, not full-text audit. [DOI](https://doi.org/10.1147/rd.32.0114).
- **MIT 18.404J, Michael Sipser (2020):** Lecture 1 finite automata, lecture 2 nondeterminism and closure, lecture 7 decision problems. Course outlines used for topic cross-check, not represented as verbatim original proofs. [Lecture resource index](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/pages/lecture-notes/).
- **Original worked derivations:** The divisible-by-three and ending-in-01 automata, inductive invariants, product acceptance conditions, graph-search equivalence method, and direct collision proof are standard mathematical constructions rederived here. Their correctness is established by the written arguments. See `examples/automata_and_grammars_lab.py` for bounded executable corroboration, not a replacement for the proofs.

Claim metadata: `metadata/007000.json`.
