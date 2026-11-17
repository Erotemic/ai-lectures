"""Chronological sorting metadata does not manufacture dates or coverage."""

from copy import deepcopy

import pytest

from ailectures.chronology import (
    MAX_YEAR, chronology_for, collection_chronology, normalize_chronology,
)


@pytest.mark.parametrize("record,label", [
    ({"start": -500}, "500 BCE"),
    ({"start": 500}, "500 CE"),
    ({"start": -700, "end": -500}, "700–500 BCE"),
    ({"start": 1200, "end": 1300}, "1200–1300 CE"),
    ({"start": -50, "end": 50}, "50 BCE–50 CE"),
    ({"start": -1, "end": 1}, "1 BCE–1 CE"),
    ({"start": -4_500_000_000, "approximate": True}, "c. 4,500,000,000 BCE"),
    ({"start": 1590, "end": 1592, "approximate": True}, "c. 1590–1592 CE"),
])
def test_historical_year_labels(record, label):
    result = normalize_chronology({"work": record})["work"]
    assert result["label"] == label
    assert result["end"] == record.get("end", record["start"])
    assert result["approximate"] == record.get("approximate", False)


def test_authored_labels_provenance_and_axis_meanings_are_retained():
    value = {
        "work": {"start": 1818, "label": "1818 first edition", "basis": "publication", "source_ids": ["first", "first"], "note": "The revision appeared later."},
        "setting": {"start": 1700, "end": 1800, "basis": "fictional setting", "approximate": True},
        "period": {"start": -500, "end": 1500, "basis": "covered period"},
        "life": {"start": 1797, "end": 1851, "basis": "author's life"},
        "witness": {"start": 1831, "basis": "revised text"},
        "source_publication": {"start": 2025},
    }
    result = normalize_chronology(value)
    assert set(result) == {"work", "period", "setting", "life", "witness"}
    assert result["work"]["start"] == 1818
    assert result["work"]["label"] == "1818 first edition"
    assert result["work"]["basis"] == "publication"
    assert result["work"]["note"] == "The revision appeared later."
    assert result["work"]["source_ids"] == ["first"]
    assert result["setting"]["approximate"]
    assert result["witness"]["start"] == 1831


@pytest.mark.parametrize("record", [
    None, [], {}, {"start": 0}, {"start": -1, "end": 0}, {"start": 1, "end": -1},
    {"start": "1592"}, {"start": 1592.0}, {"start": True}, {"start": 1592, "end": False},
    {"start": MAX_YEAR + 1}, {"start": -MAX_YEAR - 1}, {"start": 1592, "end": None},
    {"start": 1592, "approximate": "true"}, {"start": 1592, "approximate": 1},
    {"start": 1592, "label": {}}, {"start": 1592, "label": "x" * 513},
    {"start": 1592, "label": "bad\x00label"}, {"start": 1592, "basis": None},
    {"start": 1592, "note": "x" * 8001}, {"start": 1592, "source_ids": "book"},
    {"start": 1592, "source_ids": [None]}, {"start": 1592, "source_ids": [""]},
    {"start": 1592, "source_ids": ["x" * 257]}, {"start": 1592, "source_ids": ["book"] * 513},
])
def test_malformed_optional_axis_does_not_hide_other_valid_dates(record):
    result = normalize_chronology({"work": record, "period": {"start": 1500}})
    assert "work" not in result
    assert result["period"]["start"] == 1500


def test_unknown_chronology_and_empty_optional_labels():
    for value in (None, [], "1592", 1592):
        assert normalize_chronology(value) == {}
    assert normalize_chronology({"work": {"start": MAX_YEAR}})["work"]["start"] == MAX_YEAR
    assert normalize_chronology({"work": {"start": -MAX_YEAR}})["work"]["start"] == -MAX_YEAR
    assert normalize_chronology({"work": {"start": 1592, "label": "  "}})["work"]["label"] == "1592 CE"


def test_canonical_and_source_metadata_have_per_axis_precedence_without_inference():
    row = dict(id="189000", file="1592-title.md", title="Story in 1200", sources={"publication": {"year": 2025}},
               metadata={"chronology": {"work": {"start": 1818}, "setting": {"start": 1700}}},
               chronology={"work": {"start": 1831}, "life": {"start": 1797}})
    dates = chronology_for(row)
    assert dates["work"]["start"] == 1831 and dates["setting"]["start"] == 1700
    assert dates["life"]["start"] == 1797
    assert "witness" not in dates and "period" not in dates
    assert chronology_for({"id": "159200", "file": "1592-novel.md", "title": "Publication 1592"}) == {}
    assert chronology_for({"metadata": {"chronology": {"work": {"start": 1818}}}, "chronology": {"work": {"start": 0}}})["work"]["start"] == 1818
    assert chronology_for(None) == {}


def test_collection_requires_all_members_per_axis_and_deduplicates_members():
    members = {
        "A": {"chronology": {"work": {"start": 1600}, "setting": {"start": -500, "end": -300}}},
        "B": {"metadata": {"chronology": {"work": {"start": 1900}}}},
    }
    result = collection_chronology({"lectures": ["A", "A", "B"]}, members)
    assert result["work"]["start"] == 1600 and result["work"]["end"] == 1900
    assert result["work"]["basis"] == "contents"
    assert result["work"]["label"] == "Range of dated contents: 1600–1900 CE"
    assert "setting" not in result
    assert collection_chronology({"lectures": ["A", "missing"]}, members) == {}
    assert collection_chronology({"lectures": ["A", None]}, members) == {}
    assert collection_chronology({"lectures": []}, members) == {}
    assert collection_chronology({"lectures": "A"}, members) == {}


def test_explicit_collection_axis_survives_partial_or_absent_child_dates():
    collection = {"lectures": ["A", "missing"], "chronology": {
        "period": {"start": -3500, "end": 1500, "label": "Early cities to 1500", "basis": "covered period", "source_ids": ["editorial-scope"]},
    }}
    result = collection_chronology(collection, {"A": {}})
    assert result == normalize_chronology(collection["chronology"])


def test_same_work_date_and_basis_are_inherited_without_a_fictitious_collection_date():
    work = {"start": 1592, "label": "1592 received complete printing", "basis": "publication", "note": "Authorship remains debated.", "source_ids": ["edition"]}
    members = {key: {"metadata": {"chronology": {"work": deepcopy(work)}}} for key in ("A", "B")}
    members["B"]["metadata"]["chronology"]["work"]["source_ids"] = ["edition", "catalog"]
    result = collection_chronology({"lectures": ["A", "B"]}, members)["work"]
    assert result["start"] == result["end"] == 1592
    assert result["label"] == work["label"] and result["basis"] == "publication"
    assert result["source_ids"] == ["edition", "catalog"] and result["note"] == work["note"]


def test_derived_extents_keep_uncertainty_notes_sources_and_mixed_bases():
    members = {
        "A": {"chronology": {"work": {"start": -100, "end": -50, "approximate": True, "basis": "composition", "note": "First text is uncertain.", "source_ids": ["alpha"]}}},
        "B": {"chronology": {"work": {"start": 1500, "end": 1600, "basis": "publication", "note": "Different printed witnesses.", "source_ids": ["beta"]}}},
    }
    result = collection_chronology({"lectures": ["A", "B"]}, members)["work"]
    assert (result["start"], result["end"]) == (-100, 1600)
    assert result["approximate"] and result["basis"] == "mixed"
    assert result["label"] == "Range of dated contents: c. 100 BCE–1600 CE"
    assert result["source_ids"] == ["alpha", "beta"]
    assert "composition" in result["note"] and "publication" in result["note"]
    assert "First text is uncertain." in result["note"]
    assert "Different printed witnesses." in result["note"]


def test_inherited_ranges_stay_axis_specific_and_explicit_collection_wins():
    members = {
        "A": {"chronology": {"period": {"start": -500, "end": 100}, "life": {"start": 1800, "end": 1850}}},
        "B": {"chronology": {"period": {"start": -300, "end": 500}, "life": {"start": 1900, "end": 1950}}},
    }
    collection = {"lectures": ["A", "B"], "chronology": {"life": {"start": 1700, "label": "Explicit life scope"}}}
    result = collection_chronology(collection, members)
    assert (result["period"]["start"], result["period"]["end"]) == (-500, 500)
    assert result["life"]["start"] == 1700 and result["life"]["label"] == "Explicit life scope"
    assert "work" not in result and "setting" not in result


def test_normalization_and_collection_derivation_do_not_share_mutable_inputs():
    row = {"metadata": {"chronology": {"work": {"start": 1818, "source_ids": ["primary"], "note": "Retain this note."}}}}
    collection, members = {"lectures": ["A"]}, {"A": row}
    before = deepcopy((row, collection, members))
    normalized = chronology_for(row)
    inherited = collection_chronology(collection, members)
    normalized["work"]["source_ids"].append("local-change")
    inherited["work"]["source_ids"].append("another-change")
    assert (row, collection, members) == before


def test_large_anthology_keeps_extent_and_refers_to_member_qualifications():
    members = {
        str(index): {"chronology": {"work": {
            "start": 1900 + index, "basis": "publication",
            "note": str(index) + ": " + "A qualified date. " * 100,
            "source_ids": ["source-" + str(index)],
            "approximate": index == 3,
        }}} for index in range(10)
    }
    result = collection_chronology({"lectures": list(members)}, members)["work"]
    assert (result["start"], result["end"]) == (1900, 1909)
    assert result["approximate"] and result["basis"] == "contents"
    assert "Member-specific qualifications" in result["note"]
    assert len(result["source_ids"]) == 10
    assert normalize_chronology({"work": result})["work"] == result
    assert len(members["0"]["chronology"]["work"]["note"]) > 1000
