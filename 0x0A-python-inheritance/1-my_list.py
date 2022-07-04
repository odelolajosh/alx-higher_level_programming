#!/usr/bin/python3
"""
1-mylist Module
"""


class MyList(list):
    """A subclass of `list` object
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
