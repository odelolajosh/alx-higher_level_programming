#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string: Given Roman numeral

    Return:
        integer equivalent
    """
    result = 0
    symbols = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    mapped = list(map(lambda x: symbols.get(x), roman_string))
    for i, m in enumerate(mapped):
        if i <= len(mapped) - 2 and m < mapped[i + 1]:
            result -= m
        else:
            result += m
    return result
