# Children's Bedtime Stories — Episodic (Ages 3–4)

**Track ID:** `childrens-bedtime-stories-episodic-ages-3-4`  
**Series:** *Willow Bend and the Little Lights*; two completed seasons  
**Primary listener:** age three; intended age range: three to four  
**Performance:** one consistent TTS narrator; no character acting, music, effects, or images needed  
**Order:** listen in sequence for the full arc, but each episode supplies enough context to listen alone  
**Length:** determined by each story's narrative needs; no minute or word-count target

This is a **separate pack** from the existing collection of standalone bedtime stories. Here, the people, places, relationships, and shared objects remain changed from one episode to the next. An evening comes to a satisfying close every time; the listener is never left in distress until tomorrow.

## Season one: The Little-Light Walk

| Episode | Story | What changes and remains changed |
|---|---|---|
| 001000 | [Tess and the Map with Room for More](001000-tess-and-the-map-with-room-for-more.md) | Tess begins a yellow map of Willow Bend; the Little-Light Walk is announced |
| 002000 | [Bo and the Humming Bridge](002000-bo-and-the-humming-bridge.md) | Pebble Bridge and the brook enter the map; a future friend is glimpsed across it |
| 003000 | [A Small Hello at Round Pond](003000-a-small-hello-at-round-pond.md) | Tess and Bo meet Nori; the pond, willow, and ripples enter the map |
| 004000 | [The Apple That Went Traveling](004000-the-apple-that-went-traveling.md) | Nori visits the village; the orchard and old mill enter the map; the traveling apple becomes a shared memory |
| 005000 | [The Lantern That Leaned](005000-the-lantern-that-leaned.md) | Bo's silver-spotted orange lantern remains tilted; Bell Hill and its resting bench enter the map |
| 006000 | [The Little-Light Walk](006000-the-little-light-walk.md) | The festival happens; earlier people, sounds, places, and objects return; the map retains a blank edge beyond the hill |

**Story-first editorial aim:** A child can enjoy the funny footstep sounds, the traveling apple, or the crooked lantern even without noticing the arc. No explicit moral or artificial suspense is required.

## Continuity contract for future agents

Read [WORLD_BIBLE.md](WORLD_BIBLE.md) before authoring another episode. It defines the canonical relationships, map, spatial layout, recurrent objects, and season-one end state. Read [BACKLOG.md](BACKLOG.md) for possible directions, not fixed obligations. Do **not** rewrite earlier character histories, magically straighten the lantern, forget Nori's preferences, or reset the map. A future episode can develop any of those details intentionally, but must show the change on the page.

A new episode should offer a natural small recap, one locally satisfying story, a calm endpoint, and one or two earned additions to the shared world. It can be funny, mysterious, tender, or quiet. Avoid introducing more characters than an age-three listener can distinguish by context when spoken in a single voice.

## Parent-facing material and references

Each manuscript has exactly one `BEGIN SPOKEN LECTURE` / `END SPOKEN LECTURE` pair. The **For parents and caregivers** section is outside it. The parent-facing [PARENTS_GUIDE.md](PARENTS_GUIDE.md) explains optional prompts, evidence scope and sources. Metadata sidecars link narrative anchors to bibliographic records in `metadata/sources.json`. Sources support *general guidance on reading, play and age-appropriate social experiences*, not outcomes claimed for any untested original fiction.

## Import

Deliver as a single ZIP containing only `content/childrens-bedtime-stories-episodic-ages-3-4/` and relative paths. Install using the normal source importer:

```bash
python tools/content_overlay.py apply ~/Downloads/agent-e-episodic-bedtime-ages-3-4-season-1-001000-006000.zip
```

This is a new namespace, so `--replace-owned` is not needed for the first import. No other pack or shared registry requires modification.


## Season two: Beyond Bell Hill

The friends' map extends west past Bell Hill into Far Meadow. They meet Lila and Aunt Mallow; the new world develops persistent places and familiar jokes. The second six-episode season builds toward a small ribbon picnic and **finishes** that event before bedtime. No episode requires recalling its entire predecessor.

| Episode | Story | Lasting change |
|---|---|---|
| 007000 | [The Other Side of Bell Hill](007000-the-other-side-of-bell-hill.md) | Far Meadow visited; Windbreak Tree, Sitting Stone and cream cottage mapped; Lila and Aunt Mallow met; Lila wears a straw hat with blue ribbon. |
| 008000 | [Bo's Very Big Pocket](008000-bos-very-big-pocket.md) | Sitting Stone hosts the first imaginary Pocket Museum; Tess adds a tiny spoon symbol beside it; Bo takes all his items home in a bag. |
| 009000 | [Nori and the Soft-Grass Path](009000-nori-and-the-soft-grass-path.md) | Clover Nook named; Tess adds its small green circle to the map; Nori is comfortable choosing a quieter path. |
| 010000 | [The Shadow with a Very Long Scarf](010000-the-shadow-with-a-very-long-scarf.md) | Lila has visited Village Green and seen the tilted lantern; Tess draws a long shadow by Bell Hill bench; Lila suggests a ribbon picnic. |
| 011000 | [The Ribbon That Wouldn't Sit Still](011000-the-ribbon-that-wouldnt-sit-still.md) | Adult-finished three-color banner ready for Far Meadow picnic; Lila and Aunt Mallow carry it home; picnic scheduled for next day. |
| 012000 | [The Picnic Beyond the Hill](012000-the-picnic-beyond-the-hill.md) | Ribbon picnic completed; Lila and Aunt Mallow keep banner in Lila's cottage window; map preserves Willow Bend and Far Meadow; all friends safely home. |

Continuity authority: [WORLD_BIBLE.md](WORLD_BIBLE.md), including an explicit ledger for both seasons. [PARENTS_GUIDE.md](PARENTS_GUIDE.md) supplies non-spoken rationale and links. All six new manuscripts are original single-voice bedtime fiction, with no mandatory story length or imposed moral.
