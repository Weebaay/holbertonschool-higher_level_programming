# Python - Everything is Object

## Description

This project dives into Python's object model and its unique handling of variables, references, mutable and immutable types. The aim is to develop a deeper understanding of Python's object behavior to write efficient and bug-free code. 

Key questions addressed in this project include:
- How does Python manage object references?
- What are mutable and immutable types, and why do they matter?
- How does variable aliasing affect program behavior?
- What happens when variables are passed to functions?

By working through these exercises, you will build a solid foundation in Python's object management.

---

## Background Context

In Python:
- **Everything is an object**, whether it's a primitive type like `int` or complex data structures like lists.
- Mutable and immutable objects behave differently when assigned, passed, or modified.

### Example: Mutable vs Immutable
```python
# Immutable type example (int)
a = 1
b = a
a = 2
print(b)  # Output: 1

# Mutable type example (list)
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # Output: ['x', 2, 3]
```

# Learning Objectives

By the end of this project, you will be able to:

- Define what an object is.
- Differentiate between a class, an object, and an instance.
- Explain mutable vs immutable objects.
- Understand references, assignments, and aliases.
- Identify whether two variables point to the same object.
- Retrieve a variable's identifier (memory address).
- List Python's built-in mutable and immutable types.
- Describe how Python passes variables to functions and the implications for different types.

---

# Requirements

## Python Scripts

- Files must be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
- The first line of every file should be:
  ```python
  #!/usr/bin/python3

- Use the pycodestyle (version 2.7.*) coding standard.
- All scripts should be executable and end with a new line.

.txt **Answer Files**

- Answers must be single-line entries.
- No shebang (#!/usr/bin/python3) in answer files.
- All files should end with a new line.

# Tasks Overview

| Task # | Description                                                                   | File Name                |
|--------|-------------------------------------------------------------------------------|--------------------------|
| 0      | Write the function name to print an object's type.                            | `0-answer.txt`           |
| 1      | Write the function name to get a variable's identifier.                       | `1-answer.txt`           |
| 2      | Determine if two variables point to the same object after assignment.         | `2-answer.txt`           |
| 3      | Analyze object behavior when assigning one variable to another.               | `3-answer.txt`           |
| 4      | Verify the behavior of identical integers.                                    | `4-answer.txt`           |
| 5      | Determine if the IDs of variables pointing to the same object remain the same.| `5-answer.txt`           |
| 6      | Compare string objects using `==` and `is`.                                   | `6-answer.txt`           |
| 7      | Assess string comparison outcomes with different memory allocations.          | `7-answer.txt`           |
| 8      | Evaluate string aliasing and ID consistency after operations.                 | `8-answer.txt`           |
| 9      | Evaluate string aliasing and ID consistency after operations (continued).     | `9-answer.txt`           |
| 10     | Compare lists using `==` and `is`.                                            | `10-answer.txt`          |
| 11     | Compare lists using `==` and `is` (continued).                                | `11-answer.txt`          |
| 12     | Compare lists using `==` and `is` (continued).                                | `12-answer.txt`          |
| 13     | Compare lists using `==` and `is` (continued).                                | `13-answer.txt`          |
| 14     | Analyze list behavior under appending operation.                              | `14-answer.txt`          |
| 15     | Analyze list behavior under copying operation.                                | `15-answer.txt`          |
| 16     | Analyze list behavior under assigning operation.                              | `16-answer.txt`          |
| 17     | Analyze list behavior under slicing operation.                                | `17-answer.txt`          |
| 18     | Analyze list behavior under more complex operations.                          | `18-answer.txt`          |
| 19     | Write a function to return a copy of a list.                                  | `19-copy_list.py`        |
| 20     | Evaluate tuple comparison using `==` and `is`.                                | `20-answer.txt`          |
| 21     | Evaluate tuple behavior under assignment.                                     | `21-answer.txt`          |
| 22     | Evaluate tuple behavior under slicing.                                        | `22-answer.txt`          |
| 23     | Evaluate tuple behavior under concatenation.                                  | `23-answer.txt`          |
| 24     | Evaluate tuple behavior with nested objects.                                  | `24-answer.txt`          |
| 25     | Analyze tuple mutability with mutable elements.                               | `25-answer.txt`          |
| 26     | Analyze tuple immutability with immutable elements.                           | `26-answer.txt`          |
| 27     | Analyze memory behavior for an empty tuple.                                   | `27-answer.txt`          |
| 28     | Examine ID behavior for re-used immutable objects like numbers.               | `28-answer.txt`          |
| 29     | Write a blog post summarizing the project’s key learnings.                    | Blog Post URLs           |

## Author 
**Jean-Paul dijeont** Project developed as part of the Holberton School Curriculum.