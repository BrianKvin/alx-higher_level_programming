#!/usr/bin/python3
"""A module that defines a Base class"""


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*
    Attributes: __nb_objects (int) - The number of instantiated Base.
    """
    """Private class attribute"""
    __nb_objects = 0

    """"class constructor"""
    def __init__(self, id=None):
        """Public instance attribute
        initiate a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
