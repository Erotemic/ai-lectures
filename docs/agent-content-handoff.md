# Sharing content updates

Content agents can send an ordinary ZIP containing their pack directory. They do
not need a snapshot receipt, a special ZIP format, or knowledge of runtime pack
internals. Keep each agent's manuscripts, metadata, reading records, and examples
inside its assigned `content/<namespace>/` or `draft-stages/tts-<namespace>/`
directory. Server and UI development can continue separately.

## Start an authoring backlog

### Resume after the listening-route reorganization

The adult-lecture consolidation supersedes the earlier assumption that every
short source part should remain a separate lecture. The user requested actual
combined manuscripts and did not require backward compatibility. Read the
current `track.json` before continuing; do not restore removed part files from
an older ZIP or use an old item count as a completeness requirement. Combined
manuscripts retain their arguments, narratives, companions and source records.
Their sidecars' `consolidation` records preserve component attribution and
source history; they are not playback aliases. See the
[ordering and consolidation review](planning/adult-lecture-consolidation.md).

Write adult lectures around coherent subjects and endings. Review fragments
under roughly ten minutes for combination; a substantive lecture can run up to
about 40–60 minutes, with content-driven exceptions. Do not pad a finished
explanation or merge unrelated topics to reach a duration. Children's short
stories keep their intentional episode lengths. These preferences live in
`LECTURE_STYLE_RULES.md`.

The source pack and stable lecture IDs remain the authoring boundary. `track.json`
owns the full inventory; optional `navigation.json` owns listening routes and
deep dives. Append source manuscripts and metadata where they already live.
No shared server code, global registration, runtime pack build, or TTS run is
needed to continue writing.

Mathematics now has a [subject guide](../content/mathematics-guide/) and
[topic tags](content-packs.md#subjects-topic-tags-and-learning-paths). Keep broad
subject tags on the track and relevant concept tags on new lecture entries,
reusing existing labels. Place additions in their focused subject routes; a new
specialist lecture need not lengthen a starter path. Tags and route adjacency do
not supply missing prerequisite edges. State real preparation separately in the
lecture's learning metadata.

An `include_sections` route automatically includes newly indexed entries with
the specified section, in `track.json` order. Preserve that section when
continuing its strand. Explicitly curated surveys remain separate from the
expansion; they should not automatically acquire every new deep-dive installment.
For routes with explicit `lectures`, place the new ID in the appropriate route
as part of the pack-local metadata update. Original `:main` bookmarks continue
to expose the complete source sequence.

The interrupted Journey to the West writer should start with the
[pack-local continuation handoff](../draft-stages/tts-pre-1900-literature/notes/journey-west-continuation-handoff.md).
It records the exact stopping point, edition choices, and candidate IDs to
recheck. Its expanded route now follows the section automatically. The
[reorganization notes](planning/listening-routes-reorganization.md) and
[navigation format](content-packs.md#main-routes-and-deep-dives) explain the other
routes. Unfinished narrative coverage is authoring work that can continue after
the organization handoff; it does not prevent usable lectures from shipping.

### Assign an independent source pack

Give each independent agent the source ZIP and one distinct pack directory.
Agents can begin drafting immediately; server work does not need to finish first.
For a new subject, use the minimal source layout in the
[content pack guide](content-packs.md#author-an-independent-source-pack).

A task you can give an agent:

> Work only in `content/ASSIGNED-NAMESPACE/` (or the existing pack I assigned).
> Read AGENTS.md and LECTURE_STYLE_RULES.md. Build standalone audio-first
> lecture sources, keeping stable local lecture IDs and all supporting metadata,
> reading records, and examples in that directory. You may keep a BACKLOG.md
> there for planned topics, draft status, and unresolved questions. Return a ZIP
> of that directory and a short report of new or revised lectures and remaining
> questions. Do not edit shared registries, server code, or other packs. No TTS,
> runtime pack build, or repository-wide tests are needed for this handoff.

`BACKLOG.md` is optional authoring context, not a server input or publication
requirement. Keep revisions under their existing IDs. A new pack needs no central
reservation file; distinct namespaces keep agents independent. Agents sharing a
legacy pack must coordinate IDs and merge their additions, as with World History.

## Import a download

For a ZIP containing repository-relative paths:

```bash
python tools/content_overlay.py apply "$HOME/Downloads/electrical-overlay.zip"
```

The same command accepts older hash-aware overlays. `--check` is an optional
conflict preview; there is no reason to run it before every import. Importing does
not run tests, check lecture completeness, start TTS, or build runtime packs.

A ZIP containing just a pack's files can identify the destination through its
`track.json`. If the destination is ambiguous, specify it:

```bash
python tools/content_overlay.py apply update.zip --pack content/my-subject
```

Identical files are left alone. New files are added. A differing existing file
is preserved unless a supplied base hash matches. For a plain ZIP updating one
**exclusively owned** directory, explicitly allow replacement:

```bash
python tools/content_overlay.py apply electrical.zip --replace-owned
```

This option is limited to one pack. The importer keeps the previous files in
an ignored `.content-update/` recovery directory and prints its location. ZIP
omissions never delete existing files. For shared tracks, conflicting edits still
need a merge; World History additions continue to use
`tools/merge_world_history_overlay.py` as described in AGENTS.md.

## Interrupted updates and live reading

The importer stages incoming files and undo copies before changing sources.
Catalog reads and imports share a lock, so the server sees the coherent version
before or after an import. A write error rolls back the import. After a process
interruption, the next import or catalog read recovers the unfinished update.

The reader keeps usable catalog snapshots in ignored `.content-state/` storage.
It can retain a previous lecture across restarts while that file is being fixed.
Missing or malformed items, unfinished references, and unindexed manuscripts
produce diagnostics without disabling usable neighboring lectures. Newly
unindexed numbered manuscripts appear in the library; the declared course order
remains separate. Direct extraction into an exclusively owned directory still
works, but bypasses the importer's rollback and coherent-read protection.

## Packaging is the agent's work

A normal ZIP of the assigned pack is sufficient. The optional helper handles
packaging details:

```bash
python tools/content_overlay.py build \
  --pack draft-stages/tts-trades-electrical \
  --output electrical-overlay.zip
```

Without a receipt it makes an ordinary ZIP. If a source snapshot includes a
usable receipt, it automatically includes base hashes for changed files. The
recipient uses the same import command in either case. Receipts help merges;
they are not a prerequisite for writing or sharing content.

For a source-only handoff of the committed repository:

```bash
python tools/content_overlay.py snapshot --output ai-lectures-source.zip
```

That archive excludes ignored settings, recordings, caches, and listener data.
Its optional receipt is handled by the tools. Agents should return their source
files and a short change report, not modify generated runtime indexes. See the
[content pack guide](content-packs.md) for optional prepared-media exports.

Content checks remain authoring tools. Run a relevant example validator when
changing its example or logic; run focused importer/server tests when changing
that code. Routine content delivery does not require a repository-wide test run.
