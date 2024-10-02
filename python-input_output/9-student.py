#!/usr/bin/python3
"""Module 9-student: Define student to JSON"""


class Student:
    """Class that defines a student wwith first name , last name, age"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name , last name , age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary reprensentation of the student instance"""
        return self.__dict__
