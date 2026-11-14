# The World Reconsidered: flagship completion (006000–012000)

**Status:** Seven substantive lecture manuscripts, companions, and per-lecture source records. The twelve-part flagship is drafted; this is not a claim that synthesized audio has been listened to or that every source passage has received independent historical review.

## Editorial architecture

| ID | Question | Historical spine | Analytical material |
| --- | --- | --- | --- |
| 006000 | Who decides what is normal? | Quetelet; Canguilhem; changes to psychiatric classification | Statistical distributions vs. standards; reference intervals; decision thresholds; disability access |
| 007000 | Why does the whole differ from its parts? | Jane Jacobs; Schelling; Maxwell | Negative/positive feedback; routing optimization; queues, thresholds, coordination, networks |
| 008000 | Why could history have been different? | 1914 July Crisis; Tambora and 1816 | Counterfactual comparison; causation, triggers vs. structures, path dependence, historical evidence |
| 009000 | What is information? | Claude Shannon and Bell Labs | Entropy, prefix coding, error correction, noisy-channel capacity, mutual information and meaning |
| 010000 | Why does progress cause further problems? | Haber–Bosch; Jevons; CFCs; ozone measurements | Nitrogen balance, rebound arithmetic, externalities, life-cycle boundaries, delayed effects |
| 011000 | What makes a good life? | Epicurus; Aristotle; Epictetus; the Harvard longitudinal study | Happiness vs. flourishing, autonomy, competence, relationships, capabilities, conflicts of value |
| 012000 | What do we owe future generations? | Szilard's July 1945 petition; Asilomar 1975 | Expected loss, discounting, reversibility, nonidentity problem, institutional accountability |

## Editorial principles applied

- Every lecture works independently of the other eleven. No spoken chapter-to-chapter references.
- Spoken prose builds concrete examples before formal models; mathematical expressions, references and qualifications are retained in a display-only companion.
- No fabricated private conversations, feelings, or claims of privileged access to historical figures' thoughts. Anecdotes are bounded by research evidence.
- Do not equate quantitative averages with moral ideals, network models with historical segregation causation, Shannon entropy with truth or understanding, or a philosophical argument with a universal psychological result.
- Distinguish historical primary sources, institutional summaries, numerical teaching cases, and analytic interpretations.
- The shared `metadata/sources.json` is additive relative to the first five lectures; the per-lecture sidecars use `reference_recorded` unless passage-by-passage verification has occurred.

## Numerical checks

- 007000: 20 travelers, route A time `10 + n_A`, route B 30. All-A total 600 driver-minutes; 10/10 split total 500. The latter is a toy social optimum and is not an individual-choice equilibrium.
- 009000: entropy of probabilities `(1/2,1/4,1/8,1/8)` is 1.75 bits; code `0,10,110,111` has expected length 1.75; triple-repetition failure probability under independent flip rate 0.1 is 0.028; binary symmetric channel capacity is about 0.531 bits/use.
- 010000: the synthetic farm balance conserves 100 units, the energy rebound example compares 100 with 150 units, and 10-year present value of 100 at 5% vs 1% is approximately 61.39 vs 90.53.
- 012000: 50-year present value of 100 at 5% vs 1% is approximately 8.72 vs 60.80; a 0.001 chance of one-million loss has monetary expectation 1,000. These calculations do not resolve the ethical choices about thresholds and risks.

## Integration

- `track.json` lists all twelve lectures using unchanged IDs for 001000–005000.
- New lecture `metadata/<ID>.json` records all reference IDs and anchored historical claims.
- The existing audio reader receives new entries through the manifest without changes to runtime code.
- After applying the overlay, run `python -m pytest -q tests/test_world_reconsidered_track.py tests/test_audio_course_tracks.py tests/test_course_graph.py tests/test_world_history_overlay_merge.py`.

**Listening review:** not yet performed. Estimated durations depend on the voice and punctuation; punctuation, pronunciations and expressive timing should be evaluated if listeners report problems.
