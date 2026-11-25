import json
from xml.etree import ElementTree

from PIL import Image
from starlette.testclient import TestClient

from ailectures.catalog import repository_track
from ailectures.packs import export_release
from ailectures.visuals import inspect_image
from ailectures.web import create_app
from test_content_packs import media_for


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


def test_inline_equation_keeps_existing_recording_and_survives_export(tmp_path):
    repository = tmp_path / "repository"
    track = repository / "content" / "math"
    track.mkdir(parents=True)
    (track / "track.json").write_text(json.dumps({"id": "math", "lectures": [{"id": "001000"}]}))
    spoken = "The angle is theta zero.\n\nNow apply the estimate."
    (track / "001000-angle.md").write_text(
        f"# An angle\n<!-- BEGIN SPOKEN LECTURE -->\n{spoken}\n<!-- END SPOKEN LECTURE -->\n"
    )
    before = repository_track(track)
    media = media_for(before, tmp_path)
    old_release = tmp_path / "before"
    export_release(before, old_release, media=[media])
    (track / "visuals.json").write_text(json.dumps({
        "equations": {
            "angle": {"mathml": "<math><msub><mi>Θ</mi><mn>0</mn></msub></math>"},
            "active": {"mathml": '<math><mi href="/elsewhere">R</mi></math>'},
        },
        "lectures": {"001000": {"inline": [
            {"equation": "angle", "after": "The angle is theta zero."},
            {"equation": "active", "after": "Now apply the estimate."},
        ]}},
    }))
    after = repository_track(track)
    assert any("Unsupported MathML" in warning for warning in after["warnings"])
    new_release = tmp_path / "after"
    export_release(after, new_release, media=[media])
    for current_repository, release in [(repository, old_release), (None, new_release)]:
        app = create_app(tmp_path / ("installed-" + release.name), repository=current_repository,
                         visual_root=tmp_path / "missing-images", playback_only=True)
        app.state.library.store.install(release)
        with TestClient(app) as client:
            endpoint = "/api/library/lectures/math:001000"
            row = client.get(endpoint).json()
            assert row["spoken_sha256"] == before["lectures"]["math:001000"]["spoken_sha256"]
            assert client.get(endpoint + "/transcript.txt").text == spoken
            recording, = row["recordings"]
            assert recording["id"] == media[1]["id"]
            assert recording["pages"] == [spoken]
            segment, = recording["segments"]
            assert client.get(segment["url"]).content.startswith(b"RIFF")
            placement, = row["visuals"]["inline"]
            assert placement["after_word"] == 5
            equation = ElementTree.fromstring(placement["figure"]["mathml"])
            assert equation.tag == "{http://www.w3.org/1998/Math/MathML}math"
            assert equation.attrib == {"display": "block"}
