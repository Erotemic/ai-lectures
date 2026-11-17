"""Read-only catalog reuse keeps navigation cheap without delaying source updates."""

import json
from pathlib import Path

from starlette.testclient import TestClient

from ailectures.catalog import RepositoryCatalog
from ailectures.core import digest
from ailectures.library import Library
from ailectures.packs import PackStore, export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def repository(tmp_path, namespace="music"):
    folder = tmp_path / "repo" / "content" / namespace
    folder.mkdir(parents=True)
    manuscript = folder / "001000-intervals.md"
    manuscript.write_text(
        "# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\nHear an octave.\n<!-- END SPOKEN LECTURE -->\n"
    )
    (folder / "track.json").write_text(
        json.dumps(
            dict(
                id=namespace,
                title="Music",
                lectures=[dict(id="001000", file=manuscript.name)],
            )
        )
    )
    return folder.parent.parent, manuscript


def test_readonly_cache_refreshes_for_live_sources_and_other_pack_installers(tmp_path):
    repo, manuscript = repository(tmp_path)
    library = Library(tmp_path / "reader", repository=repo)
    first = library.snapshot(copy=False)
    assert library.snapshot(copy=False) is first
    writable = library.snapshot()
    writable["lectures"]["music:001000"]["title"] = "Local caller change"
    writable["lectures"]["music:001000"]["metadata"]["local"] = True
    assert (
        library.snapshot(copy=False)["lectures"]["music:001000"]["title"]
        != "Local caller change"
    )
    assert (
        "local"
        not in library.snapshot(copy=False)["lectures"]["music:001000"]["metadata"]
    )
    source_row = library.repository.snapshot(copy=False)["music"]["lectures"][
        "music:001000"
    ]
    assert "origin" not in source_row and source_row["recordings"] == []
    manuscript.write_text(manuscript.read_text().replace("octave", "fifth"))
    revised = library.snapshot(copy=False)
    assert revised is not first and revised["generation"] != first["generation"]
    assert "fifth" in revised["lectures"]["music:001000"]["transcript"]
    export_release(source_pack("stories"), tmp_path / "stories")
    PackStore(library.store.root).install(tmp_path / "stories")
    assert "stories:001000" in library.snapshot(copy=False)["lectures"]


def test_catalog_revalidation_and_one_snapshot_per_lecture_request(
    tmp_path, monkeypatch
):
    repo, manuscript = repository(tmp_path)
    app = create_app(tmp_path / "reader", repository=repo)
    with TestClient(app) as client:
        response = client.get("/api/library/catalog")
        tag = response.headers["etag"]
        cached = client.get("/api/library/catalog", headers={"If-None-Match": tag})
        assert cached.status_code == 304 and cached.content == b""
        original = app.state.library.snapshot
        calls = []

        def snapshot(**kwargs):
            calls.append(kwargs)
            return original(**kwargs)

        monkeypatch.setattr(app.state.library, "snapshot", snapshot)
        assert client.get("/api/library/lectures/music:001000").status_code == 200
        assert len(calls) == 1
        manuscript.write_text(manuscript.read_text().replace("octave", "fifth"))
        current = client.get("/api/library/catalog", headers={"If-None-Match": tag})
        assert current.status_code == 200 and current.headers["etag"] != tag


def observe_parsing(monkeypatch):
    import ailectures.catalog as module

    original = module.repository_track
    calls = []

    def tracked(directory, **kwargs):
        calls.append(Path(directory).name)
        return original(directory, **kwargs)

    monkeypatch.setattr(module, "repository_track", tracked)
    return calls


def test_only_changed_packs_are_parsed_and_unchanged_restart_reuses_cache(
    tmp_path, monkeypatch
):
    repo, manuscript = repository(tmp_path)
    repository(tmp_path, "stories")
    calls = observe_parsing(monkeypatch)
    catalog = RepositoryCatalog(repo)
    first = catalog.snapshot(copy=False)
    assert calls == ["music", "stories"]
    calls.clear()
    assert catalog.snapshot(copy=False) is first
    manuscript.write_text(manuscript.read_text().replace("octave", "fifth"))
    changed = catalog.snapshot(copy=False)
    assert calls == ["music"]
    assert changed["stories"] is first["stories"]
    calls.clear()
    restarted = RepositoryCatalog(repo).snapshot(copy=False)
    assert calls == []
    assert restarted["music"]["lectures"] == changed["music"]["lectures"]
    manuscript.write_text(manuscript.read_text().replace("fifth", "third"))
    current = RepositoryCatalog(repo).snapshot(copy=False)
    assert calls == ["music"]
    assert "third" in current["music"]["lectures"]["music:001000"]["transcript"]


def test_restarted_cached_pack_retains_export_inputs_and_watches_companions(
    tmp_path, monkeypatch
):
    repo, manuscript = repository(tmp_path)
    folder = manuscript.parent
    (folder / "metadata").mkdir()
    (folder / "examples").mkdir()
    companion = folder / "example.txt"
    companion.write_text("Original example")
    (folder / "metadata/001000.json").write_text(
        json.dumps(
            {
                "companions": [{"id": "example", "path": companion.name}],
            }
        )
    )
    for path, text in (
        ("README.md", "Pack notes"),
        ("provenance.yaml", "author: recorded"),
        ("examples/example.json", '{"value": 1}'),
    ):
        (folder / path).write_text(text)
    first = RepositoryCatalog(repo).snapshot(copy=False)["music"]
    calls = observe_parsing(monkeypatch)
    catalog = RepositoryCatalog(repo)
    cached = catalog.snapshot(copy=False)["music"]
    assert calls == []
    assert cached["extra_files"] == first["extra_files"]
    export_release(cached, tmp_path / "export")
    assert (tmp_path / "export" / "example.txt").read_text() == "Original example"
    companion.write_text("Revised example")
    revised = catalog.snapshot(copy=False)["music"]
    assert calls == ["music"]
    assert (
        revised["lectures"]["music:001000"]["revision"]
        != cached["lectures"]["music:001000"]["revision"]
    )
    calls.clear()
    (folder / "provenance.yaml").write_text("author: updated")
    assert (
        b"updated"
        in catalog.snapshot(copy=False)["music"]["extra_files"]["provenance.yaml"]
    )
    assert calls == ["music"]


def test_cached_warnings_and_curriculum_changes_survive_without_reparsing(
    tmp_path, monkeypatch
):
    repo, manuscript = repository(tmp_path)
    repository(tmp_path, "stories")
    (manuscript.parent / "metadata").mkdir()
    (manuscript.parent / "metadata/001000.json").write_text(
        json.dumps(
            {
                "related_resources": [{"source_id": "missing-reference"}],
            }
        )
    )
    curriculum = repo / "curriculum"
    curriculum.mkdir()
    relations = curriculum / "relationships.json"
    edge = ["music:001000", "supports", "stories:001000", "original reason"]
    relations.write_text(json.dumps({"edges": [edge]}))
    first = RepositoryCatalog(repo)
    first.snapshot(copy=False)
    assert first.errors
    calls = observe_parsing(monkeypatch)
    restarted = RepositoryCatalog(repo)
    snapshot = restarted.snapshot(copy=False)
    assert restarted.errors == first.errors and calls == []
    assert len(snapshot["music"]["relationships"]) == 1
    edge[-1] = "revised reason"
    relations.write_text(json.dumps({"edges": [edge]}))
    changed = restarted.snapshot(copy=False)
    assert calls == []
    assert changed["music"]["relationships"][0]["why"] == "revised reason"


def test_changed_parser_implementation_invalidates_persisted_cache(
    tmp_path, monkeypatch
):
    repo, _ = repository(tmp_path)
    RepositoryCatalog(repo).snapshot(copy=False)
    cache = repo / ".content-state" / (digest("content/music") + ".json")
    saved = json.loads(cache.read_text())
    saved["implementation"] = "previous-parser"
    cache.write_text(json.dumps(saved))
    calls = observe_parsing(monkeypatch)
    assert RepositoryCatalog(repo).snapshot(copy=False)["music"]["lectures"]
    assert calls == ["music"]


def test_presentation_sources_also_reuse_cache_until_their_inputs_change(
    tmp_path, monkeypatch
):
    import ailectures.presentations as module

    folder = tmp_path / "lectures" / "intro"
    folder.mkdir(parents=True)
    (folder.parent / "index.yaml").write_text(
        "lectures:\n  intro:\n    title: Introduction\n    deck: intro\n"
    )
    (folder / "lecture.md").write_text("A presentation transcript")
    original = module.presentation_pack
    calls = []

    def tracked(root):
        calls.append(root)
        return original(root)

    monkeypatch.setattr(module, "presentation_pack", tracked)
    first = RepositoryCatalog(tmp_path).snapshot(copy=False)
    assert len(calls) == 1
    restarted = RepositoryCatalog(tmp_path)
    assert restarted.snapshot(copy=False)["g1"] == first["g1"]
    assert len(calls) == 1
    (folder / "lecture.md").write_text("A revised presentation transcript")
    assert restarted.snapshot(copy=False)["g1"] != first["g1"]
    assert len(calls) == 2
