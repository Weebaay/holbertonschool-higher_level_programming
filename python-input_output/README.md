# Python - Input/Output
## Description

This project is part of the Python learning curriculum at Holberton School. It focuses on working with file input and output (I/O) in Python. By the end of this project, students will understand how to read from and write to files, as well as how to serialize and deserialize data using JSON. These are essential skills for working with persistent data storage in Python applications.

## Requirements

    All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
    Python scripts are formatted with pycodestyle (version 2.7.*).
    All code files end with a new line.
    Executable permissions must be set on all Python scripts.
    The first line of each Python script must be #!/usr/bin/python3.

## Files and Tasks

The project is structured with multiple Python scripts that focus on file handling and JSON operations.

| Task # | Filename                     | Description                                                                                        |
|--------|-------------------------------|----------------------------------------------------------------------------------------------------|
| 0      | `0-read_file.py`              | A function that reads a text file (UTF8) and prints it to stdout.                                  |
| 1      | `1-write_file.py`             | A function that writes a string to a text file (UTF8) and returns the number of characters written. |
| 2      | `2-append_write.py`           | A function that appends a string at the end of a text file (UTF8) and returns the number of characters added. |
| 3      | `3-to_json_string.py`         | A function that returns the JSON representation of an object (string).                             |
| 4      | `4-from_json_string.py`       | A function that returns a Python object represented by a JSON string.                              |
| 5      | `5-save_to_json_file.py`      | A function that writes an Object to a text file using a JSON representation.                       |
| 6      | `6-load_from_json_file.py`    | A function that creates an Object from a JSON file.                                                |
| 7      | `7-add_item.py`               | A script that adds all arguments to a Python list and saves them to a file.                        |
| 8      | `8-class_to_json.py`          | A function that returns the dictionary description of a simple data structure for JSON serialization of an object. |
| 9      | `9-student.py`                | A class `Student` that defines a student by first name, last name, and age, with a method that returns the dictionary representation of the instance. |
| 10     | `10-student.py`               | A class `Student` (based on Task 9) with a method to retrieve a dictionary representation based on attributes. |
| 11     | `11-student.py`               | A class `Student` (based on Task 10) with methods to save and reload the instance from a JSON file. |


## Example

   **Example usage for Task 0:**
		read_file("my_file.txt")

   **Output:**
		This is the content of the file

## Usage

To execute any of the tasks, simply run the script as shown in the examples below:
	$ ./0-read_file.py

## Author

This project was completed as part of the Holberton School curriculum by **Jean-Paul Dijeont**.