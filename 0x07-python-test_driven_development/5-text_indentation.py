#!/usr/bin/python3
"""
Module that contains function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines after specific characters

    Args:
        text: (str) text to print

    Return: nothing

    Raises: TypeError if `text` is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = text.replace(".", ".\n\n")
    buf = buf.replace("?", "?\n\n")
    buf = buf.replace(":", ":\n\n")
    new_line = buf.split("\n")
    for line in range(len(new_line)):
        print("{}".format(new_line[line].strip()),
              end=("" if (line == len(new_line) - 1) else "\n"))
