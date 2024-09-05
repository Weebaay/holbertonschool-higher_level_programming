# Python - Import & Modules
## Introduction

	This project introduces the concept of Python modules and how to import functions from one file to another.
	It also covers the usage of command-line arguments, the built-in dir() function, and how to prevent code in a script from
	being executed when it’s imported. The tasks involve writing Python programs that make use of modules, functions, and variables across different files.

## Requirements

	. Allowed editors: vi, vim, emacs
	. All files are interpreted/compiled on Ubuntu 22.04 LTS using python3 (version 3.10.*)
	. All files should end with a new line
	. The first line of all files should be exactly #!/usr/bin/python3
	. A README.md file, at the root of the project, is mandatory
	. Your code should follow the pycodestyle style (version 2.7.*)
	. All files must be executable
	. The length of your files will be tested using wc

## Project Structure

This project contains the following tasks:
0. Import a simple function from a simple file

		File: 0-add.py
		Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.

1. My first toolbox!

		File: 1-calculation.py
		Write a program that imports functions from the file calculator_1.py and performs addition, subtraction, multiplication, and division on the variables a = 10 and b = 5.

2. How to make a script dynamic!

		File: 2-args.py
		Write a program that prints the number of arguments and the list of its arguments.

3. Infinite addition

		File: 3-infinite_add.py
		Write a program that prints the result of the addition of all arguments passed on the command line.

4. Who are you?

		File: 4-hidden_discovery.py
		Write a program that prints all the names defined by the compiled module hidden_4.pyc, but only prints names that do not start with __.

5. Everything can be imported

		File: 5-variable_load.py
		Write a program that imports the variable a from the file variable_load_5.py and prints its value.

## Usage

Each Python script can be executed using the following command:

bash

	./<script_name>.py

Make sure the scripts are executable by running:

bash

	chmod +x <script_name>.py

Example for running the first task (0-add.py):

bash

	./0-add.py

## Resources

    Modules
    Command-line arguments
    Pycodestyle – Style Guide for Python Code

## Author

Jean-Paul Dijeont
