#!/usr/bin/python3
"""Module 1-my_list: Define Inherits from list
and adds print_sorted method """


class MyList(list):
    """class Mylist that inherit from list"""
    def print_sorted(self):
        """"that prints the list but sorted"""
        print(sorted(self))
