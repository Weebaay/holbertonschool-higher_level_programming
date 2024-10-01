#!/usr/bin/python3
"""Module 4-from_json_string: define From Json string to objet"""

import json


def from_json_string(my_str):
    """return object python reprented by a JSON string"""
    return json.loads(my_str)
