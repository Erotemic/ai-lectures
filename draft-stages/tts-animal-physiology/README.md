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

The course is **in progress**, not a completed finite survey. These chapters constitute a coherent initial set; follow-up chapters can deepen the physiology without extending the finished `tts-living-world` and `tts-physical-world` surveys or duplicating their nature-story framing. `tts-cell-biology-genetics` offers optional molecular background. No other pack needs to be changed to import this one.

## Files and authoring contract

- `track.json`: stable lecture order, broad course tags, lecture-specific flat tags, and explicit sections.
- `navigation.json`: complete initial listening path plus specialist routes for exchange/transport and comparative solutions.
- `metadata/NNNNNN.json`: discovery descriptions, explicit coarse-to-fine `tag_paths`, relevant article or textbook sources, source-checked narration anchors, and lecture learning notes.
- `metadata/sources.json`: a pack-local catalog of primary papers, scholarly reviews and open textbooks.
- `NNNNNN-*.md`: narrated lecture between spoken markers, followed by scientific notes, equations, and reference links outside the TTS region.

Track tags are intentionally broad. More specific terms (for example `Bohr effect`, `Nephron`, `Revised Starling principle`, `Cecotrophy`) belong on the appropriate lectures, not across the entire course. For geography, the Mojave Desert is associated with lecture 004000 because that manuscript discusses an identified field investigation there. General physiological mechanisms are not assigned artificial years, historical periods, or locations. References' publication dates are bibliographic data, not chronology covering the lecture itself.

The recorded `spoken_words` and estimated speaking times are **descriptive measurements**, never an editorial minimum, maximum or target.

## Local checks and application

From the repository root:

```bash
python draft-stages/tts-lectures/extract_narration.py --check draft-stages/tts-animal-physiology/0*.md
python tools/sync_spoken_metadata.py --tracks animal-physiology
```

For a ZIP handoff, use `python tools/content_overlay.py apply /path/to/overlay.zip`. A new pack does **not** require `--replace-owned`. This only imports the authoring sources; it does not synthesize audio or modify runtime code.
