#!/usr/bin/python3
""" Module 3-square: Define area method to square class"""


class Square:
    """
    A class that defines a square with size validation.

    Methods:
        __init__(self, size=0): Initializes with size.
        area(self): Returns the area of the square.
        size(self): Retrieves the size.
        size(self, value): Sets the size with validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
