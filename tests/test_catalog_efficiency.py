"""Check actual work avoided and history retained, without fragile timing limits."""
import json

from ailectures.core import canonical, digest
from ailectures.library import Library
from ailectures.organization import item_organization
from ailectures.packs import PackStore, export_release
from ailectures.source_snapshots import save_snapshot, historical_lecture, expand_snapshot
from test_content_packs import source_pack, media_for


def test_unchanged_selection_does_not_reload_active_catalog_json(tmp_path, monkeypatch):
    store = PackStore(tmp_path / "library")
    export_release(source_pack(), tmp_path / "release")
    store.install(tmp_path / "release")
    first = store.snapshot(copy=False)
    monkeypatch.setattr(store, "active", lambda *args: (_ for _ in ()).throw(AssertionError("unchanged snapshot reread catalog blobs")))
    assert store.snapshot(copy=False) is first


def test_restart_reuses_validation_but_rechecks_modified_media(tmp_path, monkeypatch):
    import ailectures.packs as module
    pack = source_pack()
    media = media_for(pack, tmp_path)
    manifest = export_release(pack, tmp_path / "release", media=[media])
    store = PackStore(tmp_path / "library", interval=0)
    store.install(tmp_path / "release")
    original = module.load_release
    calls = []
    def load(directory):
        calls.append(directory)
        return original(directory)
    monkeypatch.setattr(module, "load_release", load)
    restarted = PackStore(store.root, interval=0)
    assert restarted.snapshot()["lectures"] and not calls
    path, _ = restarted.media_file(manifest["release"], media[1]["id"], 0)
    path.write_bytes(path.read_bytes() + b"changed")
    assert restarted.snapshot()["lectures"]
    assert calls and restarted.errors


def test_historical_rows_are_shared_across_snapshots_and_legacy_history_survives(tmp_path):
    library = Library(tmp_path / "library")
    rows = {f"sample:{i}": dict(id=f"sample:{i}", transcript="Long standalone lecture. " * 3000) for i in range(5)}
    originals = []
    with library.store.connect() as db:
        for version in range(10):
            snapshot = {key: dict(row, origin={"release": digest(version), "source": True}) for key, row in rows.items()}
            originals.append(snapshot)
            save_snapshot(db, digest(version), snapshot)
        assert db.execute("SELECT count(*) FROM source_snapshot_rows").fetchone()[0] == len(rows)
        stored = db.execute("SELECT sum(length(document)) FROM source_snapshot_rows").fetchone()[0]
        indexes = db.execute("SELECT sum(length(catalog)) FROM source_snapshots").fetchone()[0]
        assert stored + indexes < sum(len(canonical(snapshot)) for snapshot in originals) / 5
        for version, snapshot in enumerate(originals):
            assert historical_lecture(db, digest(version), "sample:1") == snapshot["sample:1"]
            raw = db.execute("SELECT catalog FROM source_snapshots WHERE release=?", (digest(version),)).fetchone()[0]
            assert expand_snapshot(db, raw) == snapshot
        db.execute("INSERT INTO source_snapshots VALUES (?,?)", (digest("legacy"), json.dumps(originals[0])))
        assert historical_lecture(db, digest("legacy"), "sample:1") == originals[0]["sample:1"]


def test_indexed_collection_membership_preserves_categories_and_unindexed_fallback():
    collections = [dict(id="sample:main", lectures=["sample:one"], categories=["Science"], audiences=["adults"]),
                   dict(id="sample:archive", lectures=["sample:one"], role="archive", categories=["Other"])]
    memberships = {"sample:one": collections}
    namespaces = {"sample": collections}
    for key in ("sample:one", "sample:unindexed", "another:one"):
        row = dict(id=key, title="Example", metadata={})
        assert item_organization(row, collections) == item_organization(row, collections, memberships=memberships, namespaces=namespaces)


def test_shared_tag_indexes_are_reused_and_results_cannot_mutate_them(monkeypatch):
    import ailectures.tagging as tagging
    original = tagging.matching_paths(["DNA", "FFT", "Unknown topic"], tagging.TOPIC_PATHS)
    monkeypatch.setattr(tagging, "vocabulary_index", lambda *args: (_ for _ in ()).throw(AssertionError("rebuilt vocabulary for a lecture")))
    changed = tagging.matching_paths(["DNA", "FFT", "Unknown topic"], tagging.TOPIC_PATHS)
    assert changed == original
    changed[0].append("caller change")
    assert tagging.matching_paths(["DNA", "FFT", "Unknown topic"], tagging.TOPIC_PATHS) == original
    assert tagging.matching_paths(["Paris"], tagging.PLACE_PATHS, "Place: ")
