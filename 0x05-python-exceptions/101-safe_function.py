#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        sys.stderr.write("Exception: {}\n".format(err))
    finally:
        return result
