from concurrent.futures import ThreadPoolExecutor

from starlette.testclient import TestClient

from ailectures.core import Conflict
from ailectures.state import ListenerState
from ailectures.web import create_app

import pytest


def test_independent_devices_edit_current_queue_without_losing_additions(tmp_path):
    state = ListenerState(tmp_path)
    profile = state.create_profile("Listener")["id"]
    other = state.create_profile("Other listener")["id"]
    entries = [dict(id=str(i), lecture_id=f"subject:{i:06}") for i in range(6)]

    # Each device opens its own connection. Both additions survive even though
    # they did not fetch a shared queue version before submitting their action.
    def add(entry):
        return ListenerState(tmp_path).edit_queue(
            profile, dict(action="add", entry=entry)
        )

    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(add, entries))
    assert {entry["id"] for entry in state.queue(profile)} == {
        entry["id"] for entry in entries
    }
    assert state.queue(other) == []
    before = state.queue(profile)
    add(entries[0])
    assert state.queue(profile) == before
    with pytest.raises(Conflict):
        add(dict(entries[0], lecture_id="another:000000"))
    state.edit_queue(profile, dict(action="move", id="5", before="0"))
    queue = state.queue(profile)
    assert queue.index(entries[5]) + 1 == queue.index(entries[0])
    state.edit_queue(profile, dict(action="remove", id="5"))
    assert entries[5] not in state.queue(profile)
    receiver = ListenerState(tmp_path / "receiver")
    document = state.export_listener(profile)
    receiver.import_listener(document)
    receiver.import_listener(document)
    assert receiver.queue(profile) == state.queue(profile)
    receiver.edit_queue(profile, dict(action="remove", id="0"))
    with pytest.raises(Conflict):
        receiver.import_listener(document)


def test_queue_api_keeps_uninstalled_lectures_and_needs_no_login(tmp_path):
    with TestClient(create_app(tmp_path)) as client:
        profile = client.post("/api/listeners", json={"name": "Listener"}).json()["id"]
        path = f"/api/listeners/{profile}/queue"
        assert client.get(path).json() == {"entries": []}
        entry = dict(
            id="queued", lecture_id="uninstalled:001000", course_id="uninstalled:main"
        )
        assert client.post(path, json=dict(action="add", entry=entry)).json() == {
            "entries": [entry]
        }
        assert client.get(f"/api/listeners/{profile}/export").json()["queue"] == [entry]
        assert client.get("/api/library/catalog").status_code == 200
