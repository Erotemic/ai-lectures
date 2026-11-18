# Discrete Mathematics and Combinatorics

Finite structures and counting arguments, progressing from bijections and double counting through graph theory, generating functions, recurrences, matching, matroids and extremal combinatorics. Distinct from the Algorithms course: mathematical structure and proof first.

The current pack contains **13 lecture manuscripts**. Short concept chapters have been consolidated where they develop one subject. Each numbered manuscript has one spoken region; its mathematical statements, exercises, sources, and inherited component notes remain in the non-spoken companion.

## Listening routes

`track.json` owns the current manuscripts and complete sequence. `navigation.json` selects the guided and deeper routes listed below.

- **Discrete Mathematics · Counting and Finite Structures** (Guided route): `001000`, `005000`, `009000`, `011000`.
- **Discrete Mathematics · Graph Structure and Expansion** (Deep dive): `005000`, `009000`, `013000`, `014000`, `011000`, `021000`, `040000`, `042000`.
- **Discrete Mathematics · Randomness and Counting** (Deep dive): `011000`, `018000`, `013000`, `031000`.
- **Discrete Mathematics · Set Systems and Discrepancy** (Deep dive): `018000`.
- **Discrete Mathematics · Codes, Fourier Methods, and Pseudorandomness** (Deep dive): `020000`, `036000`.

## Current manuscripts

Durations are measured from the current spoken text at 145 words per minute, before synthesis; they are descriptions, not writing targets.

| ID | Lecture | Approximate minutes |
|---|---|---:|
| `001000` | [Counting, generating functions, and symmetry orbits](001000-counting-generating-functions-and-symmetry-orbits.md) | 45.5 |
| `005000` | [Graphs, matchings, and flow certificates](005000-graphs-matchings-and-flow-certificates.md) | 26.8 |
| `009000` | [Greedy graph structure, extremal bounds, and coloring](009000-greedy-graph-structure-extremal-bounds-and-coloring.md) | 23.9 |
| `011000` | [Random discrete structures: existence, reliability, and concentration](011000-random-discrete-structures-existence-reliability-and-concentration.md) | 28.8 |
| `013000` | [Submodular structure and randomized rounding](013000-submodular-structure-and-randomized-rounding.md) | 15.2 |
| `014000` | [Forced patterns, spectral expansion, and graph separators](014000-forced-patterns-spectral-expansion-and-separators-shared-core.md) | 23.7 |
| `018000` | [Set-system complexity, sampling, and constructive discrepancy](018000-set-system-complexity-sampling-and-constructive-discrepancy.md) | 42.7 |
| `020000` | [Codes, extraction, Fourier analysis, and influence](020000-codes-extraction-fourier-analysis-and-influence.md) | 37.8 |
| `021000` | [Parameterized algorithms and expander structure](021000-forced-patterns-spectral-expansion-and-separators-shared-core.md) | 12.8 |
| `031000` | [Local tests and structural containers](031000-set-systems-rounding-range-sampling-and-containers-shared-core.md) | 15.2 |
| `036000` | [Local recovery, derandomization, and Fourier uniformity](036000-local-recovery-derandomization-and-fourier-uniformity.md) | 40.1 |
| `040000` | [Hypergraph Matchings and the Absorption Method](040000-hypergraph-matchings-and-absorption.md) | 7.1 |
| `042000` | [Quasirandom Graphs and Four-Cycle Counts](042000-quasirandom-graphs-and-four-cycle-counts.md) | 5.9 |

The short 040000 hypergraph-absorption introduction and 042000 four-cycle/quasirandomness reference address distinct advanced questions. 040000 has no same-method expanded sequel in the current pack; it is labelled as a compact introduction. 042000 contains its own focused argument. They are not combined merely to make a longer recording.

## Sources and authoring

Per-lecture source records live in `metadata/`; the bibliography is in `metadata/sources.json` when present. Composition lineage and editorial revisions are recorded in per-lecture metadata and `provenance.yaml`. Original arguments and exact companions remain with their consolidated manuscript.

Read [the lecture style rules](../../LECTURE_STYLE_RULES.md) before changing narration. Use the spoken-region markers for extraction; keep raw mathematics, code, and source records in the non-spoken companion. Teaching preparation, proof dependencies, and historical influence are distinct.

## Fourier synthesis and discrete harmonic analysis (043000)

New standalone connective lecture `discrete-mathematics:043000` proves finite cyclic convolution and works a four-cycle random walk with an eigenvalue -1 that prevents mixing until the walk is made lazy. The `fourier-connections` route points from this entry to advanced coding and pseudorandomness material. It links separately to the differential-equations and number-theory discussions without duplicating their manuscripts.
