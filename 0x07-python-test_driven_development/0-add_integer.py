#!/usr/bin/python3
"""Integer Addition
contains a function for adding integers
"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the given numbers
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
