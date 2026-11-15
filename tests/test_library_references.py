import json

from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.core import lecture_revision
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def test_nested_evidence_references_survive_export_and_have_a_reading_page(tmp_path):
    directory = tmp_path / "content" / "subject"
    (directory / "metadata").mkdir(parents=True)
    (directory / "001000-lecture.md").write_text(
        "# Lecture\n<!-- BEGIN SPOKEN LECTURE -->\nAn explanation.\n<!-- END SPOKEN LECTURE -->"
    )
    (directory / "metadata" / "001000.json").write_text(
        json.dumps(
            {
                "evidence_claims": [
                    {"supports": [{"source_id": "primary", "location": "Chapter 2"}]}
                ]
            }
        )
    )
    (directory / "metadata" / "sources.json").write_text(
        json.dumps(
            {
                "sources": {
                    "primary": {
                        "title": "Primary text",
                        "url": "https://example.org/primary",
                        "license": "Public domain",
                    }
                }
            }
        )
    )
    pack = repository_track(directory)
    row = pack["lectures"]["subject:001000"]
    assert "primary" in row["sources"]
    export_release(pack, tmp_path / "export")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "export")
    with TestClient(app) as client:
        assert client.get("/references").status_code == 200
        indexed = client.get("/api/library/references").json()["items"]
        assert indexed[0]["source"] == row["sources"]["primary"]
        assert indexed[0]["used_by"][0]["id"] == row["id"]
        text = client.get("/api/library/references.txt").text
        assert "https://example.org/primary" in text and "Public domain" in text


def test_historical_references_keep_their_original_reading_notes(tmp_path):
    pack = source_pack()
    row = pack["lectures"]["music:001000"]
    row["sources"] = {
        "text": {"title": "Reading", "url": "https://example.org/reading"}
    }
    row["metadata"] = {
        "related_resources": [
            {"source_id": "text", "reason": "Compare these intervals."}
        ]
    }
    row["revision"] = lecture_revision(row)
    manifest = export_release(pack, tmp_path / "first")
    app = create_app(tmp_path / "library")
    app.state.library.store.install(tmp_path / "first")
    with TestClient(app) as client:
        historical = client.get("/api/library/lectures/music:001000").json()
        updated = source_pack()
        export_release(updated, tmp_path / "second", parent=manifest["release"])
        app.state.library.store.install(tmp_path / "second")
        assert client.get("/api/library/references").json()["items"] == []
        old = client.get(
            "/api/library/references",
            params={
                "lecture_id": row["id"],
                "release": historical["origin"]["release"],
            },
        ).json()["items"]
        assert old[0]["reasons"] == ["Compare these intervals."]
