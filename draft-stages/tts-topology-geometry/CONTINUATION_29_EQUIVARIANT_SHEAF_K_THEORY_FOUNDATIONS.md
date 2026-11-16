# Continuation 29 — Equivariant, Sheaf and K-Theory Foundations

**Date:** 2026-11-16. **Status:** 15 newly authored and registered lectures; 96 to 111 total. All earlier manuscripts remain byte-identical. New files, metadata and catalog changes are within `draft-stages/tts-topology-geometry` only.

## Purpose and dependency bridge

| New lecture | Concrete calculation or construction | Earlier advanced destination |
| --- | --- | --- |
| 018200 | Grothendieck group of bundle isomorphism classes, rank and tensor products | 024000, 040000 |
| 018300 | O(1)−1 on CP¹; K⁰(S²) and β²=0 | 040000 |
| 018400 | ch(O(1)) and ch(O(1)−1) on CP² | 024000, 036000, 040000 |
| 018500 | Dolbeault χ(O(k))=k+1, Todd correction and K pushforward | 024000, 040000 |
| 020300 | Borel quotient for a point, free circle, trivial action | 025000 |
| 020400 | d_T(dt)=−u on a free circle; d_T(ω+uμ)=0 | 021000, 025000 |
| 020500 | Tangent weights ±1 and localization of 1/e_T on S² | 025000, 029000 |
| 020600 | Full CP¹ fixed-point data, ∫x=1, ∫x²=−u and ring relation | 025000, 029000 |
| 020700 | Uniform pushforward under μ=cosθ/2 and exponential ABBV integral | 021000, 025000 |
| 022200 | Constant presheaf counterexample and local primitive obstruction | 040000 |
| 022300 | Cech C⁰=R²→C¹=R² on circle, H¹=R | 025000, 040000 |
| 022400 | Global logarithm obstruction via sheaf exponential sequence | 040000 |
| 022500 | h⁰(O(k)), h¹(O(k)) via Laurent powers, all k | 024000, 040000 |
| 022600 | Fine de Rham/Dolbeault resolutions and H^q(O(E)) | 020000, 024000, 040000 |
| 039100 | E=1→F=O(1): index −β and det index O(−1) | 040000 |

## Exactness, grading and sign conventions

- Complex topological K-theory uses `K⁰(X)` as the Grothendieck ring of complex vector bundles; the Bott class on `S²≈CP¹` is `β=[O(1)]−[1]`, giving `K⁰(S²)=Z[β]/(β²)`.
- The Chern character has rational coefficients. The integer Dolbeault index for `O(k)` on `CP¹` is `χ(O(k))=∫ch(O(k))Td(TCP¹)=k+1` for all integers k. It is *not* generally the integral of `ch(O(k))` alone.
- For period-one `S¹` actions and real equivariant cohomology, `|u|=2` and `d_T=d−uι_X`; hence `d_T²=−uL_X` and `ω+uμ` is closed under `ι_Xω=dμ`.
- On `CP¹`, action `[Z0:Z1]↦[Z0:e^{2πit}Z1]` gives tangent weights +1 at `[1:0]` and −1 at `[0:1]`. With the natural dual tautological lift, `x=c₁^T(O(1))` restricts as `(0,−u)`. This yields `H_T^*(CP¹)=R[u,x]/(x(x+u))` and the stated integrals.
- Normalize `ω=(1/(4π))sinθ dθ∧dφ`, `X=2π∂φ`, `μ=cosθ/2`, `∫ω=1`. Then `ω+uμ=x+u/2` in equivariant cohomology and the ABBV exponential agrees with the direct uniform-moment calculation.
- For a cover to compute derived sheaf cohomology by a Čech complex, appropriate acyclicity of all nonempty finite intersections is required; the particular S¹ and Stein CP¹ covers meet that requirement for the sheaves used.
- The family in 039100 has index K-class `[E]−[F]=−β` with determinant line `det ker⊗det coker*=O(−1)`. The *ordinary determinant of the family of linear maps* is a section of the **dual** line `O(1)`, where its single zero has positive local multiplicity. This distinction prevents a sign error.

## Boundaries of the new manuscripts

- Bott periodicity, full index theorem, ABBV for nonisolated fixed components, Cartan/Borel comparison and general coherent-sheaf acyclicity are stated with their hypotheses and sources; the manuscripts do not claim to prove those deep general theorems from scratch.
- The 039100 finite-dimensional model illustrates an index bundle and determinant line, not Quillen metrics or the curvature formula for actual infinite-dimensional elliptic families.
- Original Topology and Geometry lecture 032000 retains the separately identified Floer action sign issue; the new installment makes no modification to it.
- No minimum, maximum or target spoken length is applied. Word counts in `track.json` are descriptive, extracted from actual spoken regions.

## Scholarly anchors

Atiyah and Bott (1984), Duistermaat and Heckman (1982), Atiyah and Singer (1971), Bismut and Freed (1986), Hatcher's openly hosted K-theory text, Vakil's sheaf notes, the Stacks Project's Čech-to-derived comparison, and Bott and Tu supply the main structural references. Exact URLs are recorded in `metadata/sources.json`, with roles identified in each per-lecture sidecar and relevant Wikipedia links included in each manuscript.

## Further foundation needs

Contact/ Reeb dynamics and Liouville ends before wrapped Floer and ECH; careful Floer orientation/finite-energy methods; and elementary spectral-sequence computations. Treat these as proposals, not registered lectures.
