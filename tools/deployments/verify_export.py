"""Verify a curated export folder or ZIP using only the Python standard library."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from zipfile import ZipFile


def verify(path):
    path = Path(path)
    archive = ZipFile(path) if path.is_file() else None
    try:
        def read(name):
            relative = PurePosixPath(name)
            if relative.is_absolute() or '..' in relative.parts or '\\' in name:
                raise ValueError('Invalid export path')
            return archive.open(name) if archive else (path / name).open('rb')
        with read('manifest.json') as stream:
            manifest = json.load(stream)
        if manifest.get('schema_version') != 1:
            raise ValueError('Unsupported curated export manifest')
        if archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != {'manifest.json', *manifest['files']}:
                raise ValueError('Export contains unexpected or duplicate files')
        for name, expected in manifest['files'].items():
            with read(name) as stream:
                actual = hashlib.file_digest(stream, 'sha256').hexdigest()
            if actual != expected['sha256']:
                raise ValueError('Export checksum mismatch: ' + name)
        return manifest
    finally:
        if archive:
            archive.close()


if __name__ == '__main__':
    try:
        result = verify(sys.argv[1] if len(sys.argv) > 1 else '.')
        print(f"Verified {result['export_id']}: {len(result['files'])} files; "
              f"{result['content']['complete']}/{result['content']['lectures']} lectures with complete audio")
    except (OSError, ValueError, KeyError) as error:
        sys.exit(str(error))
