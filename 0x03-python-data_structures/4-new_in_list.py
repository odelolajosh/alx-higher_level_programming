#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    clone = my_list[:]

    if 0 <= idx < len(clone):
        clone[idx] = element

    return clone
