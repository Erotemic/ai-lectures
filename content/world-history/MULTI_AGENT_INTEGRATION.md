# Adding World History lectures with concurrent authors

World History lectures have stable six-digit identifiers, transcript files,
per-lecture metadata, and two shared catalogs: `track.json` and
`metadata/sources.json`. Multiple authors can work on separate series while
other authors extend the archaeology track. The catalogs therefore need an
additive merge at integration time.

## Before authoring

Inspect the **current** `track.json` and the transcript filenames, then choose
unused IDs. The `200000`–`299000` range is reserved for *How We Know*
archaeology. Historical IDs stay fixed because audio playback, feedback, and
caches refer to them. Coordination of numeric ranges is still necessary when
authors start simultaneously; the installer rejects conflicting allocations.

A new lecture overlay should contain:

- New `NNNNNN-topic.md` transcripts and `metadata/NNNNNN.json` records.
- A proposed `track.json` with those lecture entries and their browsing order.
- A proposed `metadata/sources.json` including the references needed by the
  new metadata. The proposal may be based on an earlier snapshot; its existing
  entries must still agree with the local copies.
- New, uniquely named series documentation where needed.

Avoid publishing stale copies of `README.md`, `AGENTS.md`, or a shared test file.
Those files require targeted integration after their current contents have been
reviewed. Do not reduce or bypass the test that compares the entire transcript
inventory against the catalog.

## Applying a lecture overlay

From the repository root, with the merge tool already installed:

```bash
python tools/merge_world_history_overlay.py \
    --zip ~/Downloads/new-world-history-series-overlay.zip --dry-run
python tools/merge_world_history_overlay.py \
    --zip ~/Downloads/new-world-history-series-overlay.zip
python -m pytest tests/test_audio_course_tracks.py -k world_history -q
```

The installer validates all proposed changes before writing. It merges the two
shared JSON catalogs by stable identifier, preserves existing listening order,
appends incoming records, and verifies that every transcript and metadata
record is accounted for. Different definitions of an existing ID, a missing
research source, a mismatched transcript, or an existing file with different
content causes an explicit conflict, with no files changed. Per-checkout file
locking serializes independent installers.

**Do not run `unzip -o` directly into the repository for lecture overlays.**
It overwrites shared catalogs and shared prose without understanding concurrent
changes. `unzip -l` or `unzip -t` are safe for examining an incoming archive.

## If a shared catalog was already overwritten

Recover the exact missing records from the relevant Git commits and assemble a
small recovery JSON with `sections`, `lectures`, and `sources`. Then run:

```bash
python tools/merge_world_history_overlay.py --bundle path/to/recovery.json
```

Verify that the original lecture files and metadata are present. This restores
catalog rows and research sources without renumbering or rewriting narration.
Only then update any shared README or hard-coded reader assertions against the
current checkout and rerun the catalog/reader tests.
