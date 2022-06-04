#!/usr/bin/python3
def no_c(my_string):
    clone = my_string[:]

    j = 0
    for i, ch in enumerate(clone):
        if ch == 'c' or ch == 'C':
            clone = clone[:i - j] + clone[i - j + 1:]
            j += 1
    return clone
