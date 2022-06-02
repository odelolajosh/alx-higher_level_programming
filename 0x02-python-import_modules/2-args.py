#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv) - 1
    s = ':' if count > 0 else '.'
    print('{} arguments{}'.format(count, s))
    for i in range(1, count + 1):
        print('{}: {}'.format(i, sys.argv[i]))
