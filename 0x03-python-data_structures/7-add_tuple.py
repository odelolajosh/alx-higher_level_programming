#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples

    Args:
        tuple_a: First tuple
        tuple_b: Second tuple

    Return:
        New tuple
    """

    if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0, )

    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0, )

    a1 = tuple_a[0]
    a2 = tuple_a[1]

    b1 = tuple_b[0]
    b2 = tuple_b[1]

    return (a1 + b1, a2 + b2)
