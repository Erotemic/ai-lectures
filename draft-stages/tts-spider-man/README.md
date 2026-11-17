# Spider-Man: The Comics, the Character, and the Culture

A **source-grounded audio-essay track for Spider-Man fans and curious newcomers**. Its purpose is an enjoyable listen, not a comic-by-comic recap or a narrated adaptation. Stories are explained whenever an example needs context, but the central attractions are creative personalities, memorable scenes, arguments about character, artwork and sound, production decisions, and the history of the character across media. Spoilers are flagged before the spoken narration in each manuscript. There is no required word count or running time.

## Start here

`navigation.json` defines five listening collections. **Fan Essays and Deep Dives** (`fan-essays`) is the default. The essays generally stand alone; the four introductory essays offer a route for listeners wanting more history and context before beginning. Other collections are **The Essentials in Four Essays** (`survey`), **Every Lecture** (`complete`), **Drawing and Filming the Hero** (`comics-and-screen-craft`), and **Responsibility, Work, and Time** (`peter-and-his-world`).

## The Essentials in Four Essays

| ID | Lecture | Background given |
| --- | --- | --- |
| 001000 | Spider-Man Is Born | The 1962 *Amazing Fantasy* #15 origin, Lee and Ditko, Peter's early mistake. |
| 002000 | Peter Parker's First Decade | School, work, supporting cast, Norman Osborn and Gwen Stacy. |
| 003000 | The Spider-Man Story Engine | Responsibility, secrecy, time, money, relationships and New York. |
| 004000 | The Mask Beyond Peter Parker | Costume and symbiote history, Miles Morales, and the Spider-Verse. |

## Fan Essays and Deep Dives

| ID | Essay | Central question |
| --- | --- | --- |
| 005000 | Steve Ditko, Stan Lee, and the Spider-Man You Can Feel in a Drawing | Where did the character's first visual personality come from? |
| 006000 | J. Jonah Jameson: A Man Who Keeps Hiring His Own Worst Enemy | Why is Jonah more than a recurring joke? |
| 007000 | How Spider-Man's Villains Hurt Him Without Winning the Fight | What do the best villains threaten other than his survival? |
| 008000 | Clones, Marriage, and the Problem of Letting Peter Parker Grow Up | Why does a long serial resist its hero's adulthood? |
| 009000 | Three Movie Spider-Men, Three Different Problems | What questions do Raimi, Webb and Watts ask of Peter? |
| 010000 | Why the Spider-Verse Films Look and Sound Like Thoughts | How do art direction, timing and music enact Miles's story? |
| 011000 | How to Draw a Web-Swing | How do great comics artists convey motion in still drawings? |
| 012000 | Why Spider-Man Is a Videogame Hero | How can the act of moving through a city reveal the character? |
| 013000 | Venom: From Nightmare to Antihero to Cosmic Monster | How did an antagonist become several kinds of protagonist? |
| 014000 | Miles Morales Was Not Built to Be Peter Parker Two | What makes comic-book Miles's beginning distinct? |
| 015000 | When Spider-Man Met the Goblin and the Comics Got Dangerous | What did Norman's rivalry change about the series? |
| 016000 | The Supporting Cast Has a Life of Its Own | Who makes decisions that are not just reactions to Peter? |
| 017000 | Kraven's Last Hunt | Why is a villain's apparent victory a moral defeat? |
| 018000 | Doctor Octopus: The Doctor Who Stole Spider-Man and Tried to Improve Him | Is efficient crime-fighting the same thing as being a good hero? |
| 019000 | Before the Spider-Verse: The Cartoon Spider-Men Who Had to Invent Their Own Rules | How did different television productions define Spider-Man? |
| 020000 | What If Peter Parker Had Actually Aged? | What does *Spider-Man: Life Story* reveal when time becomes real? |
| 021000 | Peter Parker Cannot Cash His Check | Why does money keep creating Spider-Man stories? |
| 022000 | The City Beneath the Mask | Why do the boroughs, crowds and infrastructure matter? |

## Editorial and provenance rules

Each lecture contains exactly one `<!-- BEGIN SPOKEN LECTURE -->` / `<!-- END SPOKEN LECTURE -->` pair. Non-spoken companions include spoiler descriptions and relevant primary records, publisher material, archives, production interviews, and occasional Wikipedia links for navigation. Per-lecture metadata in `metadata/NNNNNN.json` maps specific spoken claims to the `metadata/sources.json` bibliography. Creator interviews and retrospective accounts are treated as testimony, not automatic proof of every disputed editorial motive. Critical interpretation is not presented as a quotation from a creator.

No copyrighted comics panels, film clips, music, fonts, or binary art are bundled. The pack is a text-only content overlay under `draft-stages/tts-spider-man/` and requires no change to shared publishing scripts.

## Import

From the project repository root, after downloading the ZIP to `~/Downloads`:

```bash
unzip -t ~/Downloads/spider-man-fan-essays-06.zip
python tools/content_overlay.py apply ~/Downloads/spider-man-fan-essays-06.zip --replace-owned
python draft-stages/tts-lectures/extract_narration.py --check draft-stages/tts-spider-man/0{18,19,20,21,22}000-*.md
```

The overlay includes all **22 complete manuscripts**, index/navigation data, metadata, source records, and the backlog. Lectures 001000–017000 and their individual claim maps are unchanged from the previous pack. This overlay adds lectures 018000–022000 and updates shared track-level navigation/source files. The reading-time estimates in `track.json` are descriptive only; the lecture text is not shortened to reach a target.
