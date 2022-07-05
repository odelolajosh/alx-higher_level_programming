#!/usr/bin/python3
"""
1-write_file Module
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (string): name of text file
        text (string): text to write

    Return:
        (int): number of character written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
