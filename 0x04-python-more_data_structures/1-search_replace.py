#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list

    Args:
        my_list: given list
        search: elements to replace in the list
        replace: the new element

    Return:
        new list
    """
    return [replace if m is search else m for m in my_list]
