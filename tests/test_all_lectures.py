"""The complete inventory is a native reader page, independent of presentation tools."""
from pathlib import Path
import shutil
import subprocess

import pytest
from starlette.testclient import TestClient
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack
from test_library_stats import Navigation


def test_flat_inventory_has_a_direct_route_and_navigation(tmp_path):
    def legacy():
        pytest.fail('The flat inventory must not initialize presentation tools')
    with TestClient(create_app(tmp_path/'library', legacy_factory=legacy)) as client:
        response = client.get('/lectures?q=memory&show=all')
        assert response.status_code == 200
        nav = Navigation()
        nav.feed(response.text)
        assert '/lectures' in nav.links
        assert client.get('/api/library/catalog').json()['lectures'] == []
        for asset in ('all-lectures.mjs', 'all-lectures-model.mjs'):
            assert client.get('/library-assets/'+asset).status_code == 200


def test_flat_inventory_model_and_return_path_behavior():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is required for browser model checks')
    subprocess.run([node, str(Path(__file__).with_suffix('.mjs'))], check=True)


def test_original_audio_bookmarks_open_the_native_library(tmp_path, monkeypatch):
    from dkvis.presentation.serve import create_app as presentation_app

    def no_old_audio(*args, **kwargs):
        pytest.fail("The presentation viewer must not initialize the old audio hub")

    monkeypatch.setattr("dkvis.presentation.audio_library.AudioLectureHub", no_old_audio)
    renders = tmp_path / "renders"
    renders.mkdir()
    calls = []

    def legacy():
        calls.append(True)
        return presentation_app(renders, audio_reader=False)

    app = create_app(tmp_path / "library", legacy_factory=legacy)
    export_release(source_pack(), tmp_path / "pack")
    app.state.library.store.install(tmp_path / "pack")
    with TestClient(app) as client:
        for bookmark, expected in {
            "/audio": "/",
            "/audio?track=music": "/collections/music%3Amain",
            "/audio?track=music&lecture=001000": "/lectures/music/001000?course=music%3Amain",
            "/audio?track=missing": "/",
        }.items():
            response = client.get(bookmark, follow_redirects=False)
            assert response.is_redirect and response.headers["location"] == expected
        assert client.post("/api/audio-generation/prepare", json={}).status_code == 404
        assert not calls
        assert client.get("/?deck=example", follow_redirects=False).headers["location"] == "/presentations?deck=example"
        assert client.get("/presentations").status_code == 200
        assert client.get("/learning-paths").status_code == 200
        assert calls == [True]
