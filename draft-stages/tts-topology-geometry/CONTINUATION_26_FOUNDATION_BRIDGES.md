# Continuation 26: Foundations for Advanced Geometry

Date: 2026-11-16. Status: fourteen substantive, registered lectures added to the Topology and Geometry track. This installment is a continuation of the reconstructed Continuation 25, not a replacement for it. The track now contains 68 registered manuscripts.

## Why these additions

The 008000–013300 foundation sequence establishes the language of manifolds, forms, integration, and connections. Existing advanced lectures 014000–042000 use deeper computational and analytic techniques. This installment fills fourteen prerequisite gaps in place, with self-contained spoken narrations, non-spoken exact mathematics, worked exercises, and references.

| New ID | Primary worked material | Direct later payoffs |
| --- | --- | --- |
| 014100 | Polar/spherical metric coefficients, Christoffel symbols, geodesics | 014000, 017000, 035000 |
| 014200 | Jacobi equation, curvature and conjugate points | 014000, 023000, path-space Morse theory |
| 015100 | Chain complexes, exactness, relative pairs, torsion | 015000, 016000, 032000 |
| 015200 | Circle/sphere Mayer–Vietoris and torus cellular homology | 015000, 016000, 020000 |
| 016100 | Torus cohomology ring and oriented intersections | 016000, 039000, 042000 |
| 017100 | Geodesic triangles, curvature integration, boundary terms | 017000, 018000, 022000 |
| 018100 | Complex line clutching, Chern/Euler classes, real versus integral | 018000, 022000, 027000, 036000 |
| 019100 | Regular values, signed preimages, degree and fixed points | 019000, 023000 |
| 020100 | Hodge star, codifferential, Laplacian and explicit torus forms | 020000, 024000, 031000 |
| 020200 | Principal symbols, ellipticity, Fredholm alternative, index | 020000, 024000, 035000, 040000 |
| 021100 | Symplectic/Hamiltonian calculations and sphere rotation | 021000, 027000, 032000, 034000 |
| 022100 | Gauge laws, curvature, flat circle holonomy | 022000, 026000, 031000, 041000 |
| 023100 | Hessian indices, gradient trajectories and Morse chain complex | 023000, 025000, 032000 |
| 024100 | Elliptic de Rham operator, harmonic forms, Euler index | 024000, 040000, 041000 |

## Mathematical guardrails

- Christoffel coefficients depend on coordinates; curvature does not. A geodesic may not be globally minimizing. Jacobi fields are infinitesimal variation fields, not exact large-distance separations.
- Integral homology detects torsion, which vanishes after passing to real de Rham cohomology. Mayer–Vietoris uses the actual maps, not just dimensions. Signs in intersection pairings depend on orientation conventions.
- Gauss–Bonnet on a surface with boundary includes geodesic curvature and corner turning. Pointwise curvature need not have a fixed sign when its integral has one.
- Unitary line connection convention follows Continuation 25: `nabla = d + A`, `F = dA + A wedge A`, and `c1 = [iF/(2pi)]`. Complex clutching degree and Chern number use a compatible sphere orientation; reversing orientation reverses the signed number.
- Hodge decomposition and elliptic Fredholmness here require smooth compact manifolds without boundary unless a lecture explicitly supplies the needed boundary/domain conditions. Ellipticity does not imply invertibility.
- Hamiltonian convention is `i_{X_H} omega = dH`, with `omega = sum dq wedge dp`; this fixes the signs in Hamilton's equations and the sphere moment-map example.
- For gauge transformations, `A^g = g^{-1}Ag + g^{-1}dg`, `F^g = g^{-1}Fg`. Holonomy transforms by conjugation, and can be nontrivial even with zero curvature on a circle.
- The de Rham parity operator index equals Euler characteristic; the spin/spin-C Dirac operator has a different index formula. The Morse boundary squared equals zero only after necessary transversality and compactness arguments.
- Spoken narration uses words rather than inline mathematical LaTeX; exact notation, source references, and exercises are in non-spoken companions.
- No fixed word-count or duration targets were used. Manifest duration fields are descriptive measurements only.

## Sources

Scholarly reading is indexed under `metadata/sources.json` and linked from each `metadata/<id>.json` sidecar. Relevant foundational sources include Allen Hatcher's *Algebraic Topology* and *Vector Bundles and K-Theory*, MIT 18.965/18.950 manifold and differential geometry notes, University of Toronto's symplectic and Morse theory notes, Moore and Schnell's Hodge materials, and Notre Dame's notes on elliptic Fredholm operators. Each manuscript also includes relevant Wikipedia overview links.
