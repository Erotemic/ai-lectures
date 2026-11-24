import json

from PIL import Image
from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.packs import export_release
from ailectures.visuals import inspect_image
from ailectures.web import create_app


def test_season_covers_and_inline_visuals_follow_sources_and_exports(tmp_path, monkeypatch):
    repository = tmp_path / "repository"
    track = repository / "content" / "stories"
    track.mkdir(parents=True)
    spoken = "The friends crossed the bridge.\n\nThey found the lantern."
    tracks = []
    for local_id in ["001000", "002000"]:
        manuscript = f"{local_id}-bridge.md"
        (track / manuscript).write_text(
            f"# Bridge\n<!-- BEGIN SPOKEN LECTURE -->\n{spoken}\n<!-- END SPOKEN LECTURE -->\n"
        )
        tracks.append({"id": local_id, "file": manuscript, "section": "lanterns"})
    (track / "track.json").write_text(json.dumps({"id": "stories", "lectures": tracks}))
    before = repository_track(track)
    (track / "visuals.json").write_text(json.dumps({
        "images": {
            "cover": {"path": "season/Pine Park.png", "alt": "A lantern at the park"},
            "map": {"path": "season/Map.png", "alt": "A map of the bridge"},
            "invalid": {"path": "../private.png", "alt": "Private illustration"},
        },
        "sections": {"lanterns": "cover"},
        "lectures": {
            "001000": {"inline": [
                {"image": "map", "after": "The friends crossed the bridge."},
                {"image": "invalid", "after": "They found the lantern."},
                {"image": "map", "after": "They never said this."},
            ]},
        },
    }))
    after = repository_track(track)
    first_id = "stories:001000"
    row = after["lectures"][first_id]
    assert row["spoken_sha256"] == before["lectures"][first_id]["spoken_sha256"]
    assert row["transcript"] == spoken
    assert len(row["visuals"]["inline"]) == 1
    assert row["visuals"]["inline"][0]["after_word"] == 5
    assert len(after["warnings"]) == 2

    external = tmp_path / "external"
    folder = external / "season"
    folder.mkdir(parents=True)
    png = folder / "Pine Park.png"
    Image.new("RGB", (1200, 600), "green").save(png)
    original = png.read_bytes()
    Image.new("RGB", (96, 64), "blue").save(folder / "Map.png")
    library = tmp_path / "library"
    app = create_app(library, repository=repository, visual_root=external)
    with TestClient(app) as client:
        response = client.get("/api/library/catalog")
        tag = response.headers["etag"]
        cover = response.json()["courses"][0]["section_visuals"]["lanterns"]
        first = client.get(f"/api/library/lectures/{first_id}").json()
        second = client.get("/api/library/lectures/stories:002000").json()
        assert cover == first["visuals"]["cover"] == second["visuals"]["cover"]
        assert "path" not in cover
        assert first["visuals"]["inline"][0]["after_word"] == 5
        display = client.get(cover["src"])
        assert display.headers["content-type"] == "image/webp"
        cached, = (library / "build-cache" / "visuals").glob("*.webp")
        with Image.open(cached) as image:
            assert image.size == (480, 240)
        assert client.get(cover["original"]).content == original == png.read_bytes()
        Image.new("RGB", (1200, 600), "red").save(png)
        changed = client.get("/api/library/catalog", headers={"If-None-Match": tag})
        assert changed.status_code == 200
        assert changed.headers["etag"] != tag
        assert client.get(cover["original"]).status_code == 404

    exported = tmp_path / "exported"
    export_release(after, exported)
    assert all(path.suffix == ".json" for path in exported.rglob("*") if path.is_file())
    monkeypatch.setattr("ailectures.visuals.image_libraries", lambda: None)
    inspect_image.cache_clear()
    portable = create_app(tmp_path / "portable", visual_root=external)
    portable.state.library.store.install(exported)
    with TestClient(portable) as client:
        figure = client.get(f"/api/library/lectures/{first_id}").json()["visuals"]["cover"]
        assert figure["src"] == figure["original"]
        assert "srcset" not in figure
        assert client.get(figure["original"]).content == png.read_bytes()
        png.unlink()
        assert client.get(f"/api/library/lectures/{first_id}").json()["visuals"]["cover"] is None
