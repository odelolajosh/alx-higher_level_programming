#!/usr/bin/python3
"""
Magic Class Module
"""

import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius):
        """Initializes a Magic object"""
        self.__radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
