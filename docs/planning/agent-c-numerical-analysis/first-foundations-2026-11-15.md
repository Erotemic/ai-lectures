# Agent C — numerical-analysis foundations recovery and first arc

## Source and recovery status

November 15 synced baseline `90c123b` contains the standalone `002000-rounding-and-error-propagation.md` and its metadata. The manifest deliberately excluded `001000` because no source manuscript was present. A search of supplied Git history found no tracked `draft-stages/tts-numerical-analysis/001000-*` file; this overlay **authors new 001000 content**, not a purported restoration. The 002000 manuscript and sidecar remain unchanged.

## Completed coherent arc

| ID | Mathematical question | Distinction or guarantee |
|---|---|---|
| 001000 | When is a computed number trustworthy? | Separates model/data/discretization/iteration/rounding uncertainties; residual is not forward error |
| 002000 | What does floating point actually do? | Existing lecture, retained unchanged; standard relative rounding model and stable summation |
| 003000 | Is the exact problem sensitive? | Scalar and matrix condition numbers; near-multiple root counterexample |
| 004000 | Does the algorithm solve a nearby problem? | Backward error definitions and linear-system residual formula; stable quadratic roots |
| 005000 | How do we solve and certify a nonlinear equation? | Bisection enclosure; local Newton convergence and multiple-root counterexample |
| 006000 | How do we solve linear systems reliably? | Pivoting, matrix growth, condition and residual; QR versus normal equations |
| 007000 | What does stopping certify? | Trapezoid error theorem, contraction a posteriori bound, mixed error budget |

No duration or word-count acceptance threshold was used. Each new file contains a spoken lecture, a display-only mathematical companion, worked examples, and exercises with answers. The original course source catalog now includes SIAM monographs, MIT OpenCourseWare and publisher records. Sidecars point to those sources; historical claim anchors are recorded where the text makes a historical attribution.

## Independent calculation checks

- `001000`: exact endpoint squares verify the stated enclosure for sqrt(2); the multiple-root residual exponent is correct.
- `003000`: for the two-equation near-dependency example, changing the second right-hand side by delta * eta changes the solution from (1,1) to (1-eta,1+eta).
- `004000`: the product of the two roots of x^2+10^8*x+1 is 1; a cancellation-prone direct formula can return 0 for the small root in binary64, while the product-based method recovers roughly -10^-8.
- `005000`: the Newton rational iterates from 3/2 are 17/12, 577/408 and 665857/470832; bisection from [1,2] produces midpoint error at most 2^(-n-1) after n exact halvings.
- `006000`: the tiny-pivot matrix has 2-norm condition about 2.618; naïve elimination without pivoting on the given binary64-scale coefficients produces an incorrect first component, while the row-pivoted solve gives approximately (1,1).
- `007000`: exact arithmetic yields composite trapezoidal T_n(x^2,[0,1])=1/3+1/(6*n^2); the contraction T(x)=(x+2)/3 has error certificate equal to 1/27 at x=26/27.

These computations independently check the illustrative numbers, not the correctness of every symbolic step. Relevant mathematical hypotheses are stated in the display companions and audit checks.

## Next gaps, rather than a lecture quota

The numerical-analysis track now has a usable first arc. The next handoff priorities should be **logic-types** (identity types, transport, dependent pattern matching, semantics) and **optimization-duality** (convex conjugates and duality, constraint qualifications, algorithms, gaps). For future numerical-analysis expansion, eigenvalue sensitivity, Krylov convergence with preconditioning, integration of stiff ODEs, verified intervals, and error-aware discretization would be meaningful, but must be developed from explicit questions and examples instead of an arbitrary target count.

## Ownership and application

Only `draft-stages/tts-numerical-analysis/**` and `docs/planning/agent-c-numerical-analysis/**` are in this ZIP. Apply to the synced November 15 baseline using `tools/apply_track_overlay.py c` and run `tools/lecture_inventory.py` before a scoped commit. Do not edit G2/G3, shared code, tests, or other owners' tracks.
