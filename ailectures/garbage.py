"""Preview and explicitly collect stale audio, keeping recent text and references."""
import json
from pathlib import Path
import shutil
import sqlite3
import time
from uuid import uuid4

from .core import Conflict, digest, read_json, write_json
from .maintenance import media_lock
from .narration import speech_cache_key
from .voice_profiles import profile_cache_key
from .source_snapshots import SCHEMA, expand_snapshot


def readonly(path):
    db = sqlite3.connect(Path(path).resolve().as_uri()+'?mode=ro',uri=True)
    db.row_factory = sqlite3.Row
    return db


def directory_facts(path):
    files = []
    for item in [path,*sorted(path.rglob('*'))]:
        if item.is_symlink(): raise ValueError('Linked directories are excluded from cleanup')
        stat = item.stat()
        files.append((str(item.relative_to(path)),stat.st_size,stat.st_mtime_ns,stat.st_ino))
    return dict(bytes=sum(item.stat().st_size for item in path.rglob('*') if item.is_file()),
                modified=max(row[2] for row in files)/1e9, fingerprint=digest(files))


def scan_stage(items, report_progress, stage, total=None):
    if report_progress is None:
        yield from items
        return

    report_progress(stage, 0, total)
    checked = last_checked = 0
    next_update = time.monotonic() + 0.25
    for checked, item in enumerate(items, 1):
        yield item
        now = time.monotonic()
        if now >= next_update:
            report_progress(stage, checked, total)
            last_checked = checked
            next_update = now + 0.25
    if checked != last_checked:
        report_progress(stage, checked, total)


def retain_source_history(db, hashes, referenced, keep_text_versions, report_progress):
    protected = set(referenced)
    pending = set(hashes) if keep_text_versions > 1 else set()
    if not pending and not referenced:
        return protected

    # Keep only the text hashes for shared rows. A library may have thousands
    # of snapshots of largely the same catalog, plus older inline snapshots.
    shared_hashes = {}
    total = None
    if pending:
        if report_progress is not None:
            total = db.execute('SELECT count(*) FROM source_snapshots').fetchone()[0]
        snapshots = db.execute(
            'SELECT release,catalog FROM source_snapshots ORDER BY rowid DESC'
        )
    else:
        snapshots = (
            row
            for release in referenced
            for row in db.execute(
                'SELECT release,catalog FROM source_snapshots WHERE release=?',
                (release,),
            )
        )
    for snapshot in scan_stage(snapshots, report_progress, 'snapshots', total):
        release, raw = snapshot
        if release in referenced:
            for row in expand_snapshot(db, raw).values():
                for rec in row.get('recordings', []):
                    if rec.get('_release'):
                        protected.add(rec['_release'])
                    protected.update(
                        segment['_release'] for segment in rec['segments'] if segment.get('_release')
                    )
        if not pending:
            continue
        catalog = json.loads(raw)
        shared = catalog.get('_schema') == SCHEMA
        rows = catalog['lectures'] if shared else catalog
        for key in pending.intersection(rows):
            row = rows[key]
            if shared:
                identity = row['row']
                if identity not in shared_hashes:
                    stored = db.execute(
                        "SELECT json_extract(document, '$.spoken_sha256') "
                        'FROM source_snapshot_rows WHERE id=?',
                        (identity,),
                    ).fetchone()
                    if stored is None:
                        raise ValueError('Historical lecture row is missing')
                    shared_hashes[identity] = stored[0]
                spoken_hash = shared_hashes[identity]
            else:
                spoken_hash = row['spoken_sha256']
            if spoken_hash not in hashes[key]:
                hashes[key].append(spoken_hash)
                if len(hashes[key]) == keep_text_versions:
                    pending.remove(key)
    return protected


def garbage_plan(library, *, keep_days=30, keep_text_versions=2, report_progress=None):
    if type(keep_days) not in (int,float) or not 0 <= keep_days <= 36500: raise ValueError('keep_days must be 0–36500')
    if type(keep_text_versions) is not int or not 1 <= keep_text_versions <= 20: raise ValueError('keep_text_versions must be 1–20')
    if report_progress is not None:
        report_progress('catalog', 0, None)
    snapshot = library.snapshot(copy=False)
    current = snapshot['lectures']
    hashes = {key:[row['spoken_sha256']] for key,row in current.items()}
    referenced = set()
    # Historical audio named in progress or feedback remains reachable.
    if report_progress is not None:
        report_progress('references', 0, None)
    listener_db = library.store.state/'listeners.sqlite3'
    if listener_db.exists():
        with readonly(listener_db) as db:
            refs = [json.loads(row[0]) for row in db.execute('SELECT record FROM progress')]
            refs += [json.loads(row[0]) for row in db.execute('SELECT record FROM feedback_events')]
        for ref in refs:
            for field in ('release','pack_release'):
                release = ref.get(field)
                if not release: continue
                referenced.add(release)
    with library.store.connect() as db:
        protected = retain_source_history(db, hashes, referenced, keep_text_versions, report_progress)
    job_db = library.store.state/'production.sqlite3'
    jobs = []
    if job_db.exists():
        with readonly(job_db) as db: jobs = [dict(row) for row in db.execute('SELECT * FROM jobs')]
    active = [job for job in jobs if job['state'] in {'queued','running'}]
    for job in active:
        spec = json.loads(job['specification'])
        if base := spec.get('base_recording'): protected.add(base['release'])
        if job.get('published'): protected.add(job['published'])
    with library.store.connect() as db:
        for original, replacement in db.execute('SELECT original,replacement FROM release_aliases'):
            if original in protected:
                protected.add(replacement)
    def stale(rows):
        return bool(rows) and all(key in hashes and row['spoken_sha256'] not in hashes[key] for key,row in rows.items())
    candidates, retained = [], []
    cutoff = time.time()-keep_days*86400
    def consider(path, kind, **info):
        if not path.is_dir(): return
        try: facts = directory_facts(path)
        except (OSError,ValueError): return
        record = dict(kind=kind,path=str(path.relative_to(library.store.root)),**facts,**info)
        if facts['modified'] >= cutoff: retained.append(dict(record,reason='Within retention period'))
        else: candidates.append(record)
    stale_releases = set()
    with library.store.connect() as db:
        total = db.execute('SELECT count(*) FROM releases').fetchone()[0] if report_progress is not None else None
        releases = db.execute('SELECT release,pack_id,manifest,catalog FROM releases')
        for release in scan_stage(releases, report_progress, 'releases', total):
            release_id, pack_id, manifest, catalog = release
            if release_id in protected or json.loads(manifest).get('kind') != 'media':
                continue
            if not stale(json.loads(catalog)['lectures']):
                continue
            stale_releases.add(release_id)
            consider(library.store.packs/pack_id/release_id, 'media-release', release=release_id, pack_id=pack_id)
    exports = list((library.store.root/'exports').glob('*'))
    for path in scan_stage(exports, report_progress, 'exports', len(exports)):
        if path.is_dir() and (path/'pack.json').is_file():
            try:
                manifest = read_json(path/'pack.json')
                if manifest.get('kind')=='media' and manifest.get('release') in stale_releases:
                    consider(path,'export-copy')
            except (OSError,ValueError,KeyError): pass
    groups = {}
    for job in scan_stage(jobs, report_progress, 'generation', len(jobs)):
        spec = json.loads(job['specification'])
        row = spec.get('row',{})
        old = row.get('id') in hashes and row.get('spoken_sha256') not in hashes[row['id']]
        terminal = job['state'] not in {'queued','running'}
        if old and terminal: consider(library.store.root/'build-cache/generation'/job['id'],'generation-cache')
        if row.get('id') and 'configuration' in spec:
            key = (profile_cache_key(row['id'], spec['voice_profile'], spec.get('cache_epoch'))
                   if spec.get('voice_profile') else speech_cache_key(row['id'],spec['configuration']))
            groups.setdefault(key,[]).append(old and terminal)
    for key, eligible in scan_stage(groups.items(), report_progress, 'speech', len(groups)):
        if all(eligible): consider(library.store.root/'build-cache/speech'/key,'speech-cache')
    if report_progress is not None:
        report_progress('finalizing', 0, None)
    candidates.sort(key=lambda row:row['path'])
    policy = dict(keep_days=keep_days,keep_text_versions=keep_text_versions)
    return dict(schema_version=1,policy=policy,plan_id=digest(dict(policy=policy,candidates=candidates)),
                candidates=candidates,bytes=sum(row['bytes'] for row in candidates),retained_recent=retained,
                active_jobs=len(active),protected_releases=len(protected),
                notes=['Only stale, known lecture speech is eligible. Current and recent text, referenced historical audio, source packs, and mixed/shared speech caches are retained.',
                       'Apply requires stopped readers/exporters and no queued or running preparation jobs. No files have been removed by this preview.'])


def recover_garbage(library):
    """Finish committed deletions or restore pre-commit moves after interruption."""
    recovered = []
    for trash in library.store.root.glob('.gc-*'):
        journal = library.store.state/'gc-receipts'/(trash.name[4:]+'.json')
        if not journal.is_file(): raise ValueError('Unrecognized cleanup staging directory; inspect '+str(trash))
        receipt = read_json(journal)
        with library.store.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS gc_runs (id TEXT PRIMARY KEY)')
            committed = db.execute('SELECT 1 FROM gc_runs WHERE id=?',(receipt['id'],)).fetchone()
        if not committed:
            for index,relative in enumerate(receipt['paths']):
                from .core import contained
                source = contained(library.store.root,relative)
                moved = trash/str(index)
                if moved.exists():
                    if source.exists(): raise Conflict('Cleanup recovery would overwrite '+relative)
                    moved.rename(source)
        shutil.rmtree(trash)
        recovered.append(dict(id=receipt['id'],action='deleted' if committed else 'restored'))
    return recovered


def collect_garbage(library, plan_id, **policy):
    with media_lock(library.store.root,exclusive=True):
        recover_garbage(library)
        plan = garbage_plan(library,**policy)
        if plan['active_jobs']: raise ValueError('Finish or cancel queued/running generation jobs before cleanup')
        if plan['plan_id'] != plan_id: raise Conflict('Cleanup preview changed; review a fresh plan before applying')
        ticket = uuid4().hex
        trash = library.store.root/('.gc-'+ticket); trash.mkdir()
        moved = []
        receipt = dict(id=ticket,plan_id=plan_id,removed=len(plan['candidates']),bytes=plan['bytes'],paths=[item['path'] for item in plan['candidates']])
        write_json(library.store.state/'gc-receipts'/f'{ticket}.json',receipt)
        with library.store.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS gc_runs (id TEXT PRIMARY KEY)')
        try:
            with library.store.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                for index, item in enumerate(plan['candidates']):
                    source = library.store.root/item['path']
                    if directory_facts(source)['fingerprint'] != item['fingerprint']: raise Conflict('Audio changed since cleanup preview')
                    destination = trash/str(index)
                    source.rename(destination); moved.append((source,destination))
                    if item['kind']=='media-release':
                        db.execute('DELETE FROM selections WHERE release=?',(item['release'],))
                        db.execute('DELETE FROM releases WHERE release=?',(item['release'],))
                db.execute('INSERT INTO gc_runs VALUES (?)',(ticket,))
                library.store.compose(library.store.active(db))
                library.store._write_lock(db)
        except BaseException:
            for source,destination in reversed(moved): destination.rename(source)
            trash.rmdir()
            raise
        shutil.rmtree(trash)
        return receipt
