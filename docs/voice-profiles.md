# Saved voice profiles

In Settings → Saved voice profiles, each entry is one complete rendering recipe:
a backend connection, one fixed voice or reference, prose and title delivery,
pronunciation replacements, native speaking rate, saved-audio tempo, processing,
and output format. The generation dropdown selects that entry directly.

Use **Add profile**, or **Duplicate profile** to start from an existing entry.
The form checks the server for available voices automatically without blocking
editing. Backend voice catalog offers manual refresh and registration of an ID
already installed on that server; it does not upload recordings or create a
reference voice. Edit an existing profile to choose a different voice reference
on its backend. Duplicate it to change backends. Choose a server default and
mark profiles for quick select. The player also offers other saved profiles and
existing recordings.

**Edit profile** saves changes to the voice reference or audio settings as an
immutable revision under the same profile ID. Renaming or changing quick select leaves the audio revision alone.
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
send prose instructions with another CFG. Normal text instructions and title
instructions appear directly in the creation form for supported backends. Entering
normal text instructions selects directed narration automatically; leaving them
blank preserves stable paragraph cloning. CFG controls are in Advanced recipe
settings. Titles can use their own instruction,
CFG and pauses. Unsupported instruction controls are omitted. **Generate preview**
reads the editable preview text without creating a lecture recording;
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

## Recording a reference voice

Use the visible **Record a voice** button at the top of Settings. It selects a
compatible backend and opens the recorder directly. If recording is unavailable,
the button remains visible and Settings explains why. The recorder is also
available under **Add profile** or **Edit → Record a reference voice** for
compatible backends. Name the reference, read
the displayed prompt exactly, stop recording, and review the take. You can edit
the prompt before recording; changing it afterward discards the take so the audio
cannot accidentally be saved with different words. A take must last 3–45 seconds.
You can also upload a WebM, Ogg, MP4/M4A, WAV, or MP3 recording of those words,
up to 4 MiB.

**Save reference voice** saves and selects the reference. Then **Save voice
profile** to use it in later previews and lecture generation. A new take always
gets a new reference ID; previous references, profiles, and recordings remain
available. Reference names and saved voices are shared by users of this server.

Microphone access requires [HTTPS or localhost](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia).
The upload option remains usable when visiting a household server over plain HTTP.

The feature appears for configured **Breeze TTS 2** and **Fish S2 Pro** backends
on loopback addresses when `ffmpeg` and a writable reference directory are present.
The default directory is `~/code/local-ai/services/tts/voice-references`, relative
to the account running the lecture server. Set `DKVIS_TTS_REFERENCE_DIR` in the
server environment to use another existing shared reference directory. The TTS
service must mount that same directory at `/voices`, as in the local-ai setup.
Remote backends and other models do not expose the recorder.

The server converts each take to mono, 24 kHz, 16-bit PCM WAV and stores its exact
prompt alongside it. The TTS service discovers these pairs without restarting.
After saving, the editor reports whether the backend advertises the new reference;
if it does not, check the shared mount and refresh backend voices before generating.
Duration and format are checked mechanically; the user checks the spoken words
against the prompt.

Audio, prompts, and reference metadata stay in the private reference directory.
They are excluded from content packs, deployment bundles, and this repository.
Library backups preserve saved profile settings but do not copy this external
directory; back it up separately if you need to move or restore recorded voices.

## Trying voices with your own text

**Settings → Try voices** accepts up to 6000 characters of your own text. Choose
the saved profile whose speaking settings you want, then choose a voice from its
backend. **Refresh voices** checks the speech service for additional choices.
**Generate preview** reads the text without changing or saving the selected
profile. Switch voices and generate again to compare the same passage. The panel
keeps the four most recent previews, with their voice names and text excerpts;
playing one pauses the others and the lecture player.

Longer previews are paginated and assembled into one complete audio file.
Preview text can include Markdown headings to test title delivery. The profile
editor also has an editable **Preview text** field and **Generate preview**.
Preview files and text remain in the ignored library build cache and never
become catalog lectures or published lecture recordings. Playback-only mode
disables preview generation, and changing server mode refreshes these controls.

## Parallel generation

The reader queries Breeze's runtime endpoint for ready gateway workers and uses
that capacity for parallel blocks within one lecture. The queue and preparation
window grow with the worker count; multiple queued blocks can use both GPUs.
This is operational scheduling, so changing capacity does not create an audio
revision or invalidate recordings. A server without usable capacity discovery
starts with one worker. Counts are cached briefly and applied as engines open.

## Local state and connections

On first use, configured TTS entries import once from `tts.toml` plus its ignored
local overlay. Subsequent file edits update backend connections without replacing
saved recipes. New environment defaults do not rewrite profiles or queued jobs.
The shared slide-production clients and legacy reader APIs retain their own
configuration path.

Saved recipes, reference descriptions, backend addresses, labels and preferences live
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
`POST /api/library/voice-profiles/preview` accepts optional `text` (1–6000
characters); omitting it retains the standard sample. `duplicate_of` plus a
backend `voice` previews another voice with an existing profile's settings
without creating a profile. The response includes the audio URL and page count.
Supported backends advertise `reference_recording` in their catalog entry.
`POST /api/library/voice-profiles/backends/{id}/references` accepts `label`,
`transcript`, `media_type`, and `audio_base64`, and returns the new `voice` ID
and whether it was advertised by the backend. This upload is disabled in
playback-only mode.
Preview, default, quick-select and archive actions use the same-origin mutation
checks as other reader settings.

New preparation requests use `profile` and `profile_revision`, without a separate
voice or speed selection. Legacy requests and recordings remain supported.
Restart the reader to load this code, then reload the browser. No TTS-server
restart is required.
