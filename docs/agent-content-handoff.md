# Independent content authoring while the library evolves

Content agents can continue now. Give them a committed source snapshot and assign
each one an existing track or a new namespace. They author the same Markdown,
per-lecture metadata, reading records, and local course manifests used today.
The coordinator can keep changing the server, UI, and runtime export format.
Those implementation changes do not require agents to rewrite their lectures.

The source-overlay envelope is deliberately separate from the runtime pack
schema. Runtime releases and media transfer are implemented and tested, but can
continue to be exercised and refined before treating their layout as a permanent
external authoring API. Agents should use the exporter when needed, rather than
hand-authoring generated `pack.json`, `catalog.json`, recording indexes, or hashes.

## Prepare a handoff

Commit the source state you intend to share, then run:

```bash
python tools/content_overlay.py snapshot --output /path/to/ai-lectures-agent-source.zip
```

The archive contains the committed Git tree and a generated
`SOURCE_SNAPSHOT.json` receipt with the commit and file hashes. It contains no
Git history or ignored local data: no `.env`, private TTS overrides, recordings,
audio caches, installed packs, listener history, or experiment output. Transfer
prepared audio separately when an agent actually needs it.

Agents can unzip this snapshot into their own working directory. The receipt
must remain unchanged and uncommitted. They can initialize a local Git repository
for their own commits, but Git history is not required to return an overlay.
A file-hash receipt allows integration even after the coordinator has made
unrelated commits.

## Instructions to send with an assignment

Use an assignment with a concrete owned path, for example
`draft-stages/tts-music-theory/`, or a new `content/<namespace>/` directory.
Verify new namespaces and local lecture IDs against the supplied snapshot and
coordinate ownership. Existing World History ID reservations still apply.

Suggested handoff text:

> Read AGENTS.md and LECTURE_STYLE_RULES.md before authoring. Own only the
> assigned source-pack directory. Keep its course manifest, manuscripts,
> per-lecture metadata, reading source records, and examples together. Continue
> using the existing authored source format. Do not modify shared reader code,
> registries, common tests, root documentation, TTS configuration, or generated
> runtime-pack indexes as part of this content contribution. Put any new series
> notes or example validators inside your assigned directory. Preserve the
> SOURCE_SNAPSHOT.json receipt. Return a source overlay and a short change report.
> Include any unresolved source or teaching questions; do not hide them in audio.

For an existing track, keep its current location and qualified lecture identities.
For a new track, use `content/<namespace>/track.json` and the layout in the
[content pack guide](content-packs.md#author-an-independent-source-pack).
No shared register needs an update for discovery. Avoid moving established
folders during content authoring; adapters keep them usable during the refactor.

A pack can have several contributors, but changes to the same file require a
merge. Prefer separate pack ownership for this round. For concurrent additions
inside World History, retain the specialized additive merge workflow documented
in AGENTS.md; do not replace its shared catalogs with an older snapshot.

## Produce an overlay

From the unpacked snapshot:

```bash
python tools/content_overlay.py build \
  --pack draft-stages/tts-music-theory \
  --output /path/to/music-theory-overlay.zip
```

A new namespace uses `--pack content/<namespace>`. Repeat `--pack` only when an
agent has been assigned several disjoint directories. The tool packages changed
and new source files only, with each file's base and resulting SHA-256. It omits
unchanged files and binary media, and rejects source deletions. Propose removals
or renames separately for coordinator review so they cannot silently discard
work. Keep private materials outside source-pack directories.

Before returning work, run its relevant example validators, check spoken-region
extraction, and verify manifest membership and source references. Legacy audio
tracks use:

```bash
python tools/lecture_inventory.py
```

The new source adapter can also be checked without any speech server:

```bash
python - <<'PY'
from pathlib import Path
from ailectures.catalog import RepositoryCatalog
catalog = RepositoryCatalog(Path.cwd())
catalog.snapshot()
assert not catalog.errors, catalog.errors
PY
```

Return the overlay ZIP, its assigned directories, added/revised lecture IDs,
validation results, and any deliberate follow-up proposals. The coordinator
regenerates runtime packs and narration variants from the accepted sources.

## Integrate without replacing concurrent work

On the coordinator's current checkout:

```bash
python tools/content_overlay.py apply /path/to/music-theory-overlay.zip --check
python tools/content_overlay.py apply /path/to/music-theory-overlay.zip
```

The installer verifies scope and checksums, checks every existing file against
its base hash, and validates the resulting track before writing. The coordinator's
HEAD does not have to equal the snapshot commit. Unrelated server work and other
pack updates survive. Reapplying an identical overlay is harmless.

If a touched file changed independently, the entire preflight fails before
writing. Merge that specific conflict against the current source; do not bypass
it with `unzip -o`. The helper does not perform arbitrary textual or semantic
merges, execute incoming validators, commit changes, or delete files. Successful
writes publish manifests last so source discovery can retain its previous valid
view while new manuscripts and metadata arrive.

For World History additions that share catalogs with other authors, use
`tools/merge_world_history_overlay.py` as required by AGENTS.md. The older
completion-campaign `apply_track_overlay.py` has fixed campaign ownership and
lacks this general base-hash contract; it should not be the default for new
handoffs.

After integration, run the inventory and relevant tests, review the source diff,
and commit the accepted contribution. Runtime pack export/install can happen
independently of when agents finish their next writing batch.
