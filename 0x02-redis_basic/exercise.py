#!/usr/bin/env python3

"""This is a simple exercice on redis database
"""
import uuid
import redis


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

    def store(self, data: int | str | float | bytes):
        """method to store a data
        param: data
        return: a string
        """
        # generate a random uuid
        random_key: str = uuid.uuid1().__str__()
        self.redis.set(str(random_key), data)
        return random_key
