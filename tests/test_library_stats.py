"""The stats view uses the portable catalog and keeps playback tools optional."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess

import pytest
from starlette.testclient import TestClient
from ailectures.web import create_app


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'a' and 'data-nav' in attributes:
            self.links.append(attributes.get('href'))


def test_stats_loads_directly_without_production_or_legacy(tmp_path):
    def legacy():
        pytest.fail('Stats must not start the legacy presentation app')

    with TestClient(create_app(tmp_path / 'library', legacy_factory=legacy)) as client:
        response = client.get('/stats')
        assert response.status_code == 200
        nav = Navigation()
        nav.feed(response.text)
        assert '/stats' in nav.links
        assert '/presentations' not in nav.links
        assert 'id="presentations"' not in response.text
        catalog = client.get('/api/library/catalog').json()
        assert catalog['lectures'] == []
        for asset in ('stats.mjs', 'stats-model.mjs'):
            assert client.get('/library-assets/' + asset).status_code == 200


def test_statistics_count_content_instead_of_route_and_recording_occurrences():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is needed for browser-model checks')
    subprocess.run([node, str(Path(__file__).with_name('test_stats_model.mjs'))], check=True)
