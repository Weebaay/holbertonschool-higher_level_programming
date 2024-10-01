#!/usr/bin/python3
"""Module 5-save_to_json_file: Define Save object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file , using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
    	json.dump(my_obj, file)
