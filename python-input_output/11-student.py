#!/usr/bin/python3
"""Module 11-student: Define Student to disk and reload"""


class Student:
    """Class that defines a student wwith first name , last name, age"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name , last name , age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictonary representation of a student instance"""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace all atributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
