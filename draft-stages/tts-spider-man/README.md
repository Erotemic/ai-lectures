# Spider-Man: The Comics, the Character, and the Culture

This is an **entertaining, research-based Spider-Man audio essay collection for fans**. It is not a prose adaptation, synopsis service, encyclopedia of issues, or a retelling course. Plots matter when they enable an argument about character, comics craft, creator history, adaptation, or the decisions that made fans argue for decades.

## Start here: Fan Essays and Deep Dives

This is the **default listening collection** in `navigation.json`. The lectures are standalone, but the suggested path is:

| ID | Lecture | Why a Spider-Man fan might enjoy it |
| --- | --- | --- |
| 005000 | Steve Ditko, Stan Lee, and the Spider-Man You Can Feel in a Drawing | An original artwork correction, co-creator disputes, the Marvel Method, the Master Planner pages, and what changes when Romita takes over |
| 006000 | J. Jonah Jameson: A Man Who Keeps Hiring His Own Worst Enemy | The joke of Peter's employment, Jonah's reasonable question and disastrous answers, the Scorpion and Spider-Slayers, and a later identity reveal |
| 007000 | How Spider-Man's Villains Hurt Him Without Winning the Fight | Why Otto, Norman, Mysterio, Connors, Venom, and Kraven are different kinds of threat, including the body-swap and identity-substitution stories |
| 008000 | Clones, Marriage, and the Problem of Letting Peter Parker Grow Up | Ben Reilly, Peter and MJ's marriage, One More Day, the status quo, and an alternative in Life Story |

**Spoiler policy:** These are criticism for existing fans and will discuss major moments. Each manuscript includes a written spoiler description. The narration is audio-first, without citations interrupting every spoken sentence.

## Optional route: The Essentials in Four Essays

Lectures 001000–004000 were substantially rewritten to work as lively standalone essays with enough story summary for listeners who know Spider-Man from a film, television series, or game but have not read the comics. **The default route remains the four deeper fan essays**; the essentials route is an accessible alternative:

| ID | Lecture | Focus |
| --- | --- | --- |
| 001000 | Spider-Man Is Born | Amazing Fantasy #15, creation, origin and early moral premise |
| 002000 | Peter Parker's First Decade | Early ongoing comic, school and college, Goblin, Gwen |
| 003000 | The Spider-Man Story Engine | Responsibility, secrecy, money, time, New York and narrative consequences |
| 004000 | The Mask Beyond Peter Parker | Black suit, Venom, Miles, Ghost-Spider, Spider-Verse |

A third route, **Every Lecture**, plays all eight in track order. All IDs are stable; these rewrites change the spoken manuscripts for IDs 001000–004000, so previously generated audio for those IDs will need regeneration. Lectures 005000–008000 and their metadata are unchanged.

## Editorial direction

- Write for someone who already likes Spider-Man, while explaining precise comic-book references and continuity changes at the moment they become relevant. Aim for the tone and substance of a thoughtful documentary or a good long-form fan essay, **not a textbook survey or issue-by-issue recap**.
- Lead with a specific creative puzzle, incident, oddity, argument, or consequential creative decision, then develop that subject. Occasional humor and direct critical judgments are welcome when supported by examples; avoid mechanical trivia inventories, formulaic transitions, and artificial controversy.
- Separate **what happens in a comic** from **what its creators did in publication history** and **how the essay interprets it**. Do not turn retrospective legends, possible creator motives, or fan opinions into facts. Name collaborators rather than compressing all creation into a famous public figure.
- Length follows the topic, not a minimum or maximum. A manuscript must be satisfying to hear. Audio recordings have not been generated as part of this overlay.
- Spoilers are appropriate for detailed criticism. Give only as much plot as the listener needs to understand the analysis. Treat supporting characters as characters, not merely instruments of Peter's development.

## Sourcing and independent publishing

All pack content is under `draft-stages/tts-spider-man/`. The pack includes `track.json`, `navigation.json`, its eight complete narration manuscripts, 8 per-lecture `metadata/NNNNNN.json` claim maps, `metadata/sources.json`, this README, and `BACKLOG.md`.

Source notes are **outside** the `BEGIN SPOKEN LECTURE` / `END SPOKEN LECTURE` markers; they include relevant Wikipedia entries for navigation but use archival records, publisher issue catalogs, bibliographic catalogs, and contemporary reporting for meaningful factual claims. Interpretive readings are labelled as such. Comics, artwork, sound files and film footage are not included. The source metadata distinguishes archival records and secondary summaries from the copyrighted works themselves, which this pack does not reproduce.

The archive is an **ordinary text-only ZIP**. To import a pack update when this directory is exclusively owned:

```bash
python tools/content_overlay.py apply ~/Downloads/spider-man-foundations-revised-03.zip --replace-owned
```

This supports a fresh install or an update from parts 1 and 2. The `--replace-owned` flag is important when `track.json`, `navigation.json`, `README.md`, and `sources.json` already exist: the importer otherwise protects differing existing files. It performs recovery backups before replacement. It does not remove unrelated content or run shared publishing tools.

Future fan-focused topics and optional deep dives live in `BACKLOG.md`.
