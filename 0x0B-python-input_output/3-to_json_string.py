#!/usr/bin/python3
"""
3-to_json_string Module
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object

    Args:
        my_obj (string): given object

    Return:
        (string) json representation
    """
    return json.dumps(my_obj)
