#!/usr/bin/python3*
"""Module 8-class_to_json : Define class to json"""



def class_to_json(obj):
    """return the dictionary description with simple data structure
    for JSON serialization of object"""
    return obj.__dict__
    