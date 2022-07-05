#!/usr/bin/python3
"""
5-save_to_json_file Module
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): given object
        filename (string): write text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
