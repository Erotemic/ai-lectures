# Curated export register

Curated exports are built programmatically from tracked declarations of items,
packs and optional collections. The JSON declaration is the source of truth for
membership; this document records purpose, generated releases and test results.
Changing a declaration and rerunning the builder changes the exported library.

## Declare an export

For example, a declaration can combine whole packs with individual items:

```json
{
  "packs": ["spider-man", "godzilla", "star-wars"],
  "lectures": ["modern-literature:022200", "modern-literature:023000"]
}
```

`lectures` is the existing API field for individual items, including essays and
children's stories. This example selects all items in the three packs and the two
Dune items. To select an entire authored listening sequence instead, declare
`"collections": ["modern-literature:dune"]`.

The resolver combines the declarations as a union, removes duplicate IDs,
validates every declared selector, and includes only matching items. Selecting
one item does not pull in the rest of its pack. Prerequisites and related works
are included only when declared. The builder includes the standalone server code
automatically and gathers the selected source text, metadata, companions and
published audio without manually copying content directories.

Use the same JSON with `bundle --preview`, `prepare --selection`, and
`export_curated.py --selection`. The human-maintained declaration expresses the
desired content; the generated lock records exactly what one run exported.

## Curations

| Curation | Purpose and selection | State |
| --- | --- | --- |
| `family-mac-v1` | [Broad classics, science fiction, fan essays, American history, soapboxes and children's stories](../tools/deployments/curated-mac-library.json) | Preparing audio; initial inventory 445 entries, 97 complete, 348 missing |
| `mac-smoke-v1` | [First three Brook Road Builders stories](../tools/deployments/mac-smoke-v1.json) | Small audio-complete transfer test; Linux validation recorded below; recipient Mac validation pending |

The [family selection notes](../tools/deployments/README.md) explain the included
works, exclusions, optional additions and generation commands. Counts there are a
23 November 2026 observation; the current preview is authoritative. Neither
curation automatically starts TTS. Journey to the West and the mathematical
curricula remain outside the family selection.

## What a release contains

Use the handoff builder rather than independently assembling an arbitrary reader
wheel and content ZIP:

```bash
python tools/deployments/export_curated.py \
  --repository . --library library-data \
  --selection tools/deployments/mac-smoke-v1.json \
  --export-id mac-smoke-v1-2026-11-23 \
  --output library-data/exports/curated/mac-smoke-v1-2026-11-23.zip
```

The production machine needs `uv`, pip, the existing library and network/cache
access for build tools and dependencies. The builder copies only standalone
reader package inputs, builds its matching source distribution and universal
wheel, and downloads pure-Python dependency wheels for Python 3.11 or newer.
Native macOS binaries and a bundled Python interpreter are not included.

The single transfer ZIP contains:

| File | Purpose |
| --- | --- |
| `README.md` | Recipient installation and launch commands |
| `manifest.json` | Export ID, timestamp, code revision, exact reader source hashes, dependency versions, file checksums and audio counts |
| `selection.json` | The curator's original selectors |
| `selection.lock.json` | Exact exported lecture IDs, document/text revisions, recordings, audio hashes and pack release IDs |
| `content.zip` | A fresh library containing only the selected runtime packs and published media |
| `wheelhouse/` | Matching standalone reader wheel and pinned dependency wheels for offline installation |
| `reader-source/` | Matching standalone server source distribution, including browser assets |
| `verify_export.py` | Checksum verification using only the Python standard library |
| `export_curated.py` | The producer script used for this release |

A sibling `.receipt.json` records the outer ZIP's SHA-256, byte count, source
identity and content readiness. Keep it with the artifact. ZIPs and local receipts
belong in ignored export storage; commit the curation and test notes, not raw
media or private voice material. The Git commit is context; the per-file reader
hashes identify the actual code even when the working tree had edits.

Runtime pack catalogs include complete selected source text, canonical metadata,
reading-source records, supported companions, collection order and recordings.
This is enough to run and inspect the selected library without this checkout.
It is not an authoring overlay or a copy of every original pack-side research
note, example and provenance file. Use the [content handoff guide](agent-content-handoff.md)
for a separate editable authoring snapshot when needed. The reader source
archive covers the standalone server, not the Manim/TTS production environment.

Personal listening history, editorial feedback, production databases, queued jobs,
TTS configuration, private voice reference files and unrelated source directories
are not copied. The content archive gets a new small catalog instead of the
production database and its historical snapshots.

## Readiness and reproducibility

To queue a declaration for specific voices, use `python -m ailectures queue
--selection FILE --saved-profile ID_OR_LABEL`, repeating `--saved-profile` as
needed. `voices` lists the saved profiles, and `queue --dry-run` previews the
item/voice pairs. The [preparation commands](../tools/deployments/README.md#prepare-on-the-production-machine)
cover worker pickup, matching-profile readiness and retry behavior. The CLI
persists jobs and exits; the generation-enabled server performs the work.

The builder requires complete published audio for every selected entry. For an
explicit development snapshot, `--allow-incomplete` permits a draft, and the
manifest records its missing/partial counts. Do not call that a ready listening
library. Existing unpublished generation caches are never silently promoted into
an export.

Selectors for packs and collections can grow with the library. The builder
resolves them once and exports that exact ID list. To replay a previous content
selection, unpack its handoff and use its lock:

```bash
python tools/deployments/export_curated.py \
  --repository . --library library-data \
  --locked-selection /path/to/previous/selection.lock.json \
  --export-id mac-smoke-v1-replay \
  --output library-data/exports/curated/mac-smoke-v1-replay.zip
```

A replay refuses changed selected text, metadata or recordings. It does not
recover deleted historical files; retain the earlier artifact for that exact
release. Reader code is taken from the specified checkout and recorded again,
so intentionally testing newer code against locked content is supported. To
repeat the exact original installation, use its archived wheelhouse and content.

Reproducibility here means retaining exact source/media identities and installable
code and dependencies. It does not promise byte-identical rebuilt ZIPs: build
metadata, timestamps and SQLite storage can differ. Verify an existing release
against its receipt and manifest rather than comparing freshly rebuilt ZIP bytes.
The builder never overwrites an existing output or receipt.

## Transfer and acceptance test

On the recipient's Mac, install Python 3.11 or newer, unzip the release and open
Terminal in that directory. First verify it:

```bash
python3 verify_export.py .
```

Then follow the included README. Installation uses `pip --no-index --find-links
wheelhouse`; after Python is installed, the release supplies its own dependencies.
The server starts in installed-only, playback-only mode at
`http://localhost:8001/`. It needs no internet, source checkout, TTS service, GPU
or FFmpeg. Stop with Control-C; restore runs only once into a new library folder.
An installation can optionally add HTTPS alongside HTTP using the
[HTTPS recording instructions](voice-profiles.md#http-and-https-together).
Each installation creates or supplies its own certificate; TLS private keys are
not transferred in a curated export.

For each release, record:

1. Artifact filename, outer SHA-256 from the sibling receipt, and reader code hash.
2. Selector file and lock, selected count, and complete/partial/missing audio.
3. Clean installation from bundled wheels with package indexes disabled.
4. Restore into a new location outside the production checkout.
5. Only the selected lecture IDs appear; transcripts and reading sources open.
6. Prepared audio and range requests work, and continuation follows the retained
   collection order. The isolated reader must not need the production installation.
7. Fresh recipient listening state; repeat launch preserves newly created local
   progress. The original producer's history must not appear.
8. Recipient OS, CPU, Python and browser; what was actually tested and what remains.

Automated coverage lives in `tests/test_export_handoff.py`,
`tests/test_curated_deployment.py`, and `tests/test_deployment_and_gc.py`.

## Test record: first Mac smoke release

Release ID: `mac-smoke-v1-2026-11-23`. Local artifacts are under
`library-data/exports/curated/`; the sibling receipt holds their generated hashes.

- Archive: `mac-smoke-v1-2026-11-23.zip`, 15,681,862 bytes.
- Archive SHA-256: `8982499e26d9e929e01e96136ad7ba2f605c8dbf074af65a96efba42cfc2fae0`.
- Reader source SHA-256: `e7b6b944ef55399910b88049c76bf13d925339b202beb6448db0221a7cdca841`.
- Source checkout commit recorded by the build: `f59cb96c10199cb3eef3e17b246b9de2a5c72ab2`.

The selection is three complete Brook Road Builders stories: stable IDs
`001000`, `002000`, and `003000`. All published voices for those stories are
included; this test is not restricted to one narrator. The first build contained
8 recordings and was approximately 15.7 MB.
Three recordings are complete; five additional voices have partial published
audio. Each selected story has at least one complete recording.

Linux checks cover the built universal wheel, bundled dependencies, standalone
verification, offline installation, restoration outside the checkout, exact
selected membership, all 49 published audio-block range requests and browser
assets. The clean installation used Linux x86-64 and Python 3.13.2 with package
indexes disabled; the running server had no production package or executable
tools on its search path. Unit tests also cover
checksum tampering, draft labeling, a changed replay lock, missing-audio refusal,
source-file exclusions and preserving earlier artifacts. macOS installation,
recipient browser playback, progress after relaunch, and a larger family-library
transfer remain open acceptance checks. No TTS was run for this test.

## Expand a curation

Copy the declaration to a new versioned filename and add an entry to the register.
Change explicit pack, collection or lecture selectors, then compare its preview
with the prior lock: additions, removals, estimated listening time, missing audio
and eventual artifact size. Existing IDs must remain stable.

Generate only the selected missing audio using the preparation workflow, build
a new named release, and run the acceptance test again. Keep previous archives,
receipts and locks so a recipient can reinstall or revert. For the first family
release, the pending decision is whether to add any of the optional tracks in
the family selection notes; none are added merely by appearing in that list.
