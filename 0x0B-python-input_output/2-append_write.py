#!/usr/bin/python3
"""
2-append_write Module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
        filename (string): name of text file
        text (string): text to write

    Return:
        (int): number of character added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
