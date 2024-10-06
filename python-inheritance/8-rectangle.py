#!/usr/bin/python3
"""Module 8-rectangle: define class rectaangle inherits from basegeometry"""


class BaseGeometry:
    """BaseGeometry is a base class for geometric shapes"""

    def area(self):
        """raise an Exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize rectangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
