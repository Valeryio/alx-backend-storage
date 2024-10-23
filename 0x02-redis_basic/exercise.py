#!/usr/bin/env python3

"""This is a simple exercice on redis database
"""
import uuid
import redis


class Cache:

    def __init__(self):
        self.redis = redis.Redis(host="localhost")
        self.redis.flushdb()

    @property
    def redis(self):
        return self._redis

    @redis.setter
    def redis(self, redis_instance):
        self._redis = redis_instance

    def store(self, data):
        """method to store a data
        param: data
        return: a string
        """
        # generate a random uuid
        random_key = uuid.uuid1()
        self.redis.set(str(random_key), data)
        return str(random_key)
