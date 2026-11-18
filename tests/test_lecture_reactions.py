"""Personal star/heart choices survive retries, transfer and listener merges."""
from copy import deepcopy
from uuid import uuid4

import pytest
from starlette.testclient import TestClient

from ailectures.core import Conflict
from ailectures.state import ListenerState
from ailectures.web import create_app


def event(field="rating", value=4, stamp="2026-11-18T01:00:00.000Z", **extra):
    return dict(lecture_id="music:001000", field=field, value=value, updated_at=stamp,
                update_id=str(uuid4()), revision="a"*64, **extra)


def test_independent_fields_retries_delayed_updates_and_clearing(tmp_path):
    state = ListenerState(tmp_path)
    who = state.create_profile("Listener")["id"]
    rating, heart = event(), event("favorite", True)
    assert state.save_reaction(who, rating) == rating
    assert state.save_reaction(who, rating) == rating
    state.save_reaction(who, heart)
    cleared = event(value=None, stamp="2026-11-18T01:01:00Z")
    accepted = state.save_reaction(who, cleared)
    assert state.save_reaction(who, rating) == accepted
    fields = state.reactions(who)[rating["lecture_id"]]
    assert fields["favorite"]["value"] is True
    assert fields["rating"]["value"] is None
    assert state.reaction_summary()[rating["lecture_id"]] == dict(ratings=0, average=None, favorites=1, distribution=[0]*5)
    with pytest.raises(Conflict):
        state.save_reaction(who, dict(cleared, value=5))
    assert state.reactions(who)[rating["lecture_id"]]["rating"] == accepted


@pytest.mark.parametrize("field,value", [("rating", 0), ("rating", 6), ("rating", True), ("rating", 4.0), ("rating", "4"), ("favorite", 1), ("favorite", None), ("anything", True)])
def test_invalid_choices_do_not_modify_state(tmp_path, field, value):
    state = ListenerState(tmp_path)
    who = state.create_profile("Listener")["id"]
    with pytest.raises(ValueError):
        state.save_reaction(who, event(field, value))
    assert state.reactions(who) == {}


def test_timestamps_are_normalized_and_order_independent(tmp_path):
    state = ListenerState(tmp_path)
    who = state.create_profile("Listener")["id"]
    early = event(value=2, stamp="2026-11-17T21:00:00-05:00")
    late = event(value=5, stamp="2026-11-18T02:01:00Z")
    state.save_reaction(who, late)
    assert state.save_reaction(who, early)["value"] == 5
    for stamp in ("nonsense", "2026-11-18T02:00:00", 123):
        with pytest.raises(ValueError):
            state.save_reaction(who, event(stamp=stamp))


def test_export_import_and_merge_preserve_fields_and_tombstones(tmp_path):
    state = ListenerState(tmp_path / "one")
    person = state.create_profile("Listener")
    state.save_reaction(person["id"], event())
    state.save_reaction(person["id"], event("favorite", True))
    old = state.export_listener(person["id"])
    state.save_reaction(person["id"], event("favorite", False, "2026-11-18T03:00:00Z"))
    new = state.export_listener(person["id"])
    restored = ListenerState(tmp_path / "two")
    restored.import_listener(new)
    restored.import_listener(old)
    assert restored.reactions(person["id"]) == state.reactions(person["id"])
    invalid = deepcopy(new)
    invalid["profile"]["id"] = "bad-import"
    invalid["reactions"]["music:001000"]["rating"]["value"] = 7
    with pytest.raises(ValueError):
        restored.import_listener(invalid)
    assert len(restored.profiles()) == 1
    duplicate = str(uuid4())
    with state.connect() as db:
        db.execute("INSERT INTO profiles VALUES (?,?)", (duplicate, "LISTENER"))
    state.save_reaction(duplicate, event(value=5, stamp="2026-11-18T04:00:00Z"))
    state.save_reaction(duplicate, event("favorite", True))
    state.merge_profiles(duplicate, person["id"])
    assert state.reactions(duplicate) == state.reactions(person["id"])
    fields = state.reactions(person["id"])["music:001000"]
    assert fields["rating"]["value"] == 5
    assert fields["favorite"]["value"] is False


def test_http_choices_are_personal_persistent_and_summarized_once(tmp_path):
    app = create_app(tmp_path)
    with TestClient(app) as client:
        one = client.post("/api/listeners", json={"name":"One"}).json()["id"]
        two = client.post("/api/listeners", json={"name":"Two"}).json()["id"]
        url = f"/api/listeners/{one}/reactions"
        rating = event()
        for _ in range(2):
            assert client.post(url, json=rating).status_code == 200
        client.post(f"/api/listeners/{two}/reactions", json=event(value=2))
        client.post(url, json=event("favorite", True))
        assert client.get(url).json()["music:001000"]["rating"]["value"] == 4
        assert "favorite" not in client.get(f"/api/listeners/{two}/reactions").json()["music:001000"]
        assert client.get("/api/library/reactions").json()["music:001000"] == dict(ratings=2, average=3, favorites=1, distribution=[0,1,0,1,0])
        assert client.post(url, json=event(value=10)).status_code == 400
        assert client.post("/api/listeners/missing/reactions", json=rating).status_code == 404
    with TestClient(create_app(tmp_path)) as client:
        assert client.get(url).json()["music:001000"]["favorite"]["value"] is True
