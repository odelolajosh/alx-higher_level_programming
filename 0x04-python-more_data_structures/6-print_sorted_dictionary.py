#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys

    Args:
        a_dictionary: Given dictionary
    """
    keys = list(a_dictionary.keys())
    for key in sorted(keys):
        print(f"{key}: {a_dictionary[key]}")
