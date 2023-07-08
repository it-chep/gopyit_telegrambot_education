
# pip install redis
import redis

from django.core.cache.backends.base import BaseCache


class RedisCache(BaseCache):

    def __init__(self, server, params):
        super().__init__(params)
        self.server = server
        self.client = redis.StrictRedis.from_url(self.server)

    def get(self, key, default=None, version=None):
        try:
            val = self.client.get(key).decode()
        except:
            val = self.client.get(key)
        if val is None:
            return default
        return val

    def set(self, key, value, timeout=None, version=None):
        if timeout is None:
            timeout = self.default_timeout
        try:
            return self.client.set(key, value.encode(), timeout)
        except:
            return self.client.set(key, value, timeout)

    def delete(self, key, version=None):
        self.client.delete(key)

    # def hset(self, table, key, value):
    #     return self.client.hset(table, key, value)
    #
    # def hget(self, table, key):
    #     result = self.client.hget(table, key)
    #     if result is not None:
    #         return result.decode()
    #     return None
