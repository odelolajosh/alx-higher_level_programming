#!/usr/bin/python3
def no_c(my_string):
    clone = my_string[:]

    for i, ch in enumerate(clone):
        if ch == 'c' or ch == 'C':
            clone = clone[:i] + clone[i + 1:]
    return clone;
