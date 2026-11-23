"""Two protocols share one app lifecycle and durable reader state."""
from contextlib import closing
import json
import os
from pathlib import Path
import shutil
import socket
import ssl
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pytest

from ailectures.__main__ import main
from ailectures.serving import certificate_files, run_http_https
from ailectures.library import Library
from ailectures.packs import export_release
from test_content_packs import source_pack, media_for

pytestmark = pytest.mark.skipif(not shutil.which('openssl'), reason='Local certificate generation needs openssl')
ROOT = Path(__file__).resolve().parents[1]


def free_port():
    with closing(socket.socket()) as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


def test_local_certificate_is_reused_private_and_valid_for_declared_names(tmp_path, monkeypatch):
    cert, key = certificate_files(tmp_path, '0.0.0.0', names=['microphone.invalid'])
    assert key.stat().st_mode & 0o777 == 0o600
    output = subprocess.check_output(['openssl', 'x509', '-in', str(cert), '-noout', '-ext', 'subjectAltName'], text=True)
    assert 'DNS:microphone.invalid' in output and 'IP Address:127.0.0.1' in output
    before = (cert.read_bytes(), key.read_bytes())
    monkeypatch.setattr(subprocess, 'run', lambda *args, **kwargs: pytest.fail('Regenerated an existing certificate'))
    assert certificate_files(tmp_path, '0.0.0.0', names=['microphone.invalid']) == (cert, key)
    assert before == (cert.read_bytes(), key.read_bytes())
    assert certificate_files(tmp_path, 'localhost', certfile=cert, keyfile=key) == (cert, key)
    for invalid in ('example.com,DNS:other', '-bad', '../path'):
        with pytest.raises(ValueError):
            certificate_files(tmp_path, 'localhost', names=[invalid])


def test_bad_listener_options_fail_before_creating_certificate_or_server(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    root = tmp_path / 'library'
    for args in (['--https-port', '8001'], ['--https-port', '-1'],
                 ['--ssl-certfile', 'missing'], ['--https-port', '8443', '--ssl-certfile', 'missing']):
        with pytest.raises(SystemExit) as error:
            main(['--library', str(root), 'serve', '--installed-only', *args])
        assert error.value.code == 1
    assert not (root / 'state/tls').exists()


def test_https_config_resolves_certificate_paths_and_cli_port_override(tmp_path, monkeypatch):
    import ailectures.serving as serving
    cert, key = certificate_files(tmp_path, '127.0.0.1')
    config = tmp_path / 'library.toml'
    config.write_text(f'[https]\nport=8443\ncertfile="{cert.relative_to(tmp_path)}"\nkeyfile="{key.relative_to(tmp_path)}"\n')
    elsewhere = tmp_path / 'elsewhere'
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)
    calls = []
    monkeypatch.setattr(serving, 'run_http_https', lambda app, **kwargs: calls.append(kwargs))
    main(['--library', str(tmp_path / 'reader'), 'serve', '--installed-only',
          '--config', str(config), '--https-port', '9443'])
    assert calls == [dict(host='127.0.0.1', port=8001, https_port=9443, certfile=cert, keyfile=key)]


def test_http_https_serve_same_catalog_audio_and_state_with_one_lifespan(tmp_path):
    pack = source_pack()
    export_release(pack, tmp_path / 'release', media=[media_for(pack, tmp_path)])
    library = Library(tmp_path / 'library')
    library.store.install(tmp_path / 'release')
    http_port, https_port = free_port(), free_port()
    while https_port == http_port:
        https_port = free_port()
    trace = tmp_path / 'lifespan.txt'
    code = '''
from contextlib import asynccontextmanager
from pathlib import Path
import sys
import ailectures.web as web
from starlette.responses import JSONResponse
from starlette.routing import Route
from ailectures.__main__ import main
original=web.create_app
trace=Path(sys.argv[1])
def create(*args,**kwargs):
 app=original(*args,**kwargs)
 lifecycle=app.router.lifespan_context
 @asynccontextmanager
 async def lifespan(app):
  with trace.open('a') as stream:stream.write('start\\n')
  async with lifecycle(app):
   yield {'shared_token':'fixture'}
  with trace.open('a') as stream:stream.write('stop\\n')
 app.router.lifespan_context=lifespan
 async def state(request):return JSONResponse({'token':request.state.shared_token})
 app.router.routes.append(Route('/test-shared-state',state))
 return app
web.create_app=create
main(sys.argv[2:])
'''
    with (tmp_path / 'server.log').open('w') as log:
        process = subprocess.Popen([sys.executable, '-c', code, str(trace), '--library', str(library.store.root),
            'serve', '--installed-only', '--playback-only', '--host', '127.0.0.1', '--port', str(http_port),
            '--https-port', str(https_port)], cwd=tmp_path, env={**os.environ, 'PYTHONPATH': str(ROOT)}, stdout=log, stderr=log)
        try:
            http = f'http://127.0.0.1:{http_port}'
            https = f'https://127.0.0.1:{https_port}'
            deadline = time.monotonic() + 15
            while True:
                try:
                    with urlopen(http + '/api/library/catalog', timeout=0.5) as response:
                        plain_catalog = response.read()
                    break
                except (OSError, URLError):
                    if time.monotonic() > deadline or process.poll() is not None:
                        pytest.fail((tmp_path / 'server.log').read_text())
                    time.sleep(0.05)
            cert, = (library.store.state / 'tls').glob('*.crt')
            context = ssl.create_default_context(cafile=str(cert))
            with urlopen(https + '/api/library/catalog', context=context, timeout=3) as response:
                assert response.read() == plain_catalog
            assert trace.read_text() == 'start\n'
            for base in (http, https):
                with urlopen(base + '/test-shared-state', context=context, timeout=3) as response:
                    assert json.load(response) == {'token': 'fixture'}
                with urlopen(base + '/api/library/lectures/music:001000', context=context, timeout=3) as response:
                    row = json.load(response)
                segment = row['recordings'][0]['segments'][0]['url']
                with urlopen(Request(base + segment, headers={'Range': 'bytes=0-31'}), context=context, timeout=3) as response:
                    assert response.status == 206 and response.read().startswith(b'RIFF')
                with urlopen(base + '/library-assets/player.mjs', context=context, timeout=3) as response:
                    assert response.status == 200
            preview = json.dumps({'selection': {'packs': ['music']}, 'preview': True}).encode()
            for origin, expected in ((https, 200), (http, 403)):
                request = Request(https + '/api/library/deployment', data=preview,
                                  headers={'Content-Type': 'application/json', 'Origin': origin})
                if expected == 200:
                    with urlopen(request, context=context, timeout=3) as response:
                        assert response.status == 200
                else:
                    with pytest.raises(HTTPError) as error:
                        urlopen(request, context=context, timeout=3)
                    assert error.value.code == 403
                    error.value.close()
            request = Request(https + '/api/listeners', data=json.dumps({'name':'Fixture listener'}).encode(),
                              headers={'Content-Type':'application/json', 'Origin':https})
            with urlopen(request, context=context, timeout=3) as response:
                assert response.status < 300
            with urlopen(http + '/api/listeners', timeout=3) as response:
                assert json.load(response)['profiles'][0]['name'] == 'Fixture listener'
        finally:
            process.terminate()
            try:
                process.wait(timeout=8)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        assert process.returncode == 0, (tmp_path / 'server.log').read_text()
        assert trace.read_text() == 'start\nstop\n'


def test_second_port_conflict_does_not_start_lifespan_or_leave_http_bound(tmp_path):
    from contextlib import asynccontextmanager
    from starlette.applications import Starlette
    @asynccontextmanager
    async def lifespan(app):
        pytest.fail('Started the app before reserving both ports')
        yield
    cert, key = certificate_files(tmp_path, '127.0.0.1')
    with closing(socket.socket()) as occupied:
        occupied.bind(('127.0.0.1', 0))
        occupied.listen()
        http_port = free_port()
        with pytest.raises(SystemExit):
            run_http_https(Starlette(lifespan=lifespan), host='127.0.0.1', port=http_port,
                           https_port=occupied.getsockname()[1], certfile=cert, keyfile=key)
    with closing(socket.socket()) as available:
        available.bind(('127.0.0.1', http_port))
