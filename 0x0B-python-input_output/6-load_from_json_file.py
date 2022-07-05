#!/usr/bin/python3
"""
6-load_from_json_file Module
    Contains a function to create an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_obj (string): given json

    Return:
        (string) string representation
    """
    with open(filename, 'r', encoding="utf-8") as  f:
        return json.load(f)
