#!/usr/bin/python3
"""Module 2-is_same_class: Define exact same object"""


def is_same_class(obj, a_class):
    """returns true if object is exactly instance of
    the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
