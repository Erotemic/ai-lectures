"""An offline maintenance barrier shared by servers, exports and cleanup."""
from contextlib import contextmanager
from pathlib import Path
import fcntl


@contextmanager
def media_lock(root, *, exclusive=False):
    state = Path(root)/'state'; state.mkdir(parents=True,exist_ok=True)
    with (state/'media.lock').open('a+b') as stream:
        try:
            fcntl.flock(stream, (fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH) | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Media cleanup requires the reader and export/preparation commands to be stopped') from None
        try: yield
        finally: fcntl.flock(stream,fcntl.LOCK_UN)


def media_operation(function):
    from functools import wraps
    @wraps(function)
    def guarded(library, *args, **kwargs):
        root = library.store.root if hasattr(library, 'store') else library.root
        with media_lock(root):
            return function(library,*args,**kwargs)
    return guarded
