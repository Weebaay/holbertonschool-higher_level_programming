#!/usr/bin/python3
"""Module 9-rectangle: define a square is a rectangle"""


class Rectangle:
    """
    class reprenting a rectangle

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        rect_str = "\n".join([str(self.print_symbol) * self.__width for _ in
                              range(self.__height)])
        return rect_str

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rect_1 if both have the same aera value"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with
        width and height equal to size"""
        return cls(size, size)
