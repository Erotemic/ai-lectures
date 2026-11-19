"""Count real narrated language, not editorial sources or catalog entries."""

import json
from pathlib import Path
import subprocess
import sys
from xml.etree import ElementTree

import pytest
from starlette.testclient import TestClient

from ailectures.web import create_app
from ailectures.word_cloud import cloud_data, phrase_data


def rows():
    return [
        {"id": "stories:001000", "title": "Story one", "namespace": "stories",
         "origin": {"pack": "stories"},
         "transcript": "What matters is that context matters. This matters because context matters."},
        {"id": "stories:002000", "title": "Story two", "namespace": "stories",
         "origin": {"pack": "stories"},
         "transcript": "What matters is the example. This matters, but why? Context matters."},
        {"id": "music:001000", "title": "Music", "namespace": "music",
         "origin": {"pack": "music"},
         "transcript": "A song matters. Music matters in the end."},
    ]


def test_phrase_frequency_and_lecture_coverage_are_distinct():
    data = cloud_data(rows(), n=1, rank="count", top=15, min_lectures=1)
    matters = next(item for item in data["items"] if item["phrase"] == "matters")
    assert matters["count"] == 9
    assert matters["lectures"] == 3
    assert data["words"] == 30
    assert data["drawn"] <= len(data["items"])
    ElementTree.fromstring(data["svg"])


def test_ngram_boundaries_common_words_and_scope():
    data = cloud_data(rows(), n=3, rank="count", top=50, min_lectures=1)
    counts = {item["phrase"]: item["count"] for item in data["items"]}
    assert counts["what matters is"] == 2
    assert counts["this matters because"] == 1
    assert "matters this matters" not in counts  # a sentence boundary
    assert "is that context" in counts
    assert "is the example" in counts
    restricted = cloud_data(rows(), n=1, pack="music", min_lectures=1)
    assert restricted["lectures"] == 1
    assert next(item for item in restricted["items"] if item["phrase"] == "matters")["count"] == 2
    assert "the" not in {item["phrase"] for item in restricted["items"]}
    with_common = cloud_data(rows(), n=1, include_common=True, min_lectures=1)
    assert "the" in {item["phrase"] for item in with_common["items"]}


def test_phrase_inspection_and_bounds():
    data = phrase_data(rows(), "MATTERS")
    assert data["count"] == 9
    assert data["lectures"] == 3
    assert data["examples"][0]["count"] == 4
    assert "matters" in data["examples"][0]["excerpt"].lower()
    assert phrase_data(rows(), "what matters is")["count"] == 2
    with pytest.raises(ValueError):
        phrase_data(rows(), " ")
    with pytest.raises(ValueError):
        cloud_data(rows(), n=8)
    with pytest.raises(ValueError):
        cloud_data(rows(), pack="unknown")


def test_cloud_source_is_spoken_region_and_is_available_via_web_and_cli(tmp_path, monkeypatch):
    folder = tmp_path / "source" / "content" / "stories"
    folder.mkdir(parents=True)
    manuscript = folder / "001000-trial.md"
    manuscript.write_text(
        "# A story\nEditorial notes: hiddenword.\n"
        "<!-- BEGIN SPOKEN LECTURE -->\n"
        "What matters is the music. Music matters, and music matters.\n"
        "<!-- END SPOKEN LECTURE -->\n## Sources\nhiddenword in sources.\n"
    )
    (folder / "track.json").write_text(json.dumps({
        "id": "stories", "title": "Stories", "lectures": [{"id": "001000", "file": manuscript.name}],
    }))
    repo = folder.parents[1]
    with TestClient(create_app(tmp_path / "reader", repository=repo)) as client:
        assert client.get("/word-cloud").status_code == 200
        assert client.get("/library-assets/word-cloud.mjs").status_code == 200
        result = client.get("/api/library/word-cloud?n=1&top=20&min_lectures=1")
        assert result.status_code == 200
        payload = result.json()
        terms = {item["phrase"]: item["count"] for item in payload["items"]}
        assert terms["matters"] == 3
        assert "hiddenword" not in terms
        assert "<svg" in payload["svg"]
        inspected = client.get("/api/library/word-cloud/find?phrase=matters").json()
        assert inspected["count"] == 3
        assert len(inspected["examples"]) == 1
        assert client.get("/api/library/word-cloud?n=7").status_code == 400
        # Changing top-k reuses the current corpus calculation, not another scan.
        import ailectures.word_cloud as engine
        original = engine.cloud_data
        monkeypatch.setattr(engine, "cloud_data", lambda *a, **kw: pytest.fail("cloud recalculated"))
        cached = client.get("/api/library/word-cloud?n=1&top=2&min_lectures=1")
        assert cached.status_code == 200
        assert len(cached.json()["items"]) == 2
        monkeypatch.setattr(engine, "cloud_data", original)
        manuscript.write_text(manuscript.read_text().replace("Music matters,", "Music changes,"))
        fresh = client.get("/api/library/word-cloud?n=1&top=20&min_lectures=1").json()
        assert next(item for item in fresh["items"] if item["phrase"] == "matters")["count"] == 2
    output = tmp_path / "result.svg"
    cmd = [sys.executable, "-m", "ailectures", "word-cloud", "--repository", str(repo),
           "--n", "1", "--top", "20", "--min-lectures", "1", "--find", "matters",
           "--svg", str(output)]
    completed = subprocess.run(cmd, check=True, capture_output=True, text=True,
                               cwd=Path(__file__).resolve().parents[1])
    assert "matters" in completed.stdout
    ElementTree.parse(output)
    lookup_only = subprocess.run(
        [sys.executable, "-m", "ailectures", "word-cloud", "--repository", str(repo),
         "--find-only", "--find", "matters"],
        check=True, capture_output=True, text=True,
        cwd=Path(__file__).resolve().parents[1],
    )
    assert "matters: 2 occurrences" in lookup_only.stdout
