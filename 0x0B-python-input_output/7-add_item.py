#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
from os import path
from sys import argv


if __name__ == "__main__":
    load = __import__('6-load_from_json_file').load_from_json_file
    save = __import__('5-save_to_json_file').save_to_json_file

    _list = []

    if path.exists("add_item.json"):
        _list = load("add_item.json")

    _list.extend(argv[1:])
    save(_list, "add_item.json")
