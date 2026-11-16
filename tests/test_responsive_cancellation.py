"""Stopping synthesis must not wait for unrelated probing or media publication."""

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import shutil
import threading
import time

from starlette.testclient import TestClient

from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for


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
