#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    Args: file name - file to be appended to
           text (str) - string to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
