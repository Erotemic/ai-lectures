"""Explicit listener knowledge survives retries, concurrent edits and transfer."""

from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from uuid import uuid4

import pytest

from ailectures.core import Conflict
from ailectures.state import ListenerState


def update(event="first", lecture="math:001000", status="known", revision=None):
    return dict(id=event, lecture_id=lecture, status=status, revision=revision)


def test_restart_retry_and_explicit_unknown_do_not_rewind(tmp_path):
    state = ListenerState(tmp_path)
    profile = state.create_profile("Listener")["id"]
    first = state.set_learning(profile, update(revision="a" * 64))
    cleared = state.set_learning(profile, update("clear", status="unknown"))
    state = ListenerState(tmp_path)
    assert state.set_learning(profile, update(revision="a" * 64)) == first
    assert state.learning(profile) == {"knowledge": {"math:001000": cleared}}
    assert cleared["status"] == "unknown" and cleared["revision"] is None
    assert cleared["update_id"] == "clear"
    assert cleared["updated_at"].endswith("+00:00")
    assert state.progress(profile) == {}


def test_independent_concurrent_updates_and_identity_isolation(tmp_path):
    state = ListenerState(tmp_path)
    person = state.create_profile("Listener")["id"]
    other = state.create_profile("Another listener")["id"]
    payloads = [update(str(i), f"uninstalled:{i:06}", "uncertain") for i in range(12)]

    def save(payload):
        return ListenerState(tmp_path).set_learning(person, payload)

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(save, payloads))
    assert state.learning(person)["knowledge"] == {
        row["lecture_id"]: row for row in results
    }
    assert state.learning(other) == {"knowledge": {}}
    with pytest.raises(Conflict):
        state.set_learning(other, payloads[0])
    own = state.set_learning(other, update("other-choice", status="unknown"))
    assert state.learning(other)["knowledge"] == {own["lecture_id"]: own}


@pytest.mark.parametrize(
    "change",
    [
        {"lecture_id": "math:002000"},
        {"status": "unknown"},
        {"revision": "b" * 64},
    ],
)
def test_conflicting_event_reuse_is_rejected(tmp_path, change):
    state = ListenerState(tmp_path)
    profile = state.create_profile("Listener")["id"]
    first = state.set_learning(profile, update())
    with pytest.raises(Conflict):
        state.set_learning(profile, dict(update(), **change))
    assert state.learning(profile)["knowledge"]["math:001000"] == first


@pytest.mark.parametrize(
    "change",
    [
        {"id": ""},
        {"id": 1},
        {"lecture_id": "unqualified"},
        {"status": "mastered"},
        {"status": []},
        {"revision": "short"},
        {"revision": True},
    ],
)
def test_invalid_update_is_rejected(tmp_path, change):
    state = ListenerState(tmp_path)
    profile = state.create_profile("Listener")["id"]
    with pytest.raises(ValueError):
        state.set_learning(profile, dict(update(), **change))
    assert state.learning(profile) == {"knowledge": {}}


def test_unknown_profile_and_missing_fields_are_rejected(tmp_path):
    state = ListenerState(tmp_path)
    with pytest.raises(KeyError):
        state.set_learning("absent", update())
    with pytest.raises(KeyError):
        state.learning("absent")
    with pytest.raises(ValueError):
        state.learning(12)
    profile = state.create_profile("Listener")["id"]
    with pytest.raises(ValueError):
        state.set_learning(profile, {"id": "missing"})


def test_playback_completion_does_not_assign_knowledge(tmp_path):
    state = ListenerState(tmp_path)
    profile = state.create_profile("Listener")["id"]
    state.save_progress(
        profile,
        dict(
            update_id="finished",
            lecture_id="math:001000",
            device_id="phone",
            sequence=1,
            expected_version=0,
            seconds=120,
            completed=True,
        ),
    )
    assert state.learning(profile) == {"knowledge": {}}
    uncertain = state.set_learning(profile, update(status="uncertain"))
    state.save_progress(
        profile,
        dict(
            update_id="finished-again",
            lecture_id="math:001000",
            device_id="phone",
            sequence=2,
            expected_version=1,
            seconds=120,
            completed=True,
        ),
    )
    assert state.learning(profile)["knowledge"]["math:001000"] == uncertain


def test_transfer_keeps_old_receipts_and_merges_choices_per_lecture(tmp_path):
    source = ListenerState(tmp_path / "source")
    person = source.create_profile("Listener")
    old = source.set_learning(person["id"], update())
    cleared = source.set_learning(person["id"], update("clear", status="unknown"))
    document = source.export_listener(person["id"])
    unchanged = deepcopy(document)
    receiver = ListenerState(tmp_path / "receiver")
    assert receiver.import_listener(document) == person
    assert receiver.import_listener(document) == person
    assert document == unchanged
    assert receiver.learning(person["id"]) == source.learning(person["id"])
    assert receiver.set_learning(person["id"], update()) == old
    assert receiver.learning(person["id"])["knowledge"]["math:001000"] == cleared
    later = receiver.set_learning(person["id"], update("newer", status="uncertain"))
    independent = receiver.set_learning(
        person["id"], update("independent", "math:002000")
    )
    receiver.import_listener(document)
    assert receiver.learning(person["id"])["knowledge"] == {
        "math:001000": later,
        "math:002000": independent,
    }
    # Destination edits also transfer back without a whole-state replacement.
    source.import_listener(receiver.export_listener(person["id"]))
    assert source.learning(person["id"]) == receiver.learning(person["id"])


def test_transfer_ties_are_deterministic_and_knowledge_only_exports_work(tmp_path):
    state = ListenerState(tmp_path)
    person = state.create_profile("Listener")
    document = dict(schema_version=1, profile=person, progress={}, knowledge={})
    stamp = "2026-01-01T00:00:00+00:00"
    known = dict(
        lecture_id="math:001000",
        status="known",
        revision=None,
        updated_at=stamp,
        update_id="a",
    )
    unknown = dict(known, status="unknown", update_id="z")
    for record in (unknown, known):
        document["knowledge"] = {record["lecture_id"]: record}
        state.import_listener(document)
    assert state.learning(person["id"])["knowledge"]["math:001000"] == unknown
    assert state.set_learning(person["id"], update("a")) == known


def test_old_listener_documents_remain_supported(tmp_path):
    state = ListenerState(tmp_path)
    person = dict(id="legacy-listener", name="Listener")
    document = dict(schema_version=1, profile=person, progress={})
    assert state.import_listener(document) == person
    assert state.learning(person["id"]) == {"knowledge": {}}
    state.set_learning(person["id"], update())
    state.import_listener(document)
    assert state.learning(person["id"])["knowledge"]["math:001000"]["status"] == "known"


def test_new_explicit_choice_survives_equal_or_older_clock_reading(
    tmp_path, monkeypatch
):
    monkeypatch.setattr("ailectures.state.utcnow", lambda: "2026-01-01T00:00:00+00:00")
    state = ListenerState(tmp_path / "source")
    person = state.create_profile("Listener")
    first = state.set_learning(person["id"], update("z"))
    cleared = state.set_learning(person["id"], update("a", status="unknown"))
    assert cleared["updated_at"] > first["updated_at"]
    receiver = ListenerState(tmp_path / "receiver")
    receiver.import_listener(state.export_listener(person["id"]))
    assert receiver.learning(person["id"]) == state.learning(person["id"])
    # The receiving clock may lag the transfer's most recent receipt.
    next_choice = receiver.set_learning(person["id"], update("b", status="uncertain"))
    assert next_choice["updated_at"] > cleared["updated_at"]
    receiver.import_listener(state.export_listener(person["id"]))
    assert receiver.learning(person["id"])["knowledge"]["math:001000"] == next_choice


def test_named_merge_and_transferred_alias_keep_retry_identity(tmp_path):
    state = ListenerState(tmp_path / "source")
    person = state.create_profile("Listener")
    duplicate = str(uuid4())
    with state.connect() as db:
        db.execute("INSERT INTO profiles VALUES (?,?)", (duplicate, "LISTENER"))
    first = state.set_learning(duplicate, update())
    old_export = state.export_listener(duplicate)
    last = state.set_learning(person["id"], update("clear", status="unknown"))
    independent = state.set_learning(duplicate, update("another", "math:002000"))
    state.merge_profiles(duplicate, person["id"])
    assert state.learning(duplicate)["knowledge"] == {
        "math:001000": last,
        "math:002000": independent,
    }
    assert state.set_learning(duplicate, update()) == first
    # Importing a pre-merge device export must not recreate the removed profile.
    assert state.import_listener(old_export) == person
    assert state.profiles() == [person]
    receiver = ListenerState(tmp_path / "receiver")
    document = state.export_listener(duplicate)
    assert document["profile_aliases"] == [duplicate]
    receiver.import_listener(document)
    assert receiver.resolve_profile(duplicate) == person["id"]
    assert receiver.set_learning(duplicate, update()) == first
    assert receiver.learning(duplicate) == state.learning(person["id"])


def test_import_conflicts_roll_back_all_learning_and_alias_changes(tmp_path):
    state = ListenerState(tmp_path)
    person = state.create_profile("Listener")
    first = state.set_learning(person["id"], update())
    document = state.export_listener(person["id"])
    conflict = dict(first, status="unknown")
    another = dict(first, update_id="new", lecture_id="math:002000")
    document["knowledge_events"] = [another, conflict]
    document["knowledge"] = {}
    document["profile_aliases"] = ["new-alias"]
    with pytest.raises(Conflict):
        state.import_listener(document)
    assert state.aliases() == {}
    assert state.learning(person["id"])["knowledge"] == {"math:001000": first}
    assert len(state.export_listener(person["id"])["knowledge_events"]) == 1


def test_import_cannot_claim_another_listener_or_event(tmp_path):
    state = ListenerState(tmp_path)
    person = state.create_profile("Listener")
    other = state.create_profile("Other")
    state.set_learning(person["id"], update())
    document = state.export_listener(person["id"])
    document["profile"] = other
    with pytest.raises(Conflict):
        state.import_listener(document)
    assert state.learning(other["id"]) == {"knowledge": {}}
    document["profile"] = person
    document["profile_aliases"] = [other["id"]]
    with pytest.raises(Conflict):
        state.import_listener(document)
    assert state.resolve_profile(other["id"]) == other["id"]


@pytest.mark.parametrize(
    "change",
    [
        {"updated_at": "not-a-date"},
        {"updated_at": "2026-01-01T00:00:00"},
        {"status": "mastered"},
        {"revision": "bad"},
        {"lecture_id": "math:002000"},
    ],
)
def test_invalid_transfer_record_is_rejected_without_mutation(tmp_path, change):
    source = ListenerState(tmp_path / "source")
    person = source.create_profile("Listener")
    source.set_learning(person["id"], update())
    document = source.export_listener(person["id"])
    document["knowledge"]["math:001000"].update(change)
    destination = ListenerState(tmp_path / "destination")
    with pytest.raises(ValueError):
        destination.import_listener(document)
    assert destination.profiles() == []
