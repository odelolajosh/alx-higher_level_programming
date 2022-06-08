#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present precisely in only one set

    Args:
        set_1: Given first set
        set_2: Given second set

    Return:
        The result set
    """
    return set_1 ^ set_2
