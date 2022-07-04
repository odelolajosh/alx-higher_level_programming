#!/usr/bin/python3
"""3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """checks if an obj is a kind of a class

    Args:
        obj: given object
        a_class: given class

    Return:
        True is obj is an instance of a_class else False
    """
    return isinstance(obj, a_class)
