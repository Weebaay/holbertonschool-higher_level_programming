# Python - Inheritance
## Description

This project focuses on understanding Inheritance in Python, an essential concept in Object-Oriented Programming (OOP). It introduces how to define relationships between classes, allowing you to inherit properties and methods from a parent (or base) class. Through a series of tasks, you will learn about superclass, subclass, multiple inheritance, method overriding, and built-in functions related to inheritance such as isinstance() and issubclass().

The goal is to solidify your understanding of how inheritance promotes code reusability and organization by enabling classes to build upon existing functionality.

## Requirements

    All Python files should be executable and end with a new line.
    Your code must be compiled/interpreted using Python 3 (version 3.8.5) on Ubuntu 20.04 LTS.
    Use the pycodestyle style guide (version 2.7.*).
    All test cases should be placed in the tests/ directory.
    Your test files must be .txt files and executable with the command: python3 -m doctest ./tests/*.
    Each class and function must include appropriate documentatio

## Files and Tasks

| Task # | Filename               | Description                                                                                      |
|-------:|------------------------|--------------------------------------------------------------------------------------------------|
| 0      | `0-lookup.py`           | Function `lookup` returns a list of available attributes and methods of an object.               |
| 1      | `1-my_list.py`          | Class `MyList` that inherits from `list`. It includes a method `print_sorted()` to print a sorted list. |
| 2      | `2-is_same_class.py`    | Function `is_same_class` returns `True` if the object is exactly an instance of the specified class. |
| 3      | `3-is_kind_of_class.py` | Function `is_kind_of_class` returns `True` if the object is an instance of, or inherits from, a specified class. |
| 4      | `4-inherits_from.py`    | Function `inherits_from` returns `True` if the object is an instance of a class that inherited from the specified class. |
| 5      | `5-base_geometry.py`    | Empty class `BaseGeometry`.                                                                     |
| 6      | `6-base_geometry.py`    | Class `BaseGeometry` with a public method `area()` that raises an exception if not implemented.  |
| 7      | `7-base_geometry.py`    | Class `BaseGeometry` with a method `integer_validator()` to validate that a value is an integer. |
| 8      | `8-rectangle.py`        | Class `Rectangle` that inherits from `BaseGeometry`, with private attributes `width` and `height`. |
| 9      | `9-rectangle.py`        | Class `Rectangle` with implemented `area()` method and a custom `__str__()` method.              |
| 10     | `10-square.py`          | Class `Square` that inherits from `Rectangle` and implements the `area()` method.               |
| 11     | `11-square.py`          | Class `Square` that inherits from `Rectangle`, with a custom `__str__()` method.                |


Usage

Each Python file corresponds to a specific task. To test the functionality of any file, you can create a Python script that imports the module and run it as shown in the example below.

**Example usage for Task 1**:

	#!/usr/bin/python3
	MyList = __import__('1-my_list').MyList

	my_list = MyList()
	my_list.append(1)
	my_list.append(4)
	my_list.append(2)
	my_list.append(3)
	my_list.append(5)
	print(my_list)
	my_list.print_sorted()

	$ ./1-main.py

	[1, 4, 2, 3, 5]
	[1, 2, 3, 4, 5]

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.