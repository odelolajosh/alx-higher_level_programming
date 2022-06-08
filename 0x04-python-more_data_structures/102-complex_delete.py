#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
        Deletes keys with a specific value in a dictionary.

        Args:
            a_dictionary: Given dictionary
            value: value to get rid of

        Return:
            Modified dictionary
    """
    keys = list(a_dictionary.keys())

    for key in keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]

    return a_dictionary
