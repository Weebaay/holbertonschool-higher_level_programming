#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    temp = ""
    
    for char in text:
        temp += char
        if char in ".:?":
            print(temp.strip())
            print()
            temp = ""
    
    if temp:
        print(temp.strip())
