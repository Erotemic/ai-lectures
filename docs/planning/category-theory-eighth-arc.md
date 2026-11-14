# Category Theory, eighth arc — Higher composition and derived geometry

This addition extends the established `category-theory` audio track from 30 to 34 lectures without changing its identifier or earlier manuscripts. Each lecture has its own spoken region, mathematical companion, worked calculation, reading sidecar, and source anchors. The order is conceptual rather than historical; each can be listened to independently with the listed mathematical background.

## Lectures

| ID | Lecture | Worked mathematical anchor | Prerequisites |
| --- | --- | --- | --- |
| 031000 | Infinity-Categories: When Composition Has More Than One Witness | Two-dimensional inner horn, nerve of ordinary category, mapping space and homotopy category | Categories, nerves, homotopies |
| 032000 | Homotopy Limits: Why a Pullback Can Contain Loops | `* ×^h_{S¹} * ≃ ΩS¹ ≃ ℤ` versus strict single-point pullback; homotopy pushout of two points over `S⁰` | Pullbacks, paths, higher mapping spaces |
| 033000 | Infinity-Operads: Algebraic Laws with Room to Deform | `E₁(2) ≃ S⁰`, `E₂(2) ≃ S¹`, `E₃(2) ≃ S²`; finite pointed sets | Operads, monoidal categories, homotopy |
| 034000 | Derived and Higher Stacks: What an Intersection Can Remember | `Tor₁^{k[x]}(k,k) ≅ k` for self-intersection of the origin; transverse coordinate axes comparison | Tensor products, free resolutions, sheaves/stacks |

## Editorial and mathematical precautions

- **Infinity-categories:** Inner-horn fillers need not be unique; do not conflate a raw filler set with the contractible choices arising in appropriate universal properties. Ordinary categories have uniquely filled inner horns; Kan complexes have all horn fillers.
- **Homotopy limits:** A path-space pullback records paths, and the fiber over a basepoint of `S¹` is `ΩS¹`, with components indexed by winding number. A plain homotopy category does not in general determine the homotopy limits of an enhancement.
- **Infinity-operads:** The symmetry action does not imply strict commutativity. The distinction among `E₁`, `E₂`, `E₃`, and `E∞` comes from operation spaces and their coherences. The pointed-finite-set model also needs lifting and mapping-space axioms.
- **Derived geometry:** Distinguish the underived ring `k ⊗_{k[x]} k = k` from the derived tensor product with nontrivial Tor in degree one. The derived self-intersection is relative to the ambient line. A space-valued derived sheaf needs additional representability hypotheses to be geometric.

## Sources and validation

Research records include Kerodon, Dugger, May, Lurie, Toën–Vezzosi, Pantev–Vezzosi and the Stacks Project. Claim anchors are exact excerpts of the extracted spoken narration; mathematical formulas and bibliography remain display-only. The primary tests are `tests/test_category_theory_track.py` plus the shared audio-library and course-graph suites.

Audio synthesis and spot listening can follow editorial feedback; manuscripts should not be treated as formally proved or machine-checked mathematics merely because the repository tests pass.

## Possible next development

A separate homological-algebra arc would connect bar resolutions, the Dold–Kan correspondence, derived functors, stable infinity-categories, and cotangent complexes to the constructions introduced here. Choose future lectures based on proof dependencies and substantive examples rather than on a fixed course length.
