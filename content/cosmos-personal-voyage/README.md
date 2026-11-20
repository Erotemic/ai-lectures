# Cosmos: A Personal Voyage — After the Wonder

A **finite series of critical audio essays** on the original 1980 *Cosmos: A Personal Voyage*, created by Carl Sagan, Ann Druyan and Steven Soter. This is not a documentary retelling, a scene-by-scene guide to the thirteen broadcasts, or a replacement for watching the original. It asks why the program still works, which parts of its science and history have aged poorly, and what its voice, politics, influence and missed opportunities can teach us about communicating science.

**Status:** In progress. Four full manuscripts (`001000`–`004000`) are published. The intended scope remains six essays, not thirteen episodes; the two remaining concepts are planned but deliberately **not** indexed as completed lectures.

## Published essays

| ID | Title | Main question |
| --- | --- | --- |
| `001000` | The Universe as an Invitation: Why Cosmos Still Works | Why does a science series filmed in 1980 still have emotional force, and which aspects of its authority and historical storytelling deserve criticism? |
| `002000` | The Universe Kept Changing: What Science Did to Cosmos | How do planetary science, exoplanets, astrobiology, cosmology and climate science alter the picture Sagan presented? |
| `003000` | Alexandria, Kepler, and the Myth of the Lone Genius | How does the program dramatize the history of inquiry, and what is lost when institutions and collaborators disappear from the story? |
| `004000` | The Face and Sound of Cosmos | How do Sagan’s performance, shared authorship, practical imagery and music communicate wonder—and sometimes overstate certainty? |

All four are standalone, listener-paced manuscripts. Each has one delimited spoken section, non-spoken source commentary, and individual historical-claim metadata. Measured reading times are descriptive estimates, not targets.

## The planned shape

The two remaining essays are about the Cold War political argument and planetary responsibility (`005000`), and the legacy, blind spots and unrealized possibilities of science communication after *Cosmos* (`006000`). Their working IDs and editorial boundaries are in [BACKLOG.md](BACKLOG.md). Each explores the series holistically and uses specific scenes as evidence, not as episodes to recap.

## Evidence and interpretation

The lectures' statements about the 1980 series are distinguished from the narrator's own criticism, contemporary reception, and current scientific consensus. Historical claims should use contemporary production testimony, documentary records, and specialist scholarship rather than treating a compelling television vignette as automatically accurate. Scientific updates carry explicit dates, notably the November 19, 2026 NASA Exoplanet Archive snapshot. A scientific hypothesis that remains unresolved is not silently presented as disproven or confirmed.

The overlays contain **only Markdown and JSON**. They do not embed or distribute copyrighted television footage, transcript passages, images, recordings, or music.

## Import

From the ai-lectures repository root, with the downloaded ZIP in `~/Downloads`:

```bash
python tools/content_overlay.py apply ~/Downloads/cosmos-personal-voyage-history-and-craft-2026-11-20.zip --replace-owned
```

The overlay updates only the owned `content/cosmos-personal-voyage/` files. It leaves unrelated tracks and unpublished work untouched. The collection catalog discovers the pack without changes to shared server code.
