# Cosmos: A Personal Voyage — After the Wonder

A **completed finite series of six critical audio essays** on the original 1980 *Cosmos: A Personal Voyage*, created by Carl Sagan, Ann Druyan and Steven Soter. The series is not a documentary retelling, an episode-by-episode guide to the original thirteen broadcasts, or a replacement for watching them. It asks what still works, which scientific and historical claims have aged poorly, how the series achieved its emotional and cinematic force, and what its cultural influence and limitations teach us about communicating science.

**Status: complete.** All six manuscripts (`001000`–`006000`) are published in [track.json](track.json), with complete listening routes in [navigation.json](navigation.json). No additional lecture is needed to fulfill the original scope.

## Completed essays

| ID | Title | Central question |
| --- | --- | --- |
| `001000` | The Universe as an Invitation: Why Cosmos Still Works | Why does the original remain moving, and where does its dramatic authority mislead? |
| `002000` | The Universe Kept Changing: What Science Did to Cosmos | How did later scientific discoveries revise the 1980 picture without invalidating its spirit of inquiry? |
| `003000` | Alexandria, Kepler, and the Myth of the Lone Genius | How do historical reconstruction, heroic storytelling and the actual institutional history of science differ? |
| `004000` | The Face and Sound of Cosmos | How did performance, writing, music, visual effects and the production team create meaning and a sense of certainty? |
| `005000` | Who Speaks for Earth? A Science Documentary at the Nuclear Brink | How do the Cold War, nuclear risk, environmental stewardship and unequal planetary responsibilities complicate Sagan's universal appeal? |
| `006000` | What Cosmos Changed, and What It Could Not | What can we document about the program’s impact, what did later series inherit, and which opportunities remain open? |

## Listening and evidence

All six are stand-alone, listener-paced manuscripts. The final legacy essay closes the planned track rather than serving as a recap of the thirteen original programs. Each manuscript has exactly one marked spoken section, non-spoken source commentary and claim-level metadata in `metadata/`. Estimated speaking times describe measured manuscript lengths, not mandatory targets.

The lectures distinguish on-screen claims, independently supported history and scientific findings, dated scientific updates, production interviews, and the author's criticism. Some archive transcripts include later *Cosmos Update* content that was not in the 1980 broadcasts; revisions are identified rather than silently backdated. Scientific claims with changing quantities are dated, notably the NASA Exoplanet Archive November 19, 2026 snapshot used in `002000`. Historical uncertainty, including the fate of the Library of Alexandria, is acknowledged rather than disguised by a dramatic moral story.

Only Markdown and JSON appear in this content pack. It does **not** include copyrighted documentary footage, complete television transcripts, sound recordings, music or images.

## Import

From the ai-lectures repository root, after the prior Cosmos batches:

```bash
python tools/content_overlay.py apply ~/Downloads/cosmos-personal-voyage-final-2026-11-20.zip --replace-owned
```

This overlay updates only files in `content/cosmos-personal-voyage/`, without modifying other tracks or unpublished work.
