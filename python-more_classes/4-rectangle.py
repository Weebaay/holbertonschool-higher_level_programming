#!/usr/bin/python3
"""Module 4-rectangle: define return a string reprensation of the rectangle
    to be able to recreate new instance by using eval"""


class Rectangle:
    """
    class reprenting a rectangle

    atribute :
    __width: width of rectangle
    __height: height of rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle instance"""
        self.__heigth = height
        self.__width = width

    @property
    def width(self):
        """
        get the width of rectangle

        Returns:
            int: the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """


        Args:
            value (int): the width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the height of rectangle

        Returns:
            int : the height of rectangle
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """
        args:
        value (int): the height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__heigth

    def perimeter(self):
        """Compute the perimeter of rectangle"""
        if self.__width == 0 or self.__heigth == 0:
            return 0
        return 2 * (self.__width + self.__heigth)

    def __str__(self):
        """return a string representaion of the regtangle using the '#'"""
        if self.__width == 0 or self.__heigth == 0:
            return ""
        str_rectangle = ""
        for i in range(self.__heigth):
            str_rectangle += "#" * self.__width
            if i != self.__heigth - 1:
                str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """
        Return a string representation that can recreate the object
        using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__heigth)
