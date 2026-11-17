"""Native slide associations/builds are optional and preserve source ownership."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import threading
from types import SimpleNamespace

import pytest

from ailectures.slide_companions import SlideCompanions


class Renderer:
    def __init__(self, root):
        self.root = root
        self.built = set()
        self.calls = []
        self.entered = None
        self.resume = None
        self.failure = None

    def status(self, key):
        return dict(id=key, title="A companion", subtitle="A diagram", slide_count=2,
                    built=key in self.built, url="/legacy", download_url="/legacy/download")

    def build(self, key):
        self.calls.append(key)
        if self.entered:
            self.entered.set()
            assert self.resume.wait(timeout=5)
        if self.failure:
            raise self.failure
        self.built.add(key)
        self.rendered(key).write_text("<!doctype html><html>Prepared slides</html>")

    def rendered(self, key):
        if key not in self.built:
            raise FileNotFoundError(key)
        return self.root / (key + ".html")


@pytest.fixture
def companions(tmp_path):
    source = tmp_path / "companion-slides"
    source.mkdir()
    entries = [dict(id=key, source=key + ".json", lecture_nodes=[node])
               for key, node in [("first-deck", "g2:001000"), ("second-deck", "g2:003000")]]
    (source / "manifest.json").write_text(json.dumps(dict(schema_version=1, decks=entries)))
    for entry in entries:
        (source / entry["source"]).write_text(json.dumps(dict(
            attribution="Original diagram author", sources=[dict(id="primary", title="Primary paper")]
        )))
    rows = {
        "g2:001000": dict(id="g2:001000", sources={"paper": dict(title="A paper", url="https://example.org/paper")}, metadata=dict(
            consolidation=dict(sources=[dict(id="g2:002000", metadata=dict(
                consolidation=dict(sources=[dict(id="g2:003000", metadata={})])
            ))])
        )),
        "music:001000": dict(id="music:001000", sources={}, metadata={}),
    }
    repository = SimpleNamespace(root=tmp_path, snapshot=lambda **_: {"g2": dict(lectures=rows)})
    renderer = Renderer(tmp_path)
    service = SlideCompanions(repository, renderer_factory=lambda: renderer)
    return service, renderer, rows, source


def test_portable_import_does_not_load_repository_renderer():
    script = """
import builtins, sys
original = builtins.__import__
def guarded(name, *args, **kwargs):
    if name.split('.')[0] in {'dkvis', 'manim', 'numpy', 'networkx'}:
        raise AssertionError('Unexpected optional import: ' + name)
    return original(name, *args, **kwargs)
builtins.__import__ = guarded
from ailectures.slide_companions import SlideCompanions
assert SlideCompanions().list_for_lecture('g2:001000')['available'] is False
"""
    subprocess.run([sys.executable, "-c", script], check=True, cwd=Path(__file__).parents[1])


def test_nested_lineage_maps_all_decks_to_current_lecture(companions):
    service, renderer, rows, _ = companions
    original = deepcopy(rows)
    result = service.list_for_lecture("g2:001000")
    assert result["available"]
    assert [item["id"] for item in result["items"]] == ["first-deck", "second-deck"]
    assert all(item["lecture_ids"] == ["g2:001000"] for item in result["items"])
    assert result["items"][1]["lecture_nodes"] == ["g2:003000"]
    assert result["items"][0]["attribution"] == "Original diagram author"
    assert result["items"][0]["source_credits"][0]["sources"] == rows["g2:001000"]["sources"]
    assert service.list_for_lecture("music:001000")["items"] == []
    assert renderer.calls == []
    assert rows == original
    with pytest.raises(KeyError):
        service.list_for_lecture("g2:003000")


def test_build_is_explicit_and_html_download_never_builds(companions):
    service, renderer, _, _ = companions
    with pytest.raises(FileNotFoundError):
        service.html_file("first-deck")
    assert renderer.calls == []
    result = service.build("first-deck")
    assert result["built"] and result["state"] == "built"
    assert result["view_url"] == "/api/library/slide-decks/first-deck/html"
    assert result["download_url"] == result["view_url"] + "?download=1"
    assert service.html_file("first-deck").read_text().startswith("<!doctype html>")
    assert service.build("first-deck")["built"]
    assert renderer.calls == ["first-deck"]
    for key in ("missing", "../first-deck"):
        with pytest.raises(KeyError):
            service.build(key)


def test_parallel_build_requests_share_state(companions):
    service, renderer, _, _ = companions
    renderer.entered = threading.Event()
    renderer.resume = threading.Event()
    worker = threading.Thread(target=service.build, args=("first-deck",))
    worker.start()
    try:
        assert renderer.entered.wait(timeout=5)
        assert service.status("first-deck")["state"] == "building"
        assert service.build("first-deck")["state"] == "building"
        assert renderer.calls == ["first-deck"]
    finally:
        renderer.resume.set()
        worker.join(timeout=5)
    assert not worker.is_alive()
    assert service.status("first-deck")["state"] == "built"


def test_failed_build_can_retry_and_bad_optional_source_is_isolated(companions):
    service, renderer, rows, source = companions
    renderer.failure = RuntimeError("Renderer stopped")
    failed = service.build("first-deck")
    assert failed["state"] == "failed" and "Renderer stopped" in failed["error"]
    assert service.status("first-deck")["state"] == "failed"
    assert rows["g2:001000"]["metadata"]["consolidation"]
    renderer.failure = None
    assert service.build("first-deck")["built"]
    (source / "second-deck.json").write_text("broken JSON")
    items = service.list_for_lecture("g2:001000")["items"]
    assert items[0]["built"]
    assert items[1]["state"] == "unavailable" and not items[1]["build_available"]
    assert service.html_file("first-deck").exists()


def test_repository_listing_has_no_manim_numpy_or_networkx_import():
    script = """
import builtins, sys
original = builtins.__import__
def guarded(name, *args, **kwargs):
    if name.split('.')[0] in {'manim', 'numpy', 'networkx'}:
        raise AssertionError('Unexpected heavy import: ' + name)
    return original(name, *args, **kwargs)
builtins.__import__ = guarded
from ailectures.catalog import RepositoryCatalog
from ailectures.slide_companions import SlideCompanions
result = SlideCompanions(RepositoryCatalog('.')).list_for_lecture('g2:001000')
assert result['available'] and result['items']
assert not {'manim', 'numpy', 'networkx'}.intersection(sys.modules)
"""
    subprocess.run([sys.executable, "-c", script], check=True, cwd=Path(__file__).parents[1])
