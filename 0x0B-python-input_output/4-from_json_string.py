#!/usr/bin/python3
"""This module defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    return json.loads(my_str)


"""
#!/usr/bin/python3


import json

def from_json_string(my_str):
    return json.loads(my_str)
"""
