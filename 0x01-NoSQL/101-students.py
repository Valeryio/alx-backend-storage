#!/usr/bin/env python3

"""THis module contains a function that get the top student
from a mongodb"""


def top_students(mongo_collection):
    """compute the top student
    param: mongo_collection
    return: A list
    """
    students = mongo_collection.find()
    new_students = []
    for student in students:
        topics = student["topics"]
        average = 0
        for topic in topics:
            average += topic["score"]
        average = average / (len(topic) + 1)
        student["averageScore"] = average
        new_students.append(student)

    ordered_students = sorted(new_students, key=lambda x: x["averageScore"],
                              reverse=True)
    return ordered_students
