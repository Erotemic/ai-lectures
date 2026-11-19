# Consolidate authored source packs under content/

The migration is prepared on `migrate-content-storage`, based on `a12b2a18`
(the supplied Andrew Wiles lecture). It has not been merged into the running
checkout. Wiles is already committed on `main`.

## Result

All 52 active `draft-stages/tts-*` packs move to `content/<namespace>/`.
The two historical mathematical namespaces become `content/g2/` and
`content/g3/`; the other names follow their existing `track.json` IDs.
There are now 64 source-pack directories under `content/`, including the
mathematics guide. The 22 original scene-based decks remain under `lectures/`.
Non-content planning material remains under `draft-stages/`.

This is a source-storage change. Public pack, lecture and collection IDs,
listening order, prerequisite relationships, spoken text and audio-cache
identities are preserved. Reader data, generated recordings, listener state,
voice references and caches remain in their existing separate storage.

Discovery, CLI source/audio export, legacy reader defaults, inventory helpers,
content-merge tools, current documentation links and repository-based tests use
the canonical locations. Older generic content overlays relocate known old
paths after validating their original checksums; base-hash conflict checks and
recovery backups remain intact. Mixed old/new aliases cannot overwrite the
same destination. Ignored bytecode left in an old directory does not block
relocation. Older World History ZIPs remain supported by its specialized merger.

The World History editorial registry keeps its original identity and accepts
both old and canonical track names. Existing slide-deck JSON files retain their
original source-path provenance byte-for-byte, so the move does not invalidate
rendered slide caches. New deck seeds use the canonical paths.

## Evidence

A before/after comparison using `tools/verify_content_migration.py` confirms:

- 65 runtime packs, including the original narrated-deck adapter;
- the same 2,247 lecture identities and exact extracted narration;
- the same 451 collection records, including their ordering and membership;
- unchanged relationships and metadata/source records, allowing path relocation;
- unchanged binary extras and text extras apart from relocated path references.

Three descriptive source revisions change because non-spoken companion commands
now name their new source locations: `music-theory:033000`,
`music-theory:039000`, and `algorithms-computability-complexity:003000`.
Their spoken hashes, page inputs and audio identity are unchanged.

The final focused run passes **125 tests**, covering canonical discovery, older fixtures, source exports,
content imports, World History merges, slide companions, review-state identity,
legacy audio-cache reuse and installed-recording association across a move.
A playback-only reader with a temporary independent library exposes the complete
catalog, representative lecture JSON/source endpoints and a downloadable source
pack from the migrated files. No TTS or slide rendering was required.

Six broader-test failures reproduce with the same assertions in an isolated
export of the original commit: an old minimum lecture-count assumption, an old
default-profile assumption, and four foundational-track checks involving stale
word counts or numeric ordering. The inventory audit also reports existing stale
word-count metadata. Those issues are not changed as part of moving sources.

The only ignored files found under the original source directories were four
Python bytecode files; no recordings or private reference material need moving.
The production checkout and its running services were not used as test fixtures.

## Recheck before merging

Record a fresh catalog from the production source checkout, then compare it with
this worktree using its verification tool. If content authors have added material
since the branch point, incorporate that work into the migration branch first
and repeat the comparison; do not overwrite current source packs with an older
snapshot.

```bash
python tools/verify_content_migration.py \
  --repository /home/joncrall/code/ai-lectures \
  --record /tmp/content-before-migration.json
python tools/verify_content_migration.py \
  --compare /tmp/content-before-migration.json
```

An optional source-only preview uses its own library directory and port:

```bash
python -m ailectures --library /tmp/ai-lectures-migration-preview serve \
  --repository . --playback-only --host 127.0.0.1 --port 8002
```

This preview does not contain the production library's installed audio or
listener state. Continue using the original checkout to listen tonight. Merging
and switching the production server are separate future steps.
