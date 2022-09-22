#!/usr/bin/python3
"""2-is_same_class
"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of the specified class

    Args:
        obj: given object
        a_class: given class

    Return:
        return True is obj is exactly an instance of a_class else False
    """
    return type(obj) is a_class
