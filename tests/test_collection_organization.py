import json

from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.packs import export_release
from ailectures.web import create_app


def test_grouping_changes_do_not_change_content_or_speech_identity(tmp_path):
    folder = tmp_path / "content" / "independent-stories"
    folder.mkdir(parents=True)
    (folder / "001000-story.md").write_text(
        "# Story\n<!-- BEGIN SPOKEN LECTURE -->\nA little cloud settles down.\n<!-- END SPOKEN LECTURE -->"
    )
    plan = dict(
        id="independent-stories",
        title="Stories",
        category="Bedtime stories",
        audience="children",
        age_range_label="Ages 3–4",
        lectures=[dict(id="001000", file="001000-story.md")],
    )
    manifest = folder / "track.json"
    manifest.write_text(json.dumps(plan))
    first = repository_track(folder)
    before = first["lectures"]["independent-stories:001000"]
    plan.update(
        categories=["Stories", "Imagination"], audiences=["children", "families"]
    )
    manifest.write_text(json.dumps(plan))
    updated = repository_track(folder)
    row = updated["lectures"][before["id"]]
    assert row["revision"] == before["revision"]
    assert row["spoken_sha256"] == before["spoken_sha256"]
    assert updated["courses"]["independent-stories:main"]["categories"] == [
        "Stories",
        "Imagination",
    ]
    export_release(updated, tmp_path / "release")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "release")
    with TestClient(app) as client:
        snapshot = client.get("/api/library/catalog").json()
        assert snapshot["courses"][0]["audiences"] == ["children", "families"]
        assert snapshot["lectures"][0]["categories"] == ["Stories", "Imagination"]
        assert snapshot["courses"][0]["age_range_label"] == "Ages 3–4"
        assert client.get("/collections/independent-stories:main").status_code == 200
        assert client.get("/courses/independent-stories:main").status_code == 200


def test_unindexed_drafts_remain_browsable_outside_collection_order(tmp_path):
    folder = tmp_path / "content" / "analysis"
    folder.mkdir(parents=True)
    (folder / "track.json").write_text(
        json.dumps(dict(id="analysis", title="Analysis", lectures=[]))
    )
    (folder / "001000-draft.md").write_text(
        "# Draft\n<!-- BEGIN SPOKEN LECTURE -->\nAn unfinished example.\n<!-- END SPOKEN LECTURE -->"
    )
    with TestClient(create_app(tmp_path / "library", repository=tmp_path)) as client:
        snapshot = client.get("/api/library/catalog").json()
        assert snapshot["courses"][0]["lectures"] == []
        assert snapshot["lectures"][0]["categories"] == ["Mathematics"]
        assert snapshot["lectures"][0]["id"] == "analysis:001000"
