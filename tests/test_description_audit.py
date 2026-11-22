"""Focused contract tests for description audit provenance and prioritization."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import description_audit as audit


def fixture_repo(tmp_path):
    pack = tmp_path / "content" / "demo"
    (pack / "metadata").mkdir(parents=True)
    (pack / "track.json").write_text(json.dumps({"lectures": [
        {"id": "001000", "file": "001000-one.md", "title": "The Black Box Theorem"},
        {"id": "002000", "file": "002000-two.md", "title": "A Second Lecture"},
    ]}))
    for ident, desc in [("001000", "Proves a general theorem."),
                        ("002000", "Explains a second result with concrete examples.")]:
        (pack / "metadata" / f"{ident}.json").write_text(json.dumps({
            "lecture_id": ident, "description": desc, "other_field": 17,
        }))
    (pack / "001000-one.md").write_text(
        "<!-- BEGIN SPOKEN LECTURE -->\nThe theorem is discussed.\n"
        "<!-- END SPOKEN LECTURE -->\nBibliography might change."
    )
    (pack / "002000-two.md").write_text("Short explanation of a second result.")
    return tmp_path


def test_read_only_rank_and_recorded_full_review(tmp_path):
    repo = fixture_repo(tmp_path)
    before = audit.all_ranks(repo)
    assert len(before) == 2
    assert before[0]["review_state"] == "never_recorded"
    assert not (repo / "reviews").exists()
    rec = audit.record_audit(repo, "demo:001000", "model", "GPT-6",
                             "full_manuscript", "clean", "Read full text")
    assert rec["reviewer"]["model"] == "GPT-6"
    after = audit.all_ranks(repo)
    first = next(r for r in after if r["lecture"] == "demo:001000")
    assert first["review_state"] == "fully_reviewed"
    assert first["last_full_audit_model"] == "GPT-6"
    assert first["last_audit_depth"] == "full_manuscript"
    assert first["priority_points"] < next(r for r in after if r["lecture"] == "demo:002000")["priority_points"]


def test_description_or_spoken_change_stales_receipt(tmp_path):
    repo = fixture_repo(tmp_path)
    audit.record_audit(repo, "demo:001000", "model", "GPT-6", "full_manuscript", "clean", "Reviewed")
    # A companion-only change does not invalidate a spoken-description review.
    lecture = repo / "content/demo/001000-one.md"
    lecture.write_text(lecture.read_text() + "\nExtra bibliography")
    assert audit.all_ranks(repo)[1]["review_state"] == "fully_reviewed"
    sidecar = repo / "content/demo/metadata/001000.json"
    data = json.loads(sidecar.read_text())
    data["description"] += " Additional claim."
    sidecar.write_text(json.dumps(data))
    assert next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")["review_state"] == "stale"
    data["description"] = "Proves a general theorem."
    sidecar.write_text(json.dumps(data))
    lecture.write_text(lecture.read_text().replace("The theorem is discussed.", "The proof is discussed."))
    assert next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")["review_state"] == "stale"


def test_automated_cannot_certify_semantics(tmp_path):
    repo = fixture_repo(tmp_path)
    import pytest
    with pytest.raises(ValueError, match="cannot certify"):
        audit.record_audit(repo, "demo:001000", "tool", "regular-expression",
                           "automated", "clean", "")
    audit.record_audit(repo, "demo:001000", "tool", "regular-expression",
                       "automated", "screened", "Only structural cues")
    assert next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")["review_state"] == "automated_screen_only"


def test_targeted_review_does_not_erase_full_receipt(tmp_path):
    repo = fixture_repo(tmp_path)
    audit.record_audit(repo, "demo:001000", "model", "GPT-6", "full_manuscript", "clean", "Read all")
    audit.record_audit(repo, "demo:001000", "model", "GPT-6", "excerpts", "clean", "Checked heading")
    row = next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")
    assert row["review_state"] == "fully_reviewed"
    assert row["last_audit_depth"] == "excerpts"
    assert row["last_full_audit_model"] == "GPT-6"


def test_followup_retained_until_recheck(tmp_path):
    repo = fixture_repo(tmp_path)
    audit.record_audit(repo, "demo:001000", "model", "GPT-6", "full_manuscript",
                       "needs_followup", "Must check claim")
    item = next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")
    assert item["review_state"] == "needs_followup"
    audit.record_audit(repo, "demo:001000", "model", "GPT-6", "full_manuscript", "clean", "Resolved")
    item = next(x for x in audit.all_ranks(repo) if x["lecture"] == "demo:001000")
    assert item["review_state"] == "fully_reviewed"
