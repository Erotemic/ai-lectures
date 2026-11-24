"""Build a versioned handoff containing reader code, dependencies and selected content."""
import argparse
from datetime import datetime, timezone
from email.parser import BytesParser
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))
from ailectures.core import digest, file_digest, name, read_json, write_json
from ailectures.deployment import deployment_plan, export_deployment
from ailectures.library import Library


RUN_INSTRUCTIONS = '''# Curated lecture library

Install Python 3.11 or newer first. Unzip this folder and open Terminal here.
Verify the transfer before installing:

    python3 verify_export.py .

Create the reader environment and install its bundled dependencies offline:

    python3 -m venv .reader-env
    .reader-env/bin/python -m pip install --no-index --find-links wheelhouse ailectures-reader
    .reader-env/bin/python -m ailectures --library ./library restore ./content.zip
    .reader-env/bin/python -m ailectures --library ./library serve --installed-only --playback-only --port 18701

Open http://localhost:18701/ . Stop with Control-C. Next time, run only the last
command. Restore is only for a new library directory. Installation needs Python;
no TTS service, GPU, FFmpeg, internet access or production checkout is required.

manifest.json records this export's code, dependencies, checksums and audio
readiness. selection.json records the curator's intent. selection.lock.json
records the exact lecture IDs, text revisions and recordings actually shipped.
A draft export can have missing audio; inspect the manifest before handing it on.

reader-source/ contains the corresponding standalone server source distribution.
content.zip contains the chosen runtime packs: full source text, metadata,
reading-source records, filtered listening routes, supported companions and
published recordings. It is not an overlay of the original authoring checkout.
The original checkout revision is recorded in the manifest when available.
'''


def copy_reader(repository, destination):
    """Copy only package source/build inputs, never local databases or references."""
    source = Path(repository) / 'ailectures'
    files = sorted(source.glob('*.py')) + [source / 'pyproject.toml', source / 'README.md']
    files += sorted(p for p in (source / 'static').iterdir()
                    if p.suffix in {'.py', '.mjs', '.css', '.html', '.svg'})
    hashes = {}
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError('Reader source requires regular files: ' + path.name)
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        hashes[relative.as_posix()] = file_digest(target)
    return hashes


def build_reader(source, stage):
    distributions = stage / 'reader-source'
    subprocess.run(['uv', 'build', str(source), '--out-dir', str(distributions), '--no-build-logs'], check=True)
    wheel, = distributions.glob('*.whl')
    # The reader and its dependencies are pure Python. Resolve for the minimum
    # supported Python rather than accidentally selecting a 3.13-only dependency.
    subprocess.run([sys.executable, '-m', 'pip', 'download', '--disable-pip-version-check',
                    '--only-binary=:all:', '--platform', 'any', '--implementation', 'py',
                    '--abi', 'none', '--python-version', '3.11', '--dest', str(stage / 'wheelhouse'),
                    str(wheel)], check=True)
    wheel.unlink()  # The installable copy is now in wheelhouse/.


def content_lock(archive, expected_ids):
    lectures, releases = {}, {}
    with ZipFile(archive) as zipped:
        for path in zipped.namelist():
            parts = path.split('/')
            if len(parts) != 4 or parts[0] != 'packs' or parts[-1] != 'catalog.json':
                continue
            catalog = json.loads(zipped.read(path))
            releases[parts[1]] = parts[2]
            for key, row in catalog['lectures'].items():
                if key in lectures:
                    raise ValueError('Duplicate lecture in curated export: ' + key)
                lectures[key] = dict(revision=row['revision'], spoken_sha256=row['spoken_sha256'],
                    document_sha256=digest(row), recordings=[dict(id=r['id'], complete=r['complete'],
                        segments=[dict(index=s['index'], sha256=s['sha256']) for s in r['segments']])
                        for r in row['recordings']])
    if set(lectures) != set(expected_ids):
        raise ValueError('Selected lecture membership changed while exporting; retry')
    return dict(schema_version=1, selection=dict(lectures=sorted(lectures)), lectures=lectures, releases=releases)


def build_handoff(library, repository, selection, output, *, export_id, allow_incomplete=False, locked_selection=None):
    name(export_id)
    repository, output = Path(repository).resolve(), Path(output).resolve()
    receipt_path = output.with_suffix('.receipt.json')
    if output.exists() or receipt_path.exists():
        raise FileExistsError(output)
    if locked_selection is not None:
        if locked_selection.get('schema_version') != 1 or not isinstance(locked_selection.get('lectures'), dict):
            raise ValueError('Unsupported selection lock')
        selection = locked_selection['selection']
    # Check readiness before building code or resolving dependencies.
    plan = deployment_plan(library, selection)
    if not allow_incomplete and plan['complete'] != plan['lectures']:
        raise ValueError(f"Complete audio required: {plan['complete']}/{plan['lectures']} ready; use --allow-incomplete only for a draft")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.curated-', dir=output.parent) as temporary:
        temporary = Path(temporary)
        stage, source = temporary / 'handoff', temporary / 'reader'
        stage.mkdir()
        source_hashes = copy_reader(repository, source)
        build_reader(source, stage)
        # Resolve selectors once. New lectures added during packaging cannot
        # silently enter this release through a growing pack or collection.
        frozen = dict(lectures=plan['lecture_ids'])
        receipt = export_deployment(library, frozen, stage / 'content.zip', require_complete=not allow_incomplete)
        lock = content_lock(stage / 'content.zip', plan['lecture_ids'])
        if locked_selection is not None and lock['lectures'] != locked_selection['lectures']:
            raise ValueError('Selected text, metadata or recordings differ from the lock; retain the earlier export or create a new curation revision')
        write_json(stage / 'selection.json', selection)
        write_json(stage / 'selection.lock.json', lock)
        (stage / 'README.md').write_text(RUN_INSTRUCTIONS, encoding='utf-8')
        shutil.copyfile(Path(__file__).with_name('verify_export.py'), stage / 'verify_export.py')
        # Include the producer so the procedure is versioned with the artifact.
        shutil.copyfile(__file__, stage / 'export_curated.py')
        versions = []
        for wheel in sorted((stage / 'wheelhouse').glob('*.whl')):
            if not wheel.name.endswith('-none-any.whl'):
                raise ValueError('A standalone Mac handoff requires portable pure-Python wheels')
            with ZipFile(wheel) as zipped:
                metadata, = (p for p in zipped.namelist() if p.endswith('.dist-info/METADATA'))
                package = BytesParser().parsebytes(zipped.read(metadata))
                versions.append(dict(name=package['Name'], version=package['Version'], wheel=wheel.name))
        git = subprocess.run(['git', '-C', str(repository), 'rev-parse', 'HEAD'], capture_output=True, text=True)
        manifest = dict(schema_version=1, export_id=export_id,
            created_at=datetime.now(timezone.utc).isoformat(),
            status='draft' if receipt['complete'] != receipt['lectures'] else 'audio-complete',
            source_commit=git.stdout.strip() if git.returncode == 0 else None,
            reader_source=dict(sha256=digest(source_hashes), files=source_hashes),
            python_minimum='3.11', packages=versions,
            content={key:receipt[key] for key in ('lectures', 'complete', 'partial', 'missing', 'recordings', 'namespaces')},
            files={p.relative_to(stage).as_posix():dict(sha256=file_digest(p), bytes=p.stat().st_size)
                   for p in sorted(stage.rglob('*')) if p.is_file()})
        write_json(stage / 'manifest.json', manifest)
        archive = temporary / 'handoff.zip'
        with ZipFile(archive, 'x', compression=ZIP_DEFLATED, allowZip64=True) as zipped:
            for path in sorted(stage.rglob('*')):
                if path.is_file():
                    zipped.write(path, path.relative_to(stage).as_posix())
        # Verification is independent of the reader and never imports production.
        subprocess.run([sys.executable, str(stage / 'verify_export.py'), str(archive)], check=True)
        os.rename(archive, output)
    result = dict(export_id=export_id, path=str(output), sha256=file_digest(output), bytes=output.stat().st_size,
                  status=manifest['status'], reader_source_sha256=manifest['reader_source']['sha256'],
                  source_commit=manifest['source_commit'], **manifest['content'])
    write_json(receipt_path, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, default=REPOSITORY)
    parser.add_argument('--library', type=Path, default=Path('library-data'))
    selectors = parser.add_mutually_exclusive_group(required=True)
    selectors.add_argument('--selection', type=Path)
    selectors.add_argument('--locked-selection', type=Path, help='Replay exact content identities from an earlier selection.lock.json')
    parser.add_argument('--export-id', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    try:
        lock = read_json(args.locked_selection) if args.locked_selection else None
        result = build_handoff(Library(args.library, repository=args.repository), args.repository,
                               read_json(args.selection) if args.selection else lock['selection'],
                               args.output, export_id=args.export_id,
                               allow_incomplete=args.allow_incomplete, locked_selection=lock)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
