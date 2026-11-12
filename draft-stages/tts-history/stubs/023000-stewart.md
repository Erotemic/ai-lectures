# 023000 — G. W. Stewart: How should matrix perturbation bounds guide actual numerical work?

**Track:** History · People and ideas. **Theme:** Computing angles and stable subspaces. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# G. W. Stewart: How should matrix perturbation bounds guide actual numerical work?

A numerical linear-algebra routine returns a matrix factorization. You want to know whether the result can be trusted, and how much the answer would change if the input were perturbed. This is where perturbation theory and condition numbers become operational tools.

G. W. Stewart, often known as Pete Stewart, developed major contributions to numerical linear algebra, matrix factorizations, and perturbation analysis. His work includes books and algorithms that connect theoretical error bounds with the computations scientists perform. With Ji-guang Sun he authored Matrix Perturbation Theory in 1990, a standard reference in the subject.

Begin with two eigenvalues separated by a gap of one. A small perturbation of size one hundredth seems harmless. But if their gap is only one ten-thousandth, the same perturbation is large relative to the separation and may rotate the eigendirections substantially. The ratio of perturbation size to gap is the kind of quantity a condition estimate tries to capture.

Now change the object being measured. Instead of a single eigenvector, take a subspace spanning a cluster of nearly repeated eigenvalues. The individual eigenvectors may be poorly conditioned, while the subspace can be well conditioned if the cluster is separated from the rest of the spectrum. The right question is therefore part of the numerical problem, not merely something to ask after obtaining an answer.

Matrix factorizations introduce another layer. An algorithm may produce a backward-stable answer: the computed result is the exact answer to a nearby input problem. Perturbation theory then tells us how far that nearby problem's solution can be from the original solution. Together these two kinds of reasoning turn a computed object into a certified approximation.

Stewart's treatment of these topics emphasizes practical distinctions: normwise versus componentwise sensitivity, eigenvalues versus eigenspaces, and square versus rectangular problems. In singular-subspace estimates, Wedin-type results play a role analogous to Davis–Kahan bounds for Hermitian eigenspaces.

Stewart's contribution is a coherent framework for making sensitivity part of computation. The important result of a numerical method is not merely a set of numbers, but an explanation of which changes in the input could have produced them and what geometric features remain reliable.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

A typical perturbation scale is \(\|E\|/\delta\), where \(\delta\)
is the relevant *wanted–unwanted* spectral separation, not necessarily a
smallest internal eigenvalue gap. A backward-stability argument concerns a
nearby input; a forward subspace error requires a suitable perturbation bound.
Stewart and Sun, *Matrix Perturbation Theory* (1990).

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
