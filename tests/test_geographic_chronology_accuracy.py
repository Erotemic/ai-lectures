"""High-value regressions for curated place and literary-date axes."""
import json
from pathlib import Path

from ailectures.discovery import discovery_fields
from ailectures.tagging import PLACE_PATHS, tag_paths


ROOT = Path(__file__).resolve().parents[1]


def _lecture(path):
    return discovery_fields({'metadata': json.loads((ROOT / path).read_text())})


def test_place_paths_are_valid_and_context_specific():
    assert all(len(path) == len(set(path)) for path in PLACE_PATHS)
    assert ['Place: Europe', 'Place: Germany', 'Place: Berlin, Germany'] in tag_paths([], ['Berlin, Germany'])
    assert ['Place: Water bodies', 'Place: Oceans', 'Place: Atlantic Ocean',
            'Place: North Atlantic Ocean'] in tag_paths([], ['North Atlantic Ocean'])
    # Bare Cambridge and Great Lakes must not acquire an arbitrary continent.
    assert tag_paths([], ['Cambridge']) == [['Place: Cambridge']]
    assert tag_paths([], ['Great Lakes']) == [['Place: Great Lakes']]
    east_africa = _lecture('content/ancient-medieval-world/metadata/036840.json')
    assert ['Place: Africa', 'Place: East Africa', 'Place: African Great Lakes',
            'Place: Great Lakes'] in east_africa['tag_paths']
    england = _lecture('content/history/metadata/082000.json')
    usa = _lecture('content/history/metadata/146000.json')
    assert ['Place: Europe', 'Place: Britain', 'Place: England',
            'Place: Cambridge'] in england['tag_paths']
    assert ['Place: Americas', 'Place: North America', 'Place: United States',
            'Place: Massachusetts', 'Place: Cambridge'] in usa['tag_paths']


def test_composition_and_surviving_witness_are_separate_from_publication():
    ferdowsi = _lecture('content/world-history/metadata/087000.json')
    # Discovery paths keep the original date meaning, not just the raw year.
    assert any(p[0] == 'Composition date: CE' for p in ferdowsi['tag_paths'])
    assert any(p[0] == 'Surviving witness: CE' for p in ferdowsi['tag_paths'])
    assert not any(p[0].startswith('Work date:') for p in ferdowsi['tag_paths'])
    modern = _lecture('content/modern-literature/metadata/030000.json')
    assert any(p[0] == 'Work date: CE' for p in modern['tag_paths'])
