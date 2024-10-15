# Python - Abstract Classes and Interfaces

## Description

This project focuses on enhancing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through various exercises, you will explore abstract classes, interfaces, duck typing, multiple inheritance, mixins, and other key OOP principles. You will learn how to design, implement, and test Python programs using these OOP techniques.

## Learning Objectives

1. **Abstract Classes**  
   Understand and apply abstract classes to define common interfaces while enforcing certain levels of class abstraction.

2. **Interfaces and Duck Typing**  
   Grasp the concepts of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.

3. **Subclassing Standard Base Classes**  
   Learn to extend standard base classes like `list`, `dict`, and `iterator` to create custom data structures with specialized behaviors.

4. **Method Overriding**  
   Use method overriding to modify or enhance the behavior of base class methods.

5. **Multiple Inheritance**  
   Understand and apply multiple inheritance to form complex relationships between classes.

6. **Mixins**  
   Utilize mixins to compose behavior across unrelated classes.

## Resources

These resources are useful for better understanding the concepts covered:

- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - Python OOP Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- [sentdex - Python OOP Tutorials](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

## Project Tasks

### 0. Abstract Animal Class and its Subclasses

- Create an abstract class `Animal` with an abstract method `sound()`.
- Implement two subclasses: `Dog` and `Cat`, each overriding the `sound()` method to return "Bark" and "Meow" respectively.

### 1. Shapes, Interfaces, and Duck Typing

- Create an abstract class `Shape` with two abstract methods: `area()` and `perimeter()`.
- Implement two subclasses: `Circle` and `Rectangle`.
- Create a function `shape_info()` that uses duck typing to print the area and perimeter of any shape.

### 2. Extending the Python List with Notifications

- Create a class `VerboseList` that extends the `list` class and prints a message whenever an item is added or removed via methods like `append()`, `extend()`, `remove()`, and `pop()`.

### 3. CountedIterator - Keeping Track of Iteration

- Create a class `CountedIterator` that extends a standard Python iterator and tracks how many items have been iterated over.

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance

- Implement a class `FlyingFish` that inherits from both `Fish` and `Bird`. Override the `fly()`, `swim()`, and `habitat()` methods.

### 5. The Mystical Dragon - Mastering Mixins

- Create two mixins: `SwimMixin` and `FlyMixin`, each with methods `swim()` and `fly()`.
- Implement a class `Dragon` that inherits both mixins and adds extra behavior, such as a `roar()` method.

## Installation

1. Clone this GitHub repository:
   ```bash
   git clone https://github.com/Weebaay/holbertonschool-higher_level_programming.git

## Usage

To run the Python files, use the following command:
	./main_<task_number>.py

For example, to run the first task:
	./main_00_abc.py

## Author

This project was completed as part of the Holberton School curriculum by **Dijeont Jean-Paul**.