"""One portable selection can drive preparation and an audio-complete handoff."""
import json

import pytest

from ailectures.__main__ import main
from ailectures.deployment import export_deployment, trim_course
from ailectures.library import Library
from ailectures.packs import export_release
from test_content_packs import media_for, source_pack
from test_deployment_and_gc import install


@pytest.mark.parametrize("partial", [False, True])
def test_complete_handoff_rejects_missing_or_partial_audio_without_an_archive(tmp_path, partial):
    library = Library(tmp_path / "library")
    pack = source_pack()
    media = media_for(pack, tmp_path, complete=False) if partial else None
    export_release(pack, tmp_path / "release", media=[media] if media else [])
    library.store.install(tmp_path / "release")
    output = tmp_path / "handoff.zip"
    with pytest.raises(ValueError):
        export_deployment(library, {"packs": ["music"]}, output, require_complete=True)
    assert not output.exists()
    # Source-only/partial exports remain available when explicitly desired.
    assert export_deployment(library, {"packs": ["music"]}, output)["lectures"] == 1


def test_prepare_uses_selection_and_saved_recipe_skipping_complete_audio(tmp_path, monkeypatch):
    import ailectures.production as production
    library = Library(tmp_path / "library")
    install(library, tmp_path)
    install(library, tmp_path, "stories", media=False)
    install(library, tmp_path, "omitted", media=False)
    selection = tmp_path / "selection.json"
    selection.write_text(json.dumps({"packs": ["music", "stories"]}))
    calls = []

    class Manager:
        def __init__(self, *args, **kwargs):
            pass

        def prepare_saved(self, keys, profile):
            calls.append((keys, profile))
            return [dict(lecture_id=key, published="fixture-release") for key in keys]

        def close(self):
            calls.append("closed")

    monkeypatch.setattr(production, "GenerationManager", Manager)
    monkeypatch.chdir(tmp_path)
    main(["--library", str(library.store.root), "prepare", "--selection", str(selection),
          "--skip-complete", "--saved-profile", "fixture-profile"])
    assert calls == [(["stories:001000"], "fixture-profile"), "closed"]


def test_complete_preparation_selection_needs_no_tts_configuration(tmp_path, monkeypatch):
    import ailectures.production as production
    library = Library(tmp_path / "library")
    install(library, tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(production, "GenerationManager", lambda *args, **kwargs: pytest.fail("Opened TTS for complete selection"))
    assert main(["--library", str(library.store.root), "prepare", "--lecture", "music:001000",
                 "--skip-complete", "--profile", "unused"]) == 0


def test_cli_complete_export_and_installed_only_server(tmp_path, monkeypatch):
    import uvicorn
    library = Library(tmp_path / "library")
    install(library, tmp_path)
    output = tmp_path / "ready.zip"
    monkeypatch.chdir(tmp_path)
    main(["--library", str(library.store.root), "bundle", "--pack", "music",
          "--require-complete", "--output", str(output)])
    assert output.is_file()
    # Even inside a checkout, the recipient's server only sees installed packs.
    (tmp_path / "content").mkdir()
    captured = []
    monkeypatch.setattr(uvicorn, "run", lambda app, **kwargs: captured.append(app))
    main(["--library", str(library.store.root), "serve", "--installed-only", "--playback-only"])
    assert len(captured) == 1 and captured[0].state.library.repository is None


def test_subset_routes_only_link_to_retained_collections():
    course = dict(id="sample:study", parent_id="sample:omitted-hub",
                  related_collections=["sample:kept", "sample:omitted"],
                  preparation_collections=["sample:omitted"],
                  chapters=[dict(title="Study", lectures=["sample:one", "sample:two"], collection="sample:omitted")])
    result = trim_course(course, {"sample:one"}, {"sample:study", "sample:kept"})
    assert "parent_id" not in result and "collection" not in result["chapters"][0]
    assert result["related_collections"] == ["sample:kept"]
    assert not result["preparation_collections"]
    assert result["chapters"][0]["lectures"] == ["sample:one"]
    assert len(course["chapters"][0]["lectures"]) == 2
