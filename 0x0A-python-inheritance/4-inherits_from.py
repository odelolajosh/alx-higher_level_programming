#!/usr/bin/python3
"""
4-inherits_from Module
"""


def inherits_from(obj, a_class):
    """checks if an obj is a inherited from a class

    Args:
        obj: given object
        a_class: given class

    Return:
        True is obj is an instance of a_class else False
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
