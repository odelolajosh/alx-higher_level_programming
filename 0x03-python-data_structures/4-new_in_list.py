#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    clone = my_list[:]

    if idx >= 0 or idx < len(clone):
        clone[idx] = element

    return clone
