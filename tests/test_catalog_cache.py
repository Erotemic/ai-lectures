"""Read-only catalog reuse keeps navigation cheap without delaying source updates."""

import json

from starlette.testclient import TestClient

from ailectures.library import Library
from ailectures.packs import PackStore, export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def repository(tmp_path):
    folder = tmp_path / "repo" / "content" / "music"
    folder.mkdir(parents=True)
    manuscript = folder / "001000-intervals.md"
    manuscript.write_text(
        "# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\nHear an octave.\n<!-- END SPOKEN LECTURE -->\n"
    )
    (folder / "track.json").write_text(
        json.dumps(
            dict(
                id="music",
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
    assert (
        library.snapshot(copy=False)["lectures"]["music:001000"]["title"]
        != "Local caller change"
    )
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
