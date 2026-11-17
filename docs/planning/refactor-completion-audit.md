# Library refactor completion audit

Verified 16 November 2026 local time (17 November UTC), by GPT-6; exact runtime
variant unavailable. This closes the implemented scope of the
[refactor plan](content-packs-and-library-refactor.md): independently authored
packs, portable prepared playback, native browsing and remembered listeners,
and optional production. The requirements below have implementation and
verification evidence; completion is not inferred from this document alone.

Established authoring directories remain supported. The separately authorized
[adult consolidation](adult-lecture-consolidation.md) changed manuscript units
and playback identities deliberately; the refactor does not restore those old
fragments. Current indexes and pack-local continuation notes govern new writing.
Runtime releases are exporter outputs, not files content authors must maintain.

## Requirement disposition

| Requirement | Verified implementation and evidence | Disposition |
| --- | --- | --- |
| Independent authored packs and source overlays | Ordinary pack ZIPs, optional receipts, path/ownership protection, backups, conflict retention and journal recovery remain supported. `tests/test_content_overlay.py` covers independent contributors, stale edits, incomplete manifests and a new namespace without registry edits. Import does not run TTS, builds or editorial acceptance checks. | Complete. Keep existing authoring paths supported. |
| Catalog without TTS/render dependencies | `ailectures` discovers sources without constructing a speech engine. Fresh-process tests and the isolated installed wheel below run without `dkvis`, NumPy, NetworkX, Manim, VTK or Torch, without accessible FFmpeg/ffprobe, and with outbound connections rejected. All 21 shipped frontend assets are local and verified. | Complete. |
| Source and playable pack transfer | Immutable releases bind exact transcript, speech recipe, duration, checksums and media. Tests cover repeated local numeric IDs in different namespaces, two narrators and media add-ons. The final wheel serves a historical 35-segment real recording, a current 42-lecture source-only music pack, and an independent optional-companion fixture. Native Packs downloads reinstall successfully, with optional prepared audio and no listener data. | Complete. Historical audio retains its own transcript and is not claimed as narration of a later combined manuscript. |
| Live additions, revisions, removals and conflicts | Pack/catalog tests cover refresh, missed changes, stale snapshots, removal, immutable media, retained history and active playback. `tests/test_pack_processes.py` exercises separate OS processes: independent installs both survive; competing revisions conflict; killing activation retains the old selection and permits retry from complete files. Cache tests verify only changed sources are reparsed. | Complete. |
| Complete feedback and revision cycle | `test_feedback_revision_two_narrators_transfer_and_resume_roundtrip` in `tests/test_production_recovery.py` covers historical feedback, source revision, regeneration and transfer. `tests/test_feedback_review.py` verifies submitted/current comparison, explicit resolution, addressed revision and editorial notes without overwriting original context. | Complete. Source revision remains deliberate authoring work. |
| Existing audio feature parity | Native lecture controls provide individual-block generation, optional continuation/lookahead, whole-lecture caching, narrator selection, speech speed and cancellation. Production exposes profiles, voice discovery/registration, queue/job details and retry. References retain source records and search. The native learning map and slide panel complete the outstanding browser consolidation; old tools remain under collapsed Compatibility tools. | Complete; the main reading flow no longer needs an old viewer for these features. |
| Durable generation and batches | `tests/test_production_recovery.py`, `test_block_requests.py`, `test_audio_preparation.py` and the production JS suites cover restart, completed-page reuse, partial interruption, bounded retries, cancellation, changed settings, worker leases and publication. Production remains separate from prepared playback. | Complete. |
| Remote TTS compatibility | Controlled HTTP tests exercise native Kokoro speech and Breeze paragraph/job protocols, including timed, seekable exported media. Six configured profiles resolved in the host probe; five connections were refused and one timed out. No generation request was sent. | Controlled compatibility complete. The plan's live integration/listening check is conditional on a reachable host service; that condition was not met. |
| Household browsing and collection organization | Category-first Collections groups children's stories while preserving their separate worlds, seasons and ages. Main routes, deep dives, preparation suggestions and period routes transfer with packs. Native links, exact-ID search and collection returns remain available without exposing production details in reading. Desktop, phone, dark-mode and keyboard checks passed. | Complete. New writing joins maintained section selectors without server edits. |
| Library navigation and persistent player | The player survives native navigation. Anonymous and named listeners retain progress and editable queues; concurrent additions, rewind/conflict handling and transfer have behavioral coverage. Chromium against the isolated installed wheel continued real audio while navigating to the learning map and resumed a named listener in a second independent browser context. | Complete. Chunk/sentence navigation and legacy local-history import retain focused regression coverage. |
| Feedback safety and transfer | Feedback captures the playing revision, retains drafts on failure, and preserves historical context through revision and review. Imports merge stable event IDs idempotently and retain resolution history. Focused Python/JS tests and the isolated wheel's resolved-feedback transfer passed. | Complete. |
| Deployment and storage | Packs reports active, retained, cache and export storage plus audio/narrator coverage. `tests/test_library_storage.py` verifies backup/restore to another root with the original unavailable, including media, progress, queues, feedback and preparation intent. Published media is retained independently of disposable stopped work. | Complete. Automatic garbage collection remains deliberately unimplemented. |
| Source consolidation and authoring independence | New `content/<namespace>/` sources work without a shared registry; established paths use adapters. Source-only music exports retain notes/provenance and available declarative examples. No renderer or runtime-pack editing is required for ordinary authoring or recoverable ZIP delivery. | Authoring/export contract complete. Physical moves of existing packs are explicitly deferred while authors work. |
| Optional companions | Pack-local sources/prepared files retain exact identities and credits. Arrival/change/removal, transfer and malformed optional records are covered. Prepared HTML opens in a sandboxed native iframe without a renderer. Repository decks are discovered lazily; building requires an explicit action. Build/retry/concurrent-request behavior is tested with an injected renderer. | Complete for optional file/view/build integration. Actual slide rendering was not run: Manim is absent. Synchronization and companion-only add-on composition remain later extensions. |
| Native learning map and retained evidence | The stdlib-only map works with installed packs and no source checkout. It distinguishes preparation, proof, history/lineage, related material, listening order and collection structure. All 405 original authored claims retain exact component endpoints, types and explanations, including 61 now internal to combined lectures; six planned G4 nodes are honestly unavailable. Search, filters, incoming/outgoing focus, original evidence, URL state, keyboard selection, zoom, bounded preview and complete view are native. | Complete. Authored teaching judgments are not presented as formally validated dependencies. |
| Browser pack export | `ailectures/exports.py` fixes the source/media snapshot and creates an atomic ZIP from published artifacts. Packs offers source-only or prepared-audio downloads. API/helper tests cover exact media transfer, personal-state exclusion and invalid requests. The browser downloaded a ZIP; the isolated wheel exported/reinstalled all 35 real segments. | Complete. Runtime ZIP transfer and ordinary author-source overlays remain distinct documented contracts. |
| Regression validation | The affected contract run passed 94 Python tests with one optional-Manim skip; ten JS entrypoints passed. Final native API/companion checks passed after the installed-only deck fallback. Real desktop/mobile browser checks and the isolated wheel exercise below passed. No deck, numerical-model or presentation-source files were changed. | Complete for the affected reader/tooling scope; unrelated repository suites were not rerun. |

## Final portable-reader exercise

The final wheel was built from a copied tree outside this checkout and installed
into a fresh virtual environment using local dependency wheels. Every packaged
runtime file matched the final source snapshot. Its SHA-256 is:

```text
40d51dd5f4bfc61fbb5427cf2e114b67449b2603b18642b185e4c689c15b3451
```

No repository path was supplied to the running reader. The Python server had
neither the mathematical/render packages nor FFmpeg/ffprobe available. Its
network guard rejected non-loopback DNS/socket access and recorded zero outbound
attempts. Three installed packs contained 44 lectures, including the 42
source-only music lectures. The prepared-companion fixture was explicitly
synthetic, not represented as a production manuscript.

For the real historical `g2:149000` recording, verification covered all 35 full
file checksums, all 35 HEAD requests and 70 byte ranges (initial and midpoint),
with 1,035.264 seconds of measured speech. Chromium then decoded, briefly played
and advanced from a midpoint seek in every segment. This establishes browser
media operation, not a fresh human audition of the entire recording. Native
navigation preserved playback; a second browser context resumed the shared
listener's saved position. Both browser pages reported no JavaScript errors.

The same installation verified local assets, native learning-map relationships,
checksummed SVG/HTML companion downloads, inline HTML sandbox policy, graceful
absence of the repository renderer, source-only and prepared-audio ZIP exports,
installation into another store, listener queue/progress transfer, idempotent
resolved-feedback transfer, and pack arrival without restart. TTS reported no
configured profiles while prepared playback remained available.

The repository browser was separately inspected at desktop and 390-pixel phone
widths, in light and dark modes. The map's full accessible list remains available
beyond its preview; expansion survives opening a lecture and returning. Prepared
slides opened inside the lecture, credits/download links remained accessible,
and repository decks without Manim showed unavailable build controls. A mobile
search sizing issue found during inspection was fixed and rechecked. These are
reader presentation checks; slide contents and frozen deck compositions were
not changed or claimed visually improved.

## Repeatable focused verification

The core affected Python run was:

```bash
python -m pytest -q \
  tests/test_content_packs.py tests/test_content_overlay.py tests/test_catalog_cache.py \
  tests/test_pack_processes.py tests/test_library_storage.py tests/test_production_recovery.py \
  tests/test_block_requests.py tests/test_narrator_playback.py tests/test_voice_profiles.py \
  tests/test_imported_recordings.py tests/test_audio_preparation.py tests/test_reference_narration.py \
  tests/test_library_references.py tests/test_companion_packs.py tests/test_feedback_review.py \
  tests/test_listening_queue.py tests/test_preparation_selection.py tests/test_legacy_listener_progress.py \
  tests/test_browser_assets.py tests/test_native_library_tools.py tests/test_browser_pack_export.py \
  tests/test_learning_map.py tests/test_native_slide_companions.py
```

Browser-helper verification used:

```bash
node tests/test_library_player.mjs
node tests/test_library_progress.mjs
node tests/test_library_feedback.mjs
node tests/test_legacy_progress.mjs
node tests/test_listening_queue.mjs
node tests/test_narrator_playback.mjs
node tests/test_production_controls.mjs
node --test tests/test_production_jobs.mjs
node tests/test_learning_map.mjs
node tests/test_native_slide_companions.mjs
```

`python tools/audit_listening_routes.py --output /tmp/listening-routes.json`
reported 51 packs, 1,354 audio manuscripts and no unresolved installed route
references or unrouted material after the concurrent author additions. These
counts are a dated snapshot, not an import requirement. It still reports the
three documented short adult exceptions and 213 exempt children's stories.

The older `tools/lecture_inventory.py` diagnostic is narrower than the live
reader inventory: it reports an invalid `g2` track-ID check and six declared
word-count discrepancies in current Modern World/Journey manuscripts. Those
editorial/tool diagnostics are not silently declared fixed by this refactor and
do not block usable lectures. Owners should reconcile counts against canonical
spoken extraction during their next content pass; new source-only `content/`
packs are covered by the route/catalog inventory instead.

## Explicitly later work and the writing handoff

Physical source-folder moves, richer synchronized companions, independent
companion-only add-ons, cross-server listening synchronization, phone offline
downloads and automatic garbage collection remain outside this completion.
Public catalog/authentication, inference provisioning and wholesale visualization
tree renaming also remain outside the original refactor. These are separate
projects, not unfinished requirements hidden behind completion labels.

Independent writers can continue now using current pack indexes and the
[content handoff guide](../agent-content-handoff.md). In particular, the
[Journey continuation handoff](../../draft-stages/tts-pre-1900-literature/notes/journey-west-continuation-handoff.md)
currently covers selected-witness chapters 1–27 and starts the next batch at
chapter 28. Recheck it and current ID ownership before assigning work; do not
copy reservations or fragment counts from an older plan. No new central registry,
runtime export, TTS check, renderer build or repository-wide test is required for
a routine content contribution.
