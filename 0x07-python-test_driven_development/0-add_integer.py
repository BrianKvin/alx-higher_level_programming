#!/usr/bin/python3
#  module to add two integers


def add_integer(a, b=98):
    """
    Function that adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        sum of int (a and b)
    Raise:
        TypeError if a and b are not integers
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
