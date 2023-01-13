#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__


"""
#!/usr/bin/python3


def class_to_json(obj):
    return obj.__dict__
"""
