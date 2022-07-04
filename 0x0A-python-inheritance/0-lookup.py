#!/usr/bin/python3
"""
0-lookup Module
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj (object): object

    Return:
        list of available attributes and methods of an object
    """
    return dir(obj)
