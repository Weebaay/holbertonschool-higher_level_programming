#!/usr/bin/python3
"""Module 2-square: Define size validation in square class"""


class Square:
    """
    A class used to represent a Square.

    This class includes a private instance attribute `size`
    to represent the size of the square.
    It also provides a method to compute the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

        def area(self):
            """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
            return self.__size ** 2
