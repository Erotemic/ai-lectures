"""Native maps, companion actions and downloads work without the legacy app."""
import json
from pathlib import Path

from starlette.testclient import TestClient

from ailectures.catalog import RepositoryCatalog
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack, media_for


def test_browser_pack_export_downloads_a_real_installable_archive(tmp_path):
    pack = source_pack()
    export_release(pack, tmp_path / 'release', media=[media_for(pack, tmp_path)])
    app = create_app(tmp_path / 'library')
    app.state.library.store.install(tmp_path / 'release')
    with TestClient(app) as client:
        assert client.post('/api/library/exports', json={'pack_id': 'music'}, headers={'origin': 'https://other.invalid'}).status_code == 403
        result = client.post('/api/library/exports', json={'pack_id': 'music'}, headers={'origin': 'http://testserver'})
        assert result.status_code == 201
        receipt = result.json()
        archive = client.get(receipt['url'])
        assert archive.status_code == 200 and archive.headers['content-type'] == 'application/zip'
        assert 'attachment' in archive.headers['content-disposition']
        target = tmp_path / 'download.zip'
        target.write_bytes(archive.content)
        moved = create_app(tmp_path / 'moved')
        moved.state.library.store.install(target)
        with TestClient(moved) as portable:
            row = portable.get('/api/library/lectures/music:001000').json()
            assert row['recordings'][0]['complete']
            assert portable.get(row['recordings'][0]['segments'][0]['url'], headers={'Range': 'bytes=0-15'}).status_code == 206
        assert client.post('/api/library/exports', json={'pack_id': 'music', 'source_only': 'false'}).status_code == 400
        graph = client.get('/api/library/learning-map')
        assert graph.status_code == 200 and graph.json()['nodes']['music:001000']['available']
        assert client.get('/learning-map').status_code == 200
        optional = client.get('/api/library/slide-decks?lecture_id=music:001000').json()
        assert optional['available'] is False and not optional['items']


def test_native_slide_actions_are_explicit_and_keep_the_lecture_accessible(tmp_path):
    class Slides:
        built = False
        calls = 0
        def list_for_lecture(self, key):
            return {'available': True, 'items': [self.status('example')]}
        def status(self, key):
            if key != 'example': raise KeyError(key)
            return dict(id=key, title='Example', built=self.built)
        def build(self, key):
            self.calls += 1
            self.built = True
            return self.status(key)
        def html_file(self, key):
            self.status(key)
            if not self.built: raise FileNotFoundError(key)
            return html
    html = tmp_path / 'example.html'
    html.write_text('<!doctype html><title>A prepared deck</title>')
    slides = Slides()
    pack = source_pack()
    export_release(pack, tmp_path / 'release')
    app = create_app(tmp_path / 'library', slide_companion_service=slides)
    app.state.library.store.install(tmp_path / 'release')
    with TestClient(app) as client:
        assert client.get('/api/library/slide-decks?lecture_id=music:001000').status_code == 200
        assert slides.calls == 0
        assert client.get('/api/library/slide-decks/example/html').status_code == 404
        assert client.post('/api/library/slide-decks/example/build', json={}, headers={'origin': 'https://other.invalid'}).status_code == 403
        assert slides.calls == 0
        assert client.post('/api/library/slide-decks/example/build', json={}).json()['built']
        assert client.get('/api/library/slide-decks/example/html').text == html.read_text()
        download = client.get('/api/library/slide-decks/example/html?download=1')
        assert 'attachment' in download.headers['content-disposition']
        assert client.get('/api/library/lectures/music:001000').json()['transcript']


def test_missing_source_evidence_survives_source_catalog_and_native_map(tmp_path):
    directory = tmp_path / 'content/music'
    directory.mkdir(parents=True)
    (directory / '001000-example.md').write_text('# Example\n<!-- BEGIN SPOKEN LECTURE -->\nAn example.\n<!-- END SPOKEN LECTURE -->\n')
    (directory / 'track.json').write_text(json.dumps(dict(id='music', title='Music', lectures=[dict(id='001000', file='001000-example.md')])))
    curriculum = tmp_path / 'curriculum'
    curriculum.mkdir()
    edges = [['future:one', 'related_to', 'music:001000', 'An explicit future connection.'], ['future:one', 'proof_depends_on', 'future:two', 'A retained claim between two unavailable sources.']]
    (curriculum / 'relationships.json').write_text(json.dumps({'edges': edges}))
    catalog = RepositoryCatalog(tmp_path)
    assert len(catalog.snapshot()['music']['relationships']) == 2
    with TestClient(create_app(tmp_path / 'library', repository=tmp_path)) as client:
        graph = client.get('/api/library/learning-map').json()
        claims = [(claim['from'], edge['type'], claim['to'], claim.get('why')) for edge in graph['relationships'] for claim in edge['evidence'] if claim['origin'] == 'authored']
        assert set(claims) == {tuple(edge) for edge in edges}
        assert graph['nodes']['future:one']['url'] is None
        assert not graph['nodes']['future:two']['available']


def test_prepared_html_can_be_viewed_without_a_renderer_and_still_downloaded(tmp_path):
    from ailectures.core import file_digest, lecture_revision
    pack = source_pack()
    html = tmp_path / 'slides.html'
    html.write_text('<!doctype html><title>Prepared independently</title><p>A companion.</p>')
    row = pack['lectures']['music:001000']
    row['companions'] = [dict(id='slides', title='Prepared slides', role='prepared', media_type='text/html', path='companions/slides.html', sha256=file_digest(html))]
    row['revision'] = lecture_revision(row)
    pack['extra_files'] = {'companions/slides.html': html}
    export_release(pack, tmp_path / 'release')
    app = create_app(tmp_path / 'library')
    app.state.library.store.install(tmp_path / 'release')
    with TestClient(app) as client:
        companion = client.get('/api/library/lectures/music:001000').json()['companions'][0]
        assert 'attachment' in client.get(companion['url']).headers['content-disposition']
        view = client.get(companion['url'] + '?view=1')
        assert view.text == html.read_text()
        assert 'content-disposition' not in view.headers
        assert 'sandbox' in view.headers['content-security-policy']
        assert client.get('/api/library/slide-decks?lecture_id=music:001000').json()['available'] is False
