# Continuation 28 — Symplectic and Floer Foundations

**Date:** 2026-11-16. **Status:** 15 new substantive, registered lectures; 81 to 96 total. An incremental text-only overlay building on Continuation 27. All prior manuscripts unchanged.

## Why this material comes now

The existing advanced 032000 Floer Homology, 034000 Nonsqueezing, and later 037000 Wrapped Floer lectures use analytic and geometric steps that earlier survey lectures introduced too quickly. The new sequence supplies those steps with explicit calculations, assumptions and examples rather than creating duplicate advanced surveys. Lecture duration is determined by what the subject needs.

## Dependency bridge

| Lecture | Calculable foundation | Advanced destinations |
| --- | --- | --- |
| 021200 | J_a and the associated metric; compatible versus tame | 032000, 034000, 037000 |
| 021300 | Moser vector field and Darboux local standard form | 021000, 027000, 034000 |
| 021400 | zero section, graph df, Hessian intersection test | 032000, 037000 |
| 025100 | CP1 maps z^d, branch and area degree | 032000, 034000 |
| 025200 | J-curve PDE, exact area-energy identity, sphere exclusion | 032000, 034000 |
| 025300 | Cauchy-Riemann symbol and two genus indices | 032000, 037000 |
| 025400 | index ten and automorphism quotient six for a CP2 line | 032000, 034000 |
| 025500 | Maslov half-turn and hemisphere disk index | 030000, 032000, 037000 |
| 025600 | variational action, harmonic oscillator, capping shifts | 032000, 037000 |
| 025700 | Floer gradient equation and action-energy identity | 032000, 037000 |
| 025800 | explicit z/epsilon bubble; break versus escape | 032000, 034000, 037000 |
| 025900 | rigid-cylinder counts, compactification, gluing, d^2=0 | 032000, 037000 |
| 031100 | Novikov finiteness and action filtration | 032000, 037000, 038000 |
| 031200 | continuation correction, chain homotopy, torus bound four | 032000, 034000 |
| 031300 | T*S1 two exact graphs, two strips cancel modulo two | 032000, 037000 |

## Conventions and correctness checklist

- Fix omega = sum dq_i wedge dp_i, i_{X_H} omega = dH, compatible J with J(partial_q) = partial_p and J(partial_p) = -partial_q, and g(v,w) = omega(v,Jw).
- On T*Q set lambda = -sum p_i dq_i so d lambda = omega. This is the negative of the commonly used tautological p dq, and is chosen to match the existing 021100 track convention.
- The periodic Hamiltonian action is A_H([x,u]) = - integral_D u*omega - integral_0^1 H_t(x(t)) dt. Then dA_H(x)[xi] = integral omega(xdot - X_H, xi), and the negative-gradient Floer PDE is u_s + J_t(u)(u_t - X_H) = 0. Its energy is A_H(x_-) - A_H(x_+) for s-independent data. A time-dependent interpolation H_s contributes -integral d_s H_s to the energy identity.
- For exact Lagrangians lambda|L_i = d f_i, use path action -integral lambda - integral H + f_1(endpoint1) - f_0(endpoint0). On L0=zero, L1=graph(df) in T*S1, the primitive on L1 is -f and a constant chord's action is -f(q).
- Gromov compactness is convergence allowing bubble components and possible domain degeneration, not uniform smooth convergence on the original domain. Floer breaking, disk bubbling and escape at infinity are distinct failure modes. Exactness or asphericity rules out specified bubble types but is not the whole compactness proof.
- Fredholm index means dimension(kernel) minus dimension(cokernel). It is only the actual moduli dimension when regularity and treatment of automorphisms allow. For the parametrized CP2 line, index is ten; quotienting the free six-dimensional sphere automorphism group gives four.
- Floer differential squared zero requires zero- and one-dimensional regular moduli, compactification with the correct boundary strata, and gluing. In nonexact Lagrangian theory, unobstructedness and virtual methods may be needed instead.
- The coefficient convention for Novikov completion is given explicitly because the direction of exponents varies in the literature; the completion is an algebraic condition distinct from analytic compactness.

## Existing advanced lecture sign note — **not edited**

The older mathematical companion to 032000 writes A_H([x,u]) = **+** integral_D u*omega - integral H dt, while its Hamiltonian flow and positive-J Floer equation use the convention i_{X_H} omega = dH. Their first variations are inconsistent together. The formula compatible with the track's convention is **negative** area minus integral H, as explained and derived in 025600 and 025700 and in Salamon's Floer lecture notes (§§1.4-1.5). This overlay does not change 032000, avoiding conflicts with independent agents; a follow-up focused correction is warranted.

## Scholarship and attribution

Moser's volume-form method is attributed to Jürgen Moser (1965); Gromov's pseudoholomorphic-curve framework to his 1985 Inventiones paper; Lagrangian Floer intersection homology to Andreas Floer (1988), and Hamiltonian fixed-point Floer theory to Floer (1989). Wendl's lectures, Salamon's 1997/1999 lecture notes, and McDuff–Salamon's book supply modern mathematical expositions, not claims of original discovery. Full source links are in metadata/sources.json, and per-lecture reference roles in metadata/<id>.json. Each lecture also links to relevant Wikipedia articles.

## Next unfilled prerequisites

The Cartan model and a worked equivariant localization theorem; Čech and sheaf cohomology, K-theory and Chern character for families index; contact/Reeb dynamics, Liouville ends and maximum principles for wrapped Floer and symplectic field theory. These remain proposals, not empty transcript stubs.
