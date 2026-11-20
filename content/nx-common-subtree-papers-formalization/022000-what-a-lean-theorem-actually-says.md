# What a Lean Theorem Actually Says: Reading the Common-Subtree Proofs

<!-- BEGIN SPOKEN LECTURE -->

Suppose a program announces that it has found the maximum common subtree of two trees. There are at least three very different claims hidden in that sentence. First, it has produced an object that really is a common subtree. Second, the object is better than every competing common subtree under the specified scoring rule. Third, the program that produced the object faithfully implements a method that always returns such an optimum. A fourth claim, that the program does so within a particular time and memory budget, is different again.

The attraction of reading the Lean code in the common-subtree repository is that it forces us to put those claims into separate sentences. We can read one sentence and determine exactly what it guarantees, without guessing from a file name such as Correctness or DynamicProgram. We can also discover what the sentence does not say. The ability to read a theorem statement, and to read the shape of a proof behind it, is the skill we will develop here.

Our examples come from the 2016 weighted common subtree isomorphism formalization and the 2018 embedding dynamic program. No knowledge of tactic programming is required at the start. The goal is to turn source code back into ordinary mathematical speech, then to see how Lean checks the steps that connect those sentences.

## Begin with types, not tactics

In the 2016 mathematical specification, the vertices of the two input trees have types called V and W. They need not be integers. They could be abstract finite types with no particular numbering. The repository uses a type called FiniteTree V to represent a tree with vertices of type V. And it represents a proposed correspondence as a finite set of pairs, one vertex from V and one from W.

That choice is already doing useful mathematical work. A finite set of pairs is not a list of instructions for how to search. It is an object whose meaning does not depend on how we might enumerate it. Suppose Alice has vertices a, b, and c, and Bob has x, y, and z. A proposed mapping might consist of the pairs a with x and b with y. The representation allows us to ask whether that selection has a valid shape before we have written any algorithm at all.

Lean's declaration called PartialBijection says that no selected vertex on one side is paired with two different vertices on the other. Formally it demands uniqueness in both projections. This is stronger than merely avoiding duplicate pairs, which a set already does automatically. The pairs a with x and a with y are different set elements; they are not a partial bijection because a was used twice. Likewise a with x and b with x reuses x.

The declaration called Valid then combines several properties. The correspondence must be nonempty. It must be a partial bijection. The selected vertices must induce connected graphs on both sides. And adjacency must agree in both directions for every pair of selected correspondences. That last condition has a double arrow. If two selected vertices are adjacent in Alice's tree, their images must be adjacent in Bob's tree; and if the images are adjacent, the originals must be adjacent. Both directions distinguish an induced subtree isomorphism from a looser notion that only preserves some edges.

Notice the absence of an algorithm from this definition. No dynamic-programming table, no bipartite-matching solver, no root orientation, no Rust allocation. Valid means what the 2016 mathematical problem says it means. If the implementation changes, this definition can stay fixed.

## Turn an optimization claim into a quantified sentence

The next declaration, called IsMaximum, makes two demands about a candidate mapping. The candidate must be Valid. And for every other candidate, if that other candidate is Valid, its score is at most the score of the chosen one.

Those words are the mathematical heart of optimality. We need an actual winner, and we must rule out every better competitor. The second part is a universal statement over the universe of finite correspondences. It does not literally enumerate the competitors during a proof. A clever algorithm can establish the universal fact by structural reasoning. But the statement it establishes is still about every valid alternative, not just the alternatives a test suite happened to try.

Let's make the scoring issue concrete. Take two trees with one vertex each. There is exactly one nonempty mapping: pair those vertices. Suppose the node-pair reward is minus seven. The maximum nonempty common subtree has score minus seven. The empty mapping might be assigned score zero in some user-facing API, but it is not a valid candidate for this mathematical problem. If a theorem silently changed the candidate set to include the empty mapping, it could return zero and be correct for a different problem. This is why the seemingly small nonemptiness hypothesis is part of the specification, not decoration.

The repository's scoring type also permits a bottom value, representing negative infinity, for a forbidden or impossible score. A bottom value is not the same as an ordinary negative number, and it is certainly not zero. In a proof, the domain of a score is as important as its formula. A theorem about values in a type with bottom does not become a theorem about floating-point NaNs or machine infinities without additional justification.

If we looked only at a function named maximum, we might miss all these choices. By reading IsMaximum, we know the intended competitors, the scoring order, and the witness obligation.

## A theorem of existence is not a solver

Now read a result called exists_maximum, from the same 2016 specification. Its conclusion says that there exists a mapping satisfying IsMaximum. There is no assumption that all node weights are positive, and no assumption that the user will accept an empty answer. The proof uses a mathematical fact about finite sets: a nonempty finite family of ordered scores attains a maximum.

The proof first shows that the family of valid mappings is nonempty. A singleton mapping is always structurally valid: select one vertex from each nonempty input tree. There are no selected edges whose adjacency could disagree. Then it considers the finite family of all valid subsets of vertex pairs. A largest score exists among this family. The proof packages that witness with the requirement that every other valid mapping has score no greater.

That is a serious theorem, but it does not describe an efficient search. If a proof says there exists an optimum, Lean has not thereby compiled a high-performance optimization algorithm. In fact, the specification uses noncomputable mathematical constructions and classical reasoning where convenient. A correct existence proof and a useful program can use radically different methods. The purpose of the existence proof is to assure us that the optimum we discuss is a real mathematical target.

This gives us a practical reading habit. Whenever a theorem's conclusion begins with there exists, ask what is being produced, and whether the theorem merely establishes existence or establishes that a particular executable function produces it. A later theorem can connect those claims. It cannot be inferred from a suggestive identifier.

## How Lean writes the premises

Lean uses an arrow in theorem types in two ways that look similar but serve different roles. A function from an input type to an output type is written with an arrow. An implication between propositions is also written with an arrow. The interpretation depends on the types of the things on either side. For our purposes, read the statement in order: here are the objects we were given; here are the properties we assume; and here is the property we promise to prove.

Some hypotheses are written in square brackets. For example, the code assumes that V and W are finite types and that equality of vertices can be decided. These are typeclass hypotheses. They give access to a finite universe and to finite-set operations such as membership. The score type has algebraic and ordering hypotheses so that weighted sums, comparisons, and maxima make sense. Those assumptions limit where the theorem applies. They are not claims that all possible numerical domains or input encodings have already been handled.

The distinction between parentheses and square brackets helps a reader navigate the language but should not be confused with the mathematical difference between an important and an unimportant assumption. Finiteness is essential to the simple existence argument. A required algebraic structure can be just as essential. If an implementation uses a different number type, the task is to establish that the implementation's arithmetic satisfies an appropriate contract, not to wave away the typeclasses.

In the Lean source, implicit variables sometimes appear in braces rather than parentheses. That means Lean ordinarily infers them from the surrounding context. The variable has not vanished from the theorem. If the statement refers to a tree of type V, the type V still governs everything that follows, even if Lean fills in its name without making a caller write it.

## Read a recurrence theorem without confusing its sides

Turn now to the 2016 theorem named rooted_matching_recurrence. It fixes a pair of root vertices. On the left side of the equality is a rooted optimum, defined through the valid common-subtree witnesses. On the right is the reward for pairing those two root vertices, plus the weight of an optimal partial matching between their child branches.

This is the familiar mathematical recurrence from the paper, but its precise Lean form is more informative than a diagram. The root reward is included exactly once. The child weights include the appropriate edge reward and an optimum inside the corresponding child components. A partial matching leaves branches unmatched when pairing them would reduce the total. The theorem says these two constructions give the same number.

As a tiny illustration, suppose the first root has children a and b, and the second has children x and y. Suppose the four possible branch-pair scores are: a with x gives four; a with y gives three; b with x gives two; b with y gives minus six. If we pick the largest individual branch, four, we cannot also pick b with x because x is already used. Adding the remaining b with y would make the score worse. But the alternative matching a with y and b with x totals five. The best partial matching is five. The rooted optimum therefore receives the root-pair reward plus five, provided these are the actual optimal branch values. It is not simply the sum of the largest number in each row.

The theorem's proof has two directions, expressed by a tactic called le_antisymm. To show two ordered values are equal, first prove that the left side is at most the right side, then prove the reverse inequality. For the first inequality, choose an actual optimal rooted witness. Cut it at the selected roots. Its child branches determine a valid partial matching, and each branch score is bounded by the corresponding optimal child value. The total cannot exceed the matching optimum on the right side.

For the reverse inequality, start with the optimal child matching and choose optimal witnesses for its selected branch pairs. Assemble them under the mapped roots. Because the child branches are disjoint, the assembly is a valid rooted isomorphism. The independent rooted optimum must score at least as much as this constructed witness. The two inequalities together prove equality.

This is a mathematical proof, not a syntactic trick. The repository has separate lemmas about branch decomposition and branch assembly because both directions require real structural facts about trees. The small Lean proof calls those lemmas instead of re-proving them inline. This is a common pattern: a short theorem at the end of a file can depend on a large amount of difficult prior work.

## Read the proof body as a sequence of transformations

Many Lean proof scripts are compact if you know a handful of verbs. The command exact says: here is already a term whose type is the goal. The command apply selects a theorem or constructor whose conclusion matches the goal and leaves its premises to be proved. The command rw uses an equality to rewrite an expression. The command simp applies simplification rules, often including definitions and previously proved elementary lemmas. The command rfl establishes equality by reducing the two sides to the same expression. The command obtain takes apart an existential witness or some other structured hypothesis. A dot in a structured proof can introduce a new subgoal or case.

None of these tactics creates truth out of thin air. Lean elaborates the script into a proof term. The trusted kernel checks whether the term has the claimed type, using the definitions, axioms, and theorems available in the environment. A failed goal cannot be made true by persuasive prose. On the other hand, a successful proof checks exactly the proposition that was written. A theorem with a weaker or mistaken specification can be perfectly proved and still fail to answer the intended research question.

For a small illustration, the singleton-score theorem in Specification.lean says that a mapping consisting of one pair has score equal to the node weight of that pair. Its proof is essentially simp. But simp succeeds because earlier definitions say that the score sums node weights and unordered mapped-edge weights, and because a singleton has no mapped edges. The terse final script sits on top of explicit mathematical choices. When a source proof looks one line long, inspect the definitions that made that line possible.

## A correct step is not yet a correct table

The 2018 formalization offers a richer example. It has two boundary states: mapped and skipped. The theorem step_correct in RootedDynamicProgram.lean does not say that an arbitrary table update computes the independent optimum from arbitrary earlier values. It assumes that the supplied child lists describe the actual rooted child relation, and that every earlier state on which the current state depends already equals the corresponding independent mathematical optimum. Under those hypotheses, one evaluation step is correct.

This is exactly what a dynamic-programming proof ought to say locally. A recurrence can calculate a correct answer only if its inputs are the correct answers to the smaller problems. In Lean, the assumption appears as a quantified dependency statement. If a pair p is a dependency of the current pair, the previous table entry at p must equal sourceState at p. The theorem then proves that step at the current pair equals sourceState there.

A second theorem, evaluate_correct, supplies the missing global argument. It associates a rank with every state, proves dependencies have smaller rank, and uses sufficiently many evaluation rounds. The theorem requires a complete enumeration of state pairs and a rank bound for the queried pair. A third theorem, solve_correct, shows that the particular solve function chooses enough rounds from the finite vertex-list sizes and returns the independent state values. Here the proof really has crossed from a conditional local recurrence to a specific finite-table evaluator.

There is still another boundary. The executable evaluator described here is the formalized reference program, not the optimized production Rust embedding solver. The theorem does not mention the production function, its choice arena, the floating-point matching routine, or the Python wrapper. A proof of the reference evaluator is a useful foundation for source refinement, but it is not the refinement theorem itself.

## A disciplined way to read a large proof repository

When you open a theorem, read only the declaration until you can translate it into a sentence: for all which trees, under which numerical assumptions, given which valid or computational objects, what precise conclusion follows? Pay attention to the source of each side of an equality. An equation between two algorithms may be less informative than an equation between an independent specification and an algorithm.

Next open the definitions that appear in the conclusion. For IsMaximum, that takes us to Valid and score. For rooted_matching_recurrence, it takes us to the independently defined rootedValue and the weighted-matching objective. For step_correct, it takes us to the dependency relation and sourceState. At this stage we should know the mathematics without needing to read the implementation of every tactic.

Only then scan the proof body. Identify the strategy rather than memorizing syntax. Was the proof a finite maximum argument? Two inequalities? Induction over a contraction sequence? A rewrite by an existing representation theorem? A table invariant established by a well-founded rank? These strategies recur throughout the three papers, and they are the bridge between familiar mathematical reasoning and proof-assistant code.

Finally, state the boundary explicitly. The 2016 existence theorem establishes an optimum but no solver. The 2016 rooted recurrence establishes the mathematical identity, not the optimized runtime. The 2018 table theorem establishes the reference evaluator against independent state values, not the production Rust algorithm. That is not a criticism of the formalization. It is a way to know precisely what has been achieved and what a new theorem must still prove.

By reading these declarations this way, you can begin a formalization task at the right layer. You will know whether a missing argument is about the existence of a witness, the decomposition of a witness, the recurrence, the table evaluation order, the source implementation, or its resource use. Lean's notation stops looking like a wall of unfamiliar symbols and starts looking like a carefully annotated mathematical contract.

<!-- END SPOKEN LECTURE -->

## Companion: exact declarations and a reading key

The Lean examples below are from the **2026-11-19 supplied** `networkx_algo_common_subtree` snapshot. They are excerpts for reading, not independently executable code blocks without imports and surrounding variable declarations.

### Independent specification: `Droschinsky2016/Specification.lean`

```lean
abbrev Mapping (V W : Type*) := Finset (V × W)

def PartialBijection (pairs : Mapping V W) : Prop :=
  (∀ p ∈ pairs, ∀ q ∈ pairs, p.1 = q.1 → p = q) ∧
  (∀ p ∈ pairs, ∀ q ∈ pairs, p.2 = q.2 → p = q)

def IsMaximum (left : FiniteTree V) (right : FiniteTree W)
    (weights : Scoring V W K) (pairs : Mapping V W) : Prop :=
  Valid left right pairs ∧
    ∀ other, Valid left right other →
      score left weights other ≤ score left weights pairs
```

`Valid` additionally requires `pairs.Nonempty`, connected induced vertex images, and `Adj` equivalence. The theorem `exists_maximum` concludes `∃ pairs, IsMaximum left right weights pairs` for finite nonempty trees, with no positivity hypothesis; it uses `singleton_valid`, `feasible`, and `Finset.exists_max_image`.

### Paper recurrence: `Droschinsky2016/RootedRecurrence.lean`

```lean
theorem rooted_matching_recurrence (left : FiniteTree V) (right : FiniteTree W)
    (weights : Scoring V W K) (root : V × W) :
    rootedValue left right weights root.1 root.2 root.1 root.2 =
      weights.node root.1 root.2 + WeightedMatching.weight
        (childWeights left right weights root)
        (bestChildMatching left right weights root) := by
  apply le_antisymm
  -- first inequality: decompose an actual optimum
  -- second inequality: assemble optimal child branches
```

*Reading hint:* `rootedValue` is defined through witness feasibility, not as the result of `bestChildMatching`. The equality is therefore substantive. The two inequalities invoke `RootedValid` decomposition and `optimalBranches` assembly. The comments above summarize the proof branches rather than reproducing the full body.

### Conditional local step: `Droschinsky2018/RootedDynamicProgram.lean`

```lean
(hprevious : ∀ p,
  RootedEvaluationOrder.Depends left right leftBase rightBase p (u,v) →
  previous p.1 p.2 =
    sourceState left right weights penalty leftBase rightBase p.1 p.2)
```

This is one of `step_correct`'s actual hypotheses. `evaluate_correct` derives correctness from rank-decreasing dependencies and complete state enumeration; `solve_correct` discharges the required number of rounds for the chosen vertex lists. `unrootedOptimum_correct` evaluates the independent unrooted optimum by trying all root pairs, not by using the paper's optimized fixed-first-root split.

### Five things to distinguish when reading

| Lean text | Mathematical interpretation | Not to infer |
| --- | --- | --- |
| `∃ x, P x` | At least one object satisfies `P` | An efficient executable finder exists |
| `∀ other, Valid other → ...` | Every **valid** competitor is bounded | Every possible subset is valid |
| `x ↔ y` | Both directions, or logical equivalence | Just soundness from left to right |
| `A = B` | Equality in the types of `A` and `B` | Correctness of an unmentioned third program |
| `hprevious : ...` | A required premise of the local theorem | That the premise is automatically true for a source table |

### Reading exercises

1. Why does `Valid` need both adjacency directions? Describe an invalid pair map that preserves existing edges but fails inducedness.
2. Take two single-vertex trees with node reward minus seven. What does `exists_maximum` guarantee? What would change if empty mappings were feasible?
3. Locate the two uses of `le_antisymm` in `rooted_matching_recurrence`. Identify which side begins with an existing optimal witness and which constructs a witness from a matching.
4. Explain why the hypothesis `hprevious` in `RootedDP.step_correct` cannot simply be omitted, and which later theorem discharges it.

**Prerequisite links:** `logic-types:004000` (inductive types), `logic-types:005000`–`006000` (equality and rewriting), `logic-types:008000` (kernel checks); `mathematical-proof:009000` (quantifiers and induction). **Primary project source:** the user-supplied `networkx_algo_common_subtree` snapshot, `proofs/SubtreeProofs/Droschinsky2016/Specification.lean`, `RootedRecurrence.lean`, and `proofs/SubtreeProofs/Droschinsky2018/RootedDynamicProgram.lean`. These are source-reading examples, not new Lean proof contributions.
