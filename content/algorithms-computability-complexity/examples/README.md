# Executable companion — lower-bound search

`lower_bound_reference.py` checks a hand-coded lower-bound routine against an
independent linear-scan specification over *all* nondecreasing integer arrays
of length 0 through 8 using values from `[-2,-1,0,1,2]`, and targets from -3
to 3. It also checks the returned partition and a comparison-count bound.

```bash
python content/algorithms-computability-complexity/examples/lower_bound_reference.py --check
```

The result is a bounded test of the Python implementation, not a proof for
unbounded inputs and not a formally verified Lean theorem. The separate
mathematical correctness proof appears in lecture 003000.

## Finite-trace reduction and dovetailing lab (Lectures 004000–006000)

Run `python content/algorithms-computability-complexity/examples/finite_reductions_lab.py --check` to demonstrate accept/reject/loop distinctions, two total source-to-source instruction transformations, and fair scheduling of complementary recognizers. The interpreter uses a toy one-counter instruction language. An `UNKNOWN` result means only that a finite simulation budget has run out; neither this interpreter nor its checks decide general halting or prove Rice's theorem. Original Python reference implementation; no binary assets.

## Finite automata, stacks, and parsing lab (Lectures 007000–009000)

Run `python content/algorithms-computability-complexity/examples/automata_and_grammars_lab.py --check`.
This uses only the standard library. The DFA vs NFA comparison, product
closure, finite shortest-witness search, finite nonregularity witnesses,
CYK table, stack recognizer, independent recursive-parentheses specification,
and ambiguity counts are checked on bounded inputs. For a CNF grammar on a
fixed input, the CYK procedure terminates; this lab does not generalize its
checks to all grammars or inputs and is not a Lean/Isabelle proof.


## Selection, dynamic programming, and greedy scheduling (010000–012000)

Run `python content/algorithms-computability-complexity/examples/algorithm_design_lab.py --check`.
The code checks rank selection against sorting on small sequences, weighted
interval DP against exhaustive compatible-subset enumeration, and earliest-finish
greedy against the same independently evaluated maximum cardinality.
Counterexamples distinguish the wrong heuristic, wrong objective, and correct
algorithm. Results are finite implementation checks, not proof of linear-time
selection or all-input optimality; the mathematical proofs are in the lecture
manuscripts. No package dependencies or binary inputs.
