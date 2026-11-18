# Deploy a selected library with existing audio

Packs → **Deploy selected content on another machine** combines selected packs,
categories, and collections. Selections are a union, and each lecture appears
once. Preview reports complete, partial, and missing audio before creating a
ZIP. A bundle includes current transcripts, source records, supported companions,
listening routes filtered to the selected lectures, and published recordings.
It never calls TTS. Partially generated but unpublished job caches remain local.
Listener data, preparation jobs, TTS configuration, and voice reference files are
excluded. Use a full library backup if you also want personal state.

The CLI supports repeatable `--pack`, `--collection`, `--category`, `--tag`, and
`--lecture` selectors, or a reusable JSON selection. Parent tags include their
narrower paths. Two example selections are included:

```bash
python -m ailectures --library library-data bundle --repository . \
  --selection tools/deployments/children.json --preview
python -m ailectures --library library-data bundle --repository . \
  --selection tools/deployments/children.json --output /path/to/children-library.zip

python -m ailectures --library library-data bundle --repository . \
  --selection tools/deployments/spider-literature-history.json \
  --output /path/to/spider-literature-history.zip
```

On the other machine, install the standalone Python reader and restore into a
**new** library directory. A GPU, TTS server, Manim, and the authored checkout are
not required for playback. Installing from the reader subdirectory avoids the
optional production stack:

```bash
python -m pip install /path/to/ai-lectures/ailectures
python -m ailectures --library /srv/children-library restore children-library.zip
python -m ailectures --library /srv/children-library serve --installed-only \
  --host 0.0.0.0 --port 8001
```

`--installed-only` prevents automatic checkout discovery even if you launch from
an `ai-lectures` checkout. Omitting `--host` keeps the server on localhost. The
restore command never overlays an existing library. Existing lecture IDs,
recording IDs and audio bytes are preserved; immutable URLs are resolved against
the new library root. Source media and companion checksums are verified while
building the bundle. Optional prerequisites outside the selected content are
not automatically added.

# Clean up stale audio

Packs → Library storage → **Preview stale audio cleanup** shows eligible paths
and bytes, with an exact command for applying that preview. CLI preview:

```bash
python -m ailectures --library library-data gc --repository .
```

Defaults keep the current and previous distinct spoken-text revision and give
candidate files a 30-day grace period. Progress and editorial feedback protect
their referenced historical audio. Source packs and recordings matching retained
text stay intact, including multiple voices/formats. Removed or unknown lectures
are conservatively retained. Only known stale media releases, their production
export copies, stale job caches, and speech-cache directories used exclusively
by stale terminal jobs are eligible. Shared speech caches that also contain
current or unfinished work remain intact; old individual pages within those
mixed directories are not collected.

To keep only the current speech revision, use `--keep-text-versions 1`. To change
the grace period, use `--keep-days N`. These settings must match when applying.
Metadata-only changes do not make audio stale: comparison uses the spoken-text
hash, not description, tag, or source revision changes.

After finishing or cancelling pending generation, stop the reader and any
export/preparation commands, review the preview, and explicitly apply its plan:

```bash
python -m ailectures --library library-data gc --repository . --apply PLAN_ID
```

A changed preview is rejected. Active readers/exports and queued/running jobs
block deletion. No automatic cleanup runs on startup or while generating audio.
For an installed-only server, use `gc --installed-only` instead of `--repository`.
Cleanup receipts remain in `state/gc-receipts/`. Moves and catalog changes use a
transaction marker: after an interruption, `gc-recover` restores uncommitted
moves or finishes committed deletion, without overwriting existing files:

```bash
python -m ailectures --library library-data gc-recover
```

Keep an independent backup before intentionally deleting history. This tool does
not sweep arbitrary legacy `audio-cache/`, private voice stores, or unrecognized
folders.

# Ogg Opus for new recordings

The reader can encode new audio as Ogg Opus, independently of the upstream TTS
response format. Put this in the chosen profile in ignored `tts.local.toml`:

```toml
[profiles.YOUR_EXISTING_PROFILE]
output_format = "ogg"
```

Alternatively set `DKVIS_AUDIO_OUTPUT_FORMAT=ogg` when starting the reader.
Omitting the setting retains MP3. The server can continue returning WAV; the
reader uses FFmpeg to encode Opus at 64 kbit/s VBR. Storage format participates
in page cache identity, so Ogg and MP3 never reuse mislabeled bytes. Existing
MP3 files remain playable and transferable. Changing a running job's effective
configuration requires a new request; finish existing jobs before changing the
setting. The narrator selector labels profiles configured for Ogg Opus.

# Playback over slower connections

The browser prefetches the next two prepared blocks while the current block is
playing and retains the current prefetched block until it is no longer needed.
Transitions use the downloaded bytes rather than starting a fresh VPN request.
If the next download is still pending, playback waits for it instead of issuing
a duplicate download or replaying the previous block. Old object URLs are
revoked on advancement or narrator changes. Failed or oversized prefetches fall
back to normal playback; buffering retains the saved position.

This is a bounded in-memory buffer, not an offline download or a guarantee of
sample-perfect gapless playback on every browser/car audio system. Generation
lookahead remains a separate, explicit control and prefetching never starts TTS.
