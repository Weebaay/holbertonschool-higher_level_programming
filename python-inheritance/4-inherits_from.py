#!/usr/bin/python3
"""Module 4-inherits_from: Define object is an instance of a class that
inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited"""
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
