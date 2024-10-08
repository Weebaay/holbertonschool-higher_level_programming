#!/usr/bin/python3
""" Module 6-rectangle: Define a Rectangle with instance counting""""


class Rectangle:
    """
    class reprenting a rectangle

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0, position=(0, 0)):
        """Initialize a new rectangle instance"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.__height

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
        self.__height = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return a string representaion of the regtangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation that can recreate the object
        using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of rectangle
    is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
