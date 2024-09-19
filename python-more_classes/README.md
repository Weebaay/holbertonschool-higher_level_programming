# Python - More Classes and Objects
## Description

This project focuses on deepening your understanding of Object-Oriented Programming (OOP) in Python. It follows the Python - Classes and Objects project and covers more advanced topics such as class and instance attributes, static and class methods, and destructors.

The objective is to familiarize you with key concepts like encapsulation, abstraction, special methods, and public and private attributes.

## Requirements
	.Class and instance attributes
	.Static and class methods
	.Encapsulation and abstraction
	.Properties and accessors (getters and setters)
	.Special methods __str__, __repr__, and __del__
	.Managing instances and object counting

## Files and Tasks

| Task # | Filename           | Description                                                                                             |
|--------|--------------------|---------------------------------------------------------------------------------------------------------|
| 0      | `0-rectangle.py`   | Defines an empty class `Rectangle`.                                                                    |
| 1      | `1-rectangle.py`   | Defines a class `Rectangle` with private attributes `width` and `height`.                               |
| 2      | `2-rectangle.py`   | Adds size validation for the `Rectangle` class to ensure `width` and `height` are positive integers.    |
| 3      | `3-rectangle.py`   | Adds methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.               |
| 4      | `4-rectangle.py`   | Implements the `__str__` method to print the rectangle using the `#` character.                        |
| 5      | `5-rectangle.py`   | Implements the `__repr__` method to provide a string representation of the rectangle object.            |
| 6      | `6-rectangle.py`   | Implements the `__del__` method to show a message when an instance is deleted.                         |
| 7      | `7-rectangle.py`   | Adds a class attribute `number_of_instances` to track the number of `Rectangle` instances.              |
| 8      | `8-rectangle.py`   | Introduces a static method `bigger_or_equal` to compare the areas of two rectangles.                    |

## Example

**Example usage for Task 3:**

	#!/usr/bin/python3
	Rectangle = __import__('3-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

	# Output:
	# Area: 8 - Perimeter: 12

## Usage
**To execute any of the tasks, simply run the script as shown in the examples below:**

	$ ./0-main.py

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul.**