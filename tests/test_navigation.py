"""Routes reuse content, survive export, and fail independently of manuscripts."""

import json
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from ailectures.catalog import RepositoryCatalog, repository_track
from ailectures.navigation import route_collections
from ailectures.packs import export_release, load_release
from ailectures.web import create_app
from test_content_packs import media_for, source_pack
from tools.audit_listening_routes import audit_repository


def source(tmp_path):
    folder = tmp_path / "content" / "sample"
    folder.mkdir(parents=True)
    entries = []
    for number in (1, 2, 3):
        key = f"{number:06}"
        filename = key + "-example.md"
        (folder / filename).write_text(
            f"# Example {number}\n<!-- BEGIN SPOKEN LECTURE -->\n"
            f"An example numbered {number}.\n<!-- END SPOKEN LECTURE -->\n"
        )
        entries.append(dict(id=key, file=filename))
    (folder / "track.json").write_text(
        json.dumps(
            dict(
                id="sample",
                title="Sample",
                categories=["Mathematics"],
                lectures=entries,
            )
        )
    )
    return folder


def navigation():
    return dict(
        default_collection="survey",
        collections=[
            dict(
                id="survey",
                title="Survey",
                role="main",
                chapters=[
                    dict(
                        title="First stop",
                        lectures=["000002", "000001"],
                        collection="study",
                    ),
                ],
                related_collections=["optional:survey"],
                preparation_collections=["study", "optional:survey"],
            ),
            dict(
                id="study",
                title="Study",
                parent="survey",
                lectures=["000001", "000002", "000003"],
            ),
        ],
    )


def test_ordered_routes_reuse_content_and_round_trip_without_the_repository(tmp_path):
    folder = source(tmp_path)
    original = repository_track(folder)
    (folder / "navigation.json").write_text(json.dumps(navigation()))
    pack = repository_track(folder)
    assert pack["lectures"] == original["lectures"]
    assert (
        pack["courses"]["sample:main"]["lectures"]
        == original["courses"]["sample:main"]["lectures"]
    )
    survey = pack["courses"]["sample:survey"]
    assert survey["lectures"] == ["sample:000002", "sample:000001"]
    assert survey["chapters"][0]["collection"] == "sample:study"
    assert pack["courses"]["sample:main"]["parent_id"] == survey["id"]
    assert survey["related_collections"] == ["optional:survey"]
    assert survey["preparation_collections"] == ["sample:study", "optional:survey"]
    export_release(pack, tmp_path / "release")
    assert load_release(tmp_path / "release")["catalog"]["courses"] == pack["courses"]
    app = create_app(tmp_path / "portable")
    app.state.library.store.install(tmp_path / "release")
    with TestClient(app) as client:
        catalog = client.get("/api/library/catalog").json()
        assert {c["id"] for c in catalog["courses"]} == set(pack["courses"])
        assert client.get("/collections/sample:survey").status_code == 200
        assert client.get("/courses/sample:main").status_code == 200


@pytest.mark.parametrize(
    "defect", ["duplicate", "unknown_lecture", "unknown_link", "cycle", "bad_json"]
)
def test_bad_route_updates_retain_routes_and_allow_new_speech(tmp_path, defect):
    folder = source(tmp_path)
    path = folder / "navigation.json"
    plan = navigation()
    path.write_text(json.dumps(plan))
    catalog = RepositoryCatalog(tmp_path)
    before = catalog.snapshot()["sample"]
    if defect == "duplicate":
        plan["collections"][0]["chapters"][0]["lectures"].append("000002")
    elif defect == "unknown_lecture":
        plan["collections"][1]["lectures"].append("999999")
    elif defect == "unknown_link":
        plan["collections"][0]["related_collections"].append("absent")
    elif defect == "cycle":
        plan["collections"][1]["parent"] = "study"
    path.write_text("{" if defect == "bad_json" else json.dumps(plan))
    manuscript = folder / "000001-example.md"
    manuscript.write_text(manuscript.read_text().replace("numbered 1", "revised today"))
    # The on-disk previous snapshot also protects a fresh server after a restart.
    restarted = RepositoryCatalog(tmp_path)
    after = restarted.snapshot()["sample"]
    assert after["courses"] == before["courses"]
    assert (
        after["lectures"]["sample:000001"]["spoken_sha256"]
        != before["lectures"]["sample:000001"]["spoken_sha256"]
    )
    assert any("navigation.json" in error for error in restarted.errors)


def test_navigation_only_refresh_and_removal(tmp_path):
    folder = source(tmp_path)
    catalog = RepositoryCatalog(tmp_path)
    original = catalog.snapshot()["sample"]
    path = folder / "navigation.json"
    path.write_text(json.dumps(navigation()))
    added = catalog.snapshot()["sample"]
    assert added["lectures"] == original["lectures"]
    assert len(added["courses"]) == 3
    path.unlink()
    removed = catalog.snapshot()["sample"]
    assert removed["courses"] == original["courses"]


def test_sessions_flatten_into_the_same_playback_route_and_export(tmp_path):
    folder = source(tmp_path)
    plan = navigation()
    chapter = plan["collections"][0]["chapters"][0]
    original_members = chapter.pop("lectures")
    chapter["sessions"] = [
        dict(title="A first session", lectures=original_members[:1]),
        dict(title="A second session", lectures=original_members[1:]),
    ]
    (folder / "navigation.json").write_text(json.dumps(plan))
    pack = repository_track(folder)
    survey = pack["courses"]["sample:survey"]
    assert survey["lectures"] == ["sample:" + key for key in original_members]
    assert survey["chapters"][0]["sessions"][1]["lectures"] == ["sample:000001"]
    export_release(pack, tmp_path / "release")
    assert (
        load_release(tmp_path / "release")["catalog"]["courses"][survey["id"]] == survey
    )
    chapter["sessions"][1]["lectures"] = original_members[:1]
    (folder / "navigation.json").write_text(json.dumps(plan))
    invalid = repository_track(folder, previous=pack)
    assert invalid["courses"] == pack["courses"]
    assert any("navigation.json" in warning for warning in invalid["warnings"])


def test_audit_distinguishes_optional_packs_from_broken_available_references(tmp_path):
    folder = source(tmp_path)
    plan = navigation()
    plan["collections"][0]["chapters"][0]["lectures"].append("optional:000001")
    (folder / "navigation.json").write_text(json.dumps(plan))
    report = audit_repository(tmp_path)
    assert not report["errors"]
    assert report["optional_unavailable_references"] == [
        "optional:000001",
        "optional:survey",
    ]
    assert report["inventory"][0]["unplaced"] == []
    installed = tmp_path / "content" / "optional"
    installed.mkdir()
    (installed / "track.json").write_text(
        json.dumps(dict(id="optional", title="Optional", lectures=[]))
    )
    report = audit_repository(tmp_path)
    assert not report["optional_unavailable_references"]
    assert len(report["errors"]) == 3
    assert report["audio_manuscripts"] == 3


def test_recordings_survive_route_and_section_changes(tmp_path):
    original = source_pack("sample", text="An example numbered 1.")
    media = media_for(original, tmp_path)
    folder = source(tmp_path / "repository")
    # Existing recordings are matched by canonical speech, not navigation.
    app = create_app(tmp_path / "reader", repository=tmp_path / "repository")
    pack = repository_track(folder)
    _, recording, files = media
    media = ("sample:000001", recording, files)
    export_release(pack, tmp_path / "matching", media=[media])
    app.state.library.store.install(tmp_path / "matching")
    with TestClient(app) as client:

        def row():
            return client.get("/api/library/lectures/sample:000001").json()

        before = row()
        assert before["recordings"]
        listener = client.post("/api/listeners", json={"name": "Listener"}).json()["id"]
        progress_url = f"/api/listeners/{listener}/progress"
        saved = client.post(
            progress_url,
            json=dict(
                lecture_id=before["id"],
                revision=before["revision"],
                spoken_sha256=before["spoken_sha256"],
                recording_id=before["recordings"][0]["id"],
                course_id="sample:main",
                update_id="before-routes",
                device_id="device",
                sequence=1,
                expected_version=0,
                seconds=0.5,
                anchor_word=2,
                completed=False,
            ),
        )
        assert saved.status_code == 200
        (folder / "navigation.json").write_text(json.dumps(navigation()))
        manifest = json.loads((folder / "track.json").read_text())
        manifest["lectures"][0]["section"] = "new-section"
        (folder / "track.json").write_text(json.dumps(manifest))
        after = row()
        assert after["spoken_sha256"] == before["spoken_sha256"]
        assert [r["id"] for r in after["recordings"]] == [
            r["id"] for r in before["recordings"]
        ]
        restored = client.get(progress_url).json()[before["id"]]
        assert restored["seconds"] == 0.5 and restored["anchor_word"] == 2
        assert restored["course_id"] == "sample:main"


def test_section_route_includes_future_manuscripts_without_navigation_edits(tmp_path):
    folder = source(tmp_path)
    manifest_path = folder / "track.json"
    manifest = json.loads(manifest_path.read_text())
    for entry in manifest["lectures"]:
        entry["section"] = "ongoing" if entry["id"] != "000003" else "other"
    manifest_path.write_text(json.dumps(manifest))
    plan = navigation()
    plan["collections"][1].pop("lectures")
    plan["collections"][1]["include_sections"] = ["ongoing"]
    (folder / "navigation.json").write_text(json.dumps(plan))
    before = repository_track(folder)
    assert before["courses"]["sample:study"]["lectures"] == [
        "sample:000001",
        "sample:000002",
    ]
    filename = "000004-continuation.md"
    (folder / filename).write_text(
        "<!-- BEGIN SPOKEN LECTURE -->\nA continuation.\n<!-- END SPOKEN LECTURE -->"
    )
    manifest["lectures"].append(dict(id="000004", file=filename, section="ongoing"))
    manifest_path.write_text(json.dumps(manifest))
    after = repository_track(folder, previous=before)
    assert after["courses"]["sample:study"]["lectures"] == [
        "sample:000001",
        "sample:000002",
        "sample:000004",
    ]
    assert before["lectures"]["sample:000001"] == after["lectures"]["sample:000001"]
    export_release(after, tmp_path / "release")
    assert load_release(tmp_path / "release")["catalog"]["courses"] == after["courses"]
    (folder / "navigation.json").write_text("{")
    retained = repository_track(folder, previous=before)
    assert retained["courses"]["sample:study"] == before["courses"]["sample:study"]
    assert "sample:000004" in retained["courses"]["sample:main"]["lectures"]


def test_authored_routes_cover_their_pack_and_resolve_collection_links():
    root = Path(__file__).resolve().parents[1]
    paths = [
        *root.glob("content/*/navigation.json"),
        *root.glob("draft-stages/tts-*/navigation.json"),
    ]
    courses = {}
    for path in paths:
        manifest = path.parent / "track.json"
        if manifest.exists():
            plan = json.loads(manifest.read_text())
        else:
            pack = repository_track(path.parent)
            plan = dict(
                id=pack["id"],
                title=pack["title"],
                lectures=[
                    dict(
                        id=key.split(":", 1)[1],
                        section=pack["lectures"][key]["section"],
                    )
                    for key in pack["courses"][pack["id"] + ":main"]["lectures"]
                ],
            )
        namespace = plan["id"]
        members = [namespace + ":" + row["id"] for row in plan["lectures"]]
        main = dict(id=namespace + ":main", title=plan["title"], lectures=members)
        diagnostics = []
        routes = route_collections(
            path,
            main,
            known=set(members),
            lecture_sections={
                namespace + ":" + entry["id"]: entry.get("section", "")
                for entry in plan["lectures"]
            },
            issue=diagnostics.append,
        )
        assert not diagnostics, diagnostics
        assert routes[main["id"]]["lectures"] == members
        covered = {
            key
            for route in routes.values()
            if route.get("role") != "archive"
            for key in route["lectures"]
        }
        assert set(members) <= covered
        courses.update(routes)
    # Existing root collections can also be the target of optional links.
    for path in [
        *root.glob("content/*/track.json"),
        *root.glob("draft-stages/tts-*/track.json"),
    ]:
        namespace = json.loads(path.read_text())["id"]
        courses.setdefault(namespace + ":main", {})
    for route in courses.values():
        targets = (
            route.get("related_collections", [])
            + route.get("preparation_collections", [])
            + [
                c["collection"]
                for c in route.get("chapters", [])
                if c.get("collection")
            ]
        )
        assert all(target in courses for target in targets)
