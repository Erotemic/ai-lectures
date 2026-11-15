# Children's Bedtime Stories — Episodic (Ages 3–4)

**Track ID:** `childrens-bedtime-stories-episodic-ages-3-4`  
**First original series:** *Willow Bend and the Little Lights*  
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
