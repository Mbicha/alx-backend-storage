#!/usr/bin/env python3
""" Insert data into a document """

def insert_school(mongo_collection, **kwargs):
    """
    Args:
        mongo_collection - Document to store data
        kwargs - Dictionary elements to store
    Return:
        id of entered data
    """
    sch = mongo_collection.insert_one(kwargs)
    return [sch.inserted_id]
