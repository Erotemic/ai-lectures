# 003000 — Lord Rayleigh: What can a trial vibration tell us before we solve the full equation?

**Track:** History · People and ideas. **Theme:** Variational approximation. **Background:** introductory linear algebra; the lecture defines its local objects.

<!-- BEGIN SPOKEN LECTURE -->

# Lord Rayleigh: What can a trial vibration tell us before we solve the full equation?

Imagine a stretched string or an elastic plate. You want its natural frequency, but solving the full differential equation is difficult. Could a plausible trial motion give a useful estimate before the exact vibration is known?

John William Strutt, better known as Lord Rayleigh, explored vibration and sound in the nineteenth century. His two-volume Theory of Sound, beginning in 1877, made variational reasoning a practical instrument for physical problems. The mathematics asks us to compare a motion's stored energy with its inertia. A suitable ratio gives an estimate of a squared frequency.

For a finite matrix, the corresponding construction is called the Rayleigh quotient. Take a symmetric matrix and a nonzero trial vector. Apply the matrix to the vector, take their inner product, and divide by the vector's squared length. If the vector is a true eigenvector, the result is exactly its eigenvalue. If it is only an approximation, the quotient is an average of eigenvalues weighted by how the trial vector is distributed among their eigendirections.

Take a diagonal matrix with eigenvalues two and six. A unit vector with equal components has a Rayleigh quotient of four. It is halfway between the two eigenvalues because the squared weight of each coordinate is one half. Turn the vector toward the first axis and the quotient moves toward two. Turn it toward the second and it moves toward six.

The key physical insight is that this quotient can be easier to evaluate than the exact modes are to find. But it also exposes a problem. A good estimated eigenvalue need not automatically mean a good estimated eigenvector when other eigenvalues are nearby. Certifying the direction requires more information, especially a residual and a spectral gap.

Rayleigh's contribution stands at the bridge from modeling to approximation. The trial function is a guess informed by physics, and the quotient converts that guess into a quantitative prediction. Later variational methods refined how trial spaces should be selected and how to extract several approximate eigenvalues at once.

In spectral perturbation theory, the Rayleigh quotient is a natural starting point, but the deeper question is geometric: after the numerical approximation has produced a trial direction, how close is it to the relevant true spectral subspace?

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

For \(A=\operatorname{diag}(2,6)\) and
\(x=(\cos t,\sin t)\), the Rayleigh quotient is
\(\rho_A(x)=\langle Ax,x\rangle/\langle x,x\rangle
=2\cos^2t+6\sin^2t\).
At \(t=\pi/4\), this is \(4\). This is an eigenvalue estimate, not a bound on
which exact eigenvector the trial vector approximates.

## Reading notes (non-spoken)

The linked biography or contributor record identifies the person; the mathematical source documents a related publication or mathematical construction. The accessible topic article supplies background. Publication and personal history are distinguished from later eponymous terminology.
