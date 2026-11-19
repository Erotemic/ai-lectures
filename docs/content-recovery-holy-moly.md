# Holy-moly content recovery

18 November 2026. Integration by GPT-6 (Codex; weights/config variant unknown).

Compared all 63 manuscript candidates from 22 recovered original ZIPs against the current checkout, rather than importing their older shared catalogs wholesale. The larger raw filename audit includes deliberately consolidated files and is not a lost-content inventory.

- Restored **23 missing manuscripts**: 17 biographies and six mathematical connections.
- Of those biographies, ten already had catalog entries but lacked their files; seven require new catalog entries.
- **34 candidates were already byte-for-byte present**: nine chemistry, two SoapBox, nine Dynamic Earth, and 14 American-history lectures. The American-history directories were untracked and are included in the recovery commit.
- Left **six superseded Earth-systems alternatives** in the supplied recovery archive; their topics have current treatments listed below.

The recoverable import used `tools/content_overlay.py apply` with current base hashes and an undo copy. Existing manuscript speech, playback IDs, source records and route membership were preserved. The new material retains its supplied prose, display companions, historical claims, spacetime evidence and references. This is an integration check, not a fresh factual review or stylistic rewrite.

## Restored biographies

The six occupied original IDs are remapped. In particular, `history:133000` remains Faraday, `134000` remains the shorter Darwin biography, `135000` remains Meitner, `136000` remains McClintock, `137000` remains Lavoisier, and `138000` remains Pasteur. The longer recovered Darwin account is a separately titled expanded treatment.

| Current lecture | Original ID |
| --- | --- |
| [162000 · Grigori Perelman: The geometry of a proof, and the right to refuse](../draft-stages/tts-history/162000-perelman.md) | 133000 |
| [163000 · Girolamo Cardano: A secret, a wager, and the price of a reputation](../draft-stages/tts-history/163000-cardano.md) | 134000 |
| [164000 · Niccolò Tartaglia: The teacher who would not surrender his discovery](../draft-stages/tts-history/164000-tartaglia.md) | 135000 |
| [165000 · Julia Robinson: The birthday wish and the problem no machine could solve](../draft-stages/tts-history/165000-julia-robinson.md) | 136000 |
| [166000 · Charles Darwin: Five years at sea, twenty years of evidence](../draft-stages/tts-history/166000-darwin.md) | 137000 |
| [167000 · Albert Einstein: A life spent questioning what seems obvious](../draft-stages/tts-history/167000-einstein.md) | 138000 |
| [148000 · Subrahmanyan Chandrasekhar: The weight a star can bear](../draft-stages/tts-history/148000-chandrasekhar.md) | 148000 |
| [149000 · Dorothy Crowfoot Hodgkin: Making the invisible visible](../draft-stages/tts-history/149000-hodgkin.md) | 149000 |
| [150000 · Jocelyn Bell Burnell: The signal in the noise](../draft-stages/tts-history/150000-bell-burnell.md) | 150000 |
| [151000 · Alfred Wegener: The continents that would not stay still](../draft-stages/tts-history/151000-wegener.md) | 151000 |
| [152000 · Marie Tharp: The ocean floor was not blank](../draft-stages/tts-history/152000-tharp.md) | 152000 |
| [153000 · Fritz Haber: Bread from air](../draft-stages/tts-history/153000-haber-nitrogen.md) | 153000 |
| [153500 · Fritz Haber: War, exile, and the weight of a discovery](../draft-stages/tts-history/153500-haber-war-exile.md) | 153500 |
| [154000 · Ignaz Semmelweis: The deadly difference between two wards](../draft-stages/tts-history/154000-semmelweis.md) | 154000 |
| [155000 · Tycho Brahe: An Island Built to Measure the Heavens](../draft-stages/tts-history/155000-tycho-brahe.md) | 155000 |
| [156000 · Tu Youyou: The fever, the archive, and sample 191](../draft-stages/tts-history/156000-tu-youyou.md) | 156000 |
| [161000 · Vera Rubin: The Speed of the Invisible](../draft-stages/tts-history/161000-vera-rubin.md) | 161000 |

## Restored mathematical connections

The new lectures have explicit teaching-preparation metadata and focused routes. Existing surveys retain their previous membership. The mathematics guide adds three cross-subject paths: derivatives to optimization, least squares to conditional prediction, and measurement to uncertainty.

| Lecture | Subject |
| --- | --- |
| [One Fit, Three Mathematical Languages: Projection, Optimization, and Statistical Evidence](../draft-stages/tts-linear-algebra/028000-one-fit-three-mathematical-languages.md) | linear-algebra |
| [What a Gradient Depends On: Differentials, Geometry, and Steepest Descent](../draft-stages/tts-multivariable-calculus/071000-what-a-gradient-depends-on.md) | multivariable-calculus |
| [From Jacobians to Uncertainty Budgets: Errors, Correlations, and Nonlinearity](../draft-stages/tts-multivariable-calculus/072000-jacobians-and-uncertainty-budgets.md) | multivariable-calculus |
| [The Chain Rule Run Backward: Gradients, Backpropagation, and Adjoint Sensitivity](../draft-stages/tts-multivariable-calculus/073000-the-chain-rule-run-backwards.md) | multivariable-calculus |
| [Curvature, Conditioning, and Regularization: Why Optimization Speed Is Geometric](../draft-stages/tts-optimization-duality/017000-curvature-conditioning-and-regularization.md) | optimization-duality |
| [Conditional Expectation as Projection: Why Regression Is Only One Kind of Prediction](../draft-stages/tts-probability-measure/036000-conditional-expectation-as-projection.md) | probability-measure |

## Superseded Earth-systems alternatives

These have different prose, not byte-identical replacements. The current lectures cover their central mechanisms and examples, often in more focused treatments. Their original manuscripts and companions remain recoverable from the original ZIP bundle. No occupied IDs or current narration were replaced.

| Recovered draft | Current treatment |
| --- | --- |
| 026000-why-the-sea-has-a-tide.md | [Why High Tide Is Late: Gravity, Basins, and Moving Water](../content/earth-systems/032000-why-high-tide-is-late.md) |
| 027000-a-beach-is-a-moving-inventory.md | [The Beach Is a Conveyor: Waves, Sand, and a Moving Shoreline](../content/earth-systems/033000-the-beach-is-a-conveyor.md); [An Island That Moves: Dunes, Storms, and the Barrier Coast](../content/earth-systems/034000-an-island-that-moves.md) |
| 028000-the-coast-is-not-a-line.md | [An Island That Moves: Dunes, Storms, and the Barrier Coast](../content/earth-systems/034000-an-island-that-moves.md); [The River Meets Salt: How Estuaries Exchange Water and Life](../content/earth-systems/035000-the-river-meets-salt.md); [A Delta Is a Temporary Promise: Rivers, Mud, and Sinking Ground](../content/earth-systems/036000-a-delta-is-a-temporary-promise.md) |
| 029000-where-the-equations-meet-the-grid.md | [A Planet in Finite Boxes: The Laws Behind an Earth System Model](../content/earth-systems/026000-a-planet-in-finite-boxes.md); [The Weather Inside a Grid Cell: Clouds, Turbulence, and Tuning](../content/earth-systems/027000-weather-inside-a-grid-cell.md); [When Models Share a Boundary: Coupling the Ocean, Air, Ice, and Living Earth](../content/earth-systems/028000-when-models-share-a-boundary.md) |
| 030000-how-a-forecast-learns-the-present.md | [A Forecast Begins with a Guess: Observations, Data Assimilation, and Reanalysis](../content/earth-systems/029000-a-forecast-begins-with-a-guess.md) |
| 031000-what-kind-of-future-is-a-model-showing.md | [A Second Earth for Experiments: Controls, Forcings, and Climate Projections](../content/earth-systems/030000-a-second-earth-for-experiments.md); [When a Climate Model Is Wrong: Testing Skill, Uncertainty, and Trust](../content/earth-systems/031000-testing-a-climate-model.md) |

## Validation and provenance

Focused pack reads validate extraction, unique IDs, source resolution, metadata and navigation. Every pre-existing usable lecture in the affected packs retains its spoken hash. All 23 restored manuscripts match the original archive’s extracted speech; counts were measured from that speech. The reader API exposes the 23 lectures, all seven added routes, and resolves their prerequisite and route links. No runtime media export, TTS generation or live service restart was performed.

Each restored lecture sidecar records the original archive name and SHA-256, original manuscript path and hash, original ID and the integration scope under `content_recovery`. Existing model records are retained; integration provenance does not claim original authorship of the recovered prose.

Original bundle: `recovered-original-lecture-overlays-2026-11-18.zip`; SHA-256 `d630a5cabe4368da49a80ca77a50d8382c8a5d0e9c072ac4b8d2f5cb060b9c94`.
