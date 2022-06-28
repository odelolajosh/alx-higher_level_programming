"""Locked Class:
    Attributes can't be dynamically created
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """Initializing LockedClass object
        """
        pass
