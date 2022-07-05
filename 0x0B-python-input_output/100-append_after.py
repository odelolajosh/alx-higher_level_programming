#!/usr/bin/python3
"""
100-append_after Module
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename (string): name of file
        search_string (string): search substring
        new_string: append line
    """
    with open(filename, "r+", encoding="utf-8") as f:
        res = []
        for line in f:
            res.append(line)
            if line.rfind(search_string) != -1:
                res.append(new_string)
        f.seek(0)
        f.write("".join(res))
