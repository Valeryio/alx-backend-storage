#!/usr/bin/env python3

"""THis module list all the documents in a collection of mongo db"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """List all the documents in a collection

    param: mongo_collection
    return: A list
    """
    all_doc = []
    for doc in mongo_collection.find():
        all_doc.append(doc)
    return all_doc