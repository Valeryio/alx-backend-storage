#!/usr/bin/env python3

"""This script analyse log scripts
"""

from pymongo import MongoClient


# create the mongodb client
client = MongoClient("mongodb://localhost:27017")

# access to the logs database
db = client.logs

# getting the specific nginx collection
nginx_collection = db.nginx


requests = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
number_of_logs = nginx_collection.count_documents({})
number_of_check_status = nginx_collection.count_documents({"path": "/status"})

print(f"{number_of_logs} logs")
print("Methods:")

for i in requests:
    number_logs = nginx_collection.count_documents({"method": i})
    print(f"\tmethod {i}: {number_logs}")

print(f"{number_of_check_status} status check")
print("IPs:")
pipeline = [
        {
            "$group": {"_id": "$ip", "count": {"$sum": 1}}
            },
        {
            "$sort": {"count": -1}
            },
        {
            "$limit": 10
            }]

new_ips = nginx_collection.aggregate(pipeline)

for result in new_ips:
    print(f"\t{result['_id']}: {result['count']}")
