#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result

    Args:
        a: Dividend
        b: Divisor

    Result:
        The quotient of a and b
        None if b is 0
    """
    try:
        q = a / b
    except ZeroDivisionError:
        q = None
    finally:
        print('Inside result: {}'.format(q))
        return q
