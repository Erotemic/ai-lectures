"""Optional companion publication must preserve audio and exact historical files."""

import json
import shutil

from starlette.testclient import TestClient

from ailectures.catalog import RepositoryCatalog
from ailectures.core import lecture_revision
from ailectures.packs import PackStore, export_release
from ailectures.web import create_app
from test_content_packs import media_for, source_pack


def test_missing_companions_arrive_change_and_transfer_without_restart(tmp_path):
    repository = tmp_path / "repo"
    source = repository / "content" / "intervals"
    source.mkdir(parents=True)
    (source / "001000-listen.md").write_text(
        "# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\nCompare the pitches.\n<!-- END SPOKEN LECTURE -->\n"
    )
    (source / "metadata").mkdir()
    metadata = {
        "companions": [
            {
                "id": "score",
                "title": "Interval score",
                "role": "source",
                "path": "companions/score.json",
                "attribution": "Example author",
            },
            {"id": "bad", "path": "../outside.txt"},
        ]
    }
    (source / "metadata" / "001000.json").write_text(json.dumps(metadata))
    root = tmp_path / "live"
    with TestClient(create_app(root, repository=repository, interval=0.05)) as client:
        url = "/api/library/lectures/intervals:001000"
        initial = client.get(url).json()
        assert initial["transcript"] == "Compare the pitches."
        assert not initial.get("companions")
        assert client.get("/api/library/catalog").json()["errors"]
        (source / "companions").mkdir()
        score = source / "companions" / "score.json"
        score.write_text('{"notes": [60, 67]}')
        first = client.get(url).json()
        companion = first["companions"][0]
        assert client.get(companion["url"]).content == score.read_bytes()
        pack = RepositoryCatalog(repository).snapshot()["intervals"]
        export_release(pack, tmp_path / "release")
        score.write_text('{"notes": [60, 72]}')
        updated = client.get(url).json()
        assert updated["revision"] != first["revision"]
        assert updated["spoken_sha256"] == first["spoken_sha256"]
        assert client.get(companion["url"]).status_code == 409
        assert client.get(updated["companions"][0]["url"]).content == score.read_bytes()
        score.unlink()
        assert not client.get(url).json().get("companions")
        assert client.get(companion["url"]).status_code == 404
        assert client.get(url).json()["transcript"] == first["transcript"]
    transferred = tmp_path / "small-machine"
    store = PackStore(transferred)
    manifest = store.install(tmp_path / "release")
    shutil.rmtree(repository)
    shutil.rmtree(tmp_path / "release")
    with TestClient(create_app(transferred, interval=0.05)) as client:
        row = client.get(url).json()
        item = row["companions"][0]
        response = client.get(item["url"])
        assert response.content == b'{"notes": [60, 67]}'
        assert response.headers["content-disposition"].startswith("attachment")
        assert item["attribution"] == "Example author"
        store.remove("intervals")
        assert client.get(item["url"]).status_code == 200
        historical = client.get(
            url, params={"release": row["origin"]["release"]}
        ).json()
        assert historical["companions"][0]["url"] == item["url"]
        assert manifest["release"] in item["url"]


def test_invalid_optional_runtime_records_keep_audio_accessible(tmp_path):
    pack = source_pack()
    row = pack["lectures"]["music:001000"]
    row["companions"] = [{"id": "unfinished"}, None]
    row["revision"] = lecture_revision(row)
    export_release(pack, tmp_path / "release", media=[media_for(pack, tmp_path)])
    PackStore(tmp_path / "reader").install(tmp_path / "release")
    with TestClient(create_app(tmp_path / "reader")) as client:
        assert client.get("/api/library/catalog").status_code == 200
        detail = client.get("/api/library/lectures/music:001000").json()
        assert detail["companions"] == []
        assert (
            client.get(detail["recordings"][0]["segments"][0]["url"]).status_code == 200
        )
