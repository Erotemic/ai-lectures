# Portable content packs and the audio library

The library now has one server for source browsing, prepared audio, and optional
remote TTS. Start it from the repository with `make serve`, then open `/`.
The old audio reader is at `/audio`; original presentations are at
`/presentations`, including preserved `/?deck=...` bookmarks. Those compatibility
surfaces load only when opened. Existing render commands and scene order remain
unchanged.

The implementation is in `ailectures/`. Existing manuscripts remain in their
current directories, and new independently owned source packs can live in
`content/<namespace>/`. Each source pack owns its `track.json`, manuscripts,
metadata, reading sources, and declarative examples. No shared Python registry,
global lecture list, or navigation edit is required.

## Start the server

```bash
make serve
# Equivalent, with an explicit LAN bind:
python -m ailectures serve --repository . --host 0.0.0.0 --port 8001
```

`--library` is a global option before the command. Its default is `library-data/`,
which is ignored by Git. Keep this directory: installed media and listener state
are durable. `build-cache/` inside it can be regenerated; `packs/` and `state/`
should be backed up. The original `audio-cache/` remains intact.

There is no server mode to switch. Installed audio plays without a backend
request. Production loads TTS settings lazily, probes configured connections,
and uses the existing generation queue and audio checks. An outage affects
preparation, not browsing or prepared playback. Backend recovery requires no
server restart. Generation needs the source checkout's production modules and
FFmpeg/ffprobe; prepared playback needs neither executable nor inference hardware.

Optional connection overrides retain the original names:

```bash
python -m ailectures serve --repository . --tts-config /path/to/tts.toml
make serve AUDIO_TTS_PROFILE=kokoro AUDIO_TTS_ENDPOINT=http://127.0.0.1:8880/v1/audio/speech
```

An explicit TTS config is a complete configuration, following the existing TTS
loader. Without that override, a source checkout uses the shared configuration
and its ignored machine-local overlay. Private endpoints and reference material
remain local. No browser can choose an arbitrary TTS endpoint.

## Author an independent source pack

Use a namespace that does not conflict with an existing pack. Numeric local IDs
may repeat in other namespaces. The stable identity is the pair, such as
`music-theory:001000`; ordering belongs to the course manifest.

```text
content/my-subject/
  track.json
  001000-introduction.md
  metadata/001000.json
  metadata/sources.json
  examples/...
```

A minimal `track.json`:

```json
{
  "id": "my-subject",
  "title": "My Subject",
  "summary": "What this collection teaches.",
  "lectures": [
    {"id": "001000", "file": "001000-introduction.md", "section": "foundations"}
  ]
}
```

The Markdown uses the existing single `BEGIN SPOKEN LECTURE` / `END SPOKEN
LECTURE` HTML-comment pair. The shared extractor is now `ailectures.core.extract_text`;
the original script remains a compatible command. Reading references in sidecars
should resolve in the pack's `metadata/sources.json`; missing reading records
produce diagnostics while usable lectures remain available. Legacy G2/G3
source-catalog fallbacks are resolved into explicit records at export time.

For source handoffs, agents can return ordinary ZIPs of their assigned directory;
see the [handoff guide](agent-content-handoff.md). The source importer retains
conflicting originals and makes updates recoverable. Source discovery retains
usable snapshots across restarts while individual files are being fixed.
Agents changing the same source pack still need a deliberate merge. Existing
World History contributions continue to use `tools/merge_world_history_overlay.py`.
Use the immutable releases below when transferring prepared playback packs.

## Export and transfer

Export an existing track, including matching installed recordings:

```bash
python -m ailectures export --repository . --pack music-theory \
  --output /path/to/transfer/music-theory \
  --zip /path/to/transfer/music-theory.zip
```

Use `--source-only` to omit media. To import recordings from the original cache,
select the exact configuration used to generate them:

```bash
python -m ailectures export --repository . --pack g2 \
  --audio-profile kokoro --variant narrator-a-v1 \
  --output /path/to/transfer/operators
```

Only complete current recordings are imported by that legacy-cache command unless
`--allow-partial` is specified. An existing file alone is insufficient: its
request identity must match the current text, profile, pagination, and settings.
The importer measures durations and preserves available segment timings. Unknown
historical settings are not reconstructed from filenames or modification times.
Imported files are copied; the original cache is not modified.

Installed recordings, including deliberately partial recordings, are included
by a normal export and enumerate their exact coverage. Every recording carries
the full transcript pagination used for it. Readiness is recorded per variant;
partial audio must never be presented as a complete lecture.

On another machine:

```bash
python -m ailectures --library /path/to/library install /path/to/transfer/music-theory.zip
python -m ailectures --library /path/to/library serve --host 0.0.0.0
```

For a machine without the source checkout, build the small standalone reader:

```bash
uv build ailectures --out-dir /path/to/transfer
```

Transfer its wheel and install it with pip or uv. It packages the complete web
UI and depends on Starlette/Uvicorn, without NumPy, NetworkX, Manim, VTK, TTS
models, or FFmpeg. Use its `ailectures` command with the same arguments above.
A pack's reading links can still require Internet; all prepared playback and
reader UI assets are local.

## Live discovery and revisions

The server polls for completed releases every two seconds and also offers an
explicit Refresh action. Requests reconcile against the same committed catalog;
multiple server processes share SQLite activation state. No content change
requires restarting the server. Changing server or renderer code still does.

For unattended discovery, copy `library.example.toml` to a machine-local file:

```toml
pack_roots = ["/path/to/inbox"]
excluded = []

[pins]
```

```bash
python -m ailectures serve --config /path/to/library.toml
```

An inbox accepts `pack.json` directly, one directory below it, or two directories
below it. Copy into an outside or hidden staging directory, validate the release,
and rename the completed directory into the inbox. Archives are installed
explicitly through the CLI or Packs screen; partially copied archives are not
automatically extracted. Discovery never installs a half-written release.

Each immutable release has a digest and, for updates, a `parent` release:

```bash
python -m ailectures export --repository . --pack music-theory \
  --parent PREVIOUS_RELEASE_SHA256 --output /path/to/new-release
python -m ailectures install /path/to/new-release
```

An update is accepted only against its expected active base. Concurrent additions
of different packs both survive. Concurrent revisions of one base produce a
conflict, leaving the losing candidate staged. An explicit operator selection
can use `install --expected CURRENT_RELEASE_SHA256` to select a different release;
producers should use the correct parent instead of overriding conflicts.
Identical imports are idempotent. Dependency and identity conflicts roll back
activation, and old media remains available to active players and feedback.

`[pins]` can map a pack ID to an exact available release digest. `excluded` skips
discovery for listed packs. These are optional local policies; ordinary additions
need no configuration edits. Selection-policy changes in the config file are
read at startup; pack additions and revisions under its configured roots are live.
`remove PACK_ID` or the Packs screen disables a pack immediately and retains
its data; explicit installation re-enables it. Automatic discovery respects
that removal. Garbage collection is intentionally absent in this first release.

SQLite is the activation authority. `library.lock.json` is a generated diagnostic
snapshot, never an authored registry or an input supplied by a content producer.
A source checkout gives current authored text priority over installed text and
attaches only recordings with matching spoken content. A standalone installation
uses its selected source releases. Retained media for older speech remains
historical. Multiple media-only speech revisions without a selected source are
reported as ambiguous instead of choosing one by scan order.

Source edits, spoken edits, and media regeneration have separate identities.
A bibliography-only revision can reuse unchanged speech. Edited speech cannot
inherit an older recording as if it spoke the new words. Active players keep
their chosen revision and immutable media URLs while the library refreshes.

## Prepare audio

The Production page prepares a lecture using configured TTS profiles. The same
workflow is available without keeping a browser open:

```bash
python -m ailectures prepare --repository . \
  --lecture music-theory:001000 --profile kokoro
python -m ailectures prepare --repository . \
  --course music-theory:main --profile kokoro
```

Completed recordings publish as media packs and appear in the library. Different
narrators are retained independently. Explicitly requested preparations are stored
in `state/production.sqlite3`, including their source revision and synthesis
configuration. Course batches enqueue their full selection before processing.
The Production page lists these server-owned requests across browsers and provides
cancellation and retry controls.

Pending work resumes automatically after a restart. Worker leases bound concurrent
preparations across processes, and completed request-addressed pages in
`build-cache/speech/` are reused. Changing one passage can reuse unchanged pages;
a bibliography-only edit reuses all unchanged speech. Backend failures use bounded
retries; cancellation survives restarts. A changed voice/backend configuration
blocks the old request with an explicit status rather than generating different
speech under the old recipe. Start a new preparation to use the revised settings.
No TTS request runs during ordinary catalog loading or prepared playback; only
previously requested preparations are resumed in the background.

## Listeners and feedback

Access is immediate. Use **This device** for browser-local progress, or add/select
a named listener to share progress through this server. A device remembers the
choice. Another device selects the same listener without a password or login.
The Listening page exports/imports personal history and can copy device-local
history into a named listener where no shared position already exists.

Progress is saved locally before network work and queued for replay. Updates use
optimistic record versions and stable event IDs. Deliberate rewinds are valid;
a late checkpoint from another device cannot overwrite a newer position. The
UI retains conflicting local progress and offers an explicit choice. Completion
can be changed in Listening. Resume across narrators uses an approximate text
anchor when exact timing cannot be reused.

Feedback stays bound to the exact content revision and recording the listener
had open, even after an update. The form retains drafts across navigation and
validation errors, and captures the playback context when drafting begins rather
than moving it as playback continues. Submissions preserve a transcript snapshot. Editorial status
is appended separately; a new release never automatically closes old feedback.
The status API accepts an explicit `addressed_revision` when a fix is verified.

Feedback transfers separately from content and listener history:

```bash
python -m ailectures feedback-export /path/to/feedback.json
python -m ailectures feedback-import /path/to/reviewed-feedback.json
```

The Packs screen provides the same export/import. Feedback events carry no
listener identity. Import merges by stable IDs, is idempotent, and rolls back
on conflicting existing payloads. It does not replace local feedback with a
remote machine's snapshot.

## Pack schema and checks

Schema version 1 is validated by `ailectures.packs.load_release`:

- `pack.json` declares the pack ID, `source` or `media` kind, parent, namespaces,
  exact required releases, and release digest.
- `catalog.json` contains lecture/course records and typed relationships.
  Lecture revisions cover source, metadata, and explicit referenced source
  records; spoken text has its own SHA-256. Original presentation identities use
  stable deck names with legacy graph aliases.
- Recording records contain a variant, recipe digest, canonical speech pages,
  ordered segment paths, checksums, measured durations, media types, optional
  measured/interpolated timing records, and an explicit completeness flag.
- `checksums.json` indexes every payload file. The release digest hashes the
  canonical manifest without its own digest, together with that checksum index.
  Escaping paths, links, unsupported schemas, and damaged declared payloads
  are rejected. Unindexed side notes are ignored. Installation stages and
  validates declared payloads before activation.

New renderers and synchronized music/visual production can attach companion
sources and artifacts later. Existing validated score JSON and source notes are
preserved in source exports. This pass does not alter mathematical models,
rendered deck composition, or existing presentation scene order.

Run the portable contract tests and existing reader regression checks:

```bash
python -m pytest -q tests/test_content_packs.py
python tools/lecture_inventory.py
node tests/test_audio_reader_progress.js
```
