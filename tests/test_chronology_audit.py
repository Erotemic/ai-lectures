"""Source audits distinguish date meanings and tolerate missing optional dates."""
import json
from tools.audit_chronology import audit


def test_audit_canonicalizes_aliases_and_reports_missing_records(tmp_path):
    folder = tmp_path / 'content' / 'example'
    (folder / 'metadata').mkdir(parents=True)
    (folder / 'track.json').write_text(json.dumps(dict(id='example', lectures=[
        dict(id='001000', title='A story'), dict(id='002000', title='A lesson'),
        dict(id='003000', title='A history')])))
    (folder / 'metadata/001000.json').write_text(json.dumps(dict(chronology={
        'fictional_setting': dict(start=-500), 'work': dict(start=1900)})))
    (folder / 'metadata/003000.json').write_text(json.dumps(dict(chronology={
        'context': dict(start=1500), 'setting': dict(start=0)})))
    report = audit(tmp_path)
    assert report['lectures'] == 3
    assert report['dated'] == dict(work=1, setting=1, context=1)
    rows = {row['id']: row for row in report['items']}
    assert 'setting' not in rows['example:001000']['missing_axes']
    assert 'setting' in rows['example:003000']['missing_axes']
    assert not rows['example:002000']['dated_axes']
    assert report['packs'][0]['lectures'] == 3
