# Executable companion — lower-bound search

`lower_bound_reference.py` checks a hand-coded lower-bound routine against an
independent linear-scan specification over *all* nondecreasing integer arrays
of length 0 through 8 using values from `[-2,-1,0,1,2]`, and targets from -3
to 3. It also checks the returned partition and a comparison-count bound.

```bash
python draft-stages/tts-algorithms-computability-complexity/examples/lower_bound_reference.py --check
```

The result is a bounded test of the Python implementation, not a proof for
unbounded inputs and not a formally verified Lean theorem. The separate
mathematical correctness proof appears in lecture 003000.

## Finite-trace reduction and dovetailing lab (Lectures 004000–006000)

Run `python draft-stages/tts-algorithms-computability-complexity/examples/finite_reductions_lab.py --check` to demonstrate accept/reject/loop distinctions, two total source-to-source instruction transformations, and fair scheduling of complementary recognizers. The interpreter uses a toy one-counter instruction language. An `UNKNOWN` result means only that a finite simulation budget has run out; neither this interpreter nor its checks decide general halting or prove Rice's theorem. Original Python reference implementation; no binary assets.
