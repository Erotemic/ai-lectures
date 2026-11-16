"""Household names select listeners; merging a duplicate retains their state."""

from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

from starlette.testclient import TestClient

from ailectures.state import ListenerState
from ailectures.web import create_app


def point(lecture, event, device):
    return dict(
        lecture_id=lecture,
        update_id=event,
        device_id=device,
        seconds=3,
        sequence=1,
        expected_version=0,
        completed=False,
    )


def test_concurrent_same_name_selects_one_listener(tmp_path):
    stores = [ListenerState(tmp_path), ListenerState(tmp_path)]
    with ThreadPoolExecutor(max_workers=2) as pool:
        people = list(
            pool.map(
                lambda pair: pair[0].create_profile(pair[1]),
                zip(stores, ["jon.crall", "  JON.CRALL  "]),
            )
        )
    assert people[0]["id"] == people[1]["id"]
    assert len(stores[0].profiles()) == 1


def test_merge_duplicate_keeps_progress_queue_events_and_device_alias(tmp_path):
    state = ListenerState(tmp_path)
    original = state.create_profile("Listener")
    duplicate = str(uuid4())
    with state.connect() as db:
        db.execute("INSERT INTO profiles VALUES (?,?)", (duplicate, "listener"))
    state.save_progress(
        original["id"], point("music:001000", "original-progress", "desktop")
    )
    state.save_progress(duplicate, point("stories:001000", "phone-progress", "phone"))
    state.edit_queue(
        original["id"],
        {"action": "add", "entry": {"id": "first", "lecture_id": "music:001000"}},
    )
    state.edit_queue(
        duplicate,
        {"action": "add", "entry": {"id": "second", "lecture_id": "stories:001000"}},
    )
    assert state.merge_profiles(duplicate, original["id"]) == original
    assert state.profiles() == [original]
    assert set(state.progress(original["id"])) == {"music:001000", "stories:001000"}
    assert state.progress(duplicate) == state.progress(original["id"])
    assert [entry["id"] for entry in state.queue(duplicate)] == ["first", "second"]
    assert state.create_profile("LISTENER") == original
    with state.connect() as db:
        assert db.execute("SELECT count(*) FROM progress_events").fetchone()[0] == 2
    replay = state.save_progress(
        duplicate, point("stories:001000", "phone-progress", "phone")
    )
    assert replay["profile_id"] == original["id"]
    current = state.progress(duplicate)["stories:001000"]
    update = dict(
        point("stories:001000", "after-merge", "phone"),
        sequence=2,
        expected_version=current["version"],
    )
    assert not state.save_progress(duplicate, update).get("conflict")
    assert state.merge_profiles(duplicate, original["id"]) == original


def test_http_same_name_returns_existing_profile_and_aliases(tmp_path):
    with TestClient(create_app(tmp_path)) as client:
        first = client.post("/api/listeners", json={"name": "Listener"}).json()
        again = client.post("/api/listeners", json={"name": "listener"}).json()
        assert first == again
        assert client.get("/api/listeners").json()["profiles"] == [first]


def test_duplicate_merge_retains_furthest_point_in_unchanged_speech(tmp_path):
    state = ListenerState(tmp_path)
    person = state.create_profile("Listener")
    other = str(uuid4())
    with state.connect() as db:
        db.execute("INSERT INTO profiles VALUES (?,?)", (other, "Listener"))
    first = dict(
        point("music:001000", "farther", "desktop"),
        spoken_sha256="f" * 64,
        anchor_word=100,
    )
    later = dict(
        point("music:001000", "new-start", "phone"),
        spoken_sha256="f" * 64,
        anchor_word=10,
    )
    state.save_progress(person["id"], first)
    state.save_progress(other, later)
    state.merge_profiles(other, person["id"])
    assert state.progress(person["id"])["music:001000"]["anchor_word"] == 100
    assert state.create_profile("Ｌｉｓｔｅｎｅｒ") == person
