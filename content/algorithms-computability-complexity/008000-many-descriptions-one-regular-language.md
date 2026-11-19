# Many Descriptions, One Regular Language

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 008000 — Nondeterminism, Regular Expressions, and State Distinguishability  
**Assumed background:** Alphabets, languages, deterministic finite automata, and elementary proof by contradiction. All are briefly reintroduced.  
**Companion:** Subset construction, expression-to-automaton proof sketch, pumping lemma, Myhill–Nerode theorem, and source map.

<!-- BEGIN SPOKEN LECTURE -->

Suppose two engineers build machines to recognize the same set of messages. One draws three circles connected by arrows. The other writes a compact pattern. A third builds a machine that appears to split into several possible futures whenever it reads a character. How can we tell whether these descriptions mean the same thing? And when no finite machine can possibly perform the recognition, what kind of proof establishes that limitation?

We need to separate the language from its presentation. A language is a set of finite words over a specified alphabet. An automaton is one way to describe it. A regular expression is another. And a language may admit many distinct automata, with different numbers of states, even though they accept exactly the same words.

Begin with a deterministic finite automaton. In each state, the next symbol determines precisely one successor state. Its behavior on an entire word is just a single path. Now imagine a different device, a nondeterministic finite automaton, or N-F-A. On a given symbol it may have several possible successors, or none. In the usual version it may also take a transition that reads no input at all, called an epsilon transition.

What does acceptance mean if the machine has choices? It means that at least one complete path consumes the entire input and reaches an accepting state. It does not mean that every path succeeds. And it does not mean that a physical machine has been endowed with a power to guess the correct future. Nondeterminism here is a mathematical description of possible paths. A deterministic implementation can track the set of all currently possible states.

Consider the language of binary words ending in zero-one. Build a nondeterministic machine with three states. The initial state loops on either zero or one. On a zero it can also jump to a second state, as though guessing that this zero is the next-to-last character. From the second state, a one leads to a final accepting state, and there are no transitions out of that accepting state. The machine accepts if there exists a guess made at exactly the right place.

For the word one-zero-one, the initial state follows its loop through the first one. At the zero it has two paths. One stays in the initial state; another jumps to the second. On the final one, the second path reaches acceptance. For the word zero-one-one, a path may reach acceptance after the first two characters, but then cannot consume the final one. That path is not successful, and no other path can finish accepting. So the whole machine rejects.

A nondeterministic description can be compact because it postpones decisions instead of encoding their consequences in an explicit state list. But is its language more powerful than a deterministic automaton's? No. Michael Rabin and Dana Scott's foundational work established the central equivalence: nondeterminism does not enlarge the class of languages recognized by finite automata.

Here is the construction that makes this statement precise. If the N-F-A has a finite set Q of states, construct a D-F-A whose states are subsets of Q. After reading any input prefix, its current subset will contain exactly those N-F-A states reachable by some path consuming that prefix. Initially, include the original start state and all states accessible from it by epsilon transitions. To process a symbol, collect all successors of every state in the current subset, then add everything reachable through epsilon transitions. This new subset is the next D-F-A state.

The new machine accepts whenever its current subset contains at least one accepting N-F-A state. Why is this correct? The invariant says the subset equals the collection of states reachable after consuming the prefix. It holds for the empty input by construction. Appending one character is exactly what the transition rule simulates. By induction, it holds for every prefix, including the full word. Therefore the deterministic and nondeterministic descriptions agree on every input.

There is a cost. A set of m states has two to the m possible subsets, so the constructed deterministic automaton may have exponentially many states. Frequently far fewer subsets are reachable, but the exponential worst case is real. Nondeterminism does not expand recognizability here; it can expand succinctness. We should not confuse equal expressive power with equal representation size or equal practical compilation cost.

Next comes the third description, a regular expression. In formal-language theory, begin with expressions for the empty language, the language containing only the empty word, and languages containing a single symbol. Combine expressions using three operations: union, concatenation, and Kleene star. Union means one language or the other. Concatenation means take a word from the first and then a word from the second. Star means repeat words from the given language any finite number of times, including zero repetitions.

For example, the formal pattern 'zero or one, repeated any number of times, followed by zero-one' recognizes exactly the binary words ending in zero-one. We can write it symbolically as a parenthesized choice between zero and one, then a star, then zero and one. The star applies to the parenthesized choice, not just to the final one. Parentheses matter because they determine which language is repeated.

We can construct an epsilon N-F-A for every regular expression by structural induction. The empty, empty-word, and single-symbol expressions each have simple automata. To implement union, create a new initial branch with epsilon transitions to the two component machines. To implement concatenation, connect acceptance of the first component to the start of the second by epsilon transitions. To implement star, allow an epsilon path that accepts without repetitions, and paths that return from the component's completion to begin another repetition.

We have therefore established that every formal regular expression denotes a language recognizable by a finite automaton. The converse also holds: every finite automaton has an equivalent regular expression. One proof eliminates states one by one, replacing paths that visit an eliminated state with expressions that account for any number of loops there. The expressions may grow large, but the procedure terminates because the graph has finitely many states.

Together these constructions say that finite automata, nondeterministic finite automata, and formal regular expressions describe precisely the same languages. The equivalence is mathematical, not a claim about identical software behavior. Practical regular-expression engines often add features such as backreferences, which are not part of this formal definition and can recognize patterns beyond the regular languages. Their performance characteristics also depend heavily on implementation strategy.

Now ask for a limit theorem. We want a language that no regular expression, D-F-A, or N-F-A can describe. Consider zero repeated n times followed by one repeated n times, for any nonnegative integer n. Each individual word is easy to check with an ordinary program that has an unbounded counter. The issue is whether a fixed finite number of states can remember an arbitrary n.

There is a famous necessary condition for a language to be regular: the pumping lemma. Imagine a D-F-A with p states reading a word at least p characters long. Among its first p plus one visited states, some state repeats. The intervening nonempty segment of the input takes the machine around a loop. We can traverse that loop zero times, once, or any number of times, and then complete the rest of the input with the same acceptance outcome.

In formal terms, if a language is regular, there is a positive number p such that every word in the language of length at least p can be split into three consecutive pieces, called x, y, and z. The middle piece y is nonempty. The combined length of x and y is at most p. And replacing y with any number of copies, including none, keeps the resulting word in the language.

The order of the quantifiers matters. We are allowed to choose a sufficiently long word after the supposed pumping length is fixed. But for that word, a proponent of regularity gets to choose a valid decomposition. To prove nonregularity, we must defeat every allowed decomposition, not just the one we find most convenient.

Suppose our equal-count language were regular, and let p be its pumping length. Choose p zeros followed by p ones. Because x and y occupy only the first p characters and y is nonempty, y consists solely of zeros. Remove y by pumping zero times. The result has fewer than p zeros but still p ones, so it is not in the language. This contradicts the pumping condition. Therefore the language is not regular.

There is an important asymmetry. The pumping lemma can prove that a language is nonregular by contradiction. Merely showing that a language satisfies a pumping-like condition is not, by itself, a general proof of regularity. The lemma gives a necessary condition, not a characterization. A successful test on a finite collection of strings has even less force. We must attend to the logical direction of a theorem.

We can reach the same boundary from a more structural idea: distinguishable prefixes. Take two prefixes u and v. Call them equivalent for a language if every possible suffix w yields the same membership answer for u followed by w as for v followed by w. In other words, after u and after v, no future continuation can tell the pasts apart for the purpose of this decision.

If a D-F-A reaches the same state after u and v, those prefixes must be equivalent. Given the same suffix, the machine follows exactly the same transitions and returns the same answer. So a machine with k states can have at most k different kinds of distinguishable histories.

Surprisingly, this necessary condition is sufficient. Suppose a language has only finitely many such equivalence classes of prefixes. Create one state for each class. Start in the class of the empty prefix. On symbol a, move from the class of u to the class of u followed by a. This is well defined: if u and v are equivalent, then u followed by a and v followed by a are also equivalent, because every suffix after a is already covered by the equivalence definition. Mark a class accepting when its prefixes belong to the language. The resulting finite automaton recognizes the language exactly.

This is the substance of the Myhill–Nerode characterization. It tells us something the pumping lemma alone does not: a language is regular if and only if it has finitely many distinguishable right-context classes. Moreover, the number of classes is exactly the number of states required by a smallest complete deterministic automaton, up to renaming its states.

Look again at zero to the n followed by one to the n. The prefixes with zero zeros, one zero, two zeros, and so on are pairwise distinguishable. To distinguish prefixes of lengths i and j with i smaller than j, append i ones. The first completed word is in the language; the second is not. Thus there are infinitely many classes, and no finite automaton can recognize the language. This argument is a direct proof, rather than an appeal to a syntactic property of one proposed machine.

Historically, the characterization carries the names of John Myhill and Anil Nerode, whose related work belongs to the late nineteen fifties. Kleene's representation result and Rabin and Scott's treatment of finite automata helped establish the equivalences that make these questions precise. We should preserve the authorship of those contributions without pretending that every modern proof is copied from an original paper.

The theme is now clear. Different descriptions can hide or expose different aspects of a computation. Nondeterministic paths make composition convenient. Regular expressions make patterns concise. Deterministic states make execution explicit. Equivalence constructions prove that these presentations express the same restricted class. Distinguishable futures tell us exactly when no representation in that class can exist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

### NFA and determinization

An epsilon NFA is `N=(Q,Σ,Δ,I,F)` where `Δ:Q×(Σ∪{ε})→P(Q)`, and `I⊆Q` is a nonempty set of initial states (a singleton also suffices). Let `E(S)` be the epsilon closure of `S`.

The subset DFA has states `P(Q)` (or only its reachable part), initial state `E(I)`, transition `T(S,a)=E(⋃_{q∈S}Δ(q,a))`, and accepting subsets `S` such that `S∩F≠∅`. Induction on `w` proves that the reached subset equals all NFA states reachable through paths whose non-epsilon symbols spell `w`. Hence `L(D)=L(N)`.

**NFA for suffix `01`:** states `q0,q1,q2`, initial `q0`, accept `q2`, and transitions `Δ(q0,0)={q0,q1}`, `Δ(q0,1)={q0}`, `Δ(q1,1)={q2}`, all others empty. Determinization preserves the language.

### Regular expressions and closure

Formal regular expressions have constants `∅`, `ε`, and `a` for symbols `a∈Σ`, and constructors `R|S`, `RS`, `R*`. Semantics:

- `L(R|S)=L(R)∪L(S)`;
- `L(RS)={xy:x∈L(R),y∈L(S)}`;
- `L(R*)=⋃_{k≥0}L(R)^k`, where `L(R)^0={ε}`.

Thompson-style construction produces an epsilon NFA by induction for each constructor. The reverse direction follows by state elimination. With intermediary state `k`, the generalized edge expression from `i` to `j` updates as `R_ij ← R_ij | R_ik (R_kk)* R_kj` using expressions calculated *before* eliminating `k`. The result has an equivalent regular expression but need not be compact.

### Pumping lemma: exact order

If `L` is regular, `∃p≥1 ∀w∈L` with `|w|≥p`, `∃x,y,z` such that `w=xyz`, `|y|≥1`, `|xy|≤p`, and `∀t≥0:xy^t z∈L`.

Proof: for a DFA with `p` states the run on the first `p` characters visits `p+1` states. A repeat at positions `i<j≤p` gives `x=w[:i]`, `y=w[i:j]`, and `z=w[j:]`; traversing the repeated-state loop any number of times preserves the final state. The condition is **necessary**, not sufficient. For `L={0ⁿ1ⁿ:n≥0}`, choose `w=0ᵖ1ᵖ`; every legal `y` contains only zeros; `t=0` is a counterexample.

### Right congruence and minimal DFA

Define `u ≡_L v` iff `∀w∈Σ*: (uw∈L ⇔ vw∈L)`. This is a right congruence: `u≡_L v` implies `ua≡_L va` for any `a`. If a DFA accepts `L`, then prefixes reaching one state lie in one class, so there are at most `|Q|` classes. Conversely, if there are finitely many classes, taking classes as states gives a complete DFA. Distinct classes require distinct states, so the number of classes is the minimum DFA state count. This is the Myhill–Nerode theorem; the lecture supplies both proof directions.

For `L_end01`, prefixes `ε`, `0`, and `01` have three distinct right contexts: `01` differs from the first two on suffix `ε`, while `0` differs from `ε` on suffix `1`. The three-state DFA from 007000 is therefore minimal. For `L_equal`, prefixes `0ⁱ` are pairwise distinguishable by suffix `1ⁱ` for each pair `i<j`; there are infinitely many classes.

### Formal-language versus engine regex

A formal regular expression has only union, concatenation, and star (plus harmless abbreviations such as finite repetition). Practical expression engines may contain backreferences or other nonregular operations; the equivalence theorem applies to the formal operations. This distinction does not entail that every implementation of a regular expression runs in linear time, or that every practical extension increases expressive power.

## Exercises

1. Determinize the three-state NFA for suffix `01`. Enumerate the reachable subsets and identify which contain `q2`.
2. Prove closure under concatenation using epsilon NFAs. Why is a direct product not the most natural construction for concatenation?
3. Explain why the pumping-lemma proof must handle all legal decompositions, not just one.
4. Show that the prefixes `ε`, `0`, and `01` are pairwise distinguishable for the ends-in-01 language, and conclude a minimal-state lower bound.
5. For every `k≥1`, exhibit at least `k` pairwise distinguishable prefixes for the equal-count language.

## Source-to-claim reading map (non-spoken)

- **Kleene (1956),** “Representation of Events in Nerve Nets and Finite Automata,” *Automata Studies*, pp. 3–41, particularly the regular-events representation result. [Institutional PDF](https://www2.fiit.stuba.sk/~kvasnicka/CognitiveScience/2.prednaska/kleene56representation%5B1%5D.pdf). Historical source; not a claim that this manuscript reproduces the original proof line by line.
- **Rabin and Scott (1959),** “Finite Automata and Their Decision Problems,” *IBM Journal of Research and Development* 3(2), 114–125. Primary attribution of foundational finite-state results; publisher abstract and bibliographic record inspected. [DOI](https://doi.org/10.1147/rd.32.0114).
- **Anil Nerode (1958),** “Linear Automaton Transformations,” *Proceedings of the American Mathematical Society* 9(4), 541–544. Primary bibliography for the named theorem, supported by Stanford's historical account of Myhill and Nerode. [AMS DOI](https://doi.org/10.1090/S0002-9939-1958-0135681-9), [Stanford historical timeline](https://web.stanford.edu/class/archive/cs/cs103/cs103.1242/timeline_of_results).
- **MIT 18.404J, Michael Sipser (2020),** lectures 1–3, covering automata, regular expressions, equivalence, and pumping. [Course lecture index](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/pages/lecture-notes/). The independently stated induction proofs and worked NFA are not represented as verbatim reproductions.
- **Original formal derivations:** Subset invariant, all pumping quantifiers, both directions of Myhill–Nerode, and the explicit suffix-01 minimality proof are self-contained here; `examples/automata_and_grammars_lab.py` confirms bounded instances only.

Claim metadata: `metadata/008000.json`.
