#!/usr/bin/python3
"""Module 3-is_kind_of_class : Define same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """return true if the object is an instance of , or if the object
    is an instance of a a class that inherited from,
    the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
