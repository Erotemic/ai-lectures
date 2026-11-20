# Cosmos: A Personal Voyage — After the Wonder

A **finite series of critical audio essays** on the original 1980 *Cosmos: A Personal Voyage*, created by Carl Sagan, Ann Druyan and Steven Soter. This is not a documentary retelling, a scene-by-scene guide to the thirteen broadcasts, or a replacement for watching the original. It asks why the program still works, which parts of its science and history have aged poorly, and what its voice, politics, influence and missed opportunities can teach us about communicating science.

**Status:** In progress. Two full manuscripts (`001000` and `002000`) are published in this opening pack. The intended scope is six essays, not thirteen episodes; the four remaining concepts are planned but deliberately **not** indexed as completed lectures.

## Published essays

| ID | Title | Main question |
| --- | --- | --- |
| `001000` | The Universe as an Invitation: Why Cosmos Still Works | Why does a science series filmed in 1980 still have emotional force, and which aspects of its authority and historical storytelling deserve criticism? |
| `002000` | The Universe Kept Changing: What Science Did to Cosmos | How do planetary science, exoplanets, astrobiology, cosmology and climate science alter the picture Sagan presented? |

Both are standalone, listener-paced manuscripts. Each has one delimited spoken section, non-spoken source commentary, and individual historical-claim metadata. Measured reading times are descriptive estimates, not targets.

## The planned shape

The intended four follow-up essays are about scientific heroes and the myth of progress; visual craft, music, performance and collaboration; the Cold War political argument and planetary responsibility; and the legacy, blind spots and unrealized possibilities of science communication after *Cosmos*. Their working IDs and editorial boundaries are in [BACKLOG.md](BACKLOG.md). Each will explore the series holistically and cite specific scenes only as useful evidence.

## Evidence and interpretation

The lecture's statements about the 1980 series are distinguished from the narrator's own criticism, contemporary reception, and current scientific consensus. Historical claims should use contemporary production testimony, documentary records, and specialist scholarship rather than treating a compelling television vignette as automatically accurate. Scientific updates carry explicit dates, notably the November 19, 2026 NASA Exoplanet Archive snapshot. A scientific hypothesis that remains unresolved is not silently presented as disproven or confirmed.

The pack contains **only Markdown and JSON**. It does not embed or distribute copyrighted television footage, transcript passages, images, recordings, or music.

## Import

From the ai-lectures repository root, with the downloaded ZIP in `~/Downloads`:

```bash
python tools/content_overlay.py apply ~/Downloads/cosmos-personal-voyage-opening-2026-11-20.zip --replace-owned
```

The overlay creates a new, exclusively owned namespace, `content/cosmos-personal-voyage/`, so unrelated tracks and unpublished work are left untouched. The collection catalog discovers the pack without changes to shared server code.
