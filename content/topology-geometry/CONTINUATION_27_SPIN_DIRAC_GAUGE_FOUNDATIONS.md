# Continuation 27: Spin, Dirac and Gauge Analysis Foundations

Date: 2026-11-16. Status: 13 new substantive Topology and Geometry manuscripts registered, bringing 68 to 81. This is an incremental content overlay on Continuation 26; it does not overwrite existing manuscripts.

## Dependency bridge

The lecture sequence develops the precise local-to-global and analytic inputs assumed by existing advanced instanton, index-family, and Seiberg-Witten lectures. Foundations are inserted immediately before their first substantial advanced use where available low-significance IDs allow.

| ID | Concrete core | Supports advanced lectures |
| --- | --- | --- |
| 024200 | Weak derivatives, W1,2 to L4 in 4D, Rellich and connection products | 020200, 031000, 035000 |
| 024300 | Fourier solution of periodic Laplace equation, elliptic estimate and bootstrap | 020000, 024000, 031000 |
| 030100 | Two Pauli generators, Clifford anticommutation and Dirac symbol | 031000, 040000, 041000 |
| 030200 | Spin versus Spin-C, w2 obstruction and determinant-line lift | 040000, 041000 |
| 030300 | Spinor connection, circle spin Dirac spectrum, chirality | 040000, 041000 |
| 030400 | Lichnerowicz and Bochner vanishing, determinant curvature correction | 041000 |
| 030500 | Spin-C index (c1 squared minus signature)/8 and CP2 example | 040000, 041000 |
| 030600 | ASD elliptic deformation cohomology H0, H1, H2 | 026000, 031000, 039000 |
| 030700 | Coulomb slice, stabilizers and Kuranishi obstruction map | 031000, 039000, 041000 |
| 030800 | SU2 virtual dimension and charge-one S4 example | 031000, 039000 |
| 034100 | Energy bound 8*pi^2|k| and 4D scale invariance | 035000, 039000 |
| 034200 | Small-L2 Uhlenbeck gauge and weak convergence off concentration set | 035000 |
| 034300 | Integer-charge bubbling, removable singularities, ideal instantons | 035000, 039000 |

## Exact conventions and scope

- Riemannian Clifford multiplication: c(v)^2 = -|v|^2; Fourier principal symbols may carry i. Clifford multiplication is not the same operation as vector cross product.
- Spin iff w2(TX)=0 for oriented X. Spin-C iff w2 has an integral lift. In a Spin-C structure the determinant line has c1 congruent to w2 modulo 2.
- Spin-C Dirac index on a closed oriented four-manifold: ind_C(D_A^+) = (c1(L)^2 - signature(X))/8. This differs from the de Rham Euler operator index.
- The untwisted spin Lichnerowicz formula is D^2 = nabla*nabla + Scal/4. A determinant-line curvature correction is present in the Spin-C formula. The coefficient depends on which local connection is called A; the manuscripts consistently mean the determinant connection.
- For a closed oriented SU(2) four-manifold, the ASD index is 8k - 3(1-b1+b+), with k=c2(P)[X] >= 0 for ASD in the stated trace/orientation convention.
- Using |F|^2 vol = -tr(F wedge *F), k = (1/(8*pi*pi)) integral tr(F wedge F), the Yang-Mills energy is >= 8*pi*pi*abs(k), and ASD realizes equality for positive k.
- Weak H1 convergence, strong L2 convergence, smooth convergence off concentration points, and convergence of curvature energy measures are distinct claims. Uhlenbeck compactness at critical L2 regularity is not identical to the supercritical Lp>n/2 theorem.
- The ASD deformation maps form a complex only at an ASD solution, modulo specified central-curvature variants. Formal cohomology dimensions do not by themselves guarantee a smooth quotient moduli space.
- Bubble energy quantization in units of 8*pi*pi is stated for ASD SU(2) bundles under standard compactness/energy identity hypotheses, not arbitrary Yang-Mills fields.
- The read-aloud region is isolated with BEGIN/END SPOKEN LECTURE markers. Exact notation, exercises, citations and optional deeper references are outside that region. No fixed narration duration or word-count policy is imposed.

## Main sources and idea attribution

Liviu Nicolaescu and Tim Perutz supply modern expositions of Spin-C geometry and Dirac operators. Clifford algebra, characteristic obstructions, and the analytic index predate these expositions. The original four-dimensional compactness and removable-singularity results belong to Karen K. Uhlenbeck: *Connections with L^p Bounds on Curvature* and *Removable Singularities in Yang-Mills Fields*, both published in Communications in Mathematical Physics 83 (1982). Freed and Uhlenbeck's *Instantons and Four-Manifolds* presents the broader moduli-space framework. Exact reference links, source type/access notes, and per-lecture alignment are registered in metadata/sources.json and metadata/<id>.json.

## Still missing

The most consequential next bridges are the analysis of almost-complex and pseudoholomorphic curves, Lagrangian Floer theory and compactness, equivariant Cartan-model localization, and K-theoretic families index. They are proposals; no manuscripts for them are included in this overlay.
