"""Reloading a reader cannot mix a new app with old cached module imports."""

from urllib.parse import urljoin
import re

from starlette.testclient import TestClient

from ailectures.web import create_app


def test_updated_browser_build_has_distinct_urls_for_the_entire_module_graph(
    tmp_path, monkeypatch
):
    assets = tmp_path / "assets"
    assets.mkdir()
    (assets / "index.html").write_text(
        '<script type="module" src="/library-assets/app.mjs"></script>'
    )
    (assets / "app.mjs").write_text('import {oldId} from "./api.mjs";')
    (assets / "api.mjs").write_text("export const oldId = 1;")
    monkeypatch.setattr("ailectures.web.STATIC", assets)
    before = TestClient(create_app(tmp_path / "library"))
    old_document = before.get("/")
    old_entry = re.search(r'src="([^"]+)"', old_document.text)[1]
    old_api = urljoin(old_entry, "./api.mjs")
    assert before.get(old_api).text == "export const oldId = 1;"
    assert old_document.headers["cache-control"] == "no-cache"
    (assets / "app.mjs").write_text('import {randomId} from "./api.mjs";')
    (assets / "api.mjs").write_text("export const randomId = 2;")
    after = TestClient(create_app(tmp_path / "library"))
    entry = re.search(r'src="([^"]+)"', after.get("/").text)[1]
    api = urljoin(entry, "./api.mjs")
    assert entry != old_entry and api != old_api
    # A running build remains internally consistent even if source files change.
    assert before.get(old_api).text == "export const oldId = 1;"
    assert after.get(old_api).status_code == 404
    response = after.get(api)
    assert response.text == "export const randomId = 2;"
    assert "immutable" in response.headers["cache-control"]
    assert (
        after.get(api, headers={"If-None-Match": response.headers["etag"]}).status_code
        == 304
    )
    head = after.head(api)
    assert head.content == b"" and head.headers["content-length"] == str(
        len(response.content)
    )
    assert after.get("/library-assets/api.mjs").headers["cache-control"] == "no-cache"
    before.close()
    after.close()
