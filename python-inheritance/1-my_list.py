#!/usr/bin/python3
"""Module 1-my_list: Define Inherits from list
and adds print_sorted method """


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
