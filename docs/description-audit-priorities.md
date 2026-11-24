# Prioritizing and recording lecture metadata audits

The metadata-audit ledger is separate from the repository's factual review records. An audit receipt describes **which metadata fields were evaluated**, **how much of the manuscript was read**, **by which reviewer/model**, and **when**. A full-manuscript *metadata* audit is not a verification of historical claims, mathematical proofs, citations, or outside sources.

## Rank the next lectures

```bash
python3 tools/description_audit.py rank --scope description --top 30 \
  --csv /tmp/lecture-description-priorities.csv
python3 tools/description_audit.py rank --scope geography --top 30 \
  --csv /tmp/lecture-geography-priorities.csv
python3 tools/description_audit.py rank --scope tags --top 30
```

`--scope` accepts `description`, `title`, `tags`, `tag_paths`, `chronology`, `geography`, `learning`, `related_resources`, or `claim_evidence`. The description queue uses heuristic risk cues: heading lists, missing identifying subjects, strong proof verbs, unusually brief or generic summaries, and prior follow-ups. After eight high-scoring animal-physiology descriptions passed full-manuscript review in batch 11, a missing title word was made a *weak* cue for general titles: metaphorical titles and morphological variants had generated false positives. Named biographical subjects still receive a stronger title-anchor cue. This is a triage adjustment, not a calibrated prediction model. Other scopes mainly rank by whether a current review exists; there are a few conservative cues for empty biography geography/chronology, absent tag paths, and generic source rationales. The score is a **priority score, not a calibrated probability of an error**. A high score can be a false alarm, and a low score can miss a serious issue.

Each CSV row gives the exact `audit_scope`, revision-aware review state, last audit date/model/depth/result for *that scope*, last current full-manuscript audit, and manuscript/description fingerprints. The ranking command does not create audit records.

## Scope and depth are different

`depth` is **how** the manuscript was inspected:

- `automated`: programmatic flags and completeness checks only; cannot mark a field clean.
- `excerpts`: selected introductory or other brief excerpts checked.
- `targeted_passages`: relevant passages inspected without reading the full narration.
- `full_manuscript`: the entire spoken manuscript read and the **listed metadata scopes** assessed against it.
- `source_verified`: full manuscript and independent external sources examined for the stated metadata scopes. Do not use this unless source verification actually happened.

`scope` is **what** was evaluated:

| Scope | Metadata compared against narration |
|---|---|
| `description` | Accuracy, relative emphasis, clarity, distinctive subject matter, proof-scope language |
| `title` | Title from `track.json` identifies the lecture covered |
| `tags` | Top-level `tags` reflect primary subject matter |
| `tag_paths` | Hierarchical taxonomy paths fit the subject |
| `chronology` | `chronology`, `periods`, `spacetime_coverage` agree with stated events and ranges |
| `geography` | `places`, `geography` agree with the places the manuscript actually treats |
| `learning` | Recorded prerequisites, level, or readiness checks fit the lecture |
| `related_resources` | Resource metadata is appropriately associated with topics, **not** automatically source-verified |
| `claim_evidence` | Claim/evidence metadata corresponds to text, **not** independently fact-checked |

For example, reviewing `description`, `title`, and `tags` does *not* clear `geography` or `claim_evidence`. Checking a biography's chronology against its narration does not establish that the dates in the narration are historically correct. Record `source_verified` only when external sources were separately checked.

## Record exact scope, result, and model

```bash
python3 tools/description_audit.py record history:012000 \
  --model GPT-6 --depth full_manuscript --outcome corrected \
  --scope description --scope title --scope tags --scope geography \
  --scope-outcome description=corrected \
  --scope-outcome title=clean \
  --scope-outcome tags=corrected \
  --scope-outcome geography=corrected \
  --note 'Read entire narration and revised the preview/tags/places; sources not checked.'
python3 tools/description_audit.py history history:012000
```

With multiple scopes, a separate `--scope-outcome` is mandatory for *each*, so a correction to one field cannot be misread as a correction or clean verdict for every field. The event stores an aggregate outcome only for convenience. Use the actual reviewer/model identity; never infer a variant. For a one-scope audit, `--outcome clean` is sufficient.

Each event is append-only in `reviews/registry/description-audits-<track>.jsonl`. Schema-2 events carry `scope`, `scope_outcomes`, a fingerprint for each audited scope, `verification_basis`, model, date, depth, and an explanatory note. Spoken-manuscript changes stale all manuscript-alignment results. A metadata edit only stales the scopes whose *fingerprinted metadata* changed: changing tags does not invalidate a still-correct description review. An automated later screen cannot erase a current full-manuscript review. Old schema-1 records remain valid for `description` only; they are not silently promoted to broader metadata verification.

## Review loop

1. Choose a manageable batch near the top of the *description* queue. Periodically sample low-risk entries to check whether the ranking misses systematic errors.
2. Read the complete spoken text for `full_manuscript`, and inspect the exact metadata fields named in `scope`.
3. Correct only supported problems. Distinguish accurate descriptions from unhelpfully generic ones; do not turn a passing phrase into a main subject or inflate a proof sketch into a formal proof.
4. Record the **final** metadata fingerprints after applying any edits. Record clean fields as clean, corrected fields as corrected, and unresolved issues as `needs_followup`.
5. Generate a fresh ranking. Never convert historical bulk audits into fictitious full-manuscript receipts.

The initial eleven-lecture scoped batch covered descriptions, title alignment, and relevant taxonomy fields, with a chronology/geography check for Ky Fan. It did **not** review learning prerequisites, source support, external historical facts, or formal proof correctness. Earlier description-only full-manuscript records remain description-only. These audits should not block importing or playing lectures.

## Audit progress (23 November 2026, batch 33)

**713 current distinct full-manuscript description reviews out of 2,399 lectures (29.7%)** are recorded, up from 695 (29.0%) after batch 32. This batch adds **18 complete spoken-manuscript reviews**: eight advanced Abstract Algebra lectures and ten Analysis lectures from the complex-analysis sequence. **1,686 lectures remain** without current full-manuscript description receipts. All new receipts name `GPT-6` as reviewer, use `depth=full_manuscript`, and fingerprint the final post-edit spoken text and four audited metadata scopes.

**Twelve descriptions were refined and six retained.** The eight consolidated algebra lectures cover multiple substantial topics: Ext and K-theory; ramification, units and arithmetic heights; curve/surface Riemann–Roch and derived pushforwards; étale fundamental groups alongside descent and deformation; Tannakian reconstruction, highest weights, and flag-variety geometry; DT/PT, Hall algebras and cluster wall crossing; crystals, Demazure characters and Hecke theory; and crystalline p-adic representations. Their previews now identify the major components of the entire narration. In Analysis, the residue-theorem summary now identifies real improper-integral applications; the open-mapping summary names Schwarz–Pick; the harmonic-function summary includes conjugates and Poisson boundaries; and the normal-family summary identifies Montel, Hurwitz and Vitali. The other six complex-analysis previews accurately describe their narrations.

**All 18 previously missing flat topic-tag lists were populated**, with supported primary mathematical concepts and named theorems. **Seven hierarchical path sets were expanded** in the algebra track to index substantive topics not visible in the existing hierarchy, including K-theory, arithmetic geometry, étale fundamental groups, deformation theory, Tannakian reconstruction, wall-crossing, crystal bases, Hecke algebras and p-adic Hodge theory. The remaining 11 existing path sets and all 18 lecture titles passed against the spoken manuscripts and were retained.

Exactly **18 metadata sidecars** and two append-only audit ledgers changed alongside this progress note. This batch assessed `description`, `title`, `tags` and `tag_paths` against the complete spoken narration; it did **not** audit chronological/geographical coverage, learning prerequisites, bibliography associations, external factual accuracy or proof correctness. No lecture text, companion, source record, dependency graph, binary asset or executable code changed.

## Audit progress (23 November 2026, batch 32)

**695 current distinct full-manuscript description reviews out of 2,399 lectures (29.0%)** are recorded, up from 677 (28.2%) after batch 31. Batch 32 adds **18 complete spoken-manuscript reviews**: eight Algorithms, Computability, and Complexity lectures; eight Analysis lectures; and two Abstract Algebra lectures. **1,704 remain without current full-manuscript description receipts.** The reviewer is `GPT-6`, `depth=full_manuscript`, and the receipts contain final post-edit fingerprints and explicit per-field outcomes.

**Eight descriptions were improved; 10 existing descriptions were retained.** The formal-language summaries now mention the pumping lemma, Myhill–Nerode distinguishability, CYK parsing and context-free limits; selection and dynamic-programming previews now identify median-of-medians and weighted interval scheduling; the graph-search preview now covers cycle detection and topological sorting. Analysis summaries better describe completeness, local linearization and uniform function series. These are substantial portions of their spoken lectures, not independent additions to the subject matter. All 18 titles agree with the narrations.

**Fifteen flat topic-tag lists were improved and one hierarchical path was added.** Early mathematics and theoretical-computer-science entries had relevant `tag_paths` but empty top-level `tags`; these now index their actual central tools and theorems. The DFS lecture gained a specific DFS hierarchy path to accompany its existing BFS path. The max-flow, NP-completeness and amortized-analysis records already had adequate descriptions and topical indexing and were left unchanged.

Exactly **15 metadata sidecars changed** and three passed unchanged; the three track registries gained append-only receipts. No spoken manuscript, track title registry, bibliography, associated asset or executable code changed. This batch reviewed `description`, `title`, `tags` and `tag_paths` against the entire spoken narration; it did **not** separately certify chronological/geographical metadata, source attribution, proofs, or external factual accuracy.

## Audit progress (23 November 2026, batch 31)

**677 current distinct full-manuscript description reviews out of 2,399 lectures (28.2%)** are now recorded, up from 659 (27.5%) after batch 30. This batch adds **18 entire spoken-manuscript reviews**: two GPT-SoapBox essays, six world-history epic retellings, one pre-1900 literature story, two *Stargate SG-1* essays, one Washington biography, and six earth-systems science lectures. **1,722 lectures remain without current full-description reviews.** All new receipts identify `GPT-6`, `depth=full_manuscript`, final manuscript and field fingerprints, and explicit scope outcomes.

**Three descriptions were corrected and 15 retained**. The northern cod essay preview now addresses the 1992 collapse and contested 2024–2026 reopening in addition to salted-cod trade. The snow-crystal essay names Kepler, Bentley, Nakaya’s 1936 rabbit-hair experiment and the distinction between lattice symmetry and growth conditions. A *Journey to the West* retelling now identifies the soul-restoring pill and Manjushri’s lion. The other 15 existing descriptions and all 18 titles passed against their manuscripts.

**Eight topical tag lists and eight geographic place lists were expanded.** The six world-history additions index named figures and motifs of the *Mahabharata*, *Journey to the West*, and *Romance of the Three Kingdoms*. Four *Three Kingdoms* lectures gained places including Luoyang, Chang’an, Xiapi, and Fancheng. The two GPT-SoapBox essays received documented fishery/trade and crystallography place coverage; the Washington biography received campaign and political event indexing. The original hierarchical tag paths remained appropriate. The 1592 *Journey to the West* and 1522 *Three Kingdoms* chronology **witness** axes were retained as literary-edition dates, without confusing them with the narratives’ earlier settings. Washington’s documented lifespan and biographical period and the 2017 Oroville case-study period were also retained.

Exactly **10 selected metadata sidecars changed and eight remained byte-identical**. Six track-specific audit ledgers gained append-only receipts; previous ledger history was retained. No spoken manuscript, `track.json`, bibliography, supporting asset, or binary was edited. These audits compare metadata against the narrated text; they do **not** independently verify external historical claims, scientific results, chronology evidence, or mathematical proof correctness. The two *Stargate* receipts cover title and description, not absent per-episode taxonomy fields.

## Audit progress (23 November 2026, batch 30)

**659 current distinct full-manuscript description audits out of 2,399 lectures (27.5%)** are recorded, up from 617 (25.7%) after batch 29. This batch adds **42 complete spoken-manuscript reviews**: six American Civil War, four American Revolution, 13 Brook Road Builders, 17 episodic children's bedtime stories, and two GPT-SoapBox essays. **1,740 lectures remain without current description review receipts.** No targeted-passage-only descriptions remain. Every new receipt explicitly scopes the fields reviewed, uses final manuscript/metadata fingerprints, records `depth=full_manuscript`, and identifies `model=GPT-6`.

**One description was corrected and 41 passed without changes.** The American Civil War political-breakdown lecture now mentions the Dred Scott ruling and John Brown's raid as well as secession and Fort Sumter. The remaining previews, including all 30 new children's-story reviews and the two long essays, corresponded to their complete spoken narration without needing prose edits. All 42 titles matched.

**Nine topical tag lists and nine geographic place lists were expanded; all 42 assessed hierarchical tag-path scopes passed unchanged.** Civil War additions locate Petersburg and the Crater, Mississippi River and western operations, wartime civilian unrest, and Reconstruction enforcement laws. Revolution additions index the Boston Massacre, Bunker Hill, the First Continental Congress, the Sullivan Expedition, naval war in Chesapeake Bay, and constitutional-ratification subjects. Two GPT-SoapBox essays received narrated place coverage for the material history of blue and the Linear B decipherment. No guessed sites were added to the fictional children's stories. All ten American history chronology scopes were checked and retained. The two essays span disparate centuries and were not assigned misleading single historical-period axes.

Exactly **12 selected metadata sidecars changed and 30 remained byte-identical**. The five affected track ledgers are appended without replacing previous receipts. This batch compares metadata against the complete spoken manuscripts; it is **not** independent verification of historical sources, external claims, or scientific findings. No manuscript, `track.json`, supporting bibliography, image, or other binary asset was changed.

## Audit progress (23 November 2026, batch 29)

**617 current distinct full-manuscript description audits of 2,399 lectures (25.7%)** are recorded, up from 537 (22.4%) after batch 28. This batch adds **80 complete spoken-manuscript reviews** across 13 tracks. All seven lectures in the newly added *Godzilla* track and 53 children’s stories (28 bedtime stories and 25 linked Brook Road construction stories) were read in full, alongside 20 mathematical, scientific, historical, media, and cultural lectures. No targeted or partial-only reviews remain current. These are metadata-alignment reviews, not external evidence verification.

**Seven descriptions were refined and 73 descriptions passed unchanged.** The revised previews identify Dedekind-domain ideal factorization, primary decomposition, localization and completion; Euclidean and Diophantine arguments in number theory; the observational basis and model-dependent limits of cosmic-history reconstruction; isotope evidence for Earth's oxygenation; Indian indentured migration after emancipation; and entropy limits on heat engines. The accurate children’s stories, seven *Godzilla* lectures, and other passing previews were not rewritten to satisfy weak title-word ranking heuristics.

**Thirteen topical tag lists and eight hierarchical path lists were corrected.** The most substantial changes improve discoverability for prime factorization, Diophantine approximation, observational cosmology, dark-matter tests, deep-time history, and regional historical subjects. Track-inherited effective tags were considered before adding sidecar tags, avoiding redundant rewrites in well-indexed children’s and film-history tracks.

**Three geographic place lists and two work-publication chronology fields were refined.** The three modern-world entries now identify major narrated case-study places rather than overbroad regions. The *Miles Morales* lecture records the documented 2011 comic debut on a `work` chronology axis; the comedy-philosophy lecture records the publication years of the discussed books on the same axis, rather than confusing them with the historical or fictional settings analyzed. Chronology and geography were assessed only in the receipts explicitly scoped to them.

**Thirteen selected metadata sidecars changed; 67 were retained byte-for-byte.** All 80 new append-only review receipts assert final spoken-manuscript and individual field fingerprints with `depth=full_manuscript`, `verification_basis=manuscript_alignment`, and model `GPT-6`. Previous ledger history was retained. The baseline is the 23 November 2026 (16:36 local export) repository snapshot with the rebased batch 28 applied. No spoken manuscripts, track manifests, external references, or binary assets were modified. These reviews do **not** independently verify proof correctness, scientific findings, or historical sources.

## Audit progress (23 November 2026, batch 28)

**537 current distinct full-manuscript description audits of 2,399 lectures (22.4%)** are now recorded, up from 494 (20.7%) after batch 27. This batch **promoted the remaining 43 targeted-passage-only reviews from batch 26**, after reading each complete spoken manuscript. **No targeted-only reviews from batch 26 remain.** The 43 upgrades do not add 43 new lectures to the catalog: they complete the depth of earlier partial reviews, and the previous audit receipts remain preserved append-only.

**Nine descriptions were refined; 34 were retained unchanged.** The history previews now name the Afghan Genizah and Achaemenid administration alongside earlier periods, and the maritime-trade lecture names Barus. The operator-theory descriptions identify resolvent estimates, graph-norm convergence of spectral cutoffs, the Hilbert–Schmidt domain of a smoothed singular-value penalty, and crossed-gap assumptions for generalized frames. The linear-algebra preview adds QR, pseudoinverse and conditioning. The *Decameron* Day Four preview now recognizes the final comic reversal after nine predominantly tragic tales instead of implying a uniformly tragic ending. Technical hypotheses are described as features of the manuscripts, not independently certified proofs.

**Six topical tag lists and nine geographic place lists were expanded.** Added mathematical tags include strong versus graph-norm convergence, Cayley/Sylvester methods, operator-ideal penalties, crossed gaps and QR/least-squares methods. Historical place changes include ancient Middle Eastern cities and sites, Classic Maya centers, South and East Asian case studies, Indian Ocean ports, and Indigenous Australian and Pacific landscapes. The two *Decameron* place lists identify explicitly narrated settings of embedded fictional tales, separately from the Florence 1348 frame. The existing chronological axes and literary manuscript-witness dates were reviewed where applicable and retained. Hierarchical tag paths were already appropriate and remain unchanged. Effective inherited `track.json` tags were considered to avoid redundant sidecar indexing.

The new records include exact scopes, final manuscript and field fingerprints, `depth=full_manuscript`, and `model=GPT-6`. All previous audit ledgers are preserved. This is a **manuscript-to-metadata** audit, not external source verification, medical validation, or formal proof checking. No spoken manuscripts, track manifests, source bibliographies, graph files, or binary assets were edited. Baseline: the 23 November 2026 source snapshot (16:36 local export) with metadata batches 17–27 already present. The catalog now includes seven additional *Godzilla* lectures; no audit receipts were added for those new lectures in this batch.

## Audit progress (23 November 2026, batch 27)

**494 current distinct full-manuscript description audits of 2,392 lectures (20.7%)** are recorded, up from 469 (19.6%) after batch 26. This batch **promoted 25 existing targeted-passage reviews** after reading their entire spoken manuscripts; **43 earlier targeted-passage-only lectures remain** for complete verification. The batch is a depth upgrade of previously reviewed lectures, not 25 new catalog entries. No targeted review was silently reclassified, and the previous receipts were left intact.

**Nine descriptions were refined and sixteen passed unchanged.** The Cauchy lecture now names Cauchy-Goursat, analyticity, Cauchy estimates, Liouville and the Fundamental Theorem of Algebra. Two algebra previews now identify orbit-stabilizer/Burnside counting and the Hilbert basis theorem. Four GPT-SoapBox previews now distinguish substantial case studies, observation versus ecological inference in milky seas, and the role of selective information in cartography. The outdoor metalworking and first-aid previews now name their concrete mechanisms and age-specific instructional boundaries.

**Five topical tag lists, one hierarchical tag-path list, and three place fields were corrected.** Mathematical indexing now includes Cauchy estimates, Burnside counting, and the Hilbert basis theorem. First-aid and metalworking indexing covers airway response and nondestructive examination. The essay place additions are restricted to specific narrated examples: Cologne, Harpenden, Ise and Oslo; Haiti; and Mesopotamia, Braunschweig and Delft. All other assessed fields passed unchanged. Titles were assessed in all 25, geography where relevant, and four existing chronology records were retained after full-manuscript comparison. Effective inherited track tags were considered before adding sidecar tags.

This review examines **metadata agreement with the spoken narration**. It does not independently verify medical guidance, external scientific or historical evidence, or mathematical proofs. The archive changes sidecar metadata and appends review receipts only; no lecture manuscripts, source bibliographies, track manifests, or binary assets are edited. Its baseline is the 22 November snapshot with metadata batches 17-26 applied.

## Audit progress (23 November 2026, batch 26)

**469 current distinct full-manuscript description reviews out of 2,392 lectures (19.6%)** are recorded, up from 457 (19.1%) after batch 25. Batch 26 also added **68 further section-spanning targeted-passage audits**, which are deliberately **not counted** as full-manuscript reviews. Across 31 tracks, **80 distinct lectures** received field-specific checks this batch: 12 whole spoken texts and 68 section-by-section reviews with targeted substantive passages. The catalog currently has 68 partial-review-only descriptions and 1,855 without recorded description audits; the partial entries remain eligible for full verification. Each receipt explicitly records its depth, and none claims independent clinical, factual, historical-source, or mathematical-proof validation.

**Fifteen descriptions were corrected; 65 descriptions retained.** Revised mathematical previews distinguish the Hilbert–Schmidt versus operator-norm hypotheses for spectral gap bounds, double-angle bounds and branch choices, chain-level calculations from gluing methods in topology, Galois correspondence, and Morse/elliptic results. Practical-skills previews now reflect the breadth of narrated first-aid environmental exposures and trauma, navigation, combustion-safe retrofit diagnostics, carpentry, masonry anchoring, electrical connections, and plumbing pressure diagnostics. A long manuscript with a short accurate preview was not treated as inherently defective.

**Seventy-three topical tag lists and 65 hierarchical tag-path lists were expanded.** Mathematical tags add specific operator, spectral, geometric, proof, numerical, and algebraic methods; practical skills add safety and diagnostic mechanisms. Ancient-world history receives site-level documentary and archaeological indexing, literature entries index specific works, and the media and essay entries were checked against *effective* catalog tags inherited from each lecture's `track.json`. An empty sidecar tag list was not treated as a defect where inherited tags already supplied a subject.

**Eighteen geographic place fields were expanded**, mainly in ancient-medieval archaeological and modern-history surveys; a few literary and essay cases received explicitly narrated real-world places. Site and country entries were checked for direct manuscript support, rather than filled from general background knowledge. Fictional locations were not converted into fabricated real-world geography. Nine relevant chronology scopes were compared against narrated dates and retained without changes; no unsupported date ranges or period axes were added.

Batch 26 is based on the 22 November source snapshot after batches 17–25. Exactly **74 selected metadata sidecars** changed; six audited sidecars remained identical. The review registry adds distinct scoped receipts and preserves all earlier ledger bytes. No lecture manuscript, source bibliography, dependency graph, binary asset, or external source was changed. The targeted-passages subset is a partial audit, not a full-text audit, and should not be silently promoted into full-coverage totals.

## Audit progress (23 November 2026, batch 25)

**457 current distinct full-manuscript description reviews out of 2,392 lectures (19.1%)** are recorded, up from 379 (15.8%) after batch 24. Batch 25 adds **78** complete spoken-manuscript reviews across 28 tracks. The selection spans archaeology, paleoclimate, modern and pre-1900 literature, scientific biography, practical engineering, proof-oriented mathematics and algorithms, animation, television, and two GPT-SoapBox essays. All 78 descriptions and titles were compared against the actual narration, with covered topical and hierarchical indexing evaluated as well. Geographic and chronology fields received separately scoped checks when relevant.

**Five descriptions were corrected and 73 retained.** The population-gap spectral-statistics preview now names the Yu–Wang–Samworth population-eigengap refinement and distinguishes the principal-subspace result from eigenvector alignment. The KKT preview now identifies its sufficiency assumptions, multiplier existence, dual attainment, and nonconvex limitations. The primitive-roots preview now distinguishes finite-field multiplicative cyclicity, odd prime-power lifting, and composite-modulus counterexamples. The vernal-pool essay description now reflects conservation decisions and changing hydroperiods; the authority-and-refusal lecture now identifies its Asch, Milgram, My Lai, Tuskegee, and Challenger cases. These are claims of correspondence with manuscripts, **not** independent certification of proofs, medicine, history, or sources.

**Forty-nine topical tag lists and 59 hierarchical tag-path lists were expanded.** Retelling entries now index their particular plots, themes, and narrative techniques rather than only broad genres; archaeological lectures name the dating, conservation, and evidentiary methods they develop. Mathematical and computer-science additions identify results and constraints, including partial versus total computability, reductions, tree-dynamic-programming proof structure, and primitive-root conditions. The *Star Wars* and *Stargate SG-1* sidecars were treated separately from the effective catalog: `track.json` lecture tags already merge into the catalog, so missing sidecar tags alone were **not** counted as missing topical indexing. Those reviewed media essays needed only a few additional hierarchical paths. Exact sidecar-field differences, not mere inclusion in a review, determine the correction counts.

**Fourteen geographic place fields were expanded.** These include identified archaeological sites in South Asia, Britain, Sweden, Guatemala, Cambodia, Tanzania, and Persia; major deep-time case-study locations; grounded locations for *Beloved*, *Kindred*, and *The Remains of the Day*; the northeastern United States, Massachusetts, and California in the vernal-pool essay; and institutional case-study places for the authority-and-refusal lecture. Fictional landscapes from *Star Wars*, *Stargate SG-1*, and science-fiction novels were not turned into fabricated geographic coordinates. Selected biographies' already detailed chronology and place fields were checked and retained.

**Two chronology fields were corrected**, both in Earth-systems paleoclimate lectures: a year describing a published ice-core or marine-isotope study now uses the `work` axis instead of the `period` axis. Those publication dates do not describe the age of glacial samples or paleoenvironmental events. Other selected publication, life, and setting chronologies were checked without inventing dates to fill gaps.

Batch 25 is based on the 22 November source snapshot with batches 17–24 applied. Its 78 scoped, complete-manuscript receipts contain final manuscript and field fingerprints, a named reviewer model, and separate `clean`/`corrected` outcomes. Existing audit ledgers remain append-only. No lecture manuscript, source bibliography, external factual review, or binary asset is modified.

## Audit progress (22 November 2026, batch 24)

**379 current distinct full-manuscript description reviews out of 2,392 lectures (15.8%)** are recorded, up from 305 (12.8%) after batch 23. Batch 24 adds **74 full spoken-manuscript reviews**, twice the preceding batch: 32 global modern-history chapters, 24 advanced multivariable-calculus/PDE chapters, four Spider-Man studies, three music/audio engineering chapters, two foundational physics chapters, three scientific biographies, four modern-literature lectures, and two GPT-SoapBox essays. All were assessed against the exact narration, title, description and existing topic hierarchy; geography and chronology were scoped separately where relevant. Existing audits were preserved rather than promoted to new review depth.

**Eight descriptions needed revision; 66 were accurate and retained.** Six modern-world previews now identify substantive cases absent from the earlier summary, including Qing calendar disputes and Jaipur astronomy in the early-modern science lecture, and distinct twentieth-century political and institutional episodes. The heat-engine preview now names Carnot efficiency, heat pumps and information erasure, while the phase-transition preview distinguishes nucleation, symmetry breaking, critical scaling, glasses and superconductors. Mathematical previews were not rewritten for length or style: the reviewed PDE lectures already distinguished weak formulations, existence, compactness and regularity at the level described by the narration. These checks are not proofs of mathematical correctness.

**Seventy topic lists and 46 hierarchical tag-path sets were expanded.** The 24 selected multivariable/PDE lectures previously had no topical tags, despite substantive discussion of the Euler–Lagrange equation, weak lower semicontinuity, compact embeddings, mixed finite elements, inf–sup conditions, elliptic regularity, harmonic measure, capacity and mountain-pass existence. Comic-book previews were already accurate but lacked topical tags; music chapters were indexed by broad production categories without their signal-processing mechanisms. Modern-literature additions distinguish the original fictional works and their literary method, rather than using only `Literature` and `Novels`.

**Thirty-nine place fields were expanded**, chiefly in global modern-history chapters whose narration names regional cases while the field records an entire ocean, continent or geopolitical period. This includes Indian Ocean ports, Atlantic plantation economies, interwar anticolonial movements, Asian decolonization, African structural adjustment, and later migration and global-supply-chain cases. Scientific biography `spacetime_coverage` remains unchanged; simpler `places` arrays now include previously omitted, explicitly narrated visits and educational settings. *Things Fall Apart* is indexed to southeastern Nigeria without treating fictional Umuofia as a real mappable settlement; the invented worlds of *The Dispossessed* have no fabricated real-world places. The two GPT-SoapBox essays already had detailed thematic and hierarchical indexing, so changes were restricted to significant, narrated case-study locations.

**Seven chronology scopes were checked and remained unchanged:** three scientific lives with detailed recorded dates and four published works dated within their narrations. An author's lifespan, publication year and fictional setting remain different kinds of dates. Composite historical surveys were not assigned a single invented year range. The 74 full-manuscript receipts have field-specific `clean` or `corrected` outcomes for exactly the scopes reviewed, and current hashes of the final metadata and spoken text. No receipt asserts independent fact-checking, historical-source verification, clinical validation or formal proof certification.

Batch 24 is based on the 22 November source snapshot after batches 17–23, and modifies only 74 selected metadata sidecars, eight append-only audit ledgers, and this progress document. No lecture manuscripts, source registries, claims, dependency graphs or binary assets were changed.
