# Numerical Analysis and Reliable Computation

The course begins with a question: **what, exactly, can a computed answer certify?** It separates mathematical specification, measurement and model uncertainty, numerical approximation, and arithmetic effects before building practical algorithms.

## Available lectures

- 001000 — When to Trust a Computed Answer: Models, Data, Approximation, and Tolerances
- 002000 — Small Errors, Large Consequences: Rounding and Error Propagation
- 003000 — Conditioning: When the Problem Amplifies Small Errors
- 004000 — Backward Error: Which Nearby Problem Did the Algorithm Solve?
- 005000 — Finding Roots: Brackets, Newton's Method, and Honest Stopping Rules
- 006000 — Linear Algebra in Finite Precision: Pivoting, Conditioning, and Residuals
- 007000 — Convergence and Error Certificates: Knowing When to Stop

Each numbered manuscript has exactly one spoken region between `BEGIN SPOKEN LECTURE` and `END SPOKEN LECTURE`. Exact equations, theorem statements, exercises, and references appear in display-only companions. The numbering intentionally retains the original `002000` lecture without modification.

The `001000` entry is a **new composition**, not recovery of a lost original: no copy was found in the supplied Git history. The catalog lists only present, readable manuscript files. Individual lecture metadata and a track bibliography live under `metadata/`.

This course emphasizes independently checked examples, explicitly scoped guarantees, and the distinction among conditioning, algorithm stability, residuals, and forward error. Later extensions may treat iterative linear algebra, interpolation and quadrature, ODE discretization, interval verification, and error-aware scientific workflows when they add real conceptual depth.
