# AI Lectures portable reader

One local server browses independently installed lecture packs, plays prepared
audio, and optionally uses the repository's existing TTS clients. Listener
profiles are optional names for shared progress. Content never requires login.

From a source checkout:

```bash
python -m ailectures serve --repository .
```

Open `http://127.0.0.1:8001/`. `make serve` selects the same library and explicitly
binds to the LAN, following this repository's existing serving convention.
Original presentation bookmarks and `/audio` remain available through a lazily
loaded compatibility app. Content-pack updates require no restart. Changes to
server code require restarting the process.

Collections provide title/ID search, section and session jumps, and expandable
contents. Search changes the view; playback still follows the full collection's
original order. Breadcrumbs show the collection hierarchy, while return links
preserve the route and search used to open a lecture. References, related routes,
complete original sequences, and recording preparation remain under Resources
& connections.

Press `/` to search the current collection, or Ctrl/Cmd+K to search the library.
Browsing options include category, audience, audio availability, every nested
collection, and sorting by title or duration. Exact lecture IDs work in both
searches. Browser asset changes require a server restart, just like server code.

The native Learning map separates teaching preparation, proof dependencies,
source relationships and listening order. Open it from the header or from a
collection or lecture, filter its connections, and select an entry to follow
incoming or outgoing links. The complete view and original component evidence
remain available alongside the diagram preview. It works with installed packs
without the presentation tools.

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
