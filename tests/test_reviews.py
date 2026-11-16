"""Tests for the lecture review layer (tools/run_reviews.py).

Covers: the anchor verifier, revision hashing, plan states, the registry
state machine (dedup, regression re-open, stale sweep), the resume invariant
(a crashed mid-run is never re-billed), adjudication, and pack disjointness.
The reviewer is a scripted fake; no model is called.
"""

import importlib.util
import json

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("run_reviews", REPO / "tools" / "run_reviews.py")
rr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rr)

BEGIN = "<!-- BEGIN SPOKEN LECTURE -->"
END = "<!-- END SPOKEN LECTURE -->"

NARRATION_A_V1 = ("The city of Anu-ur was built in three thousand five hundred BCE.\n"
                  "Scholars still argue about its walls.")
NARRATION_A_STALE = ("The city of Anu-ur was built long before the common era.\n"
                     "Scholars still argue about its walls.")
NARRATION_B = "A calm story about rivers."


def _manuscript(title: str, spoken: str, companion: str = "") -> str:
    body = f"# {title}\n\n{BEGIN}\n{spoken}\n{END}\n"
    if companion:
        body += "\n" + companion + "\n"
    else:
        body += "\nCompanion note (not spoken).\n"
    return body


def _companion_with_wiki() -> str:
    return ("## Historical and textual companion (not spoken)\n\n"
            "### Further reading\n\n"
            "- Wikipedia: **City of Anu-ur** <https://en.wikipedia.org/wiki/City_of_Anu-ur>\n")


def _companion_without_wiki() -> str:
    return ("## Historical and textual companion (not spoken)\n\n"
            "### Further reading\n\n"
            "- A scholarly essay on rivers (publisher page).\n")


class FakeReviewer:
    """Scripted stand-in for the 27b reviewer. Counts calls per lecture."""

    def __init__(self, script: dict):
        self.script = script
        self.calls = {}
        self.payloads = {}

    def __call__(self, base, key, model, system, user, **kw):
        for lid, marker in self.script["_markers"].items():
            if marker in user:
                self.calls[lid] = self.calls.get(lid, 0) + 1
                self.payloads[lid] = user
                f = self.script[lid]
                content = json.dumps(f) if isinstance(f, list) else f
                return {"choices": [{"message": {"content": content}}],
                        "usage": {"total_tokens": 1}}
        raise AssertionError("unexpected reviewer call")


def make_repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    (root / "reviews" / "contract").mkdir(parents=True)
    (root / "reviews" / "registry").mkdir(parents=True)
    (root / "reviews" / "runs").mkdir(parents=True)
    (root / "reviews" / "contract" / "prompt-v1.md").write_text("You are the finder.\n",
                                                               encoding="utf-8")
    (root / "reviews" / "contract" / "prompt-v2.md").write_text(
        "You are the finder (v2, further-reading aware).\n", encoding="utf-8")
    (root / "reviews" / "contract" / "prompt-v2w.md").write_text(
        "You are the finder (v2w, wiki bulk).\n", encoding="utf-8")
    (root / "reviews" / "contract" / "prompt-v3.md").write_text(
        "You are the finder (v3).\n", encoding="utf-8")

    pack = root / "content" / "fixpack"
    (pack / "metadata").mkdir(parents=True)
    (pack / "track.json").write_text(json.dumps({
        "id": "fixpack", "title": "Fix Pack",
        "editorial_policy": "Source-grounded.",
        "lectures": [
            {"id": "0A", "title": "City", "file": "0A.md", "section": "s"},
            {"id": "0B", "title": "Rivers", "file": "0B.md", "section": "s"},
        ]}, indent=1), encoding="utf-8")
    (pack / "0A.md").write_text(_manuscript("City", NARRATION_A_V1,
                                            _companion_with_wiki()), encoding="utf-8")
    (pack / "0B.md").write_text(_manuscript("Rivers", NARRATION_B,
                                            _companion_without_wiki()), encoding="utf-8")
    (pack / "metadata" / "0A.json").write_text(json.dumps({
        "schema_version": 1, "lecture_id": "0A",
        "related_resources": [{"source_id": "s1", "reason": "main source"}],
        "historical_claims": [{"claim": "built in 3500 BCE",
                               "audit_status": "reference_recorded",
                               "source_limitations": []}],
    }), encoding="utf-8")
    (pack / "metadata" / "0B.json").write_text(json.dumps({
        "schema_version": 1, "lecture_id": "0B", "related_resources": []}), encoding="utf-8")
    (pack / "metadata" / "sources.json").write_text(json.dumps({
        "id": "fixpack",
        "sources": {
            "s1": {"title": "Source One", "kind": "book", "access": "owned",
                   "notes": "", "url": "https://example.org/s1"},
            "s2": {"title": "Source Two", "kind": "article", "access": "abstract",
                   "notes": "", "url": "https://example.org/s2"},
        }}, indent=1), encoding="utf-8")

    other = root / "draft-stages" / "otherpack"
    (other / "metadata").mkdir(parents=True)
    (other / "track.json").write_text(json.dumps({
        "id": "otherpack", "title": "Other", "lectures": [
            {"id": "0C", "title": "C", "file": "0C.md"}]}), encoding="utf-8")
    (other / "0C.md").write_text(_manuscript("C", "Something else entirely."), encoding="utf-8")
    return root


def script_for():
    return {
        "_markers": {"0A": "The city of Anu-ur", "0B": "calm story"},
        "0A": [
            {"category": "unverified_claim",
             "anchor": "built in three thousand five hundred BCE",
             "claim": "The city was built in 3500 BCE.",
             "detail": "No registered source covers the founding date.",
             "confidence": "high", "source_ids": ["s1"]},
            {"category": "glossed_step",
             "anchor": "a sentence that exists nowhere in the narration",
             "claim": "Unlocatable.", "detail": "Should be dropped.",
             "confidence": "low", "source_ids": []},
        ],
        "0B": [],
    }


def run_cli(root: Path, *args, fake=None):
    if fake is not None:
        orig = rr.call_reviewer
        rr.call_reviewer = fake
        try:
            code = rr_main(root, args)
        finally:
            rr.call_reviewer = orig
        return code
    return rr_main(root, args)


def rr_main(root: Path, args) -> int:
    old = rr.sys.argv
    rr.sys.argv = ["run_reviews", "--repo", str(root), *args]
    try:
        rr.main()
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 0
    finally:
        rr.sys.argv = old
    return 0


def snapshot(packs: list[Path]) -> dict:
    out = {}
    for pack in packs:
        for p in sorted(pack.rglob("*")):
            if p.is_file():
                out[str(p)] = (p.stat().st_mtime_ns, p.read_bytes())
    return out


# ---------------------------------------------------------------- tests

def test_anchor_verifier():
    narration = "The city of Anu-ur was built in\nthree thousand five hundred BCE."
    assert rr.verify_anchor("built in three thousand five hundred BCE", narration) == \
        "built in\nthree thousand five hundred BCE"
    assert rr.verify_anchor("built in three thousand six hundred BCE", narration) is None
    assert rr.verify_anchor("nonexistent words here at all", narration) is None
    assert rr.verify_anchor("", narration) is None


def test_extraction():
    text = "# T\n\n" + BEGIN + "\n**bold** words\n\n## Head\n{END}\n\nNotes".format(END=END)
    spoken = rr.extract_spoken(text)
    assert "bold words" in spoken and "Head" in spoken
    with pytest.raises(ValueError):
        rr.extract_spoken("no markers at all")
    with pytest.raises(ValueError):
        rr.extract_spoken(BEGIN + "a\n" + END + BEGIN + "b\n" + END)


def test_companion_extraction():
    text = _manuscript("T", "spoken words", "## Companion (not spoken)\n\nFurther reading here.")
    assert rr.extract_spoken(text).strip() == "spoken words"
    assert "Further reading here" in rr.extract_companion(text)
    assert rr.extract_companion("no markers at all") == ""


def test_payload_shows_companion_and_urls(tmp_path):
    root = make_repo(tmp_path)
    fake = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", fake=fake)
    p0a, p0b = fake.payloads["0A"], fake.payloads["0B"]
    assert "<<<COMPANION" in p0a and "City of Anu-ur" in p0a
    assert "https://en.wikipedia.org/wiki/City_of_Anu-ur" in p0a
    assert "https://example.org/s1" in p0a  # source urls exposed
    assert "<<<COMPANION" in p0b and "scholarly essay on rivers" in p0b
    assert "en.wikipedia.org" not in p0b  # the label may mention Wikipedia; no link may


def test_unit_revision_tracks_every_input(tmp_path):
    root = make_repo(tmp_path)
    track = rr.Track(root, root / "content" / "fixpack")
    base = rr.unit_revision(track, "0A")
    assert rr.unit_revision(track, "0A") == base
    (root / "content" / "fixpack" / "0A.md").write_bytes(b"tampered")
    assert rr.unit_revision(track, "0A") != base
    (root / "content" / "fixpack" / "0A.md").write_text(
        _manuscript("City", NARRATION_A_V1, _companion_with_wiki()), encoding="utf-8")
    assert rr.unit_revision(track, "0A") == base
    src = root / "content" / "fixpack" / "metadata" / "sources.json"
    src.write_text(src.read_text() + " ", encoding="utf-8")  # shared input moves every unit
    assert rr.unit_revision(track, "0A") != base


def test_plan_run_dedup_stale_regression(tmp_path):
    root = make_repo(tmp_path)
    packs = [root / "content" / "fixpack", root / "draft-stages" / "otherpack"]
    before = snapshot(packs)

    store = rr.Store(root)
    track = rr.Track(root, root / "content" / "fixpack")

    # Never reviewed.
    run_cli(root, "plan", "--track", "fixpack")
    cov = store.load_coverage("fixpack")
    assert cov == []

    fake = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", fake=fake)
    assert fake.calls == {"0A": 1, "0B": 1}

    # 0A: one real finding kept, one bogus anchor dropped. 0B: clean.
    rows = store.load_findings("fixpack")
    assert len(rows) == 1
    r0 = rows[0]
    assert r0["lecture_id"] == "0A" and r0["status"] == "open"
    assert r0["anchor"] == "built in three thousand five hundred BCE"
    assert r0["category"] == "unverified_claim" and r0["source_ids"] == ["s1"]
    assert r0["first_seen"]["run"] == r0["last_seen"]["run"]
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0A"]["outcome"] == "findings:1" and covs["0A"]["open"] == 1
    assert covs["0B"]["outcome"] == "clean" and covs["0B"]["adjudicated_at"]

    # The review run must not have touched either pack.
    assert snapshot(packs) == before

    # Re-run at the same revision: same identity dedups, no new row.
    fake2 = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--fresh", fake=fake2)
    rows = store.load_findings("fixpack")
    assert len(rows) == 1
    assert rows[0]["last_seen"]["run"] != rows[0]["first_seen"]["run"]
    assert rows[0]["first_seen"]["run"] == r0["first_seen"]["run"]

    # Adjudicate: confirm, then resolve; unit becomes adjudicated.
    fid = rows[0]["finding_id"]
    runid = rows[0]["last_seen"]["run"]
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", runid, "--unit", "0A",
            "--finding", fid, "--decision", "confirmed", "--note", "checked s1: no date",
            "--as", "test-adjudicator")
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "confirmed"
    assert rows[0]["adjudication"]["by"] == "test-adjudicator"
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", runid, "--unit", "0A",
            "--finding", fid, "--decision", "resolved", "--note", "reworded",
            "--as", "test-adjudicator")
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "resolved"
    assert rows[0]["resolution"]["revision"]
    assert [h["status"] for h in rows[0]["history"]] == ["open", "confirmed", "resolved"]
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0A"]["open"] == 0 and covs["0A"]["adjudicated_at"]

    # Regression: the text changes, the same claim comes back -> re-opened.
    (root / "content" / "fixpack" / "0A.md").write_text(
        _manuscript("City", NARRATION_A_V1 + "\nIt stands today."), encoding="utf-8")
    fake3 = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--fresh", fake=fake3)
    rows = store.load_findings("fixpack")
    assert len(rows) == 1
    assert rows[0]["status"] == "open"
    assert any("regression" in h.get("note", "") for h in rows[0]["history"])

    # Stale sweep: the sentence is reworded away -> the live finding goes stale.
    (root / "content" / "fixpack" / "0A.md").write_text(
        _manuscript("City", NARRATION_A_STALE), encoding="utf-8")
    fake4 = FakeReviewer({"_markers": fake3.script["_markers"], "0A": [], "0B": []})
    after_edits = snapshot(packs)
    run_cli(root, "run", "--track", "fixpack", "--fresh", fake=fake4)
    rows = store.load_findings("fixpack")
    assert len(rows) == 1 and rows[0]["status"] == "stale"
    assert rows[0]["history"][-1]["status"] == "stale"

    # Disjointness: no reviewer activity modified the packs (baseline: after
    # this test's own deliberate content edits).
    assert snapshot(packs) == after_edits


def test_bad_reviewer_output_is_nonfatal_and_retryable(tmp_path):
    root = make_repo(tmp_path)
    store = rr.Store(root)

    bad = FakeReviewer({"_markers": {"0A": "The city of Anu-ur", "0B": "calm story"},
                        "0A": "I have considered the narration carefully. It is fine.",
                        "0B": "[not really json] prose"})
    run_cli(root, "run", "--track", "fixpack", fake=bad)
    assert bad.calls == {"0A": 1, "0B": 1}
    run = rr.Run(store, [p.name for p in store.runs_dir.iterdir()][0])
    prog = run.progress()
    assert prog["stages"]["0A"]["stage"] == "review_failed"
    assert prog["stages"]["0A"]["error"]
    assert run.raw_path("0A").is_file()
    assert store.load_findings("fixpack") == []

    # A later invocation re-bills a failed unit and succeeds.
    good = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--resume", run.id, "--unit", "0A", "--unit", "0B",
            fake=good)
    assert good.calls == {"0A": 1, "0B": 1}
    rows = store.load_findings("fixpack")
    assert [r["lecture_id"] for r in rows] == ["0A"]
    prog = run.progress()
    assert prog["stages"]["0A"]["stage"] == "verified"
    assert prog["stages"]["0B"]["stage"] == "adjudicated"  # clean unit


def test_resume_is_not_rebilled(tmp_path):
    root = make_repo(tmp_path)
    store = rr.Store(root)

    fake = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--unit", "0A", "--one", fake=fake)
    assert fake.calls == {"0A": 1}
    run = rr.Run(store, [p.name for p in store.runs_dir.iterdir()][0])

    # Crash simulation: raw exists, but registry/coverage were never written and
    # the progress pointer says 'reviewed'.
    assert run.raw_path("0A").is_file()
    prog = run.progress()
    prog["stages"]["0A"]["stage"] = "reviewed"
    rr._write_json(run.progress_path, prog)
    store.save_findings("fixpack", [])
    store.save_coverage("fixpack", [])

    fake2 = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--resume", run.id, "--unit", "0A",
            fake=fake2)
    assert fake2.calls == {}, "resume must not re-bill a completed review"
    rows = store.load_findings("fixpack")
    assert len(rows) == 1 and rows[0]["status"] == "open"
    assert rr._read_jsonl(store.coverage_path("fixpack"))[0]["outcome"] == "findings:1"

    # Content moved mid-run: the old raw must be discarded and re-billed.
    (root / "content" / "fixpack" / "0A.md").write_text(
        _manuscript("City", NARRATION_A_STALE), encoding="utf-8")
    fake3 = FakeReviewer({"_markers": fake2.script["_markers"], "0A": [], "0B": []})
    run_cli(root, "run", "--track", "fixpack", "--resume", run.id, "--unit", "0A",
            fake=fake3)
    assert fake3.calls == {"0A": 1}
    assert store.load_findings("fixpack")[0]["status"] == "stale"


def test_disjointness_static(tmp_path):
    root = make_repo(tmp_path)
    code = run_cli(root, "verify")
    assert code == 0
    # A reviews/ dir inside a pack is a hard failure.
    (root / "content" / "fixpack" / "reviews").mkdir()
    assert run_cli(root, "verify") == 1


def test_dry_run_makes_no_calls_or_writes(tmp_path):
    root = make_repo(tmp_path)
    before = snapshot([root / "content" / "fixpack", root / "draft-stages" / "otherpack",
                       root / "reviews"])
    calls = []
    orig = rr.call_reviewer
    rr.call_reviewer = lambda *a, **k: calls.append(a)
    try:
        run_cli(root, "run", "--track", "fixpack", "--dry-run")
    finally:
        rr.call_reviewer = orig
    assert calls == []
    assert snapshot([root / "content" / "fixpack", root / "draft-stages" / "otherpack",
                     root / "reviews"]) == before


def test_missing_wiki_link_lifecycle(tmp_path):
    root = make_repo(tmp_path)
    store = rr.Store(root)
    script = {"_markers": {"0A": "The city of Anu-ur", "0B": "calm story"},
              "0A": [],
              "0B": [{"category": "missing_wiki_link",
                      "anchor": "A calm story about rivers.",
                      "claim": "The lecture is about rivers and their course.",
                      "detail": "No Wikipedia entry point; the article 'Rivers' is "
                                "substantial. Existing further reading: a scholarly essay.",
                      "confidence": "high", "source_ids": []}]}
    fake = FakeReviewer(script)
    run_cli(root, "run", "--track", "fixpack", fake=fake)
    rows = store.load_findings("fixpack")
    assert len(rows) == 1
    r0 = rows[0]
    assert r0["lecture_id"] == "0B" and r0["category"] == "missing_wiki_link"
    assert r0["status"] == "open" and r0["confidence"] == "high"
    assert r0["anchor"] == "A calm story about rivers."
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0B"]["outcome"] == "findings:1" and covs["0B"]["contract"] == "v2"
    assert covs["0A"]["outcome"] == "clean" and covs["0A"]["contract"] == "v2"

    run = rr.Run(store, [p.name for p in store.runs_dir.iterdir()][0])
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", run.id, "--unit", "0B",
            "--finding", r0["finding_id"], "--decision", "confirmed",
            "--note", "confirmed: no wiki entry point in the companion")
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "confirmed"
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", run.id, "--unit", "0B",
            "--finding", rows[0]["finding_id"], "--decision", "resolved",
            "--note", "wiki link added to further reading")
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "resolved"
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0B"]["open"] == 0 and covs["0B"]["adjudicated_at"]


def test_contract_recheck_flow(tmp_path):
    root = make_repo(tmp_path)
    store = rr.Store(root)
    fake = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--contract-version", "v2", fake=fake)
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0A"]["contract"] == "v2" and covs["0B"]["contract"] == "v2"

    # A contract bump makes every v2 unit recheckable, but only --recheck-contract
    # (or explicit --unit) bills the reviewer again.
    fake2 = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--contract-version", "v3",
            "--recheck-contract", "--fresh", fake=fake2)
    assert fake2.calls == {"0A": 1, "0B": 1}
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0A"]["contract"] == "v3" and covs["0B"]["contract"] == "v3"

    # Without the flag, a unit that is current, clean, and on the same contract
    # is not re-billed (only the still-active 0A is).
    fake3 = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", "--contract-version", "v3",
            "--fresh", fake=fake3)
    assert fake3.calls == {"0A": 1}, "current+clean unit must not be re-billed on contract bump"


def test_report_writes_for_run(tmp_path):
    root = make_repo(tmp_path)
    fake = FakeReviewer(script_for())
    run_cli(root, "run", "--track", "fixpack", fake=fake)
    run = rr.Run(rr.Store(root), [p.name for p in rr.Store(root).runs_dir.iterdir()][0])
    run_cli(root, "report", "--run", run.id)
    text = (run.dir / "report.md").read_text(encoding="utf-8")
    assert "findings:1" in text or "open (1)" in text
    assert "unverified_claim" in text and "3500 BCE" in text


def test_version_num():
    assert rr.version_num("v1") == 1
    assert rr.version_num("v2") == 2
    assert rr.version_num("v2w") == 2
    assert rr.version_num("v2.1") == 2
    assert rr.version_num("v3") == 3
    assert rr.version_num(None) == 0
    assert rr.version_num("") == 0


def script_wiki():
    return {"_markers": {"0A": "The city of Anu-ur", "0B": "calm story"},
            "0A": [],
            "0B": [{"category": "missing_wiki_link",
                    "anchor": "A calm story about rivers.",
                    "claim": "The lecture is centrally about rivers.",
                    "detail": "Further reading has only a scholarly essay; no "
                              "Wikipedia entry point; 'Rivers' would serve.",
                    "confidence": "high", "source_ids": [],
                    "wiki_articles": ["Rivers"]}]}


def test_wiki_bulk_pass(tmp_path):
    root = make_repo(tmp_path)
    store = rr.Store(root)

    # First bulk pass bills both units: 0A is already wiki-complete (clean),
    # 0B gets a finding with the structured article field.
    fake = FakeReviewer(script_wiki())
    run_cli(root, "run", "--track", "fixpack", "--prompt-variant", "wiki",
            "--fresh", fake=fake)
    assert fake.calls == {"0A": 1, "0B": 1}

    rows = store.load_findings("fixpack")
    assert len(rows) == 1
    r0 = rows[0]
    assert r0["lecture_id"] == "0B"
    assert r0["category"] == "missing_wiki_link"
    assert r0["wiki_articles"] == ["Rivers"]
    assert r0["status"] == "open"

    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0A"]["contract"] == "v2w" and covs["0A"]["outcome"] == "wiki:clean"
    assert covs["0B"]["contract"] == "v2w" and covs["0B"]["outcome"] == "wiki:1"

    # Second bulk pass: nothing to bill (live finding; clean-at-revision).
    fake2 = FakeReviewer(script_wiki())
    run_cli(root, "run", "--track", "fixpack", "--prompt-variant", "wiki",
            "--fresh", fake=fake2)
    assert fake2.calls == {}

    # Batch adjudication via decisions file, no --unit.
    run_id = sorted(p.name for p in store.runs_dir.iterdir())[-1]
    dfile = tmp_path / "d1.json"
    dfile.write_text(json.dumps({r0["finding_id"]: {"decision": "confirmed",
                                                    "note": "no wiki link in companion"}}))
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", run_id,
            "--decisions-file", str(dfile))
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "confirmed"

    dfile2 = tmp_path / "d2.json"
    dfile2.write_text(json.dumps({rows[0]["finding_id"]: {"decision": "resolved",
                                                         "note": "wiki link added"}}))
    run_cli(root, "adjudicate", "--track", "fixpack", "--run", run_id,
            "--decisions-file", str(dfile2))
    rows = store.load_findings("fixpack")
    assert rows[0]["status"] == "resolved"
    covs = {c["lecture_id"]: c for c in store.load_coverage("fixpack")}
    assert covs["0B"]["open"] == 0 and covs["0B"]["adjudicated_at"]

    # Resolved at the same revision: the bulk pass still skips it (no loop).
    fake3 = FakeReviewer(script_wiki())
    run_cli(root, "run", "--track", "fixpack", "--prompt-variant", "wiki",
            "--fresh", fake=fake3)
    assert fake3.calls == {}

    # A full-contract plan must not treat wiki-only (v2w) units as current.
    track = rr.Track(root, root / "content" / "fixpack")
    st = rr.unit_status(store, track, "0B", "v2")
    assert st["needed"] == "contract_kind"
    assert rr.needs_work(st)
