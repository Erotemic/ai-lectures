"""Named legacy recordings can fill their holes without re-synthesizing audio."""

import shutil

from starlette.testclient import TestClient

from ailectures.core import digest
from ailectures.library import Library
from ailectures.packs import export_release, recording_id
from ailectures.web import create_app
from dkvis.presentation.audio_library import split_pages
from test_block_requests import TEXT
from test_content_packs import media_for
from test_production_recovery import setup_library, manager_for, finished


def imported_library(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=TEXT
    )
    key = "music:001000"
    rec, old_files = media_for(pack, tmp_path, variant="legacy-import")[1:]
    template = rec["segments"][0]
    rec.update(
        label="test",
        recipe=digest("old-import"),
        pages=split_pages(TEXT, max_chars=250),
        segments=[],
        complete=False,
    )
    files = {}
    for index in [0, 3]:
        path = f"artifacts/legacy-import/{index}.wav"
        rec["segments"].append(dict(template, index=index, path=path))
        files[path] = audio
    rec["id"] = recording_id(rec)
    export_release(
        pack, tmp_path / "legacy", parent=manifest["release"], media=[(key, rec, files)]
    )
    library.store.install(tmp_path / "legacy")
    return library, rec, audio, config


def test_recognized_import_fills_only_missing_blocks_and_transfers(
    tmp_path, monkeypatch
):
    library, old, audio, config = imported_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(text.split()[0])
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        with TestClient(
            create_app(library.store.root, interval=0.05, generation_manager=manager)
        ) as client:
            row = client.get("/api/library/lectures/music:001000").json()
            options = client.get(
                "/api/library/production/narrators?lecture_id=music:001000"
            ).json()
            assert len(options["choices"]) == 1
            choice = options["choices"][0]
            assert choice["profile"] == "test" and choice["recording_id"] == old["id"]
            assert (
                choice["base_recording_id"] == old["id"]
                and "recording:legacy-import" in choice["aliases"]
            )
            request = client.post(
                "/api/library/production/prepare",
                json=dict(
                    lecture_id=row["id"],
                    revision=row["revision"],
                    profile="test",
                    voice="af_alloy",
                    base_recording_id=old["id"],
                ),
            )
            assert request.status_code == 202, request.text
            result = finished(manager, request.json()["id"])
            assert result["state"] == "ready" and result["inventory"]["ready"] == 4
            assert calls == ["Second", "Third"]
            current = client.get("/api/library/lectures/music:001000").json()
            complete = next(r for r in current["recordings"] if r["complete"])
            assert complete["generator"]["inherited_recordings"][0]["id"] == old["id"]
            preview = client.get(
                f"/api/library/production/jobs/{result['id']}/playback"
            ).json()
            inherited = preview["recordings"][0]["segments"][0]
            assert "/api/library/media/" in inherited["url"]
            assert client.get(inherited["url"]).status_code == 200
            assert (
                client.post(
                    "/api/library/production/prepare",
                    json=dict(
                        lecture_id=row["id"],
                        profile="test",
                        voice="am_echo",
                        base_recording_id=old["id"],
                    ),
                ).status_code
                == 400
            )
            installed = next(
                release
                for release in library.store.active()
                if release["release"] == result["published"]
            )
            target = Library(tmp_path / "transferred")
            target.store.install(installed["directory"])
        with TestClient(create_app(target.store.root)) as receiver:
            moved = receiver.get("/api/library/lectures/music:001000").json()
            assert moved["recordings"][0]["complete"]
            for segment in moved["recordings"][0]["segments"]:
                assert receiver.get(segment["url"]).status_code == 200
    finally:
        manager.close()
