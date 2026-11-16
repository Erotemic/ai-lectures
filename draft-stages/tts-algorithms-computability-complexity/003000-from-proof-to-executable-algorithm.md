# From Mathematical Proof to Executable Algorithm

**Track:** Algorithms, Computability, and Complexity  
**Lecture:** 003000 — Specification, Refinement, Verification  
**Assumed background:** Arrays, sorted order, binary search, and mathematical induction.  
**Companion:** Hoare-style proof, reference implementation, bounded exhaustive checks, and a refinement checklist.

<!-- BEGIN SPOKEN LECTURE -->

Consider a routine with a reassuring name: binary search. You call it on a sorted array, it returns an index, and a hundred unit tests pass. Now a second programmer changes the implementation so that it handles duplicate keys differently. Are you still running the same algorithm? Did the change preserve correctness? The answer depends on a question that should have been settled before either programmer wrote a line of code: what exactly was the routine required to return?

Let's make that question precise. We are given an array whose elements are in nondecreasing order, and a target value. Our goal is not merely to find some matching element. It is to return the earliest position at which the array element is greater than or equal to the target. If no such position exists, return the array's length. This operation is commonly called a lower-bound search. It handles absent targets and duplicate values in a particularly useful, deterministic way.

Take the array one, two, two, five. If the target is two, the answer is position one, counting from zero, not position two. If the target is three, the answer is position three, even though the value three is not present. If the target is six, the answer is position four, the length of the array. For an empty array the answer is zero. These examples are not extra rules layered on afterward. They are consequences of one specification.

A concise mathematical description says that the answer is the smallest index where the predicate 'array entry is at least the target' becomes true, or the array length if it never becomes true. Sortedness makes this predicate monotone: once the predicate becomes true at a position, it remains true at every later position. That monotonicity is precisely the information binary search exploits.

Now design the state. We keep two integer boundaries, low and high. Initially low is zero and high is the array length. The interval from low, inclusive, to high, exclusive, contains the position where the boundary between smaller and not-smaller may occur. At every step we pick the middle index. If the middle entry is less than the target, the answer must lie strictly to the right of that index, so we set low to middle plus one. Otherwise the middle entry is at least the target, so it is still a candidate; we set high to middle.

The procedure stops when low equals high and returns that value. You may have seen versions of binary search that return as soon as an equal value is found. That version can solve a different specification—find any match—but it cannot, without more work, guarantee the first matching position. The exact return rule is a design choice with mathematical consequences.

How do we prove our version correct? Here is the key. At all times, every position strictly before low contains an element less than the target. And every position at or after high contains an element greater than or equal to the target. We also maintain zero less than or equal to low, low less than or equal to high, and high less than or equal to the array length. These are the loop invariants.

Before the first iteration, low is zero and high is the array length. There are no positions before zero and none beyond the array length. Both assertions are true without inspecting a single element. That is the base case.

Now assume the assertions hold at the beginning of an iteration, and low is strictly less than high. The middle index is at least low and strictly less than high, so it is a valid array position. If its value is below the target, sortedness tells us that every preceding value is below the target too. By setting low to middle plus one, we enlarge the region already known to be too small. The claim about values beyond high does not change.

In the other branch, the middle entry is at least the target. Sortedness tells us that every later entry is at least the target. Setting high to middle expands the region known to be large enough. The claim about entries before low remains true. In either branch the invariant is preserved. We have an inductive proof, not an inference from a set of lucky test cases.

But again, partial correctness is only half the story. Why must the loop stop? The difference between high and low is a nonnegative integer. Whenever low is below high, the algorithm chooses a middle index in that interval. In the first branch low increases to at least low plus one. In the second branch high decreases to at most high minus one. The interval becomes strictly shorter. A nonnegative whole number cannot decrease indefinitely, so the loop terminates.

At termination low equals high. Every earlier entry is too small, and every entry at or beyond that index is large enough. There is exactly one position satisfying those two conditions: the first large-enough index, or the array length if there is none. The algorithm therefore returns the required lower bound, including in the cases involving duplicates, missing values, and empty inputs.

This is what it means to derive a procedure from a specification. The specification tells us the answer we want. The invariant describes the information the state carries. The update rule preserves that information. A decreasing measure proves progress. The terminal condition turns the preserved information into the requested answer.

There is a historical lineage to this style of reasoning, but it should be attributed carefully. Robert Floyd's nineteen sixty-seven paper, 'Assigning Meanings to Programs,' develops assertions associated with program control flow and discusses proving termination by a decreasing quantity. C. A. R. Hoare's nineteen sixty-nine paper, 'An Axiomatic Basis for Computer Programming,' develops axiomatic reasoning about programs. These are foundational sources for program verification. Our particular lower-bound invariant is a modern teaching derivation, not a claim that either author invented this precise example.

We can now translate the method into code. In Python, the main loop fits into a few lines. Store the array's length in high. While low is smaller than high, compute the midpoint using integer division. Compare the middle entry with the target. Move low past that entry if it is too small; otherwise move high down to the middle. Return low. The version supplied in the companion runs exactly those steps and includes a separate, intentionally simpler specification function for checking results.

I want to be precise about the difference between the proof and that checking code. The proof makes a statement about all nondecreasing arrays over an appropriately ordered domain and assumes exact arithmetic for the boundaries. The executable checker enumerates many small arrays and compares the optimized routine with a direct scan. That is a strong regression test for these instances, and it can catch accidental edits. But it is not an exhaustive proof over arrays of arbitrary length or arbitrary values.

The implementation language also changes our obligations. In Python, integer values grow as needed, so calculating low plus high has no fixed-width integer overflow. In a language where the index type has a maximum value, computing the midpoint as low plus high, divided by two, can overflow before the division occurs. A safer expression is low plus half of high minus low, provided the intermediate arithmetic and bounds are valid. Joshua Bloch reported in two thousand six that a long-standing Java binary search implementation and a version discussed in Jon Bentley's work shared an overflow problem. The moral is not that mathematical proofs are useless; it is that a proof about unbounded integers is not automatically a proof about bounded machine arithmetic.

There are other gaps between model and implementation. A Python list supports indexed access under the usual runtime model; a streamed file does not. A comparator that says one value is less than another must have the ordering properties assumed in the proof. A floating-point value such as NaN can defeat the ordinary picture of a total numeric order if one naively uses less-than comparisons. A memory access might throw an exception. An index conversion might narrow an integer. A concurrent thread might mutate the array while the search runs. Each situation challenges an assumption, and each requires either a stronger contract or a changed implementation.

That is why a useful proof should state its *precondition* as well as its *postcondition*. The precondition here is not merely 'give me an array.' It includes a fixed sequence whose entries are sorted by the same consistent total order used in comparisons. The postcondition is not merely 'return some integer.' It gives a bound on the index and two universal properties of the entries on either side. If the precondition fails, our theorem does not apply. We may choose to detect certain invalid inputs, but checking sortedness in linear time would change the cost profile of a supposedly logarithmic operation.

The distinction between what a program does and what it promises also helps with software interfaces. If a library returns 'any matching index' rather than 'the first matching index,' clients must not rely on leftmost behavior just because one implementation happens to exhibit it. Conversely, if the public specification promises a lower bound, a faster replacement must preserve the property even if it uses a completely different internal strategy. A good contract allows implementation freedom while preserving observable meaning.

How does this lead to machine-checked proofs? One route is to define the mathematical specification inside a proof assistant, write the implementation in the assistant's functional language, and prove the implementation returns the specified result. Another route is to verify a higher-level algorithm and connect it through a refinement chain to the executable language and machine model. In Lean, for example, inductive definitions, recursive functions, and well-founded recursion provide ways to express computations whose termination obligations are explicit. A theorem can then establish that the function meets a mathematical specification.

But do not mistake a formal-looking snippet for a verified result. A Lean theorem proves the statement actually elaborated and checked by the kernel, using its stated assumptions and definitions. It does not certify an unrelated Python or Rust routine because their names resemble the definitions. A verified bridge requires a correspondence theorem, a trusted or verified translation, or a clearly justified relationship between the models. The companion to this lecture deliberately includes an executable Python reference and a human-level proof; it does not pretend to contain a compiled Lean proof that we have not checked.

There is one more dimension: complexity. Every iteration reduces the candidate interval by approximately half. Starting from n elements, the interval becomes empty after at most about the base-two logarithm of n plus one comparisons, with details depending on the exact boundary convention. If the array uses constant-time random access and each comparison has constant cost, the comparison and time bounds are logarithmic. A proof of correctness and a proof of efficiency have different logical conclusions, though both can use the same decreasing interval.

And there is a third conclusion still beyond our proof. Even if binary search has logarithmic worst-case comparison cost, we have not shown that no better algorithm exists in every possible computational model. A lower bound for ordered searching under specific comparison assumptions is a different kind of theorem from this upper bound. We should keep these obligations separate even when they appear together in one library function.

Here is a useful exercise for engineering judgment. Suppose you are writing a lower-bound routine for a large codebase, and a colleague proposes replacing it with a highly optimized version. Ask them to state the same precondition and postcondition. Ask whether duplicates, empty inputs, out-of-range targets, integer widths, ordering semantics, and concurrent mutation are handled consistently. Ask what the new cost model assumes. Then design tests that target exactly the points where the proof or refinement argument could fail. This is not ceremony. It is how to make an implementation faster without quietly solving a different problem.

The same methodology scales to dynamic programming, graph algorithms, balanced trees, numerical algorithms, and proof-driven code generation. A proof for an abstract graph function is valuable; proving that an optimized adjacency representation implements that graph is a further step. A complexity bound for an abstract map operation is valuable; accounting for memory allocations and hashing behavior is another. Elegant software architecture often means making these boundaries explicit enough that one component can change without invalidating the reasoning about the others.

We began with a tiny searching routine. It led us through an exact specification, a loop invariant, an argument for termination, a cost analysis, implementation hazards, and the limits of formal verification. That sequence is the backbone of trustworthy algorithm design. The challenge is not only to write instructions that appear to work. It is to know what they mean, why they work for every admissible input, how the meaning survives translation into code, and which parts of that claim we have actually established.

<!-- END SPOKEN LECTURE -->

## Formal companion — not narrated

### Mathematical contract

Let `A` be a finite sequence of length `n` over a fixed total order, sorted nondecreasingly. For target `x`, define

\[
\operatorname{lowerBound}(A,x)=\min\bigl(\{i\in\{0,\ldots,n-1\}:x\le A[i]\}\cup\{n\}\bigr).
\]

The output `k` must satisfy

\[
0\le k\le n,\quad
(\forall i<k,\ A[i]<x),\quad
(\forall j,\ k\le j<n\Rightarrow x\le A[j]).
\]

This postcondition uniquely identifies the result for sorted `A`.

### Human-level total correctness proof

Pseudocode:

```text
lo := 0
hi := length(A)
while lo < hi:
    mid := lo + (hi - lo) // 2
    if A[mid] < x:
        lo := mid + 1
    else:
        hi := mid
return lo
```

Invariant `I(lo,hi)`:

1. `0 ≤ lo ≤ hi ≤ n`;
2. every `i < lo` satisfies `A[i] < x`;
3. every `hi ≤ j < n` satisfies `x ≤ A[j]`.

**Initialization:** both quantified regions are empty.

**Preservation:** `lo ≤ mid < hi` when `lo < hi`. If `A[mid] < x`, sortedness gives `A[i] < x` for each `i ≤ mid`; otherwise sortedness gives `x ≤ A[j]` for each `j ≥ mid`. All bounds remain valid.

**Termination:** `hi-lo` is a natural-number variant. If the condition is true it strictly decreases in either branch.

**Postcondition:** at exit `lo=hi=k`; the last two invariant clauses are precisely the desired partition.

**Cost:** worst-case comparisons `O(log(n+1))` under random access and constant-cost comparisons. For `n=0`, zero array comparisons; the `n+1` form avoids an undefined logarithm at zero.

### Implementation and checking

The file `examples/lower_bound_reference.py` is a standard-library implementation plus independent direct-scan specification and bounded enumeration. Run:

```bash
python draft-stages/tts-algorithms-computability-complexity/examples/lower_bound_reference.py --check
```

This tests the *implementation* but is not a machine-checked theorem. No Lean project or theorem is included or claimed to have been checked.

### Evidence map

- **Robert W. Floyd, “Assigning Meanings to Programs” (1967)**, *Proceedings of Symposia in Applied Mathematics* 19, pp. 19–32: control-flow assertions, correctness, termination measures. [Bibliographic record](https://doi.org/10.1090/psapm/019/0235771).
- **C. A. R. Hoare, “An Axiomatic Basis for Computer Programming” (1969)**, *Communications of the ACM* 12(10), pp. 576–580, 583: axiomatic rules for program properties. [Original paper](https://doi.org/10.1145/363235.363259).
- **Erik Demaine, Jason Ku, Justin Solomon, MIT 6.006 Spring 2020**, Lecture 1: specification, correctness, efficiency, inductive arguments. [MIT lecture notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf).
- **Joshua Bloch, “Extra, Extra — Read All About It: Nearly All Binary Searches and Mergesorts Are Broken” (2006)**: specific overflow failure in binary search and relation to a source-level proof. [Original author blog](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/).
- **Jeremy Avigad, Leonardo de Moura, Soonho Kong, Sebastian Ullrich, *Theorem Proving in Lean 4***, Chapter 8: inductive types and recursion. [Lean book](https://lean-lang.org/theorem_proving_in_lean4/Induction-and-Recursion/).

### Refinement obligations for a real implementation

- Define sortedness, total order, and mutation policy.
- Specify index type and out-of-range behavior.
- Preserve the loop invariant under actual integer arithmetic, not an idealization that ignores overflow.
- Ensure array indexing is valid in every iteration, including `n=0`.
- Separate correctness of an abstract model from the trusted connection to native code.
- State any performance assumptions (random access, comparator complexity, allocation and cache behavior).

### Questions to carry into the next lecture

1. How would the postcondition change if the routine must return the last index satisfying `A[i]≤x`?
2. What fails if the input is not sorted?
3. Where exactly is a proof required for a Rust port using `usize` indices?
4. Can the same contract be implemented without branch-based binary search?
5. What would constitute a real formal proof of the *executable* code, rather than proof of a similar mathematical function?
