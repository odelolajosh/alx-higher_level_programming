#!/usr/bin/python3
"""
9-student Module
    Contains a class declaration for a student
"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Instantiates a student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a `Student` instance """
        return self.__dict__.copy()
