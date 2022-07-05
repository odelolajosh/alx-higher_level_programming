#!/usr/bin/python3
"""
8-class_to_json Module
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object

    Args:
        obj (object): given object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
