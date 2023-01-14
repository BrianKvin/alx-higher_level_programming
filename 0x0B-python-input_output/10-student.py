#!/usr/bin/python3


"""A class student that defines a student based on 9-student.py"""
class Student:
    def __init__(self first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance
        Args: attrs (list) - optional list of attribute name
        if attrs is a list of strings, 
        represents only thise attrs included in the list
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
