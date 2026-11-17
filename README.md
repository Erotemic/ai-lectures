# AI Lectures

An AI-authored library of lectures and stories, with a local web reader,
optional speech synthesis, and portable content packs. The collection covers
mathematics, history, literature, music, practical subjects, and children's
stories. Manuscripts and source notes live in Git; recordings and listener
state live in a separate local library.

The project is built around listening. A lecture should carry its explanation
in spoken language, with equations, code, images, scores, and references in
companions where they help. Material can be read as text, heard independently,
or followed through an ordered collection. Authors can revise a manuscript or
add a subject without rebuilding presentations or editing a global registry.

## Start the library

From the repository root, with Python 3.11–3.13 and
[uv](https://docs.astral.sh/uv/) installed:

```bash
make serve
```

Open <http://127.0.0.1:8001/>. `make serve` installs the serving dependencies and
binds to the LAN; another device can use the server's address on port 8001.
Use `make serve PORT=8002` to change the port, or `make serve HOST=127.0.0.1`
to bind only to this machine. Named listeners share progress and queues across
devices without accounts or passwords; the LAN binding is intended for a
trusted network.

Browsing transcripts and playing prepared audio need no running AI model,
Manim, VTK, or LaTeX. Generating new audio additionally needs a configured TTS
service and FFmpeg/ffprobe. Source content updates appear without restarting;
restart after changing server code and reload after changing browser code.

| Page | What it does |
| --- | --- |
| Library and Collections | Browse subjects, search lectures, sort by subject dates, and choose guided routes or extended studies |
| Study plan | Build a prerequisite order for a goal or starting point, with known and uncertain background |
| Lecture | Read the transcript, play or prepare audio, follow the text, and open references or companions |
| Listening | Resume saved positions and manage a listening queue |
| Production | Prepare recordings and inspect, cancel, or retry generation jobs |
| Packs | Inspect installed content, audio coverage, and storage |
| References and Feedback | Find further reading and record feedback against the relevant content revision |

The [content pack guide](docs/content-packs.md) documents the reader, server,
TTS configuration, exports, backups, and feedback.

## What's in the collection

The source directories contain both drafts and developed series. Coverage and
review status vary by subject; an indexed manuscript is not a claim that it has
been independently verified or has a complete recording. Browse the running
library for the current inventory and audio availability.

| Area | Examples and source locations |
| --- | --- |
| Mathematics and computing | [Analysis](draft-stages/tts-analysis/), [algebra](draft-stages/tts-abstract-algebra/), [topology and geometry](draft-stages/tts-topology-geometry/), [category theory](draft-stages/tts-category-theory/), [probability](draft-stages/tts-probability-measure/), and [algorithms](draft-stages/tts-algorithms-computability-complexity/) |
| History and science | [Ancient and medieval worlds](content/ancient-medieval-world/), [world history and historical evidence](draft-stages/tts-world-history/), [modern history](draft-stages/tts-modern-world/), [deep time](draft-stages/tts-deep-time/), and [people behind mathematical ideas](draft-stages/tts-history/) |
| Literature and writing | [Classics before 1900](draft-stages/tts-pre-1900-literature/), [twentieth-century literature](draft-stages/tts-modern-literature/), [fiction writing](draft-stages/tts-fiction-writing/), and [comedy](draft-stages/tts-comedy-history/) |
| Music | [Music theory and composition](draft-stages/tts-music-theory/), including pack-local examples and companions |
| Practical subjects and trades | [Household maintenance](draft-stages/tts-practical-household-maintenance/), [food science](draft-stages/tts-practical-food-science/), [tools and measurement](draft-stages/tts-practical-tools-and-measurement/), [electrical systems](draft-stages/tts-trades-electrical/), and other practical/trade packs |
| Children's stories | [Standalone bedtime stories](content/bedtime-stories/), [episodic stories](content/childrens-bedtime-stories-episodic-ages-3-4/), and [Brook Road Builders](content/brook-road-builders-ages-3-4/) |

A **pack** owns its manuscripts, metadata, sources, and examples. A
**collection** is an ordered listening route through that material. Pack-local
navigation can offer a survey and deeper branches using the same lecture IDs
and recordings. Reorganizing a route does not require copying transcripts or
regenerating speech.

Mathematics opens a [subject guide](content/mathematics-guide/) with four suggested
learning paths and six subject families. Click topic tags to follow concepts
across courses, or adapt a path in Study plan using your known and uncertain
background. [Subject organization and tags](docs/content-packs.md#subjects-topic-tags-and-learning-paths)
are source-owned metadata; advanced courses and individual lectures remain
directly accessible.

Collections can also display oldest or newest first using work dates, periods
covered, story settings, lifespans, or textual witnesses. Date ranges and
uncertainty stay visible; undated items come last. **Listen in displayed order**
adds a chronological view to your queue, including any search filter. The
authored collection order remains available. See the
[date metadata guide](docs/content-packs.md#dates-and-chronological-browsing)
when extending a pack's coverage.

## Write and revise content

Start with [the lecture style rules](LECTURE_STYLE_RULES.md). The material
determines form and length; no fixed runtime, word count, or narrative template
is required. Support substantive claims, make prerequisites clear, and keep
spoken narration understandable without the authoring conversation.

New subjects can use an independently owned directory:

```text
content/my-subject/
  track.json                  # stable IDs and manuscript inventory
  001000-introduction.md      # authored text
  metadata/001000.json        # lecture metadata and reading references
  metadata/sources.json       # bibliographic source records
  navigation.json            # optional listening routes
  examples/                  # optional examples and companions
```

Existing packs under `draft-stages/tts-*/` remain supported; their directory
name does not determine their editorial readiness. Keep their established
paths and IDs when extending them. Narration is the text between one
`<!-- BEGIN SPOKEN LECTURE -->` / `<!-- END SPOKEN LECTURE -->` pair in each
manuscript. Display material and detailed references can remain outside that
region. Track sources, model attribution, and substantive revisions with the
content.

See [authoring a source pack](docs/content-packs.md#author-an-independent-source-pack)
for the manifest and metadata contract, and
[the handoff guide](docs/agent-content-handoff.md) for independent authoring and
recoverable ZIP imports. Routine content delivery needs no TTS run, media build,
or repository-wide test suite.

[Editorial review](reviews/README.md) records findings against particular
revisions, with source checking and adjudication separate from the initial
reviewer. Findings are diagnostics: they do not disable usable lectures or
certify that an unflagged lecture is correct. Listener feedback retains the
transcript and recording context needed for later revision.

## Generate and share audio

Configure speech services in `tts.toml`, with machine-specific overrides in the
ignored `tts.local.toml`. The Production page can prepare a lecture or a whole
collection. The equivalent CLI includes:

```bash
uv run --extra serve python -m ailectures prepare --repository . \
  --lecture music-theory:001000 --profile kokoro
```

Completed recordings are retained independently for different narrators.
Matching speech can be reused when surrounding metadata changes; preparation
requests survive a server restart. See
[the production workflow](docs/content-packs.md#prepare-audio)
for configuration and job behavior.

Export a source pack with its matching installed recordings:

```bash
uv run --extra serve python -m ailectures export --repository . \
  --pack music-theory --output /path/to/transfer/music-theory \
  --zip /path/to/transfer/music-theory.zip
```

A standalone reader can install and play prepared packs without this checkout,
the rendering stack, FFmpeg, or an inference service. The
[reader installation guide](ailectures/README.md) covers building and installing
its wheel; the [transfer guide](docs/content-packs.md#export-and-transfer)
explains source-only exports, recordings, and revisions.

## Keep source and personal data separate

Commit manuscripts, manifests, bibliographic records, examples, attribution,
and code. The default ignored `library-data/` directory holds installed packs,
recordings, listener progress, queues, feedback, and preparation state. Preserve
it when moving machines; it contains durable data as well as build caches.

```bash
uv run --extra serve python -m ailectures backup /path/to/library-backup.zip
uv run --extra serve python -m ailectures --library /path/to/new-library \
  restore /path/to/library-backup.zip
```

A library backup and a Git checkout preserve different things: export source
packs when transferring authored material to a reader without the repository.
See [storage and backups](docs/content-packs.md#storage-and-backups) for what is
included. Keep private endpoints, voice references, recordings, and personal
experiments in ignored local storage. `renders/`, `media/`, and `slides-*/`
remain generated presentation outputs.

## Related work

These projects address overlapping parts of authoring, synthesis, and listening.
The [related-work notes](docs/related-work.md) give source links, scope, research
results, and possible directions for this repository.

| Project | Relevant work |
| --- | --- |
| [okcourse](https://github.com/mmacy/okcourse) | Generates course outlines, lecture manuscripts, cover art, and audiobook-style audio |
| [Google Audio Overviews](https://support.google.com/gemininotebook/answer/16212820?hl=en) | Creates spoken overviews from uploaded sources, with configurable formats and focus |
| [Open Notebook](https://github.com/lfnovo/open-notebook) | Self-hosted source organization, research tools, and podcast generation |
| [Podcastfy](https://github.com/souzatharsis/podcastfy) | A Python pipeline for turning multimodal sources into configurable audio conversations |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Converts existing ebooks into narrated audiobooks with chapters and metadata |
| [Audiobookshelf](https://github.com/advplyr/audiobookshelf) | Self-hosted audiobook/podcast playback, libraries, and progress synchronization |
| [Storyteller](https://storyteller-platform.dev/) | Aligns ebooks and audiobooks for synchronized reading and listening using EPUB media overlays |

For research on learning, [PAIGE (Do et al., 2024)](https://arxiv.org/abs/2409.04645)
studies personalized educational podcasts; a
[reflection-prompt study (Menon et al., 2025)](https://arxiv.org/abs/2508.04787)
reports similar learning outcomes across its conditions and lower perceived
attractiveness with prompts. These studies motivate evaluation; neither
establishes learning benefits for this library.

## Repository map

| Location | Purpose |
| --- | --- |
| `ailectures/` | Portable reader, catalog, storage, playback UI, and production integration |
| `content/`, `draft-stages/tts-*/` | Authored source packs and their local metadata |
| `reviews/` | Revision-bound editorial findings and review tooling contract |
| `tools/` | Content handoffs, audits, review runner, and maintenance utilities |
| `docs/content-packs.md` | Reader operation, source format, TTS, transfer, and backups |
| `docs/agent-content-handoff.md` | Independent authoring and recoverable imports |
| `docs/related-work.md` | Related software, learning research, and publishing standards |
| `lectures/`, `dkvis/`, `curriculum/`, `companion-slides/` | Original presentation curriculum, shared media tools, and visual companions |

## Narrated presentations

The project began with Davis–Kahan mathematics and its formalization. The
Narrated Manim/VTK lectures, Lean companions, and the slide/video pipeline remain available;
they are one part of a broader library. Original presentations are at
`/presentations`, the compatibility audio reader is at `/audio`, and the older
curriculum graph is at `/learning-paths`.

<a id="browse-and-watch-rendered-material"></a>

Use [the presentation production guide](dkvis/presentation/README.md) for
rendering, narrated video, audio processing, and the original media server;
the indexed lectures retain their existing scene sequences and narration.
Unnarrated Davis–Kahan decks and standalone demos are maintained in the `dk`
repository. This checkout keeps the scene implementations and VTK asset renderer
needed by the narrated sine-theta lecture, the narrated matching lectures, and
shared media production. Checked mathematical models and their tests remain here.
The [original vision and history plan](docs/planning/lecture-project-vision-and-history.md)
records the mathematical project's goals.

### Updating one scene

[Partial rebuild instructions](dkvis/presentation/README.md#updating-one-scene)
now live with the presentation tools, including the requirement to rebuild the
cover when visible model attribution changes.
