# Python - Test-driven Development
## Description

This project is part of the Python curriculum at Holberton School, focusing on Test-Driven Development (TDD) in Python. The goal is to understand the importance of tests, how to write them, and how to apply TDD methodology. This project emphasizes writing documentation and tests before implementing the actual code.
## Requirements

	.	All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
	.	Python scripts must be formatted with pycodestyle (version 2.7.*).
	.	All code files must end with a new line.
	.	Executable permissions must be set on all Python scripts.
	.	The first line of each Python script must be #!/usr/bin/python3.
	.	All your test files should be inside a folder tests.
	.	All test files should be executed by using this command: python3 -m doctest ./tests/*.

## Files and Tasks
| Task # | Filename                            | Description                                                                                         |
|--------|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| 0      | `0-add_integer.py`                  | A function that adds two integers. Test cases provided to ensure type validation and addition rules. |
| 1      | `2-matrix_divided.py`               | A function that divides all elements of a matrix. Each element is rounded to 2 decimal places.       |
| 2      | `3-say_my_name.py`                  | A function that prints "My name is <first name> <last name>" and validates the input types.          |
| 3      | `4-print_square.py`                 | A function that prints a square with the character `#`, with proper size validation.                 |
| 4      | `5-text_indentation.py`             | A function that prints text with two new lines after each of these characters: `.`, `?`, and `:`.    |
| 5      | `tests/6-max_integer_test.py`       | Unittests for the `max_integer` function, checking edge cases such as empty lists and negative values.|

## Example

**Example usage for Task 0**:
	add_integer(1, 2)
	# Output:
	# 3

**Example usage for Task 3**:
	print_square(4)
	# Output:
	####
	####
	####
	####

## Usage

To run the test cases for any function, simply execute the command below:
	$ python3 -m doctest ./tests/<test_file>.txt

## Author

This project was completed as part of the Holberton School curriculum by **Jean-Paul Dijeont**.