# Spider-Man: The Comics, the Character, and the Culture

A self-contained, audio-first, general-audience lecture track on the history, storytelling, and cultural afterlives of Spider-Man. The track treats **Spider-Man as a collaborative comics creation**, rather than collapsing him into a single film continuity or describing fictional events as publication history.

## First installment: four full manuscripts

| ID | Lecture | Scope |
| --- | --- | --- |
| 001000 | Spider-Man Is Born | 1962 origin, Stan Lee and Steve Ditko, the page as a visual medium, moral responsibility |
| 002000 | Peter Parker's First Decade | *Amazing Spider-Man* #1–122, graduation into adulthood, supporting cast, Goblin, Gwen's death |
| 003000 | The Spider-Man Story Engine | Moral limits, time conflicts, work and money, public reputation, secrecy, and urban setting |
| 004000 | The Mask Beyond Peter Parker | Black suit/Venom, evolving Peter, *Ultimate Spider-Man*, Miles, Gwen, Spider-Verse and adaptations |

The default listening route includes all four in this order. Manuscripts are **complete spoken lectures**, not brief outlines. They contain spoilers for major early comics and selected modern continuities, marked at the top of each file.

## Source discipline

- The 1962 issue, selected comic bibliographies, Library of Congress archival resources, publisher reading lists, creator credits, and studio/award records are identified in `metadata/sources.json`.
- Each lecture has claim-level anchors and cited source IDs in `metadata/<lecture-id>.json`.
- The non-spoken companions include direct links to relevant **Wikipedia** articles for further orientation; primary issue and archival records are preferred for claims about creators and publication history.
- Interpretation is identified as criticism, not attributed to a creator unless supported by a named source. The track distinguishes *Amazing Fantasy* #15 from later adaptations of Uncle Ben's moral, and distinguishes mainstream Marvel, Ultimate, Earth-65, and film worlds.
- No scanned art, comic panels, copyrighted dialogue, audio, or other binary media are included. This pack is original critical and historical narration, not a reproduction of the comics.

## Packaging and integration

The entire source pack is under `draft-stages/tts-spider-man/`, with independent metadata and no edits to shared publishing tools. Apply via the existing `tools/content_overlay.py apply` importer. Existing TTS workflows can discover the track when the pack is imported. Audio has not been generated.

New material should append lectures under stable IDs and update the pack-owned `track.json`, `navigation.json` when needed, claim sidecars, and source records. See `BACKLOG.md` for the candidate expansion route; it is not an indexed set of draft lectures.

**Editorial principle:** Substantive lectures should be as long as the material warrants. Do not turn every comic issue into one lecture or make a list of disconnected trivia. Historical authorship, primary narrative, and critical interpretation are different subjects and should remain intelligible when heard aloud.
