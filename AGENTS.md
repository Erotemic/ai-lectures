# Agent instructions for `ai-lectures`

The repository is an extensible AI-authored lecture library. The current
mathematical material originated in a Davis--Kahan research project, but future
curricula need not be about operator theory. Prioritize rigorous, standalone,
listener-paced narration, supporting mathematics, and relevant reading notes
when editing `draft-stages/tts-lectures/`. Preserve the existing working media
production tools; broader reorganizations are outside a lecture-content pass.


The visualizations are reusable Manim/VTK scenes composed into several decks.
Shared slide/transcript/TTS/video production lives in `dkvis/presentation/`.
Learning scenes and models belong in `dkvis/learning/<topic>/`; authored lecture
text lives in numbered `lectures/` folders. `lectures/index.yaml` owns stable
lecture IDs, prerequisites and course membership; `python -m dkvis.lectures`
previews NetworkX topological ordering, and `--apply` organizes folders.
Use `lecture_path(ID)` in deck manifests rather than hard-coding numbered paths.
Ordering keys must not become Python package names or deck identities. Read
`dkvis/learning/README.md` for the module contract and current catalog.
`DeckSpec.narration` selects an authored transcript. Do not add topic names,
scene-name prefixes, or transcript paths to the shared production tools.
Keep legacy scene files where they are until a conceptual migration is useful.
Preserve presentation content and ordering during organization-only work.

The completed presentation is now named `kitware-talk`; **do not change its
scene order or change a scene just to improve the new `comprehensive` deck**.
The `comprehensive` deck is the editable long presentation and should include
every distinct source-grounded mathematical visualization in a coherent order.
The older reference decks and `study` continue as regression/learning surfaces.

For substantial slide work, also read `briefs/slide-authoring.md` and
`dkvis/components/README.md`. Read the relevant deck brief when editing that
deck; the frozen Kitware, comprehensive, and deep-study briefs have distinct
scopes.

The old `sine-theta-short`, part decks and `sine-theta-full` are reference
compositions. Preserve their behavior. Use `dkvis/decks/comprehensive.py` to
reorganize the long presentation, rather than modifying the frozen Kitware talk.

Render and inspect slides before claiming a visual improvement. Use draft
quality while iterating. Every scene's final build must contain the complete
intended static content because the handout generator captures final builds.

Presentation-specific `*` / `**` depth belongs in the deck manifest.  Existing
class-level `depth` attributes are compatibility fallbacks and should disappear
as scenes are migrated.

The checked numerical models and their tests are evidence-bearing code.  Do not
change them to make a picture prettier.  If a new visualization needs a new
specialization, implement and test it in the model layer first.

Prefer small conceptual migrations over a mechanical rename of the whole tree.
For future visual work, use short incremental passes:

1. list and render the affected scenes at draft quality;
2. inspect them for clipping, unreadable math, duplicated material and color drift;
3. improve reusable scenes outside `kitware-talk` (or create alternatives);
4. render again before claiming a visual improvement;
5. rebuild `comprehensive` and its standalone HTML when the sequence is ready.

Do not write brittle tests asserting text labels, slide captions, or paragraphs.
Tests should cover numerical model behavior, deck integrity, and actual helper
behavior. Inspect rendered outputs for visual correctness.

## Novelty tour

Before editing `novelty-tour`, read [its brief](briefs/novelty-tour.md) for the
source/target color crosswalk and exact verified scope. Preserve the distinction
between this deck's transport notation and the older sine-theta notation.

## Canonical sine-theta notation

Do not reintroduce `U`/`V` as aliases for the ranges of the sine-theta frames.
The core exposition names the objects the theorem operates on directly:

- `Ahat`: operator under study in the general theorem; Lean/source names this `A`;
- `E0, A0`: trial frame and trial-coordinate operator;
- `F0`: exact wanted frame; `F1, Lambda1`: exact unwanted frame/block;
- `R = Ahat E0 - E0 A0`;
- `Theta0(E0,F0)` / `sinTheta0(E0,F0)`: angles/error between their ranges;
- `delta`: certified spectral separation, not a generic eigengap.

In perturbation slides only, keep `A` permanently equal to the original operator
and write `Ahat = A + H`.  Choose the trial pair from original `A`, so
`A E0 = E0 A0`, `R = H E0`, and `||R|| <= ||H||`.  Use `g` for an original
eigengap of `A`; never silently identify it with `delta`.  `U,V` may still be
used when they are genuinely the notation of another statement, such as
Proposition 4.4.

## Lecture authoring

Read the [project vision and history plan](docs/planning/lecture-project-vision-and-history.md)
when planning lecture coverage. The north star is understanding the full
Davis–Kahan paper, the repository's extensions, and their prerequisites. Use
Lean to progressively validate the learning map; do not block obvious useful
lecture drafts on a complete formal dependency tree. Keep teaching prerequisites,
proof dependencies, and historical influence distinct.

Before writing or revising a lecture, read
[LECTURE_STYLE_RULES.md](LECTURE_STYLE_RULES.md). It records the user's directly
expressed teaching and narration preferences. Keep those rules there rather than
copying or extending them in multiple instruction files. Technical mechanics
belong in [the authoring guide](dkvis/learning/README.md) and
[the implementation notes](briefs/slide-authoring.md).

## Lecture model provenance

Maintain the lecture's `provenance.yaml` when changing content, following the
[model attribution instructions](dkvis/learning/README.md#model-attribution).
They specify the separate slide/transcript revision records, runtime model
identity, and generation-time snapshots. Include the cover when attribution
changes so its visible model credit is refreshed; see the
[partial-update instructions](README.md#updating-one-scene).

## External illustrations

Use images with on-slide attribution. Commit selection/access logic and source
records, not downloaded images. Keep images and their license/provenance
snapshots in the portable ignored asset store, as described in
[the asset guide](docs/EXTERNAL_ASSETS.md). Reuse the attributed-image component
for portraits. Retain original creator credit separately from lecture/model
authorship; do not silently substitute another image if access fails.

## Private voice material

Private reference identifiers, recordings, reference transcripts, and personal
experiment outputs must remain in ignored local storage and out of committed
examples or documentation. Use only approved reference names in shared
examples. Raw voice recordings remain untracked even when their basenames
are approved for documentation.

## Independent content pack handoffs

Content authoring can continue independently of the library refactor. Read
[the handoff guide](docs/agent-content-handoff.md) when preparing or integrating
agent source snapshots. Each content agent should own an explicit pack directory;
keep its manuscripts, metadata, source records, and examples together. Existing
source paths remain supported; new packs can use `content/<namespace>/`.

Ordinary ZIPs of assigned pack directories are supported. Use
`tools/content_overlay.py apply` for recoverable imports and conflict protection;
snapshot receipts and hash-aware packaging are optional conveniences handled by
the tools. Plain ZIP replacements require an explicitly exclusive pack scope.
Content-only updates must not modify shared server code, global registries, or
machine state. Keep editorial diagnostics separate from delivery: an unindexed
manuscript or incomplete citation must not disable usable lectures. Do not run
repository-wide tests, TTS, or builds for routine content imports; use focused
checks when changing the relevant tooling.
Runtime pack files are exporter outputs, not an authoring contract that agents
need to hand-maintain. The specialized World History merge rules below continue
to apply to concurrent additions within that shared track.

## Concurrent World History lecture work

The World History audio track accepts contributions from multiple agents.
Stable lecture IDs are public playback/cache identifiers. Reserve and verify
new IDs against the *current* repository before starting a series. The
`200000`–`299000` range belongs to the independent *How We Know* archaeology
strand; literary series must use another free range.

Do not install a stale overlay with `unzip -o` over the repository. It can
replace `draft-stages/tts-world-history/track.json`,
`metadata/sources.json`, shared tests, or the README and discard work by
other agents. Instead apply lecture overlays with
`python tools/merge_world_history_overlay.py --zip /path/to/overlay.zip`.
That tool merges catalog additions by ID and refuses differing existing files.
Contributions should contain new transcript and per-lecture metadata files,
unique per-series documentation, and proposed shared JSON catalogs. Avoid
rewriting common tests and README files for routine lecture additions. Run the
world-history reader tests after integrating and verify the full inventory.

<!-- BEGIN llm_resource_tally v0.3.0 (managed block — regenerated by `install`; edits below will be overwritten) -->
## LLM resource accounting
A git post-commit hook — and Claude Code hooks when wired — records the measured token and model
usage this repository costs. It is automatic bookkeeping and is not part of whatever task you were
given.

- Rows and mutable rollups are written under `.llm_resource_tally/local/`, which is gitignored.
  Recording therefore never modifies a tracked file and never blocks a commit, merge, rebase, or
  stash.
- Never hand-edit, hand-count, revert, or clean up ledger rows, and never let accounting block the
  repository work you were asked to do. Recording is best-effort by design.
- Treat totals as coverage of observed, allocated work rather than proof of complete history.
  Cross-repo/submodule duplicate guards are local to this user and machine, and
  `python3 .llm_resource_tally/tool doctor` can identify common gaps but cannot prove historical
  completeness.
- **Publish before you hand off substantial work.** Run
  `python3 .llm_resource_tally/tool publish`: it snapshots local rows onto the append-only ledger
  at `.llm_resource_tally/ledger/` and refreshes lifetime totals at
  `.llm_resource_tally/lifetime-totals.json`. Stage and commit what it writes in whichever
  repository owns those paths, preferably as its own commit so accounting stays out of unrelated
  diffs. This is routine — nobody should have to remember to ask you for it, and unpublished rows
  exist only on this machine.
- If accounting itself looks unhealthy, run `python3 .llm_resource_tally/tool doctor` — it checks
  hook wiring, backends, transcript retention, and ledger health, and names what to fix. Otherwise
  continue the repository task normally.
- After a fresh clone, run `python3 .llm_resource_tally/tool install` once to arm git-local hooks.
  It is offline and idempotent, and it reads the committed `.llm_resource_tally/settings.json`
  policy.
<!-- END llm_resource_tally -->
