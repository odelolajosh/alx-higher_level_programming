#!/usr/bin/python3
"""
101-add_attribute Module
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible

    Args:
        obj (object): given object
        name (string): attribute name
        value (Any): attribute value

    Raises:
        TypeError: if new attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
