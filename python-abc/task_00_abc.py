#!/usr/bin/python3
"""Module task_00abc: Define abstract animal class and its subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """create an abstract class named animal using the ABC package"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """subclasses of animal named Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclassesof animal named Cat"""

    def sound(self):
        return "Meow"
