#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    Assume all values are only integers

    Args:
        a_dictionary: Given dictionary

    Return:
        A key with the biggest integer value.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary.keys(), key=a_dictionary.get)
