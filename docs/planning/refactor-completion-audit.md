# Library refactor completion audit

This audit tracks the full [refactor plan](content-packs-and-library-refactor.md)
while independent authors continue from the `6ad779d` source handoff. Existing
source directories and playback identities remain stable during that work.
Completion requires evidence for the remaining items, not just a passing subset
of tests.

| Requirement | Current evidence | Remaining work |
| --- | --- | --- |
| Independent authored packs and source overlays | `6ad779d`: ordinary ZIP imports, optional receipts, retained conflicts, journal recovery, shared catalog lock, and usable snapshots across restart. The 37 focused import/catalog tests pass. | Keep source paths stable for external authors; no routine tests or builds on content import. |
| Catalog without TTS/render dependencies | `tests/test_content_packs.py` fresh-process boundary and clean installed wheel validation. | Recheck after final packaging changes. |
| Source and playable pack transfer | Existing operator-theory export served from an isolated installation without FFmpeg, TTS modules, or outbound connections. | Repeat final export/import against final schema and reader. |
| Live additions, revisions, removals and conflicts | Pack tests cover two producers, stale updates, immutable media, and retained historical records. | Add real process-level concurrency and interrupted-publication coverage. |
| Complete feedback and revision cycle | Production roundtrip test covers two narrators, historical feedback, changed text, regeneration, transfer and retained listening history. Feedback review adds submitted/current transcript comparison, explicit resolution, addressed revision and editorial notes. | Complete; authoring revisions remain deliberate source work. |
| Durable generation and batches | Nine focused production tests pass, covering restart, partial-page reuse, bounded retries, cancellation, changed settings, worker leases and protocol/transfer behavior. Desktop/mobile Production inspection verified course submission, retry controls and no horizontal overflow. | Complete; live backend listening remains conditional on connectivity. |
| Remote TTS compatibility | Controlled HTTP tests exercise native Kokoro speech and Breeze paragraph/job APIs with measured WAV-to-MP3 conversion. | Check host-service reachability and run a live integration if available. |
| Library navigation and persistent player | Desktop/mobile checks cover browsing, playback, shared listener resume and compatibility URLs. The editable queue now supports anonymous and named listeners, independent concurrent additions, reorder/remove, history transfer and automatic consumption. Three focused queue/progress tests and JS queue checks passed; two browser contexts verified shared ordering and sequential playback. | Timing-based highlighting and old progress import. |
| Feedback safety and transfer | Four focused feedback tests and the JS helper checks pass. Desktop/mobile browser exercise confirmed comparison, explicit resolution tied to the current revision, persistence and original-context retention. Imports merge event IDs and retain status history. | Complete. |
| Deployment and storage | Reader wheel and local immutable pack directories work independently of the repository. | Pack size/coverage UI, backup workflow, retention accounting and safe cleanup policy. |
| Source consolidation | New namespaces work under `content/`; existing paths use adapters. | Complete a conceptual migration only when compatibility and pending overlays remain safe. |
| Optional companions | Validated music score JSON survives source export; original presentation tools and scene order are preserved. | Generic companion artifact contract and reader links; richer synchronization remains explicitly deferred. |
| Regression validation | Original implementation: 502 repository tests passed, two Manim-dependent skips. Subsequent imports and production changes have focused behavioral tests. | Verify new behavior in its affected modules and inspect changed UI. Recheck packaging after reader boundaries change; avoid repeatedly running unrelated suites. |

Current production changes preserve completed speech independently of manuscript
revisions. A composed source-plus-media view is retained for feedback, including
standalone installations that did not author the original source pack. Runtime
pack internals can evolve without changing the source-overlay contract used by
content authors.
