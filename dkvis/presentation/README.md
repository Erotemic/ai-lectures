# Shared presentation production

This is the original slide and narrated-video toolchain. For the current audio
library, source packs, and prepared playback, start with the
[repository README](../../README.md) and [content pack guide](../../docs/content-packs.md).

Use `python -m dkvis.presentation {list,slides,text,video,audio,serve}`. Deck manifests,
not this package, select the mathematics, scenes, and transcript. The package
can be imported without Manim, VTK, or a speech server; rendering loads those
dependencies only when needed.

| File | Responsibility |
| --- | --- |
| `build.py` | Manim rendering, asset preparation, HTML/PDF export and final-frame handouts |
| `narration.py` | Read the manifest-selected transcript; export slide/build text and a manifest |
| `audio.py` | Speech requests, sentence-aware chunking, cutoff retries, cache keys and lossless joins |
| `serve.py` / `library.html` | Local media catalog, chapter lookup, embedded viewers and range-capable file serving |
| `audio_quality.py` | Cached loudness/peak measurements, onset/boundary review reports, compression and two-pass normalization |
| `video.py` | Check clip/note alignment, synchronize builds with audio, write chapters and assemble the video |
| `alignment.py` / `cue_video.py` | Locate authored words and schedule visual events within unchanged speech passages |
| `tts.py` | Load `tts.toml`, ignored `.env` and CLI configuration |
| `media.py` | Media duration and FFmpeg concat-list helpers |
| `timing.py` | Shared append-only operation timings and per-run summaries |
| `paths.py` | Resolve the visualization root without relying on the caller's working directory |

Keep speech chunking and caching independent of lesson content. Preserve the
server-duration guard, full-audio-plus-pause video length, and exact note/build
preflight when changing production code. TTS profiles are shared across decks.
`DKVIS_TTS_PROFILE` selects a machine-local default; `MATCHING_TTS_PROFILE`
remains a fallback for existing `.env` files. Private endpoints never belong in
tracked files or logged settings.

Outputs retain the established `renders/<deck>*` and `slides-<deck>/` layout,
including the `-light` suffix for the light theme. Audio remains under each
deck's `<deck>-narrated/audio/<profile>/` directory, with content-based request
keys. Timings retain `renders/logs/render-timings.jsonl`. Existing artifacts
can be reused when their embedded notes match the transcript.

The old `dkvis.build_slides`, `dkvis.matching_narration`,
`dkvis.matching_video`, and `render_matching_video.sh` commands only preserve
existing invocation patterns. Maintained callers use this package and
`render_video.sh`. The wrappers contain no production logic.


## Render presentations and narrated video

Run commands from the repository root. The rendering stack is optional for the
audio library:

```bash
uv sync --extra slides --extra serve --extra test
# Add --extra vtk when rendering VTK scenes.
```

Manim also needs the host's Cairo, Pango, FFmpeg, and LaTeX packages. Deck
manifests live in `dkvis/decks/`; authored presentation transcripts and model
attribution live in numbered `lectures/` folders. See the
[learning-module contract](../learning/README.md),
[slide-authoring notes](../../briefs/slide-authoring.md).

```bash
make slides DECK=operators-sylvester QUALITY=l
make video DECK=operators-sylvester TTS_PROFILE=kokoro
make lectures-video TTS_PROFILE=kokoro
```

`QUALITY=l` selects draft slides. Video generation needs the selected TTS service.
`SKIP_RENDER=1` reuses existing slide renders; `REFRESH_AUDIO=1` forces fresh
speech. Normal reruns reuse matching speech and encoded segments. Narrator
profiles retain separate outputs. Unnarrated reference presentations are maintained in the `dk` repository.

Use `tts.toml` and ignored `tts.local.toml` for speech profiles. An explicit
`TTS_CONFIG` selects a complete config file rather than that automatic overlay.
The Make interface also accepts `TTS_ENDPOINT`, `TTS_MODEL`, `TTS_VOICE`,
`TTS_LANGUAGE`, `TTS_RESPONSE_FORMAT`, `TTS_TIMEOUT`, and `TTS_INSTRUCTION`.
`TTS_REQUEST` is a JSON object of extra API request fields; `TTS_SETTINGS` is a
JSON object of client settings such as chunking or postprocessing. Explicit
named options take precedence over client settings. `VIDEO_ARGS` supplies
additional renderer CLI flags. Keep private endpoints and voice material local.
See [the pronunciation guide](../../pronunciations/README.md) for synthesis-only
spelling hints and [long-passage narration experiments](#long-passage-narration-experiments)
for the separate conditioning and alignment workflow.

### Updating one scene

Edit the scene and its corresponding narration, then run:

```bash
make video DECK=prereq-complementary-projection TTS_PROFILE=kokoro UPDATE_SCENES="CpSplit"
```

`UPDATE_SCENES` renders the selected scenes, exports the complete HTML/PDF/handout,
and assembles the full lecture. The separate `SCENES` / `--scenes` option makes a
selected-scene video preview. Do not combine `UPDATE_SCENES` with `SKIP_RENDER=1`.

If model attribution changes, include the cover, for example
`UPDATE_SCENES="CpTitle CpSplit"`, so its visible credit is refreshed. Update the
lecture's `provenance.yaml` following
[the attribution contract](../learning/README.md#model-attribution). A rebuilt
cover appears in an existing MP4 only after video assembly.

For slides alone, use `make slides DECK=... SCENES="CpSplit"`; a later video
build with `SKIP_RENDER=1` assembles the current pieces. Shared visual styles,
scene additions, and reordering can affect the whole deck and warrant a full
render. Inspect draft renders before claiming a visual improvement, and keep
each scene's complete intended static content in its final build for handouts.

## Measure and repair existing audio

From `visualizations/`, with FFmpeg/FFprobe installed:

```bash
uv run python -m dkvis.presentation audio analyze renders/prereq-projections.narrated.mp4 \
  --timeline renders/prereq-projections-narrated/timeline-crall.json \
  --out renders/audio-quality/projections-analysis

uv run python -m dkvis.presentation audio repair renders/prereq-projections.narrated.mp4 \
  --timeline renders/prereq-projections-narrated/timeline-crall.json \
  --out renders/audio-quality/projections-corrected
```

Choose a fresh output directory for each repair. Open `report.html` for original
and corrected video players, clickable RMS plots, and timestamped candidate
issues. `report.json` retains the numerical measurements. Repair writes
`leveled.mp4`, a lossless `leveled.wav`, processed request chunks and a new
timeline. Originals remain available. The video stream and chapters are copied;
speech lengths, pauses and slide timestamps are preserved. This requires neither
the speech server nor Manim. Analysis also accepts a WAV/MP3 without a timeline;
request-boundary diagnostics require a timeline and its source audio.

Measurements include integrated loudness (LUFS), true peak (dBTP), loudness
range (LU), sample peaks, near-rail samples and a 100 ms RMS envelope. The latter
uses decoded mono audio; near-rail samples flag a possible saturation problem,
not proof of clipping in the original multichannel signal. For each request,
we compare the 90th percentile of active RMS windows in its first two seconds
with the remaining body. Boundary checks compare the preceding request's last
two active seconds with the next request's first two. A difference above 6 dB
is a listening candidate. Windows below −55 dBFS are excluded; this is a level
gate, not speech recognition. Natural emphasis, phonetics and breathy endings
can trigger flags. The report helps locate issues; it does not certify speech
quality, identity consistency, pronunciation or completeness.

Exact request membership comes from `.parts.json` join sidecars. Older renders
use `audio_join` entries in `renders/logs/render-timings.jsonl`. Keep those logs
and the raw audio cache with a render: if a joined file has no provenance, repair
refuses to guess its request boundaries.

## Configure processing and speech delivery

`tts.toml` has a shared `[postprocess]` table; override individual values in
`[profiles.NAME.postprocess]`. Future `video` runs automatically process cached
raw speech with these settings. Set `enabled = false` to bypass processing.
The initial speech preset uses:

- a 60 Hz high-pass filter;
- preliminary per-request level matching, with a maximum upward gain of 24 dB
  before compression;
- a gentle compressor: −20 dBFS threshold, 2.5:1 ratio, 5 ms attack, 180 ms release;
- measured two-pass FFmpeg `loudnorm`, targeting −18 LUFS and −1.5 dBTP, with a
  7 LU loudness-range target. Peak protection may prevent exact target loudness.

The preliminary gain cap is not a total amplification limit: the final
normalizer can add gain. Compression and normalization cannot repair a clipped
source or change an excited intonation into a calm one. The final AAC encode can
slightly overshoot the WAV's true-peak target; the report measures the finished
MP4 as well as the chunks. See FFmpeg's [loudnorm](https://ffmpeg.org/ffmpeg-filters.html#loudnorm)
and [acompressor](https://ffmpeg.org/ffmpeg-filters.html#acompressor) documentation.

Raw request keys depend on speech text/model/settings. Processing keys depend
on raw content, processing settings and FFmpeg version, so changing loudness or
compression reuses speech while rebuilding its processed copies. A different
prompt or chunk size requires new speech. All caches, reports, WAVs, MP4s and
operation logs live under ignored `renders/`; commit only source/configuration.
Timing records include measurement, processing and remux durations, cache hits,
and processing settings, alongside the existing speech and video timings. Nested
operation times overlap and must not be added to estimate wall time.

The cloned-voice profiles allow up to 110 words / 750 characters per request, with
the existing 60-second cutoff detection and subdivision retained. Its prompt asks
for warm, clear delivery at steady conversational loudness with restrained
emphasis. Explicit `cfg_scale = 2.0` reduces the instruction-conditioned server
default of 4.0 observed in the current local Breeze implementation. These are
starting settings for the next synthesis/listening comparison; the offline
repairs measure only the mechanical processing, not the revised prompt.


## Refresh a server-side reference voice

The client cannot detect a replacement reference recording or reference
transcript behind an unchanged TTS endpoint/model/voice name. Use
`make video DECK=prereq-basics TTS_PROFILE=crall-math-dk-v2-breeze-tts2 SKIP_RENDER=1 REFRESH_AUDIO=1`,
or pass `--refresh-audio` to `render_video.sh`, to bypass cached synthesis.
The Make variable also propagates through `make lectures-video` and
`make prerequisites-video`. It resynthesizes every speech chunk in the selected
lecture(s), replaces matching raw cache files, processes the new audio, and
reassembles the videos. Processing and encoded-segment caches still compare their
actual inputs. No cache deletion is required. `SKIP_RENDER=1` requires up-to-date
visual builds. The flag is off by default; normal runs keep using matching caches.

Changing the voice name changes the request digest, which retains the previous
raw requests under their old keys. Reference files stored only on the server
are not themselves inputs to the client-side digest.

## Render different narrators concurrently

Final videos include the configured narrator identity, for example
`renders/001000_prereq-projections.crall-math-dk-v2-breeze-tts2.narrated.mp4` and
`renders/001000_prereq-projections.af_heart-kokoro.narrated.mp4`. By default this is the
profile name; `narrator_voice` combines a reference-speaker label with the model.
Use separate profiles for separate narrators. A custom `--output` must also be distinct for each run.

Build the shared visual slides once, then narrate them in parallel:

```bash
./render_video.sh --deck prereq-projections --tts-profile crall-math-dk-v2-breeze-tts2 --skip-render &
./render_video.sh --deck prereq-projections --tts-profile kokoro --skip-render &
wait
```

Run `make slides DECK=prereq-projections` first if the slide clips need rebuilding.
Concurrent Manim builds of the same deck share visual output paths, so use
`--skip-render` for both narration runs. Narration exports, audio caches, clips,
concat lists, chapters, timelines and final videos are profile-specific.
Preview clips and assembly metadata are also separate from full runs. Two runs
using the same profile still share its caches and outputs; run those sequentially.

Use `renders/<deck>-narrated/timeline-<narrator>.json` for analysis and repair
(or `timeline-<narrator>.preview.json` for a preview). New renders no longer write
the ambiguous `timeline.json` alias. Existing videos and timelines retain their
old names until explicitly rebuilt; the legacy unsuffixed video is not updated.


## Avoid clicks at narration boundaries

The default `postprocess.edge_fade_ms = 8.0` ramps each speech request to and
from zero over eight milliseconds. The final assembly also ramps the edges of
individual narrated builds. No samples or slide pauses are removed. Set this
value to zero to disable the fades.

Final videos now assemble a lossless `narration-<profile>.wav` directly from the
source speech at the build timestamps, then encode that complete track to AAC
once. The video stream is still copied. The independently encoded audio in the
intermediate video clips is not used for the final soundtrack. This avoids
carrying separate AAC priming/padding boundaries into the full presentation.
The lossless assembly is profile-specific, including a separate preview variant.

To apply only the boundary treatment to an existing video, preserving its levels
and compression:

```bash
uv run python -m dkvis.presentation audio repair \
  renders/prereq-projections.kokoro.narrated.mp4 \
  --timeline renders/prereq-projections-narrated/timeline-kokoro.json \
  --profile kokoro --edges-only --out renders/audio-quality/projections-clicks
```

As with other repairs, choose a fresh output directory. The report now lists
nonzero source edges above −50 dBFS. Such an edge can click when joined to
silence; it is not proof that a listener will hear a click. A fade cannot remove
an artifact already inside a spoken word. Listen to the comparison before
replacing a previously rendered video. Originals are preserved. Each report keeps an `original` media snapshot and a
timeline snapshot so a concurrent new render cannot change its comparison.


## Local library server

`make serve` starts the unified library at `/` and loads this original catalog
and player lazily at `/presentations`. `python -m dkvis.presentation serve`
still starts the original player directly for `renders/`. For example:

```bash
uv run --extra serve python -m dkvis.presentation serve --host 127.0.0.1 --port 8002
```

Use `--help` for media-directory options. The unified reader's port and network
binding are described in the [quick start](../../README.md#start-the-library).
Static media uses Starlette's byte-range
implementation; keep that behavior when modifying the server. HTML asset paths
remain relative under `/files/`, and PDFs use the browser's built-in viewer.

For this compatibility viewer, restart after registering new Python deck code:
Python deck definitions and the cached index are loaded into the running
process. The UI Refresh button rescans generated files for known decks; it is
not a Python module reload. New renders of existing decks need only Refresh.

The catalog scans one selected folder at a time and lists only registered decks.
Loose preview clips and orphan transcript exports do not become lecture entries.
Lecture titles and ordering
come from the existing YAML index. Narrated MP4 names select their own profile's
timeline; previews use preview timelines, repaired videos use their neighboring
timeline, and MP4 metadata supplies a fallback. No video is transcoded by this
server. Position storage includes the file's modification time, so a new render
does not inherit an old version's timing. The `serve` extra stays independent of
Manim and TTS dependencies. Run its HTTP tests with `uv run --extra serve --extra
test pytest -q tests/test_media_server.py`.


## Narrator names and native captions

The preferred cloned-voice profile is `crall-math-dk-v2-breeze-tts2`: reference
basename `crall-math-dk-v2`, model `breeze-tts2`. It writes public video, timeline,
and transcript variants with that same complete name. `narrator_voice` holds the
reference/voice basename, and `narrator_id` combines it with the model actually
selected. Overriding `--voice` changes the output name and discards reference
metadata that described the previous voice.

The original `crall` profile is retained for compatibility with its original
voice/cache namespace. Its new output labels use `crall-math-dk-breeze-tts2`.
Built-in voice profiles similarly expose both identifiers, such as
`af_heart-kokoro` and `ryan-breeze-tts2`. Existing artifact names and generation
snapshots are preserved. The library honors remembered selections; otherwise it
prefers the most recently generated full video rather than a hard-coded alias.

The visible **CC: off/on** button alongside playback controls toggles captions
directly and stays synchronized with the native player menu. Native caption
options remain available, including in fullscreen. Captions start off for each
selected video. Caption words are the recorded TTS input, with approximate timing
within each request. The speed selector offers rates up to 4× and remembers the
selected rate in this browser.

Timestamp buttons seek 50 milliseconds inside the selected passage (less for
a very short passage). This avoids displaying the preceding video frame when
an exact boundary falls between frames or browser timestamps are rounded.


## Viewer feedback

The lecture library has a feedback box below navigation and above the spoken
transcript. **Save feedback** stores one JSON record per submission in
`visualizations/feedback/` by default, outside the disposable `renders/` tree.
This is viewer-authored data: back it up separately; it is ignored by Git.
For a custom media directory, feedback defaults to a sibling `feedback/` folder.
Use `serve --feedback-directory /path/to/feedback` to choose another location
outside the publicly served media tree.

Records include feedback text, UTC submission time, the stable lecture ID,
the selected file/narrator, its generation metadata and SHA-256 fingerprint,
and the playback timestamp and chapter. The timestamp is captured when typing
starts. Original generation attribution and current lecture source attribution
are stored separately. HTML and PDF views can receive feedback too; lectures
with no rendered media receive lecture-level feedback.

Drafts are saved locally in the browser for each selected file generation and
restored when switching lectures or voices. A failed save leaves the text in
place. If a file was regenerated after the viewer selected it, saving is rejected
rather than attributing the old feedback to the new video; copy the draft before
refreshing and reviewing the updated lecture. Restart the server after updating
the Python code; no media rebuild is needed for the feedback UI.


## Reference and generation records

`tts.toml` declares portable reference filenames in the profile's `reference`
table. The server still receives its normal voice ID, not local reference paths.
`DKVIS_TTS_REFERENCE_DIR` in ignored `.env` optionally supplies a local copy for
recording basenames, sizes, UTC modification dates, WAV format/duration, and
reference transcript text.
No reference audio bytes, absolute host paths, or new reference hashes are saved.
These observations do not attest that a remote server has byte-identical files.
Use a new reference basename when recording a new version.

New raw speech sidecars keep their actual generation timestamp, request options
(instruction, guidance, seed if supplied), reference observations, and optional
server runtime metadata. Profiles with `record_server_runtime = true` query the
local-ai `/v1/runtime` endpoint once per video run. Supported fields include model
and source revisions, backend, dtype, device, sample rate, and fast-mode settings.
Unreachable or unsupported endpoints are recorded as unavailable and do not block
synthesis. Server defaults that were not reported remain unknown.

Video sidecars snapshot full build-time TTS settings, postprocessing settings,
pauses, and FFmpeg version. Timeline `speech_parts[].synthesis` snapshots the
original raw-chunk records, so cached chunks retain their original reference and
request settings even if the current configuration has changed. A cache hit
never relabels old synthesis as a new generation. Older chunks without these
fields remain unrecorded rather than being backfilled.

The private endpoint URL remains outside artifact metadata; its existing opaque
cache identifier is retained. The selected video metadata also accompanies saved
viewer feedback, preserving the reference/model identity that the feedback concerns.

## Phrase-timed animations

A transcript-adjacent `animation_cues.yaml` opts its deck into phrase timing for
normal videos. `video.py` synthesizes each build as before, then asks
`render_cued_build` to retime its existing animation clip against the aligned
speech. Cues do not create additional speech chunks. The `align` extra supplies
CPU inference dependencies; `render_video.sh` includes it. The CLI option
`--no-align-animations` disables this step. Decks without authored cues retain
their existing behavior.

Event pieces and their concatenated visual have content-based caches, separate
from speech and final muxing. Timeline entries retain `visual_source`, `visual`
and `animation_cues`. The retimed visual's sidecar includes the measured schedule
and alignment key. Keep cue phrases unique within their build and source offsets
strictly increasing. Re-render changed scene clips before changing these offsets.

### Feedback on on-demand audio lectures (G2, G3, and History)

The audio player at `/audio` now has the same **Lecture feedback** form as the
visual lecture player. Open G2, G3, or History, select a speech page, and type a note.
The first keystroke captures the track, lecture, page, voice, TTS profile,
speech-generation speed, and playback position when a generated page is loaded.
A page can receive feedback before its audio has been generated; in that case
only the lecture/page context is saved. Changing pages after typing begins does
not silently retarget the draft.

**Save feedback** writes a new JSON record under the same private `feedback/`
directory used by the visual player. Records contain the spoken-text and page
fingerprints; generated-page feedback additionally includes the audio cache
identity and audio SHA-256. A source edit or regeneration that invalidates the
captured identity prevents stale submissions. Browser-local drafts are keyed
by track, lecture, TTS profile, voice, and synthesis speed, and survive page
and lecture switching. A failed save retains the draft.

Both players use `/api/feedback` and the server's `--feedback-directory` option.
This does not require re-synthesizing speech or changing the lecture sources.

## Long-passage narration experiments

`make tts-experiment` compares three conditioning strategies without replacing a
lecture's normal narration: `original` uses the approved reference throughout;
`previous` uses the preceding generated phrase after the first passage;
`anchored` combines the original excerpt and preceding phrase **into one reference
recording**. The last strategy is a composite-reference experiment, not native
multi-context inference. All variants share the first generation and use the same
text, instruction, model and seed. A seed does not guarantee deterministic server
inference.

First render the selected deck's Manim scenes as usual. Then, from the repository root:

```bash
make tts-experiment DECK=operators-rayleigh-ritz \
  VOICE_DIR=/path/to/server-shared/voice-references \
  TTS_ENDPOINT="$LECTURE_TTS_ENDPOINT" \
  TTS_PROFILE=crall-math-dk-v2-breeze-tts2
```

Set `LECTURE_TTS_ENDPOINT` locally to your server's speech URL. `VOICE_DIR` must
be a writable directory that the server reads for voice references; the runner
publishes immutable, content-named `.wav`/`.txt` pairs there. It never replaces the
original named recording. The default reference files are
`crall-math-dk-v2.wav` and `crall-math-dk-v2.txt` under that directory. Override
`REFERENCE_AUDIO` and `REFERENCE_TEXT` together to use another approved pair.
Keep recordings and personal reference information outside Git.

The pilot selects `RrCompress RrQuotient RrSolve`. Set `EXPERIMENT_SCENES` to
other scene names, `CONDITIONING_MODES` to a subset of
`original previous anchored`, and use the usual `TTS_MODEL`, `TTS_VOICE`,
`TTS_INSTRUCTION`, `TTS_REQUEST` and `TTS_SETTINGS` Make options. Other controls
pass through `EXPERIMENT_ARGS`, for example:

```bash
make tts-experiment DECK=operators-rayleigh-ritz \
  VOICE_DIR=/path/to/server-shared/voice-references \
  TTS_ENDPOINT="$LECTURE_TTS_ENDPOINT" \
  EXPERIMENT_ARGS='--max-words 120 --tail-seconds 6 --skip-video'
```

The optional `align` extra downloads an English Wav2Vec2 acoustic model on first
use and installs CPU PyTorch on Linux. Models stay in the local Hugging Face
cache. The experiment runs the model on CPU; it does not need the TTS server's
GPU. FFmpeg is required. `uv` installs these optional dependencies automatically
for this Make target. The upstream acoustic model is
[`facebook/wav2vec2-base-960h`](https://huggingface.co/facebook/wav2vec2-base-960h).

Passages contain complete sentences and can span several visual builds. Forced
alignment locates the authored words in generated speech. Existing animations
then wait for their cue, play, and retain their result. Authored phrase cues and
source animation offsets live in a lecture's `animation_cues.yaml`; see
[the Rayleigh–Ritz cues](../../lectures/002749_rayleigh_ritz/animation_cues.yaml).
Each `phrase` must occur exactly once within its narrated build. `visual_at`
selects an increasing time offset within the original Manim clip;
`offset_seconds` optionally adjusts its spoken cue. Missing cue files fall back
to one animation per build. This estimates timing, **not** pronunciation: review
low-confidence words and listen to the result. The timing manifest records both
cue confidence and any animation speed adjustment needed to fit the speech.

Open the printed `renders/experiments/<deck>/<run>/index.html` through the media
server's `/files/experiments/.../index.html` route. It includes synchronized
videos, optional captions, speeds up to 4×, raw/processed audio, individual
passages, join excerpts, generation times, and loudness diagnostics. Captions
come from the authored transcript; they can therefore conceal a spoken error.
The experiment is not registered as a separate lecture in the library.

Speech is cached by its actual API request, including endpoint, text, temporary
conditioning voice, model and settings. A preceding clip's changed audio changes
the next conditioning voice, invalidating subsequent chained speech. Alignment
is cached by audio bytes, transcript and acoustic model revision. Visual event
clips are cached independently by source animation, timing and encoding settings.
Editing cue timing reassembles video without regenerating speech. `REFRESH_AUDIO=1`
creates a fresh attempt directory, preserving earlier listening comparisons.
Generated references remain in the shared local directory for reproducibility;
remove an experiment's `dkvis-exp-*` pairs only when they are no longer needed
for replaying its requests. Do not delete ordinary named voice references.

Generation/request settings, reference basenames and fingerprints, conditioning
lineage, source snapshot, alignment revision and processing measurements accompany
the output. Detailed stage timings also enter `renders/logs/`. All generated
media, references, reports and model caches remain untracked.
