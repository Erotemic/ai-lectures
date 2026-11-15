"""Agent source overlays are independent of runtime packaging and cannot clobber stale files."""

from pathlib import Path
import json
import shutil
import subprocess
from zipfile import ZipFile

import pytest

from tools.content_overlay import (
    SNAPSHOT,
    OVERLAY,
    OverlayConflict,
    apply,
    build,
    sha,
    snapshot,
)


def pack(root, namespace):
    directory = root / "content" / namespace
    (directory / "metadata").mkdir(parents=True)
    filename = "001000-introduction.md"
    (directory / filename).write_text(
        "# Introduction\n<!-- BEGIN SPOKEN LECTURE -->\nAn explanation with an example.\n<!-- END SPOKEN LECTURE -->\n"
    )
    (directory / "track.json").write_text(
        json.dumps(
            {
                "id": namespace,
                "title": namespace,
                "lectures": [{"id": "001000", "file": filename}],
            }
        )
    )
    (directory / "metadata/001000.json").write_text(
        json.dumps({"lecture_id": "001000", "transcript": filename})
    )
    return directory


def baseline(root):
    marker = {
        "schema_version": 1,
        "base_commit": "base-commit",
        "files": {
            p.relative_to(root).as_posix(): sha(p.read_bytes())
            for p in root.rglob("*")
            if p.is_file()
        },
    }
    (root / SNAPSHOT).write_text(json.dumps(marker))


def test_independent_agents_can_continue_from_same_snapshot(tmp_path):
    repo = tmp_path / "coordinator"
    repo.mkdir()
    pack(repo, "music")
    pack(repo, "history")
    baseline(repo)
    left, right = tmp_path / "left", tmp_path / "right"
    shutil.copytree(repo, left)
    shutil.copytree(repo, right)
    for work, namespace in [(left, "music"), (right, "history")]:
        transcript = work / "content" / namespace / "001000-introduction.md"
        transcript.write_text(
            transcript.read_text().replace("an example", "a worked example")
        )
        (work / "content" / namespace / "README.md").write_text(
            "Pack-specific author notes."
        )
        build(work, [f"content/{namespace}"], tmp_path / f"{namespace}.zip")
    (repo / "server-code.py").write_text("Coordinator work continued independently.\n")
    assert len(apply(repo, tmp_path / "music.zip", check=True)) == 2
    assert not (repo / "content/music/README.md").exists()
    assert len(apply(repo, tmp_path / "music.zip")) == 2
    assert len(apply(repo, tmp_path / "history.zip")) == 2
    assert apply(repo, tmp_path / "music.zip") == []
    assert (
        repo / "server-code.py"
    ).read_text() == "Coordinator work continued independently.\n"


def test_stale_same_pack_revision_conflicts_before_any_write(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    pack(repo, "music")
    baseline(repo)
    agent = tmp_path / "agent"
    shutil.copytree(repo, agent)
    incoming = agent / "content/music/001000-introduction.md"
    incoming.write_text(incoming.read_text().replace("example", "different example"))
    (agent / "content/music/README.md").write_text("New notes")
    build(agent, ["content/music"], tmp_path / "changes.zip")
    local = repo / "content/music/001000-introduction.md"
    local.write_text(local.read_text().replace("example", "coordinator example"))
    before = local.read_bytes()
    with pytest.raises(OverlayConflict):
        apply(repo, tmp_path / "changes.zip")
    assert local.read_bytes() == before
    assert not (repo / "content/music/README.md").exists()


def test_new_namespace_needs_no_shared_registry(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    baseline(repo)
    agent = tmp_path / "agent"
    shutil.copytree(repo, agent)
    pack(agent, "new-subject")
    build(agent, ["content/new-subject"], tmp_path / "new.zip")
    assert len(apply(repo, tmp_path / "new.zip")) == 3
    assert (repo / "content/new-subject/track.json").exists()
    assert not (repo / "registry.json").exists()


def test_invalid_resulting_inventory_is_rejected_before_mutation(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    pack(repo, "music")
    baseline(repo)
    agent = tmp_path / "agent"
    shutil.copytree(repo, agent)
    manifest = agent / "content/music/track.json"
    plan = json.loads(manifest.read_text())
    plan["lectures"] = []
    manifest.write_text(json.dumps(plan))
    build(agent, ["content/music"], tmp_path / "invalid.zip")
    old = (repo / "content/music/track.json").read_bytes()
    with pytest.raises(ValueError, match="manifest"):
        apply(repo, tmp_path / "invalid.zip")
    assert (repo / "content/music/track.json").read_bytes() == old


def test_source_deletions_require_explicit_review(tmp_path):
    pack(tmp_path, "music")
    baseline(tmp_path)
    (tmp_path / "content/music/001000-introduction.md").unlink()
    with pytest.raises(ValueError, match="deletion"):
        build(tmp_path, ["content/music"], tmp_path / "deletion.zip")


def test_global_files_cannot_be_smuggled_into_pack_overlay(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    pack(repo, "music")
    baseline(repo)
    payload = b"change global code"
    manifest = {
        "schema_version": 1,
        "base_commit": "base",
        "pack_roots": ["content/music"],
        "files": {"ailectures/web.py": {"base_sha256": None, "sha256": sha(payload)}},
    }
    with ZipFile(tmp_path / "bad.zip", "w") as z:
        z.writestr(OVERLAY, json.dumps(manifest))
        z.writestr("ailectures/web.py", payload)
    with pytest.raises(ValueError, match="outside declared pack"):
        apply(repo, tmp_path / "bad.zip")
    assert not (repo / "ailectures").exists()


def test_source_snapshot_only_contains_committed_tree(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    (repo / ".gitignore").write_text(".env\naudio-cache/\n")
    (repo / "README.md").write_text("Source material")
    subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "Fixture",
        ],
        check=True,
    )
    (repo / ".env").write_text("PRIVATE=not-for-transfer")
    (repo / "audio-cache").mkdir()
    (repo / "audio-cache/private.wav").write_bytes(b"private recording")
    archive = tmp_path / "source.zip"
    revision = snapshot(repo, archive)
    with ZipFile(archive) as z:
        assert ".env" not in z.namelist()
        assert not any(p.startswith("audio-cache/") for p in z.namelist())
        receipt = json.loads(z.read(SNAPSHOT))
        assert receipt["base_commit"] == revision
        assert receipt["files"]["README.md"] == sha(z.read("README.md"))
