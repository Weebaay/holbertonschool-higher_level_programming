#!/usr/bin/python3
"""Module 1-Square: Define private size class square"""
class Square:
    """
    A class used to represent a Square.

    ...

    Attributes
    ----------
    size : int
        The size of one side of the square (private attribute).

    Methods
    -------
    __init__(self, size):
        Initializes the Square instance with a specific size.

    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of one side of the square.
        """
        self.__size = size
