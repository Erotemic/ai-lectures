# Spider-Man: The Comics, the Character, and the Culture

An **entertaining, source-grounded collection of Spider-Man audio essays** for fans and curious newcomers. These are not prose adaptations of the comics or encyclopedic issue recaps. Plots are summarized when needed to make an argument about artists, film technique, characters, history, or editorial choices intelligible to listeners who know Peter and Miles mainly from screen adaptations.

## Default listening route: Fan Essays and Deep Dives

The eight deeper essays stand alone, with concepts and continuities explained when first introduced. Their order is a useful path but not a prerequisite chain.

| ID | Essay | The interesting question |
| --- | --- | --- |
| 005000 | Steve Ditko, Stan Lee, and the Spider-Man You Can Feel in a Drawing | Who made Spider-Man's earliest visual personality, and why is credit hard to assign? |
| 006000 | J. Jonah Jameson: A Man Who Keeps Hiring His Own Worst Enemy | What makes Jameson more than a recurring joke? |
| 007000 | How Spider-Man's Villains Hurt Him Without Winning the Fight | Why do different villains threaten different parts of Peter's life? |
| 008000 | Clones, Marriage, and the Problem of Letting Peter Parker Grow Up | Why does long-running continuity resist personal change? |
| 009000 | Three Movie Spider-Men, Three Different Problems | How do Raimi, Webb, and Watts pose different questions for the same hero? |
| 010000 | Why the Spider-Verse Films Look and Sound Like Thoughts | How can frames, compositing, collage, and music enact Miles's story? |
| 011000 | How to Draw a Web-Swing: Spider-Man's Artists and the City Beneath Him | How do Ditko, Romita, Andru, McFarlane, Bagley and Pichelli make a body travel through panels? |
| 017000 | Kraven's Last Hunt: The Villain Who Thought the Costume Was the Man | Why can Kraven win his self-invented contest and fail the ethical one? |

**Spoilers:** These essays discuss major outcomes in comics and films. Every manuscript includes a non-spoken spoiler notice, including the dark ending of *Kraven's Last Hunt*. Visual criticism is narrated so that it makes sense without accompanying images. Production claims are sourced to credited artists, production staff, studios, original comics records, or creators' own retrospective testimony, with those source types distinguished in metadata.

## The Essentials in Four Essays

Lectures 001000–004000 are a separate newcomer-friendly collection, already revised before this installment. They remain **byte-for-byte unchanged** in this update.

| ID | Essay | Context provided |
| --- | --- | --- |
| 001000 | Spider-Man Is Born | *Amazing Fantasy* #15, Lee and Ditko, Peter's original moral mistake |
| 002000 | Peter Parker's First Decade | High school and college, the supporting cast, the Goblin, Gwen Stacy |
| 003000 | The Spider-Man Story Engine | Responsibility, secrecy, money, the city, and time |
| 004000 | The Mask Beyond Peter Parker | Black suit, symbiotes, Miles Morales, and the Spider-Verse |

`navigation.json` keeps `fan-essays` as the default collection, `survey` as the four-essay introduction, and `complete` as a twelve-essay route. A further `comics-and-screen-craft` route connects the new visual-media discussions. IDs 012000–016000 remain open for future essays; Kraven is ID 017000 to avoid reserving one of those IDs.

## Text-only pack and provenance

All content is in `draft-stages/tts-spider-man/`, including the twelve complete manuscripts, `track.json`, `navigation.json`, twelve `metadata/NNNNNN.json` claim maps, `metadata/sources.json`, `BACKLOG.md`, and this README. Spoken narration appears exclusively inside `BEGIN SPOKEN LECTURE` and `END SPOKEN LECTURE` markers. Non-spoken source companions include relevant Wikipedia articles for reference and official/primary production records, catalogs, interviews and archives for factual grounding. Interpretation is distinguished from production history. No comic pages, movie footage, binary art or music is embedded.

To import the ZIP from the repository root (fresh installs and replacements supported):

```bash
python tools/content_overlay.py apply ~/Downloads/spider-man-fan-essays-04.zip --replace-owned
```

The importer safeguards conflicting pack-owned files with recovery backups when replacement is selected. It does not overwrite unrelated content or require shared publishing-code edits.
