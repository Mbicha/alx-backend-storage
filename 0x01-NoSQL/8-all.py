#!/usr/bin/env python3
""" List all documents """

def list_all(mongo_collection) -> list:
    """
    Args:
        mongo_collection (collections) - collections of a database
    Return:
        Empty list if None and List of collection if not none
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)
    
    return documents
