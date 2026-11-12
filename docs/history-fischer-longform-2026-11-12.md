# Ernst Fischer: long-form History promotion

**Baseline:** Source snapshot `7732823` with Jordan, Rayleigh, Ritz and Courant overlays applied. This incremental ZIP promotes only `007000` and updates its associated catalog/readings.

**Length:** 5,836 extracted spoken words, approximately 40.2 minutes at 145 WPM (actual synthesized audio depends on voice and pacing). Replaces a 367-word archived portrait.

**Narration:** Historical life and the methods of Fischer's 1905 finite-matrix min–max result, Fischer and Riesz's separate 1907 Fourier/L² papers, mean-square convergence and completeness, 1908 Hadamard–Fischer inequality, the algebraic influence acknowledged by Emmy Noether, and the forced 1938 retirement from Cologne because of Jewish ancestry. The Noether relationship does not imply ownership of her theorems. There is no assertion of Fischer participating in the Nazi regime; specialist sources document persecution.

**Mathematical checks:** `diag(1,3,7)` two-plane intersection yields middle eigenvalue 3; `phi_n=sqrt(2) sin(n pi x)` and `c_n=1/n` gives `sum c_n^2=pi^2/6`; shrinking spikes have pointwise-zero limit but fixed L² norm; Gram matrix `[[2,1],[1,3]]` has determinant 5 versus block product 6. Modern abstract equivalences are not projected back wholesale onto 1907 primary formulations.

**Sources:** Fifteen named reading records including MacTutor, Neue Deutsche Biographie, an Erlangen faculty register, specialist research on Nazi dismissals, original-paper catalog entries, John Horváth's Riesz–Fischer historical analysis, Noether's acknowledgment, and scholarly matrix-inequality history. Each stable identifier resolves in `metadata/sources.json`.

**Delivery:** No audio, slides, images or unrelated source code. Remove the superseded `stubs/007000-fischer.md` and `stubs/metadata/007000.json` with the explicit `git rm` command accompanying the ZIP. Other archived portraits are retained.
