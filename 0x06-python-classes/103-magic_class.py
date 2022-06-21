#!/usr/bin/python3
"""
Square Class Module
"""

import math


class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
