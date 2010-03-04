import sys
import traceback

class BaseBackend(object):
    def __init__(self, exp, queue, payload, worker=None):
        excc, _, tb = sys.exc_info()
        
        self._exception = excc
        self._traceback = traceback.format_exc()
        self._worker = worker
        self._queue = queue
        self._payload = payload
    
    
    def _parse_traceback(self, trace):
        """Return the given traceback string formatted for a notification."""
        return trace
    
    def _parse_message(self, exc):
        """Return a message for a notification from the given exception."""
        return '%s: %s' % (exc.__class__.__name__, str(exc))
    