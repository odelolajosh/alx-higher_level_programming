#!/usr/bin/python3
"""
4-from_json_string Module
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_obj (string): given json

    Return:
        (string) string representation
    """
    return json.loads(my_str)
