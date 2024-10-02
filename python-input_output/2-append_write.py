#!/usr/bin/python3
"""Module 2-append_write: Define append to a file"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file UTF8 and
    return the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
