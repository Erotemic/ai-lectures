# Information Theory: From Questions to Communication

Mathematical foundations and worked proofs for compression, dependable communication over noisy links, statistical evidence, and the cost of allowed approximation. The original introductory lectures are preserved; the new lectures deepen the proofs and extend the course to sources with memory and lossy coding.

## Recommended listening order

- `information-theory:001000` - Entropy, questions, prefix codes, and Kraft's inequality (existing introduction)
- `information-theory:004000` - **Why Typical Sequences Can Be Compressed** (iid AEP and both source coding bounds)
- `information-theory:002000` - Mutual information, data processing, and channel capacity (existing introduction)
- `information-theory:005000` - **How Reliable Messages Cross a Noisy Channel** (random coding and Fano converse)
- `information-theory:003000` - Divergence, log loss, and statistical learning (existing introduction)
- `information-theory:006000` - **How Much Can We Afford to Forget?** (rate-distortion)
- `information-theory:007000` - **Entropy Rates and Sources with Memory** (Markov sources and prediction)

For a shorter specialized route, `navigation.json` also offers source compression and memory, reliable noisy communication, statistical prediction, and lossy compression. A lecture can be read or listened to independently after its stated prerequisites. No non-text assets are bundled.

## Where this course draws the line

The finite-alphabet iid theorems are derived under explicit sampling, code, and error assumptions. The stationary Markov material is separate from iid typicality. The rate-distortion example uses a stipulated Hamming loss; it is not a universal perceptual measure. The distinction between existence proofs and efficient practical codecs is retained throughout.

## Source notes

Original source annotations are in `metadata/sources.json`; each lecture's sidecar links the relevant references. Mathematical companions at the end of manuscripts contain exact formulas, qualifications, and exercises, outside the spoken narration.
