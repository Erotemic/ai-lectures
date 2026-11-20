# When Rust Becomes a Lean Theorem: Charon, Aeneas, and the Source Contract

<!-- BEGIN SPOKEN LECTURE -->

Imagine a dynamic program whose mathematics has been proved correct. Its recurrence is exact. Its table invariant is exact. Its matching subroutine is described by a mathematical maximization over every permitted pairing. Then somebody implements that subroutine in Rust. It stores the matrix in vectors, changes an assignment cost from a signed integer to a wider accumulator, and translates the returned assignment into pairs of original indices. The function passes every test we can think to run.

There is still a gap. The theorem about an abstract matching does not say that this particular Rust program returns that matching. A proof about an independently written Lean function would not say so either. To cross the gap, we must connect the executable source code, its actual data representations, and its success and error behavior to the mathematical specification.

The common-subtree repository has already crossed this boundary for an important component. Its verified signed partial-matching API is written in Rust, translated into Lean with Charon and Aeneas, and accompanied by a theorem about the public function's result. This is a good case for learning what source-level verification looks like before trying to prove an entire optimized tree solver. We will follow the real pipeline and the real theorem, not a hypothetical translation that succeeds by assumption.

## From mathematics to a concrete function

The mathematical matching problem begins with two finite sets of vertices and a weight assigned to each permitted cross-edge. A partial matching contains pairs with no repeated left or right endpoint. Its score is the sum of the selected weights. Forbidden edges are not selectable. The empty matching is legal and has score zero. The optimum is the greatest score among all these legal matchings.

That definition is deliberately independent of a storage layout. We could represent the left and right sets with arbitrary finite types. We could represent a matching as a finite set of pairs. We could quantify over all such sets to define the optimum without suggesting whether the code will use arrays, heaps, or hash tables.

The concrete verified Rust API chooses a different interface. The input is a borrowed slice of rows, with each row a vector of optional signed 64-bit weights. A present integer is a permitted pair. An absent entry forbids it. The output is either an error or a structure containing a vector of matched index pairs and a total score held in a signed 128-bit integer.

This representation forces us to answer questions that the mathematical definition did not need. Are all rows the same width? Which width is meant if there are no rows? Can the sum of the two dimensions fit the internal assignment representation? What happens if a conversion overflows? Can a returned pair refer outside the input matrix? If two output pairs use the same row or column, what detects the bug? A complete function specification must answer each question.

One useful discovery in this repository is that the public matching theorem addresses both successful and rejected inputs. It is not merely a statement beginning, 'assuming the algorithm succeeds.' It says what a valid result means and what errors are permitted when the input representation does not satisfy the accepted shape and size conditions.

## Why Charon and Aeneas appear

Charon reads Rust source through a compiler-aware extraction process and produces an intermediate representation commonly called LLBC. Aeneas consumes the extracted representation and generates functional definitions and proof-oriented semantics in a theorem prover. Here the chosen backend is Lean. The translated definitions give us something linked to the maintained Rust function rather than a second, independently hand-written model that might drift from it.

The repository's regeneration script is named `dev/regenerate_rust_lean.sh`. It pins a release of the tools, installs the corresponding Rust toolchain, extracts maintained Rust crates, and generates Lean modules under `proofs/SubtreeProofs/Rust/Generated`. The concrete generated modules include `VerifiedAssignmentCore.lean` and `VerifiedOrderedCore.lean`. The script has a check mode that compares regenerated output with the retained files instead of silently changing the semantics under the proof.

The workflow is more substantial than reading Rust and writing Lean lookalike code. Suppose the source function indexes a slice after checking its bounds. The translated function and the verification libraries expose the indexing operation and its safety condition. Suppose the source uses checked arithmetic. The proof must establish that the value fits or account for the checked failure. Suppose the function has a loop. The proof requires a termination measure and an invariant describing the state after each iteration.

This is also not a claim that a compiler is formally verified from Rust source to machine code. There is a trusted extraction and translation boundary, and the project pins and checks the generated artifacts. A theorem about translated source semantics is stronger than a theorem about a hand-written recurrence, but it is not a blanket theorem about every compiler optimization, allocator operation, or physical runtime cost.

## An input that fits on paper

Let's take a rectangular matrix with two rows and three columns. In the first row, the weights are seven, forbidden, and minus four. In the second row, the weights are six, five, and forbidden. The word 'forbidden' means the Rust input contains no value at that position, not an integer near negative infinity.

The maximum partial matching pairs the first row with column zero, earning seven, and the second row with column one, earning five. The total score is twelve. Those pairs do not share a row or column, and both select permitted entries. We can compare them with alternatives. Assigning the second row to column zero earns six, but prevents the first row from taking its seven-point edge. The first row could then take its minus-four edge, but would be worse off doing so. Omitting that edge leaves six. Matching the first row to column zero alone earns seven. Twelve is therefore optimal.

The negative entry is worth keeping in the example because it prevents an easy but incorrect interpretation of the Rust interface. A permitted negative edge is still permitted. The optimizer is simply free to leave it unmatched. The output does not need to include every permitted pair, or even the maximum number of pairs. If every permitted weight were negative, the empty matching would be optimal with score zero.

The public Rust function uses an assignment reduction. It constructs a larger square cost matrix with dummy structure, solves a perfect assignment in that matrix, and decodes only the real, useful matched pairs. The source's decoding logic retains compatible original positions of positive weight. Nonpositive entries can be omitted without lowering the optimum, because this is a partial matching. The output for our example uses original zero-based coordinates: row zero, column zero; and row one, column one. A dummy assignment column is not a node in the original input. The decoder must not leak it into the output.

This is the sort of correctness we can state precisely. The output pairs must have unique coordinates, every pair must lie within the input dimensions and select a permitted weight, the sum of their selected weights must equal the stored total, and no other valid partial matching may score more. That is stronger than returning the right number twelve. A function that returned twelve along with a duplicated or out-of-range pair would not meet the witness specification.

## A specification for success and failure

Open `Rust/MatchingEntrypoint.lean`. It introduces a predicate called `Admissible`. The input must be rectangular, and the combined dimensions must satisfy two machine-size bounds used by the implementation: the sum is at most the maximum unsigned 32-bit value, and strictly below the machine's maximum `usize` value. The empty matrix is represented with width zero.

The theorem then introduces `ResultSpec`, a proposition about the actual return value. In the success case, the input is admissible and the result satisfies `CorrectPartial`. That correctness predicate is defined in `MatchingSolveBuiltMatrix.lean`. It says that the returned list has no duplicate pairs, corresponds exactly to a mathematically defined finite matching on the original input indices, that the finite matching is globally maximum, and that the returned 128-bit total equals its mathematical weight.

In the error case, `ResultSpec` allows a nonrectangular error for a nonrectangular matrix, or a too-large error for a rectangular matrix that violates the prescribed size bounds. Notice the order: shape validation precedes the dimension rejection in the public function. A matrix with inconsistent row lengths is rejected for its shape rather than allowed to wander deeper into the matching code and fail somewhere incidental.

The source's Rust error type contains other variants, including assignment failure and arithmetic overflow. Merely observing those variants does not mean they are possible outcomes of every public call. The verified total specification proves that, for the represented input family covered by this theorem, the public function either returns a correct result or one of the specified shape and size rejections. It is not enough to say that the program checks arithmetic; the proof must show that the relevant checked operations cannot produce an unexpected error on admitted inputs.

The central theorem is `max_weight_partial_matching_total_spec`. Its conclusion applies to the actual translated `matching.max_weight_partial_matching` function and says that every result satisfies `ResultSpec`. A companion theorem, `max_weight_partial_matching_spec`, specializes this: whenever the input is admissible, the function succeeds with a correct matching. The theorem does not ask the caller to provide the optimum matching or a proof of the internal assignment algorithm. Those are established by the imported helper theorems and the composition in the source-level proof.

## The chain inside the matching theorem

The proof does not expand the whole translated Rust program into one enormous calculation. It composes smaller verified calls, each with a contract. A theorem about row validation says the boolean produced by the actual checking loop agrees with rectangularity. A dimension theorem handles checked addition and the bounds needed for the square assignment. Cost-construction lemmas connect the actual matrix cells to the mathematical matching-to-assignment reduction.

The assignment routine has its own correctness argument. Once a valid square assignment is available, a matching bridge explains how its choices correspond to a maximum partial matching in the original matrix. That bridge must handle the dummy rows and columns, which exist only to turn an optional pairing into a perfect assignment. It also has to account for the change from maximizing profits to minimizing costs.

The decoding theorem is particularly tangible. `MatchingDecoding.decode_pairs_spec` follows the actual loop that builds the returned vector of pairs. For each left row, it reads the chosen assignment column, translates that column back into the right input coordinate when appropriate, checks that the selected original weight is positive, and either appends a pair or skips it. The proof uses a loop invariant: the vector built so far equals the independently specified decoded prefix of the assignment. It also proves that the returned coordinates are in their original input spaces, not the dummy assignment space.

The total score has another representation boundary. The original matrix contains signed 64-bit weights. The output uses a signed 128-bit accumulator. The proof establishes the bounds needed for safe cost negation and accumulation in the accepted dimension regime. It links the returned integer to the exact mathematical sum. We should not mistake that for a theorem about arbitrary floating-point inputs or about an unbounded mathematical integer being stored in a machine word without conditions.

Finally, the public theorem uses the verified lower-level contracts in the same order as the real source control flow: derive the width, check rectangularity, check the dimension, take the special nonpositive branch if applicable, build the cost matrix when needed, solve the assignment, decode the original-index pairs, and return the result. The proof explicitly accounts for rejected inputs. The advantage of this structure is that we can understand each interface independently and then see how their postconditions become the next call's preconditions.

## A function theorem is not a system theorem

We now possess a valuable source-level result: the actual signed-integer matching core satisfies a precise input-output specification. It is tempting to announce that the Droschinsky tree solver is verified. That would skip several more bridges.

A tree dynamic program calls matching as one ingredient in a larger recurrence. The matching matrix is built from child-pair scores, and those scores depend on previous tree states. To use the matching theorem in a tree-solver proof, we must first prove that every matrix entry fed to the source function represents the intended mathematical child-branch value. We must prove the source's table schedule supplies correct earlier values. We must prove it handles forbidden pairs and impossible states with the intended semantics. And if the source uses the paper's optimized family of related matching problems, we must prove that the reused solution has the same value as the independent matching optimum, rather than merely having a fast update procedure.

The production Rust graph solver also uses numerical and representation choices that are not the `Option i64` matrix contract just discussed. In particular, the production interfaces can use floating-point scores and maintain choice information for path reconstruction. The pinned source and proof records leave the complete floating-point refinement, the optimized unrooted embedding proof, and the full Python/NetworkX boundary as distinct obligations. A theorem about exact integer matching does not silently extend across a cast to floating point or an additional layer of graph-object conversion.

The ordered-tree branch illustrates the same boundary from the other direction. There, the repository has a public indexed Rust theorem, `maximum_common_embedding_indexed_indices`, that proves original ordered-edge indices are unique, in bounds, and associated with an independently maximum ordered contraction under explicit input-size assumptions. That is more than a theorem about score computation. It reaches returned witness identities for a specific source entry point. But it concerns the ordered-tree problem and that indexed reference path; it does not prove the optimized 2016 or 2018 graph backends.

A useful way to organize the full verification project is as a commuting diagram, even if we do not draw one. Along one route, begin with input mathematical trees, pass through the independent common-subtree specification, and arrive at an optimal witness and score. Along another route, encode the input as vectors or graph arrays, execute the actual Rust functions, and decode their returned indices and paths. The proof must establish that both routes describe the same feasible optimal result, within the numerical and error contract of the public API.

The diagram has several edges, and the project has already proved some of them. That is why this repository's theorem inventory is more informative than a yes-or-no label saying 'formally verified.' We can identify a proved standalone matching source contract, a proved mathematical rooted recurrence, a proved reference table, a proved indexed ordered path, and open source-to-optimized-graph bridges. Each one establishes a distinct part of the eventual result.

## What a proof engineer would inspect next

For the matching function, a productive reading order begins at `ResultSpec` rather than at the first line of generated Lean. Understand `Admissible` and `CorrectPartial`; then inspect `max_weight_partial_matching_total_spec` and follow the helper contracts for shape validation, cost construction, assignment, and decoding. Only after you know what those theorems say should you inspect the translated function's detailed control flow.

If your goal were to extend the proof into an optimized 2016 tree solver, I would next isolate one call from a rooted state to its matching-family implementation. Specify the desired child matrix independently, relate actual child-index arrays to that matrix, establish that every query reads only completed descendant states, and use the existing source matching theorem at the call boundary. Then prove that the returned choice information reconstructs exactly the selected child branches. The global tree-optimality argument can reuse the already proved recurrence once these lower-level bridges are in place.

For the 2018 solver, the analogous task is harder because a common-tree edge may traverse paths. Choice reconstruction must preserve the selected skeleton, internally disjoint path realizations, and the rule that a direct-edge reward is earned only when both realized paths are single edges. A source matching theorem can verify the selection of child pairs, but it cannot by itself verify the meaning of a path represented by those pairs.

Source-level cost is yet another question. A program can return a mathematically correct maximum and still take exponential time. The `max_weight_partial_matching_total_spec` theorem speaks about functional behavior and errors, not an asymptotic bound for the complete optimized tree algorithm. Proving such a bound requires a cost model tied to actual operations and an argument for how the recurrence schedule and matching reuse aggregate those costs.

We began with an apparently simple task: show that an implementation of a matching subroutine really computes the mathematical matching optimum. We ended up with a precise chain of representations, validation, arithmetic, choice reconstruction, and source-level control flow. This is the characteristic work of formalizing an implementation. The mathematical theorem says what should be computed. The source theorem says what a particular program does. Between them lies the engineering of a representation relation and enough intermediate lemmas to prove that the two agree.

<!-- END SPOKEN LECTURE -->

## Companion: an end-to-end matching contract in the supplied source

**Snapshot:** `networkx_algo_common_subtree` archive dated 2026-11-19. These are theorem names and abbreviated source excerpts for reading, not claims of new Lean proof contributions.

### The translation boundary

- Maintained Rust source: `rust/crates/verified_assignment_core/src/matching.rs`.
- Pinned extraction/check command: `dev/regenerate_rust_lean.sh --check` (requires the repository's expected toolchain; **not executed** as part of authoring this lecture).
- Generated Lean: `proofs/SubtreeProofs/Rust/Generated/VerifiedAssignmentCore.lean`.
- Source proof: `proofs/SubtreeProofs/Rust/MatchingEntrypoint.lean`.
- Helper proofs: `MatchingValidation.lean`, `MatchingCostConstruction.lean`, `MatchingSolveBuiltMatrix.lean`, `MatchingDecoding.lean`, `MatchingAssignmentBridge.lean`.

### Machine representation versus mathematical specification

| Layer | Concrete objects | Correctness question |
| --- | --- | --- |
| Independent matching | `Finset (Fin n × Fin m)` with `Option ℤ` weights | Does a feasible matching maximize the original signed objective? |
| Rust input | `Slice (Vec (Option I64))` | Is the matrix rectangular, and do size/overflow bounds hold? |
| Internal assignment | Square cost matrix with dummy rows/columns | Does perfect assignment preserve the optimal partial-matching weight? |
| Rust output | `Vec<MatchedPair>` and an `i128` total | Do unique in-range coordinates decode the exact independent optimum and weight? |
| Source proof | `matching.max_weight_partial_matching ... ⦃ output => ResultSpec ... ⦄` | Does the *translated actual function* always satisfy the success-or-rejection specification? |

In `MatchingEntrypoint.lean`:

```lean
def Admissible (weights : Slice (alloc.vec.Vec (Option I64))) : Prop :=
  Rectangular weights (width weights).val ∧
  weights.length+(width weights).val ≤ U32.max ∧
  weights.length+(width weights).val < Usize.max

def ResultSpec (weights : Slice (alloc.vec.Vec (Option I64)))
    (output : core.result.Result matching.PartialMatching matching.MatchingError) : Prop :=
  match output with
  | .Ok result => Admissible weights ∧ CorrectPartial weights ... result
  | .Err error =>
    (error = .NonRectangular ∧ ¬ Rectangular weights ...) ∨
    (error = .TooLarge ∧ Rectangular weights ... ∧ sizeViolation)
```

`sizeViolation` in the abbreviated excerpt stands for the source's explicit disjunction of `U32.max` and `Usize.max` size violations. The source spells out both conditions; the ellipses above are not runnable Lean.

```lean
theorem max_weight_partial_matching_total_spec (weights : Slice (alloc.vec.Vec (Option I64))) :
    matching.max_weight_partial_matching weights ⦃ output => ResultSpec weights output ⦄
```

`max_weight_partial_matching_spec` derives successful exact-optimal output for admissible inputs. `MatchingSolveBuiltMatrix.CorrectPartial` includes list uniqueness, correspondence with a finite set of original coordinates, independent `WeightedMatching.IsMaximum`, and equality of the returned weight to the mathematical sum.

### Worked 2 × 3 input

| Original left row | Right 0 | Right 1 | Right 2 |
| --- | ---: | ---: | ---: |
| 0 | 7 | forbidden | −4 |
| 1 | 6 | 5 | forbidden |

The optimum is `{(0,0),(1,1)}` with weight `12`. A valid output cannot contain a dummy assignment coordinate, a forbidden pair, or a duplicate row/column. A matrix with a second row of different length is a `NonRectangular` rejection. A present negative weight is not a forbidden edge.

### Boundaries that remain separate

- The source matching theorem covers an **exact signed-integer partial-matching API** under a stated shape/size contract. It is not an IEEE-754 `f64` theorem.
- `Droschinsky2016/RootedDynamicProgram.lean` and `Droschinsky2018/RootedDynamicProgram.lean` prove reference score evaluators against independent tree optima; they do **not** establish equivalence to all production graph-source calls.
- `Rust/IndexedOrderedEntrypoint.lean` proves original-edge position invariants for a **different**, ordered-tree entry point; this does not bridge unordered subtree isomorphism or topological embedding.
- The pinned Droschinsky statement crosswalk leaves optimized unrooted structural/schedule correctness, native floating-point behavior, production witness reconstruction, and global source-time/space complexity open.

### Reading exercises

1. Why does the return type `Result` require proving the error cases, rather than assuming that the matching algorithm always returns a matching?
2. For the example, show that adding the permitted edge `(0,2)` of weight −4 cannot improve a maximum partial matching. Why would the argument differ for a *perfect* matching?
3. Locate the `DecodedPrefix`-style loop invariant in `MatchingDecoding.decode_pairs_spec`. What would fail if a dummy column were returned unchanged as a right input index?
4. Find the exact theorem boundary at which a real Rust function is shown to return the independent `WeightedMatching.IsMaximum` witness. Which additional representation theorem would the optimized tree solver need in order to invoke that result for its child-pair matrix?

**Broader source trail:** `proofs/README.md`, `proofs/VERIFICATION.md`, `docs/planning/paper_statement_crosswalk.md`, `docs/planning/droschinsky_2016_2018_verified_rust_lean.md`, and the maintained Rust/Lean files named above. Prerequisite lectures: `012000`, `022000`, `024000`; optional Lean foundations: `logic-types:005000`–`008000`.
