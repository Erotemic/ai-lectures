# Spoken-language word and phrase clouds

The library's **Word cloud** page (`/word-cloud`) visualizes the language actually
spoken in its lectures. It works with source repositories and installed reader
packs, without requiring audio generation, JavaScript libraries, or external
services. It is also linked from the Stats page.

- Choose all lectures or a single content pack, 1-4 consecutive words, and the
  number of terms to display (top 25-150).
- Rank by **occurrences** or by the **number of different lectures** containing
  a phrase. The latter helps find phrases that recur across many manuscripts,
  rather than repetitions within one lecture.
- Raise the minimum lecture count to exclude phrases isolated to individual
  talks. Common function-only expressions are hidden by default, but multiword
  phrases containing substantive words (such as *this matters because*) remain.
- Click terms in the cloud or count table, or search for an arbitrary phrase, to
  inspect its total frequency, rate per 10,000 spoken words, and excerpts from
  the lectures in which it occurs most often. The excerpt links lead directly
  to the corresponding lecture page.
- Export the visualization as a portable SVG or the full ranked table as CSV.

The command line uses the **same** normalization, counting, and SVG layout:

```bash
python -m ailectures word-cloud --repository . --n 3 --top 60 --rank lectures
python -m ailectures word-cloud --repository . --pack world-history --n 2 --find "matters"
python -m ailectures word-cloud --repository . --find-only --find "what matters is"
python -m ailectures word-cloud --repository . --n 4 \
  --svg "$HOME/Downloads/lecture-fourgrams.svg"
```

The CLI also supports `--lecture namespace:ID`, `--rank count`, `--min-lectures`,
`--include-common`, `--find-only`, and `--json`. From an installed reader without a source
repository, omit `--repository` and pass `--library` before `word-cloud` to
analyze installed transcripts.

## Counting rules and interpretation

Only the **spoken transcript** is counted. Editorial notes, citations, metadata,
source catalogs, and TTS artifacts are excluded. Unicode letters, case, and
apostrophe variants are normalized; digits and notation identifiers are
excluded. Phrase windows do not span sentence or paragraph boundaries.

Counts are absolute, not adjusted for authorship, genre, period, or vocabulary.
Common technical terms can be frequent for good reasons. A word cloud is a
screening tool, not an automatic prose-quality judgment. Review the actual
passages before changing manuscripts. Only top terms appear on the image when
space is available; the ranked table and CSV retain the full selection.

The backend recomputes after manuscript revisions and caches the most recent
queries per catalog generation. For a very large corpus, the first request for
a new phrase length can take tens of seconds; changing only top-k does not
recount, and recent queries are served from memory. Long n-gram counts may require substantial temporary RAM
because they are exact, not sampled.
