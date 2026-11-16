# Journey to the West: return to the expanded-retelling writer

Repository state checked 16 November 2026. This handoff concerns organization
and continuation of the existing expanded retelling. No compact overview has
been written or published by this agent. There are no manuscript scratch files
in this handoff directory.

## Current published source scope

The owning pack remains `draft-stages/tts-pre-1900-literature/`, namespace
`pre-1900-literature`. Its `track.json` currently indexes 465 manuscripts. The
expanded Journey strand has **25 manuscripts, local IDs 441000–465000**, covering
**chapters 1–12 in the selected linked Chinese witness**. No numbered manuscripts
in this pack were outside `track.json` at this check.

| Selected source chapter | Stable local lecture IDs | Scope |
| --- | --- | --- |
| 1–3 | 441000–443000 | Stone Monkey, Subodhi, dragon treasure, death registers |
| 4–5 | 444000–447000 | Heavenly horses, Great Sage title, peaches, banquet, army |
| 6–7 | 448000–451000 | Guanyin/Erlang, transformations, furnace, Buddha's palm |
| 8 | 452000–454000 | Scripture mission and Guanyin's recruitment of future companions |
| 9, edition-sensitive | 455000–457000 | Chen Guangrui, River Child, family-origin narrative |
| 10 | 458000–459000 | Fisherman/woodcutter, divination, dragon wager, dream execution |
| 11 | 460000–462000 | Taizong in the underworld and return; melon messenger |
| 12 | 463000–465000 | Borrowed body/debt, Water-and-Land ceremony, Guanyin and the oath |

The authoritative continuation map is
`notes/journey-west-expanded-retelling-source-map.md` in that pack. It records
individual manuscript filenames, source chapters, and primary links. The pack
README's final Journey section gives the same scope.

**Chapters 13–100 remain unwritten in this expanded strand.** World History's
existing `048000–053000` is a separate complete-plot narrative survey, followed
by `054000` on textual/historical evidence. Keep those IDs and texts unchanged;
they are not replacements for, or missing installments of, the expanded strand.

## Exact point of continuation

`465000-journey-west-expanded-guanyin-revealed-and-xuanzangs-oath.md` ends after
Xuanzang has accepted the mission and sworn not to return empty-handed. Taizong
has made him his sworn brother and arranged the papers and departure. The
farewell and road are still ahead. The monk does not yet know the full stories
of the companions already awaiting him.

Continue with the selected witness's **chapter 13**, “Trapped in the tiger's
lair; the Gold Star relieves danger / At Double-Fork Ridge, Boqin detains the
monk.” This includes departure, the early loss and rescue, and hunter Liu Boqin.
Then chapter 14 brings the monk to Wukong beneath the mountain, the release,
and the difficult start of their relationship; chapter 15 brings the dragon
and the replacement white horse at Eagle-Sorrow Stream. Those are source
boundaries, not requirements to compress each chapter into one episode.

Primary chapter headers checked directly:

- [Chapter 13](https://zh.wikisource.org/wiki/西遊記/第013回)
- [Chapter 14](https://zh.wikisource.org/wiki/西遊記/第014回)
- [Chapter 15](https://zh.wikisource.org/wiki/西遊記/第015回)

As of this check, **466000, 467000, 468000, 469000, 470000, and 471000** were
absent from both this pack's inventory and its numbered manuscript filenames.
These are **verified candidates, not a reservation**. Recheck current files and
coordinate ownership before assigning them; IDs in other namespaces are not a
collision. Retain all existing playback/cache IDs.

## Edition and evidence decisions to preserve

The selected [chapter 9](https://zh.wikisource.org/wiki/西遊記/第009回) explicitly
labels its River Child material as an addition by Wang Xiangxu and Huang
Zhouxing in the Qing Kangxi period. This was rechecked in the live page header.
The expanded episodes 455000–457000 follow that witness deliberately; they are
not evidence that the material occupied the same position in the 1592
Shidetang printing. Other editions may place it in an appendix or arrange the
numbering differently. Compare **subject/title as well as chapter number**.

Do not silently switch witnesses halfway through the continuation. Record a
conscious change and its numbering consequences if a different edition is used.
Wikisource is a transmitted public-domain Chinese text, not a facsimile of the
1592 edition. The traditional Wu Cheng'en attribution remains qualified.

The family-origin story, underworld, divine bureaucracy, and monsters are events
in the novel, not verified biography of the historical Xuanzang. The existing
source map specifically protects the tragic end of Wenjiao's story from being
recast as an uncomplicated happy reunion. Historical Xuanzang and his seventh-
century travels remain a different evidentiary subject, developed in 054000.

Use original English prose from the primary narrative. Anthony C. Yu's revised
translation is a scholarly orientation, not prose to reproduce. Existing
`cl-jtw-yu-2012` records publisher metadata; do not claim access to the complete
translation merely because the publisher page was consulted.

## Files to append when the original writer resumes

1. Add new numbered manuscript files with exactly one spoken marker pair. The
   episode's material determines its length and stopping point; no word or
   chapter-count quota is part of the handoff.
2. Add matching `metadata/ID.json` sidecars. Follow `metadata/465000.json` for
   transcript filename, related resources, exact unique speech anchors, source
   IDs and meaningful locators. Classify the retold events as fictional narrative
   events. Distinguish interpretation and historical context.
3. Merge new primary chapter records into the **current**
   `metadata/sources.json`, preserving every existing key and record. IDs such as
   `cl-jtw-ch13`, `cl-jtw-ch14`, and `cl-jtw-ch15` were not present at this check;
   recheck before creating them. Maintain direct links to the selected witness.
4. Append new lecture entries to the current `track.json` in expanded narrative
   order, using section
   `late-ming-chinese-novel-journey-to-the-west-expanded-retelling`. Record actual
   canonical spoken words and the descriptive 145-wpm estimate, not a target.
5. The `journey-west-expanded` collection in `navigation.json` uses
   `include_sections` for this strand. New indexed entries using that exact
   section join the expanded route automatically in `track.json` order.
   Do not append a second explicit `lectures` list to the selector. Update its
   scope summary/title and the source map to describe the chapters completed.
   The shorter main route is curated separately; do not insert every expanded
   installment into it.
6. Preserve collection ID `pre-1900-literature:journey-west-expanded` and its
   link to `world-history:journey-west`. The display title now correctly says
   chapters 1–12, in progress. The World History route supplies the separately
   completed six-part retelling plus context; it does not complete the expanded
   strand or replace its source manuscripts.
7. Preserve prior authorship. Attribute new narration to the writer's actual
   runtime model/known variant, with date, files, sources and scope; keep slide
   attribution separate if slides are later added. Follow
   `dkvis/learning/README.md#model-attribution` and use the required exact-model
   `Co-authored-by:` trailer for any agent-authored commit. Do not copy another
   agent's model identity from old metadata or commits.

Coordinate the explicit pack/file scope with the repository owner. For a source
ZIP, use `tools/content_overlay.py apply` and its conflict protection rather than
installing stale shared `track.json`, `navigation.json`, or `sources.json` files
with `unzip -o`. A whole-pack replacement needs genuinely exclusive scope. No
server-code change, TTS run, media build, or repository-wide test is needed to
continue these source manuscripts. Focused source checks can verify unique IDs,
files, extraction, exact anchors, bibliography resolution and updated routes.

## Handoff author and checks

Prepared by GPT-6 (exact runtime variant unavailable), as a source/continuation audit. The reorganization owner integrated this
pack-local copy and updated the route instructions to match the section selector. Inspected the current track, navigation branch, source-map,
README, final spoken ending of 465000, its sidecar, current source records, and
the selected witness's chapter 9 and 13–15 headers. No new overview manuscript,
metadata record, source catalog, or public stable ID was created by this agent.
