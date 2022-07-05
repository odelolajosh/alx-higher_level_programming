#!/usr/bin/python3
"""
0-read_file Module
"""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdout

    Args:
        filename (string): name of text file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
