# Uploaded content additions, 16 November 2026

Inspected 81 uploaded ZIPs in ignored `untracked/` storage (72 distinct byte
archives). Existing versions, duplicates, and fragments already absorbed into
combined lectures were skipped, following the user's instruction to integrate
only obviously new data.

| Source archive | New material | Destination |
| --- | --- | --- |
| `journey-to-the-west-chapters-76-81-overlay.zip` | Six lectures, IDs 549000–554000 | `draft-stages/tts-pre-1900-literature/` |
| `journey-to-the-west-chapters-82-87-overlay.zip` | Six lectures, IDs 555000–560000 | Same pack |
| `ancient-geographic-rotation-2026-11-16-overlay.zip` | Seven lectures, IDs 054000–060000: Medea, three Buddhacarita parts, Li Sao, Zamyad Yasht, and Setne | `content/literature-survey/` |

The original Journey imports encountered differing existing provenance or README
files. The importer protects those files by refusing the whole batch. Filtered
addition batches were applied through `tools/content_overlay.py`, preserving
current catalogs and existing source variants while adding the new manuscripts,
metadata, 29 reading records, and continuation notes. Recovery copies remain in
ignored `.content-update/` storage. Original uploaded archives remain untouched.

Journey now has 72 expanded-retelling manuscripts through chapter 87; the next
authoring chapter is 88. Chapters 88–100 remain unfinished. The full pre-1900
pack has 123 indexed manuscripts; the literature-survey pack has 58. Counts are
snapshots, not authoring constraints.

Focused checks validated extraction, metadata, all 424 new exact source anchors,
source references, current index files, and curated route membership. Prior track
entries and source records were preserved. No narration was rewritten or audio
generated. Import/coherent-reader and crash-recovery checks passed. Every
uploaded manuscript ID was accounted for as current or an absorbed component;
this does not assert that differing old documents were reconciled.

Integration and audit by GPT-6 (exact runtime variant unavailable). Original
content authorship remains recorded in the imported metadata and provenance.
