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
