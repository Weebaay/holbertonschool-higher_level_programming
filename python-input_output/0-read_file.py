#!/usr/bin/python3
""" Module 0-read_file : Define read file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
