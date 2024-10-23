#!/usr/bin/env python3

"""This is a simple exercice on redis database
"""
import uuid
import redis
from collections.abc import Callable


class Cache:

    def __init__(self):
        self._redis = redis.Redis(host="localhost")
        self._redis.flushdb()

    @property
    def redis(self):
        return self._redis

    @redis.setter
    def redis(self, redis_instance):
        self._redis = redis_instance

    def get(self, key: str, fn: Callable = None):
        try:
            result = self.redis.get(key)
            if isinstance(fn, int):
                return self.get_int(key)
            elif isinstance(fn, str):
                return self.get_str(key)
            else:
                return result
        except AssertionError:
            pass

    def get_str(self, key: str):
        return str(self.redis.get(key))

    def get_int(self, key: str):
        return int(self.redis.get(key))

    def store(self, data):
        """method to store a data
        param: data
        return: a string
        """
        # generate a random uuid
        random_key = uuid.uuid1()
        self.redis.set(str(random_key), data)
        return str(random_key)
