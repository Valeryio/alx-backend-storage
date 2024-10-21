#!/usr/bin/env python3

"""This module contains a function that insert into a nosql db
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """It insert into a collection a different elements
    """
    id = mongo_collection.insert_one(kwargs)
    return id
