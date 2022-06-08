#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: Given dictionary
        key: Argument will be always a string
        value: Argument will be any type

    Return:
        Modified dictionary
    """
    a_dictionary[key] = value
    return (a_dictionary)
