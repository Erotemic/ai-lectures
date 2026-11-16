# Why No Program Can Decide Every Halting Question

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 004000 — Computability and Mathematical Limits  
**Assumed background:** A program can take a finite string as input; a program may halt or continue forever.  
**Companion:** Exact diagonal theorem, bounded-halting exception, proof sketch, and claim-to-source map.

<!-- BEGIN SPOKEN LECTURE -->

Consider a tool that inspects a program before anyone runs it. The tool promises a simple answer. Will this program ever finish on this particular input? If it will finish, the tool says yes. If it will run forever, the tool says no. It never gets stuck, and it never makes a mistake.

It sounds like the ultimate program analyzer. Infinite loops can waste computing resources, block a service, or make a verification task fail to return. A perfect detector would seem to settle all of them. But there is a precise mathematical obstruction: no algorithm can make that promise for every program and every input in a sufficiently general model of computation.

The important words are *every*, *never gets stuck*, and *never makes a mistake*. Removing any one of them changes the question. We can detect many infinite loops. We can establish termination for many programs. We can run a program and observe that it has halted. We can even decide the halting question for carefully restricted programming languages. What we cannot have is a total, correct, general-purpose decision procedure for arbitrary programs.

Let us build the impossibility result rather than invoke it as a slogan.

First choose a precise model. Think of a Turing machine as a finite program operating on a tape whose usable portion is not bounded in advance. A machine has a finite description. That description can itself be encoded as a finite string. A universal machine can read such a description, together with some input data, and simulate the described machine. This is how the mathematical model supports the idea that programs can be data for other programs.

We distinguish the machine's behavior from the outcome of our analysis. A machine *halts* if it reaches a designated stopping state after finitely many steps. It may halt by accepting or rejecting; either counts as halting. If it executes indefinitely, it does not halt. We are not asking whether it returns a useful answer, whether it crashes under a particular operating system, or whether it eventually reaches a point where a human stops watching.

Here is the proposed decision procedure. Call it H. Give H two finite descriptions: a program P and an input x. H always terminates. It answers yes exactly when P eventually halts on x, and answers no exactly when P does not halt on x. Those are the entire rules of the hypothetical procedure.

If H existed, we could create a second program, D, that uses H in a deliberately contrary way. D receives the encoding of a program Q. It asks H what Q will do when Q receives its *own* description as input. If H says Q will halt, D deliberately loops forever. If H says Q will not halt, D halts immediately.

That definition contains no mystical self-awareness. The description of Q is just an ordinary finite string. D passes that same string to H as the program argument and as the input argument. A universal computational model lets us encode and manipulate such strings mechanically. D then chooses between two perfectly elementary actions: stop, or keep executing a loop.

Now give D its own description. Let d be the finite string encoding D. Ask what happens when D runs on d.

Suppose D on d halts. The only way D chooses to halt is if H predicted that D on d would never halt. But H was assumed always correct. So if D halts, it must not halt.

Suppose instead that D on d never halts. The only way D chooses to run forever is if H predicted that D on d would halt. Again H was assumed always correct. So if D does not halt, it must halt.

Neither possibility is consistent with the promised behavior of H. Therefore H cannot exist.

Notice the exact form of the conclusion. We derived a contradiction from the existence of a *total* decision procedure that answers every halting question correctly. We did not derive a contradiction from the existence of programs that analyze particular kinds of loops. We did not show that mathematical proofs of termination are impossible. And we did not show that an analyzer must fail on any particular program that we happen to care about.

The result is stronger than a report that we have not yet invented a sufficiently good tool. The proof covers every candidate algorithm in the model. If someone proposes a new universal halting detector, that detector becomes another possible H. The same construction then gives an input on which the detector's claimed total correctness cannot hold.

Let us examine why the diagonal construction works. Imagine a table. Across its columns are possible program inputs. Down its rows are possible encoded programs. Each cell records whether one program halts on one input. The diagonal cells ask whether the program in a particular row halts when given the encoding that names that very row. The proposed D reverses the yes-or-no behavior on those diagonal cases. When D itself appears among the rows, its own diagonal entry cannot agree with the table's supposed complete decision procedure. The construction is called *diagonalization* because it uses those self-indexed cells.

The word *diagonalization* is historically older than computability theory. Cantor used a diagonal construction to reason about infinite sets. But our proof is not simply an assertion that there are more mathematical questions than programs. It exhibits a specific, finitely described decision problem that defeats every total solver. Counting arguments can establish that some sets of strings are undecidable, because there are countably many programs but far more sets of strings. The diagonal halting argument tells us which natural problem is undecidable and why.

Here is another way to appreciate the boundary. Suppose you run a program for a million steps. It has not halted. Are you entitled to answer no? Of course not. It might halt after a million and one steps, or after an astronomically larger number. You can decide the *bounded* question: does this program halt within the first million simulated steps? Simulate a million steps, or stop earlier if it halts, and answer accordingly. The bounded question is decidable because you have placed a finite upper limit on the observation. The unbounded question has no such limit.

A finite timeout is therefore a legitimate engineering choice, but it answers a different question. If the process exceeds the timeout, the result is unknown relative to the original halting problem. Reporting 'definitely infinite loop' at that point would confuse lack of observation with a proof of nontermination. Conversely, if the simulation actually reaches a halting state, that observed finite execution is a valid positive witness that the program halts.

This asymmetry is useful. We have a general way to recognize positive halting instances. Simulate the program; if it halts, say yes. On a program that never halts, the recognizer can continue indefinitely. It is not a decider, but it does correctly identify every yes instance eventually. That distinction between recognizing and deciding will become a central part of computability theory.

Some nontermination proofs are straightforward. A loop might repeatedly execute a command that leaves all relevant state unchanged. Another program might increase an integer without any condition under which it stops. A termination analyzer can establish a decreasing measure for a recursive function, or use a well-founded ordering to show that an execution cannot continue indefinitely. Such proofs are real results. They simply do not combine into one infallible algorithm for every general program.

The opposite direction is important too. A loop that looks simple syntactically can conceal a difficult mathematical question. Imagine a program that systematically searches for a counterexample to some conjecture and halts only when it finds one. Whether it halts depends on whether such a counterexample exists. A particular conjecture may eventually be resolved by mathematics, which then resolves that particular program's behavior. The halting theorem does not say that we can never learn the answer for an individual instance. It says there is no single algorithm that always supplies the answer for arbitrary program-and-input pairs.

We should also distinguish the mathematics from the slogans of software engineering. 'Finding every bug is impossible' is too broad a summary of this theorem. A specified finite-state device can sometimes be exhaustively analyzed. A program running with an explicit finite bound on memory and input can, under suitable deterministic assumptions, be explored until it halts or repeats an entire configuration. A repeated full configuration in a deterministic transition system implies that subsequent execution will repeat. But making state space finite changes the computational model and the scope of the question. The theorem's unbounded, universal setting is doing real work.

There is a subtle but important technical detail. The contradiction requires D to be a permitted program and its description to be an admissible input. If we instead design a restricted language in which programs cannot interpret arbitrary code and cannot execute an unbounded loop, the construction may not be expressible. Strongly normalizing calculi deliberately guarantee termination of the computations that their typing rules permit. That guarantee does not provide a solution to the halting problem for arbitrary programs outside the calculus. It restricts the class of programs under discussion.

This distinction has implications for verification. A proof assistant may accept definitions for which it can establish termination, or require more explicit reasoning for other definitions. A trusted termination checker can be perfectly sound on its accepted input class without being complete for all possible terminating programs. Some terminating programs will resist its automatic methods. Soundness means it does not certify a false termination claim. Completeness, in this context, would mean it could certify every true one. The universal halting theorem blocks the fantasy of an unrestricted automatic mechanism that decides all such claims.

The historical record deserves careful wording. Alan Turing developed his machine model in a paper received in nineteen thirty-six and published in nineteen thirty-seven. Its main presentation concerns machines producing computable sequences and distinguishes *circle-free* from *circular* behavior; it uses a diagonal argument to establish an undecidability result and applies the model to the Entscheidungsproblem. Today's compact formulation, 'given a program and input, does it halt?', expresses a closely related standard theorem. It would be inaccurate to pretend that the modern two-argument pseudocode is a verbatim passage from Turing's original paper.

The broader mathematical lesson is a change of expectations. Before encountering undecidability, it is natural to imagine that every precisely stated yes-or-no question should admit an algorithm if we are patient or ingenious enough. The halting theorem demonstrates that precision alone is not sufficient. It marks a boundary between problems that can be decided by a general algorithm and problems for which that demand is logically impossible.

It also tells us something constructive about how to ask better questions. Instead of saying, 'Can this tool prove that every program terminates or runs forever?', ask whether it can prove termination for a well-defined language, whether it can produce a witness when a program halts, whether it can analyze bounded behavior, and whether its claims are sound. Every one of those questions can have useful, rigorous answers.

The next time you see a computer stuck in what looks like an infinite loop, remember both halves of the story. There may be a simple explanation and a decisive proof for that very program. There cannot be a universal procedure guaranteed to settle the question for every possible program. That is not a deficiency in one piece of software. It is a theorem about computation itself.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — modern formulation

Fix an effective encoding of deterministic Turing machines over strings in `Σ*` and a universal simulator. Let `HALT = {⟨M,w⟩ : M halts on input w}`, where *halts* includes accepting and rejecting. Invalid encodings can be assigned a fixed convention; this does not affect undecidability on valid encodings.

**Theorem:** No total computable `H : Σ* × Σ* → {0,1}` satisfies `H(⟨M⟩,w) = 1` iff `M(w)` halts for every valid machine `M` and input `w`.

**Proof:** Assume `H`. Define `D(q)` to simulate `H(q,q)` and then:

```text
if H(q,q) = 1: loop forever
else:          halt
```

The assumed totality of `H` makes `D` a well-defined machine. Let `d = ⟨D⟩`. Then `D(d) ↓` iff `H(d,d) = 0` iff `D(d) ↑`, contradiction. `↓` means halt, `↑` means diverge. There is no dependence on a particular programming language's source-code quoting mechanism; the proof uses effective encodings and universality.

**Bounded variant:** `HALT_WITHIN = {⟨M,w,t⟩ : M halts in at most t transitions on w}` is decidable by simulating at most `t` steps, when the input encodes a natural number `t`. The cost of this decider depends on the encoding of `t` and the simulation model. If it says no, it does *not* answer membership in `HALT`.

**Finite deterministic configurations:** In a genuinely finite state space, either a halting state is reached or a complete configuration repeats; the latter certifies indefinite repetition. Assumes the entire future-relevant configuration is among the finite states (not just the instruction pointer).

### Investigate

1. Write two different tiny programs that provably do not halt, and provide the invariant or cycle that establishes it. Why does verifying these cases not contradict the theorem?
2. Formalize the distinction between `HALT_WITHIN` and `HALT`. What would have to be assumed to infer non-halting from a failed bounded search?
3. What breaks in the diagonal proof if H can abstain instead of answering yes or no? What breaks if H is allowed to run forever on some input?
4. Distinguish a program *accepting*, *rejecting*, and *looping*. Which outcomes satisfy the `HALT` property?

## Source-to-claim reading map (non-spoken)

- **Turing, 1936–37:** *On Computable Numbers*, sections 5–8 and 11, credited for universality, diagonal arguments, and the original decision-problem context. The source is not claimed to state the modern two-argument theorem verbatim. [Publisher record](https://doi.org/10.1112/plms/s2-42.1.230).
- **Liesbeth De Mol, Stanford Encyclopedia of Philosophy, *Turing Machines* (2025 revision):** sections 2.3 and 2.4.2–2.4.3 distinguish Turing's original circle-free problem from the modern halting formulation. [Open entry](https://plato.stanford.edu/entries/turing-machine/).
- **Stanford Encyclopedia of Philosophy, *Computability and Complexity*:** sections 2.2–2.4, particularly diagonal halting set `K`. [Open entry](https://plato.stanford.edu/entries/computability/).
- **MIT 6.045J (Spring 2011):** official lecture index, Lecture 7 (decidability) and Lecture 8 (undecidable problems), as independent modern teaching context. [Course index](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/). The indexing page is accessible; individual linked PDFs were not treated as inspected full text.
- **Original proof and engineering examples:** The H/D pseudocode and bounded/finite-state comparisons above are independent expositions of the standard theorem, not quotations from the referenced works. The executable companion supplies finite examples only; it cannot mechanically prove the universal undecidability theorem.

See `metadata/004000.json` for exact anchors and per-claim provenance.
