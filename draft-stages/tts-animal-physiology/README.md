# How Animals Work: Comparative Physiology

An independent, audio-first nature-and-science content pack about the physical and biological work required to keep an animal alive. The guiding question is **how different organisms solve shared physiological problems** rather than how to memorize the anatomy of one species. The narration develops mechanisms, measurements, tradeoffs, and experimentally testable explanations in continuous spoken prose.

## Published manuscripts in this handoff

| Stable ID | Title | Problem investigated |
| --- | --- | --- |
| 001000 | The Environment Inside an Animal | Homeostasis, set points, sensors, effectors, negative feedback, acclimatization and evolution. |
| 002000 | How an Animal Gets Oxygen | Diffusion and partial pressure; gills, lungs, air sacs, insect tracheae, hemoglobin and hypoxia. |
| 003000 | Circulation Is More Than a Heart | Pressure, flow, hydraulic resistance, cardiac output, capillary exchange, lymphatics and comparative architectures. |
| 004000 | The Price of Keeping Water | Osmotic gradients, fish and shark strategies, kidneys, Malpighian tubules, nitrogen waste, salt glands and desert water budgets. |
| 005000 | How Food Becomes an Animal | Digestion and absorption, energy budgets, rumen and hindgut fermentation, gut microbes and plastic digestive capacity. |
| 006000 | What Muscles Pull Against | Sarcomeres, ATP and calcium, skeletons and muscular hydrostats, tendons, locomotion and cost of transport. |
| 007000 | How a Nerve Signal Travels | Ionic gradients, action potentials, the squid axon, synapses, myelin and distributed arm control in octopuses. |
| 008000 | How a Body Knows Where It Is | Touch, body position, insect strain sensors, hair cells, lateral-line flow, vestibular balance and hearing. |
| 009000 | What Light Becomes | Photons, retinal transduction, eye optics, sensitivity, color information and mantis-shrimp behavior experiments. |
| 010000 | Senses Without a Picture | Chemical patterns, insect odor tracking, contact taste, electroreception and infrared pit organs. |
| 011000 | A Body in the Weather | Heat transfer, endothermy and ectothermy, thermoneutrality, insulation, countercurrent exchange, penguin huddles and evaporative cooling. |
| 012000 | What Metabolism Measures | ATP and energy expenditure, direct and indirect calorimetry, field estimates, aerobic scope, and contested metabolic scaling exponents. |
| 013000 | When Life Slows Down | Hummingbird torpor, bear hibernation, subzero squirrel supercooling, insect diapause, and protective wood frog freezing. |
| 014000 | Messages in the Blood | Secretin, receptors and second messengers; hormone routes, feedback, transport and measurement. |
| 015000 | The Meal, the Fast, and the Pancreas | Insulin, glucagon, gut incretins, leptin, fuel allocation and the Toronto insulin discovery. |
| 016000 | A Stress Response Has a History | Sympathetic control, the HPA axis, glucocorticoid pulses, sampling and recovery. |
| 017000 | When a Body Changes Its Rules | Frog and insect metamorphosis, gonadotropin pulses and melatonin seasonal coding. |

The course is **in progress**, not a completed finite survey. These seventeen chapters build a coherent sequence from physiological systems into thermal, energetic and endocrine regulation; follow-up chapters can deepen the physiology without extending the finished `tts-living-world` and `tts-physical-world` surveys or duplicating their nature-story framing. `tts-cell-biology-genetics` offers optional molecular background. No other pack needs to be changed to import this one.

## Files and authoring contract

- `track.json`: stable lecture order, broad course tags, lecture-specific flat tags, and explicit sections.
- `navigation.json`: expanded main listening path plus deep dives on exchange/transport, comparative solutions, movement/control, sensory physiology, and temperature/energy, and endocrine coordination.
- `metadata/NNNNNN.json`: discovery descriptions, explicit coarse-to-fine `tag_paths`, relevant article or textbook sources, source-checked narration anchors, and lecture learning notes.
- `metadata/sources.json`: a pack-local catalog of primary papers, scholarly reviews and open textbooks.
- `NNNNNN-*.md`: narrated lecture between spoken markers, followed by scientific notes, equations, and reference links outside the TTS region.

Track tags are intentionally broad. More specific terms (for example `Bohr effect`, `Nephron`, `Revised Starling principle`, `Cecotrophy`) belong on the appropriate lectures, not across the entire course. For geography, the Mojave Desert is associated with lecture 004000 because that manuscript discusses an identified field investigation there. The movement and nerve chapters reference historically dated experiments (sliding filaments in 1954; squid-axon conductance studies in 1952), but their subject is biological mechanism, so those publication years belong in sources and evidence anchors rather than top-level period-coverage fields. General physiological mechanisms are not assigned artificial years, historical periods, or locations. References' publication dates are bibliographic data, not chronology covering the lecture itself.

The thermal and metabolic chapters include dated 1950 chamber experiments in Alaska and Panama, Antarctic penguin observations, and specific work in the Andes and Alaska; their source locations are discoverable but mechanism chapters are not assigned historical periods from publication dates. The sensory chapters discuss dated experimental work on rods (1979), olfactory receptors (1991), insect OR channels (2008), snake infrared receptors (2010), and mantis-shrimp color (2014). Their mechanisms are not assigned artificial place or period tags; years remain in evidence records and reading notes.

The endocrine unit develops chemical communication across four distinct explanatory problems: general hormone receptors and feedback; energy allocation between meals; acute and longer stress-response timing; and developmental and seasonal scheduling. The historical research in secretin, insulin and GnRH is attributed within the manuscripts and source records. **Toronto** is indexed for the documented insulin discovery; **Puerto Rico** is indexed for the native coquí case. None of the general endocrine mechanisms is assigned a synthetic historical coverage period just because a reference paper was published in a particular year.

The recorded `spoken_words` and estimated speaking times are **descriptive measurements**, never an editorial minimum, maximum or target.

## Local checks and application

From the repository root:

```bash
python draft-stages/tts-lectures/extract_narration.py --check draft-stages/tts-animal-physiology/0*.md
python tools/sync_spoken_metadata.py --tracks animal-physiology
```

For a ZIP handoff, use `python tools/content_overlay.py apply /path/to/overlay.zip`. For an existing pack, changes to previously installed `track.json`, `navigation.json`, `README.md`, `BACKLOG.md` and `sources.json` require `--replace-owned` in the exclusively owned pack scope; the importer retains recovery copies. Run `--check` first if local edits may conflict. This only imports the authoring sources; it does not synthesize audio or modify runtime code.
