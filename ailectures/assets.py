"""Serve a consistent browser build, including its relative module imports."""

from hashlib import sha256
from pathlib import Path

from starlette.datastructures import Headers
from starlette.responses import HTMLResponse, Response
from starlette.staticfiles import StaticFiles

from .core import digest


class LibraryAssets(StaticFiles):
    def __init__(self, directory):
        super().__init__(directory=directory)
        self.files = {
            path.name: path.read_bytes()
            for path in Path(directory).iterdir()
            if path.suffix in {".mjs", ".css", ".html", ".svg"}
        }
        self.hashes = {
            name: sha256(data).hexdigest() for name, data in self.files.items()
        }
        self.version = digest(self.hashes)[:16]

    def document(self):
        html = (
            self.files["index.html"]
            .decode("utf-8")
            .replace("/library-assets/", f"/library-assets/{self.version}/")
        )
        return HTMLResponse(html, headers={"Cache-Control": "no-cache"})

    async def get_response(self, path, scope):
        if scope["method"] not in {"GET", "HEAD"}:
            return Response(status_code=405)
        prefix, separator, filename = path.partition("/")
        versioned = bool(separator)
        name = filename if versioned else path
        if (versioned and prefix != self.version) or name not in self.files:
            return Response(status_code=404)
        headers = {
            "Cache-Control": "public, max-age=31536000, immutable"
            if versioned
            else "no-cache",
            "ETag": '"' + self.hashes[name] + '"',
        }
        if Headers(scope=scope).get("if-none-match") == headers["ETag"]:
            return Response(status_code=304, headers=headers)
        headers["Content-Length"] = str(len(self.files[name]))
        media_type = (
            "text/css"
            if name.endswith(".css")
            else "text/html"
            if name.endswith(".html")
            else "image/svg+xml"
            if name.endswith(".svg")
            else "text/javascript"
        )
        return Response(
            self.files[name] if scope["method"] == "GET" else b"",
            media_type=media_type,
            headers=headers,
        )
