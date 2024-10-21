#!/usr/bin/env python3

"""This module contains a function that update a mongo db
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """It update a collection
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
