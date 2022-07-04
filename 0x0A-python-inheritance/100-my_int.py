#!/usr/bin/python3
"""
100-my_int Module
"""


class MyInt(int):
    """A subclass of `int` object
    """

    def __eq__(self, other):
        """ make == comparison """
        return super().__eq__(other)

    def __ne__(self, other):
        """ make != comparison """
        return super().__ne__(other)
