#!/usr/bin/python3
"""Module 6-square: Define position attribute and enhance my_print method"""


class Square:
    """ A class define square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given size and position.

        Args:
            size (int): The size of the square (must be >= 0).
            position (tuple): The position where the square will be printed.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The new position for the square
            (a tuple of 2 positive integers).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#',
        taking into account its position.
        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
