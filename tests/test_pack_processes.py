"""Publication boundaries exercised with independent, killable OS processes."""

import json
import select
import subprocess
import sys

from ailectures.packs import PackStore, export_release
from test_content_packs import source_pack


def start(root, source, hook=""):
    code = (
        """
import json, sys
from ailectures.packs import PackStore
from ailectures.core import Conflict
store = PackStore(sys.argv[1])
"""
        + hook
        + """
print('ready', flush=True)
sys.stdin.read(1)
try:
    print(json.dumps(store.install(sys.argv[2])), flush=True)
except Conflict:
    print('conflict', flush=True)
"""
    )
    return subprocess.Popen(
        [sys.executable, "-c", code, str(root), str(source)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def line(child):
    assert select.select([child.stdout], [], [], 15)[0], "child publication timed out"
    return child.stdout.readline().strip()


def run_pair(root, paths):
    children = [start(root, path) for path in paths]
    try:
        for child in children:
            assert line(child) == "ready"
        for child in children:
            child.stdin.write("x")
            child.stdin.flush()
        results = [line(child) for child in children]
        for child in children:
            assert child.wait(timeout=15) == 0, child.stderr.read()
        return results
    finally:
        for child in children:
            if child.poll() is None:
                child.kill()
            child.communicate(timeout=15)


def test_independent_processes_merge_and_competing_revisions_conflict(tmp_path):
    root = tmp_path / "library"
    PackStore(root)
    paths = [tmp_path / "music", tmp_path / "stories"]
    for namespace, path in zip(["music", "stories"], paths):
        export_release(source_pack(namespace), path)
    results = run_pair(root, paths)
    assert all(result != "conflict" for result in results)
    store = PackStore(root)
    assert set(store.snapshot()["lectures"]) == {"music:001000", "stories:001000"}
    base = json.loads(results[0])["release"]
    revisions = [tmp_path / "a", tmp_path / "b"]
    for text, path in zip(["First revision.", "Second revision."], revisions):
        export_release(source_pack("music", text), path, parent=base)
    results = run_pair(root, revisions)
    assert results.count("conflict") == 1
    assert len(store.active()) == 2


def test_killed_activation_keeps_old_selection_and_complete_files_retry(tmp_path):
    root = tmp_path / "library"
    first = tmp_path / "first"
    export_release(source_pack(), first)
    store = PackStore(root)
    base = store.install(first)
    revision = tmp_path / "revision"
    updated = export_release(
        source_pack(text="A revised interval."), revision, parent=base["release"]
    )
    # compose runs after writing the new selection, inside its SQLite transaction.
    hook = """
def interrupted(rows):
    print('before-commit', flush=True)
    sys.stdin.read(1)
store.compose = interrupted
"""
    child = start(root, revision, hook)
    try:
        assert line(child) == "ready"
        child.stdin.write("x")
        child.stdin.flush()
        assert line(child) == "before-commit"
        # Another process can still read the prior committed catalog.
        assert PackStore(root).active()[0]["release"] == base["release"]
        child.kill()
        child.communicate(timeout=15)
        assert PackStore(root).active()[0]["release"] == base["release"]
        assert (
            root / "packs" / base["id"] / updated["release"] / "catalog.json"
        ).is_file()
        store.install(revision)
        assert store.active()[0]["release"] == updated["release"]
        assert (
            store.historical(base["release"], "music:001000")[0]["transcript"]
            != "A revised interval."
        )
    finally:
        if child.poll() is None:
            child.kill()
        child.communicate(timeout=15)
