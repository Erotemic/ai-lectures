"""Explicit block selections share a voice queue without expanding to a lecture."""

from concurrent.futures import ThreadPoolExecutor
import shutil
import sqlite3
import time

from starlette.testclient import TestClient

from ailectures.core import digest
from ailectures.jobs import JobStore
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished

TEXT = "\n\n".join(
    ((name + " passage has a clear example. ") * 5).strip()
    for name in ("First", "Second", "Third", "Fourth")
)


def test_one_block_two_voices_extend_then_whole_lecture_reuses_cache(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=TEXT
    )
    calls = []

    def sender(text, settings, dest):
        calls.append((settings.voice, text.split()[0]))
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        with TestClient(
            create_app(library.store.root, interval=0.05, generation_manager=manager)
        ) as client:
            selected = dict(
                lecture_id="music:001000", profile="test", voice="af_alloy", blocks=[1]
            )
            request = client.post("/api/library/production/prepare", json=selected)
            assert request.status_code == 202, request.text
            one = finished(manager, request.json()["id"])
            assert calls == [("af_alloy", "Second")] and one["requested_blocks"] == [1]
            row = client.get("/api/library/lectures/music:001000").json()
            rec = row["recordings"][0]
            assert not rec["complete"] and [s["index"] for s in rec["segments"]] == [1]
            assert client.get(rec["segments"][0]["url"]).status_code == 200
            other = finished(
                manager,
                manager.prepare("music:001000", "test", voice="am_echo", blocks=[1])[
                    "id"
                ],
            )
            assert calls == [("af_alloy", "Second"), ("am_echo", "Second")]
            extended = finished(
                manager,
                manager.prepare(
                    "music:001000", "test", voice="af_alloy", blocks=[1, 2]
                )["id"],
            )
            assert extended["id"] == one["id"] and extended["requested_blocks"] == [
                1,
                2,
            ]
            assert calls[-1] == ("af_alloy", "Third") and len(calls) == 3
            full = finished(
                manager, manager.prepare("music:001000", "test", voice="af_alloy")["id"]
            )
            assert full["requested_blocks"] is None
            assert len(calls) == 5 and calls.count(("af_alloy", "Second")) == 1
            row = client.get("/api/library/lectures/music:001000").json()
            assert any(r["complete"] for r in row["recordings"])
            assert len(row["recordings"]) == 2
    finally:
        manager.close()


def test_scoped_restart_and_extension_preserve_published_blocks_without_build_cache(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=TEXT
    )
    calls = []

    def sender(text, settings, dest):
        calls.append(text.split()[0])
        shutil.copyfile(audio, dest)

    first = manager_for(library, config, sender)
    job = first.prepare("music:001000", "test", blocks=[2])
    live = first._jobs[job["id"]]
    deadline = time.monotonic() + 3
    while live["engine"].inventory("000000", live["settings"])["ready"] != 1:
        assert time.monotonic() < deadline
        time.sleep(0.01)
    first.close()  # Completed cache, still-unacknowledged intent.
    second = manager_for(library, config, sender)
    try:
        result = finished(second, job["id"])
        assert (
            result["state"] == "ready"
            and result["requested_blocks"] == [2]
            and calls == ["Third"]
        )
        # Emulate a transferred partial pack: its build cache is not portable.
        shutil.rmtree(library.store.root / "build-cache" / "speech")
        second.cancel(job["id"])  # A completed request remains ready.
        # Requesting another block uses the same queue and preserves the installed third block.
        result = finished(
            second, second.prepare("music:001000", "test", blocks=[1])["id"]
        )
        row = library.snapshot()["lectures"]["music:001000"]
        assert {s["index"] for s in row["recordings"][0]["segments"]} == {1, 2}
        assert calls == ["Third", "Second"]
    finally:
        second.close()


def test_scopes_merge_atomically_fence_publication_and_reset_after_cancel(tmp_path):
    store = JobStore(tmp_path)
    job = digest("shared")
    spec = {"source": "same"}
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(
            pool.map(lambda block: store.enqueue([(job, spec)], blocks=[block]), [1, 2])
        )
    assert store.get(job)["requested_blocks"] == [1, 2]
    store.claim("owner")
    called = []
    assert (
        store.publish(
            job,
            "owner",
            {"ready": 1},
            lambda: called.append(True),
            requested_blocks=[1],
        )
        is None
    )
    assert not called and store.get(job)["state"] == "running"
    store.cancel(job)
    store.enqueue([(job, spec)], blocks=[3])
    assert store.get(job)["requested_blocks"] == [3]
    store.cancel(job)
    store.enqueue([(job, spec)])
    assert store.get(job)["requested_blocks"] is None
    # An existing database migrates its original whole-lecture intent unchanged.
    with store.connect() as db:
        db.execute("ALTER TABLE jobs DROP COLUMN requested_blocks")
    assert JobStore(tmp_path).get(job)["requested_blocks"] is None


def test_block_requests_have_one_reserved_slot_behind_background_work(tmp_path):
    store = JobStore(tmp_path)
    whole = [digest("lecture-one"), digest("lecture-two")]
    store.enqueue([(key, {"lecture": key}) for key in whole])
    assert len(store.claim("background", limit=2)) == 2
    first, second = digest("first-block"), digest("second-block")
    store.enqueue([(first, {"lecture": "first"})], blocks=[1])
    store.enqueue([(second, {"lecture": "second"})], blocks=[1])
    assert [job["id"] for job in store.claim("foreground", limit=2)] == [first]
    assert store.claim("another-worker", limit=2) == []
    store.cancel(first)
    assert [job["id"] for job in store.claim("another-worker", limit=2)] == [second]
