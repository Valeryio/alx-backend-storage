#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    school_collection.insert_one({"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]})
    school_collection.insert_many([{"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}])
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))