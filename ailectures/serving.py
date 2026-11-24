"""Serve HTTP and optional HTTPS from one app, event loop and lifespan."""
from contextlib import ExitStack, contextmanager, nullcontext
import asyncio
import ipaddress
import logging
from pathlib import Path
import shutil
import signal
import ssl
import subprocess
import tempfile

from .core import digest


@contextmanager
def quiet_catalog_polls():
    """Keep routine catalog revalidations out of the server access log."""
    def keep_access_record(record):
        args = record.args
        if not isinstance(args, tuple) or len(args) != 5:
            return True
        _, method, path, _, status = args
        return not (method == 'GET' and status == 304 and isinstance(path, str)
                    and path.partition('?')[0] == '/api/library/catalog')

    logger = logging.getLogger('uvicorn.access')
    logger.addFilter(keep_access_record)
    try:
        yield
    finally:
        logger.removeFilter(keep_access_record)


def certificate_files(root, host, *, certfile=None, keyfile=None, names=()):
    if bool(certfile) != bool(keyfile):
        raise ValueError('HTTPS requires both --ssl-certfile and --ssl-keyfile')
    if certfile:
        certfile, keyfile = Path(certfile), Path(keyfile)
    else:
        identities = {'localhost', '127.0.0.1', '::1', *names}
        if host not in {'0.0.0.0', '::', '[::]'}:
            identities.add(host.strip('[]'))
        alternatives = []
        for identity in sorted(identities):
            try:
                alternatives.append('IP:' + str(ipaddress.ip_address(identity)))
            except ValueError:
                import re
                if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9.-]*', identity):
                    raise ValueError('Use a hostname or IP address for --https-name')
                alternatives.append('DNS:' + identity)
        folder = Path(root) / 'state' / 'tls'
        folder.mkdir(parents=True, exist_ok=True, mode=0o700)
        identity = digest(alternatives)[:16]
        certfile, keyfile = folder / (identity + '.crt'), folder / (identity + '.key')
        if not certfile.exists() or not keyfile.exists():
            if not shutil.which('openssl'):
                raise ValueError('Generating a self-signed certificate needs openssl; alternatively provide --ssl-certfile and --ssl-keyfile')
            with tempfile.TemporaryDirectory(prefix='.certificate-', dir=folder) as temporary:
                cert, key = Path(temporary) / 'cert.pem', Path(temporary) / 'key.pem'
                result = subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes',
                    '-keyout', str(key), '-out', str(cert), '-days', '365',
                    '-subj', '/CN=AI Lectures local server', '-addext', 'subjectAltName=' + ','.join(alternatives)],
                    capture_output=True, text=True)
                if result.returncode:
                    raise ValueError('Could not generate the local HTTPS certificate; provide a certificate/key pair instead')
                key.chmod(0o600)
                key.replace(keyfile)
                cert.replace(certfile)
    # Validate the pair before binding either port or starting background jobs.
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)
    return certfile, keyfile


async def serve_listeners(app, servers, sockets):
    previous = {}
    def stop(signum, frame):
        for server in servers:
            server.handle_exit(signum, frame)
    try:
        for sig in (signal.SIGINT, signal.SIGTERM):
            previous[sig] = signal.signal(sig, stop)
        # Uvicorn lifespan is disabled per listener so this runs exactly once.
        async with app.router.lifespan_context(app) as state:
            for server in servers:
                server.shared_state = state or {}
            tasks = [asyncio.create_task(server.serve(sockets=[sock]))
                     for server, sock in zip(servers, sockets)]
            try:
                done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                for task in done:
                    task.result()
            finally:
                for server in servers:
                    server.should_exit = True
                await asyncio.gather(*tasks, return_exceptions=True)
    finally:
        for sig, handler in previous.items():
            signal.signal(sig, handler)


def run_http_https(app, *, host, port, https_port, certfile, keyfile):
    import uvicorn
    if not 0 <= port <= 65535 or not 0 <= https_port <= 65535:
        raise ValueError('Listener ports must be between 0 and 65535')
    if port == https_port and port != 0:
        raise ValueError('HTTP and HTTPS need different ports')
    class Listener(uvicorn.Server):
        def capture_signals(self):
            return nullcontext()  # The shared coordinator handles both listeners.
        async def startup(self, sockets=None):
            self.lifespan.state.update(self.shared_state)
            await super().startup(sockets=sockets)
    configs = [uvicorn.Config(app, host=host, port=port, lifespan='off', loop='asyncio'),
               uvicorn.Config(app, host=host, port=https_port, lifespan='off', loop='asyncio',
                              ssl_certfile=str(certfile), ssl_keyfile=str(keyfile))]
    with ExitStack() as cleanup:
        sockets, servers = [], []
        for config in configs:
            config.load()
            sock = config.bind_socket()
            cleanup.callback(sock.close)
            sockets.append(sock)
            server = Listener(config)
            servers.append(server)
        asyncio.run(serve_listeners(app, servers, sockets))
