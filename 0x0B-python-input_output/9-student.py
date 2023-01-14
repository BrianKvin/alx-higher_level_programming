#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student using public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A public method that retrives a dictionary representation of the Student"""
        return self.__dict__
