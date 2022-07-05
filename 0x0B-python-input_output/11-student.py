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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a `Student` instance

            Args:
                attrs (list): a list of string, attributes names to be filtered

            Return:
                (dict): dictionary representation of `Student` instance
        """
        json = self.__dict__.copy()
        if attrs is None or not all([type(attr) is str for attr in attrs]):
            return json

        _json = {}
        for attr in attrs:
            if attr in json:
                _json[attr] = json[attr]

        return _json

    def reload_from_json(self, json):
        """replaces all attributes of the student instance

        Args:
            json (dict): attribute replacement
        """
        for key, value in json.items():
            self.__dict__[key] = value
