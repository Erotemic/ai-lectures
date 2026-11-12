# 028000 — Richard J. Samworth: How do we turn a deterministic angle theorem into a statistical guarantee?

**Track:** History · People and ideas. **Theme:** Statistical subspaces. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Richard J. Samworth: How do we turn a deterministic angle theorem into a statistical guarantee?

A perturbation theorem is deterministic. It says that if two operators satisfy particular bounds and a spectral separation condition, their subspaces cannot be too far apart. Statistical inference adds randomness: the operator we actually compute is estimated from data, and its error varies from sample to sample.

Richard J. Samworth is a coauthor, with Yi Yu and Tengyao Wang, of the 2015 Biometrika paper A Useful Variant of the Davis–Kahan Theorem for Statisticians. The paper makes a classical eigenvector-rotation estimate easier to integrate into statistical arguments by expressing the decisive separation using population eigenvalues alone.

Take a population covariance matrix and a sample covariance matrix. Their difference is a random matrix. Probability theory can provide an inequality saying that, with high probability, its operator norm is smaller than a chosen threshold. The spectral theorem provides the population eigenspaces. A perturbation theorem converts the matrix-norm event into a statement about the principal angles between population and sample subspaces.

The logic has two stages. First, prove or obtain a probability bound for the estimation error. Second, on every event where that error bound holds, apply a deterministic subspace theorem. Keeping the stages separate makes the result easier to check. The perturbation theorem itself does not say how the sample covariance concentrates; that comes from the statistical model and its assumptions.

Imagine a population covariance with two large, nearby eigenvalues and a substantial gap before the third. If an application seeks a two-dimensional principal component subspace, the gap after the second eigenvalue is relevant. The tiny difference between the first and second is not the one that determines whether their span is stable. This is a statistical reason to state the target as a subspace rather than an ordered list of sample eigenvectors.

The 2015 result also considers singular subspaces for rectangular matrices. This matters in applications where an estimated signal matrix or embedding is not a covariance matrix and left and right directions carry different interpretations.

The paper is a collaboration; its authors share the credit for its theorems. Samworth's place in this historical track is an occasion to understand the meeting of two disciplines: deterministic geometry supplies an implication, and probability theory supplies the chance that its premises are satisfied by the data.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

Let \(\Sigma\) be population covariance, \(\widehat\Sigma\) sample
covariance, and \(E=\widehat\Sigma-\Sigma\). For an event
\(\mathcal E=\{\|E\|\le\varepsilon\}\), the deterministic subspace bound
applies pointwise on \(\mathcal E\) whenever its spectral-gap conditions hold.
A concentration inequality supplies \(\mathbb P(\mathcal E)\), not the
geometry itself. This division is central to statistical applications.

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
