#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary: Given dictionary
        key: String key to delete

    Return:
        Modified dictionary
    """
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
