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

- `010000`: **Gunditjmara: Budj Bim and the Living Country**. An attributed
  educational encounter with a **living** Gunditjmara creation account and the
  linked Stone Country/Sea Country landscape; includes kooyang aquaculture,
  colonisation, and water restoration. This is **not** a reproduction or an
  authorized Gunditjmara songline performance. Its claim records and cultural-IP
  boundaries are in `metadata/010000.json` and the manuscript companion.

- `011000`: **Klamath: Llao, Skell, and the Heart at Crater Lake**. A
  narrative reading of the stolen heart, its recovery, the battle with
  Llao and the Wizard Island ending, with a distinct creation account
  attributed to Perry Chocktoot and geological context. The main story
  relies on scholarly **synopses** of Robert David's Klamath-language
  record; Barker (1963) pp. 71–75 remain to be checked directly. Not an
  authorized Klamath performance. See `metadata/011000.json`.

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

## Ancient epics, narrative literature, and the next written-work expansion

- `012000`: **Theogony: The Violent Birth of Order**. Hesiod's entire surviving poem traversed in narrative order, including the opening Muses, divine births, Cronus, Prometheus, the Titan war, Typhoeus and Zeus's settlement. Does not merge Pandora's jar from *Works and Days*.
- `013000`–`015000`: **Genesis, three narrative parts**. Received chapters 1–11 (creation through Babel); 12–36 (Abraham, Sarah, Hagar, Isaac, Rebekah, Esau, Jacob, Leah, Rachel, Dinah); 37–50 (Joseph, Judah and Tamar, famine, reconciliation and Joseph's coffin). Literary history and theological interpretation are distinguished from independently verified history.
- `016000`: **Oresteia: The House That Could Not Stop Killing**. All three surviving plays: *Agamemnon*, *Libation Bearers* and *Eumenides*, ending with the contested tied acquittal and Athena's accommodation of the Furies. Not an invented reconstruction of the lost *Proteus*.
- `017000`–`018000`: **The Panchatantra**, a two-part retelling of the five principal book frames and selected nested stories. The identified text is Purnabhadra's 1199 Sanskrit recension, read through Arthur Ryder's 1925 translation; this is not the lost ancient urtext.

The sixteenth-century or modern history of a work's translations is not treated as its original date. Each new lecture has independently checkable plot anchors, source locators, public-domain orientation links, and measured speech counts. The written-work queue remains open for further full narratives.

## Ancient narrative works — next full-story batch (2026-11-16)

The next four roadmap commissions are now **authored and indexed** as nine recordings, using the previous IDs and source names unchanged. Their speaking durations are measurements, not editing targets.

| IDs | Received work | Scope |
|---|---|---|
| `019000`–`020000` | *Zhuangzi* | Inner Chapters 1–7 and explicitly separate selected Outer Chapter parables; no fiction of a continuous original novel or uniformly identifiable single author. |
| `021000`–`023000` | Apuleius, *The Golden Ass* | Books I–XI; Lucius, the framed Cupid-and-Psyche tale, changing masters, and Isis/Osiris ending. Not Ovid. |
| `024000`–`026000` | *Exodus* | Received chapters 1–40; oppression and escape, wilderness and law, tabernacle plan, golden calf and renewal, completion and cloud. |
| `027000` | Kālidāsa, *Śakuntalā* | Seven-act recognition drama; kept distinct from the epic *Mahābhārata* version. |

Individual manuscripts list their primary-text/translation boundaries, public sources and Wikipedia orientation links. Claim anchors in `metadata/0xxxxx.json` point to specific received chapters, books or acts; interpretation is original narration, not a quotation of a translation. No generated audio or images are included.

## Homeric Hymns and Sophocles — full narratives (2026-11-16)

Six new original narrations follow separately transmitted Greek works rather than a fabricated single mythological novel.

- `028000`: **The Homeric Hymn to Demeter: The Season of Loss** (2,099 spoken words; 14.5 minutes at 145 wpm). Claim locators: `metadata/028000.json`.
- `029000`: **The Homeric Hymn to Apollo: The Island and the Mountain** (2,031 spoken words; 14 minutes at 145 wpm). Claim locators: `metadata/029000.json`.
- `030000`: **The Homeric Hymn to Hermes: A Newborn Thief and a New Song** (1,954 spoken words; 13.5 minutes at 145 wpm). Claim locators: `metadata/030000.json`.
- `031000`: **The Homeric Hymn to Aphrodite: The Goddess on the Mountain** (1,860 spoken words; 12.8 minutes at 145 wpm). Claim locators: `metadata/031000.json`.
- `032000`: **Sophocles, Oedipus Tyrannus: The King Who Investigated Himself** (2,694 spoken words; 18.6 minutes at 145 wpm). Claim locators: `metadata/032000.json`.
- `033000`: **Sophocles, Antigone: The Law and the Dead** (2,439 spoken words; 16.8 minutes at 145 wpm). Claim locators: `metadata/033000.json`.

The four long hymns are anonymous poems collected under a conventional Homeric label. The Delian and Pythian movements of the Apollo hymn may have distinct composition histories. Sophocles's tragedies are separately composed plays, not a single Theban trilogy; their legendary sequence need not match production chronology. Companion and source records distinguish received-story claims from historical evidence. No audio, slides or other binary media are included.
