"""Old scene narration enters the portable reader without renderer imports."""

from pathlib import Path
import builtins
import shutil

import pytest
from starlette.testclient import TestClient

from ailectures.core import BEGIN, END, text_digest
from ailectures.manuscripts import read_scene_narration, spoken_transcript
from ailectures.presentations import presentation_pack
from ailectures.library import Library
from ailectures.packs import export_release
from ailectures.web import create_app
from test_production_recovery import manager_for, finished
from test_content_packs import media_for

SCENES = """# Source and editorial notes
Not spoken.

## FirstScene: First visible title
Why: Motivation stays unspoken.
Recall: Reminder stays unspoken.

First narrated
paragraph.

<!-- beat -->

Second narrated paragraph.

## SecondScene: Another visible title
Why: Another motivation.
Recall: Another reminder.

Final narration.
"""


def test_scene_and_marked_manuscripts_produce_the_same_declared_speech():
    sections = read_scene_narration(SCENES, scenes=["FirstScene", "SecondScene"])
    assert list(sections) == ["FirstScene", "SecondScene"]
    assert sections["FirstScene"].beats == (
        "First narrated paragraph.",
        "Second narrated paragraph.",
    )
    speech = "\n\n".join(section.text for section in sections.values())
    assert spoken_transcript(SCENES) == spoken_transcript(
        BEGIN + "\n" + speech + "\n" + END
    )
    assert (
        "Not spoken" not in speech
        and "Motivation" not in speech
        and "Reminder" not in speech
    )
    with pytest.raises(ValueError, match="scene order"):
        read_scene_narration(SCENES, scenes=["SecondScene", "FirstScene"])
    with pytest.raises(ValueError, match="spoken-region"):
        spoken_transcript(BEGIN + SCENES)
    with pytest.raises(ValueError, match="motivation"):
        read_scene_narration(
            SCENES.replace("Why: Motivation stays unspoken.", "No declared motivation.")
        )


def write_presentation_repository(root, source=SCENES):
    folder = root / "lectures" / "000000_example"
    folder.mkdir(parents=True)
    (folder / "lecture.md").write_text(source)
    (root / "lectures/index.yaml").write_text(
        "lectures:\n  example:\n    title: Example\n    deck: example-deck\n    requires: []\n"
    )
    return root


def test_migrated_deck_is_a_portable_audio_lecture_without_dk_imports(
    tmp_path, monkeypatch
):
    repository = write_presentation_repository(tmp_path / "repository")
    original = builtins.__import__

    def no_renderers(name, *args, **kwargs):
        if name == "dkvis" or name.startswith(("dkvis.", "manim")):
            raise ImportError("Optional production stack is absent")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", no_renderers)
    pack = presentation_pack(repository)
    row = pack["lectures"]["g1:example-deck"]
    assert row["kind"] == "audio" and row["deck"] == "example-deck"
    assert row["aliases"] == ["g1:000000_example"]
    assert row["transcript"] == spoken_transcript(SCENES)
    assert row["spoken_sha256"] == text_digest(row["transcript"])
    export_release(pack, tmp_path / "release")
    library = Library(tmp_path / "library")
    library.store.install(tmp_path / "release")
    with TestClient(create_app(library.store.root, playback_only=True)) as client:
        catalog = client.get("/api/library/catalog").json()
        assert (
            catalog["lectures"][0]["kind"] == "audio"
            and catalog["lectures"][0]["words"] > 0
        )
        assert (
            client.get("/api/library/lectures/g1:example-deck").json()["transcript"]
            == row["transcript"]
        )
        assert client.get("/lectures/g1/example-deck").status_code == 200


def test_unusable_narration_keeps_the_deck_and_its_diagnostic(tmp_path):
    repository = write_presentation_repository(
        tmp_path / "repository", source="# Slides only\nEditorial material."
    )
    row = presentation_pack(repository)["lectures"]["g1:example-deck"]
    assert row["kind"] == "presentation" and row["transcript"] == ""
    assert row["metadata"]["narration_diagnostic"]


def test_legacy_production_wrapper_uses_the_shared_parser(tmp_path):
    from dkvis.presentation.narration import read_narration, Narration

    source = tmp_path / "lecture.md"
    source.write_text(SCENES)
    parsed = read_narration(source, scenes=["FirstScene", "SecondScene"])
    assert parsed == read_scene_narration(SCENES)
    assert isinstance(parsed["FirstScene"], Narration)


def test_migrated_narration_can_generate_with_existing_public_identity(
    tmp_path, monkeypatch
):
    if not shutil.which("ffprobe"):
        pytest.skip("ffprobe unavailable")
    monkeypatch.setattr("dkvis.presentation.tts.load_env", lambda: None)
    pack = presentation_pack(write_presentation_repository(tmp_path / "repository"))
    row = pack["lectures"]["g1:example-deck"]
    export_release(pack, tmp_path / "release")
    library = Library(tmp_path / "library")
    library.store.install(tmp_path / "release")
    audio = next(iter(media_for(pack, tmp_path)[2].values()))
    config = tmp_path / "tts.toml"
    config.write_text(
        '[profiles.test]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="af_alloy"\nresponse_format="mp3"\n'
    )
    manager = manager_for(
        library, config, lambda text, settings, dest: shutil.copyfile(audio, dest)
    )
    try:
        profile = manager.profile_catalog()["profiles"][0]
        request = manager.prepare_saved([row["id"]], profile["id"])[0]
        assert finished(manager, request["id"])["state"] == "ready"
        record = library.snapshot()["lectures"][row["id"]]["recordings"][0]
        assert record["complete"] and record["spoken_sha256"] == row["spoken_sha256"]
    finally:
        manager.close()
