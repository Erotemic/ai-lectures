"""Plan and atomically enqueue declared content for saved rendering profiles."""
from .deployment import select_content


def selected_audio(snapshot, selection, *, all_audio=False):
    if all_audio:
        if any(selection.values()):
            raise ValueError('Use --all or explicit content selectors, not both')
        keys = sorted(key for key, row in snapshot['lectures'].items() if row.get('kind') == 'audio')
        if not keys:
            raise ValueError('No audio lectures are available')
    else:
        keys = select_content(snapshot, selection)
    if any(snapshot['lectures'][key].get('kind') != 'audio' for key in keys):
        raise ValueError('Select audio items; presentation rendering is a separate workflow')
    return keys


def resolve_profiles(catalog, selectors):
    result = {}
    for selector in selectors:
        matches = [p for p in catalog['profiles'] if p['id'] == selector]
        if not matches:
            matches = [p for p in catalog['profiles'] if p['label'].casefold() == selector.casefold()]
        if not matches:
            matches = [p for p in catalog['profiles'] if p['voice'] == selector]
        if not matches:
            raise ValueError(f'No saved profile matches {selector!r} as an ID, label or voice ID; run voices to list choices')
        if len(matches) > 1:
            candidates = '; '.join(f"{p['id']} ({p['label']})" for p in matches)
            raise ValueError(f'Saved voice profile {selector!r} is ambiguous; choose an exact profile ID: {candidates}')
        profile = matches[0]
        if not profile['available'] or profile['archived']:
            raise ValueError(f'Saved voice profile {selector!r} is unavailable')
        result[profile['id']] = profile
    if not result:
        raise ValueError('Choose at least one saved voice profile')
    return list(result.values())


def queue_audio(manager, selection, profiles, *, all_audio=False, dry_run=False):
    snapshot = manager.library.snapshot(copy=False)
    keys = selected_audio(snapshot, selection, all_audio=all_audio)
    voices = resolve_profiles(manager.profile_catalog(), profiles)
    requests, plans = [], []
    # Freeze and validate every recipe before writing any jobs. No engine,
    # network discovery, runtime capacity probe or synthesis starts here.
    for profile in voices:
        remaining = []
        for key in keys:
            row = snapshot['lectures'][key]
            prepared = any(recording['complete']
                and recording['spoken_sha256'] == row['spoken_sha256']
                and recording.get('generator', {}).get('profile') == profile['id']
                and recording['generator'].get('profile_revision') == profile['revision']
                for recording in row['recordings'])
            if not prepared:
                remaining.append(key)
        requests.extend(manager.saved_requests(remaining, profile['id'], profile_revision=profile['revision'], snapshot=snapshot))
        plans.append(dict(id=profile['id'], label=profile['label'], revision=profile['revision'],
                          voice=profile['voice'], complete=len(keys)-len(remaining), requested=len(remaining)))
    previous = manager.jobs.states()
    if not dry_run:
        manager.jobs.enqueue(requests, requeue_ready=True)
    jobs = [dict(id=key, lecture_id=spec['row']['id'], profile=spec['profile'],
                 profile_revision=spec['voice_profile']['revision'],
                 action='new' if key not in previous else 'reuse' if previous[key] in {'queued','running'} else 'retry')
            for key, spec in requests]
    return dict(dry_run=dry_run, lectures=len(keys), voices=len(voices),
                complete=sum(p['complete'] for p in plans), requested=len(requests),
                new=sum(job['action']=='new' for job in jobs),
                reused=sum(job['action']=='reuse' for job in jobs),
                retried=sum(job['action']=='retry' for job in jobs), profiles=plans, jobs=jobs)
