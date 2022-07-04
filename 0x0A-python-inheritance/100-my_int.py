#!/usr/bin/python3
"""
100-my_int Module
"""


class MyInt(int):
    """A subclass of `int` object
    """

    def __eq__(self, __x):
        """ make == comparison """
        return super().__eq__(__x)

    def __ne__(self, __x):
        """ make != comparison """
        return super().__ne__(__x)
