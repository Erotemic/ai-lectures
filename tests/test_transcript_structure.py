"""Transcript display headings preserve source roles without changing speech."""

from starlette.testclient import TestClient
from ailectures.core import BEGIN, END, extract_text, lecture_revision
from ailectures.narration import transcript_headings
from ailectures.web import create_app
from ailectures.library import Library
from ailectures.packs import export_release
from test_content_packs import source_pack


def test_marked_titles_keep_levels_and_occurrence_offsets():
    source = (
        "# Not spoken\n"
        + BEGIN
        + "\n# Shared heading\n\nWe discuss Shared heading here.\n\n### Shared heading\n\nFinal words.\n"
        + END
    )
    text = extract_text(source).strip()
    headings = transcript_headings(source, text)
    assert [(h["start"], h["end"], h["level"]) for h in headings] == [
        (0, 2, 1),
        (7, 9, 3),
    ]
    assert all(h["spoken"] for h in headings)
    assert transcript_headings(source, "A different revision.") == ()
    assert transcript_headings({"format": "unknown"}, text) == ()


def test_scene_captions_are_unspoken_and_body_word_offsets_remain_stable():
    source = "# Editorial\nNot spoken.\n## Cover: A title\nWhy: Motivation.\nRecall: Reminder.\n\nA title.\n\n## Details: A visible section\nWhy: Motivation.\nRecall: Reminder.\n\nBody words.\n"
    from ailectures.manuscripts import spoken_transcript

    text = spoken_transcript(source)
    headings = transcript_headings(source, text)
    assert headings[0]["spoken"] and (headings[0]["start"], headings[0]["end"]) == (
        0,
        2,
    )
    assert not headings[1]["spoken"] and headings[1]["start"] == headings[1]["end"] == 2
    assert headings[1]["text"] == "A visible section"
    assert "A visible section" not in text


def test_structure_is_display_metadata_not_part_of_source_or_recording_identity(
    tmp_path,
):
    source = BEGIN + "\n# A title\n\nBody words.\n" + END
    pack = source_pack(text=extract_text(source).strip())
    key = next(iter(pack["lectures"]))
    pack["lectures"][key]["source"] = source
    pack["lectures"][key]["revision"] = lecture_revision(pack["lectures"][key])
    export_release(pack, tmp_path / "source")
    library = Library(tmp_path / "reader")
    library.store.install(tmp_path / "source")
    original = library.snapshot()["lectures"][key]
    with TestClient(create_app(library.store.root, playback_only=True)) as client:
        row = client.get("/api/library/lectures/" + key).json()
        assert row["transcript_headings"][0]["level"] == 1
        assert (
            row["spoken_sha256"] == original["spoken_sha256"]
            and row["revision"] == original["revision"]
        )
        assert (
            "transcript_headings"
            not in client.get("/api/library/catalog").json()["lectures"][0]
        )
    assert "transcript_headings" not in library.snapshot()["lectures"][key]
