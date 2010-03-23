import datetime
from base import BaseBackend
from pyres import ResQ
class RedisBackend(BaseBackend):
    def save(self, resq=None):
        if not resq:
            resq = ResQ()
        data = {
            'failed_at' : str(datetime.datetime.now()),
            'payload'   : self._payload,
            'error'     : self._parse_message(self._exception),
            'backtrace' : self._parse_traceback(self._traceback),
            'queue'     : self._queue
        }
        if self._worker:
            data['worker'] = self._worker
        data = ResQ.encode(data)
        resq.redis.rpush('resque:failed', data)
    
    @classmethod
    def count(cls, resq):
        return int(resq.redis.llen('resque:failed'))

    @classmethod
    def all(cls, resq, start=0, count=1):
        from base64 import b64encode
        items = resq.redis.lrange('resque:failed', start, count) or []
        ret_list = []
        for i in items:
            failure = ResQ.decode(i)
            failure['redis_value'] = b64encode(i)
            ret_list.append(failure)
        return ret_list

    @classmethod
    def clear(cls, resq):
        return resq.redis.delete('resque:failed')
    
