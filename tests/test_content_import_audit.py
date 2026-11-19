"""Read-only import diagnostics distinguish missing content from occupied IDs."""

from pathlib import Path
import json
from zipfile import ZipFile

import pytest
from tools.audit_content_imports import inspect_archives


def test_inventory_reports_matching_missing_and_conflicting_assignments(tmp_path):
    root = tmp_path / "repo"
    pack = root / "content/example"
    pack.mkdir(parents=True)
    (pack / "001000-existing.md").write_text("Existing text")
    (pack / "track.json").write_text(
        json.dumps(
            {
                "lectures": [
                    {"id": "001000", "title": "Current", "file": "001000-existing.md"}
                ]
            }
        )
    )
    archive = tmp_path / "sample.zip"
    with ZipFile(archive, "w") as z:
        z.writestr("content/example/001000-existing.md", "Existing text")
        z.writestr("content/example/001000-older.md", "Older alternate text")
        z.writestr(
            "content/example/track.json",
            json.dumps(
                {
                    "lectures": [
                        {"id": "001000", "title": "Older", "file": "001000-older.md"}
                    ]
                }
            ),
        )
    duplicate = tmp_path / "duplicate.zip"
    duplicate.write_bytes(archive.read_bytes())
    report = inspect_archives(root, [archive, duplicate])
    assert report["summary"] == dict(
        archives=2,
        unique_archives=1,
        manuscript_versions=2,
        matching_manuscripts=1,
        missing_manuscripts=1,
        changed_manuscripts=0,
    )
    assert report["archives"][0]["catalog_issues"][0]["kind"] == "different_assignment"
    assert (pack / "001000-existing.md").read_text() == "Existing text"
    assert not (pack / "001000-older.md").exists()


def test_archive_path_traversal_is_rejected_without_writes(tmp_path):
    archive = tmp_path / "bad.zip"
    with ZipFile(archive, "w") as z:
        z.writestr("../escape.md", "No writes")
    with pytest.raises(ValueError):
        inspect_archives(tmp_path, [archive])
    assert not (tmp_path.parent / "escape.md").exists()
