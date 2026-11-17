"""Discovery metadata survives portable releases without becoming prerequisites."""

import json

from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.graph import learning_map
from ailectures.organization import browse_sections, topic_tags
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def test_topic_tags_normalize_without_making_bad_optional_labels_fatal():
    assert topic_tags([" Analysis ", "analysis", None, "Linear algebra", "bad\nlabel", "x" * 81]) == ["Analysis", "Linear algebra"]
    assert topic_tags("Probability") == ["Probability"]
    assert topic_tags({"topic": "Probability"}) == []
    assert browse_sections([None, {"title": "Broken", "collections": [None, "../invalid"]}], "guide") == []


def test_topics_and_optional_directory_transfer_without_changing_speech(tmp_path):
    folder = tmp_path / "content" / "sample"
    folder.mkdir(parents=True)
    (folder / "001000-example.md").write_text("# Linear maps\n<!-- BEGIN SPOKEN LECTURE -->\nA map carries vectors to vectors.\n<!-- END SPOKEN LECTURE -->\n")
    manifest = dict(id="sample", title="Sample", categories=["Mathematics"], lectures=[dict(id="001000", file="001000-example.md")])
    track = folder / "track.json"
    track.write_text(json.dumps(manifest))
    first = repository_track(folder)
    manifest["tags"] = ["Linear algebra"]
    manifest["lectures"][0]["tags"] = ["Linear maps", "linear algebra"]
    track.write_text(json.dumps(manifest))
    (folder / "navigation.json").write_text(json.dumps(dict(default_collection="guide", collections=[
        dict(id="guide", title="Guide", role="hub", lectures=[], guide_for=["Mathematics"], browse_sections=[dict(title="Subjects", collections=["route", "optional:main"])]),
        dict(id="route", title="Route", parent="guide", lectures=["001000"]),
    ])))
    pack = repository_track(folder, strict=True)
    row = pack["lectures"]["sample:001000"]
    assert row["tags"] == ["Linear algebra", "Linear maps"]
    assert row["transcript"] == first["lectures"][row["id"]]["transcript"]
    assert row["spoken_sha256"] == first["lectures"][row["id"]]["spoken_sha256"]
    assert pack["courses"]["sample:main"]["lectures"] == first["courses"]["sample:main"]["lectures"]
    assert "browse_sections" not in pack["courses"]["sample:route"]
    assert "guide_for" not in pack["courses"]["sample:route"]
    export_release(pack, tmp_path / "release")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "release")
    with TestClient(app) as client:
        catalog = client.get("/api/library/catalog").json()
        assert catalog["lectures"][0]["tags"] == row["tags"]
        assert client.get("/api/library/lectures/" + row["id"]).json()["tags"] == row["tags"]
        guide = next(course for course in catalog["courses"] if course["id"] == "sample:guide")
        assert guide["browse_sections"][0]["collections"] == ["sample:route", "optional:main"]
        graph = client.get("/api/library/learning-map").json()
        assert graph["nodes"][row["id"]]["tags"] == row["tags"]
        links = [edge for edge in graph["relationships"] if edge["type"] == "directory_link"]
        assert len(links) == 2 and all(edge["category"] == "organization" for edge in links)
        assert not graph["nodes"]["collection:optional:main"]["available"]
        assert not any(edge["type"] == "hard_depends_on" for edge in graph["relationships"])


def test_tags_do_not_turn_into_learning_dependencies():
    graph = learning_map(dict(generation="test", courses={}, relationships=[], lectures={
        "first:one": dict(id="first:one", title="First", tags=["Spectral theory"]),
        "second:two": dict(id="second:two", title="Second", tags=["Spectral theory"]),
    }))
    assert graph["nodes"]["first:one"]["tags"] == ["Spectral theory"]
    assert graph["relationships"] == []


def test_bad_optional_directory_on_an_installed_pack_does_not_escape_normalization(tmp_path):
    pack = source_pack("example")
    pack["courses"]["example:main"].update(browse_sections="malformed", guide_for={"invalid": True}, tags={"invalid": True})
    export_release(pack, tmp_path / "release")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "release")
    with TestClient(app) as client:
        catalog = client.get("/api/library/catalog").json()
        course = catalog["courses"][0]
        assert "browse_sections" not in course and "guide_for" not in course
        assert course["tags"] == []
        assert catalog["lectures"][0]["id"] == "example:001000"
