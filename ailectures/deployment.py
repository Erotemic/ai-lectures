"""Selected-content library bundles: published media and sources, no machine state."""
from copy import deepcopy
import json
from pathlib import Path
import os
import tempfile
from uuid import uuid4
from zipfile import ZipFile, ZIP_DEFLATED

from .maintenance import media_operation
from .core import contained, file_digest, write_json
from .discovery import discovery_fields
from .organization import item_organization
from .packs import PackStore, export_release

FIELDS = ('packs', 'collections', 'categories', 'tags', 'lectures')


def select_content(snapshot, selection):
    if not isinstance(selection, dict) or set(selection) - set(FIELDS):
        raise ValueError('Select packs, collections, categories, tags, or lecture IDs')
    criteria = {}
    for field in FIELDS:
        values = selection.get(field, [])
        if not isinstance(values, list) or not all(isinstance(v, str) and v.strip() for v in values):
            raise ValueError(f'{field} must be a list of labels or IDs')
        criteria[field] = set(values)
    if not any(criteria.values()):
        raise ValueError('Select at least one content group')
    rows, courses = snapshot['lectures'], snapshot['courses']
    known = dict(packs={p['id'] for p in snapshot['packs']}, collections=set(courses), lectures=set(rows), categories=set(), tags=set())
    facets = {}
    for key, row in rows.items():
        fields = item_organization(row, list(courses.values()))
        tags = set(fields['tags']) | {label for path in fields['tag_paths'] for label in path}
        facets[key] = set(fields['categories']), tags
        known['categories'].update(fields['categories']); known['tags'].update(tags)
    for field in FIELDS:
        if missing := criteria[field] - known[field]:
            raise ValueError(f'Unknown {field}: '+', '.join(sorted(missing)))
    selected = set(criteria['lectures'])
    for key in criteria['collections']:
        selected.update(lecture for lecture in courses[key]['lectures'] if lecture in rows)
    for key, row in rows.items():
        categories, tags = facets[key]
        if (row.get('origin', {}).get('pack') in criteria['packs']
                or key.split(':')[0] in criteria['packs']
                or categories & criteria['categories'] or tags & criteria['tags']):
            selected.add(key)
    if not selected:
        raise ValueError('No available lectures match this selection')
    return sorted(selected)


def deployment_plan(library, selection, *, snapshot=None):
    snapshot = snapshot or library.snapshot(copy=False)
    keys = select_content(snapshot, selection)
    rows = [snapshot['lectures'][key] for key in keys]
    complete = sum(any(rec['complete'] for rec in row['recordings']) for row in rows)
    partial = sum(bool(row['recordings']) and not any(rec['complete'] for rec in row['recordings']) for row in rows)
    return dict(selection=selection, lecture_ids=keys, lectures=len(keys), complete=complete, partial=partial,
                missing=len(keys)-complete-partial, recordings=sum(len(row['recordings']) for row in rows),
                namespaces=sorted({key.split(':')[0] for key in keys}))


def trim_course(course, selected, course_ids):
    result = deepcopy(course)
    def trim(node):
        if 'lectures' in node: node['lectures'] = [key for key in node['lectures'] if key in selected]
        for field in ('chapters', 'sessions'):
            if field in node:
                node[field] = [trim(child) for child in node[field]]
                node[field] = [child for child in node[field] if child.get('lectures') or child.get('chapters') or child.get('sessions')]
        return node
    trim(result)
    if 'children' in result: result['children'] = [key for key in result['children'] if key in course_ids]
    if result.get('parent') not in course_ids: result.pop('parent', None)
    if 'browse_sections' in result:
        for section in result['browse_sections']: section['collections'] = [key for key in section['collections'] if key in course_ids]
        result['browse_sections'] = [s for s in result['browse_sections'] if s['collections']]
    return result


@media_operation
def export_deployment(library, selection, output, *, title='Selected lecture library'):
    output = Path(output).resolve()
    if output.exists(): raise FileExistsError(output)
    if output.is_relative_to(library.store.packs) or output.is_relative_to(library.store.state):
        raise ValueError('Choose an output outside packs/ and state/')
    snapshot = library.snapshot(copy=False)
    plan = deployment_plan(library, selection, snapshot=snapshot)
    selected = set(plan['lecture_ids'])
    course_ids = {key for key, course in snapshot['courses'].items() if selected.intersection(course['lectures'])}
    courses = {key:trim_course(snapshot['courses'][key], selected, course_ids) for key in course_ids}
    namespaces = sorted(set(plan['namespaces']) | {key.split(':')[0] for key in courses})
    authored = library.repository.snapshot(copy=False) if library.repository else {}
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.deployment-', dir=output.parent) as temporary:
        stage = Path(temporary)
        target = PackStore(stage/'library')
        for namespace in namespaces:
            rows = {key:deepcopy(snapshot['lectures'][key]) for key in selected if key.split(':')[0] == namespace}
            media, extras = [], {}
            for key, row in rows.items():
                for rec in row['recordings']:
                    public = {k:deepcopy(v) for k,v in rec.items() if not k.startswith('_')}
                    files = {}
                    for original, segment in zip(rec['segments'], public['segments']):
                        release = original.get('_release', rec.get('_release'))
                        if not release: raise ValueError('Finish publishing recordings before exporting')
                        path, _ = library.store.media_file(release, original.get('_recording', rec['id']), segment['index'])
                        files[segment['path']] = path
                        for field in list(segment):
                            if field.startswith('_'): segment.pop(field)
                    media.append((key,public,files))
                for companion in row.get('companions', []):
                    if namespace in authored:
                        path, _ = library.repository.companion_file(key, companion['id'], companion['sha256'])
                    else:
                        origin = row['origin']
                        _, directory = library.store.historical(origin.get('pack_release',origin['release']),key)
                        path = contained(directory, companion['path'])
                        if file_digest(path) != companion['sha256']: raise ValueError('Companion changed while exporting')
                    extras[companion['path']] = path
            pack = dict(id=namespace,title=authored.get(namespace,{}).get('title') or next((p['title'] for p in snapshot['packs'] if p['id']==namespace),namespace),lectures=rows,
                        courses={key:course for key,course in courses.items() if key.split(':')[0]==namespace},
                        relationships=[r for r in snapshot['relationships'] if r['from'] in rows and r['to'] in selected],extra_files=extras)
            release = stage/('release-'+namespace)
            export_release(pack,release,media=media)
            # Authored companions can change independently while copying. Check
            # the staged bytes against the selected snapshot before publication.
            for row in rows.values():
                for companion in row.get('companions', []):
                    if file_digest(contained(release,companion['path'])) != companion['sha256']:
                        raise ValueError('Companion changed while exporting; retry the selection')
            target.install(release)
        write_json(target.root/'backup.json',dict(schema_version=1,warnings=[],deployment=dict(title=title,**plan)))
        archive = stage/'deployment.zip'
        with ZipFile(archive,'x',compression=ZIP_DEFLATED,allowZip64=True) as zipped:
            for path in sorted(target.root.rglob('*')):
                if path.is_file() and (path.relative_to(target.root).parts[0] in {'packs','state'} or path.name=='backup.json'):
                    zipped.write(path,path.relative_to(target.root).as_posix())
        os.rename(archive,output)
    return dict(**plan,path=str(output),bytes=output.stat().st_size,title=title)


def browser_deployment(library, selection, *, title='Selected lecture library'):
    ticket = uuid4().hex
    root = library.store.root/'exports'/ticket
    root.mkdir(parents=True)
    try:
        receipt = export_deployment(library,selection,root/'pack.zip',title=title)
        receipt.update(id=ticket,filename='lecture-library-'+ticket[:12]+'.zip')
        write_json(root/'receipt.json',receipt)
        return receipt
    except BaseException:
        import shutil
        shutil.rmtree(root)
        raise
