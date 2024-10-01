#!/usr/bin/python3
"""Module 1-write_file: Define Write to a file"""


def write_file(filename="", text=""):
    """writes a string to text file UTF8 and return the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
