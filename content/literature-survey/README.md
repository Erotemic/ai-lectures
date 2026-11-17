# Literature: standalone introductions and narrative readings

This independently owned pack supplies standalone readings of literary works.
Some have longer studies elsewhere in the library; the new ancient narratives
are complete, source-supported readings in their own right. The introductions establish
their own characters, settings, narrative arcs, and interpretive questions.
They discuss endings. Exact episode durations are descriptive estimates, not
conditions for acceptance.

Currently indexed:

- `001000`: **The Decameron: A World Made by Telling**. The complete frame and
  selected tales explain the structure and interpretive range of the whole book.
  This is not a retelling of all one hundred tales. Extended study:
  `pre-1900-literature:decameron`.
- `002000`: **Three Kingdoms: The Price of Loyalty**. The received novel's entire
  political arc, from the oath to reunification, with historical and fictional
  evidence distinguished. Extended study: `world-history:three-kingdoms`.
- `003000`: **Shahnameh: Kings, Heroes, and the World They Lose**. The poem's
  whole arc through selected episodes, with legendary and historical modes
  distinguished. Extended study: `world-history:shahnameh`.

- `006000`: **The Aeneid: The Cost of a Promised Future**. All twelve books,
  including the fall of Troy, Dido, the underworld, the Italian war, and the last
  killing. Standalone addition to the ancient route.
- `007000`: **The Argonautica: Medea and the Voyage of the Argo**. The full
  outward voyage, quest, and return in Apollonius's four-book poem, with Medea's
  agency and the Apsyrtus episode retained.
- `008000`: **Metamorphoses: A World That Will Not Stay Still**. A connected
  traversal of all fifteen books through representative scenes, *not* every tale
  in the collection.
- `009000`: **Nala and Damayanti: The King Who Lost at Dice**. The entire embedded
  Mahabharata episode, including the second wager's ethically difficult terms.
  Companion to `world-history:024000`, which introduces the tale briefly.

The reader also exposes five period routes assembled from existing recordings
across packs. Those routes link to extended studies and explicitly identify
unfinished openings. Further introductory prose is optional future authoring;
organization does not depend on completing every expansion or synopsis.

The authoring boundaries and optional IDs are recorded in
[the authoring scope](notes/authoring-scope.md).
Only usable manuscripts appear in `track.json`. Source records, claim anchors,
and transcript attribution accompany each indexed lecture. The separate
`provenance.yaml` records authorship of these new texts; it does not reassign
authorship of the earlier deep dives or the primary literary works.

The reader discovers this pack without a registry edit. No synthesis or runtime
pack build is necessary to review a source addition. Run focused source checks
with `python -m pytest -q tests/test_literature_survey_pack.py`.
