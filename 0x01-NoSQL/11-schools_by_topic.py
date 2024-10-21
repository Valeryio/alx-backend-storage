#!/usr/bin/env python3

"""This module contains a functino that update others
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """It returns the list of schools having
    a specific topic

    param: mongo_collection,
    param: topic
    return: A list
    """
    specific_schools = []
    all_schools = mongo_collection.find()

    for school in all_schools:
        for i in school["topics"]:
            if i == topic:
                specific_schools.append(school)
    return specific_schools
