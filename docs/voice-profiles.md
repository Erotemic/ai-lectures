# Saved voice profiles

In Settings → Saved voice profiles, each entry is one complete rendering recipe:
a backend connection, one fixed voice or reference, prose and title delivery,
pronunciation replacements, native speaking rate, saved-audio tempo, processing,
and output format. The generation dropdown selects that entry directly.

Use **Add profile**, or **Duplicate profile** to start from an existing
entry. Only creation and duplication offer a backend voice selector. The catalog
can refresh advertised voices or register an ID already installed on that server;
it does not upload recordings or create a reference voice. Existing profiles keep
their backend and voice fixed. Choose a server default and mark profiles for quick
select. The player also offers other saved profiles and existing recordings.

**Edit profile** saves changed audio settings as an immutable revision under the
same profile ID. Renaming or changing quick select leaves the audio revision alone.
Queued jobs retain their complete recipe snapshot. New generation uses the chosen
revision; previous revisions and legacy recordings remain separately playable.
Clearing a profile's lecture cache affects that revision only. Archiving hides a
profile from new generation without deleting its recordings.

## Delivery and speed

Native speaking rate is a synthesis request, available only on an adapter that
supports it. Kokoro uses `speed`. Breeze TTS 2 currently has no advertised native
rate control here. **Saved-audio tempo** uses FFmpeg after synthesis and updates
word timing offsets. The player's playback-speed control changes listening only.

Breeze's stable paragraph mode uses plain cloning at CFG 1. Directed mode can
send prose instructions with another CFG. Titles can use their own instruction,
CFG and pauses. Unsupported instruction controls are omitted. **Test title and
prose** generates a small local preview without creating a lecture recording;
preview synthesis is disabled in playback-only mode.

Loudness, filtering and compression are optional and run once on the assembled
page. Imports preserve the old reader's behavior with this processing disabled,
even if the original slide-production profile enabled it. Ogg Opus remains the
default saved format. Advanced settings expose request parameters, pronunciation
replacements and request bounds; identity, input and rate cannot be overridden
through extra request parameters.

Change **Voice/model generation revision** when server weights or reference
material changes. The reader cannot detect every remote model replacement. A
server URL relocation preserves identity; changing its model makes incompatible
profiles unavailable. Duplicate a profile for the newly configured backend.

## Local state and connections

On first use, configured TTS entries import once from `tts.toml` plus its ignored
local overlay. Subsequent file edits update backend connections without replacing
saved recipes. New environment defaults do not rewrite profiles or queued jobs.
The shared slide-production clients and legacy reader APIs retain their own
configuration path.

Saved recipes, private references, backend addresses, labels and preferences live
in `LIBRARY/state/render-profiles.sqlite3`, alongside the reader's other local
state. Keep the library directory ignored. Never copy private profiles into shared
TOML examples or source packs. Full library backups include this state and should
be treated as private; selected-content deployment bundles exclude it. Published
recordings carry opaque profile IDs and revision hashes along with their existing
voice/model provenance, without embedding the private recipe or reference files.

For other compatible services, a local backend entry can explicitly declare
supported request fields; absence means unsupported:

```toml
[profiles.example.capabilities]
native_rate_field = "speed" # Alternatively "duration_factor" (inverse rate)
instruction_field = "instructions"
```

Only declare fields implemented by that service. This does not make an unsupported
parameter work. Connection URLs remain server-local configuration, not editable
from a browser.

## API

`GET /api/library/voice-profiles` returns saved profiles, revisions, defaults and
backend capabilities. Add `?archived=1` to include archived profiles.
`GET /api/library/voice-profiles/{id}` returns editable recipe settings.
`POST /api/library/voice-profiles/save` creates a profile or saves an edit;
edits require `id` and `expected_revision`, while duplication uses `duplicate_of`.
Backend voice catalogs are under `/api/library/voice-profiles/backends/{id}/voices`.
Preview, default, quick-select and archive actions use the same-origin mutation
checks as other reader settings.

New preparation requests use `profile` and `profile_revision`, without a separate
voice or speed selection. Legacy requests and recordings remain supported.
Restart the reader to load this code, then reload the browser. No TTS-server
restart is required.
