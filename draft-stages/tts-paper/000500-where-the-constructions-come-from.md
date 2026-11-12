# 000500 — Where the constructions come from

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** orientation. **Audience:** no prerequisites beyond the orientation lecture; the mathematics is developed in the rest of the course.

<!-- BEGIN SPOKEN LECTURE -->

Where the constructions come from

The Davis–Kahan angle theorems combine ideas that grew up separately, over almost a century, in geometry, mechanics, operator theory, and matrix analysis. A reader of the 1970 paper, or of the recent journal paper that checks and extends it, meets these ideas already assembled. This lecture takes them apart again, one strand at a time, so that each construction in the course has a place and a purpose. It is a map of the mathematics, organized by the questions each strand answered. It makes no claim about who influenced whom beyond what the cited works document.

There are five strands, and a sixth that ties them together. How should two subspaces be compared? How can an eigenvector be approximated, and how good is the approximation? How do spectral subspaces move when an operator changes? How large is the solution of an operator equation when two spectra are separated? And how should the size of an operator be measured when no single number is enough? Davis and Kahan's work joins all five to answer one question: given an approximate subspace and a computable residual, how far can it be from the exact spectral subspace?

Comparing two subspaces

The first strand is geometry. For two lines, a single angle describes their relative position. For two planes in four-dimensional space, one angle is not enough, and Camille Jordan, in his 1875 essay on geometry in n dimensions, introduced the sequence of angles now called principal angles: the smallest angle between any vector of one subspace and any vector of the other, then the smallest angle among vectors perpendicular to those, and so on.

The same angles appeared in statistics. Harold Hotelling's 1936 paper on relations between two sets of variates introduced canonical correlations, which are the cosines of principal angles between two column spaces of data. In numerical linear algebra, Åke Björck and Gene Golub gave numerical methods in 1973 for computing principal angles and vectors from orthonormal bases.

In infinite dimensions, a list of angles may not exist, and the geometry has to be carried by operators. Jacques Dixmier in 1948 and Chandler Davis in 1958 studied the relative position of two closed subspaces in operator terms, and Paul Halmos's 1969 paper titled Two Subspaces gave the block form in which a pair of projections, on its generic part, looks like two lines in a plane with an operator in place of the angle. The cosine–sine decomposition, which writes a partitioned unitary matrix with matching cosine and sine blocks, grew out of the same geometry; Paige and Wei's history traces it from Jordan through the ideas assembled by Davis and Kahan to G. W. Stewart's explicit formulation in 1977.

In the course, this strand gives the principal angles, the angle operator Theta and its directed parts, Halmos's form, and the classification of pairs.

Approximating eigenvectors

The second strand comes from mechanics. Rayleigh, in The Theory of Sound, published in 1877, estimated vibration frequencies by evaluating energy ratios on guessed shapes, the quantity now called the Rayleigh quotient. Walter Ritz, in work published in 1909, made this systematic: choose a finite-dimensional space of trial functions and solve the eigenvalue problem restricted to it. The Rayleigh–Ritz method produces approximate eigenvalues and eigenvectors, and the residual measures how far they are from exact.

Eigenvalues turned out to be well behaved. Hermann Weyl's 1912 work on the distribution of eigenvalues contains comparison inequalities whose modern matrix form says that ordered eigenvalues of Hermitian matrices move by no more than the size of a perturbation, and the Courant–Fischer min-max principle characterizes eigenvalues through Rayleigh quotients over subspaces. Eigenvectors are not as well behaved: two matrices with the same eigenvalues can have perpendicular eigenvectors. A theory of eigenvector, or eigenspace, accuracy had to bring in something more, a gap in the spectrum.

In the course, this strand gives trial frames, trial operators, residuals, the Rayleigh–Ritz choice, and the example showing that eigenvalue stability does not imply eigenvector stability.

Moving spectral subspaces

The third strand is perturbation theory for operators. Franz Rellich, in papers from 1937 to 1942, developed a rigorous perturbation theory for self-adjoint operators depending on a parameter. Béla Sz.-Nagy, in work published in 1947, constructed a unitary operator carrying one spectral projection onto a nearby one, and Tosio Kato gave the construction a streamlined algebraic form, using the operator Q P plus the identity minus Q times the identity minus P and its polar factor, later presented in his book on perturbation theory for linear operators. Barry Simon's survey of Kato's work recounts this history.

This is the direct rotation of the course: the canonical unitary taking one subspace onto another, which Davis and Kahan characterized by positive diagonal blocks and studied for its extremal properties.

The spectral theorem itself, and the spectral projections for regions of the spectrum, belong to this strand as well. They are what make the exact wanted subspace a well-defined object even when the operator is unbounded and has no eigenvectors.

Separated spectra and operator equations

The fourth strand is an operator equation. James Joseph Sylvester studied the matrix equation A X minus X B equals C in 1884, and its solvability depends on the two coefficient matrices having no common eigenvalue. Marvin Rosenblum extended the theory to bounded operators with disjoint spectra in 1956, and studied the case of self-adjoint coefficients in 1969.

For angle bounds, solvability is not enough; what matters is the size of the solution. When the residual is projected onto the complement of the exact subspace, the coordinates of the trial vectors in that complement satisfy a Sylvester equation whose coefficients are the trial operator and the unwanted exact block. If the two spectra are separated by delta in the right geometric shape, the solution is at most the right-hand side divided by delta. That is the bridge from a residual to an angle.

In the course, this strand gives the Sylvester equation, Davis and Kahan's Theorems 5.1 and 5.2, the distance-only Hilbert–Schmidt estimate, and the treatment of unbounded coefficients through cutoffs.

Measuring operators

The fifth strand is the measurement of operators by their singular values. John von Neumann in 1937 characterized the unitarily invariant norms on matrices as symmetric gauge functions of the singular values. Robert Schatten's 1950 monograph developed normed operator ideals, such as the trace class and the Hilbert–Schmidt class, in infinite dimensions. Ky Fan's 1951 inequalities for sums of the largest eigenvalues and singular values provide the comparison principle that lets one inequality, proved for every Ky Fan norm, hold for every unitarily invariant norm at once.

In the course, this strand gives unitarily invariant norms, Ky Fan dominance, operator ideals and the membership conditions that go with them, and Q-norms.

The synthesis

Chandler Davis studied the rotation of eigenvectors under perturbation in papers of 1963 and 1965. With William Kahan he announced new bounds in 1969, and published the full treatment in 1970 in a paper titled The Rotation of Eigenvectors by a Perturbation, Part Three. Its four headline theorems, for the sine, the tangent, the doubled sine, and the doubled tangent of the angle operator, each combine the strands: an angle operator from the geometry, a residual or perturbation from the approximation theory, a gap and a Sylvester estimate from operator theory, and a statement in every unitarily invariant norm from the theory of singular values. The paper also develops the direct rotation's geometry and extremal properties, Sylvester estimates for unbounded operators, generalized sine and tangent theorems, and results selecting which spectral subspace a double-angle bound refers to.

After the synthesis

The ideas spread. Per-Åke Wedin, in 1972, gave the corresponding perturbation bounds for singular subspaces of general rectangular matrices. Stewart's work connected the angle geometry with least-squares sensitivity and matrix computations. In statistics, an empirical covariance matrix approximates a population covariance, and eigenspace error is the central question; Yi Yu, Tengyao Wang, and Richard Samworth gave in 2015 a variant of the sine-theta theorem whose gap is measured in the population spectrum, and Chen, Chi, Fan, and Ma's survey of spectral methods shows how widely such bounds are used.

The transport question of Section 4 of the 1970 paper had its own afterlife. Bolotnikov, Li, and Rodman, in 2001, studied minimal distortion problems for unitary maps carrying one subspace onto another, proving optimality for Q-norms and giving counterexamples for some Schatten norms. Later work on metrics on the space of subspaces returned to the same questions.

A recent journal paper revisits the 1970 paper result by result. It finds that twenty-eight of the twenty-nine selected results hold as stated, and that Proposition 4.4, the claim that the direct rotation minimizes every unitarily invariant norm of the full displacement for real subspaces at small angles, is false. It gives a real four-dimensional counterexample at every positive angle, which turns out to be a real form of Davis and Kahan's own complex example, identifies the failed step, and proves the Q-norm statement that replaces it. And it answers the optimization question that the counterexample raises: the minimum trace-norm displacement of a real orthogonal transport is a matching problem on the principal angles.

To summarize. Principal angles come from Jordan's geometry, with parallels in Hotelling's statistics and operator versions from Dixmier, Davis, and Halmos. Trial subspaces and residuals come from Rayleigh and Ritz, and eigenvalue stability from Weyl and the min-max principle. The direct rotation comes from Sz.-Nagy and Kato's transport of spectral projections. The separation estimate comes from the Sylvester equation, studied by Sylvester and Rosenblum. The norms come from von Neumann, Schatten, and Ky Fan. Davis and Kahan joined these into the angle theorems, and later work extended them to singular subspaces, statistics, and the optimization of transports.

These are mathematical lineages, not a record of who read whom. Where the course attributes a specific construction to a specific paper, the attribution is to what that paper contains.

<!-- END SPOKEN LECTURE -->

---

## Companion (display only)

| Strand | People and works | Course lectures |
|---|---|---|
| Comparing subspaces | Jordan 1875; Hotelling 1936; Dixmier 1948; Davis 1958; Halmos 1969; Björck–Golub 1973; Stewart 1977; Paige–Wei 1994 | 003900, 004000, 004500 |
| Approximating eigenvectors | Rayleigh 1877; Ritz 1909; Weyl 1912; Courant–Fischer | 003000 |
| Moving subspaces | Rellich 1937–42; Sz.-Nagy 1947; Kato (1955 report; 1966 book); Simon 2018 survey | 005000, 005500, 001000 |
| Operator equations | Sylvester 1884; Rosenblum 1956, 1969 | 008000–012000 |
| Measuring operators | von Neumann 1937; Schatten 1950; Ky Fan 1951 | 006000, 013000 |
| Synthesis | Davis 1963, 1965; Davis–Kahan 1969, 1970 | 020000–023000 |
| Afterwards | Wedin 1972; Yu–Wang–Samworth 2015; Chen–Chi–Fan–Ma 2021; Bolotnikov–Li–Rodman 2001; Qiu–Zhang–Li 2005; Zhang–Qiu 2010 | 017000–025700 |

Source: journal paper, Section 2 and Table 1 (“Mathematical sources used in the Davis–Kahan formalization”). Historical claims are anchored in `metadata/000500.json`; each awaits primary-passage comparison.
