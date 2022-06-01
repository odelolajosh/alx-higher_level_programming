#!/usr/bin/python3
for n in range(122, 96, -1):
    asc = n if n % 2 == 0 else n - 32
    print("{:c}".format(asc), end='')
