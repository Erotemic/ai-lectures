# AI Lectures portable reader

One local server browses independently installed lecture packs, plays prepared
audio, and optionally uses the repository's existing TTS clients. Listener
profiles are optional names for shared progress. Content never requires login.

From a source checkout:

```bash
python -m ailectures serve --repository .
```

Open `http://127.0.0.1:18701/`. `make serve` selects the same library and explicitly
binds to the LAN, following this repository's existing serving convention.
Original presentations remain available at `/presentations`. Old `/audio`
bookmarks redirect into the library. Content-pack updates require no restart.
Changes to server code require restarting the process.

Library is the starting point for browsing collections by category. Lectures
lists individual items, and History keeps recent listening and the queue.
Collections provide title/ID search, section and session jumps, and expandable
contents. Search changes the view; playback still follows the full collection's
original order. Breadcrumbs show the collection hierarchy, while return links
preserve the route and search used to open a lecture. References, related routes,
and complete original sequences remain under Resources & connections.
**Generate all audio** appears under **Resources & connections** when generation
is available. **Cache whole lecture** is under **Audio blocks & generation**.
Older recordings remain playable. Select a current profile to generate new
audio. The reader distinguishes
missing audio for the selected profile revision from available older recordings.
Spoken edits require audio for the revised transcript. The lecture page links
to an available earlier recording, and preparation reuses blocks whose text
and rendering settings still match.
In Production, **Cancel all preparation jobs** stops queued and running jobs.
Cached audio stays available when you retry.

For repeatable bulk generation, `python -m ailectures voices` lists saved
rendering profiles. `python -m ailectures queue --selection FILE --saved-profile
PROFILE_OR_VOICE` queues the same declaration used by an export; use an exact
profile ID, label, or unique voice ID. Repeat
`--saved-profile` for multiple voices and add `--dry-run` to preview. It skips
complete item/profile-revision pairs, persists jobs without starting synthesis,
and lets the running generation-enabled reader consume them. See the
[curated preparation workflow](../tools/deployments/README.md#prepare-on-the-production-machine).

The Library landing page's **Recently listened** section can be collapsed using
its heading. It starts expanded and remembers the open/closed choice for each
listener in that browser. The expanded section retains resume, next-item and
full listening-history links.

### Illustrations

Season sections and their episodes share covers declared in a pack's
`visuals.json`. The default asset directory is `generated-assets/accepted`.
To serve images stored elsewhere, pass `--visual-root /path/to/illustrations`
to `ailectures serve` or set `visual_root` in the server TOML. Without a source
checkout, the default is relative to the server's working directory.

Use an `images` object with an image ID, relative PNG, JPEG, or WebP `path`, descriptive `alt`
text, and optional `caption`. The `sections` object maps stable section keys
from `track.json` to image IDs. A local lecture ID in `lectures` can set a
different `cover` or add `inline` placements with an `image` ID and an
`after` field containing a unique passage from the spoken transcript.
An inline figure appears after the corresponding paragraph or spoken sentence.
For a display equation, declare an ID in `equations` with `mathml` containing
a `<math>` element with presentation markup. The inline placement uses
`equation` in place of `image`, with the same `after` anchor. The reader renders
equations directly from the pack metadata. The spoken text and audio timing
stay separate from the placement.

The reader caches small WebP display copies under `library-data/build-cache/visuals`
when Pillow is available. The repository's `serve` extra includes Pillow.
The standalone reader displays the originals and can use the optional
`illustrations` extra for WebP display copies. Click any illustration to open
its original. Git and library exports carry the placement metadata.
Supply the original files independently on each server.

Narrated source decks use the same audio lecture model as the standalone tracks.
Their `g1:` IDs and slide links remain stable; authored scene narration is adapted
to the shared transcript format without speaking editorial Why/Recall notes.
Content discovery and playback need no deck or Manim imports. The old production
parser delegates to the shared parser in `ailectures/manuscripts.py`.
Every lecture page links to its owning track, independently of search, graph,
or listening-route return links. Expanded inventory rows link to that track too.
“Not generated” means a usable transcript exists and audio can be queued.

Named references to lectures, tracks, collections, and content packs should link
to the relevant page or filtered contents whenever available. Pack cards and
statistics link to the pack’s lecture inventory. Current-page headings and
selection controls can remain plain text.

New web-generated recordings default to Ogg Opus. Spoken Markdown section titles
receive isolated synthesis and pauses, with title-specific instructions on
supported servers. The transcript preserves title and section-heading hierarchy
in both plain and playable views, including unspoken scene captions. Display
structure shares the player’s seek boundaries and does not invalidate audio.
Queued legacy jobs keep their original MP3 recipe.

Saved voice profiles fix one backend voice and its full rendering recipe. Manage
defaults, quick select, title instructions, rate and processing in Settings. See
[the voice profile guide](../docs/voice-profiles.md) for revisions and local state.

Selected-content deployment, stale-audio cleanup, Ogg Opus generation, and
buffered playback are described in [the deployment and audio guide](../docs/deploying-selected-library.md).
Packs can build a portable subset with its existing published audio; the CLI
includes ready-to-edit children and Spider-Man/literature/history selections.

All lectures (`/lectures`) is a flat inventory of every available item, including
unindexed manuscripts and deep dives. Items appear once across overlapping
collections. Search includes descriptions, creator names, topics, places, dates,
and IDs; filters select category, pack, tag, or audio availability. Sort by title,
ID, duration, or a selected date meaning. Show all displays the full inventory
without grouping it into collections. Concise list is the default, showing up to
250 single-line rows with expandable descriptions, tags, and feedback. The View
selector also offers Detailed list and Cards; its choice is saved on this device.
Filters, view choices, and the full-list view are bookmarkable, and lecture
return links preserve them. Browsing this inventory does not change collection
playback order. When sorting by a date, concise rows show that date, and a
coverage count makes missing metadata visible. Date coverage filters select
dated or undated items; undated items always follow dated items. Story-setting
dates remain distinct from publication, composition, and nonfictional historical
environments. Stats links to both dated and undated groups for each date meaning.

Press `/` to search the current collection, or Ctrl/Cmd+K to search the library.
Browsing options include category, audience, audio availability, every nested
collection, and sorting by title or duration. Exact lecture IDs work in both
searches. Browser asset changes require a server restart, just like server code.

Stats (`/stats`) summarizes the live catalog: unique lectures, collections,
packs, transcript words, estimated listening time, complete and partial audio,
and current companion files. Subject, audience, collection, and pack tables
show coverage; collection search links directly to the listening routes.
The primary coverage explorer starts with broad geographic branches and supports
topics, authors, and each date meaning. Parent totals include descendants and
count each lecture once. Expand branches to compare narrower tags and see the
largest contributing sections, their lecture shares, and estimated listening.
Each tag has a lecture list with linked titles; multi-lecture sections also
expand into their individual lecture links. The lecture count opens the full
filtered inventory. Lecture pages link back to Content stats, retaining the
coverage dimension, search, and sort in the URL.
Sections count each authored section within a pack once, with unsectioned
lectures counted separately; they are editorial units, not distinct works.
Order can compare names, section counts, lecture counts, or listening time.
Labels without a recorded broader geographic path remain available separately,
and metadata completeness is shown for the selected dimension. Original direct
place counts are retained under Metadata coverage and direct place labels.
Every Stats section is independently collapsible and remembers its state on this
device. Coverage opens initially; the remaining detail sections start closed.
Geography starts at continent scale, with North and South America beneath the
Americas and Central America beneath North America. Oceans, polar areas, and
regions spanning continents appear separately. Historical names retain their
identity; context-specific paths resolve ambiguous place names only in the
lectures that supply that context.
Library totals count each lecture once across overlapping routes. Listening
estimates use 145 words per minute. The former Presentations navigation tab
has been removed; existing presentation bookmarks still work.

Lecture items now show compact descriptions and work creator credits. Search
includes descriptions, outlines, creator names, and tags. Place, named-period,
and date tags help explore coverage; date tags distinguish publication/work,
historical period, story setting, lifetime, and surviving witness. Stats includes
these coverage views and work authors, with links to the corresponding tags.
Catalog clients can inspect these fields without downloading transcripts.

Topic graph (`/topic-graph`) starts with broad topics and adds connections in
batches as you click nodes. Expanding another branch keeps earlier branches;
there is no fixed neighborhood limit. Topics reveal finer topics before lecture
nodes, with separate controls to add lecture batches. Search can reveal a deep
path without loading all its siblings. Collapse branch (or Shift-click), Fit
graph, Focus selected, and Reset graph control the explored view. Zooming out
hides finer topics, lectures, and labels; offscreen nodes are omitted from SVG
rendering while their exploration state is retained. Branches, positions, and
zoom are saved per collection/dimension for the current browser tab. Lecture
lists are collapsible and contain links back to the lecture pages, with audio
availability shown separately from lecture membership. Explicit expansion frames
and reveals the new batch even when the graph was zoomed out. Existing reverse
connections are not offered again as new connections.

Tags support explicit broader-to-narrower paths for topics, geography, and
time. Stats → Coverage from broad to specific expands these dimensions with
unique lecture counts; any parent label filters all lectures carrying that
path. Lecture pages expose their paths, and All lectures searches and filters
ancestor labels as well as specific tags. Common existing tags acquire curated
broader associations; authors can add pack-local `tag_paths` without registration.
Date paths distinguish composition from publication, story setting, historical
coverage, lifetime, and textual witnesses. Wide ranges stay broad, and uncertain
years retain their qualifiers. See [the authoring contract](../docs/content-packs.md#coarse-to-fine-tag-paths).

Lecture tools & feedback is a collapsible sidebar, initially open on desktops
and closed on phones; the choice is saved on this device. Ratings and the heart
favorite toggle sit beside Lecture feedback. The sidebar links to both the plain
text transcript and full raw lecture JSON for the displayed release. Further
reading expands independently and links to a dedicated reading page with source
authors, publication details, notes, and full source records where available.

Lectures have 1–5-star ratings (with a clear option) and a heart favorite toggle.
These choices belong to the selected listener and sync across devices; “This
device” keeps them in browser storage. Offline changes are saved locally and
retried automatically. Ratings and hearts merge independently so changing one
cannot erase the other. Cleared choices are retained as tombstones to prevent
an older device or imported backup from resurrecting them. Listener exports,
imports, profile merges, and library backups retain these choices. They follow
stable lecture IDs across transcript revisions and record the revision at which
each choice was made.

All lectures → Filter and sort → Your feedback selects favorites, rated or
unrated lectures, or a minimum star rating. Order → Your highest rated sorts
by your stars. Each result has a heart toggle and your current rating. Shared
listener rating totals and distributions are available under Packs → Review
feedback → Star ratings & favorites; device-only choices are not included.
Pending audio blocks use an orange fill and solid border, with a deeper orange
for the block currently rendering. Numbers and state labels remain available.

On phones, Menu opens all navigation and listener controls. The compact fixed
player keeps the lecture, playing track, timeline, 15-second skips, Next and
upcoming lecture visible. More retains native audio controls, playback speed,
track selection and automatic continuation. Page spacing follows the player's
actual height, including expanded controls and device safe areas.

Automatic next-lecture playback follows the selected track's complete order,
independently of browsing or search filters. More → Playing track can change that
route; starting a listening queue follows the queue instead. The continuation
preference is remembered on the device. Complete prepared recordings continue
through their blocks by default, respecting an explicitly saved single-block
preference. Audio blocks & generation retains all preparation, block-selection,
lookahead, cancellation and speech-speed controls. Automatic lecture changes
use prepared audio and stop when the selected voice has none; they do not start
missing-audio generation. Queued occurrences restart from the beginning, and
track/queue endings stop without wrapping.

The native Learning map separates teaching preparation, proof dependencies,
source relationships and listening order. Open it from the header or from a
collection or lecture, filter its connections, and select an entry to follow
incoming or outgoing links. The complete view and original component evidence
remain available alongside the diagram preview. It works with installed packs
without the presentation tools.

Study plan constructs an order from your chosen destination or collection and
your stated background. Required teaching links constrain the order; authored
listening order breaks ties. Starting partway through a collection still adds
unmet prerequisites. Confident familiarity removes material, while uncertain
familiarity stays as review unless explicitly assumed. Readiness questions,
explanations, missing material, cycles and incomplete coverage remain visible.
Listen in this order adds the result to your queue and starts its first step.

Familiarity is independent of listening completion. Anonymous choices stay on
the device; named listeners share them and retain them in history exports and
library backups. Content changes require reconfirming familiarity, including
when a short part's ID survives as a larger combined lecture. Metadata-only
changes retain the manuscript identity used for familiarity. The map has its
existing detailed operator-course relationships plus reviewed learning notes
for 21 foundational proof, linear-algebra, multivariable and introductory-analysis
lectures; other coverage is explicitly incomplete.

Lecture pages open prepared HTML slide companions directly, with attribution
and downloads. A repository checkout also exposes its existing slide decks and
an explicit Build action when the optional renderer is installed. Opening the
panel never builds a deck or starts audio generation. Missing slide tools do
not prevent reading or listening.

Packs → Transfer this pack creates a downloadable ZIP of the selected pack's
transcripts, notes, companions and optionally its published recordings. This
does not generate missing audio or include listening history. These are playback
releases; independent authors still exchange ordinary source-directory ZIPs
using the source-overlay handoff guide.

For an independent playback installation, build and transfer the reader wheel:

```bash
uv build ailectures --out-dir /path/to/transfer
```

On the playback machine, install `ailectures_reader-0.1.0-py3-none-any.whl` with
pip or uv, then run:

```bash
ailectures --library /path/to/library install /path/to/content-pack.zip
ailectures --library /path/to/library serve --host 0.0.0.0
```

The reader depends on Starlette and Uvicorn. Prepared playback imports no
`dkvis`, NumPy, NetworkX, Manim, VTK, model runtime, or TTS configuration, and
requires no FFmpeg executable. All browser assets are packaged locally.
Repository adapters and optional production use the source checkout's existing
dependencies and configuration; the standalone wheel is sufficient for playback.

See [the operator and pack guide](../docs/content-packs.md) in the source
repository for export, revisions, live discovery, progress, and feedback.

Authored audio sources use `content/<namespace>/` consistently. The original 22
scene-based narrated decks remain in `lectures/`. Reader data, recordings and
build caches are separate from source packs; moving sources does not move them.

Catalog construction indexes collection membership and the shared tag vocabulary,
and unchanged selections reuse already loaded catalog documents. Installed
releases retain a validation fingerprint across restarts: unchanged managed files
skip repeated full media hashing, while changed files and new imports undergo
validation. Playback reports changed published checksums as warnings and serves
the available bytes; missing or undecodable audio still cannot play.

New historical source snapshots store shared lecture rows plus small revision
indexes, so generating another block does not duplicate every transcript in its
pack. Existing snapshots remain readable and are not deleted or compacted by this
change. A database already enlarged by old snapshots will retain that allocated
space.
