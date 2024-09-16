# Python - Classes and Objects
## Description

This project is part of the Python curriculum at Holberton School, focusing on Object-Oriented Programming (OOP) concepts in Python. It introduces the principles of classes, objects, attributes, and methods, emphasizing the importance of data encapsulation, abstraction, and information hiding. By the end of this project, students will have a solid understanding of how to define and interact with Python classes and apply OOP best practices.
## Requirements

	. All files are interpreted/compiled on Ubuntu 20.04LTS using python3 (version 3.8.5).
	. Python scripts must be formatted with pycodestyle (version 2.7.*).
	. All code files must end with a new line.
	. Executable permissions must be set on all Python scripts.
	. The first line of each Python script must be #!/usr/bin/python3.

## Files and Tasks
## Files and Tasks

| Task # | Filename                   | Description                                                                                           |
|--------|----------------------------|-------------------------------------------------------------------------------------------------------|
| 0      | `0-square.py`              | Defines an empty class `Square`.                                                                      |
| 1      | `1-square.py`              | Defines a class `Square` with a private instance attribute `size`.                                     |
| 2      | `2-square.py`              | Adds size validation to the `Square` class, ensuring it is an integer and non-negative.               |
| 3      | `3-square.py`              | Adds a method `area` to calculate the area of the square.                                             |
| 4      | `4-square.py`              | Introduces getter and setter for the private attribute `size`, ensuring encapsulation.                |
| 5      | `5-square.py`              | Adds a method `my_print` to print the square using the `#` character.                                 |
| 6      | `6-square.py`              | Introduces `position` attribute, allowing the square to be printed at a specified offset.             |

## Example

**Example usage for Task 3**:

	Square = __import__('3-square').Square

	my_square = Square(3)
	print("Area: {}".format(my_square.area()))

	# Output:
	# Area: 9

## Usage

**To execute any of the tasks, simply run the script as shown in the examples below**:
	$ ./0-main.py

## Author

This project was completed as part of the Holberton School curriculum by **Jean-Paul Dijeont**.
