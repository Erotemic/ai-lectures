"""The complete inventory is a native reader page, independent of presentation tools."""
from pathlib import Path
import shutil
import subprocess

import pytest
from starlette.testclient import TestClient
from ailectures.web import create_app
from test_library_stats import Navigation


def test_flat_inventory_has_a_direct_route_and_navigation(tmp_path):
    def legacy():
        pytest.fail('The flat inventory must not initialize presentation tools')
    with TestClient(create_app(tmp_path/'library', legacy_factory=legacy)) as client:
        response = client.get('/lectures?q=memory&show=all')
        assert response.status_code == 200
        nav = Navigation()
        nav.feed(response.text)
        assert '/lectures' in nav.links
        assert client.get('/api/library/catalog').json()['lectures'] == []
        for asset in ('all-lectures.mjs', 'all-lectures-model.mjs'):
            assert client.get('/library-assets/'+asset).status_code == 200


def test_flat_inventory_model_and_return_path_behavior():
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is required for browser model checks')
    subprocess.run([node, str(Path(__file__).with_suffix('.mjs'))], check=True)
