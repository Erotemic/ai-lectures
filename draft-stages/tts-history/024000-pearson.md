# 024000 — Karl Pearson: Why is a principal component an optimization problem?

**Track:** History · People and ideas. **Theme:** Statistical subspaces. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Karl Pearson: Why is a principal component an optimization problem?

Imagine a cloud of data points with two measured coordinates. It stretches much farther in one diagonal direction than the other. If we want to replace two coordinates by one, the direction of largest spread is a natural candidate.

Karl Pearson's 1901 paper On Lines and Planes of Closest Fit to Systems of Points in Space is part of the early history of what is now called principal component analysis. Pearson worked in statistics and mathematical methods during a period when these ideas were being brought together, although the modern statistical formulation and name came through later work by Harold Hotelling.

In the plane, choose a line through the center of the data. Project each point orthogonally onto the line, then measure the squared distances from the points to their projections. A best-fit line minimizes the total squared perpendicular error. Equivalently, for centered data, it maximizes the variance of the projected coordinates.

These are two descriptions of the same calculation. The total squared length of the centered data is fixed. Splitting each data vector into its component along the line and its perpendicular component divides that squared length into two parts. Minimizing the perpendicular part therefore maximizes the along-line part.

The best direction is an eigenvector of the covariance matrix for its largest eigenvalue. The remaining orthogonal eigenvectors describe successive directions of variation. When we retain several of them, the object that matters is their span: a principal component subspace.

This is where perturbation theory enters modern statistics. The sample covariance matrix is estimated from a finite data set. It differs from the population covariance matrix we would ideally know. How much can the leading principal component subspace move under that estimation error? The answer depends on a separation between the retained and discarded eigenvalues.

Pearson's place in this history is an early geometric formulation of dimensionality reduction. The line is chosen through an optimization problem, and the eigenvector is the algebraic expression of that optimization. The subsequent spectral perturbation results tell us when the estimated line or plane is stable enough to interpret.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For centered observations with covariance \(\Sigma\), a unit direction \(u\)
maximizes projected variance \(u^*\Sigma u\) precisely when it is a
leading eigenvector. In Euclidean data,
\(\sum_i\|x_i\|^2=\sum_i|u^*x_i|^2+
\sum_i\|x_i-uu^*x_i\|^2\).
Pearson's 1901 line-and-plane fitting precedes Hotelling's 1933 statistical
principal-components treatment.

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
