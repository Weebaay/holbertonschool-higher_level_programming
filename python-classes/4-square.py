#!/usr/bin/python3
"""
    Module 4-square: Define getter and setter for size attribute
    in Square class
    """


class Square:
    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square (must be >= 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def __str__(self):
        """string of square"""
        return "Square of size {}".format(self.__size)

    def __repr__(self):
        """ Square"""
        return "Square({})".format(self.__size)
