"""Stopping synthesis must not wait for unrelated probing or media publication."""

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import shutil
import threading
import time

from starlette.testclient import TestClient

from ailectures.web import create_app
from test_production_recovery import finished, setup_library, manager_for


def test_cancel_acknowledges_while_inventory_is_blocked(tmp_path, monkeypatch):
    text = (
        ("First passage has a clear example. " * 5).strip()
        + "\n\n"
        + ("Second passage gives another idea. " * 5).strip()
    )
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=text
    )
    sender_started, release_sender = threading.Event(), threading.Event()
    probe_started, release_probe = threading.Event(), threading.Event()

    def sender(text, settings, dest):
        if text.startswith("Second"):
            sender_started.set()
            release_sender.wait(8)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    request = manager.prepare("music:001000", "test")
    assert sender_started.wait(3)
    engine = manager._jobs[request["id"]]["engine"]
    original = engine.inventory

    def inventory(*args, **kwargs):
        probe_started.set()
        release_probe.wait(8)
        return original(*args, **kwargs)

    monkeypatch.setattr(engine, "inventory", inventory)
    pool = ThreadPoolExecutor(max_workers=2)
    tick = pool.submit(manager.tick)
    try:
        assert probe_started.wait(2)
        # No lifespan/background coordinator: the deliberately blocked tick is
        # the only coordinator, while DELETE runs through the actual HTTP route.
        client = TestClient(create_app(library.store.root, generation_manager=manager))
        response = pool.submit(
            client.delete, f"/api/library/production/jobs/{request['id']}"
        ).result(timeout=2)
        assert response.status_code == 200 and response.json()["state"] == "cancelled"
        assert not tick.done()
        assert manager.jobs.get(request["id"])["state"] == "cancelled"
        client.close()
    finally:
        release_probe.set()
        release_sender.set()
        tick.result(timeout=3)
        pool.shutdown(wait=True)
        manager.close()
    assert not manager.jobs.get(request["id"])["published"]
    assert manager.jobs.get(request["id"])["inventory"]["ready"] == 1


def test_cancel_during_staging_prevents_activation_and_rediscovery(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)

    def sender(text, settings, dest):
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    request = manager.prepare("music:001000", "test")
    live = manager._jobs[request["id"]]
    deadline = time.monotonic() + 3
    while live["engine"].inventory("000000", live["settings"])["ready"] != 1:
        assert time.monotonic() < deadline
        time.sleep(0.01)
    staged, release_stage = threading.Event(), threading.Event()
    original = library.store.stage_install

    @contextmanager
    def stage(*args, **kwargs):
        with original(*args, **kwargs) as prepared:
            staged.set()
            release_stage.wait(8)
            yield prepared

    monkeypatch.setattr(library.store, "stage_install", stage)
    pool = ThreadPoolExecutor(max_workers=2)
    tick = pool.submit(manager.tick)
    try:
        assert staged.wait(3)
        response = pool.submit(manager.cancel, request["id"]).result(timeout=2)
        assert response["state"] == "cancelled" and not tick.done()
        assert manager.jobs.get(request["id"])["inventory"]["ready"] == 1
    finally:
        release_stage.set()
        tick.result(timeout=3)
        pool.shutdown(wait=True)
        manager.close()
    assert manager.jobs.get(request["id"])["published"] is None
    library.store.reconcile(force=True)
    assert [row["pack_id"] for row in library.store.active()] == [pack["id"]]
    assert not list(library.store.root.glob(".install-*"))


def test_cancel_all_updates_the_queue_while_the_coordinator_is_busy(tmp_path, monkeypatch):
    library, _, _, audio, config = setup_library(tmp_path, monkeypatch)
    sender_started, release_sender = threading.Event(), threading.Event()
    probe_started, release_probe = threading.Event(), threading.Event()
    hold = threading.Event()

    def sender(text, settings, dest):
        if hold.is_set():
            sender_started.set()
            release_sender.wait(8)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender, max_active_jobs=1)
    client = TestClient(create_app(library.store.root, generation_manager=manager))
    try:
        ready = manager.prepare("music:001000", "test", speed=0.9)
        published = finished(manager, ready["id"])["published"]
        assert published
        hold.set()
        running = manager.prepare("music:001000", "test")
        assert sender_started.wait(3)
        queued = manager.prepare("music:001000", "test", speed=1.2)
        assert queued["state"] == "queued"
        engine = manager._jobs[running["id"]]["engine"]
        original_inventory = engine.inventory
        stop_requested = threading.Event()
        original_cancel = engine.cancel

        def inventory(*args):
            probe_started.set()
            release_probe.wait(8)
            return original_inventory(*args)

        def cancel(*args):
            stop_requested.set()
            return original_cancel(*args)

        monkeypatch.setattr(engine, "inventory", inventory)
        monkeypatch.setattr(engine, "cancel", cancel)
        with ThreadPoolExecutor(max_workers=2) as pool:
            tick = pool.submit(manager.tick)
            try:
                assert probe_started.wait(2)
                url = "/api/library/production/jobs"
                assert client.delete(url, headers={"Origin": "https://another.test"}).status_code == 403
                response = pool.submit(client.delete, url).result(timeout=2)
                assert response.status_code == 200 and response.json() == {"cancelled": 2}
                assert stop_requested.is_set() and not tick.done()
                assert client.delete(url).json() == {"cancelled": 0}
                states = {job["id"]: job["state"] for job in client.get(url).json()["jobs"]}
                assert states == {ready["id"]: "ready", running["id"]: "cancelled", queued["id"]: "cancelled"}
                assert manager.jobs.get(ready["id"])["published"] == published
            finally:
                release_probe.set()
                release_sender.set()
                tick.result(timeout=3)
    finally:
        client.close()
        release_sender.set()
        manager.close()


def test_cancel_all_during_worker_start_skips_synthesis(tmp_path, monkeypatch):
    library, _, _, _, config = setup_library(tmp_path, monkeypatch)
    opening, release_open = threading.Event(), threading.Event()
    started = threading.Event()

    def sender(*args):
        started.set()

    manager = manager_for(library, config, sender)
    open_job = manager._open

    def delayed_open(record):
        opening.set()
        release_open.wait(8)
        return open_job(record)

    monkeypatch.setattr(manager, "_open", delayed_open)
    try:
        with ThreadPoolExecutor(max_workers=2) as pool:
            preparing = pool.submit(manager.prepare, "music:001000", "test")
            try:
                assert opening.wait(3)
                assert pool.submit(manager.cancel_all).result(timeout=2) == {"cancelled": 1}
            finally:
                release_open.set()
            assert preparing.result(timeout=3)["state"] == "cancelled"
        assert not manager._jobs
        assert not started.is_set()
    finally:
        manager.close()
