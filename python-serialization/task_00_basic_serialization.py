#!/usr/bin/python3
"""Module task__00_basic_serialization : Define basic serialization"""


import json


def serialize_and_save_to_file(data, filename):
    """serializz a python dictionary and save in file JSON"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Move file json and deserialize in python dictionary"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
