#!/usr/bin/python3
for tens in range(0, 9):
    for units in range(tens + 1, 10):
        if (tens == 8 and units == 9):
            print('{:d}{:d}'.format(tens, units))
        else:
            print('{:d}{:d},'.format(tens, units), end=' ')
