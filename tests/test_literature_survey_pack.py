"""Source integrity for the compact introductions, independent of prose style."""

import json
from pathlib import Path

from ailectures.catalog import repository_track
from ailectures.core import extract_text


def test_compact_introductions_resolve_sources_and_record_actual_speech_counts():
    directory = Path(__file__).resolve().parents[1] / "content" / "literature-survey"
    plan = json.loads((directory / "track.json").read_text())
    sources = json.loads((directory / "metadata" / "sources.json").read_text())[
        "sources"
    ]
    assert len({row["id"] for row in plan["lectures"]}) == len(plan["lectures"])
    for row in plan["lectures"]:
        speech = extract_text((directory / row["file"]).read_text()).strip()
        assert row["spoken_words"] == len(speech.split())
        assert row["estimated_minutes_at_145_wpm"] == round(
            len(speech.split()) / 145, 1
        )
        notes = json.loads((directory / "metadata" / (row["id"] + ".json")).read_text())
        assert notes["lecture_id"] == row["id"]
        assert notes["transcript"] == row["file"]
        for resource in notes.get("related_resources", []):
            assert resource["source_id"] in sources
        for claim in notes.get("historical_claims", []):
            assert speech.count(claim["anchor"]) == 1
            assert set(claim["source_ids"]) <= sources.keys()
    pack = repository_track(directory, strict=True)
    assert len(pack["lectures"]) == len(plan["lectures"])
